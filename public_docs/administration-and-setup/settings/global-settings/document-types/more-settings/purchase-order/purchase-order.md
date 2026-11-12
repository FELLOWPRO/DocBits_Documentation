# Bestellung

## Übersicht

Diese Einstellung aktiviert den Abschnitt [**Purchase Order Matching**](../../../../../../end-user-and-partner-section/end-user-section/purchase-order-matching/README.md), der nach der Dokumentvalidierung erreichbar wird.

<mark style="color:red;">**Hinweis**</mark>: Für den Dokumenttyp **Invoice** müssen zusätzlich die folgenden Voraussetzungen erfüllt sein:

* Die Einstellung **Purchase Order** muss eingeschaltet sein (wie auf dieser Seite beschrieben)
* Die Rechnung muss vom Typ **Purchase Invoice** sein
* Eine **Extracted Table** muss vorhanden sein

## Aktivierungsschritte <a href="#activation-steps" id="activation-steps"></a>

1. Gehen Sie zu **Settings → Document Types**.
2. Suchen Sie die Karte des Dokumenttyps und klicken Sie auf das Zahnrad (**More Settings**).
3. Öffnen Sie den Abschnitt **Purchase Order** und schalten Sie **Purchase Order** ein.

<figure><img src="../../../../../../.gitbook/assets/po-settings-purchase-order-de-20261031.png" alt="More Settings des Dokumenttyps Invoice mit geöffnetem Abschnitt Purchase Order"><figcaption><p>Der Abschnitt <strong>Purchase Order</strong> in <strong>More Settings</strong>. Der erste Schalter aktiviert den Bestellabgleich für den Dokumenttyp, die Schalter darunter verfeinern ihn.</p></figcaption></figure>

## **Funktionalität**

Sobald die Einstellung eingeschaltet ist, steht der Abschnitt [**Purchase Order Matching**](../../../../../../end-user-and-partner-section/end-user-section/purchase-order-matching/README.md) nach der Dokumentvalidierung zur Verfügung.

### Welche Menge abgeglichen wird

Welche Menge der Bestellung der Abgleich heranzieht, hängt von **PO match server side** ab:

* **PO match server side off** – neben dem Schalter **Purchase Order** steht eine Auswahlliste **Match quantity**. Wählen Sie **Quantity**, **Received Quantity** oder **Received Delivery Open Quantity**. DocBits gleicht mit dem eingebauten Abgleich ab und vergleicht die gewählte Menge.
* **PO match server side on** – der Abgleich läuft mit dem Regelsatz des Dokumenttyps, und **Match quantity** gehört zu diesen Regeln. Die Kopfzeile des Abschnitts zeigt dann den Link **Configure PO matching rules**, der die Regeln öffnet. Siehe [Purchase Order Matching Rules](purchase-order-matching-rules.md).

{% hint style="info" %}
Die Aufnahme oben entstand mit eingeschaltetem **PO match server side**; die Auswahlliste **Match quantity** ist auf diesem Bildschirm deshalb nicht zu sehen — sie wird in den Abgleichsregeln festgelegt.
{% endhint %}

### Vorauszahlung vor Wareneingang

Manche Rechnungen kommen vor der Ware. Um eine solche Rechnung gegen die bestellte statt gegen die empfangene Menge abzugleichen, schalten Sie **Allow pre-payment before goods receipt** im selben Abschnitt ein.

Der Schalter erscheint nur, wenn alle drei Bedingungen erfüllt sind:

* der Dokumenttyp ist **Invoice**,
* **Purchase Order** ist eingeschaltet,
* und die abgeglichene Menge ist **Received Quantity**.

Ändern Sie die abgeglichene Menge auf einen anderen Wert, verschwindet der Schalter aus den Einstellungen. Auf dem [PO matching screen](../../../../../../end-user-and-partner-section/end-user-section/purchase-order-matching/README.md) erscheint dann **Match as pre-payment** unterhalb von **Use Lines Net Amount for Matched Total**, mit dem Hinweis *Match on ordered quantity instead of received quantity*. Der Schalter ist ausgegraut und mit einer Notiz versehen, wenn der Lieferant im ERP nicht vor dem Wareneingang berechnet werden darf.

Solange der Schalter eingeschaltet ist, liest der Bildschirm für manuelle Verknüpfungen und für die abgeglichene Summe die bestellte Menge, nicht die empfangene. Die Auswahl wird am Dokument gespeichert und **Auto Match** läuft erneut; schlägt dieser Abgleich fehl, kehrt die Auswahl auf ihren vorherigen Wert zurück.
