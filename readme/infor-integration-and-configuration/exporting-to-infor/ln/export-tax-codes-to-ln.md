# Exportieren von Steuercodes nach LN

## **Übersicht:**

\
Dieser Leitfaden führt Sie durch den Einrichtungsprozess, um sicherzustellen, dass Steuercodes korrekt von DocBits nach LN exportiert werden.

## **Einzelne Steuercodes**

### **Schritt 1: Liste von Werten einrichten**

1.  Gehen Sie zu **Einstellungen** -> **Dokumentenverarbeitung** -> **Liste von Werten**.

    <figure><img src="../../../.gitbook/assets/TaxCodes_1.png" alt="Geöffnetes Einstellungen-Menü mit dem Bereich Dokumentenverarbeitung und dem Eintrag Liste von Werten"><figcaption>Einstellungen: Dokumentenverarbeitung > Liste von Werten</figcaption></figure>
2.  Klicken Sie auf **Neu**.

    <figure><img src="../../../.gitbook/assets/TaxCodes_2.png" alt="Seite Liste von Werten mit den vorhandenen Listen und der Schaltfläche Neu"><figcaption>Liste von Werten mit den vorhandenen Listen</figcaption></figure>
3.  Erstellen Sie eine Liste mit dem Namen `Tax_Country` und klicken Sie auf **Speichern**.

    <figure><img src="../../../.gitbook/assets/TaxCodes_3.png" alt="Dialog Neue Liste mit dem Namen Tax_Country" width="563"><figcaption>Liste Tax_Country anlegen</figcaption></figure>
4.  Erstellen Sie die folgenden drei zusätzlichen Listen:

    * `Tax_Code_Full`
    * `Tax_Code_Reduced`
    * `Tax_Code_Free`

    <div><figure><img src="../../../.gitbook/assets/TaxCodes_28.png" alt="Dialog Neue Liste mit dem Namen Tax_Code_Full"><figcaption>Liste Tax_Code_Full anlegen</figcaption></figure> <figure><img src="../../../.gitbook/assets/TaxCodes_29.png" alt="Dialog Neue Liste mit dem Namen Tax_Code_Reduced"><figcaption>Liste Tax_Code_Reduced anlegen</figcaption></figure> <figure><img src="../../../.gitbook/assets/TaxCodes_30.png" alt="Dialog Neue Liste mit dem Namen Tax_Code_Free"><figcaption>Liste Tax_Code_Free anlegen</figcaption></figure></div>
5.  Klicken Sie auf eine der neu erstellten Listen, um sie zu öffnen. Drücken Sie dann die Schaltfläche **Zeile hinzufügen**, um eine neue Zeile hinzuzufügen.

    <figure><img src="../../../.gitbook/assets/TaxCode_4.png" alt="Seite Liste von Werten mit der Schaltfläche Zeile hinzufügen unter der geöffneten Liste"><figcaption>Eine Zeile zur geöffneten Liste hinzufügen</figcaption></figure>
6.  Geben Sie die gewünschten jeweiligen Werte aus **LN** ein und drücken Sie **Speichern**, um die Änderungen zu speichern.

    * Wenn Sie mehrere Werte haben, können Sie auf **Weitere Werte hinzufügen** klicken, um diese hinzuzufügen.

    <div><figure><img src="../../../.gitbook/assets/TaxCodes_5.png" alt="Dialog Werte anlegen mit einem eingetragenen LN-Steuercode im Feld Name"><figcaption>LN-Steuercode im Feld Name eintragen</figcaption></figure> <figure><img src="../../../.gitbook/assets/TaxCodes_27.png" alt="Dialog Werte anlegen mit dem über Weitere Werte hinzugefügten Wert 800"><figcaption>Zweiten Wert über Weitere Werte hinzufügen</figcaption></figure></div>

    * **HINWEIS:** Sie finden die Steuercodes in LN unter: **Common** → **Taxation** → **Master Data** → **Tax Codes** → **Tax Codes by Country**

    <figure><img src="../../../.gitbook/assets/TaxCodes_LN.png" alt="Infor LN, Sitzung Steuercodes nach Land für Österreich mit den Spalten Steuercode und Steuerart"><figcaption>LN: Common > Taxation > Master Data > Tax Codes > Tax Codes by Country</figcaption></figure>

