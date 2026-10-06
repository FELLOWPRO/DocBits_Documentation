# Verbrauchter PO-Zeilenstatus

**Der Verbrauchte PO-Zeilenstatus** färbt Bestellpositionen (PO-Positionen) in der Abgleichsansicht entsprechend dem Anteil ein, der bereits abgeglichen wurde. Aktivieren Sie die Einstellung für den Dokumenttyp Ihrer Rechnungen, wenn Ihr Team noch nicht genutzte, teilweise genutzte und vollständig genutzte PO-Positionen schnell erkennen soll. Die Farbe ist nur ein visuelles Hilfsmittel; prüfen Sie vor der Entscheidung, ob eine Position erneut abgeglichen werden kann, die **Abgeglichene Menge** und die gewählte PO-Mengenspalte.

## Einstellung aktivieren

1. Öffnen Sie **Einstellungen → Dokumenttypen**. Suchen Sie den Dokumenttyp, den Sie für Ihre Rechnungen verwenden, und wählen Sie das Zahnrad auf seiner Karte, um **Weitere Einstellungen** zu öffnen. Der Screenshot zeigt die Karte **Rechnung**. Lassen Sie die Schalter **Aktivieren** und **Extraktion** unverändert.

   <figure><img src="../../../../../../.gitbook/assets/1-consumed-po-line-document-types-de.png" alt="Dokumenttypen-Seite mit der Rechnung-Karte und ihrem Zahnrad für Weitere Einstellungen"><figcaption><p>Weitere Einstellungen über die Rechnung-Karte öffnen.</p></figcaption></figure>

2. Klappen Sie **Bestellung** auf, falls es eingeklappt ist. Suchen Sie **Status der verbrauchten Bestellposition** und aktivieren Sie seinen Schalter. Das ist eine eigene Einstellung, unabhängig von **Dokumentstatus für Einkaufsbestellung aktualisieren** weiter unten im selben Abschnitt.

   <figure><img src="../../../../../../.gitbook/assets/2-consumed-po-line-settings-de.png" alt="Abschnitt Bestellung der Weitere-Einstellungen-Seite mit dem sichtbaren Schalter Status der verbrauchten Bestellposition"><figcaption><p>Den Schalter „Status der verbrauchten Bestellposition“ wählen.</p></figcaption></figure>

   <figure><img src="../../../../../../.gitbook/assets/3-consumed-po-line-toggle-de.png" alt="Nahaufnahme des Labels Status der verbrauchten Bestellposition und seines Schalters"><figcaption><p>Der Schalter ist in diesem Beispiel ausgeschaltet; schalten Sie ihn ein, um die Abgleichsfarben zu sehen.</p></figcaption></figure>

3. Öffnen Sie eine Rechnung mit Bestellabgleich und prüfen Sie ihre PO-Positionen. Die Beispiele unten zeigen, wie die Positionsfarben zum Abgleichstatus gehören. Die Abgleichsschritte finden Sie unter [Bildschirm „Bestellabgleich“](../../../../../../end-user-and-partner-section/end-user-section/purchase-order-matching/README.md).

## Die PO-Positionsfarben lesen

| Aussehen | Bedeutung | Was prüfen |
| --- | --- | --- |
| Unauffällig oder weiß | Für diese PO-Position wurde noch keine Menge abgeglichen. | PO-Menge und Rechnungsposition vor dem Abgleich prüfen. |
| Blauer Ton | Sie haben die Position in der aktuellen Abgleichsansicht ausgewählt. | Die Auswahl ist vorübergehend; sie bedeutet nicht, dass die Position vollständig abgeglichen ist. |
| Blassorange | Ein Teil der Menge ist abgeglichen, aber die abgeglichene Menge liegt unter der gewählten PO-Menge. | Prüfen, welche Menge noch verfügbar ist. |
| Blassviolett | Die abgeglichene Menge erreicht mindestens die gewählte PO-Menge. | Gehen Sie nicht davon aus, dass weitere Menge verfügbar ist. |

<figure><img src="../../../../../../.gitbook/assets/image (470).png" alt="PO-Position mit abgeglichener Menge null und ohne Statusfarbe"><figcaption><p>Für diese Position wurde noch keine Menge abgeglichen.</p></figcaption></figure>

<figure><img src="../../../../../../.gitbook/assets/image (472).png" alt="PO-Position mit blauem Auswahlton in der Abgleichsansicht"><figcaption><p>Die Position ist für den aktuellen Abgleich ausgewählt.</p></figcaption></figure>

<figure><img src="../../../../../../.gitbook/assets/consumed_po_line_status.png" alt="PO-Position mit blassoranger Hintergrundfarbe und abgeglichener Menge unter der PO-Menge"><figcaption><p>Die Position ist teilweise genutzt.</p></figcaption></figure>

<figure><img src="../../../../../../.gitbook/assets/image (473).png" alt="PO-Position mit blassvioletter Hintergrundfarbe und abgeglichener Menge gleich der PO-Menge"><figcaption><p>Die Position ist vollständig genutzt.</p></figcaption></figure>

Eine durchgestrichene Position hat eine andere Bedeutung: Ihr PO-Status ist möglicherweise durch [PO-Deaktivierungsstatus](purchase-order-disable-statuses.md) ausgeschlossen. Prüfen Sie diese Einstellung, wenn sich eine Position nicht auswählen lässt.
