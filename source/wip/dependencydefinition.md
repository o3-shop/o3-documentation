# Definition of dependencies

The package composition is defined by a dependency tree. This contains a list of all the necessary packages to be able to install an executable shop.

We use [Composer](https://getcomposer.org/) to compile the packages, which is also used for patch installations, updates and upgrades. 

We are aware that the use of Composer increases the demands on the shop administrator and also on the server. On the other hand, there are various advantages:

- A compilation created with Composer can cover larger ranges of system environments.

  For example, the current shop supports PHP 7.4 to PHP 8.2. It could be possible that there is no package constellation that can cover this entire range equally. So we might have to narrow down the system requirements without Composer.
  
- More optimised for each environment

  Composer can decide for individual packages within their given version range which version is the most optimal depending on the environment. This may mean that a shop installation for PHP 7.4 contains different code than the version for PHP 8.2. 
  
- Security

  Packages can be updated independently of the release cycle of the main project (implicit update - e.g. when security holes are found). In the case of monolithic packages without package management, the entire shop would always have to be replaced in these cases.
  
- Dependency management

  Each package can define in a very detailed way in which environment it can be installed. So it is (almost) impossible that modules for O3-Shop 1.0 are installed in O3-Shop 2.0 if this would not work there.
  
- Module installation

  Composer offers solutions for technical challenges that have to be solved by module authors. Therefore, there is no alternative to using it for modules.
  
- Deployment

  Large shop installations face special challenges such as plannable updates with the shortest possible downtime. Composer makes it possible to automatically set up a defined shop constellation including all custom plugins and custom themes and is. In addition, the process can also be integrated into automatic workflows.
  
- Patch-compatible

  Composer allows the update-safe and recoverable modification of code components (e.g. in the context of a hotfix).
  
Within limits, it is possible to bypass the direct use of Composer. For new and test installations, we offer ready-to-use complete packages for download, which, however, do without the advantages mentioned.

---

# Definition von Abhängigkeiten

Die Paketzusammenstellung wird durch einen Abhängigkeitsbaum definiert. Dieser enthält eine Liste aller notwendigen Pakete, um einen lauffähigen Shop installieren zu können.

Zur Zusammenstellung der Pakete verwenden wir [Composer](https://getcomposer.org/), der damit ebenso bei Patchintallationen, Updates und Upgrades zum Einsatz kommt. 

Uns ist bewusst, dass die Verwendung von Composer die Anforderungen an den Shopbetreuer und auch an den Server erhöht. Dem gegenüber stehen diverse Vorteile:

- Eine mit Composer erstellte Zusammenstellung kann größere Bereiche an Systemumgebungen abdecken.

  Der aktuelle Shop unterstützt z.B. PHP 7.4 bis PHP 8.2. Es könnte möglich sein, dass es keine Paketkonstellation gibt, die diese gesamte Reichweite gleichermaßen abdecken kann. Wir müssten also ohne Composer eventuell die Systemanforderungen eingrenzen.
  
- optimierter für jede Umgebung

  Composer kann für einzelne Pakete innerhalb ihrer vorgegebenen Versionsspanne entscheiden, welche Version umgebungsabhängig die Optimalste ist. Das kann dazu führen, dass eine Shopinstallation für PHP 7.4 anderen Code enthält, als die Version für PHP 8.2. 
  
- Sicherheit

  Pakete können unabhängig vom Releasezyklus des Hauptprojekts aktualisiert werden (implizites Update - z.B. bei gefundenen Sicherheitslücken). Bei monolithischen Paketen ohne Paketverwaltung müsste in diesen Fällen immer der gesamte Shop ausgetauscht werden.
  
- Abhängigkeitenverwaltung

  Jedes Paket kann sehr kleinteilig definieren, in welcher Umgebung es installiert werden kann. So ist (fast) ausgeschlossen, dass Module für den O3-Shop 1.0 im O3-Shop 2.0 installiert werden, wenn dies dort nicht funktionieren würde.
  
- Modulinstallation

  Composer bietet Lösungen für technische Herausforderungen, die von Modulautoren gelöst werden müssen. Daher ist die Verwendung auch für Module ohne Alternative.
  
- Deployment

  Große Shopinstallationen stehen vor besonderen Herausforderungen wie planbare Updates mit möglichst kurzer Downtime. Composer ermöglicht das automatische Aufsetzen einer definierten Shopkonstellation inkl. aller Custom Plugins und Custom Themes und ist. Außerdem lässt sich der Ablauf auch in automatische ABläufe einbinden.
  
- Patch-fähig

  Composer erlaubt das updatesichere und wiederherstellbare Ändern von Codebestandteilen (z.B. im Rahmen eines Hotfix).
  
In Grenzen kann man die direkte Verwendung von Composer umgehen. Für Neu- und Testinstallationen bieten wir fertig zusammengesetzte Komplettpakete zum Download, die jedoch auf die genannten Vorteile verzichten.