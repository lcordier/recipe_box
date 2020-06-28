from setuptools import setup

"""
    python3 setup.py sdist bdist_wheel
    python3 -m twine upload dist/*

    https://packaging.python.org/tutorials/packaging-projects/
"""

def readme():
    with open('README.md') as f:
        return f.read()


setup(
    name='recipe_box',
    version='0.1.2',
    py_modules=['recipe_box'],
    description='Utility to scrape recipes and put it in a local Zettelkasten.',
    long_description=readme(),
    long_description_content_type='text/markdown',
    # https://pypi.org/classifiers/
    classifiers=[
        'Development Status :: 4 - Beta',
        'Environment :: Console',
        'Intended Audience :: End Users/Desktop',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Topic :: Utilities',
    ],
    keywords='utility recipe scraper zettelkasten',
    url='http://github.com/lcordier/recipe_box/',
    author='Louis Cordier',
    author_email='lcordier@gmail.com',
    license='MIT',
    install_requires=[
        'recipe-scrapers',
    ],
    entry_points={
        'console_scripts': [
            'recipe_box=recipe_box:main',
        ],
    },
)
