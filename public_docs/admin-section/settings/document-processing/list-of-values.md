# Liste von Werten

## Übersicht

Die **Liste von Werten**-Funktion ermöglicht es Ihnen, vordefinierte Wertemengen zu erstellen und zu verwalten. Dies ist besonders nützlich für die Konfiguration von Dropdown-Menüs im [**Felder**](../../../administration-and-setup/settings/global-settings/document-types/fields/)-Bereich, die später in der **Feldvalidierung** verwendet werden können.

Diese Listen können für verschiedene Unterorganisationen angepasst werden und unterstützen mehrere Sprachen, was Flexibilität über **DocBits** hinweg bietet.

## Wie greife ich zu?

Sie können auf die **Liste von Werten** zugreifen, indem Sie zu **Einstellungen → Verarbeitung von Dokumenten → Liste von Werten** navigieren.

![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/settings_list_of_values.png)

## Wie füge ich eine Liste hinzu oder lösche sie

### Erstellen einer neuen Liste von Werten

1.  Klicken Sie auf **Neu** in der oberen rechten Ecke des Bildschirms.

    ![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/list_of_values_1.png)
2. Geben Sie einen **Name** für Ihre Liste ein.
3. _(Optional)_ Wählen Sie eine **Unterorganisation** aus, für die die Liste aktiv sein soll.
4.  Klicken Sie auf **Speichern**, um die Liste zu erstellen.

    ![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/list_of_values_2.png)

### Wie lösche ich eine Liste

Um eine Liste zu löschen, klicken Sie auf das Mülleimer-Symbol neben der entsprechenden Liste.

![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/list_of_values_13.png)

