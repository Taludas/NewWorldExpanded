# New World Expanded

![Thumbnail](https://user-images.githubusercontent.com/64583643/189413460-86d79429-272c-4c3a-b243-3733c109e044.png)

 Diese Mod erweitert die New World Map Generation mit neu gestalteten OW-Inseln und neuen Kartenvorlagen für mehr Abwechslung und Wiederspielbarkeit des Spiels. Außerdem findet ihr hier die Mod "Koloss der Neuen Welt: Expedition nach Mayabeque", das die Region der Neuen Welt um eine völlig neue Session erweitert, die nur darauf wartet erkundet zu werden.

 Wenn dir diese Mods gefallen und du mich unterstützen möchtest, kannst du sie gerne mit deinen Freunden teilen. Ihr könnt mir auch einen Kaffee bei Ko-Fi ausgeben!

[![ko-fi](https://ko-fi.com/img/githubbutton_sm.svg)](https://ko-fi.com/W7W8L558T)

## How to use

- Automatische Installation über den Anno-Mod-Browser, der über das Hauptmenü des Anno 1800-Spiels erreichbar ist.
- Verwende entweder den [iModYourAnno](https://github.com/anno-mods/iModYourAnno/releases) Mod-Manager oder weiß [wie man Mods manuell installiert](https://github.com/jakobharder/anno1800-mod-loader#mods).
- Wenn du die Mod manuell herunterlädst, verwende das Archiv von [GitHub releases] (https://github.com/Taludas/NewWorldExpanded/releases). Lade nicht das gesamte Repo herunter! Es werden dann mesh-files der Inseln fehlen (durchsichtige Inseln)!

## Changelog
<details>
    <summary>Patch Notes Version 3.0.4</summary>

* Updates:
    - Mehrere Updates für "Koloss der Neuen Welt: Expedition nach Mayabeque":
      - schalte das Gasprodukt frei, um hoffentlich das Problem des unsichtbaren NW-Gasminen-Baumenüeintrags zu lösen, wenn man diesen DLC nicht benutzt oder besitzt
      - Update der gemeinsamen Mod "combi allocations" von Qurila
      - Gemeinsame Mod "Pools und Definitionen" für die Jaguar-Jagdhütte hinzugefügt
</details>

<details>
    <summary>Patch Notes Version 3.0.3</summary>

* Updates:
    - Mehrere Korrekturen für "Koloss der Neuen Welt: Expedition nach Mayabeque":
      - Ruinen-Quest ENDLICH repariert?! Die erste Renovierungsquest sollte sich nicht mehr automatisch erledigt werden. Dies sollte den Fehler beheben, dass das Monument in Stufe 3/3 keine Ressourcen und Arbeitskräfte bekommt.
      - behebt die fehlende Forderung nach der Produktion von Jaguar-Pelzen für alle Sprachdateien außer Englisch/Deutsch in der Questbeschreibung von "Restaurierung der Kolonie: Das Koloniale Export-Imperium".
      - Kompatibilität für den Starttrigger mit der Mod "Trelawney Quest Skip" hinzugefügt.
</details>

<details>
    <summary>Patch Notes Version 3.0.2</summary>

* Updates:
    - Mehrere Korrekturen für "Koloss der Neuen Welt: Expedition nach Mayabeque":
      - neuer erweiterter Mod-Trigger von Serp für alle möglichen Bedingungen zum Starten der Questline für Mayabeque
      - Behebung des Problems, dass die Produktionszeit des Grand Hotel Santa Cruz von 5:00 auf 4:30 und dann wieder zurücksprang, indem die Produktionszeit auf 0 Sekunden reduziert wurde.
      - Behebung des Problems, dass die Ruinen der Burg Santa Cruz zu früh freigeschaltet wurden, weil DefaultLockedState = 0 für die Ruinen zu Testzwecken in v1.0.12 eingeführt und versehentlich drinnen gelassen wurde. Siehe Release für Probleme und mögliche Lösungen, die sich aus diesem Fehler ergeben.
</details>

<details>
    <summary>Patch Notes Version 3.0.1</summary>

* Updates:
    - Mehrere Korrekturen für "Koloss der Neuen Welt: Expedition nach Mayabeque":
      - Fix für Map-Template: Kleine Änderung der Position von Palomas Insel, um ein Clipping in die große Nachbarinsel im Südosten zu verhindern (besonders wenn man mit NW Expanded Mod gleichzeitig spielt)
      - Santa Cruz wurde nochmals bearbeitet, um einige Palmen in den Dschungel einzustreuen.
      - Fix für fehlende LoadAfterId für Serps "Cape Trewlany disabler" Mod
      - Fix für modinfo.json Tippfehler bei LoadAfterId
      - Fix für Grand Hotel Santa Cruz, dass nun keine "0%" Produktivität im Sandbox Modus zeigt
      - Fix für Grand Hotel, dies versorgt NW Tourism Hotels nun mit dem entsprechenden Happiness Need (siehe obiger Fix)
      - Fix für Quest zum Bau des Kontors auf Santa Cruz: Die Quest wird nun als erledigt gezählt, selbst wenn das Kontor gebaut wird, bevor die zugehörige Quest ausgelöst wurde.
      - Die Quest zum Bau des Kontors auf Santa Cruz wird nun gestartet, wenn man die Session zum ersten Mal betritt: die Quest zum Bau des Materials und des Kontors wird parallelisiert, um zu verhindern, dass Spieler das Kontor löschen müssen, um die Quest zu lösen, wenn sie die Questline nicht Wort für Wort befolgt haben (man musste erst zwingend das Baumaterial bei Vasco abholen).
      - Fix für "NW-Tourism" Mod: Bar, Cafe, Restaurant und NW-Monument werden nun freigeschaltet, wenn Touristen nur in Cape Trelawny und nicht in der Alten Welt angesiedelt sind
      - Fix für die erste Quest zur Auswahl eines Wirtshauses bei Verwendung von KIs: KI-Wirtshaus zählen nicht mehr
      - Coop Trigger für Questline bei Verwendung von Cap Trelawny hinzugefügt
      - Kompatibilität mit Kingsgrove hinzugefügt (aktualisierte Kingsgrove-Mod auf mod.io hochgeladen)
      - Fix für den Verlust der Burgruine nach Kontor-Zerstörung/Verlust durch die KI, Quest ist allerdings immer noch fehlerhaft, wenn dies vor der anfänglichen Renovierung von Ruine zu Gerüst passiert, da sie dann als Ruine bleibt und zu einem CTD führt, wenn man versucht, sie zu auszubauen.
      - Mehrere Loca-Dateien korrigiert und aktualisiert
      - Traditionelle chinesische Loca hinzugefügt
</details>

<details>
    <summary>Patch Notes Version 3.0.0</summary>

* Neue Mod:
    - Hinzufügen von "Koloss der Neuen Welt: Expedition nach Mayabeque". Für weitere Informationen über diese Mod besucht bitte die Mod-Seite auf [mod.io](https://mod.io/g/anno-1800/m/colossus-of-the-new-world-finding-mayabeque)

* Updates:
    - Die Mod "Muddy Rivers Removed" wurde für GU18 angepasst:
      - Drastische Reduzierung der Dateigröße mit den neuen Möglichkeiten von Loader11.

</details>
<details>
    <summary>Patch Notes Version 2.0.0</summary>

* Updates:
    - Die Mod wurde für GU18 angepasst:
      - Anpassungen für die alleinige Nutzung über mod.io (vorher fehlten Inseltexturen).
      - Drastische Reduzierung der Dateigröße mit den neuen Möglichkeiten von Loader11.

* Anpassungen:
    - Ich habe eine Version zur Verfügung gestellt, die eine randomisierte Kartenvorlage für die Neue Welt verwendet (hauptsächlich für die Verwendung mit mod.io, fortgeschrittene Benutzer können iMYA für mehr Anpassungsmöglichkeiten verwenden)

</details>
<details>
    <summary>Patch Notes Version 1.2.0</summary>

* Anpassungen:
    - Um die Dateigröße gering zu halten, habe ich die Mod in zwei Mods aufgeteilt: "Muddy Rivers removed" und "New World Expanded". Die erste ersetzt nur die Flussfarbe der NW-Insel durch eine blaue. New World Expanded ist die Hauptmod, der die neu geskinnten Inseln hinzufügt!

* Aktualisierungen:
    - Die Mod wurde für eine bessere Nutzung mit iModYourAnno v0.5 angepasst, die standardmäßig verwendete Kartenvorlage ist jetzt "Corners". Das Problem mit der endlosen Ladeschleife bei mehreren Spielern aufgrund von fehlerhaften iMYA-Einstellungen wurde behoben. Unabhängig davon, was man in iMYA einstellt, erhält man nun immer eine der drei Kartenvorlagen.

</details>
<details>
    <summary>Patch Notes Version 1.1.0</summary>

* Aktualisierungen:
  - Aktualisierung der Mod, so dass nur noch ein Mod-Ordner anstelle der separaten Installationsverzeichnisse verwendet wird.

</details>
<details>
    <summary>Patch Notes Version 1.0.0</summary>

* Aktualisierungen:
  - Alle Inseldateien auf GU16 Version aktualisiert.
    - Vergrößerte Kartenvorlagen für GU16 hinzugefügt (neues Savegame erforderlich, alte Kartenvorlagen vergrößern sich nicht auf die neuen, sondern verwenden die alte Erweiterung)
    - muddy rivers mit neuen Inseln aus GU16 aktualisiert
    - Modularität durch iMYA vorbereitet, im Moment sind nur die Kartenvorlagen modular, wenn man die neuen Inseln deaktivieren will oder keine schlammigen Flüsse will, muss man die Assets-Datei jetzt manuell bearbeiten (die <Include> Tags mit der entsprechenden xml-Datei entfernen).

</details>
<details>
    <summary>Patch Notes Version 0.1.2</summary>

* Ein Fehler wurde behoben, bei dem einige Inseln nicht die neue Textur erhielten. Bitte ladet die neueste Version herunter und überschreibt den Download von v0.1.0!
*
</details>
<details>
    <summary>Patch Notes Version 0.1.1</summary>

* HOTFIX: Ich habe vergessen, die wichtigste Datei von allen hinzuzufügen! Die Materialset-Texturdatei! Bitte ladet die neueste Version herunter und überschreibt den Download von v0.1.0!
*
</details>
<details>
    <summary>Patch Notes Version 0.1.0</summary>

* Inseldateien hinzugefügt.
* Neu geskinnte OW-Inseln zum Zufalls-Pool hinzugefügt
* Neue Kartenvorlagen hinzugefügt
* Version mit blauen Flüssen in NW anstelle von schlammigen Flüssen hinzugefügt
</details>

-----

![banner](https://user-images.githubusercontent.com/64583643/189413451-f866f2cf-2e93-4c53-9e47-547e6d874627.png)
## New World Expanded: Reskinned Old World Islands for the New World
Dieses Modul enthält 15 neu geskinnte Alte Welt-Inseln, um sie im Zufalls-Pool für die Kartengenerierung in der Neue Welt für mehr Abwechslung in der Session zu verwenden, wo man normalerweise immer wieder die gleichen Inseln findet. Die Inseln haben kein neues Mesh, nur die Texturen und Requisiten sind ersetzt, um in die Neue Welt zu passen.

Schaut selbst, wie gut die Abwechslung in der Neuen Welt tatsächlich ist und was ihr euch vorstellen könnt, vielleicht ein kleines tropisches Touristenparadies?

Im Vorgriff auf kommende Mods habe ich auch funktionale Fluss-Slots eingebaut. ~~Im Moment gibt es noch keine Flussgebäude, also kann man sie für nichts anderes nutzen, als die Mühe zu bewundern, die ich hatte, um geeignete Positionen für sie zu finden.~~ **Vollständig kompatibel mit meiner Mod [River Slots](https://github.com/Taludas/RiverSlots), die 11 neue Flussplatzgebäude zur OW und NW hinzufügt!**

-----

![banner_maptemplates](https://user-images.githubusercontent.com/64583643/210533908-00429c86-5cb7-464f-8e04-d044400c6ca5.png)
## New World Expanded: New Map Templates for the NW session
Dieses Modul enthält 3 neue Kartenvorlagen für jede Regionsgröße (groß, mittel, klein), die bei der Spielerstellung ausgewählt werden können.
- Ecken: Inspiriert von der OW-Ecken-Kartenvorlage mit großen Inseln in den Ecken und kleinen Inseln in der Mitte der Karte.
- Inselbogen: Inspiriert von der OW-Inselbogenvorlage mit den meisten Inseln im unteren Teil der Karte und nur einigen kleinen Inseln im Norden/Osten.
- Piratenhöhle: Alle großen Inseln liegen dicht um den Piratenplatz herum, so dass es ziemlich gefährlich ist, sich dort niederzulassen und Handel zu treiben.

-----

![banner_rivercolour](https://user-images.githubusercontent.com/64583643/189413458-592e3a64-f896-42ed-a016-98c2d7551e0b.png)
## New World Expanded: River Colour
Mit diesem Modul wird lediglich die Farbe der Flüsse auf den Vanilla-NW-Inseln von schlammigem Braun auf Blau geändert, so dass man eher ein Gefühl von tropischem Paradies als von Amazonas-Regenwald bekommt.

-----

![banner_colossus](https://github.com/Taludas/NewWorldExpanded/assets/64583643/c4aaa035-478a-49c6-9db0-7f7abbabac12)
## "Koloss der Neuen Welt: Expedition nach Mayabeque"

Folgt Vasco Oliveira in die Länder seiner ehemaligen Kolonialverwaltung! Nach seiner demütigenden Niederlage in Crown Falls und seiner Rehabilitierung im "Silbernen Käfig" sinnt er nun auf Rache an seinem ehemaligen Herrn: König Joao von La Corona. Da die vorangegangenen Ereignisse an seiner Verfassung gezehrt haben, bittet er Euch um Hilfe: Nehmt seine Einladung an und findet einen Weg in die vergessenen Kolonien von Mayabeque (sprich: "Majabek"). Unterstützt ihn in seinem Bestreben, die untergegangene Kolonialmacht zu neuem Ruhm zu führen! Aber seid vorsichtig, eure Reise wird nicht unbemerkt bleiben und nicht jeder wird eure Pläne für die Landstriche Mayabeques unterstützen...

Eine Mod in DLC-Größe, die dem Spiel eine zweite Session in der Neuen Welt hinzufügt, einschließlich einer 15 Quests langen Story mit zwei verschiedenen Enden, einer umgewandelten Kontinentalinsel Crown Falls und einigen anderen ausgefallenen Dingen wie zwei neuen Monumenten mit einzigartigen Effekten, zwei neuen Händlern und einer weiteren neuen Möglichkeit, mehr "arktisches Gas" und "Bärenfelle" zu erzeugen.

Die wichtigste Neuerung von "Colossus of the New World" ist eine neue Region namens Mayabeque, die nach dem Abschluss einer Reihe von Quests und einer Expedition freigeschaltet wird, die verfügbar ist, sobald man 1 Investor besitzt. Die Expedition bietet auch ein komplett eigenes Expeditionsereignis. (Wenn ihr alle Entscheidungen des Ereignisses erkunden wollt, nehmt ein mittelmäßiges Schiff und nicht die besten Items mit, sonst könnt ihr das Ereignis bei den ersten Entscheidungen vielleicht überspringen. Speichert auch vor dem Ereignis, um alle Enden zu erforschen.)

Es ist eine zweite Session in der Neuen Welt und besteht aus einer Mischung verschiedener Inselgrößen, von denen eine einzigartig ist, nämlich die große Kontinentalinsel "Santa Cruz", die sich im östlichen Teil der Region befindet. Einige von euch werden Crown Falls vielleicht wiedererkennen, aber sie wurde mit angepassten Texturen und Props vollständig in das Neue-Welt-Setting konvertiert. Die Session enthält auch eine Reihe von fünf einzigartigen küstenfreien Inseln, die aus dem Szenario "Der Postpokal" bekannt sind. Diese Klippeninseln können nur per Luftschiff besiedelt werden (wenn ihr das volle Potenzial dieser Klippeninseln ausschöpfen wollt, müsst ihr den DLC "Reich der Lüfte" aktivieren, um sie zu besiedeln) und verfügen über einige seltene Ressourcen, die ihr sicherlich nutzen wollt, um eure Investoren mit ihren anspruchsvollen Bedürfnissen zu versorgen. Um die lokale Wirtschaft zu unterstützen, haben zwei neue Händler Warenlager in der Region errichtet. Ansonsten ist das Gameplay in dieser Session, einschließlich der verfügbaren Bevölkerung, Gebäude, Waren, Ressourcen und Fruchtbarkeiten etc. das gleiche wie im Rest der Neuen Welt.

Der DLC enthält eine 15 Quests lange Storyline, die sich um den Aufbau der neuen Kolonialmacht dreht, die von einem bekannten Charakter aus einem anderen DLC unterstützt wird. Um alle Möglichkeiten der Geschichte zu erkunden, solltet ihr ein zweites Spiel beginnen, um herauszufinden, welches Ende am besten zu eurem Spielstil passt. (oder ladet den Save vor der DecisionQuest) Während ihr der Questlinie folgt, habt ihr die Möglichkeit, eine von zwei Versionen eines einzigartigen Monuments auf der Insel Santa Cruz zu errichten, das entweder eurem Militär und eurer Handelsflotte zugute kommt oder euer Tourismusimperium ine eine neue Dimension befördert (um diesen Teil der Questlinie abzuschließen, müsst ihr die DLCs "Aufstieg der Neuen Welt" und "Reisezeit" sowie die Mod "New World Tourism" aktivieren).

Für weitere Informationen und Bilder, besucht die Mod-Website auf [mod.io](https://mod.io/g/anno-1800/m/colossus-of-the-new-world-finding-mayabeque)