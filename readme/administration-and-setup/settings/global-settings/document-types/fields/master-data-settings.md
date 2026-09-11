# Stammdaten-Einstellungen

## Übersicht

Im Abschnitt der **Stammdaten-Einstellungen** der **Felder**-Einstellungen für einen bestimmten **Dokumenttyp** können Sie Stammdaten-Zuordnungen zu Feldern anzeigen und konfigurieren, die bei der Feldvalidierung verwendet werden, unter Verwendung von Daten aus [**Stammdaten**](../../../../../admin-section/settings/document-processing/master-data-lookup.md).

Diese Zuordnungen definieren, wie Stammdaten während der Validierung auf einzelne Felder angewendet werden. Diese Seite bietet eine ausführliche Anleitung, wie Sie diese Zuordnungen konfigurieren und verwalten.

## **Zugriff auf** Stammdaten-Einstellungen **Einstellungen**

Um auf die **Stammdaten-Einstellungen** zuzugreifen:

1.  Gehen Sie zu **Einstellungen → Globale Einstellungen → Dokumenttypen**

    ![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/settings_document_types.png)
2.  Wählen Sie den gewünschten **Dokumenttyp** und klicken Sie auf **Felder**.

    ![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/settings_document_types_fields.png)
3.  Klicken Sie auf **Stammdaten-Einstellungen**

    ![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/fields_master_data_settings_1.png)

## Stammdaten

Im Abschnitt **Stammdaten** können Sie Lookup-Konfigurationen aus Ihren Stammdaten erstellen, um sie als Feldzuordnungen während der Feldvalidierung zu verwenden.

### Standard-Einträge

Im Abschnitt **Stammdaten** werden bestimmte Default-Einträge von **DocBits** bereitgestellt. Diese Einträge:

* Können nicht bearbeitet oder gelöscht werden
* Können deaktiviert werden, wenn sie nicht benötigt werden

Default-Einträge sind zur einfachen Identifizierung deutlich mit einem **Default** tag gekennzeichnet.

![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/fields_master_data_settings_2.png)

### **Lookup-Konfiguration erstellen**

Um eine neue Lookup-Konfiguration für Stammdaten zu erstellen:

1. Navigieren Sie zum Abschnitt **Stammdaten**.
2.  Klicken Sie oben rechts auf **Lookup-Konfiguration erstellen**.

    ![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/fields_master_data_settings_3.png)
3. Konfigurieren Sie die folgenden Optionen:
   * **Nachschlagename**\
     Der Name der Lookup-Konfiguration.
   * **Lookup Dataset Name**\
     Wählen Sie das Dataset aus, das für diese Lookup-Konfiguration verwendet werden soll.
   * **Konfliktverarbeitung**\
     Ein Konflikt bedeutet, dass die Suche mehr als einen Datensatz gefunden hat. Diese Einstellung legt fest, was dann passiert:
     * **Best Score** – Verwendet den Eintrag, der zu den meisten Feldern passt. Lässt das Feld nie leer und kann deshalb den falschen Datensatz wählen.
     * **Return None** – Lässt das Feld leer, damit ein Benutzer den richtigen Datensatz auswählt.
     * **Return First** – Verwendet den ersten gefundenen Wert.
   *   **Kontext Typ**

       Gibt an, wo im Dokument die Lookup-Konfiguration angewendet wird. Wählen Sie zwischen:

       **HEADER**

       Der Lookup wird in der Feldvalidierung verwendet. Konfigurieren Sie Folgendes:

       * **Alle abgleichen**\
         Wenn aktiviert, muss ein Datensatz zu **allen** verwendeten Feldern passen. Wenn deaktiviert (Standard), genügt **ein** passendes Feld, was eine längere Trefferliste ergibt.

       ![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/fields_master_data_settings_4.png)

       \
       **LINE**

       Der Lookup wird innerhalb einer Dokumenttabelle verwendet. Konfigurieren Sie Folgendes:

       * **Kontextdetails**\
         Wählen Sie die spezifische Tabelle, auf die der Lookup angewendet werden soll.
       * **Alle abgleichen**\
         Wenn aktiviert, muss ein Datensatz zu **allen** verwendeten Feldern passen. Wenn deaktiviert (Standard), genügt **ein** passendes Feld, was eine längere Trefferliste ergibt.

       ![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/fields_master_data_settings_5.png)
{% hint style="info" %}
**Alle abgleichen** und **Konfliktverarbeitung** wirken zusammen und entscheiden, ob ein Lieferant automatisch erkannt wird. Die Einrichtungsseite erklärt beide mit Beispielen:

