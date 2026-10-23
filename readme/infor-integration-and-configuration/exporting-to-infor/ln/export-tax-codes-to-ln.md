# Exportieren von Steuercodes nach LN

## **Übersicht:**

\
Dieser Leitfaden führt Sie durch den Einrichtungsprozess, um sicherzustellen, dass Steuercodes korrekt von DocBits nach LN exportiert werden.

## **Einzelne Steuercodes**

### **Schritt 1: Liste von Werten einrichten**

1.  Gehen Sie zu **Einstellungen** -> **Dokumentenverarbeitung** -> **Liste von Werten**.

    <figure><img src="../../../.gitbook/assets/site-extra-list-of-values-de.png" alt="Wertelisten in DocBits; organisationsbezogene Listennamen sind ausgeblendet."><figcaption><p>Wertelisten in DocBits; organisationsbezogene Listennamen sind ausgeblendet.</p></figcaption></figure>
2.  Klicken Sie auf **Neu**.

    <figure><img src="../../../.gitbook/assets/TaxCodes_2.png" alt="Seite List of Values mit hervorgehobener Schaltfläche New in der Symbolleiste"><figcaption></figcaption></figure>
3.  Erstellen Sie eine Liste mit dem Namen `Tax_Country` und klicken Sie auf **Speichern**.

    <figure><img src="../../../.gitbook/assets/TaxCodes_3.png" alt="Dialog New List of Values mit dem eingetragenen Namen Tax_Country und sichtbarer Schaltfläche Save" width="563"><figcaption></figcaption></figure>
4.  Erstellen Sie die folgenden drei zusätzlichen Listen:

    * `Tax_Code_Full`
    * `Tax_Code_Reduced`
    * `Tax_Code_Free`

    <div><figure><img src="../../../.gitbook/assets/TaxCodes_28.png" alt="Seite List of Values mit dem in der Liste erstellten Eintrag Tax_Code_Full"><figcaption></figcaption></figure> <figure><img src="../../../.gitbook/assets/TaxCodes_29.png" alt="List of Values-Seite mit dem in der Liste erstellten Eintrag Tax_Code_Reduced"><figcaption></figcaption></figure> <figure><img src="../../../.gitbook/assets/TaxCodes_30.png" alt="List of Values-Seite mit dem in der Liste erstellten Eintrag Tax_Code_Free"><figcaption></figcaption></figure></div>
5.  Klicken Sie auf eine der neu erstellten Listen, um sie zu öffnen. Drücken Sie dann die Schaltfläche **Zeile hinzufügen**, um eine neue Zeile hinzuzufügen.

    <figure><img src="../../../.gitbook/assets/TaxCode_4.png" alt="Seite List of Values für Tax_Country mit sichtbarer Schaltfläche Add Row in der Symbolleiste"><figcaption></figcaption></figure>
6.  Geben Sie die gewünschten jeweiligen Werte aus **LN** ein und drücken Sie **Speichern**, um die Änderungen zu speichern.

    * Wenn Sie mehrere Werte haben, können Sie auf **Weitere Werte hinzufügen** klicken, um diese hinzuzufügen.

    <div><figure><img src="../../../.gitbook/assets/TaxCodes_5.png" alt="Liste der Werte für Tax_Country mit einem neuen Zeileneintrag und der Schaltfläche Save"><figcaption></figcaption></figure> <figure><img src="../../../.gitbook/assets/site-extra-list-value-new-de.png" alt="Leerer deutscher Dialog zum Anlegen eines Listenwerts. Der tatsächliche Titel „Werte schaffen“ ist missverständlich; „Englisch“ bezeichnet die ausgewählte Übersetzungssprache. Es wurde nichts gespeichert."><figcaption><p>Leerer deutscher Dialog zum Anlegen eines Listenwerts. Der tatsächliche Titel „Werte schaffen“ ist missverständlich; „Englisch“ bezeichnet die ausgewählte Übersetzungssprache. Es wurde nichts gespeichert.</p></figcaption></figure></div>

    * **HINWEIS:** Sie finden die Steuercodes in LN unter: **Common** → **Taxation** → **Master Data** → **Tax Codes** → **Tax Codes by Country**

    <figure><img src="../../../.gitbook/assets/TaxCodes_LN.png" alt="Bildschirm LN Tax Codes by Country unter Common, Taxation, Master Data mit der Übersicht der Steuerkennzeichen"><figcaption></figcaption></figure>