### **Schritt 2: Felder in DocBits hinzufügen**

1.  Navigieren Sie zu **Einstellungen** -> **Globale Einstellungen** -> **Dokumenttypen**.

    <figure><img src="../../../.gitbook/assets/TaxCodes_6.png" alt="Geöffnetes Menü Globale Einstellungen mit dem Eintrag Dokumenttypen"><figcaption>Einstellungen: Globale Einstellungen > Dokumenttypen</figcaption></figure>
2.  Wählen Sie das Menü **Felder** für den Dokumenttyp, in dem Sie die Felder hinzufügen möchten.

    <figure><img src="../../../.gitbook/assets/docbits_docbits_image_8.png" alt="Seite Dokumenttypen mit dem Menü Felder unter jedem Dokumenttyp"><figcaption>Menü Felder des Dokumenttyps öffnen</figcaption></figure>
3.  Unter **Mehrwertsteuer & Beträge** erstellen Sie sechs neue Felder wie folgt:

    <figure><img src="../../../.gitbook/assets/TaxCodes_8.png" alt="Registerkarte Felder mit der Gruppe Mehrwertsteuer &amp; Beträge und der Schaltfläche Neu erstellen"><figcaption>Registerkarte Felder: Gruppe Mehrwertsteuer &amp; Beträge</figcaption></figure>

<table data-header-hidden><thead><tr><th width="306"></th><th width="139"></th><th width="119"></th><th></th></tr></thead><tbody><tr><td><strong>Name</strong></td><td><strong>Titel</strong></td><td><strong>Feldtyp</strong></td><td><strong>Liste von Werten</strong></td></tr><tr><td><code>tax_country</code></td><td>Tax Country</td><td>Dropdown</td><td>Tax_Country</td></tr><tr><td><code>tax_country_2</code></td><td>Tax Country Reduced</td><td>Dropdown</td><td>Tax_Country</td></tr><tr><td><code>tax_country_3</code></td><td>Tax Country Free</td><td>Dropdown</td><td>Tax_Country</td></tr><tr><td><code>tax_code_without_country</code></td><td>Tax Code</td><td>Dropdown</td><td>Tax_Code_Full</td></tr><tr><td><code>tax_code_without_country_2</code></td><td>Tax Code Reduced</td><td>Dropdown</td><td>Tax_Code_Reduced</td></tr><tr><td><code>tax_code_without_country_3</code></td><td>Tax Code Free</td><td>Dropdown</td><td>Tax_Code_Free</td></tr></tbody></table>

<div><figure><img src="../../../.gitbook/assets/TaxCodes_10.png" alt="Dialog Dokumentfelddetails für tax_country mit Feldtyp Dropdown und Liste Tax_Country"><figcaption>Feld tax_country: Dropdown, Liste Tax_Country</figcaption></figure> <figure><img src="../../../.gitbook/assets/TaxCodes_11.png" alt="Dialog Dokumentfelddetails für tax_country_2 mit Titel Tax Country Reduced"><figcaption>Feld tax_country_2: Dropdown, Liste Tax_Country</figcaption></figure> <figure><img src="../../../.gitbook/assets/TaxCodes_12.png" alt="Dialog Dokumentfelddetails für tax_country_3 mit Titel Tax Country Free"><figcaption>Feld tax_country_3: Dropdown, Liste Tax_Country</figcaption></figure></div>

<div><figure><img src="../../../.gitbook/assets/TaxCodes_13.png" alt="Dialog Dokumentfelddetails für tax_code_without_country mit Liste Tax_Code_Full"><figcaption>Feld tax_code_without_country: Dropdown, Liste Tax_Code_Full</figcaption></figure> <figure><img src="../../../.gitbook/assets/TaxCodes_14.png" alt="Dialog Dokumentfelddetails für tax_code_without_country_2 mit Liste Tax_Code_Reduced"><figcaption>Feld tax_code_without_country_2: Dropdown, Liste Tax_Code_Reduced</figcaption></figure> <figure><img src="../../../.gitbook/assets/TaxCodes_15.png" alt="Dialog Dokumentfelddetails für tax_code_without_country_3 mit Liste Tax_Code_Free"><figcaption>Feld tax_code_without_country_3: Dropdown, Liste Tax_Code_Free</figcaption></figure></div>

