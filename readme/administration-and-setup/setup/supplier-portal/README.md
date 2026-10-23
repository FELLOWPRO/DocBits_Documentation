# Lieferantenportal

## Übersicht

{% embed url="https://youtu.be/R5IrCpiP__4" %}
{% endembed %}


Diese Seite erklärt, wie man das **Lieferanten-Portal** aktiviert und nutzt, sowie wo man alle relevanten Einstellungen findet. Das Lieferanten-Portal ermöglicht es Ihnen, Lieferanten zu **DocBits** einzuladen. Sobald der Zugang gewährt ist, können Lieferanten sich anmelden, um den Status ihrer **Bestellungen** und **Rechnungen** direkt in **DocBits** einzusehen.

## So aktivieren Sie das Lieferanten-Portal

1.  Gehen Sie zu **Einstellungen → Verarbeitung von Dokumenten → Module**.

    ![Einstellungsseite von DocBits mit geöffnetem Menü Document Processing und den Einträgen Module, Export, OCR Settings sowie Classification and Extraction](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/settings_module.png)
2.  Aktivieren Sie im Abschnitt **Versand & Lieferant** die Option **Lieferanten-Portal**.

    ![Einstellungsseite Modules in DocBits mit dem Abschnitt Shipping & Supplier und der Option Supplier Portal](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/supplier_portal_1.png)

## Einstellungen des Lieferanten

Sobald die Funktion **Lieferanten-Portal** aktiviert ist, erscheint ein neuer Abschnitt **Einstellungen des Lieferanten** am Ende des Menüs **Einstellungen**.

<figure><img src="../../../.gitbook/assets/supplier_general_settings-de.png" alt="Allgemeine Einstellungen des Lieferantenportals: zusätzliche Felder der Einladung."><figcaption><p>Allgemeine Einstellungen des Lieferantenportals: zusätzliche Felder der Einladung.</p></figcaption></figure>

[**Allgemeine Einstellungen des Lieferanten**](../../settings/supplier-setting/supplier-general-settings.md): Hier können Sie das **Lieferanten-Portal** anpassen, indem Sie Ihr Firmenlogo hochladen, das im Header aller E-Mail-Vorlagen angezeigt wird, und rechtliche Dokumente wie die Nutzungsbedingungen und die Datenschutzrichtlinie verwalten.

[**E-Mail-Vorlagen**](../../settings/supplier-setting/editing-email-templates.md)**:** Hier können Sie die Einladung E-Mail-Vorlagen erstellen und testen, die an eingeladene Lieferanten gesendet werden.

**Lieferant Layout:** Hier können Sie die Layouts erstellen und verwalten, die definieren, welche Informationen neue Lieferanten während des Registrierungsprozesses bereitstellen müssen.

[**Exportkonfiguration**](../../settings/supplier-setting/export-configuration-for-supplier-portal-for-m3.md): Hier können Sie definieren, wie Daten zwischen dem **Lieferanten-Portal** und dem **Infor M3**-System mithilfe von ION- und IDM-Mapping-Dateien zugeordnet und synchronisiert werden.

**Berechtigungen für Lieferanten**: Hier können Sie die Berechtigungen konfigurieren, die Lieferanten im **Lieferanten-Portal** haben werden. Sie können auch Lieferanten gruppieren, um den Zugriff und die Einstellungen über mehrere Lieferanten hinweg einfacher zu verwalten.

Eine detaillierte Anleitung zu allen Einstellungen des Lieferanten finden Sie [hier](../../settings/supplier-setting/).

## Dashboard für Lieferanten <a href="#supplier-permissions" id="supplier-permissions"></a>

Sie können auf das **Dashboard für Lieferanten** über das linke Menü zugreifen, wie unten gezeigt.

![Supplier Dashboard in DocBits mit den Zahlen zu All Supplier, Pending Approval und Pending Registration und einer Tabelle mit Test Supplier-Zeilen](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/supplier_portal_2.png)

Alle von Ihnen erstellten Lieferanten werden hier angezeigt.

## Filter für Lieferanten

Sie können nach Lieferanten anhand von N**ame** oder N**ummer** suchen oder die erweiterten Filter verwenden, um die Ergebnisse nach:

* **Lieferantengruppen**
* **Status**
* **Erstellt am**

einzugrenzen.

Sie können auch angeben, wie viele Lieferanten pro Seite angezeigt werden sollen.

![Filterbereich des Supplier Dashboards mit Supplier Groups, Status, Created On, Supplier Per Page und einer Schaltfläche Clear Filters](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/supplier_portal_9.png)

Zusätzlich können Sie schnell nach den Status **Genehmigung ausstehend** oder **Anstehende Registrierung** filtern, indem Sie auf die entsprechende Kategorie links von der Filterleiste klicken.

![Dashboard document table with Document name, Imported on, Type, Status, Assigned to, Pages and Invoice number columns](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/10.png)

## Status der Lieferanten

Wenn Sie das **Lieferanten-Portal** verwenden, ist es wichtig, die verschiedenen Status zu verstehen, die Lieferanten haben können. Unten finden Sie eine Liste aller möglichen Lieferantenstatus und deren Bedeutungen:

