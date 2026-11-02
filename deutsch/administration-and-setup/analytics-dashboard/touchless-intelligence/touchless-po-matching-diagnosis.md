# Bestellabgleich-Diagnose

## Übersicht

Viele Rechnungen bleiben bei der Bestellung stehen. Die Rechnung sagt das eine, die Bestellung (PO) etwas anderes, und DocBits kann nicht selbst entscheiden, ob beide zusammengehören. Jedes solche Dokument braucht eine Person, ist also **nicht touchless**.

Touchless Intelligence zeigt Ihnen, **warum** ein Bestellabgleich gescheitert ist und **wie** DocBits abgleichen wollte. Diese Seite erklärt die beiden beteiligten Pipeline-Schritte, die Gründe, die Sie sehen werden, und den **Entscheidungsablauf des Bestellabgleichs**, ein Diagramm, das die Abgleichschritte nacheinander zeigt.

### Wo Sie den Bestellabgleich in Touchless Intelligence sehen

| Wo                                                                                               | Was Sie sehen                                                                                                                                                                 |
| ------------------------------------------------------------------------------------------------ | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Wo Touchless zuerst verloren geht** (Übersichts-Tab)                                           | Ein Balken wie _Bestellpositionsabgleich: PO-Positionsabweichung_. Er zeigt, wie viele Dokumente dort stehen geblieben sind                                                   |
| **Lieferantenpotenziale**                                                                        | Ein Lieferant mit der Grundursache **Bestellabgleich**                                                                                                                        |
| **Lieferantendiagnose**, Abschnitt **Wie diese Organisation abgleicht** und das **Fehlermuster** | Der Entscheidungsablauf mit dem Regelsatz Ihrer Organisation                                                                                                                  |
| **Dokumentverlauf**                                                                              | Der Schritt **Bestellpositionsabgleich** mit dem Status **blockiert** und dem Grund                                                                                           |
| **Einstellungen → Dokumenttypen → Weitere Einstellungen → Bestellung**                           | Die Abgleichregeln selbst. Siehe [Purchase Order Matching Rules](../../settings/global-settings/document-types/more-settings/purchase-order/purchase-order-matching-rules.md) |

## Die zwei Bestellschritte

| Schritt                           | Frage                                                  | Stoppt mit                                                                                                                                      |
| --------------------------------- | ------------------------------------------------------ | ----------------------------------------------------------------------------------------------------------------------------------------------- |
| **9 · Bestellsuche**              | Gibt es eine Bestellung zu dieser Rechnung?            | _Bestellung nicht gefunden_                                                                                                                     |
| **10 · Bestellpositionsabgleich** | Passt jede Rechnungsposition zu einer Bestellposition? | _PO-Positionsabweichung_, _PO-Positionskennung abweichend_, _Stückpreis außerhalb der Bestell-Toleranz_, _Menge außerhalb der Bestell-Toleranz_ |

Ein Dokument, das bei Schritt 9 oder 10 stehen bleibt, erscheint in der Lieferanten-Warteschlange mit dem ersten Blocker **Bestellabgleich**.

## Gründe, warum ein Bestellabgleich scheitert