4.  Nach dem Speichern jedes Feldes klicken Sie auf **Einstellungen speichern**, um die Änderungen anzuwenden.

    <figure><img src="../../../.gitbook/assets/TaxCodes_20.png" alt="Registerkarte Felder mit der Schaltfläche Einstellungen speichern über der Feldliste"><figcaption>Einstellungen speichern, um die neuen Felder zu übernehmen</figcaption></figure>

### **Schritt 3: Layout bearbeiten**

1.  Gehen Sie zu **Einstellungen** -> **Globale Einstellungen** -> **Dokumenttypen**.

    <figure><img src="../../../.gitbook/assets/TaxCodes_6.png" alt="Geöffnetes Menü Globale Einstellungen mit dem Eintrag Dokumenttypen"><figcaption>Einstellungen: Globale Einstellungen > Dokumenttypen</figcaption></figure>
2.  Öffnen Sie das Menü **Layout bearbeiten** für den Dokumenttyp, den Sie bearbeiten möchten.

    <figure><img src="../../../.gitbook/assets/TaxCodes_19.png" alt="Seite Dokumenttypen mit dem Link Layout bearbeiten unter jedem Dokumenttyp"><figcaption>Layout bearbeiten des Dokumenttyps öffnen</figcaption></figure>
3.  Wählen Sie die entsprechende **Dokumentenherkunft** aus, für die Sie die Steuercodes anwenden möchten.

    <figure><img src="../../../.gitbook/assets/TaxCodes_26.png" alt="Layout-Builder mit der Auswahl des Dokumentursprungs und der Werkzeugleiste der Vorlage"><figcaption>Layout-Builder: Dokumentursprung auswählen</figcaption></figure>
4.  Scrollen Sie nach unten zum Abschnitt **Tax Details**.

    <figure><img src="../../../.gitbook/assets/TaxCodes_21.png" alt="Layout-Builder mit der Gruppe Steuerdetails und ihren Feldern im Elementbaum"><figcaption>Zur Gruppe Steuerdetails scrollen</figcaption></figure>
5. Erweitern Sie das Dropdown-Menü **Form-Elemente**.
6.  Verwenden Sie im Abschnitt Tax Details den **Horizontal Separator**. Ziehen Sie ihn zwischen die Unterabschnitte in Tax Details, um diese klar zu trennen und es übersichtlich zu halten.

    <figure><img src="../../../.gitbook/assets/TaxCodes_22.png" alt="Layout-Builder mit aufgeklappter Auswahl Formularelemente"><figcaption>Formularelemente aufklappen</figcaption></figure>
7. Erweitern Sie das Dropdown-Menü **Felder**.
8.  Suchen Sie nach **Tax Country** und ziehen Sie das Feld in den entsprechenden Bereich.

    <figure><img src="../../../.gitbook/assets/TaxCodes_23.png" alt="Layout-Builder mit dem in den Bereich Steuerdetails gezogenen Feld Tax Country"><figcaption>Tax Country in den Bereich Steuerdetails ziehen</figcaption></figure>
9.  Suchen Sie nach **Tax Code** und ziehen Sie das Feld in den entsprechenden Bereich.

    <figure><img src="../../../.gitbook/assets/TaxCodes_24.png" alt="Layout-Builder mit dem unter Tax Country abgelegten Feld Tax Code"><figcaption>Tax Code in den Bereich Steuerdetails ziehen</figcaption></figure>
10. Speichern Sie die Vorlage.

    <figure><img src="../../../.gitbook/assets/TaxCodes_25.png" alt="Layout-Builder mit gespeicherter Vorlage und beiden Steuerfeldern in der Gruppe Steuerdetails"><figcaption>Gespeicherte Vorlage mit beiden Steuerfeldern</figcaption></figure>

### Schritt 4: Überprüfen, ob alles funktioniert hat

Nachdem Sie ein neues Dokument in DocBits mit den ausgewählten korrekten Dokumenteneinstellungen hochgeladen haben, sollten Sie jetzt in der Lage sein, die Steuercodes auszuwählen, die Sie in Schritt 1 zu den Listen von Werten hinzugefügt haben.

