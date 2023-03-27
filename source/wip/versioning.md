# Versioning

The O3 shop consists of various **packages** that are assembled into a functional **compilation**. Each package has its own version number, independent of the other packages. We use a 3-part version number according to the scheme `Major.Minor.Patch`.

The version numbers are to be assigned strictly according to the principle of [semantic versioning](https://semver.org/spec/v2.0.0.html). In plain language this means

- **Patch**: The right-hand version number stands exclusively for API-compatible patch changes.

  This includes only bug fixes without changes to the code structure or new functions. The code of the new version should be fully compatible with the previous version. The update should be able to be installed without deep compatibility checks.
  
- **Update**: The middle version stands for changes at the minor level.

  This can contain function changes, new functions or API-compatible structural changes. If bug fixes require structural changes, these are also rolled out as minor updates.
  
- **Upgrade**: The version number on the left represents changes at the major level.

  In an upgrade, more extensive structural changes or major comprehensive function changes are included, which do not have to be backwards compatible. If technically necessary, these can also be bug fixes.

We have documented the compilations and major package versions in [compilation overview](compilation.md).

---

# Versionierung

Der O3-Shop besteht aus verschiedenen **Paketen**, die zu einer funktionsfähigen **Kompilation** zusammengestellt werden. Jedes Paket hat seine eigene, von den anderen Paketen unabhängige, Versionsnummer. Wir verwenden eine 3-teilige Versionsnummer nach dem Schema `Major.Minor.Patch`.

Die Versionsnummern sollen strikt nach dem Prinzip der [semantischen Versionierung](https://semver.org/spec/v2.0.0.html) vergeben werden. Im Klartext heißt dies:

- **Patch**: Die rechte Versionsstelle steht ausschließlich für API-kompatible Patchänderungen.

  Diese umfasst ausschließlich Fehlerkorrekturen ohne Änderung der Codestruktur oder neue Funktionen. Der Code der neuen Version soll vollständig mit der vorherigen Version kompatibel wird. Die Aktualisierung soll ohne tiefgreifende Kompatibilitätskontrolle installiert werden können.
  
- **Update**: Die mittlere Versionsstelle steht für Änderungen auf dem Minorlevel.

  Hierin können Funktionänderungen, neue Funktionen oder auch API-kompatible Strukturänderungen enthalten sein. Wenn Fehlerkorrekturen Strukturänderungen erfordern, werden diese ebenfalls als Minorupdate ausgerollt.
  
- **Upgrade**: Die linke Versionsstelle steht für Änderungen auf dem Majorlevel.

  In einem Upgrade sind umfangreichere Strukturänderungen oder große umfassende Funktionsänderungen enthalten, die nicht rückwärtskompatibel sein müssen. Sofern technisch nötig, können dies auch Fehlerkorrekturen sein.
  
Die Kompilationen und wichtigsten Paketversionen haben wir unter [Zusammenstellungsübersicht](compilation.md) dokumentiert.