### **Schritt 2: Felder in DocBits hinzufügen**

1.  Navigieren Sie zu **Einstellungen** -> **Globale Einstellungen** -> **Dokumenttypen**.

    <figure><img src="../../../.gitbook/assets/site-extra-document-types-de.png" alt="Dokumenttypen: Wählen Sie beim entsprechenden Typ die Felder. Es wurden keine Schalter verändert."><figcaption><p>Dokumenttypen: Wählen Sie beim entsprechenden Typ die Felder. Es wurden keine Schalter verändert.</p></figcaption></figure>
2.  Wählen Sie das Menü **Felder** für den Dokumenttyp, in dem Sie die Felder hinzufügen möchten.

    <figure><img src="../../../.gitbook/assets/docbits_docbits_image_8.png" alt="DocBits Bild"><figcaption></figcaption></figure>
3.  Unter **Mehrwertsteuer & Beträge** erstellen Sie sechs neue Felder wie folgt:

    <figure><img src="../../../.gitbook/assets/TaxCodes_8.png" alt="Seite der Feldeinstellungen für einen Dokumenttyp mit dem aufgeklappten Abschnitt VAT and Amounts"><figcaption></figcaption></figure>

<table data-header-hidden><thead><tr><th width="306"></th><th width="139"></th><th width="119"></th><th></th></tr></thead><tbody><tr><td><strong>Name</strong></td><td><strong>Titel</strong></td><td><strong>Feldtyp</strong></td><td><strong>Liste von Werten</strong></td></tr><tr><td><code>tax_country</code></td><td>Tax Country</td><td>Dropdown</td><td>Tax_Country</td></tr><tr><td><code>tax_country_2</code></td><td>Tax Country Reduced</td><td>Dropdown</td><td>Tax_Country</td></tr><tr><td><code>tax_country_3</code></td><td>Tax Country Free</td><td>Dropdown</td><td>Tax_Country</td></tr><tr><td><code>tax_code_without_country</code></td><td>Tax Code</td><td>Dropdown</td><td>Tax_Code_Full</td></tr><tr><td><code>tax_code_without_country_2</code></td><td>Tax Code Reduced</td><td>Dropdown</td><td>Tax_Code_Reduced</td></tr><tr><td><code>tax_code_without_country_3</code></td><td>Tax Code Free</td><td>Dropdown</td><td>Tax_Code_Free</td></tr></tbody></table>

<div><figure><img src="../../../.gitbook/assets/TaxCodes_10.png" alt="Seite „Fields settings“ mit dem neuen Dropdown-Feld Tax Country und der Liste der Werte Tax_Country"><figcaption></figcaption></figure> <figure><img src="../../../.gitbook/assets/TaxCodes_11.png" alt="Seite Fields settings mit dem neuen Dropdown-Feld Tax Country Reduced und der List of Values Tax_Country"><figcaption></figcaption></figure> <figure><img src="../../../.gitbook/assets/TaxCodes_12.png" alt="Seite der Feldeinstellungen mit dem neuen Dropdown-Feld Tax Country Free und der Liste der Werte Tax_Country"><figcaption></figcaption></figure></div>

<div><figure><img src="../../../.gitbook/assets/TaxCodes_13.png" alt="Seite Fields settings mit dem neuen Dropdown-Feld Tax Code und der List of Values Tax_Code_Full"><figcaption></figcaption></figure> <figure><img src="../../../.gitbook/assets/TaxCodes_14.png" alt="Seite Fields settings mit einem neuen Dropdown-Feld Tax Code Reduced und der List of Values Tax_Code_Reduced"><figcaption></figcaption></figure> <figure><img src="../../../.gitbook/assets/TaxCodes_15.png" alt="Seite Fields settings mit einem neuen Dropdown-Feld Tax Code Free und der List of Values Tax_Code_Free"><figcaption></figcaption></figure></div>

