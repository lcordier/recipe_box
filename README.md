# Recipe Box

![Recipe Box](recipe_box.jpg)

This program takes a recipe URL, scrapes the recipe website, converts it to [Markdown](https://daringfireball.net/projects/markdown/syntax)
format and store it in your local [Zettelkasten](https://www.youtube.com/watch?v=XUltI4v_UU4).
I use the free [Obsidian](https://obsidian.md/) Zettelkasten software and re-purpose it as a electronic recipe box.

The user can edit the recipe, fix errors, make notes, rate it, add #tags and [[backlinks]] to organise his/her collection.

A recipe box can be a [treasure chest](https://www.ourstate.com/a-kitchens-riches/), but you have to put in some effort.

The idea is not to have the biggest collection of recipes, but to have the most valuable one. The one with the recipes you've
personally tested and most of your family love.

Since the recipes are stored in simple plain text files it is easy to share with your friends and family, or pass down to the
next generation years from now.

> In our age when cloud services can shut down, get bought, or change privacy policy any day, the last thing you want is proprietary formats and data lock-in.
>
> With Obsidian, your data sits in a local folder. Never leave your life's work held hostage in the cloud again.
>
> Plain text Markdown also gives you the unparalleled interoperability to use any kind of sync, encryption, or data processing that works with plain text files.

You could still backup your recipe collection to a private GitHub repository. You could also convert the Markdown files into a
PDF and print a physical book as a personalised gift. You'll need those #tags and [[backlinks]] to organise it thou.

## Installation

1. `pip install recipe-box`

2. Install [Obsidian](https://obsidian.md/) to view the pretty recipes ;)

## How To Use

First run `recipe_box` without parameters to create the config file, $HOME/.config/recipe_box/recipe_box.json

```
{
    "recipe_box": "~/recipe_box/"
}
```

Here you can customize the name and location of your recipe box.

Then you are ready to download recipes. Search one of the supported sites for a recipe you like, copy the URL.

```
$ recipe_box https://www.bbc.co.uk/food/recipes/better_for_you_chocolate_83771
```

Open Obsidian, open vault and point it to your recipe_box.

## Supported Recipe Sites

These sites are scraped by the excellent [recipe-scrapers](https://github.com/hhursev/recipe-scrapers) library.
To add a new [recipe site](https://github.com/hhursev/recipe-scrapers#if-you-want-a-scraper-for-a-new-site-added).

* [101cookbooks.com](https://101cookbooks.com/)
* [allrecipes.com](https://allrecipes.com/)
* [archanaskitchen.com](https://archanaskitchen.com/)
* [bbc.co.uk](https://bbc.co.uk/)
* [bbc.com](https://bbc.com/)
* [bbcgoodfood.com](https://bbcgoodfood.com/)
* [bettycrocker.com](https://bettycrocker.com/)
* [bonappetit.com](https://bonappetit.com/)
* [budgetbytes.com](https://budgetbytes.com/)
* [closetcooking.com](https://closetcooking.com/)
* [cookieandkate.com](https://cookieandkate.com/)
* [cooking.nytimes.com](https://cooking.nytimes.com/)
* [cookpad.com](https://cookpad.com/)
* [cookstr.com](https://cookstr.com/)
* [copykat.com](https://copykat.com/)
* [countryliving.com](https://countryliving.com/)
* [cybercook.com.br](https://cybercook.com.br/)
* [delish.com](https://delish.com/)
* [en.wikibooks.org](https://en.wikibooks.org/)
* [epicurious.com](https://epicurious.com/)
* [finedininglovers.com](https://finedininglovers.com/)
* [fitmencook.com](https://fitmencook.com/)
* [food.com](https://food.com/)
* [foodnetwork.com](https://foodnetwork.com/)
* [foodrepublic.com](https://foodrepublic.com/)
* [geniuskitchen.com](https://geniuskitchen.com/)
* [gonnawantseconds.com](https://gonnawantseconds.com/)
* [gousto.co.uk](https://gousto.co.uk/)
* [greatbritishchefs.com](https://greatbritishchefs.com/)
* [healthyeating.nhlbi.nih.gov](https://healthyeating.nhlbi.nih.gov/)
* [heinzbrasil.com.br](https://heinzbrasil.com.br/)
* [hellofresh.co.uk](https://hellofresh.co.uk/)
* [hellofresh.com](https://hellofresh.com/)
* [inspiralized.com](https://inspiralized.com/)
* [jamieoliver.com](https://jamieoliver.com/)
* [justbento.com](https://justbento.com/)
* [marmiton.org](https://marmiton.org/)
* [matprat.no](https://matprat.no/)
* [mindmegette.hu](https://mindmegette.hu/)
* [misya.info](https://misya.info/)
* [momswithcrockpots.com](https://momswithcrockpots.com/)
* [motherthyme.com](https://motherthyme.com/)
* [mybakingaddiction.com](https://mybakingaddiction.com/)
* [myrecipes.com](https://myrecipes.com/)
* [ohsheglows.com](https://ohsheglows.com/)
* [panelinha.com.br](https://panelinha.com.br/)
* [paninihappy.com](https://paninihappy.com/)
* [przepisy.pl](https://przepisy.pl/)
* [realsimple.com](https://realsimple.com/)
* [receitas.ig.com.br](https://receitas.ig.com.br/)
* [ricette.giallozafferano.it](https://ricette.giallozafferano.it/)
* [seriouseats.com](https://seriouseats.com/)
* [simplyquinoa.com](https://simplyquinoa.com/)
* [simplyrecipes.com](https://simplyrecipes.com/)
* [southernliving.com](https://southernliving.com/)
* [steamykitchen.com](https://steamykitchen.com/)
* [tastesoflizzyt.com](https://tastesoflizzyt.com/)
* [tastykitchen.com](https://tastykitchen.com/)
* [thehappyfoodie.co.uk](https://thehappyfoodie.co.uk/)
* [thekitchn.com](https://thekitchn.com/)
* [thepioneerwoman.com](https://thepioneerwoman.com/)
* [thespruceeats.com](https://thespruceeats.com/)
* [thevintagemixer.com](https://thevintagemixer.com/)
* [tine.no](https://tine.no/)
* [tudogostoso.com.br](https://tudogostoso.com.br/)
* [twopeasandtheirpod.com](https://twopeasandtheirpod.com/)
* [vegolosi.it](https://vegolosi.it/)
* [whatsgabycooking.com](https://whatsgabycooking.com/)
* [yummly.com](https://yummly.com/)