* **Open**: Bestehender Lieferant, der noch nicht zum Portal eingeladen wurde.
* **Anstehende Registrierung**: Lieferant wurde eingeladen, hat aber den Registrierungsprozess noch nicht abgeschlossen.
* **Ausstehender Lieferanteninput**: Registrierung ist abgeschlossen, aber weitere Eingaben oder Änderungen sind vom Lieferanten erforderlich.
* **Genehmigung ausstehend**: Lieferant hat die Registrierung abgeschlossen und wartet auf die erste Genehmigung.
* **Ausstehende AP-Genehmigung**: Lieferant hat die erste Genehmigung erhalten und wartet auf eine zweite (Buchhaltung) Genehmigung.
* **Genehmigt**: Lieferant hat den Prozess abgeschlossen und wurde vollständig genehmigt.
* **Abgelehnt**: Die Registrierung oder Genehmigung des Lieferanten wurde abgelehnt.

## Werkzeuge im Dashboard für Lieferanten

Rechts von der Suchleiste finden Sie mehrere Werkzeuge, die Ihnen helfen, mit dem Dashboard effizienter zu interagieren und es zu verwalten.

### Dashboard aktualisieren <a href="#refresh-table" id="refresh-table"></a>

![Tabelle Supplier Dashboard in DocBits mit der Schaltfläche zum Aktualisieren der Tabelle in der oberen Symbolleiste](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/supplier_portal_3.png)

Klicken Sie auf diese Schaltfläche, um das Dashboard zu aktualisieren und die aktuellsten Daten und Status zu laden.

### Tabellenspalten für die Organisation festlegen <a href="#set-table-columns-for-organization" id="set-table-columns-for-organization"></a>

![Supplier-Dashboard-Tabelle in DocBits mit der Schaltfläche zum Festlegen der Tabellenspalten in der oberen Symbolleiste](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/supplier_portal_4.png)

Klicken Sie auf diese Schaltfläche, um ein Menü zu öffnen, in dem Sie die Sichtbarkeit der Spalten in der Bestelltabelle verwalten können. Verwenden Sie die Kontrollkästchen und Pfeiltasten, um Spalten zwischen den sichtbaren und versteckten Abschnitten zu verschieben. Sie können auch Spalten durch Ziehen und Ablegen der Spaltennamen neu anordnen. Klicken Sie auf **Fertig**, um Ihre Änderungen zu speichern.

![Menü Columns settings für die Lieferantentabelle mit ausgeblendeten Spalten wie Supplier Number, Status und Created On sowie den Schaltflächen Cancel und Done](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/supplier_portal_7.png)

### Analytik <a href="#analytics" id="analytics"></a>

![Supplier Dashboard in DocBits mit den Registerkarten All Supplier, Pending Approval und Pending Registration sowie der Lieferantentabelle mit den Spalten Supplier Name und Status](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/supplier_portal_5.png)

Durch Klicken auf diese Schaltfläche wird ein neuer Abschnitt geöffnet, der zeigt, wie viele Lieferanten kurz vor dem Ablauf stehen und wann.\
Klicken Sie auf eine beliebige Kategorie, um einen Filter anzuwenden und nur diese Lieferanten anzuzeigen.

![Analysebereich des Supplier Dashboards mit Expired (13) und Ablauf-Zahlen für 1 Month, 6 Month und 1 Year](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/supplier_portal_8.png)

## Lieferanten erstellen und Registrierungs-E-Mail senden

### **Um einen neuen Lieferanten zu erstellen:**

1.  Klicken Sie auf das Pluszeichen (+) in der oberen rechten Ecke.

    ![Supplier Dashboard in DocBits mit den Registerkarten All Supplier, Pending Approval und Pending Registration sowie der Lieferantentabelle mit den Spalten Supplier Name und Status](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/supplier_portal_6.png)
2.  Füllen Sie die erforderlichen Felder aus und klicken Sie dann auf **Speichern**.

    ![Formular Add Supplier in DocBits mit den Feldern Supplier Group, Supplier Name, Supplier Responder und Payment Terms sowie den Schaltflächen Cancel und Save](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/supplier_portal_11.png)
3. Der Lieferant erhält automatisch eine E-Mail mit einem Link zur Erstellung seines Kontos.

### **Um eine Registrierungs-E-Mail an einen bestehenden Lieferanten zu senden:**

1. Suchen Sie den Lieferanten im **Dashboard für Lieferanten**.
2. Klicken Sie auf das Drei-Punkte-Menü in der Spalte **Aktionen**.
3.  Wählen Sie **Magic Link**.

    ![Supplier Dashboard in DocBits mit geöffnetem Zeilenmenü und der Option Magic Link](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/supplier_portal_12.png)
4. Überprüfen Sie die Details des Lieferanten.
5.  Klicken Sie auf **Senden**, um den Registrierungslink per E-Mail zu versenden.

    ![Bestätigungsbereich Magic Link in DocBits mit den Details zu Supplier Group, Supplier Name und Supplier Responder sowie den Schaltflächen Cancel und Send](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/supplier_portal_13.png)

## Wie funktioniert der Registrierungsprozess für den Lieferanten?

Nachdem eine Einladung per E-Mail gesendet wurde, muss der Lieferant den Registrierungsprozess abschließen, um auf das **Lieferanten-Portal** zuzugreifen.

Eine detaillierte Schritt-für-Schritt-Anleitung zum Registrierungsprozess finden Sie [hier](supplier-registration.md).