4.  Nach dem Speichern jedes Feldes klicken Sie auf **Einstellungen speichern**, um die Änderungen anzuwenden.

    <figure><img src="../../../.gitbook/assets/TaxCodes_20.png" alt="Seite Fields settings mit den neu erstellten Steuerfeldern und hervorgehobener Schaltfläche Save Settings"><figcaption></figcaption></figure>

### **Schritt 3: Layout bearbeiten**

1.  Gehen Sie zu **Einstellungen** -> **Globale Einstellungen** -> **Dokumenttypen**.

    <figure><img src="../../../.gitbook/assets/site-extra-document-types-de.png" alt="Dokumenttypen: Wählen Sie beim entsprechenden Typ die Felder. Es wurden keine Schalter verändert."><figcaption><p>Dokumenttypen: Wählen Sie beim entsprechenden Typ die Felder. Es wurden keine Schalter verändert.</p></figcaption></figure>
2.  Öffnen Sie das Menü **Layout bearbeiten** für den Dokumenttyp, den Sie bearbeiten möchten.

    <figure><img src="../../../.gitbook/assets/TaxCodes_19.png" alt="Seite Document Types mit geöffneter Option Edit Layout für einen Dokumenttyp im Menü"><figcaption></figcaption></figure>
3.  Wählen Sie die entsprechende **Dokumentenherkunft** aus, für die Sie die Steuercodes anwenden möchten.

    <figure><img src="../../../.gitbook/assets/TaxCodes_26.png" alt="Layout-Editor mit geöffnetem Dropdown Document Origin zur Auswahl des passenden Ursprungs"><figcaption></figcaption></figure>
4.  Scrollen Sie nach unten zum Abschnitt **Tax Details**.

    <figure><img src="../../../.gitbook/assets/TaxCodes_21.png" alt="Layout-Editor, nach unten zum Abschnitt Tax Details der Dokumentvorlage gescrollt"><figcaption></figcaption></figure>
5. Erweitern Sie das Dropdown-Menü **Form-Elemente**.
6.  Verwenden Sie im Abschnitt Tax Details den **Horizontal Separator**. Ziehen Sie ihn zwischen die Unterabschnitte in Tax Details, um diese klar zu trennen und es übersichtlich zu halten.

    <figure><img src="../../../.gitbook/assets/TaxCodes_22.png" alt="Layout-Editor mit aufgeklapptem Dropdownmenü Form Elements und hervorgehobenem Werkzeug Horizontal Separator"><figcaption></figcaption></figure>
7. Erweitern Sie das Dropdown-Menü **Felder**.
8.  Suchen Sie nach **Tax Country** und ziehen Sie das Feld in den entsprechenden Bereich.

    <figure><img src="../../../.gitbook/assets/TaxCodes_23.png" alt="Layout-Editor mit aufgeklapptem Dropdown Form Fields und der Suche nach dem Feld Tax Country"><figcaption></figcaption></figure>
9.  Suchen Sie nach **Tax Code** und ziehen Sie das Feld in den entsprechenden Bereich.

    <figure><img src="../../../.gitbook/assets/TaxCodes_24.png" alt="Layout-Editor mit erweitertem Dropdown Form Fields und laufender Suche nach dem Feld Tax Code"><figcaption></figcaption></figure>
10. Speichern Sie die Vorlage.

    <figure><img src="../../../.gitbook/assets/TaxCodes_25.png" alt="Layout-Editor mit hervorgehobener Schaltfläche Save nach dem Platzieren der Steuerfelder"><figcaption></figcaption></figure>

### Schritt 4: Überprüfen, ob alles funktioniert hat

