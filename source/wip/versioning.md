# Versioning

The O3 shop consists of various **packages** that are assembled into a functional **compilation**. Each package has its own version number, independent of the other packages. We use a 3-part version number according to the scheme `Major.Minor.Patch`.

The version numbers are to be assigned strictly according to the principle of [semantic versioning](https://semver.org/spec/v2.0.0.html). In plain language this means

- **patch**: The right-hand version number stands exclusively for patch changes.

  This includes only bug fixes without changes to the code structure or new functions. The code of the new version should be fully compatible with the previous version. The update should be able to be installed without deep compatibility checks.
  
- **update**: The middle version place stands for changes on the minor level.

  This can contain small function changes, new functions or even clear structural changes. If error corrections require structural changes, these are also rolled out as minor updates.
  
- **upgrade**: The left version digit stands for changes at the major level.

  In an upgrade, more extensive structural changes or major comprehensive functional changes are included that do not have to be backwards compatible.
  
We have documented the compilations and major package versions under [...].

---

# Versionierung

Der O3-Shop besteht aus verschiedenen **Paketen**, die zu einer funktionsfähigen **Kompilation** zusammengestellt werden. Jedes Paket hat seine eigene, von den anderen Paketen unabhängige, Versionsnummer. Wir verwenden eine 3-teilige Versionsnummer nach dem Schema `Major.Minor.Patch`.

Die Versionsnummern sollen strikt nach dem Prinzip der [semantischen Versionierung](https://semver.org/spec/v2.0.0.html) vergeben werden. Im Klartext heißt dies:

- **Patch**: Die rechte Versionsstelle steht ausschließlich für Patchänderungen.

  Diese umfasst ausschließlich Fehlerkorrekturen ohne Änderung der Codestruktur oder neue Funktionen. Der Code der neuen Version soll vollständig mit der vorherigen Version kompatibel wird. Die Aktualisierung soll ohne tiefgreifende Kompatibilitätskontrolle installiert werden können.
  
- **Update**: Die mittlere Versionsstelle steht für Änderungen auf dem Minorlevel.

  Hierin können kleine Funktionänderungen, neue Funktionen oder auch übersichtliche Strukturänderungen enthalten sein. Wenn Fehlerkorrekturen Strukturänderungen erfordern, werden diese ebenfalls als Minorupdate ausgerollt.
  
- **Upgrade**: Die linke Versionsstelle steht für Änderungen auf dem Majorlevel.

  In einem Upgrade sind umfangreichere Strukturänderungen oder große umfassende Funktionsänderungen enthalten, die nicht rückwärtskompatibel sein müssen.
  
Die Kompilationen und wichtigsten Paketversionen haben wir unter [...] dokumentiert.