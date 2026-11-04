# M3 API Export Diagnoseleitfaden

### 1. Erstkonfiguration

Bevor Sie mit der Fehlerbehebung beginnen, stellen Sie sicher, dass Sie mit den erwarteten Eingaben für den M3-Endpunkt vertraut sind, mit dem Sie arbeiten.

#### 1.1 Zugriff auf M3 API-Dokumentation

* Melden Sie sich bei **M3** an.
* Gehen Sie zu **API-Bereich → API-Dokumentation**.
* Suchen und wählen Sie den relevanten Endpunkt aus (z. B. `APS450MI` für exportbezogene Rechnungen).
* Wählen Sie die entsprechende Funktion aus (z. B. `Hinzufügen`).

#### 1.2 API-Anforderungen verstehen

* Überprüfen Sie alle **erforderlichen Felder** in der API-Dokumentation.
* Achten Sie auf wichtige Felder wie:
  * `DIVI`
  * `ACDT` (Buchungsdatum)
  * `CUCD` (Währungscode)
  * `SINO` (Lieferantenrechnungsnummer)
* Bestätigen Sie die Feld **Datentypen**, **Groß-/Kleinschreibung** und **Formatierungsregeln** (z. B. `JJJJ-MM-TT` für Daten).

### 2. Testen von API-Aufrufen direkt in M3

Dieser Schritt überprüft, ob die M3-API mit manuellen Eingaben wie erwartet funktioniert.

#### 2.1 Generieren einer Testanfrage in M3

* Im M3-API-Dokumentationstool:
  * Füllen Sie Testdaten für erforderliche Felder aus.
  * Klicken Sie auf **Ausführen**, um die Anfrage auszuführen.
  * Kopieren Sie das resultierende **cURL** und **JSON-Body**.

#### 2.2 Debuggen mit Postman

* Öffnen Sie **Postman** und erstellen Sie eine neue **POST**-Anfrage.
* Fügen Sie den JSON-Body oder cURL ein.
* Fügen Sie erforderliche Header hinzu (z. B. Autorisierung).
* Klicken Sie auf **Senden** und beobachten Sie das Ergebnis:
  * `200 OK`: Die Anfrage war erfolgreich.
  * Fehler: Überprüfen Sie die Nachricht, um Details darüber zu erfahren, was schief gelaufen ist.

### 3. Vergleich von M3 API mit DocBits-Mapping

Nachdem Sie bestätigt haben, dass die API mit Testdaten funktioniert, vergleichen Sie sie mit dem, was DocBits tatsächlich sendet.

#### 3.1 Exportieren von Beispieldaten aus DocBits

*   Öffnen Sie die **DocBits API-Dokumentation**:

    Verwenden Sie den Endpunkt **/export/get\_infor\_export\_api\_json**.
* Geben Sie die **Dokumenten-ID** eines problematischen Dokuments ein.
* Führen Sie den Export durch, um die **JSON-Payload** anzuzeigen, die DocBits an M3 senden wird.

#### 3.2 Vergleich von API-Payloads

* Platzieren Sie das **M3-Test-JSON** und das **DocBits-Export-JSON** nebeneinander.
* Überprüfen Sie:
  * **Feldnamen**: Stellen Sie sicher, dass die Namen _genau_ übereinstimmen, einschließlich Groß-/Kleinschreibung (`DIVI` ≠ `divi`).
  * **Datentypen**: Überprüfen Sie, ob Zeichenfolgen, Zahlen und Daten ordnungsgemäß formatiert sind.
  * **Fehlende Felder**: Identifizieren Sie alle Felder, die in der Anfrage von M3 vorhanden sind, aber in DocBits fehlen.

### 4. Behebung häufiger Probleme

| Problem                             | Wahrscheinliche Ursache                                 | Lösung                                                                                     |
| ----------------------------------- | ------------------------------------------------------- | ------------------------------------------------------------------------------------------ |
| Fehlendes Feld                      | Ein erforderliches Feld ist in DocBits nicht zugeordnet | Fügen Sie das fehlende Feld in der DocBits-Exportkonfiguration hinzu.                      |
| Feld-Groß-/Kleinschreibung (`DIVI`) | M3 ist Groß-/Kleinschreibung-sensitiv                   | Verwenden Sie die richtige Groß-/Kleinschreibung in der Feldzuordnung.                     |
| Ungültiges `accountingDate`-Format  | Falsches oder fehlendes Datum                           | Passen Sie es an das von M3 erwartete Format an (z. B. `JJJJ-MM-TT`).                      |
| Unerwarteter API-Fehler             | Zusätzliche oder nicht erkannte Felder                  | Vergleichen Sie mit bekannten funktionierenden Payloads und bereinigen Sie unnötige Daten. |

### 5. Wenn Probleme bestehen bleiben

Wenn das Problem nach Durchführung der oben genannten Schritte nicht behoben ist:

1. **Dokumentieren** Sie das Problem:
   * Fehlermeldung und Statuscode
   * Beispiel M3-Anfrage und DocBits-Export-JSON
2. **Fassen** Sie Ihre Fehlerbehebung zusammen:
   * Was Sie versucht haben
   * Hauptunterschiede zwischen Test- und fehlerhaften Payloads beobachtet
3. **Eskalieren** Sie an einen Entwickler:
   * Fügen Sie alle Daten und Ergebnisse hinzu
   * Heben Sie vermutete Problemstellen hervor