| Grund, den Sie sehen                          | Was er bedeutet                                                                                                              | Typische Ursache                                                                                                                                 | Was zu ändern ist                                                                                                                                                                                |
| --------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| **Bestellung nicht gefunden**                 | DocBits hat zur Bestellnummer auf der Rechnung keine Bestellung gefunden                                                     | Die Bestellnummer wird falsch gelesen oder fehlt; die Bestellung wurde noch nicht importiert; die Bestellung gehört zu einem anderen Lieferanten | Prüfen Sie die Extraktion der Bestellnummer für diesen Lieferanten, den Import der Bestellstammdaten und die Verknüpfung mit dem Lieferanten                                                     |
| **PO-Positionsabweichung**                    | Die Rechnungspositionen passten nicht zu den Bestellpositionen                                                               | Der Lieferant verwendet eigene Artikelnummern; die Beschreibung weicht ab; Positionen wurden zusammengeführt oder aufgeteilt                     | Prüfen Sie die Zuordnung der Artikelnummern und die **Regelprioritäten** in den Abgleichregeln; fügen Sie eine Regel für die Art hinzu, wie der Lieferant Positionen kennzeichnet                |
| **PO-Positionskennung abweichend**            | Die Positionsnummer oder Kennung auf der Rechnung passt nicht zur Bestellung                                                 | Der Lieferant nummeriert Positionen neu                                                                                                          | Gleichen Sie nach Artikel und Menge statt nach Positionsnummer ab                                                                                                                                |
| **Stückpreis außerhalb der Bestell-Toleranz** | Der Preis weicht stärker ab als die erlaubte Toleranz                                                                        | Eine echte Preisänderung, eine Rundungsdifferenz oder eine andere Preiseinheit                                                                   | Prüfen Sie die **Toleranz Stückpreis** (Unit price tolerance) im Regelsatz; korrigieren Sie die Bestellung oder fragen Sie den Lieferanten                                                       |
| **Menge außerhalb der Bestell-Toleranz**      | Die Menge weicht stärker ab als die erlaubte Toleranz                                                                        | Teillieferung, Überlieferung                                                                                                                     | Prüfen Sie **Menge abgleichen auf** (Match quantity on) und die **Toleranz Menge** (Quantity tolerance)                                                                                          |
| **Fehler im Bestellabgleich-Dienst**          | Der Abgleichdienst konnte nicht antworten                                                                                    | Ein vorübergehendes technisches Problem                                                                                                          | Starten Sie die Dokumente neu; wenden Sie sich an den Support, wenn es wieder auftritt                                                                                                           |
| **Automatischer Bestellexport deaktiviert**   | Die Einstellung **Auto export if PO matched 100%** ist aus, daher werden abgeglichene Dokumente nicht automatisch exportiert | Die Einstellung ist aus                                                                                                                          | Schalten Sie die Einstellung ein, wenn Sie den automatischen Export wünschen. Siehe [Auto Export if PO Matched 100%](../../settings/document-processing/module/auto-export-if-po-matched-100.md) |

{% hint style="info" %}
Nicht jeder Grund im Bestellabgleich lässt sich in DocBits beheben. Sendet der Lieferant eine falsche Bestellnummer, steht auf der Karte **Nur Lieferantenaktion**: Der Lieferant muss das Dokument korrigieren und erneut senden.
{% endhint %}

## Der Entscheidungsablauf des Bestellabgleichs

Der Entscheidungsablauf zeigt, wie DocBits versucht, eine Rechnungsposition mit einer Bestellposition abzugleichen. Er hat **fünf Stufen**, und der erste Treffer gewinnt:

1. **Einzelabgleich-Validierung** (Single match validation): Die Regeln werden nach Priorität angewendet. Das ist der Normalfall, eine Rechnungsposition und eine Bestellposition
2. **Mehrfachabgleich-Validierung** (Multi match validation): nach einem Einzelabgleich, wenn auf einer Seite mehrere Positionen beteiligt sind
3. **Summenabgleich-Validierung** (Total match validation): nur, wenn gar nichts gepasst hat. Die Summe der Bestellposition wird mit der Summe ihrer Tabellenpositionen verglichen
4. **Einzelabweichungs-Validierung** (Single mismatch validation): Der Stückpreis wird ignoriert, sodass eine Position nach Artikel und Menge abgeglichen werden kann, auch wenn der Preis abweicht
5. **Fallback-Logik** (Fallback logic): Es bleiben eine Bestellposition und eine Tabellenposition übrig, also werden sie einander zugeordnet

Innerhalb der Stufen probiert DocBits in dieser Reihenfolge:

* **Exakter Abgleich für alle Regeln**: Jeder verglichene Wert ist identisch
* **Toleranzbasierter Abgleich**: Numerische Werte dürfen innerhalb der Toleranz abweichen
* **Verpackungskriterien**: der letzte Durchgang, basierend auf den verpackungsbezogenen Kriterien des Regelsatzes

Jeder Schritt fragt **Treffer gefunden?** Die Antwort **Ja** (grün) führt zu **Treffer gefunden**, und das Dokument läuft weiter. Die Antwort **Kein Treffer** (rot) führt zum nächsten Schritt, und nach dem letzten Schritt lautet das Ergebnis **Kein Treffer gefunden**: Das Dokument bleibt stehen und braucht eine Person.

