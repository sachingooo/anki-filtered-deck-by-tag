# Filtered Deck By Tag
An Anki add-on that creates a filtered deck from the browser sidebar. Used for studying by tag instead of by deck.

## Usage
1. Right click a tag in the browser sidebar
2. Select "Create Filtered Deck" from the right-click menu. A filtered deck will be created from the tag you right clicked on.
3. Modify your searches in the config! See below for the config that I use. 

Right click menu:

![image](https://user-images.githubusercontent.com/62180448/218291471-142ebd77-2fa2-4f2d-84dc-cf9b0ff342ca.png)




## Configuration
Configuration options can be found in the add-on config, accessible from Tools → Add-ons → Select the add-on → Config. This addon will create a filtered deck from the tag you right clicked on, and appends supplemental search text to that search text (based on what you configure). Multiple configuration options are permitted. 
* There is an array named `supplementalSearchTexts`, which is an array of strings. For each string that you add, a new option will be added in the right click menu on the browse screen for tags, corresponding to that string. 
* There is a paired array of strings named `shortNames`. These correspond to the names you want to give each of these options. These entries should correspond to the entries in `supplementalSearchTexts`. 
* By default, there is a limit of 9999 cards that are added to the deck (maximum allowed by Anki). I personally use 300 cards as the limit, because it's sufficiently high that I'd never personally want to study a deck that large without breaking it up. If you'd like to change the limit of the number of cards pulled into the filtered deck, modify the `numCards` in the config. 
* The addon automatically unsuspends cards that should belong in the deck. To disable this, mark the `unsuspendAutomatically` configuration option as false.
* You can change the default order used for the filtered decks. It currently defaults to Order Due. In order to change this, modify the value of `defaultOrder` in the configuration to one of the following integer values:
    * 0 for Oldest
    * 1 for Random
    * 2 for Increasing intervals
    * 3 for Decreasing intervals
    * 4 for Most lapses
    * 5 for Order added
    * 6 for Order due (default)
    * 7 for Latest added first
    * 8 for Relative overdueness

For more detail on what each of these orders mean, see the [Anki User Manual](https://docs.ankiweb.net/filtered-decks.html#order)

As an example, here's what I use in my config:

```
{
	"numCards": 9999,
	"shortNames": [
		"high yield due",
		"high yield due and new",
		"due and new"
	],
	"supplementalSearchTexts": [
		"tag:#AK_Step1_v11::^Other::^HighYield::1-HighYield is:due",
		"tag:#AK_Step1_v11::^Other::^HighYield::1-HighYield (is:due OR is:new)",
		"(is:due OR is:new)"
	],
	"unsuspendAutomatically": true,
	"defaultOrder": 6
}
```

## Notes
* This add-on <i>creates</i> the filtered deck. It does not regularly <i>rebuild</i> that filtered deck. For that, I recommend one of the rebuild all add-ons. 
* Bug reports should be added to the issues page in the GitHub repository. 
