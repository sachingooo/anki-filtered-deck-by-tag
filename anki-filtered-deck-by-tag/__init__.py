# Filtered Deck From Tag
#
# Copyright (C) 2022  Sachin Govind
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU Affero General Public License as
# published by the Free Software Foundation, either version 3 of the
# License, or (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Affero General Public License for more details.
#
# You should have received a copy of the GNU Affero General Public License
# along with this program.  If not, see <https://www.gnu.org/licenses/>.

from aqt import mw
from aqt.qt import *
from aqt.utils import tooltip
from anki.collection import SearchNode
from aqt.browser import SidebarItem, SidebarTreeView, SidebarItemType
from aqt.gui_hooks import browser_sidebar_will_show_context_menu

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from aqt.browser import SidebarTreeView  # type: ignore

config = mw.addonManager.getConfig(__name__)
assert len(config["supplementalSearchTexts"]) == len(config["shortNames"]
                                                     ), "Length of supplementalSearchTexts and shortNames are not the same in Filtered Deck From Tag addon configuration."


def _filteredDeckFromTag(sidebar: "SidebarTreeView",  menu: QMenu, item: SidebarItem, index: QModelIndex):
    # Adds our option to the right click menu for tags in the deck browser
    if item.item_type == SidebarItemType.TAG:
        menu.addSeparator()
        if len(config["supplementalSearchTexts"]) == 0:
            menu.addAction("Create Filtered Deck",
                           lambda: _createFilteredDeck(item, ""))
        else:
            for i in range(len(config["supplementalSearchTexts"])):
                supplementalSearchText = config["supplementalSearchTexts"][i]
                shortName = config["shortNames"][i]
                menu.addAction("Create Filtered Deck - %s" % shortName,
                               lambda sst=supplementalSearchText, sn=shortName: _createFilteredDeck(item, sst, sn))


def _createFilteredDeck(item: SidebarItem, supplementalSearchText, shortName):
    if not item.full_name or len(item.full_name) < 2:
        return

    col = mw.col
    if col is None:
        raise Exception('collection is not available')

    search = col.build_search_string(SearchNode(tag=item.full_name))
    search += " " + supplementalSearchText
    deckName = _formatDeckNameFromTag(item.name)
    if len(shortName) > 0:
        deckName += " - %s" % shortName
    numberCards = 300

    # modifications based on config
    if config:
        if config["numCards"] > 0:
            numberCards = config["numCards"]
        if config["unsuspendAutomatically"]:
            cidsToUnsuspend = col.find_cards(search)
            col.sched.unsuspend_cards(cidsToUnsuspend)

    mw.progress.start()
    did = col.decks.new_filtered(deckName)
    deck = col.decks.get(did)
    deck["terms"] = [[search, numberCards, 6]]  # 6 = DYN_DUE constant
    col.decks.save(deck)
    col.sched.rebuildDyn(did)
    mw.progress.finish()
    mw.reset()
    tooltip("Created filtered deck from tag %s " % (item.name))


def _formatDeckNameFromTag(tagName: str):
    # Make the deck name readable
    pieces = tagName.split("_")
    if len(pieces) == 1:
        return tagName
    if pieces[0].isnumeric():
        pieces.pop(0)

    return " ".join(pieces)


# Append our option to the context menu
browser_sidebar_will_show_context_menu.append(_filteredDeckFromTag)
