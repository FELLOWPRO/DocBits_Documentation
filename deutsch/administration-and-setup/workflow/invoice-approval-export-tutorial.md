---
description: "Eine Trainingsrechnung prüfen, mit einer Bestellung abgleichen, zuweisen, genehmigen und die tatsächliche Zustellung beim Exportempfänger bestätigen."
---

# Eine Rechnung von der Prüfung bis zum Export begleiten

Thomas begleitet eine Rechnung durch die echte deutsche DocBits-Oberfläche: Upload, Positionskorrektur, Bestellabgleich, Zuständigkeit, persönliche Freigabe und nachgewiesener Export. Er erstellt zwei eigene Standard Workflows und prüft ihre Wirkung mit gezielten manuellen Tests.

{% embed url="https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/workflow-business-case-admin/v1/de.mp4" %}

[Mit Untertiteln ansehen](https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/workflow-business-case-admin/v1/de.html) · [Video öffnen](https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/workflow-business-case-admin/v1/de.mp4) · [Untertitel (WebVTT)](https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/workflow-business-case-admin/v1/de.vtt) · [Transkript](https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/workflow-business-case-admin/v1/de.txt) · 8:13

## Der Geschäftsfall

Die synthetische Trainingsrechnung hat zwei Positionen zu 1000 und 500 Euro netto. Die zugehörige Bestellung ist bereits importiert. Die Rechnung enthält 1500 Euro netto, 285 Euro Umsatzsteuer und einen Gesamtbetrag von 1785 Euro.

| Prüfschritt | Ergebnis im Video |
| --- | --- |
| Rechnungspositionen | Tabellenbereich markieren, zwei Zeilen auslesen, Spalten zuordnen und Artikelnummern korrigieren |
| Bestellabgleich | Zwei tatsächliche Verbindungen; Menge und Einzelpreis innerhalb der jeweiligen Toleranz von 0,5 Prozent |
| Abgestimmter Betrag | 1500 Euro netto, offener Betrag 0 Euro |
| Zuständigkeit | Docs Admin A; Status **Genehmigung ausstehend** |
| Persönliche Freigabe | Genehmigung über die vorbereitete Freigabevorlage gespeichert |
| Export | **Abgeschlossen** in DocBits; tatsächlicher Exportverlauf und Empfang mit HTTP 200 |

## Prüfung und Freigabe konfigurieren

1. Vergleichen Sie Rechnungsnummer, Lieferant, Bestellreferenz und Summen mit dem Beleg. Übernehmen und speichern Sie die korrekten Positionen.
2. Öffnen Sie den **PO-Abgleich**, prüfen Sie beide Tabellen und starten Sie **Auto PO Match**. Kontrollieren Sie die Verbindungen, Toleranzen und Summen.
3. Erstellen Sie einen Standard Workflow mit **Dokumenttyp Ist Rechnung**. Begrenzen Sie den Schulungsfall zusätzlich über **Dokumentfeld → Rechnungsnummer → Entspricht** auf genau diesen Beleg.
4. Ergänzen Sie unter **Und** die Karte **Mit Bestellung vergleichen** mit **Ist**. Eine Bestellnummer allein belegt keinen Abgleich innerhalb der Toleranz.
5. Fügen Sie unter **Dann** die Benutzerzuweisung und die Änderung zu **Genehmigung ausstehend** hinzu. Im Beispiel steht **Workflows auslösen** auf **Falsch**.
6. Speichern Sie die Regel. Legen Sie im Test Manager ein eigenes Szenario mit den gespeicherten Dokumentdaten und der Statuserwartung an. Prüfen Sie zusätzlich das tatsächliche Dokument.
7. Konfigurieren Sie bei Bedarf die sprachabhängige Freigabevorlage im Layout Builder. Im Video werden eine Schaltfläche mit der Aktion **Genehmigen** und die benötigten Rechnungsfelder hinzugefügt.
8. Öffnen Sie die wartende Rechnung, vergleichen Sie die Angaben mit dem Beleg und genehmigen Sie sie persönlich.

