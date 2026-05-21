# Volltextsuche-Einstellungen

<figure><img src="../../../.gitbook/assets/fulltext_search_settings.png" alt="Volltextsuche-Einstellungen"><figcaption><p>Volltextsuche-Einstellungen — Dialog "Modul erforderlich"</p></figcaption></figure>

Die Volltextsuche-Einstellungen legen fest, was DocBits indexiert und wie diese Inhalte für die Suche über Dokumente, ERP-Stammdaten und Vorlagen hinweg verfügbar werden. Die Einstellungsseite öffnet sich nur, wenn das **Volltextsuche-Modul** aktiviert ist — siehe [Volltextsuche](../document-processing/module/fulltext-search.md) für die Suchsprache der Endbenutzer.

## Voraussetzungen

Das Volltextsuche-Modul muss unter **Einstellungen → Dokumentenverarbeitung → Modul → Dashboards → Volltextsuche** aktiviert sein. Ist das Modul deaktiviert, fragt ein Dialog ab, ob Sie:

* **Zu den Modulen** — Wechseln Sie zur Modul-Konfiguration, um die Einstellungen zu prüfen.
* **Jetzt aktivieren** — Aktivieren Sie das Volltextsuche-Modul direkt (startet ein DocSearch-Abonnement).

Die Einstellungsseite selbst wird erreichbar, sobald das Modul aktiv ist.

## Aufbau der Seite

Die Einstellungsseite ist in drei Reiter unterteilt, von denen jeder einen anderen Inhaltstyp behandelt, den die Volltextsuche indexieren kann.

### Reiter "Dokumente"

Der Reiter Dokumente betrifft alles rund um die Indexierung verarbeiteter Dokumente:

* **Indexierungs-Statistik** — Summen für indexierte und ausstehende Dokumente, manuell aktualisierbar.
* **Vektor-Einstellungen** — drei organisationsweite Schalter, die festlegen, ob die Vektor-Indexierung parallel zur Text-Indexierung läuft. Die Vektor-Indexierung versorgt den `vector:`-Suchmodus und die Funktion "Ähnliche finden".
* **Reindexierungs-Aktionen** — starten Sie eine vollständige oder inkrementelle Neuindexierung. Während die Neuindexierung läuft, sehen Sie den aktuellen Fortschritt (Dokumente pro Minute, voraussichtliche Restzeit), den Status des Streams und gegebenenfalls den letzten Fehler.
* **Synchronisierungs-Diagnose** — bei Bedarf abrufbare Diagnose für Fälle, in denen der Index nicht mit dem zugrunde liegenden Dokumentenspeicher übereinstimmt.

<mark>Die Neuindexierung ist nicht zerstörerisch — die bestehende Suche funktioniert weiter, während der neue Index aufgebaut wird.</mark>

### Reiter "ERP"

Der Reiter ERP steuert die Indexierung der ERP-Stammdaten — Lieferanten, Kunden, Artikel und ähnliche Entitäten. Jede Entität hat einen eigenen Schalter:

* **Indexierung** — die Entität wird textlich indexiert und ist im Dashboard durchsuchbar.
* **Vektor** — die Entität wird vektoriell indexiert und kann durch semantische Anfragen gefunden werden.

Über die Aktion **Alle umschalten** am Listenanfang lässt sich derselbe Ein/Aus-Zustand für alle Entitäten gleichzeitig anwenden. Die Indexierung läuft im Hintergrund; eine Anzeige pro Zeile zeigt den aktuellen Fortschritt.

### Reiter "Vorlagen"

Der Reiter Vorlagen listet die Vorlagen-Versionen, die dem Volltextindex bekannt sind. Diese Ansicht hilft, nach einem Redeploy zu bestätigen, dass die benötigten Vorlagen-Versionen im Index vorhanden sind.

## Was indexiert wird

Sobald aktiviert und konfiguriert, ermöglicht die Volltextsuche:

* Die Suche über den gesamten Inhalt eines Dokuments (nicht nur die Metadatenfelder).
* Das Auffinden von Dokumenten anhand von Text in den hochgeladenen Dateien.
* Erweiterte Suchoperatoren für präzise Anfragen.
* Den direkten Zugriff auf Suchergebnisse vom Dashboard aus.
* Semantische Suche (`vector:`-Präfix), wenn die Vektor-Indexierung für den jeweiligen Inhaltstyp aktiv ist.

Die vollständige Referenz der Suchsprache — einschließlich Bereichsabfragen, intelligenter Filter und KI-Suchmodus — finden Sie auf der Modul-Seite [Volltextsuche](../document-processing/module/fulltext-search.md).
