# Update strategy

The compilation of the O3 shop is defined in collective packages (so-called metapackages). For installation we offer the metapackages "shop-metapackage-ce" and the enclosing "o3-shop" project.

The use of the O3 metapackages is not mandatory. If you prefer your own package compositions, you can use our metapackages as a template. However, we only test our package compilations for functionality. The respective author is responsible for his own compilations.

During installation, the shop is fixed to a version number of the metapackage. If the installation is to be updated, an update process must be carried out. Here we distinguish between 
- implicit updates
- explicit updates 

## implicit updates

This update is carried out without specifying a new version number of the shop.
This way, only bug fixes can be installed. Based on the patch definition, no new functions are added in this way. The installation can usually be carried out without extensive testing. Nevertheless, we recommend appropriate tests.

Implicit updates are only available under certain conditions. For example, the release date of the installed shop version must not be too long ago or the patches must not affect the code structure too much.

```
composer update ...
```

## explicit updates

This updates to a new shop version. The target version is explicitly specified during the update process.

Functional changes or structural changes are installed here. However, this may also include error corrections that are no longer available for the previous shop version, e.g. for reasons of age.

Explicit updates are to be tested extensively by the shop operator before productive use in conjunction with all extensions used, in order to identify and solve compatibility problems in advance.

```
composer require o3-shop/shop-metapackage-ce:v1.2.0
```

---

# Updatestrategie

Die Kompilation des O3-Shops wird in Sammelpaketen (so genannten Metapackages) definiert. Zur Installation bieten wir die Metapackages "shop-metapackage-ce" und das umschließende "o3-shop"-Projekt an.

Die Verwendung der O3-Metapackages ist keine Pflicht. Wer eigene Paketzusammenstellungen bevorzugt, kann unsere Metapackages als Vorlage verwenden. Jedoch testen wir ausschließlich unsere Paketzusammenstellungen auf Funktionsfähigkeit. Für eigene Kompilationen ist der jeweilige Autor selbst verantwortlich.

Bei der Installation wird der Shop auf eine Versionsnummer des Metapackage festgeschrieben. Soll die Installation aktualisiert werden, ist die Durchführung eines Updateprozesses notwendig. Hierbei unterscheiden wir zwischen 
- impliziten Updates
- expliziten Updates 

## implizite Updates

Diese Aktualisierung wird durchgeführt, ohne eine neue Versionsnummer des Shops anzugeben.
Damit lassen sich ausschließlich Fehlerkorrekturen installieren. Auf Grund der Patchdefinition werden so keine neuen Funktionen hinzugefügt. Die Installation kann in der Regel ohne umfangreichen Prüfungsaufwand durchgeführt werden. Wir empfehlen dennoch entsprechende Tests.

Implizite Updates stehen nur unter bestimmten Bedingungen zur Verfügung. So darf der Veröffentlichungszeitpunkt der installierten Shopversion nicht zu lang her sein oder die Patches dürfen sich nicht zu sehr auf die Codestruktur auswirken.

```
composer update ...
```

## explizite Updates

Hierbei wird auf eine neue Shopversion aktualisiert. Die Zielversion wird beim Updateprozess ausdrücklich angegeben.

Hierbei werden Funktionsänderungen oder Strukturänderungen installiert. Jedoch können hier auch Fehlerkorrekturen enthalten sein, die z.B. aus Altersgründen für die bisherige Shopversion nicht mehr verfügbar sind.

Explizite Updates sind vor dem Produktiveinsatz in Verbindung mit allen eingesetzten Erweiterungen durch den Shopbetreiber umfangreich zu testen, um Kompatibilitätsprobleme vorab zu erkennen und zu lösen.

```
composer require o3-shop/shop-metapackage-ce:v1.2.0
```