Nachdem Sie ein neues Dokument in DocBits mit den ausgewählten korrekten Dokumenteneinstellungen hochgeladen haben, sollten Sie jetzt in der Lage sein, die Steuercodes auszuwählen, die Sie in Schritt 1 zu den Listen von Werten hinzugefügt haben.

<figure><img src="../../../.gitbook/assets/TaxCodes_31.png" alt="Validierungsbildschirm eines hochgeladenen Dokuments mit geöffneten Werten der Steuerkennzeichen-Dropdownliste"><figcaption></figcaption></figure>

## Mehrere Steuercodes

### **Schritt 1: Liste von Werten einrichten**

1.  Gehen Sie zu **Einstellungen** -> **Dokumentenverarbeitung** -> **Liste von Werten**.

    <figure><img src="../../../.gitbook/assets/site-extra-list-of-values-de.png" alt="Wertelisten in DocBits; organisationsbezogene Listennamen sind ausgeblendet."><figcaption><p>Wertelisten in DocBits; organisationsbezogene Listennamen sind ausgeblendet.</p></figcaption></figure>
2.  Klicken Sie auf **Neu**.

    <figure><img src="../../../.gitbook/assets/TaxCodes_2.png" alt="Seite List of Values mit hervorgehobener Schaltfläche New in der Symbolleiste"><figcaption></figcaption></figure>
3.  Erstellen Sie eine Liste mit dem Namen `Tax_Country` und klicken Sie auf **Speichern**.

    <figure><img src="../../../.gitbook/assets/TaxCodes_3.png" alt="Dialog New List of Values mit dem eingetragenen Namen Tax_Country und sichtbarer Schaltfläche Save" width="563"><figcaption></figcaption></figure>
4.  Erstellen Sie die folgenden drei zusätzlichen Listen:

    * `Tax_Code_Full`
    * `Tax_Code_Reduced`
    * `Tax_Code_Free`

    <div><figure><img src="../../../.gitbook/assets/TaxCodes_28.png" alt="Seite List of Values mit dem in der Liste erstellten Eintrag Tax_Code_Full"><figcaption></figcaption></figure> <figure><img src="../../../.gitbook/assets/TaxCodes_29.png" alt="List of Values-Seite mit dem in der Liste erstellten Eintrag Tax_Code_Reduced"><figcaption></figcaption></figure> <figure><img src="../../../.gitbook/assets/TaxCodes_30.png" alt="List of Values-Seite mit dem in der Liste erstellten Eintrag Tax_Code_Free"><figcaption></figcaption></figure></div>
5.  Klicken Sie auf eine der neu erstellten Listen, um sie zu öffnen. Drücken Sie dann die Schaltfläche **Zeile hinzufügen**, um eine neue Zeile hinzuzufügen.

    <figure><img src="../../../.gitbook/assets/TaxCode_4.png" alt="Seite List of Values für Tax_Country mit sichtbarer Schaltfläche Add Row in der Symbolleiste"><figcaption></figcaption></figure>
6.  Geben Sie die gewünschten jeweiligen Werte aus **LN** ein und drücken Sie **Speichern**, um die Änderungen zu speichern.

    * Wenn Sie mehrere Werte haben, können Sie auf **Weitere Werte hinzufügen** klicken, um diese hinzuzufügen.

    <div><figure><img src="../../../.gitbook/assets/TaxCodes_5.png" alt="Liste der Werte für Tax_Country mit einem neuen Zeileneintrag und der Schaltfläche Save"><figcaption></figcaption></figure> <figure><img src="../../../.gitbook/assets/site-extra-list-value-new-de.png" alt="Leerer deutscher Dialog zum Anlegen eines Listenwerts. Der tatsächliche Titel „Werte schaffen“ ist missverständlich; „Englisch“ bezeichnet die ausgewählte Übersetzungssprache. Es wurde nichts gespeichert."><figcaption><p>Leerer deutscher Dialog zum Anlegen eines Listenwerts. Der tatsächliche Titel „Werte schaffen“ ist missverständlich; „Englisch“ bezeichnet die ausgewählte Übersetzungssprache. Es wurde nichts gespeichert.</p></figcaption></figure></div>

    * **HINWEIS:** Sie finden die Steuercodes in LN unter: **Common** → **Taxation** → **Master Data** → **Tax Codes** → **Tax Codes by Country**

    <figure><img src="../../../.gitbook/assets/TaxCodes_LN.png" alt="Bildschirm LN Tax Codes by Country unter Common, Taxation, Master Data mit der Übersicht der Steuerkennzeichen"><figcaption></figcaption></figure>

