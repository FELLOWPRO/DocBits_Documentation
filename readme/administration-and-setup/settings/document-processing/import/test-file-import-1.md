# Test: Dateiimport 1

## Zweck

Diese Tests prüfen den Import von PDF- und TIFF-Dateien. Sie stellen sicher, dass die Dateien erfolgreich verarbeitet und gespeichert werden.

#### Testvorbereitung und Bereinigung

* **Vorbereitung:** Vor jedem Test wird eine Vorbereitungsmeldung protokolliert.
* **Bereinigung:** Nach jedem Test werden alle vom Testbenutzer erstellten Dokumente aus der Datenbank gelöscht. Dadurch beeinflussen keine zurückgebliebenen Daten die nachfolgenden Tests.

#### Testszenarien

1. **PDF-Datei importieren:**
   * **PDF-Import testen (`test_import_pdf`):** Die Datei `FellowBananaInvoice.pdf` ins System importieren.
   * **Erwartetes Ergebnis:** Die Datei wird erfolgreich importiert; eine Dokument-ID wird zurückgegeben.
2. **TIFF-Datei importieren:**
   * **TIFF-Import testen (`test_import_tiff`):** Die Datei `TIFF_FILE.TIF` ins System importieren.
   * **Erwartetes Ergebnis:** Die Datei wird erfolgreich importiert; eine Dokument-ID wird zurückgegeben.

## Erläuterung der einzelnen Tests

* **Vorbereitung und Bereinigung:**
  * Für jeden Test werden Vorbereitungs- und Bereinigungsmeldungen protokolliert.
  * Die Datenbankbereinigung (`clean_documents`) löscht alle vom Testbenutzer erstellten Dokumente, um einen sauberen Ausgangszustand herzustellen.
* **Dateiimporttests:**

  **PDF-Datei importieren:**
  * Den Testbenutzer laden.
  * Den Dateipfad `tests/files/pdfs/FellowBananaInvoice.pdf` festlegen.
  * Die PDF-Datei mit der Klasse `FileImporter` importieren.
  * Prüfen, ob die Antwort eine Liste mit Erfolgsmeldung und Dokument-ID ist.

  **TIFF-Datei importieren:**
  * Den Testbenutzer laden.
  * Den Dateipfad `tests/files/pdfs/TIFF_FILE.TIF` festlegen.
  * Die TIFF-Datei mit der Klasse `FileImporter` importieren.
  * Prüfen, ob die Antwort eine Liste mit Erfolgsmeldung und Dokument-ID ist.

## Codestruktur

* **Logger:** Protokolliert Debugmeldungen während Vorbereitung, Bereinigung und Testausführung.
* **Datenbankhelfer:** Führt für die Bereinigung Abfragen ohne Rückgabewerte aus.
* **Dateiimporter:** Übernimmt den Import der Dateien ins System.
* **Fixtures:** Die Fixture `set_up` verwaltet Vorbereitung und Bereinigung der Tests.
* **Tests:**
  * `test_import_pdf`: Prüft den Import einer PDF-Datei.
  * `test_import_tiff`: Prüft den Import einer TIFF-Datei.

#### Zusammenfassung

Die Tests prüfen, ob PDF- und TIFF-Dateien korrekt importiert werden und die Dateiimportfunktion unterschiedliche Dateitypen verarbeiten kann.
