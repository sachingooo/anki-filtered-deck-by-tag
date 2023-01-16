# Filtered Deck By Tag
An Anki add-on that creates a filtered deck from the browser sidebar. Used for studying by tag instead of by deck.

## Usage
1. Right click a tag in the browser sidebar
2. Select "Create Filtered Deck" from the right-click menu. A filtered deck will be created from the tag you right clicked on. 

## Configuration
Configuration options can be found in the add-on config, accessible from Tools → Add-ons → Select the add-on → Config. 
* By default, there is search text that is added to the end of the filtered deck search (is:due OR is:new) so that studying the tag pulls all new or due cards - this replicates studying by deck most closely. To modify this search text that's added, change the value of the `supplementalSearchText` variable in the config. 
* By default, there is a limit of 300 cards that are added to the deck. I chose this because it's sufficiently high that I'd never personally want to study a deck that large without breaking it up. If you'd like to change the limit of the number of cards pulled into the filtered deck, modify the `numCards` in the config. 
* The addon automatically unsuspends cards that should belong in the deck. To disable this, mark the unsuspendAutomatically configuration option as false.

## Notes
* This add-on <i>creates</i> the filtered deck. It does not regularly <i>rebuild</i> that filtered deck. For that, I recommend one of the rebuild all add-ons. 
* Bug reports should be added to the issues page here. 