### **Schritt 2: Felder in DocBits hinzufügen**

1.  Navigieren Sie zu **Einstellungen** -> **Globale Einstellungen** -> **Dokumenttypen**.

    <figure><img src="../../../.gitbook/assets/site-extra-document-types-de.png" alt="Dokumenttypen: Wählen Sie beim entsprechenden Typ die Felder. Es wurden keine Schalter verändert."><figcaption><p>Dokumenttypen: Wählen Sie beim entsprechenden Typ die Felder. Es wurden keine Schalter verändert.</p></figcaption></figure>
2.  Wählen Sie das Menü **Felder** für den Dokumenttyp, in dem Sie die Felder hinzufügen möchten.

    <figure><img src="../../../.gitbook/assets/docbits_docbits_image_8.png" alt="DocBits Bild"><figcaption></figcaption></figure>
3.  Unter **Mehrwertsteuer & Beträge** erstellen Sie sechs neue Felder wie folgt:

    <figure><img src="../../../.gitbook/assets/TaxCodes_8.png" alt="Seite der Feldeinstellungen für einen Dokumenttyp mit dem aufgeklappten Abschnitt VAT and Amounts"><figcaption></figcaption></figure>

<table data-header-hidden><thead><tr><th width="306"></th><th width="139"></th><th width="119"></th><th></th></tr></thead><tbody><tr><td><strong>Name</strong></td><td><strong>Titel</strong></td><td><strong>Feldtyp</strong></td><td><strong>Liste von Werten</strong></td></tr><tr><td><code>tax_country</code></td><td>Tax Country</td><td>Dropdown</td><td>Tax_Country</td></tr><tr><td><code>tax_country_2</code></td><td>Tax Country Reduced</td><td>Dropdown</td><td>Tax_Country</td></tr><tr><td><code>tax_country_3</code></td><td>Tax Country Free</td><td>Dropdown</td><td>Tax_Country</td></tr><tr><td><code>tax_code_without_country</code></td><td>Tax Code</td><td>Dropdown</td><td>Tax_Code_Full</td></tr><tr><td><code>tax_code_without_country_2</code></td><td>Tax Code Reduced</td><td>Dropdown</td><td>Tax_Code_Reduced</td></tr><tr><td><code>tax_code_without_country_3</code></td><td>Tax Code Free</td><td>Dropdown</td><td>Tax_Code_Free</td></tr></tbody></table>

<div><figure><img src="../../../.gitbook/assets/TaxCodes_13.png" alt="Seite Fields settings mit dem neuen Dropdown-Feld Tax Code und der List of Values Tax_Code_Full"><figcaption></figcaption></figure> <figure><img src="../../../.gitbook/assets/TaxCodes_11.png" alt="Seite Fields settings mit dem neuen Dropdown-Feld Tax Country Reduced und der List of Values Tax_Country"><figcaption></figcaption></figure> <figure><img src="../../../.gitbook/assets/TaxCodes_12.png" alt="Seite der Feldeinstellungen mit dem neuen Dropdown-Feld Tax Country Free und der Liste der Werte Tax_Country"><figcaption></figcaption></figure></div>

<div><figure><img src="../../../.gitbook/assets/TaxCodes_10.png" alt="Seite „Fields settings“ mit dem neuen Dropdown-Feld Tax Country und der Liste der Werte Tax_Country"><figcaption></figcaption></figure> <figure><img src="../../../.gitbook/assets/TaxCodes_14.png" alt="Seite Fields settings mit einem neuen Dropdown-Feld Tax Code Reduced und der List of Values Tax_Code_Reduced"><figcaption></figcaption></figure> <figure><img src="../../../.gitbook/assets/TaxCodes_15.png" alt="Seite Fields settings mit einem neuen Dropdown-Feld Tax Code Free und der List of Values Tax_Code_Free"><figcaption></figcaption></figure></div>

