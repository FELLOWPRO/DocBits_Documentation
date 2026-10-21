# Dann

Eine **Then**-Karte teilt einem Workflow mit, was nach seinem **When**-Trigger und allen **And**-Bedingungen zu tun ist. Wählen Sie im **Workflow-Builder** unter **Then...** **Karte hinzufügen** aus. Wählen Sie links eine Kategorie oder geben Sie einen Namen in **Karte suchen** ein. Wählen Sie eine Kartenvorschau aus, um sie hinzuzufügen, füllen Sie die auf der Karte angezeigten Felder aus und speichern Sie den Workflow. Scrollen Sie in der Auswahl, um weitere Karten anzuzeigen. Wählen Sie **×**, um es zu schließen, ohne eine Karte hinzuzufügen. Die vollständige Sequenz finden Sie unter [Workflow](..)].

Die Vorschauen unten zeigen verfügbare Aktionen, nicht abgeschlossene Einstellungen. Wählen Sie die Aktion aus, die dem gewünschten Ergebnis entspricht.

## Dokumentfeld

Setzen oder invertieren Sie ein Kontrollkästchen, fügen Sie Text in ein Feld ein oder kopieren Sie ein Feld in ein anderes. Wählen Sie die von der Karte geforderten Feldnamen und Werte aus. Siehe [Dokumentfeld](document-field).

<figure><img src="../../../.gitbook/assets/then-category-document-field-de.png" alt="Deutscher Then-Karten-Picker mit ausgewählter Kategorie „Dokument Feld"; die Vorschauen zeigen Kontrollkästchen-, Text- und Feld-Kopier-Aktionen."><figcaption>Ein Feld ändern oder seinen Inhalt kopieren.</figcaption></figure>

## Dokument

Wählen Sie **Das Dokument genehmigen** oder **Das Dokument ablehnen**, wenn der Workflow diese Entscheidung treffen soll. Verwenden Sie zuerst eine **Und**-Bedingung, wenn die Genehmigung von einer Prüfung abhängig sein soll. Siehe [Dokument](document).

<figure><img src="../../../.gitbook/assets/then-category-document-de.png" alt="Deutscher Then-Karten-Picker mit ausgewählter Kategorie „Dokument"; die Vorschauen „Genehmigen Sie das Dokument" und „Dokument ablehnen" sind sichtbar."><figcaption>Das aktuelle Dokument genehmigen oder ablehnen.</figcaption></figure>

## Logik

Verwenden Sie diese Karten, um Werte zwischen Zahlen-, Text- und booleschen Formaten zu konvertieren oder einen Wert aus JSON zu lesen. Wählen Sie die Ein- und Ausgabefelder auf der ausgewählten Karte aus.

<figure><img src="../../../.gitbook/assets/then-category-logic-de.png" alt="Deutscher Then-Karten-Picker mit ausgewählter Kategorie „Logik"; die sichtbaren Vorschauen wandeln Datentypen um und lesen Werte aus JSON."><figcaption>Werte für einen späteren Workflow-Schritt umwandeln.</figcaption></figure>

## Status

Wählen Sie **Status ändern**, um das Dokument in einen ausgewählten Status zu verschieben. Die Karte kann auch einen anderen Workflow auslösen. Siehe [Status](status).

<figure><img src="../../../.gitbook/assets/then-category-status-de.png" alt="Deutscher Then-Karten-Picker mit ausgewählter Kategorie „Status"; die Vorschau „Status ändern" enthält ein Statusfeld und optionalen Workflow-Trigger."><figcaption>Das Dokument in einen anderen Status verschieben.</figcaption></figure>

## Eingabeaufforderungen und Skripte

Wählen Sie diese Kategorie, um ein DocOperator-Eingabeaufforderungsskript auszuführen. Wählen Sie das Skript und die von der Karte angeforderten Variablen aus. Die Karte bietet auch Ausführungseinstellungen wie Wiederholungsversuche.

<figure><img src="../../../.gitbook/assets/then-category-prompts-scripts-de.png" alt="Deutscher Then-Karten-Picker mit ausgewählter Kategorie „Prompts und Skripte"; eine DocOperator-Prompt-Skript-Vorschau ist sichtbar."><figcaption>Ein konfiguriertes DocOperator-Prompt-Skript ausführen.</figcaption></figure>

## Exportieren