<figure><img src="../../../.gitbook/assets/touchless-po-matching-flow-de.png" alt="Der Entscheidungsablauf des Bestellabgleichs: Kopfzeile mit dem Regelsatz, fünf nummerierte Abgleichstufen mit ihren Durchgängen und die Endpunkte Treffer gefunden und Kein Treffer gefunden"><figcaption><p>Der Entscheidungsablauf des Bestellabgleichs, geöffnet über <strong>Wie diese Organisation abgleicht</strong> auf der Seite Lieferantendiagnose. Die Kopfzeile zeigt den Regelsatz (Version 7, im Besitz dieser Organisation) und die Toleranzen. Darunter laufen die fünf Stufen mit ihren Durchgängen von oben nach unten. Grün führt zu <strong>Treffer gefunden</strong>, rot führt zum nächsten Schritt und endet in <strong>Kein Treffer gefunden</strong>. Beispielorganisation mit Demodaten.</p></figcaption></figure>

### Was die Kopfzeile des Diagramms Ihnen sagt

| Feld                                         | Bedeutung                                                                                                                |
| -------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------ |
| **Dokumenttyp**                              | Der Dokumenttyp, zu dem der Regelsatz gehört, zum Beispiel INVOICE                                                       |
| **Version des Regelsatzes**                  | Die Version der Abgleichregeln, zum Beispiel v3                                                                          |
| **Eigentümer des Regelsatzes**               | **Diese Organisation** (Ihre eigenen Regeln) oder **Mitgelieferter Standard-Regelsatz** (die Standardregeln von DocBits) |
| **Veröffentlicht**                           | Wann die Version veröffentlicht wurde                                                                                    |
| **Menge abgleichen auf**                     | Welche Menge verglichen wird (bestellte Menge, offene Menge)                                                             |
| **Toleranzbetrag**                           | Ob die Toleranzen aus den Attributen des Dokumenttyps oder aus dem Regelsatz stammen                                     |
| **Toleranz Stückpreis** / **Toleranz Menge** | Wie stark ein Preis oder eine Menge abweichen darf                                                                       |
| **Standardtoleranz**                         | Die Toleranz für alle anderen numerischen Werte                                                                          |

Im Beispiel oben zeigen die Toleranzen **nicht konfiguriert** und **nicht in Kraft: Attribut entscheidet**. Das heißt: Der Regelsatz selbst hat keine eigene Toleranz, und die Zeile **Toleranzbetrag** sagt, dass die Toleranzen aus den **Attributen des Dokumenttyps** kommen. Eine Toleranz entscheidet nur, wenn sie in Kraft ist. Lesen Sie diese Zeile zuerst, wenn eine Preis- oder Mengenabweichung Dokumente blockiert: Sie sagt Ihnen, **wo** Sie die Toleranz ändern müssen.

Der Zustand des Regelsatzes wird als Hinweis angezeigt: **Aktive Version** (diese Regeln entscheiden), **Genehmigt, nicht aktiv**, **Entwurf, noch nicht in Kraft** oder **Versionsstatus unbekannt**. Nur die aktive Version entscheidet.

Haben Transformationsregeln ein Dokument vor dem Abgleich verändert, sagt das Diagramm es, zum Beispiel _2 angewendet: (Namen)_ oder _„(Regel)“ hat (Tabelle) neu aufgebaut: Hier ging der Bestellabgleich verloren_. Das ist eine häufige versteckte Ursache: Eine Regel, die eine Tabelle umformatiert, kann einen Abgleich zerstören, der vorher funktioniert hat.

## Beispiele

Die Zahlen in den Beispielen dienen der Veranschaulichung.

### Beispiel 1: Preis innerhalb der Toleranz

Eine Rechnungsposition hat einen Stückpreis von **10,40**. Die Bestellposition sagt **10,00**. Die Toleranz für den Stückpreis beträgt **5 %**.

* Der **exakte Abgleich** scheitert (10,40 ist nicht 10,00).
* Der **toleranzbasierte Abgleich** gelingt: Die Abweichung beträgt **4 %** und liegt damit innerhalb von 5 %.
* Die Position ist abgeglichen. **Treffer gefunden.**

