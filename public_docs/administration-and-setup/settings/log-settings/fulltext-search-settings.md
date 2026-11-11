# Volltextsuche-Einstellungen

<figure><img src="../../../.gitbook/assets/fulltext_search_settings.png" alt="Volltextsuche-Einstellungen in der Sandbox mit einem Dialog, der das erforderliche Modul erklärt, und den Schaltflächen Go to Modules und Enable Now"><figcaption><p>Ist die Volltextsuche deaktiviert, erklärt dieser Dialog die nächsten Schritte.</p></figcaption></figure>

Die Volltextsuche-Einstellungen legen fest, was DocBits indexiert und wie diese Inhalte über Dokumente, ERP-Stammdaten und Vorlagen hinweg durchsuchbar werden. Die Einstellungsseite zeigt einen Anforderungsdialog, bis das **Fulltext Search module** aktiviert ist — die benutzerseitige Abfragesprache finden Sie unter [Fulltext Search](../document-processing/module/fulltext-search.md).

## Voraussetzungen

Das **Fulltext Search module** muss unter **Settings → Module → Dashboards & Analytics → Full text search** aktiviert sein. Ist das Modul nicht aktiviert, bietet der Dialog drei Aktionen:

* **Help (?)** — Öffnet die Volltextsuche-Dokumentation in einem neuen Tab, bevor Sie eine Einstellung ändern.
* **Go to Modules** — Öffnet die Moduleinstellungen von Dashboards & Analytics, um die Konfiguration zu prüfen.
* **Enable Now** — Öffnet den Abonnement-Dialog. Prüfen und bestätigen Sie diesen Dialog, bevor das Modul aktiviert wird; ein Klick auf diese Schaltfläche allein aktiviert es nicht.

Die Einstellungsseite selbst wird verfügbar, sobald das Modul aktiv ist.

## Aufbau der Seite

Die Einstellungsseite ist in drei Reiter gegliedert: **Documents**, **ERP** und **Templates**. Jeder Reiter umfasst einen anderen Inhaltstyp, den die Volltextsuche indexieren kann.

### Reiter Documents

Der Reiter Documents umfasst alles rund um die Indexierung verarbeiteter Dokumente:

* **Indexing statistics** — Summen für indexierte und ausstehende Dokumente, bei Bedarf aktualisiert.
* **Vector preferences** — drei organisationsweite Schalter, die steuern, ob die Vektorindexierung parallel zum Textindex für Dokumente läuft. Die Vektorindexierung ermöglicht den Abfragemodus `vector:` und die Funktion „Find Similar“.
* **Reindex actions** — startet eine vollständige oder inkrementelle Neuindexierung. Während eine Neuindexierung läuft, sehen Sie den Live-Fortschritt (Dokumente pro Minute, voraussichtliche Restzeit), den aktuellen Stream-Status und den letzten Fehler (falls vorhanden).
* **Sync diagnostics** — bei Bedarf abrufbare Diagnose für Fälle, in denen der Index nicht mit dem zugrunde liegenden Dokumentenspeicher übereinzustimmen scheint.

<mark>Die Neuindexierung ist nicht destruktiv — die bestehende Suche funktioniert weiter, während der neue Index aufgebaut wird.</mark>

### Reiter ERP

Der Reiter ERP steuert die Indexierung der ERP-Stammdaten — Lieferanten, Kunden, Artikel und ähnliche Entitäten. Jede Entität hat einen eigenen Schalter:

* **Indexing** — indexiert die Entität im Textindex, sodass sie im Dashboard durchsuchbar ist.
* **Vector** — indexiert die Entität im Vektorindex, sodass sie über semantische Abfragen gefunden werden kann.

Mit der Aktion **Toggle all** am Anfang der Liste wenden Sie denselben Ein-/Aus-Zustand gleichzeitig auf alle Entitäten an. Die Indexierung startet im Hintergrund; eine Anzeige in jeder Zeile zeigt an, wenn sie läuft.

### Reiter Templates

Der Reiter Templates listet die Vorlagenversionen, die dem Volltextindex bekannt sind. Mit dieser Ansicht bestätigen Sie nach einem erneuten Deployment, dass die von Ihnen genutzten Vorlagenversionen im Index vorhanden sind.

## Was indexiert wird

Sobald aktiviert und konfiguriert, ermöglicht die Volltextsuche:

* Die Suche über den gesamten Dokumentinhalt (nicht nur über Metadatenfelder).
* Das Auffinden von Dokumenten anhand von Text in hochgeladenen Dateien.
* Erweiterte Suchoperatoren für präzise Abfragen.
* Den direkten Zugriff auf Suchergebnisse aus dem Dashboard.
* Die semantische Suche (`vector:`-Präfix), wenn die Vektorindexierung für den jeweiligen Inhaltstyp aktiv ist.

Die vollständige Referenz der Abfragesprache — einschließlich Bereichsabfragen, intelligenter Filter und des KI-Suchmodus — finden Sie auf der Modulseite [Fulltext Search](../document-processing/module/fulltext-search.md).
