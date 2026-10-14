# Verbrauchter PO-Zeilenstatus

**Consumed PO line status** färbt Bestellpositionen in der Abgleichsansicht danach ein, wie viel von jeder Position bereits abgeglichen wurde. Aktivieren Sie die Einstellung für den Rechnungs-Dokumenttyp, wenn Ihr Team unbenutzte, teilweise genutzte und vollständig genutzte PO-Positionen schnell erkennen soll. Die Farbe ist eine visuelle Hilfe; prüfen Sie die **Matched Quantity** und die Spalte mit der ausgewählten PO-Menge, bevor Sie entscheiden, ob eine Position erneut abgeglichen werden kann.

## Die Einstellung aktivieren

1. Öffnen Sie **Settings → Document Types**. Suchen Sie den Dokumenttyp, den Sie für Ihre Rechnungen verwenden, und wählen Sie das Zahnrad auf der Karte, um **More Settings** zu öffnen. Der Screenshot zeigt die **Invoice**-Karte. Lassen Sie die Schalter **Activate** und **Extraction** unverändert.

   <figure><img src="../../../../../../.gitbook/assets/consumed-po-line-document-types-en.png" alt="Seite Document Types mit der Invoice-Karte und ihrem More-Settings-Zahnrad"><figcaption><p>Öffnen Sie More Settings über die Invoice-Karte.</p></figcaption></figure>

2. Klappen Sie **Purchase Order** auf, falls der Bereich eingeklappt ist. Suchen Sie **Consumed PO line status** und aktivieren Sie den zugehörigen Schalter. Dies ist eine eigene Einstellung und nicht dasselbe wie **Update Document Purchase Order Status** weiter unten im selben Abschnitt.

   <figure><img src="../../../../../../.gitbook/assets/consumed-po-line-settings-en.png" alt="Abschnitt Purchase Order in More Settings, in dem der Schalter Consumed PO line status sichtbar ist"><figcaption><p>Wählen Sie den Schalter Consumed PO line status.</p></figcaption></figure>

   <figure><img src="../../../../../../.gitbook/assets/consumed-po-line-toggle-en.png" alt="Nahansicht der Beschriftung und des Schalters Consumed PO line status"><figcaption><p>Der Schalter ist in diesem Beispiel ausgeschaltet; schalten Sie ihn ein, um die Abgleichsfarben anzuzeigen.</p></figcaption></figure>

3. Öffnen Sie eine Rechnung mit Bestellabgleich und prüfen Sie deren PO-Positionen. Die folgenden Beispiele zeigen, wie die Zeilenfarben mit dem Abgleichsstatus zusammenhängen. Die Schritte zum Abgleich finden Sie unter [Bestellabgleich](../../../../../../end-user-and-partner-section/end-user-section/purchase-order-matching/README.md).

## Die PO-Zeilenfarben lesen

| Darstellung | Bedeutung | Was zu prüfen ist |
| --- | --- | --- |
| Einfarbig oder weiß | Für diese PO-Position wurde noch keine Menge abgeglichen. | Prüfen Sie vor dem Abgleich die PO-Menge und die Rechnungsposition. |
| Blaue Tönung | Sie haben die Position in der aktuellen Abgleichsansicht ausgewählt. | Die Auswahl ist vorübergehend; sie bedeutet nicht, dass die Position vollständig abgeglichen ist. |
| Hellorange | Es wurde bereits eine Menge abgeglichen, die abgeglichene Menge liegt aber unter der ausgewählten PO-Menge. | Prüfen Sie, wie viel Menge noch übrig ist. |
| Helles Violett | Die abgeglichene Menge entspricht mindestens der ausgewählten PO-Menge. | Gehen Sie nicht davon aus, dass noch weitere Menge verfügbar ist. |

<figure><img src="../../../../../../.gitbook/assets/image (470).png" alt="PO-Position mit abgeglichener Menge null und ohne Statusfarbe"><figcaption><p>Es wurde noch keine Menge abgeglichen.</p></figcaption></figure>

<figure><img src="../../../../../../.gitbook/assets/image (472).png" alt="PO-Position mit blauer Auswahltönung in der Abgleichsansicht"><figcaption><p>Die Position ist für den aktuellen Abgleich ausgewählt.</p></figcaption></figure>

<figure><img src="../../../../../../.gitbook/assets/consumed_po_line_status.png" alt="PO-Position mit hellorangem Hintergrund und einer abgeglichenen Menge unter der PO-Menge"><figcaption><p>Die Position ist teilweise verbraucht.</p></figcaption></figure>

<figure><img src="../../../../../../.gitbook/assets/image (473).png" alt="PO-Position mit hellviolettem Hintergrund und einer abgeglichenen Menge, die der PO-Menge entspricht"><figcaption><p>Die Position ist vollständig verbraucht.</p></figcaption></figure>

Eine durchgestrichene Position hat eine andere Bedeutung: Ihr PO-Status kann durch [PO disable statuses](purchase-order-disable-statuses.md) ausgeschlossen sein. Prüfen Sie diese Einstellung, wenn eine Position nicht ausgewählt werden kann.