Bei einer Toleranz von **3 %** scheitert auch der toleranzbasierte Abgleich. Nach allen Stufen bleibt das Dokument mit **Stückpreis außerhalb der Bestell-Toleranz** stehen. Das Diagramm zeigt genau diesen Weg, und die Lösung ist entweder die Toleranz (wenn 4 % für Ihr Geschäft akzeptabel sind) oder eine Korrektur beim Lieferanten.

### Beispiel 2: Die Artikelnummern des Lieferanten weichen von Ihren ab

Ein Lieferant stellt den Artikel **„A-4711-X“** in Rechnung, Ihre Bestellung sagt **„4711“**. Keine Regel vergleicht die beiden, also wird kein Treffer gefunden, und Touchless Intelligence fasst alle Rechnungen dieses Lieferanten in einem Cluster zusammen: **Bestellpositionsabgleich, PO-Positionsabweichung**, 27 Dokumente.

* Im Cluster lesen Sie _27 betroffen, 27 rückgewinnbar_, erwarteter Zuwachs zum Beispiel **+8,7 PP**.
* Die Lösung liegt auf Ihrer Seite: Fügen Sie eine Regel hinzu oder ändern Sie die Reihenfolge, sodass nach der Artikelnummer des Lieferanten oder nach der Beschreibung abgeglichen wird, oder pflegen Sie die Artikelnummern des Lieferanten in den Stammdaten.
* Nachdem Sie die Regel geändert haben, wenden Sie die Änderung mit einem [Änderungsvorschlag](touchless-change-proposals.md) an und lesen zwei Wochen später die **Änderungshistorie**: Pure-Quote vorher und nachher.

### Beispiel 3: Die Bestellung ist noch nicht da

Rechnungen treffen ein, bevor die Bestellung importiert wurde. Sie bleiben bei der **Bestellsuche** mit **Bestellung nicht gefunden** stehen. Das Cluster zeigt eine kurze Spitze. Die Lösung liegt in der Reihenfolge Ihrer Prozesse oder im Zeitplan des Bestellimports, nicht in den Abgleichregeln. Prüfen Sie **Wo Touchless zuerst verloren geht**: Ein Balken _Bestellsuche: Bestellung nicht gefunden_, der nach jeder Importlücke wächst, deutet auf diese Ursache hin.

### Beispiel 4: Eine Regel hat die Tabelle neu aufgebaut

Nachdem eine Transformationsregel für die Tabelle eines Lieferanten in Kraft getreten war, fiel die Abgleichquote dieses Lieferanten stark ab. Das Diagramm eines betroffenen Dokuments sagt _„(Regel)“ hat (Tabelle) neu aufgebaut: Hier ging der Bestellabgleich verloren_. Die Lösung ist, die Transformationsregel anzupassen oder rückgängig zu machen, nicht die Abgleichregeln.

## Eine Routine für Probleme beim Bestellabgleich

1. Öffnen Sie **Wo Touchless zuerst verloren geht**. Liegt ein Schritt des Bestellabgleichs unter den ersten drei?
2. Öffnen Sie die **Lieferantenpotenziale** und sortieren Sie nach **Erwartetem Zuwachs**. Nehmen Sie den Lieferanten mit der Grundursache **Bestellabgleich** und dem Status **RECOVERABLE**.
3. Öffnen Sie die **Lieferantendiagnose** und lesen Sie das Cluster: Grund, betroffene Dokumente, **Was zu ändern ist**, **Fehlende Evidenz**.
4. Öffnen Sie **Wie diese Organisation abgleicht** und prüfen Sie den Regelsatz: Version, Eigentümer und Toleranzen.
5. Öffnen Sie ein **Beispieldokument** und seinen [Dokumentverlauf](touchless-document-trace.md): Welcher Schritt, welcher Grund?
6. Ändern Sie **eine** Sache (Regelreihenfolge, Toleranz, Artikelzuordnung) mit einer Vorschau, damit die **Änderungshistorie** sie messen kann.

## Weiterführende Seiten

* [Touchless Intelligence](./)
* [Lieferantendiagnose und Fehlermuster](touchless-supplier-diagnosis.md)
* [Dokumentverlauf](touchless-document-trace.md)
* [Änderungsvorschläge und Berichte](touchless-change-proposals.md)
* [Purchase Order Matching Rules](../../settings/global-settings/document-types/more-settings/purchase-order/purchase-order-matching-rules.md)
* PO Matching Cards: Complete Guide