<figure><img src="../../../.gitbook/assets/TaxCodes_31.png" alt="Feldprüfung einer Rechnung mit ausgefüllten Auswahllisten Tax Country und Tax Code"><figcaption>Die neuen Auswahllisten in der Feldprüfung</figcaption></figure>

## Mehrere Steuercodes

### **Schritt 1: Liste von Werten einrichten**

1.  Gehen Sie zu **Einstellungen** -> **Dokumentenverarbeitung** -> **Liste von Werten**.

    <figure><img src="../../../.gitbook/assets/TaxCodes_1.png" alt="Geöffnetes Einstellungen-Menü mit dem Bereich Dokumentenverarbeitung und dem Eintrag Liste von Werten"><figcaption>Einstellungen: Dokumentenverarbeitung > Liste von Werten</figcaption></figure>
2.  Klicken Sie auf **Neu**.

    <figure><img src="../../../.gitbook/assets/TaxCodes_2.png" alt="Seite Liste von Werten mit den vorhandenen Listen und der Schaltfläche Neu"><figcaption>Liste von Werten mit den vorhandenen Listen</figcaption></figure>
3.  Erstellen Sie eine Liste mit dem Namen `Tax_Country` und klicken Sie auf **Speichern**.

    <figure><img src="../../../.gitbook/assets/TaxCodes_3.png" alt="Dialog Neue Liste mit dem Namen Tax_Country" width="563"><figcaption>Liste Tax_Country anlegen</figcaption></figure>
4.  Erstellen Sie die folgenden drei zusätzlichen Listen:

    * `Tax_Code_Full`
    * `Tax_Code_Reduced`
    * `Tax_Code_Free`

    <div><figure><img src="../../../.gitbook/assets/TaxCodes_28.png" alt="Dialog Neue Liste mit dem Namen Tax_Code_Full"><figcaption>Liste Tax_Code_Full anlegen</figcaption></figure> <figure><img src="../../../.gitbook/assets/TaxCodes_29.png" alt="Dialog Neue Liste mit dem Namen Tax_Code_Reduced"><figcaption>Liste Tax_Code_Reduced anlegen</figcaption></figure> <figure><img src="../../../.gitbook/assets/TaxCodes_30.png" alt="Dialog Neue Liste mit dem Namen Tax_Code_Free"><figcaption>Liste Tax_Code_Free anlegen</figcaption></figure></div>
5.  Klicken Sie auf eine der neu erstellten Listen, um sie zu öffnen. Drücken Sie dann die Schaltfläche **Zeile hinzufügen**, um eine neue Zeile hinzuzufügen.

    <figure><img src="../../../.gitbook/assets/TaxCode_4.png" alt="Seite Liste von Werten mit der Schaltfläche Zeile hinzufügen unter der geöffneten Liste"><figcaption>Eine Zeile zur geöffneten Liste hinzufügen</figcaption></figure>
6.  Geben Sie die gewünschten jeweiligen Werte aus **LN** ein und drücken Sie **Speichern**, um die Änderungen zu speichern.

    * Wenn Sie mehrere Werte haben, können Sie auf **Weitere Werte hinzufügen** klicken, um diese hinzuzufügen.

    <div><figure><img src="../../../.gitbook/assets/TaxCodes_5.png" alt="Dialog Werte anlegen mit einem eingetragenen LN-Steuercode im Feld Name"><figcaption>LN-Steuercode im Feld Name eintragen</figcaption></figure> <figure><img src="../../../.gitbook/assets/TaxCodes_27.png" alt="Dialog Werte anlegen mit dem über Weitere Werte hinzugefügten Wert 800"><figcaption>Zweiten Wert über Weitere Werte hinzufügen</figcaption></figure></div>

    * **HINWEIS:** Sie finden die Steuercodes in LN unter: **Common** → **Taxation** → **Master Data** → **Tax Codes** → **Tax Codes by Country**

    <figure><img src="../../../.gitbook/assets/TaxCodes_LN.png" alt="Infor LN, Sitzung Steuercodes nach Land für Österreich mit den Spalten Steuercode und Steuerart"><figcaption>LN: Common > Taxation > Master Data > Tax Codes > Tax Codes by Country</figcaption></figure>

