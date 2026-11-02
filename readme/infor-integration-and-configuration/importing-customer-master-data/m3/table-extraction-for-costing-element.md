# Tabellenextraktion für Costing Element

Navigieren Sie zu **Settings → Document Processing → Classification and Extraction**

<figure><img src="../../../.gitbook/assets/image (432).png" alt="Einstellungsseite Classification and Extraction in DocBits mit den Regelkarten Table Extraction, AI Table extraction und Table extraction for costing element"><figcaption></figcaption></figure>

<mark style="color:red;">**Hinweis:**</mark> Um die Tabellenextraktion für **Costing Elements** zu aktivieren, müssen Sie zunächst die entsprechende Costing-Element-Tabelle in **DocBits** importieren. Ohne diese Konfiguration werden Benutzer beim Öffnen eines Dokuments auf den folgenden Fehler stoßen:

_**„Costing elements are not properly configured. Please ask your admin to configure it."**_

## Schritte zum Import von Costing Elements aus M3

1. **Zugriff auf PPS280 in M3:**
   * Drücken Sie auf der M3-Startseite `Command + R` und suchen Sie nach **PPS280**.
   * Wählen Sie eine beliebige/alle Zeilen aus den Ergebnissen aus.
2. **Daten exportieren:**
   *   Klicken Sie im nächsten Menü auf **TOOLS → Export to Excel**.\\

       <figure><img src="../../../.gitbook/assets/image (433) (1).png" alt="M3-Bildschirm PPS280 Costing Element mit geöffnetem Tools-Menü, das Personalize, User Settings und Link Manager auflistet"><figcaption></figcaption></figure>
   *   Wählen Sie **Export All Rows** und drücken Sie dann **EXPORT**.

       <figure><img src="../../../.gitbook/assets/image (435) (1).png" alt="Dialog Export to Excel mit den Optionen Export currently selected rows und Export all rows, den Datenformat-Auswahlen und den Schaltflächen Export to Excel und Cancel"><figcaption></figcaption></figure>
3. **Excel-Datei bearbeiten:**\
   Öffnen Sie die heruntergeladene Excel-Datei und nehmen Sie die folgenden Änderungen vor:
   * **Spalten umbenennen:**
     * Spalte A → `costing_element`
     * Spalte B → `description`
     * Spalte H → `charge_operator`
     * Spalte J → `charge_type`
     * Spalte K → `distribution_method`
     * Spalte L → `distribution_type`
     * Spalte N → `charge_sequence_number`.
       * Geben Sie die entsprechenden Sequenznummern ein.
       * Wenn das Feld leer gelassen wird, verwendet das System standardmäßig **10**.
   * **Entfernen Sie alle anderen Spalten**, die **oben nicht aufgeführt sind**, auch wenn sie **Daten enthalten oder nicht leer sind**.
4. **Visuelles Beispiel – Vorher und Nachher:**\
   Nachfolgend finden Sie Beispiele der Excel-Datei _vor_ und _nach_ der Anwendung der erforderlichen Änderungen:
   *   **Vor der Änderung:**

       <figure><img src="../../../.gitbook/assets/image (4) (1) (1) (1) (1) (1) (1) (1) (1) (2).png" alt="Excel-Tabelle vor der Änderung mit den Spalten A bis N beginnend mit Elemnt Name und Zeilen mit Kostenträgerdaten"><figcaption></figcaption></figure>
   *   **Nach der Änderung:**

       <figure><img src="../../../.gitbook/assets/image (2) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1).png" alt="Settings menu panel with expandable configuration categories and toggle switches on the right side"><figcaption></figcaption></figure>
5. **In CSV konvertieren:**
   * Speichern Sie die geänderte Excel-Datei als `.csv`
6. **In DocBits hochladen:**

* Gehen Sie zu **Settings → Document Processing → Master Data Lookup**
*   Klicken Sie auf das Plus neben „imported"

    <figure><img src="../../../.gitbook/assets/image (437).png" alt="Seite „Master Data Lookup“ in DocBits mit dem Baum aus Input data, ERP API Data, Imported und DocBits Master Data"><figcaption></figcaption></figure>
* Füllen Sie die erforderlichen Informationen aus
  * **Data Type**: `costing_element`
  * **File**: Wählen Sie Ihre geänderte `.csv`-Datei
  * **Delimiter**: `comma`
  * **On Conflict**: Wählen Sie eine Strategie zur Konfliktlösung
  *   **Auto-generate ID**: Stellen Sie sicher, dass diese Option **aktiviert** ist\\

      <figure><img src="../../../.gitbook/assets/image (438) (1).png" alt="CSV-Upload-Dialog mit Data Type costing_element, der Datei Costing-Element_Modified.csv, Delimiter Komma, On Conflict REPLACE und Auto Generate Id"><figcaption></figcaption></figure>