4.  Nach dem Speichern jedes Feldes klicken Sie auf **Einstellungen speichern**, um die Änderungen anzuwenden.

    <figure><img src="../../../.gitbook/assets/TaxCodes_20.png" alt="Seite Fields settings mit den neu erstellten Steuerfeldern und hervorgehobener Schaltfläche Save Settings"><figcaption></figcaption></figure>

### **Schritt 3: Layout bearbeiten**

1.  Gehen Sie zu **Einstellungen** -> **Globale Einstellungen** -> **Dokumenttypen**.

    <figure><img src="../../../.gitbook/assets/site-extra-document-types-de.png" alt="Dokumenttypen: Wählen Sie beim entsprechenden Typ die Felder. Es wurden keine Schalter verändert."><figcaption><p>Dokumenttypen: Wählen Sie beim entsprechenden Typ die Felder. Es wurden keine Schalter verändert.</p></figcaption></figure>
2.  Öffnen Sie das Menü **Layout bearbeiten** für den Dokumenttyp, den Sie bearbeiten möchten.

    <figure><img src="../../../.gitbook/assets/TaxCodes_19.png" alt="Seite Document Types mit geöffneter Option Edit Layout für einen Dokumenttyp im Menü"><figcaption></figcaption></figure>
3.  Wählen Sie die entsprechende **Dokumentenherkunft** aus, für die Sie die Steuercodes anwenden möchten.

    <figure><img src="../../../.gitbook/assets/TaxCodes_26.png" alt="Layout-Editor mit geöffnetem Dropdown Document Origin zur Auswahl des passenden Ursprungs"><figcaption></figcaption></figure>
4.  Scrollen Sie nach unten zum Abschnitt **Tax Details**.

    <figure><img src="../../../.gitbook/assets/TaxCodes_21.png" alt="Layout-Editor, nach unten zum Abschnitt Tax Details der Dokumentvorlage gescrollt"><figcaption></figcaption></figure>
5. Erweitern Sie das Dropdown-Menü **Form-Elemente**.
6.  Verwenden Sie im Abschnitt Steuerdetails das **Sub Group** Werkzeug. Ziehen Sie es neben ein vorhandenes Feld.

    <figure><img src="../../../.gitbook/assets/TaxCodesMulti_1.png" alt="Layout-Editor mit ausgeklapptem Dropdown Form Elements und hervorgehobenem Werkzeug Sub Group"><figcaption></figcaption></figure>
7.  Um Ihrer Sub Group einen Namen zu geben, klicken Sie auf die Sub Group und geben Sie den gewünschten Namen im Feld **Label** ein.

    <div><figure><img src="../../../.gitbook/assets/TaxCodesMulti_2.png" alt="Layout-Editor mit einem neu hinzugefügten, ausgewählten Sub-Group-Element im Abschnitt Tax Details"><figcaption></figcaption></figure> <figure><img src="../../../.gitbook/assets/TaxCodesMulti_3.png" alt="Layout-Editor mit geöffnetem Label-Feld der ausgewählten Sub Group zum Benennen"><figcaption></figcaption></figure></div>
8.  Ziehen Sie die Felder, die zu dieser Gruppe gehören, in das **Sub Group** Feld.

    <figure><img src="../../../.gitbook/assets/TaxCodeMulti_4.png" alt="Layout-Editor, in dem ein Feld in die neue Untergruppe im Abschnitt Tax Details gezogen wird"><figcaption></figcaption></figure>