Starten Sie einen Export, exportieren Sie mit einer ausgewählten Konfiguration oder stellen Sie einen endgültigen Export in die Warteschlange. Wählen Sie die auf Ihrer Karte angezeigte Exportkonfiguration und Option für ausstehende Aufgaben. Siehe [Export](export).

<figure><img src="../../../.gitbook/assets/then-category-export-de.png" alt="Deutscher Then-Karten-Picker mit ausgewählter Kategorie „Exportieren"; die Vorschauen zeigen Start-, konfigurierten, Warteschlangen- und alternativen Export."><figcaption>Auswählen, wann und wie das Dokument exportiert wird.</figcaption></figure>

## Aufgabe

Erstellen Sie eine Aufgabe oder Benachrichtigung und weisen Sie sie einem Benutzer oder einer Gruppe zu. Geben Sie den von der Karte geforderten Titel, die Beschreibung, die Priorität und die Benachrichtigungseinstellungen ein. Einige Karten werden nacheinander zugewiesen. Siehe [Aufgabe](task).

<figure><img src="../../../.gitbook/assets/then-category-task-de.png" alt="Deutscher Then-Karten-Picker mit ausgewählter Kategorie „Aufgabe"; die sichtbaren Vorschauen erstellen oder weisen Aufgaben und Benachrichtigungen zu."><figcaption>Folgearbeit für eine Person oder Gruppe anlegen.</figcaption></figure>

## E-Mail

Senden Sie eine E-Mail mit einer ausgewählten Vorlage entweder an Empfänger oder an Gruppen. Wählen Sie die Vorlage und das Ziel auf der Karte aus.

<figure><img src="../../../.gitbook/assets/then-category-email-de.png" alt="Deutscher Then-Karten-Picker mit ausgewählter Kategorie „E-Mail"; die Vorschauen senden eine Vorlagen-E-Mail an Empfänger oder Gruppen."><figcaption>Eine E-Mail mit Vorlage senden.</figcaption></figure>

## Tisch

Ändern Sie Einträge oder berechnen Sie Werte in einer Dokumententabelle. Wählen Sie die von der Karte angeforderte Tabelle, Spalten, den Operator und die Ergebnisspalte aus. Siehe [Tabelle](table).

<figure><img src="../../../.gitbook/assets/then-category-table-de.png" alt="Deutscher Then-Karten-Picker mit ausgewählter Kategorie „Tabelle"; die Vorschauen ändern Einträge und berechnen Ergebnis-Spalten."><figcaption>Daten in Tabellen aktualisieren oder berechnen.</figcaption></figure>

## Bevollmächtigter

Weisen Sie das Dokument einem Benutzer, einer Gruppe, einem Empfänger oder einer Unterorganisation zu. Einige Karten verwenden ein Feld oder eine Entscheidungstabelle und bieten einen Fallback. Wählen Sie das richtige Ziel und den richtigen Fallback für die ausgewählte Karte. Siehe [Beauftragter](assignee).

<figure><img src="../../../.gitbook/assets/then-category-assignee-de.png" alt="Deutscher Then-Karten-Picker mit ausgewählter Kategorie „Zugewiesener Benutzer"; die sichtbaren Vorschauen weisen eine Person, einen Empfänger, eine Gruppe oder einen Lieferantenkontakt zu."><figcaption>Das Dokument der nächsten verantwortlichen Person oder Gruppe zuweisen.</figcaption></figure>

## Aktion

Führen Sie einen anderen Workflow aus, senden Sie eine HTTPS-Anfrage, rufen Sie eine API auf oder verwenden Sie die Kostensteigerungsberechnungskarte. Diese Aktionen können sich auf andere Systeme auswirken; Fragen Sie Ihren Administrator, welchen Endpunkt und welche Einstellungen Sie verwenden möchten. Siehe [Aktion](action).

<figure><img src="../../../.gitbook/assets/then-category-action-de.png" alt="Deutscher Then-Karten-Picker mit ausgewählter Kategorie „Aktion"; die Vorschauen zeigen Workflow ausführen, HTTPS-Anfrage, API-Aufruf und Kostensteigerungs-Berechnung."><figcaption>Einen weiteren Workflow oder eine Integrationsaktion starten.</figcaption></figure>

[Detaillierte Logikkartenfelder, JSON-Pfade, Trigger und Tests](../cards-overview/logic-cards-guide.md).