### **Schritt 2: Felder in DocBits hinzufügen**

1.  Navigieren Sie zu **Einstellungen** -> **Globale Einstellungen** -> **Dokumenttypen**.

    <figure><img src="../../../.gitbook/assets/TaxCodes_6.png" alt="Geöffnetes Menü Globale Einstellungen mit dem Eintrag Dokumenttypen"><figcaption>Einstellungen: Globale Einstellungen > Dokumenttypen</figcaption></figure>
2.  Wählen Sie das Menü **Felder** für den Dokumenttyp, in dem Sie die Felder hinzufügen möchten.

    <figure><img src="../../../.gitbook/assets/docbits_docbits_image_8.png" alt="Seite Dokumenttypen mit dem Menü Felder unter jedem Dokumenttyp"><figcaption>Menü Felder des Dokumenttyps öffnen</figcaption></figure>
3.  Unter **Mehrwertsteuer & Beträge** erstellen Sie sechs neue Felder wie folgt:

    <figure><img src="../../../.gitbook/assets/TaxCodes_8.png" alt="Registerkarte Felder mit der Gruppe Mehrwertsteuer &amp; Beträge und der Schaltfläche Neu erstellen"><figcaption>Registerkarte Felder: Gruppe Mehrwertsteuer &amp; Beträge</figcaption></figure>

<table data-header-hidden><thead><tr><th width="306"></th><th width="139"></th><th width="119"></th><th></th></tr></thead><tbody><tr><td><strong>Name</strong></td><td><strong>Titel</strong></td><td><strong>Feldtyp</strong></td><td><strong>Liste von Werten</strong></td></tr><tr><td><code>tax_country</code></td><td>Tax Country</td><td>Dropdown</td><td>Tax_Country</td></tr><tr><td><code>tax_country_2</code></td><td>Tax Country Reduced</td><td>Dropdown</td><td>Tax_Country</td></tr><tr><td><code>tax_country_3</code></td><td>Tax Country Free</td><td>Dropdown</td><td>Tax_Country</td></tr><tr><td><code>tax_code_without_country</code></td><td>Tax Code</td><td>Dropdown</td><td>Tax_Code_Full</td></tr><tr><td><code>tax_code_without_country_2</code></td><td>Tax Code Reduced</td><td>Dropdown</td><td>Tax_Code_Reduced</td></tr><tr><td><code>tax_code_without_country_3</code></td><td>Tax Code Free</td><td>Dropdown</td><td>Tax_Code_Free</td></tr></tbody></table>

<div><figure><img src="../../../.gitbook/assets/TaxCodes_13.png" alt="Dialog Dokumentfelddetails für tax_code_without_country mit Liste Tax_Code_Full"><figcaption>Feld tax_code_without_country: Dropdown, Liste Tax_Code_Full</figcaption></figure> <figure><img src="../../../.gitbook/assets/TaxCodes_11.png" alt="Dialog Dokumentfelddetails für tax_country_2 mit Titel Tax Country Reduced"><figcaption>Feld tax_country_2: Dropdown, Liste Tax_Country</figcaption></figure> <figure><img src="../../../.gitbook/assets/TaxCodes_12.png" alt="Dialog Dokumentfelddetails für tax_country_3 mit Titel Tax Country Free"><figcaption>Feld tax_country_3: Dropdown, Liste Tax_Country</figcaption></figure></div>

<div><figure><img src="../../../.gitbook/assets/TaxCodes_10.png" alt="Dialog Dokumentfelddetails für tax_country mit Feldtyp Dropdown und Liste Tax_Country"><figcaption>Feld tax_country: Dropdown, Liste Tax_Country</figcaption></figure> <figure><img src="../../../.gitbook/assets/TaxCodes_14.png" alt="Dialog Dokumentfelddetails für tax_code_without_country_2 mit Liste Tax_Code_Reduced"><figcaption>Feld tax_code_without_country_2: Dropdown, Liste Tax_Code_Reduced</figcaption></figure> <figure><img src="../../../.gitbook/assets/TaxCodes_15.png" alt="Dialog Dokumentfelddetails für tax_code_without_country_3 mit Liste Tax_Code_Free"><figcaption>Feld tax_code_without_country_3: Dropdown, Liste Tax_Code_Free</figcaption></figure></div>

