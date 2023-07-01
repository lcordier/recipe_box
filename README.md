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

* [claudia.abril.com.br](https://claudia.abril.com.br/)
* [www.acouplecooks.com](https://www.acouplecooks.com)
* [www.afghankitchenrecipes.com](http://www.afghankitchenrecipes.com/)
* [akispetretzikis.com](https://akispetretzikis.com/)
* [ah.nl](https://ah.nl/)
* [allrecipes.com](https://allrecipes.com/)
* [alltommat.se](https://alltommat.se/)
* [altonbrown.com](https://altonbrown.com/)
* [amazingribs.com](https://amazingribs.com/)
* [ambitiouskitchen.com](https://ambitiouskitchen.com/)
* [archanaskitchen.com](https://archanaskitchen.com/)
* [www.arla.se](https://www.arla.se/)
* [www.atelierdeschefs.fr](https://www.atelierdeschefs.fr/)
* [averiecooks.com](https://averiecooks.com/)
* [baking-sense.com](https://baking-sense.com/)
* [bakingmischief.com](https://bakingmischief.com/)
* [bbc.com](https://bbc.com/)
* [bbc.co.uk](https://bbc.co.uk/)
* [bbcgoodfood.com](https://bbcgoodfood.com/)
* [bettybossi.ch](https://bettybossi.ch/)
* [bettycrocker.com](https://bettycrocker.com/)
* [biancazapatka.com](https://biancazapatka.com/)
* [bigoven.com](https://bigoven.com/)
* [blueapron.com](https://blueapron.com/)
* [bonappetit.com](https://bonappetit.com/)
* [www.bodybuilding.com](https://www.bodybuilding.com/)
* [bowlofdelicious.com](https://bowlofdelicious.com/)
* [briceletbaklava.ch](https://briceletbaklava.ch/)
* [budgetbytes.com](https://budgetbytes.com/)
* [castironketo.net](https://castironketo.net/)
* [cdkitchen.com](https://cdkitchen.com/)
* [chefkoch.de](https://chefkoch.de/)
* [www.chefnini.com](https://www.chefnini.com/)
* [closetcooking.com](https://closetcooking.com/)
* [comidinhasdochef.com](https://comidinhasdochef.com/)
* [cookeatshare.com](https://cookeatshare.com/)
* [cookieandkate.com](https://cookieandkate.com/)
* [cookingcircle.com](https://cookingcircle.com/)
* [cookinglight.com](https://cookinglight.com/)
* [cookpad.com](https://cookpad.com/)
* [cookstr.com](https://cookstr.com/)
* [www.coop.se](https://www.coop.se/)
* [copykat.com](https://copykat.com/)
* [countryliving.com](https://countryliving.com/)
* [creativecanning.com](https://creativecanning.com/)
* [cucchiaio.it](https://cucchiaio.it/)
* [cuisineaz.com](https://cuisineaz.com/)
* [cybercook.com.br](https://cybercook.com.br/)
* [www.davidlebovitz.com](https://www.davidlebovitz.com/)
* [delish.com](https://delish.com/)
* [www.ditchthecarbs.com](https://www.ditchthecarbs.com/)
* [domesticate-me.com](https://domesticate-me.com/)
* [downshiftology.com](https://downshiftology.com/)
* [www.dr.dk](https://www.dr.dk/)
* [www.eatingbirdfood.com](https://www.eatingbirdfood.com/)
* [www.eatingwell.com](https://www.eatingwell.com/)
* [eatsmarter.com](https://eatsmarter.com/)
* [eatsmarter.de](https://eatsmarter.de/)
* [eatwhattonight.com](https://eatwhattonight.com/)
* [emmikochteinfach.de](https://emmikochteinfach.de/)
* [ethanchlebowski.com](https://ethanchlebowski.com/)
* [epicurious.com](https://epicurious.com/)
* [recipes.farmhousedelivery.com](https://recipes.farmhousedelivery.com/)
* [fifteenspatulas.com](https://fifteenspatulas.com/)
* [finedininglovers.com](https://finedininglovers.com/)
* [fitmencook.com](https://fitmencook.com/)
* [food.com](https://food.com/)
* [food52.com](https://food52.com/)
* [foodandwine.com](https://foodandwine.com/)
* [foodnetwork.com](https://foodnetwork.com/)
* [foodrepublic.com](https://foodrepublic.com/)
* [www.forksoverknives.com](https://www.forksoverknives.com/)
* [forktospoon.com](https://forktospoon.com/)
* [fredriksfika.allas.se](https://fredriksfika.allas.se/)
* [www.750g.com](https://www.750g.com)
* [geniuskitchen.com](https://geniuskitchen.com/)
* [www.gesund-aktiv.com](https://www.gesund-aktiv.com/)
* [giallozafferano.it](https://giallozafferano.it/)
* [gimmesomeoven.com](https://gimmesomeoven.com/)
* [godt.no](https://godt.no/)
* [goodfooddiscoveries.com](https://goodfooddiscoveries.com/)
* [recietas.globo.com](https://recietas.globo.com/)
* [gonnawantseconds.com](https://gonnawantseconds.com/)
* [gousto.co.uk](https://gousto.co.uk/)
* [greatbritishchefs.com](https://greatbritishchefs.com/)
* [halfbakedharvest.com](https://halfbakedharvest.com/)
* [handletheheat.com](https://handletheheat.com/)
* [www.hassanchef.com](https://www.hassanchef.com/)
* [headbangerskitchen.com](https://headbangerskitchen.com/)
* [www.heb.com](https://www.heb.com/)
* [heinzbrasil.com.br](https://heinzbrasil.com.br/)
* [hellofresh.com](https://hellofresh.com/)
* [hellofresh.co.uk](https://hellofresh.co.uk/)
* [www.hellofresh.de](https://www.hellofresh.de/)
* [www.hellofresh.fr](https://www.hellofresh.fr/)
* [www.hellofresh.nl](https://www.hellofresh.nl/)
* [www.hellofresh.ie](https://www.hellofresh.ie/)
* [www.homechef.com](https://www.homechef.com/)
* [hostthetoast.com](https://hostthetoast.com/)
* [www.ica.se](https://www.ica.se/)
* [receitas.ig.com.br](https://receitas.ig.com.br/)
* [www.im-worthy.com](https://www.im-worthy.com/)
* [indianhealthyrecipes.com](https://indianhealthyrecipes.com)
* [www.innit.com](https://www.innit.com/)
* [inspiralized.com](https://inspiralized.com/)
* [jamieoliver.com](https://jamieoliver.com/)
* [jimcooksfoodgood.com](https://jimcooksfoodgood.com/)
* [joyfoodsunshine.com](https://joyfoodsunshine.com/)
* [justataste.com](https://justataste.com/)
* [justbento.com](https://justbento.com/)
* [www.justonecookbook.com](https://www.justonecookbook.com/)
* [kennymcgovern.com](https://kennymcgovern.com/)
* [www.kingarthurbaking.com](https://www.kingarthurbaking.com)
* [www.kitchenstories.com](https://www.kitchenstories.com/)
* [kochbar.de](https://kochbar.de/)
* [koket.se](http://koket.se/)
* [www.kptncook.com](https://www.kptncook.com/)
* [kuchnia-domowa.pl](https://kuchnia-domowa.pl/)
* [www.kwestiasmaku.com](https://www.kwestiasmaku.com/)
* [www.latelierderoxane.com](https://www.latelierderoxane.com)
* [leanandgreenrecipes.net](https://leanandgreenrecipes.net)
* [lecremedelacrumb.com](https://lecremedelacrumb.com/)
* [www.lecker.de](https://www.lecker.de)
* [lekkerensimpel.com](https://lekkerensimpel.com)
* [littlespicejar.com](https://littlespicejar.com/)
* [livelytable.com](http://livelytable.com/)
* [lovingitvegan.com](https://lovingitvegan.com/)
* [www.maangchi.com](https://www.maangchi.com)
* [madensverden.dk](https://madensverden.dk/)
* [www.madewithlau.com](https://www.madewithlau.com/)
* [marleyspoon.com.au](https://marleyspoon.com.au/)
* [marleyspoon.com](https://marleyspoon.com/)
* [marleyspoon.de](https://marleyspoon.de/)
* [marleyspoon.at](https://marleyspoon.at/)
* [marleyspoon.be](https://marleyspoon.be/)
* [marleyspoon.nl](https://marleyspoon.nl/)
* [marleyspoon.se](https://marleyspoon.se/)
* [marmiton.org](https://marmiton.org/)
* [www.marthastewart.com](https://www.marthastewart.com/)
* [matprat.no](https://matprat.no/)
* [meljoulwan.com](https://meljoulwan.com/)
* [www.melskitchencafe.com](https://www.melskitchencafe.com/)
* [mindmegette.hu](http://mindmegette.hu/)
* [minimalistbaker.com](https://minimalistbaker.com/)
* [misya.info](https://misya.info/)
* [www.mobkitchen.co.uk](https://www.mobkitchen.co.uk/)
* [momswithcrockpots.com](https://momswithcrockpots.com/)
* [monsieur-cuisine.com](https://monsieur-cuisine.com/)
* [motherthyme.com](http://motherthyme.com/)
* [mybakingaddiction.com](https://mybakingaddiction.com/)
* [mykitchen101.com](https://mykitchen101.com/)
* [mykitchen101en.com](https://mykitchen101en.com/)
* [www.myplate.gov](https://www.myplate.gov/)
* [myrecipes.com](https://myrecipes.com/)
* [healthyeating.nhlbi.nih.gov](https://healthyeating.nhlbi.nih.gov/)
* [www.nosalty.hu](https://www.nosalty.hu/)
* [nourishedbynutrition.com](https://nourishedbynutrition.com/)
* [nutritionbynathalie.com/blog](https://nutritionbynathalie.com/blog)
* [cooking.nytimes.com](https://cooking.nytimes.com/)
* [ohsheglows.com](https://ohsheglows.com/)
* [omnivorescookbook.com](https://omnivorescookbook.com)
* [owen-han.com](https://owen-han.com/)
* [101cookbooks.com](https://101cookbooks.com/)
* [www.paleorunningmomma.com](https://www.paleorunningmomma.com/)
* [www.panelinha.com.br](https://www.panelinha.com.br/)
* [paninihappy.com](https://paninihappy.com/)
* [www.pickuplimes.com](https://www.pickuplimes.com/)
* [www.pingodoce.pt](https://www.pingodoce.pt/)
* [popsugar.com](https://popsugar.com/)
* [practicalselfreliance.com](https://practicalselfreliance.com/)
* [pressureluckcooking.com](https://pressureluckcooking.com/)
* [www.primaledgehealth.com](https://www.primaledgehealth.com/)
* [www.projectgezond.nl](https://www.projectgezond.nl/)
* [przepisy.pl](https://przepisy.pl/)
* [purelypope.com](https://purelypope.com/)
* [purplecarrot.com](https://purplecarrot.com/)
* [rachlmansfield.com](https://rachlmansfield.com/)
* [rainbowplantlife.com](https://rainbowplantlife.com/)
* [realfood.tesco.com](https://realfood.tesco.com/)
* [realsimple.com](https://realsimple.com/)
* [recipetineats.com](https://recipetineats.com/)
* [redhousespice.com](https://redhousespice.com/)
* [reishunger.de](https://reishunger.de/)
* [rezeptwelt.de](https://rezeptwelt.de/)
* [rosannapansino.com](https://rosannapansino.com)
* [rutgerbakt.nl](https://rutgerbakt.nl/)
* [sallysbakingaddiction.com](https://sallysbakingaddiction.com)
* [sallys-blog.de](https://sallys-blog.de)
* [www.saveur.com](https://www.saveur.com/)
* [seriouseats.com](https://seriouseats.com/)
* [simple-veganista.com](https://simple-veganista.com/)
* [simplyquinoa.com](https://simplyquinoa.com/)
* [simplyrecipes.com](https://simplyrecipes.com/)
* [simplywhisked.com](https://simplywhisked.com/)
* [simply-cookit.com](https://simply-cookit.com/)
* [skinnytaste.com](https://skinnytaste.com/)
* [sobors.hu](https://sobors.hu/)
* [www.southerncastiron.com](https://www.southerncastiron.com/)
* [southernliving.com](https://southernliving.com/)
* [spendwithpennies.com](https://spendwithpennies.com/)
* [www.springlane.de](https://www.springlane.de)
* [steamykitchen.com](https://steamykitchen.com/)
* [streetkitchen.hu](https://streetkitchen.hu/)
* [sunbasket.com](https://sunbasket.com/)
* [sundpaabudget.dk](https://sundpaabudget.dk/)
* [www.sunset.com](https://www.sunset.com/)
* [sweetcsdesigns.com](https://sweetcsdesigns.com/)
* [sweetpeasandsaffron.com](https://sweetpeasandsaffron.com/)
* [tasteofhome.com](https://tasteofhome.com)
* [tastesbetterfromscratch.com](https://tastesbetterfromscratch.com)
* [tastesoflizzyt.com](https://tastesoflizzyt.com)
* [tasty.co](https://tasty.co)
* [tastykitchen.com](https://tastykitchen.com/)
* [theclevercarrot.com](https://theclevercarrot.com/)
* [thehappyfoodie.co.uk](https://thehappyfoodie.co.uk/)
* [www.thekitchenmagpie.com](https://www.thekitchenmagpie.com/)
* [thekitchn.com](https://thekitchn.com/)
* [thenutritiouskitchen.co](https://thenutritiouskitchen.co/)
* [thepioneerwoman.com](https://thepioneerwoman.com/)
* [thespruceeats.com](https://thespruceeats.com/)
* [thevintagemixer.com](https://thevintagemixer.com/)
* [thewoksoflife.com](https://thewoksoflife.com/)
* [timesofindia.com](https://timesofindia.com/)
* [tine.no](https://tine.no/)
* [tudogostoso.com.br](https://tudogostoso.com.br/)
* [twopeasandtheirpod.com](https://twopeasandtheirpod.com/)
* [usapears.org](https://usapears.org/)
* [www.valdemarsro.dk](https://www.valdemarsro.dk/)
* [vanillaandbean.com](https://vanillaandbean.com/)
* [vegolosi.it](https://vegolosi.it/)
* [vegrecipesofindia.com](https://vegrecipesofindia.com/)
* [watchwhatueat.com](https://watchwhatueat.com/)
* [www.weightwatchers.com](https://www.weightwatchers.com/)
* [whatsgabycooking.com](https://whatsgabycooking.com/)
* [www.wholefoodsmarket.com](https://www.wholefoodsmarket.com/)
* [www.wholefoodsmarket.co.uk](https://www.wholefoodsmarket.co.uk/)
* [woop.co.nz](https://woop.co.nz/)
* [woolworths.com.au/shop/recipes](https://woolworths.com.au/shop/recipes)
* [en.wikibooks.org](https://en.wikibooks.org/)
* [yemek.com](https://yemek.com/)
* [yummly.com](https://yummly.com/)
* [zeit.de](https://zeit.de/)
* [zenbelly.com](https://zenbelly.com/)


## Acknowledgements

**Recipe Box** was inspired by [Jay Goel](https://github.com/poundifdef)'s [plainoldrecipe](https://github.com/poundifdef/plainoldrecipe).

**Recipe Box** wouldn't be possible without [hhursev](https://github.com/hhursev)'s [recipe-scrapers](https://github.com/hhursev/recipe-scrapers).


## Contributors

* [Sayantan Santra](https://github.com/SinTan1729)


## License

**Recipe Box** is licensed under the [MIT license](LICENSE).
