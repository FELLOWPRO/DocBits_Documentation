# Table Extraction for costing Element

Navigieren Sie zu **Settings → Document Processing → Classification and Extraction**

<mark style="color:red;">**Hinweis:**</mark> Um die Tabellenextraktion für **Costing Elements** zu aktivieren, müssen Sie zunächst die entsprechende Costing-Element-Tabelle in **DocBits** importieren. Ohne diese Konfiguration werden Benutzer beim Öffnen eines Dokuments auf den folgenden Fehler stoßen:

_**„Costing elements are not properly configured. Please ask your admin to configure it."**_

## Schritte zum Import von Costing Elements aus M3

1. **Zugriff auf PPS280 in M3:**
   * Drücken Sie auf der M3-Startseite `Command + R` und suchen Sie nach **PPS280**.
   * Wählen Sie eine beliebige/alle Zeilen aus den Ergebnissen aus.
2. **Daten exportieren:**
   * Klicken Sie im nächsten Menü auf **TOOLS → Export to Excel**.\\
   * Wählen Sie **Export All Rows** und drücken Sie dann **EXPORT**.
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
   * **Vor der Änderung:**
   *   **Nach der Änderung:**

       <figure><img src="../../../.gitbook/assets/image (41) (1).png" alt=""><figcaption></figcaption></figure>
5. **In CSV konvertieren:**
   * Speichern Sie die geänderte Excel-Datei als `.csv`
6. **In DocBits hochladen:**

* Gehen Sie zu **Settings → Document Processing → Master Data Lookup**
* Klicken Sie auf das Plus neben „imported"
* Füllen Sie die erforderlichen Informationen aus
  * **Data Type**: `costing_element`
  * **File**: Wählen Sie Ihre geänderte `.csv`-Datei
  * **Delimiter**: `comma`
  * **On Conflict**: Wählen Sie eine Strategie zur Konfliktlösung
  * **Auto-generate ID**: Stellen Sie sicher, dass diese Option **aktiviert** ist\\