4.  Nach dem Speichern jedes Feldes klicken Sie auf **Einstellungen speichern**, um die Änderungen anzuwenden.

    <figure><img src="../../../.gitbook/assets/TaxCodes_20.png" alt="Registerkarte Felder mit der Schaltfläche Einstellungen speichern über der Feldliste"><figcaption>Einstellungen speichern, um die neuen Felder zu übernehmen</figcaption></figure>

### **Schritt 3: Layout bearbeiten**

1.  Gehen Sie zu **Einstellungen** -> **Globale Einstellungen** -> **Dokumenttypen**.

    <figure><img src="../../../.gitbook/assets/TaxCodes_6.png" alt="Geöffnetes Menü Globale Einstellungen mit dem Eintrag Dokumenttypen"><figcaption>Einstellungen: Globale Einstellungen > Dokumenttypen</figcaption></figure>
2.  Öffnen Sie das Menü **Layout bearbeiten** für den Dokumenttyp, den Sie bearbeiten möchten.

    <figure><img src="../../../.gitbook/assets/TaxCodes_19.png" alt="Seite Dokumenttypen mit dem Link Layout bearbeiten unter jedem Dokumenttyp"><figcaption>Layout bearbeiten des Dokumenttyps öffnen</figcaption></figure>
3.  Wählen Sie die entsprechende **Dokumentenherkunft** aus, für die Sie die Steuercodes anwenden möchten.

    <figure><img src="../../../.gitbook/assets/TaxCodes_26.png" alt="Layout-Builder mit der Auswahl des Dokumentursprungs und der Werkzeugleiste der Vorlage"><figcaption>Layout-Builder: Dokumentursprung auswählen</figcaption></figure>
4.  Scrollen Sie nach unten zum Abschnitt **Tax Details**.

    <figure><img src="../../../.gitbook/assets/TaxCodes_21.png" alt="Layout-Builder mit der Gruppe Steuerdetails und ihren Feldern im Elementbaum"><figcaption>Zur Gruppe Steuerdetails scrollen</figcaption></figure>
5. Erweitern Sie das Dropdown-Menü **Form-Elemente**.
6.  Verwenden Sie im Abschnitt Steuerdetails das **Sub Group** Werkzeug. Ziehen Sie es neben ein vorhandenes Feld.

    <figure><img src="../../../.gitbook/assets/TaxCodesMulti_1.png" alt="Layout-Builder mit dem Werkzeug Untergruppe in der Auswahl Formularelemente"><figcaption>Werkzeug Untergruppe auswählen</figcaption></figure>
7.  Um Ihrer Sub Group einen Namen zu geben, klicken Sie auf die Sub Group und geben Sie den gewünschten Namen im Feld **Label** ein.

    <div><figure><img src="../../../.gitbook/assets/TaxCodesMulti_2.png" alt="Layout-Builder mit einer neuen leeren Untergruppe neben einem vorhandenen Feld"><figcaption>Untergruppe neben einem Feld ablegen</figcaption></figure> <figure><img src="../../../.gitbook/assets/TaxCodesMulti_3.png" alt="Eigenschaftenbereich mit dem Feld Label der neuen Untergruppe"><figcaption>Untergruppe im Feld Label benennen</figcaption></figure></div>
8.  Ziehen Sie die Felder, die zu dieser Gruppe gehören, in das **Sub Group** Feld.

    <figure><img src="../../../.gitbook/assets/TaxCodeMulti_4.png" alt="Layout-Builder mit den in die neue Untergruppe verschobenen Steuerfeldern"><figcaption>Steuerfelder in die Untergruppe verschieben</figcaption></figure>
9. Erweitern Sie das Dropdown-Menü **Felder**.
10. Suchen Sie nach **Tax** und ziehen Sie die entsprechenden Felder, wie **Tax Country** und **Tax Code**, in die entsprechende Sub Group.

    <figure><img src="../../../.gitbook/assets/TaxCodeMulti_5.png" alt="Layout-Builder mit Tax Country und Tax Code innerhalb der Untergruppe"><figcaption>Tax Country und Tax Code in der Untergruppe</figcaption></figure>