<mark style="color:red;">**Hinweis**</mark>: Die Liste wird sofort gelöscht. Listen, die mit dem [**Standard**](list-of-values.md#system-definierte-listen-und-zeilen)-Tag gekennzeichnet sind, können nicht gelöscht werden.

## Wie füge ich Werte zu einer bestehenden Liste hinzu, bearbeite oder entferne sie

Sie können Werte in einer bestehenden **Liste von Werten** mit einer der folgenden Methoden verwalten:

* [**Werte manuell hinzufügen**](list-of-values.md#werte-manuell-hinzufugen) – Geben Sie Werte einzeln über die Benutzeroberfläche ein.
* [**Werte aus einer CSV-Datei importieren**](list-of-values.md#werte-aus-einer-csv-datei-importieren) – Laden Sie eine CSV-Datei hoch, um mehrere Werte auf einmal hinzuzufügen.

### Werte manuell hinzufügen

1.  Klicken Sie auf die Liste, die Sie ändern möchten.

    ![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/list_of_values_3.png)
2.  Klicken Sie auf **Aktionen**.

    ![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/list_of_values_4.png)
3.  Klicken Sie auf **Zeile hinzufügen**.

    ![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/list_of_values_5.png)

Jetzt können Sie mehrere Eigenschaften für jeden Eintrag angeben:

![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/list_of_values_6.png)

**Wert**: So wird der Artikel intern in **DocBits** gespeichert. Er bleibt in allen Sprachen gleich und dient auch als Standardanzeigetext während der Feldvalidierung, wenn kein Etikett für die ausgewählte Sprache angegeben ist.

**Etikett**: Dies ist der Text, der auf dem Validierungsbildschirm angezeigt wird, basierend auf der ausgewählten Sprache. Wenn kein Etikett für die aktive Sprache in DocBits verfügbar ist, wird das System standardmäßig den **Wert** anzeigen.

**Sprache**: Gibt die Sprache an, in der das Etikett angezeigt wird.\
Eine detailliertere Erklärung finden Sie [hier](list-of-values.md#fugen-sie-ubersetzungen-zu-ihren-werten-hinzu).

**Unterorganisationen**: Gibt an, für welche **Unterorganisation** die Zeile aktiv sein soll. Wenn dies leer gelassen wird, ist die Zeile für alle Organisationen verfügbar.

**Synonyme**: Hier können Sie zusätzliche Werte angeben, die helfen, Ihr Dokument zu trainieren.\
Wenn **EUR** Ihr primärer **Wert** ist, können Sie EURO und € als **Synonyme** hinzufügen. Wenn das Dokument mit einem dieser **Synonyme** trainiert wird, erkennt **DocBits** automatisch EUR als den entsprechenden Wert aus Ihrer Liste. <mark style="color:red;">**Hinweis**</mark>: Jedes Synonym muss durch Drücken von **Enter** bestätigt werden, um es zur Liste hinzuzufügen.

4.  Nachdem Sie alle gewünschten Eigenschaften eingegeben haben, klicken Sie auf die Schaltfläche **Speichern**, um die Zeile hinzuzufügen.

    ![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/list_of_values_11.png)

### Werte aus einer CSV-Datei importieren

Um mehrere Werte auf einmal über den CSV-Import hinzuzufügen:

1.  Klicken Sie auf die Liste, die Sie aktualisieren möchten.

    ![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/list_of_values_3.png)
2.  Klicken Sie auf **Aktionen**.

    ![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/list_of_values_4.png)
3.  Klicken Sie auf **CSV hochladen**.

    ![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/list_of_values_7.png)
4. Klicken Sie auf **Datei**, um die CSV-Datei auszuwählen, die Sie hochladen möchten.
5. Wählen Sie das entsprechende **Begrenzungszeichen** aus, das in der CSV-Datei verwendet wird (`;` oder `,`).
6.  Klicken Sie auf **Hochladen**, um die Werte zu importieren.

    ![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/list_of_values_8.png)

### Vorhandene Werte bearbeiten

1. Suchen Sie die Zeile, die Sie bearbeiten möchten.
2. Klicken Sie auf die drei Punkte in der **Aktionen**-Spalte.
3.  Wählen Sie **Bearbeiten** aus dem Dropdown-Menü.

    ![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/list_of_values_10.png)
4. Nehmen Sie die erforderlichen Änderungen vor.
5.  Klicken Sie auf **Speichern**, um Ihre Änderungen anzuwenden.

    ![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/list_of_values_11.png)

### Werte löschen

1. Suchen Sie die Zeile, die Sie löschen möchten.
2. Klicken Sie auf die drei Punkte in der **Aktionen**-Spalte.
3.  Wählen Sie **Löschen** aus dem Dropdown-Menü.

    ![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/list_of_values_12.png)

<mark style="color:red;">**Hinweis**</mark>: Die Zeile wird sofort gelöscht. Zeilen, die mit dem [**Standard**](list-of-values.md#system-definierte-listen-und-zeilen)-Tag gekennzeichnet sind, können nicht gelöscht werden.

## Fügen Sie Übersetzungen zu Ihren Werten hinzu

Sie können so viele Übersetzungen hinzufügen, wie es unterstützte Sprachen in **DocBits** gibt.

Um eine Übersetzung hinzuzufügen:

1.  Klicken Sie auf das Plus (+) Symbol.

    ![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/list_of_values_14.png)
2.  Wählen Sie eine Sprache aus dem Dropdown-Menü aus.

    ![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/list_of_values_15.png)
3.  Geben Sie die gewünschte Übersetzung im **Etikett**-Feld ein.

    ![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/list_of_values_16.png)
4.  Um eine weitere Übersetzung hinzuzufügen, klicken Sie erneut auf das Plus (+) Symbol.

    ![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/list_of_values_17.png)
5.  Um eine Übersetzung zu entfernen, klicken Sie auf das Mülleimer-Symbol.

    ![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/list_of_values_18.png)
6.  Wenn Sie fertig sind, klicken Sie auf die Schaltfläche **Speichern**, um Ihre Übersetzungen zu speichern.

    ![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/list_of_values_19.png)

<mark style="color:red;">**Hinweis**</mark>: Wenn kein **Etikett** für die aktive Sprache verfügbar ist, wird DocBits standardmäßig den **Wert** anzeigen.

## System-definierte Listen und Zeilen

Einige Listen werden vom System vordefiniert und sind mit dem **Standard**-Tag gekennzeichnet. Diese Listen können nicht gelöscht werden, aber Sie können neue Zeilen hinzufügen und diese neu hinzugefügten Zeilen bei Bedarf entfernen.

![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/list_of_values_9.png)

Innerhalb dieser Standardlisten sind bestimmte Zeilen mit dem **Standard**-Tag gekennzeichnet – dies sind systemdefinierte Einträge. Sie können neue **Etiketten** in verschiedenen Sprachen hinzufügen, aber diese Standardzeilen können nicht gelöscht werden.

![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/list_of_values_20.png)
