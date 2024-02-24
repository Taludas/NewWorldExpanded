# New World Expanded

![Thumbnail](https://user-images.githubusercontent.com/64583643/189413460-86d79429-272c-4c3a-b243-3733c109e044.png)

 This mod enhances the New World map generation with reskinned OW Islands and fresh map templates for more variety and replayability of the game. There is also "Colossus of the New World: Finding Mayabeque" which adds a completely new session to the New World region for you to explore.

 Für die deutsche Version des readmes, bitte [hier](readme_german.md) klicken.

 If you like this mod and want to support me, feel free to share it with your friends. You can also buy me a coffee at Ko-Fi!

[![ko-fi](https://ko-fi.com/img/githubbutton_sm.svg)](https://ko-fi.com/W7W8L558T)

## How to use

- Automatic install using the Anno Mod Browser, available from the main menu of your Anno 1800 game.
- Either use [iModYourAnno](https://github.com/anno-mods/iModYourAnno/releases) mod manager or know [how to install mods manually](https://github.com/jakobharder/anno1800-mod-loader#mods).
- If you download the mod manually, use the archive from [GitHub releases](https://github.com/Taludas/NewWorldExpanded/releases). Don't download the whole repo! (If you do the latter, you will find yourself with missing island mesh files! -> Invisible islands)

## Changelog
<details>
    <summary>Patch Notes Version 3.0.3</summary>

* Updates:
    - Several fixes for "Colossus of the New World: Finding Mayabeque":
      - fix ruin quest FINALLY?! The first renovation Quest should not autocomplete anymore. This should fix the bug, that the Monument doesn't acquire resources and workforce in stage 3/3.
      - fix missing Jaguar Furs production requirement for all language files other than English/German in quest description of "Restoring the Colony: The Colonial Export Imperium".
      - add compatibility for start trigger with "Trelawney Quest Skip" mod.
</details>

<details>
    <summary>Patch Notes Version 3.0.2</summary>

* Updates:
    - Several fixes for "Colossus of the New World: Finding Mayabeque":
      - new advanced mod trigger by Serp for all possible conditions to start the Questline for Mayabeque
      - fix issue with cycle time of the Grand Hotel Santa Cruz going from 5:00 to 4:30 and then jumping back by reducing the cycle time to 0 seconds.
      - fix issue with early unlock of the Ruins of Castle Santa Cruz due to DefaultLockedState 0 introduced for the ruins for testing in v1.0.12 and left inside accidentally. See release for issues and possible solutions coming from this bug.
</details>

<details>
    <summary>Patch Notes Version 3.0.1</summary>

* Updates:
    - Several fixes for "Colossus of the New World: Finding Mayabeque":
      - Fix for map template: Small change to the position of Paloma's island to prevent clipping into the large neighbouring island in the southeast (especially if you play with NW Expanded Mod at the same time)
      - Santa Cruz has been reworked to add some palm trees variation to the jungle
      - Fix missing LoadAfterId for Serps "Cape Trewlany disabler" Mod
      - Fix modinfo.json typo in LoadAfterId
      - Fix Grand Hotel Santa Cruz showing "0%" Productivity in Sandbox
      - Fix Grand Hotel not supplying NW Tourism Hotels with the corresponding Happiness Need (see above fix)
      - Fix Quest to build Kontor on Santa Cruz: Quest now resolves when Kontor is built before the Quest triggered.
      - Quest to build Kontor on Santa Cruz will now be started when entering session for the first time, parallelizing the build material and kontor building quest, to prevent players from having to delete the Kontor to solve the quest, if they didn't follow the Questline word for word.
      - [NW Tourism] Fix Bar, Cafe, Restaurant and NW Monument not unlocking if Tourists are only settled in Cape Trelawny
      - Fix first quest to select a pub when using AIs: AI pubs no longer count
      - Coop Trigger for Questline when using Cap Trelawny
      - Add Compatibility with Kingsgrove (upload updated Kingsgrove mod to mod.io)
      - Fix loosing castle ruin after Kontor destruction/loss through AI, Quest is still bugged when this happens before the initial renovation from ruin to scaffolding happens, as it then stays as a ruin and will lead to a CTD when trying to upgrade.
      - Fix and update several loca files
      - add traditional chinese loca
</details>

<details>
    <summary>Patch Notes Version 3.0.0</summary>

* Additions:
    - Added "Colossus of the New World: Finding Mayabeque". For more information about this mod please visit the mod page on [mod.io](https://mod.io/g/anno-1800/m/colossus-of-the-new-world-finding-mayabeque)

* Updates:
    - Adjusted the mod "Muddy Rivers Removed" for GU18:
      - Drastically reduce file size with the new possibilities of Loader11.
</details>
<details>
    <summary>Patch Notes Version 2.0.0</summary>

* Updates:
    - Adjusted the mod for GU18:
      - Make compatible for usage via mod.io (previously island textures were missing)
      - Drastically reduce file size with the new possibilities of Loader11.

* Adjustments:
    - Made a version available which uses a randomized map template for the New World (primarily for usage with mod.io, advanced users may use iMYA for more tweakability)

</details>
<details>
    <summary>Patch Notes Version 1.2.0</summary>

* Adjustments:
    - In order to keep the file size low, I split the mod into two mods: "Muddy Rivers removed" and "New World Expanded". The first only replaces the NW island's river colour with a blue one. New World Expanded is the main mod, adding the reskinned islands!

* Updates:
    - Adjusted the mod for better usage with iModYourAnno v0.5, default map template used is now "Corners". Fixed the issue with multiple people having a endless loading loop due to faulty iMYA tweaking. No matter what you tweak in iMYA, you will now always get one of the three map templates.

</details>
<details>
    <summary>Patch Notes Version 1.1.0</summary>

* Updates:
    - Update the mod to only use one mod folder instead of the separate installation directories.

</details>
<details>
    <summary>Patch Notes Version 1.0.0</summary>

* Updates:
    - Updated all Island Files to GU16 version.
    - Added Enlarged Map Templates for GU16 (new Savegame required, old map templates won't enlarge themselves to the new ones, but use the old extension)
    - Updated muddy rivers with new Islands from GU16
    - Prepared modularity through iMYA, right now only the map templates are modular, if you want to disable the new islands or don't want muddy rivers, you have to manually edit the assets file right now (remove the <Include> Tags with the appropriate xml-File).

</details>
<details>
    <summary>Patch Notes Version 0.1.2</summary>

* Fixed a bug where some islands didn't get the new texture. Please download the latest release and overwrite the download of v0.1.0!

</details>
<details>
    <summary>Patch Notes Version 0.1.1</summary>

* HOTFIX: I forgot to add the most important file of all! The materialset texture file! Please download the latest release and overwrite the download of v0.1.0!

</details>
<details>
    <summary>Patch Notes Version 0.1.0</summary>

* Added island files.
* Added reskinned OW islands to random pool
* Added new map templates
* Added version with blue rivers in NW instead of muddy ones
</details>

-----

![banner](https://user-images.githubusercontent.com/64583643/189413451-f866f2cf-2e93-4c53-9e47-547e6d874627.png)
## New World Expanded: Reskinned Old World Islands for the New World
This module contains 15 reskinned OW islands to use it in the random pool for map generation in the NW for more variety in the session where you normally find all the same islands again and again. The Islands have no new mesh, only the textures and props are replaced to fit the NW.

Have a look for yourself how good some variety in the NW actually is and what you can think of, maybe a little tropical touristic paradise?

In anticipation of upcomming mods I also integrated functional river slots on them. ~~For now, there are no river buildings, so you can't use them for anything apart from admiring the effort I had to find suitable positions for them.~~ **Fully compatible with my mod [River Slots](https://github.com/Taludas/RiverSlots) which adds 11 new river slot buildings to the OW and NW!**

-----

![banner_maptemplates](https://user-images.githubusercontent.com/64583643/210533908-00429c86-5cb7-464f-8e04-d044400c6ca5.png)
## New World Expanded: New Map Templates for the NW session
This module contains 3 new map templates for each region size (large, medium, small) which you can choose at game generation.
- Corners: Inspired by OW corners map template with large islands in the corners and small ones in the center of the map.
- Island Arch: Inspired by the OW island arch template with the majority of the islands in the bottom of the map and only some small ones to the north/east.
- Pirates Den: All big islands are located tightly around the pirates slot, so it is quite dangerous to settle and trade there.

-----

![banner_rivercolour](https://user-images.githubusercontent.com/64583643/189413458-592e3a64-f896-42ed-a016-98c2d7551e0b.png)
## New World Expanded: River Colour
This module only changes the vanilla islands river colour to blue instead of the muddy brown so you can have more of a tropical paradise instead of an Amazonas feeling.

-----

![banner_colossus](https://github.com/Taludas/NewWorldExpanded/assets/64583643/c4aaa035-478a-49c6-9db0-7f7abbabac12)
## Colossus of the New World: Finding Mayabeque

Follow Vasco Oliveira into the lands of his former colonial administration! After his humiliating defeat in Crown Falls and his rehabilitation in the "Season of Silver", he now seeks revenge on his former master: King Joao of La Corona. As the previous events have taken their toll on his constitution, he asks you for help: accept his invitation and find a way to the forgotten colony settlements of Mayabeque (Pronounced "Majabek"). Support him in his endeavour to lead the diminished colonial power to new glory! But be careful, your journey may not go unnoticed and not everyone will support your plans for the lands of Mayabeque...

A DLC sized mod that adds a second New World session to the game, including a 15-quest long story with two different ends, a converted Crown Falls continental island and some other fancy stuff like two new Monuments with unique effects, two new Traders and another new way to generate more 'arctic gas' and 'bear furs'.

The main addition of "Colossus of the New World" is a new region called Mayabeque, unlocked after completing a series of Quest and an Expedition available once you house 1 Investor. The Expedition also features one completely custom Expedition Event. (If you want to explore all decisions of the Event, bring a medicore boat and not the best items, otherwise you might be able to skip the event on the first decisions. Also save before the Event to explore all endings.)

It is a second New World region and consists of a mixture of different island sizes with one of them being unique, it is the big continental island named "Santa Cruz", located in the eastern part of the region. Some of you may identify Crown Falls, but it has been fully converted to the New World setting with adapted textures and props. The session also features a set of five unique coast-free islands known from the "Clash of Couriers" Scenario. These cliff islands can only be settled via Airship (if you want to utilise these Cliff islands to their full potential, you will need the "Empires of the Skies" DLC enabled to settle them) and feature some rare ressources, you will surely try to exploit to provide your Investors with their sophisticated needs. To support your local economy, two new traders have established warehouses in the new region. Otherwise the Gameplay in this region, including available population, buildings, goods, resources and fertilities etc. is the same as in the rest of the New World.

The DLC includes a 15-quest long storyline which surrounds the build-up of the new colonial power, assisted by a well known character of another DLC. The questline has two unique endings, so to explore all possibilites of the story, you may want to start a second game to discover which one suits your playstyle best. While following the questline you will get the option to build up one of two versions of a unique monument on Santa Cruz island, either benefiting your military and trading fleet or boosting your Tourism Empire to a new level (To complete this part of the Questline you will need the "New World Rising" and "Tourist Season" DLCs and the Mod "New World Tourism" enabled.)

For further information and some pictures from the mod, visit its site on [mod.io](https://mod.io/g/anno-1800/m/colossus-of-the-new-world-finding-mayabeque)