11. Wiederholen Sie die Schritte 5 bis 10 zwei Mal, um den folgenden Zustand zu erreichen:

    <figure><img src="../../../.gitbook/assets/TaxCodeMulti_6.png" alt="Layout-Builder mit drei Steueruntergruppen für vollen, reduzierten und steuerfreien Satz"><figcaption>Drei Untergruppen für voll, reduziert und steuerfrei</figcaption></figure>
12. Speichern Sie die Vorlage.

    <figure><img src="../../../.gitbook/assets/TaxCodeMulti_7.png" alt="Layout-Builder mit gespeicherter Vorlage für mehrere Steuercodes"><figcaption>Vorlage für mehrere Steuercodes speichern</figcaption></figure>

### Schritt 4: Überprüfen, ob alles funktioniert hat und die resultierenden Änderungen

Nachdem Sie ein neues Dokument in DocBits mit den ausgewählten korrekten Dokumenteneinstellungen hochgeladen haben, können Sie die Steuercodes auswählen, die Sie in Schritt 1 hinzugefügt haben, und mehrere Steuercodes hinzufügen, die in Schritt 3 konfiguriert wurden.

* Das Dokument beginnt mit drei verschiedenen Abschnitten: einem für Steuerbeträge voll, einem für Steuerbeträge reduziert und einem für Steuerbeträge frei.
* Durch Klicken auf die Plus-Schaltfläche innerhalb eines Abschnitts wird eine Duplikation erstellt, die mehrere Einreichungen zum ausgewählten Steuersatz ermöglicht.

<figure><img src="../../../.gitbook/assets/TaxCodeMulti_8.png" alt="Feldprüfung mit drei getrennten Steuerabschnitten sowie Plus- und Entfernen-Schaltfläche"><figcaption>Drei Steuerabschnitte in der Feldprüfung</figcaption></figure>

* Abschnitte können durch Klicken auf die Entfernen-Schaltfläche gelöscht werden.

<figure><img src="../../../.gitbook/assets/TaxCodeMulti_9.png" alt="Feldprüfung mit einem über die Plus-Schaltfläche duplizierten Steuerabschnitt"><figcaption>Weiteren Abschnitt über die Plus-Schaltfläche hinzufügen</figcaption></figure>

* Gesamtbeträge werden als Summe aller Abschnitte berechnet.
* Die Validierung des Gesamtbetrags wird basierend auf allen Steuerabschnitten geändert.
* Skripte für neue Abschnitte können nur angewendet werden, nachdem Felder zur Ansicht hinzugefügt wurden.

### Hinweis für LN:

In **LN** wird die USt-Position basierend auf der Positionsnummer aus dem Dropdown-Menü Steuercode/Steuerland ausgefüllt. Nur die Positionsnummer wird zum Export gesendet.

<figure><img src="../../../.gitbook/assets/TaxCodesLN_2.png" alt="Infor LN, Sitzung Steuerzeilen nach externer Rechnung mit der Spalte Steuerposition"><figcaption>LN: Tax Lines by External Invoice</figcaption></figure>

<figure><img src="../../../.gitbook/assets/TaxCodesLN_3.png" alt="Infor LN, Sitzung Steuerzeilen nach externer Rechnung mit der Positionsnummer"><figcaption>LN: die Positionsnummer wird als USt-Position exportiert</figcaption></figure>

#### **Export-Mapping**

Um die Steuerzeile mit der Kostenzeile zu verknüpfen:

1. Fügen Sie `TaxLine` zur Liste **InvoiceCostFields** hinzu.
2. Fügen Sie den folgenden Eintrag hinzu, der dem Beispiel unten folgt:\
   `ICF_TaxLine = TF_position`

<figure><img src="../../../.gitbook/assets/TaxCodeMulti_10.png" alt="Exportzuordnung mit dem Eintrag ICF_TaxLine neben den Rechnungskostenfeldern"><figcaption>Exportzuordnung: ICF_TaxLine = TF_position</figcaption></figure>