{% content-ref url="../../../../setup/document-types/fuzzy-data-configuration-with-master-data.md" %}
[fuzzy-data-configuration-with-master-data](../../../../setup/document-types/fuzzy-data-configuration-with-master-data.md)
{% endcontent-ref %}
{% endhint %}

4.  Klicken Sie auf **Speichern**, um die Lookup-Konfiguration zu erstellen.

    ![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/fields_master_data_settings_6.png)

### Aktionen für bestehende Lookup-Konfiguration

Um eine bestehende Lookup-Konfiguration zu verwalten, klicken Sie auf die drei Punkte oben rechts in der Konfiguration, die Sie ändern möchten.

![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/fields_master_data_settings_7.png)

Folgende Aktionen sind verfügbar:

* **Aktivieren / Deaktivieren**\
  Schaltet den Status der Lookup-Konfiguration um.
  * Aktive Konfigurationen sind mit einem **Aktiv**-Tag markiert.
  * Inaktive Konfigurationen sind mit einem **Inaktiv**-Tag markiert.
*   **Duplizieren**\
    Nach Eingabe eines Namens und einem Klick auf **Fertig** wird eine Kopie der ausgewählten Lookup-Konfiguration erstellt.

    ![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/fields_master_data_settings_8.png)
* **Bearbeiten/Siehe**\
  Ermöglicht die Änderung der ausgewählten Lookup-Konfiguration.\
  Nach Ihren Änderungen klicken Sie auf **Speichern**, um sie anzuwenden.\
  <mark style="color:red;">**Hinweis**</mark>: Default-Lookup-Konfigurationen können nur angezeigt, nicht bearbeitet werden. Die Option **Bearbeiten** wird durch **Siehe** ersetzt.
*   **Löschen**\
    Löscht die ausgewählte Lookup-Konfiguration nach Bestätigung dauerhaft.\
    <mark style="color:red;">**Hinweis**</mark>: Nur Konfigurationen ohne **Default** tag können gelöscht werden.

    ![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/fields_master_data_settings_9.png)

### Neues Feld erstellen

So fügen Sie Ihrer Lookup-Konfiguration ein neues Feld hinzu:

1. Öffnen Sie die gewünschte Lookup-Konfiguration.
2.  Klicken Sie oben rechts auf **erstellen.**

    ![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/fields_master_data_settings_10.png)
3. Konfigurieren Sie die erforderlichen Optionen.
   * **Nachschlagefeld**\
     Das Feld, das im ausgewählten Lookup-Dataset durchsucht wird.
   * **Validierungsfeld**\
     Das Feld, das während der Feldvalidierung angezeigt wird.
   * **Übergeordnetes Feld** (optional)\
     Dieses Feld wird verwendet, um die Korrektheit des Werts im **Validierungsfeld** zu validieren, indem sichergestellt wird, dass er dem entsprechenden übergeordneten Eintrag im Lookup-Dataset entspricht.
   * **Suchoperator** (optional)\
     Wählen Sie, wie **DocBits** nach Treffern im Lookup-Dataset sucht:
     * **Smart** – _(Default)_ Ignoriert Leerzeichen und Satzzeichen und sucht den Begriff **irgendwo** im Feld. "Meier" findet deshalb auch "Meier Bau GmbH".
     * **Enthält** – Sucht nach Einträgen, die den exakten Begriff irgendwo im Feld enthalten.
     * **Endet mit** – Sucht nach Einträgen, die mit dem angegebenen Begriff enden.
     * **genau** – Sucht nach einer exakten Übereinstimmung des gesamten Werts.
     * **Beginnt mit** – Sucht nach Einträgen, die mit dem angegebenen Begriff beginnen.
   * **Auto-Trigger** (optional)\
     Wenn aktiviert, füllt DocBits automatisch alle Felder in der Lookup-Konfiguration aus, sobald dieses Feld ausgefüllt ist.
   *   **Suchbar** (optional)\
       Wenn aktiviert, können Benutzer während der Feldvalidierung manuell nach Stammdaten suchen **und** das Feld nimmt an der automatischen Suche teil. Lassen Sie es deaktiviert, wenn das Feld das automatische Ergebnis nicht beeinflussen soll.

       ![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/fields_master_data_settings_12.png)

       ![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/fields_master_data_settings_13.png)