Die Übergabe in den Status **Genehmigung ausstehend** ist noch keine Genehmigung. In diesem Beispiel war der Testadministrator dem Dokument bereits zugeordnet; das Video belegt keine Übergabe von einem anderen Benutzer.

## Den Export gezielt prüfen

Nach der Genehmigung steht die Rechnung zunächst auf **Exportfehler**, weil in der Schulungsorganisation noch keine passende Exportanbindung eingerichtet ist. Die Genehmigung selbst ist gespeichert. Thomas erstellt anschließend einen separaten, auf dieselbe Rechnungsnummer begrenzten Exportworkflow:

- Karte **Exportdokument mit Exportkonfiguration** und ausdrücklich ausgewählter temporärer Testempfänger.
- **Ausstehende Aufgaben ignorieren: Falsch**.
- **Status nach dem Export: Abgeschlossen**.

Der gezielte manuelle Test führt einen tatsächlichen Export aus. Thomas prüft danach den gespeicherten Dokumentstatus, den Exportverlauf mit Empfangsbestätigung und die beim unabhängigen Testempfänger eingegangenen Rechnungsdaten. Rechnungsnummer, Bestellnummer und Beträge stimmen überein.

{% hint style="info" %}
**Was die Nachweise bestätigen:** Die Testanzeige vergleicht hier den Status im internen Testdatensatz. Ein **Pass** allein ist deshalb kein Zustellnachweis. Der Export wird zusätzlich am wirklichen Dokument und beim Empfänger bestätigt. Der temporäre Empfänger zeigt die Zustellung, keine Buchung in einem ERP-System.
{% endhint %}

## Den Schulungsfall in den Betrieb übertragen

Beide Regeln bleiben während dieser Übung in der Liste ausgeschaltet und werden gezielt manuell getestet. Die Demonstration zeigt keine automatische Ausführung einer aktivierten Regel. Manuelle Tests können reale Änderungen und Exporte auslösen; verwenden Sie eigene Trainingsdokumente und ein dafür vorgesehenes Ziel.

Für den Betrieb müssen die passende Lizenz, Berechtigungen, Zuständigkeiten, Freigabevorlage und Exportkonfiguration vorhanden sein. Ergänzen Sie vor einer Aktivierung insbesondere die gewünschte Status- beziehungsweise Freigabebedingung des Exportworkflows. Die Rechnungsnummer allein ist keine allgemeine Freigabeprüfung. Die eigens angelegte Testanbindung und die temporären Freigabevorlagen wurden nach der Aufnahme entfernt.

<details>
<summary>Kapitel und Transkript</summary>

