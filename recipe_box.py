#!/usr/bin/env python

""" Scrape a recipe, convert it to Markdown and store it in a Zettelkasten.

    A free recipe-box.

    1. https://obsidian.md/
    2. https://www.ourstate.com/a-kitchens-riches/
"""
import argparse
import json
import os
import sys

try:
    import httpx
    url_getter = httpx.Client(http2=True)
except ImportError:
    import requests
    url_getter = requests

from recipe_scrapers import scrape_me, WebsiteNotImplementedError, SCRAPERS


ROOT = '~/.config/recipe_box/'


def ensure_directory_exists(path, expand_user=True, file=False):
    """ Create a directory if it doesn't exists.

        Expanding '~' to the user's home directory on POSIX systems.
    """
    if expand_user:
        path = os.path.expanduser(path)

    if file:
        directory = os.path.dirname(path)
    else:
        directory = path

    if not os.path.exists(directory) and directory:
        try:
            os.makedirs(directory)
        except OSError as e:
            # A parallel process created the directory after the existence check.
            pass

    return path


def valid_filename(directory, filename=None, ascii=False):
    """ Return a valid "new" filename in a directory, given a filename/directory=path to test.

        Deal with duplicate filenames.
    """
    def test_filename(filename, count):
        """ Filename to test for existence.
        """
        fn, ext = os.path.splitext(filename)
        return fn + '({})'.format(count) + ext

    return_path = filename is None

    # Directory is a path.
    if filename is None:
        filename = os.path.basename(directory)
        directory = os.path.dirname(directory)

    # if ascii:
    #     filename = unidecode(unicode(filename))
    #     filename = ' '.join(filename.splitlines()).strip()
    #     filename = filename.decode('ascii', 'ignore')

    # Allow for directories.
    items = set(os.listdir(directory))
    if filename in items:
        count = 1
        while test_filename(filename, count) in items:
            count += 1
        if return_path:
            return os.path.join(directory, test_filename(filename, count))
        return test_filename(filename, count)
    else:
        if return_path:
            return os.path.join(directory, filename)
        return filename


def process_recipe(config, scraper, url, verbose=False):
    """ Process the recipe at a given URL.
    """
    recipe_box = ensure_directory_exists(config['recipe_box'])
    media = ensure_directory_exists(os.path.join(config['recipe_box'], 'media'))

    prefix = scraper.title().lower()
    path = os.path.join(recipe_box, prefix + '.md')
    path = valid_filename(path)
    recipe = open(path, 'w')

    try:
        image_url = scraper.image()
        response = url_getter.get(image_url)
    except:
        filename = None
    else:
        # Not sure about image urls without filename extensions, might need python-magic.
        # Also, os.path.splitext(url), probably not a good idea. ;)
        filename = os.path.splitext(os.path.basename(path))[0] + os.path.splitext(scraper.image())[1]
        filepath = os.path.join(media, filename)
        image = open(filepath, 'wb')
        image.write(response.content)
        image.close()
        if verbose:
            print('Saving {url} -> {path}'.format(url=image_url, path=filepath))

    recipe.write('# {title}\n'.format(title=scraper.title()))
    if filename:
        recipe.write('![[{filename}]]\n'.format(filename=filename))
    recipe.write('\n')
    # This is a placeholder for the user's own notes about the recipe.
    recipe.write('## Notes\n')
    recipe.write('\n')
    recipe.write('## Metadata\n')
    recipe.write('Yields: {yields}\n'.format(yields=scraper.yields()))
    recipe.write('Total Time: {total_time}\n'.format(total_time=scraper.total_time()))
    recipe.write('\n')
    recipe.write('## Ingredients\n')
    for ingredient in scraper.ingredients():
        recipe.write('* {ingredient}\n'.format(ingredient=ingredient))

    recipe.write('\n')
    recipe.write('## Instructions\n')
    for instruction in scraper.instructions().split('\n'):
        instruction = instruction.strip()
        if instruction:
            if instruction[0].isdigit():
                recipe.write('{instruction}\n'.format(instruction=instruction))
            else:
                recipe.write('1. {instruction}\n'.format(instruction=instruction))

    recipe.write('\n')
    recipe.write('[{url}]({url})\n'.format(url=url))
    recipe.close()
    # if verbose:
    print('Saving {url} -> {path}'.format(url=url, path=path))


def main():
    """ Console script entry point.
    """
    parser = argparse.ArgumentParser()
    parser.add_argument('url', metavar='URL', type=str, nargs='*', default='', help='recipe url')
    parser.add_argument('-l', dest='list', action='store_true', default=False, help='list all available sites')
    parser.add_argument('-w', dest='wild_mode', action='store_true', default=False, help="try scraping 'unknown' site using wild-mode (some editing of the recipe might be required)")
    parser.add_argument('-v', dest='verbose', action='store_true', default=False, help='verbose output')
    args = parser.parse_args()

    if args.list:
        for host in sorted(SCRAPERS):
            print(host)
        sys.exit()

    wild_mode = args.wild_mode
    verbose = args.verbose

    config_path = ensure_directory_exists(os.path.join(ROOT, 'recipe_box.json'), file=True)
    if not os.path.exists(config_path):
        config = {'recipe_box': '~/recipe_box/'}
        with open(config_path, 'w') as f:
            json.dump(config, f, indent=4)
    else:
        with open(config_path, 'r') as f:
            config = json.load(f)

    for url in args.url:
        if url:
            try:
                scraper = scrape_me(url, wild_mode=wild_mode)
            except WebsiteNotImplementedError:
                print('No scraper defined for {url}'.format(url=url))
                print('Try using the -w [wild-mode] option, your mileage may vary.')
                print('')
                print('It is recommended you add it to recipe-scrapers site, that way everybody gains from the effort.')
                print('https://github.com/hhursev/recipe-scrapers#if-you-want-a-scraper-for-a-new-site-added')
                print('')
                print('Once someone has added the new scraper:')
                print('pip install --upgrade recipe-scrapers')
            else:
                process_recipe(config, scraper, url, verbose)


if __name__ == '__main__':
    main()