9. Erweitern Sie das Dropdown-Menü **Felder**.
10. Suchen Sie nach **Tax** und ziehen Sie die entsprechenden Felder, wie **Tax Country** und **Tax Code**, in die entsprechende Sub Group.

    <figure><img src="../../../.gitbook/assets/TaxCodeMulti_5.png" alt="Layout-Editor mit aufgeklappter Fields-Dropdownliste und Suche nach dem Feld Tax Country"><figcaption></figcaption></figure>
11. Wiederholen Sie die Schritte 5 bis 10 zwei Mal, um den folgenden Zustand zu erreichen:

    <figure><img src="../../../.gitbook/assets/TaxCodeMulti_6.png" alt="Layout-Editor mit der Steuer-Untergruppe im Abschnitt Tax Details nach dem Wiederholen der Schritte"><figcaption></figcaption></figure>
12. Speichern Sie die Vorlage.

    <figure><img src="../../../.gitbook/assets/TaxCodeMulti_7.png" alt="Layout-Editor mit hervorgehobener Schaltfläche Save nach dem Anordnen der Steuer-Untergruppen"><figcaption></figcaption></figure>

### Schritt 4: Überprüfen, ob alles funktioniert hat und die resultierenden Änderungen

Nachdem Sie ein neues Dokument in DocBits mit den ausgewählten korrekten Dokumenteneinstellungen hochgeladen haben, können Sie die Steuercodes auswählen, die Sie in Schritt 1 hinzugefügt haben, und mehrere Steuercodes hinzufügen, die in Schritt 3 konfiguriert wurden.

* Das Dokument beginnt mit drei verschiedenen Abschnitten: einem für Steuerbeträge voll, einem für Steuerbeträge reduziert und einem für Steuerbeträge frei.
* Durch Klicken auf die Plus-Schaltfläche innerhalb eines Abschnitts wird eine Duplikation erstellt, die mehrere Einreichungen zum ausgewählten Steuersatz ermöglicht.

<figure><img src="../../../.gitbook/assets/TaxCodeMulti_8.png" alt="Validierungsbildschirm eines hochgeladenen Dokuments mit den Steuerabschnitten und der Plus-Schaltfläche"><figcaption></figcaption></figure>

* Abschnitte können durch Klicken auf die Entfernen-Schaltfläche gelöscht werden.

<figure><img src="../../../.gitbook/assets/TaxCodeMulti_9.png" alt="Validierungsbildschirm eines hochgeladenen Dokuments mit einem Steuerbereich und hervorgehobener Entfernen-Schaltfläche"><figcaption></figcaption></figure>

* Gesamtbeträge werden als Summe aller Abschnitte berechnet.
* Die Validierung des Gesamtbetrags wird basierend auf allen Steuerabschnitten geändert.
* Skripte für neue Abschnitte können nur angewendet werden, nachdem Felder zur Ansicht hinzugefügt wurden.

### Hinweis für LN:

In **LN** wird die USt-Position basierend auf der Positionsnummer aus dem Dropdown-Menü Steuercode/Steuerland ausgefüllt. Nur die Positionsnummer wird zum Export gesendet.

<figure><img src="../../../.gitbook/assets/TaxCodesLN_2.png" alt="LN-Bildschirm mit dem anhand der Positionsnummer des Steuerkodes ausgefüllten Feld USt Position"><figcaption></figcaption></figure>

<figure><img src="../../../.gitbook/assets/TaxCodesLN_3.png" alt="LN-Bildschirm mit der exportierten Rechnung und dem ausgefüllten Wert USt Position"><figcaption></figcaption></figure>

#### **Export-Mapping**

Um die Steuerzeile mit der Kostenzeile zu verknüpfen:

1. Fügen Sie `TaxLine` zur Liste **InvoiceCostFields** hinzu.
2. Fügen Sie den folgenden Eintrag hinzu, der dem Beispiel unten folgt:\
   `ICF_TaxLine = TF_position`

<figure><img src="../../../.gitbook/assets/TaxCodeMulti_10.png" alt="List of Values von InvoiceCostFields mit dem Eintrag TaxLine und dem Mapping ICF_TaxLine"><figcaption></figcaption></figure>