4.  Klicken Sie auf **Speichern**, um das neue Feld zu erstellen.

    ![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/fields_master_data_settings_11.png)

### Aktionen für bestehendes Feld

Um ein bestehendes Feld zu verwalten, klicken Sie in der Spalte **Aktionen** auf die drei Punkte neben dem Feld, das Sie ändern möchten.

![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/fields_master_data_settings_14.png)

Folgende Aktionen sind verfügbar:

* **Bearbeiten/Siehe**\
  Ermöglicht die Änderung des ausgewählten Feldes.\
  Nach Ihren Änderungen klicken Sie auf **Speichern**, um sie anzuwenden.\
  <mark style="color:red;">**Hinweis**</mark>: Default-Felder können nur angezeigt, nicht bearbeitet werden. In diesen Fällen erscheint die Option **Bearbeiten** als **Siehe**.
*   **Löschen**\
    Löscht das ausgewählte Feld nach Bestätigung dauerhaft.\
    <mark style="color:red;">**Hinweis**</mark>: Nur Felder ohne **Default** tag können gelöscht werden.

    ![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/fields_master_data_settings_9.png)

## LOV-Stammdaten

Der Abschnitt **LOV-Stammdaten** ermöglicht es Ihnen, Dropdown-Konfigurationen zu erstellen, die Werte aus Ihren Stammdaten verwenden. Diese Dropdowns können eigenständig sein oder von anderen Dropdowns abhängen, wodurch dynamische Filterung und kaskadierende Auswahlen während der Feldvalidierung ermöglicht werden.

### Lov Lookup Config erstellen

Eine Lov Lookup Config definiert, wie Dropdown-Optionen aus einer Stammdatentabelle bezogen werden und wie diese Werte angezeigt und in Dokumentfelder übernommen werden.

**So erstellen Sie eine neue Lov Lookup Config:**

1. Navigieren Sie zum Abschnitt **LOV-Stammdaten**.
2.  Klicken Sie oben rechts auf **Lov Lookup Config erstellen**.

    ![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/fields_master_data_settings_15.png)
3. Konfigurieren Sie die folgenden Optionen:
   * **Lov Name nachschlagen**\
     Der Name der lov lookup config.
   * **Lookup Lov Dataset Name**\
     Wählen Sie die Stammdatentabelle aus, die für diese lov lookup config verwendet werden soll.
   *   **Kontext Typ**\
       Gibt an, wo im Dokument die lov lookup config angewendet wird:

       **HEADER**

       Die lov lookup config wird in der Feldvalidierung verwendet. Konfigurieren Sie Folgendes:

       * **Nachschlage-Etikettenfeld**\
         Wählen Sie die Spalte, deren Wert im Dropdown angezeigt wird.
       * **Nachschlagewertfeld**\
         Wählen Sie die Spalte, deren Wert intern gespeichert und für die Filterung verwendet wird, wenn eine Auswahl getroffen wird. Dieser Wert wird dem Benutzer nicht angezeigt.
       * **Außerhalb des Feldes**\
         Definiert das Feld in der Feldvalidierung, das das ausgewählte Label aus dem Dropdown erhält.

       ![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/fields_master_data_settings_16.png)

       \
       **LINE**

       Die lov lookup config wird innerhalb einer Dokumenttabelle verwendet. Konfigurieren Sie Folgendes:

       * **Kontextdetails**\
         Wählen Sie die spezifische Tabelle, in der diese lov lookup config aktiv sein soll.
       * **Nachschlage-Etikettenfeld**\
         Die Spalte, deren Wert im Dropdown angezeigt wird.
       * **Nachschlagewertfeld**\
         Wählen Sie die Spalte, deren Wert intern gespeichert und für die Filterung verwendet wird, wenn eine Auswahl getroffen wird. Dieser Wert wird dem Benutzer nicht angezeigt.
       * **Außerhalb des Feldes**\
         Gibt das Zielfeld in der Tabelle an, in das das ausgewählte Label übernommen wird.

       ![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/fields_master_data_settings_17.png)