| Kapitel | Start |
| --- | --- |
| Thomas: Rechnung, Freigabe und Export | [0:00](https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/workflow-business-case-admin/v1/de.mp4#t=0.000) |
| Eine eigene Trainingsrechnung hochladen | [0:06](https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/workflow-business-case-admin/v1/de.mp4#t=6.167) |
| Kopf- und Summenfelder prüfen | [0:24](https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/workflow-business-case-admin/v1/de.mp4#t=24.125) |
| Die tatsächlichen Rechnungspositionen übernehmen | [0:52](https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/workflow-business-case-admin/v1/de.mp4#t=52.542) |
| Bestellpositionen abgleichen und das Ergebnis prüfen | [1:40](https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/workflow-business-case-admin/v1/de.mp4#t=100.125) |
| Die begrenzte Prüf- und Zuweisungsregel erstellen | [2:18](https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/workflow-business-case-admin/v1/de.mp4#t=138.042) |
| Die Prüfregel gezielt am echten Beleg testen | [3:46](https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/workflow-business-case-admin/v1/de.mp4#t=226.875) |
| Ein nutzbares Freigabeformular vorbereiten | [4:27](https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/workflow-business-case-admin/v1/de.mp4#t=267.917) |
| Die Rechnung persönlich freigeben | [5:06](https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/workflow-business-case-admin/v1/de.mp4#t=306.917) |
| Einen eigenen Exportworkflow auf den Testempfänger begrenzen | [5:42](https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/workflow-business-case-admin/v1/de.mp4#t=342.417) |
| Den gezielten Export ausführen | [6:39](https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/workflow-business-case-admin/v1/de.mp4#t=399.708) |
| Den Export in DocBits und beim Empfänger bestätigen | [7:08](https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/workflow-business-case-admin/v1/de.mp4#t=428.750) |
| Den Schulungsfall abgeschlossen prüfen | [7:53](https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/workflow-business-case-admin/v1/de.mp4#t=473.417) |

**Thomas: Rechnung, Freigabe und Export**

Heute begleite ich eine Rechnung durch Prüfung und Freigabe bis zum überprüften Export.

**Eine eigene Trainingsrechnung hochladen**

Für diesen Ablauf verwende ich eine eigene synthetische Rechnung. Sie hat zwei Positionen, eine Bestellnummer und einen Gesamtbetrag von siebzehnhundertfünfundachtzig Euro. Ich wähle die PDF-Datei aus, klassifiziere sie als Rechnung und lade sie hoch. Die eigentliche Verarbeitung überspringe ich im Schnitt. Nach der Verarbeitung prüfe ich genau dieses neue Dokument. Die zugehörige Bestellung ist bereits mit beiden Positionen importiert.

**Kopf- und Summenfelder prüfen**

Zuerst vergleiche ich die Rechnungsnummer mit dem Beleg und bestätige das Feld mit Enter. Dann prüfe ich den Lieferanten und die Bestellreferenz. Die Summen müssen ebenfalls stimmen: fünfzehnhundert Euro netto, zweihundertfünfundachtzig Euro Umsatzsteuer und siebzehnhundertfünfundachtzig Euro insgesamt. Danach öffne ich die Tabellenextraktion.

**Die tatsächlichen Rechnungspositionen übernehmen**

Hier wurden zunächst keine Positionen erkannt. Ich schalte den Trainingsmodus ein und starte die automatische Tabellenerkennung. Auch danach bleibt die Tabelle leer. Also markiere ich den Tabellenbereich direkt im Beleg, einschließlich der Überschrift und beider Positionen. Über das Speichersymbol lasse ich diesen Bereich auslesen. Jetzt erscheinen die beiden Zeilen. Beschreibung, Menge und Einzelpreis sind bereits zugeordnet. Die zusammengefasste erste Spalte ordne ich der Artikelnummer zu, die Nettospalte dem Nettobetrag. Danach beende ich den Trainingsmodus. Bei den beiden Artikelnummern entferne ich die mit erkannte Positionsnummer und vergleiche den Rest wieder mit dem Beleg. Abschließend speichere ich die korrigierten Daten. Für den Abgleich brauche ich jeweils die Artikelnummer aus der Bestellung.

**Bestellpositionen abgleichen und das Ergebnis prüfen**

Die Bestellnummer lädt die passende Bestellung. Damit sind die Bestellzeilen noch nicht mit den Rechnungspositionen verbunden. Ich prüfe zuerst beide Tabellen. Dann starte ich Auto PO Match. Beide Positionen sind jetzt verbunden. Bei Menge und Einzelpreis gelten jeweils null Komma fünf Prozent Toleranz. Hier stimmen die Werte sogar genau überein: zehn Stück zu hundert Euro und ein Stück zu fünfhundert Euro. DocBits zeigt Gespeichert, eine abgestimmte Summe von fünfzehnhundert Euro und einen offenen Betrag von null. Ich öffne die erste Verbindung, prüfe die zugehörige Bestellzeile und speichere den Abgleich noch einmal.

**Die begrenzte Prüf- und Zuweisungsregel erstellen**

Jetzt öffne ich die Workflow-Liste und erstelle die Regel für diesen Geschäftsfall. Ich gebe ihr einen eindeutigen Namen. So erkenne ich später, welche Regel für die Prüfung und Zuweisung zuständig ist. Unter Wenn stelle ich den Dokumenttyp auf Ist Rechnung. Diese erste Bedingung legt fest, für welche Art von Dokument die Regel überhaupt in Betracht kommt. Unter Und füge ich ein Dokumentfeld hinzu, wähle die Rechnungsnummer und den Vergleich Entspricht. Als Wert trage ich genau unsere Rechnungsnummer ein. Beide Bedingungen müssen zusammen erfüllt sein; andere Belege bleiben damit außerhalb dieses Schulungsfalls. Als weitere Bedingung wähle ich Mit Bestellung vergleichen und dann Ist. Die verbundenen Positionen müssen damit bei Menge und Preis innerhalb der Toleranz liegen. Eine Bestellnummer allein reicht dafür nicht. Unter Dann füge ich die Zuweisung an einen Benutzer hinzu. Ich suche unseren zuständigen Testadministrator und wähle ihn aus. Hier ist das Docs Admin A; für euren Betrieb gehört an diese Stelle die tatsächlich zuständige Person. Als nächste Aktion ändere ich den Dokumentstatus auf Genehmigung ausstehend. Zuweisung und Statusübergabe gehören hier zusammen. Damit wartet die Rechnung auf die persönliche Prüfung; sie ist durch diese Regel noch nicht genehmigt. Workflows auslösen setze ich hier auf Falsch. So startet diese Statusänderung keine weitere Workflow-Verarbeitung. Ich speichere die Regel und lasse sie für unseren gezielten manuellen Test in der Liste ausgeschaltet.

**Die Prüfregel gezielt am echten Beleg testen**

Für den manuellen Test lege ich ein gespeichertes Testszenario an. Ich wähle unsere Prüfregel und gebe dem Fall einen eindeutigen Namen. Die Eingabedatei enthält die gespeicherten Daten unserer Rechnung mit beiden Bestellverbindungen. Als erwartetes Ergebnis prüfe ich den Status Genehmigung ausstehend. Dann speichere ich den Fall und starte genau diesen Test. Für den gespeicherten Ergebnisstand lade ich die Testliste anschließend neu. Jetzt steht der Test auf Pass. Ich kehre zum Dashboard zurück und kontrolliere zusätzlich das tatsächliche Dokument: Unsere Rechnung wartet auf Genehmigung und ist Docs Admin A zugewiesen. Der Bestellabgleich bleibt erhalten.

**Ein nutzbares Freigabeformular vorbereiten**

Für die persönliche Freigabe braucht der Dokumenttyp auch eine Freigabevorlage. In dieser Testorganisation fehlt sie noch. Im Layout Builder bereite ich deshalb eine eigene deutsche Vorlage vor. Ich füge zunächst eine Gruppe und darin eine Schaltfläche hinzu. Als Aktion wähle ich Genehmigen und gebe dem Button eine verständliche Beschriftung. Aus den Dokumentfeldern ziehe ich Rechnungsnummer, Lieferantenname, Bestellung und Gesamtbetrag in die Vorlage. Diese Angaben sollen direkt neben dem Beleg sichtbar sein. Anschließend speichere ich die Vorlage und öffne unsere wartende Rechnung erneut. Die Vorlage gehört zu diesem Dokumenttyp und dieser Sprache.

**Die Rechnung persönlich freigeben**

Die Rechnung öffnet sich jetzt mit der vorbereiteten Freigabevorlage. Hier prüfe ich noch einmal die Rechnungsnummer, den Lieferanten, die Bestellnummer und den Gesamtbetrag gegen den Beleg. Jetzt klicke ich auf Genehmigen. Die Freigabe wird gespeichert und DocBits kehrt zum Dashboard zurück. Als erster Genehmiger ist unser Testadministrator hinterlegt. Danach steht die Rechnung allerdings auf Exportfehler. Es gibt in dieser Testorganisation noch keine Exportanbindung. Die gespeicherte Genehmigung belegt also noch keinen erfolgreichen Export. Den prüfe ich jetzt separat.

**Einen eigenen Exportworkflow auf den Testempfänger begrenzen**

Für den Export verwende ich einen eigenen temporären Testempfänger. Seine Anbindung ist bereits vorbereitet und für die allgemeine Exportauswahl ausgeschaltet. In der Workflow-Liste erstelle ich dafür eine zweite, klar benannte Regel und wähle wieder Rechnung als Dokumenttyp. Auch diese Regel begrenze ich unter Und auf das Dokumentfeld Rechnungsnummer. Ich wähle Entspricht und trage die Nummer unseres Schulungsbelegs ein. Andere Rechnungen sollen von dieser Regel nicht erfasst werden. Unter Dann füge ich Exportdokument mit Exportkonfiguration hinzu. In der Karte wähle ich gezielt unseren temporären Testempfänger aus. Die ausgeschaltete Konfiguration lässt sich hier ausdrücklich für diesen einzelnen Workflow angeben. Ausstehende Aufgaben ignorieren setze ich auf Falsch. Offene Aufgaben sollen einen Export also weiterhin verhindern. Als Status nach erfolgreichem Export bleibt Abgeschlossen eingestellt. Auch diese Regel speichere ich und lasse sie ausgeschaltet.

**Den gezielten Export ausführen**

Nun lege ich ein eigenes manuelles Szenario für den Exportworkflow an. Ich wähle die gespeicherte Regel, benenne den Fall und lade die Daten der bereits genehmigten Rechnung. Danach speichere ich das Szenario. Ich starte genau diesen Fall. Wichtig ist die Grenze der Testanzeige: Der erwartete Status bezieht sich hier auf den internen Testdatensatz. Ein Pass allein bestätigt deshalb noch keine Zustellung. Jetzt prüfe ich den wirklichen Dokumentstatus und den Exportverlauf.

**Den Export in DocBits und beim Empfänger bestätigen**

Zurück im Dashboard steht unsere Rechnung auf Abgeschlossen. Im Exportverlauf öffne ich den tatsächlichen Eintrag für den Testempfänger. Das Ergebnis ist erfolgreich; in der Antwort stehen die Empfangsbestätigung und eine eigene Belegkennung. Zusätzlich öffne ich den unabhängigen Testempfänger. Hier ist eine echte Dokumentexport-Anfrage angekommen. Dokumentnummer und Dateiname stimmen mit unserer Rechnung überein. Der Empfänger hat mit HTTP zweihundert geantwortet. In den empfangenen Feldern stehen die Bestellnummer und die erwarteten Beträge: fünfzehnhundert Euro netto, zweihundertfünfundachtzig Euro Steuer und siebzehnhundertfünfundachtzig Euro insgesamt. Damit ist die Zustellung an diesen Testempfänger nachgewiesen. Eine Buchung in einem ERP-System zeigt dieser Test nicht.

**Den Schulungsfall abgeschlossen prüfen**

Damit ist die Rechnung durchgängig geprüft: Positionen übernommen, Bestellung abgeglichen, Zuständigkeit und Freigabe übergeben, persönlich genehmigt und beim Exportempfänger bestätigt. Die beiden Schulungsregeln bleiben inaktiv. Für den Betrieb würde ich erst die passende Freigabe- und Exportkonfiguration prüfen und die Regeln danach gezielt aktivieren.

</details>

## Weiterführende Seiten

- [Einen Standard Workflow erstellen und testen](standard-workflow-builder.md#standard-workflow-tutorial)
- [Workflow-Änderungen mit Regressionstests prüfen](workflow-regression-tests.md)
- [PO-Abgleich](cards-overview/po-matching-complete-guide.md)
