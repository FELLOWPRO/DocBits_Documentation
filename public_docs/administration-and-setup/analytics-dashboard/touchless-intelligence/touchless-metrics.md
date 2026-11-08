# Kennzahlen und Berechnung

<!-- touchless-admin-video-v2-20261104:start -->
**Videokapitel (Prüffassung):** [Die Quoten berechnen](https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/touchless-intelligence-preview-admin/v2/en.html#chapter=03).
<!-- touchless-admin-video-v2-20261104:end -->

### Korrekte Extraktion und ein touchless Prozess sind zweierlei

**DocBits kann jeden Rechnungswert korrekt lesen, und die Rechnung kann trotzdem AP-Aufmerksamkeit brauchen, weil die Daten des Quellsystems abweichen.** AP steht für Accounts Payable, also die Gruppe, die Lieferantenrechnungen bearbeitet. Prüfen Sie diese beiden Fragen getrennt:

| Frage | Vergleich | Was das Ergebnis Ihnen sagt |
| --- | --- | --- |
| **Hat DocBits das Dokument korrekt gelesen?** | Die Originalrechnung gegen die extrahierten Kopffelder und Tabellenzeilen, vor jeder manuellen Korrektur | Extraktionsqualität: Stimmt der extrahierte Wert mit dem überein, was tatsächlich auf der Rechnung steht? |
| **Konnte der Prozess ohne Eingriff abgeschlossen werden?** | Die korrekt extrahierte Rechnung gegen die Bestellung und die von Infor ERP gelieferten Stammdaten, zusammen mit der aufgezeichneten Verarbeitungshistorie | Prozessautomatisierung: Konnten die konfigurierten Prüfungen, der Abgleich und der Export ohne Korrektur oder Neustart abgeschlossen werden? |

Ein abweichender Wert in Infor sagt für sich genommen nicht, welche Seite falsch liegt. Prüfen Sie die Rechnung, den vereinbarten Auftrag und die tatsächlich nach DocBits importierten Daten. Die Quelle kann falsch sein, der Import kann veraltet sein, oder der Lieferant hat einen anderen Wert in Rechnung gestellt.

{% hint style="info" %}
**Die Touchless-Quote misst den Prozess, nicht die Extraktionsgenauigkeit.** Ein AP-assisted Dokument beweist keinen Extraktionsfehler von DocBits. Umgekehrt beweist eine bestandene Extraktionsstufe oder ein hoher Confidence-Score nicht, dass jeder Wert korrekt ist. Das stellen Sie nur fest, indem Sie das Originaldokument mit den extrahierten Werten vergleichen.
{% endhint %}

Jedes Dokument endet in genau **einem** Ergebnis:

| Ergebnis              | Bedeutung                                                                                           | Zählt in die Quote                                                                          |
| --------------------- | --------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------ |
| **Pure touchless**    | Vom Import bis zum Export verarbeitet, **ganz ohne menschliches Zutun**                             | Ja, als Erfolg                                                                             |
| **AP touchless**      | Lief automatisch, und eine Person gab nur die **fachliche Freigabe**. Es war keine Korrektur nötig  | Ja, als Erfolg                                                                             |
| **AP assisted**       | Erfolgreich abgeschlossen, aber eine Person musste **ein Feld korrigieren, das Dokument neu starten** oder anderweitig eingreifen; das kann auch dann nötig sein, wenn die Extraktion korrekt war | Ja, außerhalb des Touchless-Zählers; es benennt für sich genommen nicht die Ursache |
| **Process exception** | Endete mit einem **Fehler**, wurde **abgelehnt**, **vom ERP zurückgewiesen** oder **blieb in der Pipeline hängen** | Ja, als Fehlschlag                                                                         |
| **In progress**       | Noch nicht abgeschlossen                                                                            | **Nein**. Es gibt noch kein Ergebnis                                                       |
| **Not eligible**      | Gelöscht, archiviert, ein Testdokument oder ein ausgeschlossener Dokumenttyp                        | **Nein**                                                                                   |

Die **AP-Touchless-Quote**, einschließlich der Dokumente, bei denen nur freigegeben wurde, lautet:

```
rate = (Pure touchless + AP touchless)
       ÷ (Pure touchless + AP touchless + AP assisted + Process exception)
```

Hier meint **AP touchless** im Zähler das Dokumentergebnis „nur Freigabe“. Der **AP-touchless-Prozentsatz** im Dashboard ist die kombinierte Quote: reine Dokumente plus Dokumente mit reiner Freigabe. **Addieren Sie die beiden angezeigten Prozentsätze nicht.** Die reine Quote verwendet im Zähler nur reine Dokumente, bei gleichem Nenner.

Dokumente, die noch **in progress** oder **not eligible** sind, fließen nie in die Berechnung ein. Das schützt die Quote: Ein Dokument, das vor fünf Minuten eingegangen ist, kann sie nicht nach unten ziehen.

{% hint style="info" %}
**Eine Berührung zählt dauerhaft.** Sobald eine Person ein Dokument berührt hat, bleibt es als berührt gezählt, auch wenn ein späterer automatischer Lauf niemanden gebraucht hätte. **Ein Neustart des Dokuments macht es nicht wieder touchless.** Die Quote bildet die Arbeit ab, die tatsächlich stattgefunden hat.
{% endhint %}

### Beispielrechnung (illustrative Zahlen)

In 30 Tagen sind 200 Dokumente eingegangen:

| Ergebnis                      | Dokumente |
| ----------------------------- | --------- |
| Pure touchless                | 120       |
| AP touchless                  | 30        |
| AP assisted                   | 30        |
| Process exception             | 10        |
| In progress                   | 8         |
| Not eligible (Testdokumente)  | 2         |

* Nenner: 120 + 30 + 30 + 10 = **190**. Die 8 Dokumente mit Status in progress und die 2 nicht teilnahmeberechtigten Dokumente bleiben außen vor.
* **Pure touchless**: 120 ÷ 190 = **63,2 %**
* Anteil mit **nur Freigabe**: 30 ÷ 190 = **15,8 %**. Das ist der Anteil dieses Ergebnisses, nicht die kombinierte AP-Touchless-Quote.
* **AP-Touchless-Quote**: (120 + 30) ÷ 190 = **78,9 %**

Der Tab zeigt ein **Ziel** (70 %, sofern Ihre Organisation kein anderes verwendet). In diesem Beispiel liegt die kombinierte AP-Quote über 70 %, während die reine Quote von 63,2 % darunter liegt. Vergleichen Sie das Ziel mit der Quote, die die jeweilige Karte oder Grafik ausweist.

Klicken Sie oben rechts auf **How touchless is calculated**, um diese Erklärung innerhalb von DocBits zu öffnen, mit den Zahlen Ihres eigenen Zeitraums (Dokumente im Zeitraum, noch in progress, ausgeschlossen, gemessen).

<figure><img src="https://raw.githubusercontent.com/FELLOWPRO/DocBits_Documentation/refs/heads/main/public_docs/.gitbook/assets/touchless-report-methodology-en-20261104.png" alt="Aktuelle Trainingspopulation: 201 teilnahmeberechtigte abgeschlossene Rechnungen, keine noch in Verarbeitung und keine ausgeschlossen. Die 107 vollautomatischen Rechnungen ergeben 53,2 %; mit 11 Rechnungen mit reiner Freigabe sind es 118 und 58,7 %. Diese Prozessquoten messen nicht die Extraktionsgenauigkeit."><figcaption><p>Aktuelle Trainingspopulation: 201 teilnahmeberechtigte abgeschlossene Rechnungen, keine noch in Verarbeitung und keine ausgeschlossen. Die 107 vollautomatischen Rechnungen ergeben 53,2 %; mit 11 Rechnungen mit reiner Freigabe sind es 118 und 58,7 %. Diese Prozessquoten messen nicht die Extraktionsgenauigkeit.</p></figcaption></figure>
<!-- English source image: touchless-report-methodology-en-20261104.png -->

### Beispiel: 100 % korrekt extrahiert, 80 % AP touchless

Nehmen Sie an, eine Prüfung der Originalrechnungen und ihrer extrahierten Werte bestätigt, dass **alle 100 abgeschlossenen, teilnahmeberechtigten Rechnungen korrekt extrahiert wurden**. Ihre Verarbeitungsergebnisse sind:

| Was passiert ist | Dokumente | Ergebnis |
| --- | --- | --- |
| Rechnung und Quelldaten stimmten überein; der gesamte Prozess lief automatisch durch | 70 | Pure touchless |
| Rechnung und Quelldaten stimmten überein; es war nur die fachliche Freigabe nötig | 10 | AP touchless (Ergebnis „nur Freigabe“) |
| Die Rechnungsdaten wurden korrekt extrahiert, aber die importierten Infor-Daten wichen ab. AP klärte die Abweichung und startete die Dokumente in DocBits nach der Korrektur der Quelldaten manuell neu; danach liefen sie erfolgreich durch | 20 | AP assisted |

* **Korrekt extrahierte Dokumente in dieser geprüften Stichprobe:** 100 ÷ 100 = **100 %**.
* **Pure-Touchless-Quote:** 70 ÷ 100 = **70 %**.
* **AP-Touchless-Quote:** (70 + 10) ÷ 100 = **80 %**.

Das ist kein Widerspruch: Die Extraktion war bei allen Rechnungen korrekt, während 20 wegen der Quelldaten einen Eingriff in die Verarbeitung brauchten. Die **Angabe von 100 % Extraktion ist ein illustratives Ergebnis einer separaten Dokumentprüfung**, kein zusätzlicher KPI, den dieses Dashboard ausweist. Berechnen Sie sie nicht allein aus den Touchless-Ergebnissen.

### Beispiele: Was musste AP tatsächlich tun?

Die folgenden Fälle sind illustrativ und nicht die einzelnen Dokumente hinter den Screenshots. Die erfolgreichen Ergebnisse setzen voraus, dass die Verarbeitung abgeschlossen ist, einschließlich der erforderlichen ERP-Bestätigung.

| Fall | Originalrechnung / DocBits-Extraktion / Quelldaten | Aktion von AP und Ergebnis | Wo Sie nachforschen |
| --- | --- | --- | --- |
| **Extraktionsfehler** | Bestellnummer `45001234` / falsch extrahiert als `45001284` / der korrekte Auftrag `45001234` existiert in Infor | AP korrigiert die extrahierte Nummer; die Rechnung endet als **AP assisted** | Extraktion für diesen Lieferanten |
| **Abweichung im Quellsystem** | Stückpreis 10,00 € / korrekt extrahiert 10,00 € / die importierte Infor-Bestellung sagt 9,00 €, außerhalb der konfigurierten Toleranz | AP bestätigt, dass 10,00 € der vereinbarte Preis ist, veranlasst die Korrektur der Bestellung und startet die Rechnung in DocBits manuell neu; sie endet als **AP assisted** | Bestelldaten in Infor und deren Import |
| **Verzögerung beim Import** | Die Bestellnummer ist auf der Rechnung und in DocBits korrekt / die Bestellung existiert in Infor, hat DocBits aber noch nicht erreicht | Wenn ein späterer Import und ein erneuter Versuch ohne aufgezeichneten menschlichen Eingriff oder Freigabe automatisch durchlaufen, kann das Ergebnis **Pure touchless** bleiben. Ein manueller Neustart mit anschließendem Erfolg ergibt **AP assisted** | Zeitpunkt des Imports und die tatsächliche Laufhistorie |
| **Ablehnung durch das ERP** | Die Extraktion ist korrekt, aber das ERP weist das exportierte Dokument zurück | **Process exception**, solange es als endgültige ERP-Ablehnung eingestuft ist, auch wenn jemand zuvor eingegriffen hat | ERP-Ablehnung und Nachweise zum Export |

**Selbst eine kleine aufgezeichnete Korrektur oder ein manueller Neustart zählt als Eingriff.** AP assisted bedeutet „eine Person hat bei der Verarbeitung des Dokuments geholfen“; es ist nicht der Name eines eigenen KI-Assistenten. Ein Problem mit den Quelldaten und ein Extraktionsproblem können daher dasselbe Ergebnis haben und trotzdem unterschiedliche Korrekturen erfordern.

Die Einstufung verwendet die Ereignisse, die DocBits aufzeichnet. Gehen Sie nicht davon aus, dass Arbeit, die nur in Infor geleistet wurde, ohne entsprechendes aufgezeichnetes DocBits-Ereignis automatisch als AP-Eingriff zählt. Behalten Sie diese Arbeit ebenfalls in der Diagnose im Blick.

### Welche AP-Aktionen als Eingriff zählen

Das Folgende setzt einen erfolgreichen Abschluss voraus, einschließlich der erforderlichen ERP-Bestätigung. Entscheidend sind die aufgezeichnete Aktion und ihr Urheber, nicht die Dauer der Arbeit.

| Aktion | Wirkung auf das Dokumentergebnis |
| --- | --- |
| Öffnen, lesen, filtern, vergleichen oder eine Vorschau ansehen | Erzeugt für sich genommen keinen Eingriff in die Verarbeitung; Pure Touchless bleibt möglich |
| Fachliche Freigabe erteilen, auch eine zweite Freigabe | AP Touchless, wenn kein Eingriff in die Verarbeitung vorlag |
| Ein Kopffeld oder eine Tabellenzelle ändern und speichern | AP Assisted; selbst eine gespeicherte Korrektur zählt |
| Ein Dokument manuell validieren und weiterleiten, auch ohne einen Wert zu korrigieren | AP Assisted; manuelle Validierung ist nicht dasselbe wie reine Freigabe |
| Die Verarbeitung oder den Export manuell neu starten | AP Assisted; ein späterer automatischer Lauf hebt den Eingriff nicht auf |
| Automatischer System-Retry oder automatisches Schreiben eines Workflows | Erzeugt für sich genommen keinen menschlichen Eingriff; frühere menschliche Berührungen bleiben bestehen |
| Daten nur in Infor korrigieren | Externe Arbeit ist nicht automatisch ein aufgezeichnetes DocBits-Ereignis; dokumentieren Sie sie separat und prüfen Sie die anschließende Aktion in DocBits |
| Endgültige Ablehnung durch das ERP nach einer Korrektur | Process exception hat Vorrang; der Eingriff bleibt in der Historie erhalten |

Ein Klick auf Save ohne Nachweis eines geänderten Werts belegt keine Korrektur. Prüfen Sie, ob er auch eine manuelle Validierung oder einen Neustart ausgelöst hat.

### Das AP-Label hat zwei Bedeutungen

| Stelle | Bedeutung |
| --- | --- |
| AP-Prozentsatz in der Kopfzeile | Kombiniert Pure + nur Freigabe: (120 + 30) / 190 = 78,9 % |
| Dokumentenzahl unter diesem Prozentsatz im aktuellen Bericht | Kombiniert Pure + nur Freigabe: 150 = 120 + 30 |
| Ergebnis-Kategorie AP Touchless, etwa der MCP-Bucket `AP_TOUCHLESS` | Eigene Kategorie „nur Freigabe“: 30 / 190 = 15,8 % |
| Blaue AP-Linie im aktuellen [Dashboard-Trend-Screenshot](touchless-dashboard.md) | Kombinierte Quote aus Pure + nur Freigabe an jedem Punkt, mit der Population dieses Punktes |

Die endgültigen Ergebnis-Kategorien summieren sich auf 100 % der gemessenen Population. Die Prozentsätze für Pure und für das kombinierte AP überlappen sich und dürfen nicht addiert werden.

### Wie aktuell die Zahlen sind

Ergebnisse werden **alle 15 Minuten neu berechnet**. Das Ergebnis eines Dokuments kann sich noch ändern, nachdem es zum ersten Mal erscheint: Das ERP bestätigt einen Export unter Umständen erst Stunden später. Die Zeile **Data as of …** am unteren Rand des Tabs zeigt, wann die Zahlen zuletzt berechnet wurden.





## Verwandte Seiten

* [Touchless Intelligence](./)
* [Das Dashboard verwenden](touchless-dashboard.md)
* [Durchgerechnete Beispiele: Preis und Menge](touchless-examples.md)
* [Supplier Diagnosis and Issue Clusters](touchless-supplier-diagnosis.md)
* [PO Matching Diagnosis](touchless-po-matching-diagnosis.md)
* [Document Trace](touchless-document-trace.md)
* [Change Proposals and Reports](touchless-change-proposals.md)
* [Touchless mit MCP erklären und verbessern](touchless-mcp.md)

<!-- Documentation review 2026-11-04: extraction quality vs process outcomes; KPI and terminal-outcome definitions checked against DocBits_API c51f350c728acb8ac964098d15f7b006bce273f4, module/automation_intelligence/kpi.py and bucket.py. Existing native screenshots retained and checked separately from illustrative examples. -->
<!-- Completion review 2026-11-04: owned synthetic PO examples, MCP schema/read evidence, human-action classification, KPI labels and screenshot proof limits. -->