4.  Klicken Sie auf **Speichern**, um die lov lookup Konfiguration zu erstellen.

    ![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/fields_master_data_settings_18.png)

### Aktionen für bestehende Lookup-Konfiguration

Um eine bestehende lov lookup config zu verwalten, klicken Sie auf die drei Punkte oben rechts in der Konfiguration.

![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/fields_master_data_settings_19.png)

**Verfügbare Aktionen:**

* **Aktivieren / Deaktivieren**\
  Schaltet den Status der lov lookup config um.
  * **Aktiv**-Konfigurationen sind mit einem **Aktiv**-Tag markiert.
  * **Inaktiv**-Konfigurationen sind mit einem **Inaktiv**-Tag markiert.
*   **Duplizieren**\
    Nach Eingabe eines Namens und Klick auf **Fertig** wird eine Kopie der ausgewählten lov lookup config erstellt.

    ![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/fields_master_data_settings_21.png)
* **Bearbeiten / Siehe**\
  Ändern Sie die ausgewählte Konfiguration. Nach den Änderungen klicken Sie auf **Speichern**.
*   **Löschen**\
    Löscht die Konfiguration nach Bestätigung dauerhaft.

    ![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/fields_master_data_settings_20.png)

### Neues Feld erstellen

Innerhalb jeder lov lookup config können Sie zusätzliche Felder als Dropdowns definieren, die als Vorfilter für die Haupt-lov-Logik fungieren.

Diese Felder werden ausgewertet, bevor das Haupt-lov-Dropdown geladen wird. Basierend auf den in diesen Feldern ausgewählten Werten werden die Ergebnisse des Haupt-lov-Feldes dynamisch gefiltert — so werden abhängige Dropdowns ermöglicht.\
Beispielsweise kann die Auswahl eines Landes in einem Vorfilterfeld die Stadtauswahl im Haupt-lov-Dropdown eingrenzen.

Zusätzlich zum Erstellen neuer Felder können Sie auch vorhandene Felder als Vorfilter verwenden. Wenn dies konfiguriert ist, filtert der in dem bestehenden Feld gewählte Wert das Haupt-lov-Dropdown automatisch.

**So fügen Sie ein neues Feld hinzu:**

1. Öffnen Sie die gewünschte lov lookup config.
2.  Klicken Sie oben rechts auf **erstellen.**

    ![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/fields_master_data_settings_22.png)
3.  Konfigurieren Sie die erforderlichen Optionen.

    **Feldkonfigurationsoptionen (gilt für die Kontexte HEADER und LINE):**

    * **Nachschlagefeld**\
      Die Spalte, die im ausgewählten Dataset für Dropdown-Werte durchsucht wird.
      * **Feld filtern**\
        Gibt das Feld an, dessen Wert verwendet wird, um die Ergebnisse der lov lookup config vor dem Laden des Haupt-Dropdowns vorzufiltern.
      * **Wert filtern** (optional)\
        Fügen Sie statische Filter hinzu, um die Lookup-Ergebnisse weiter einzugrenzen.
      * **Erforderlich**\
        Wenn aktiviert, muss dieses Feld ausgefüllt sein, bevor abhängige Dropdowns befüllt werden können.
4.  Klicken Sie auf **Speichern**, um das neue Feld zu erstellen.

    ![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/fields_master_data_settings_23.png)

### Aktionen für bestehendes Feld

Um ein bestehendes Feld innerhalb einer lov lookup config zu verwalten, klicken Sie in der Spalte **Aktionen** auf die drei Punkte neben dem Feld.

![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/fields_master_data_settings_24.png)

**Verfügbare Aktionen:**

* **Bearbeiten**\
  Ändern Sie das ausgewählte Feld. Nach den Änderungen klicken Sie auf **Speichern**, um diese anzuwenden.
*   **Löschen**\
    Entfernt das Feld nach Bestätigung dauerhaft.

    ![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/fields_master_data_settings_20.png)
