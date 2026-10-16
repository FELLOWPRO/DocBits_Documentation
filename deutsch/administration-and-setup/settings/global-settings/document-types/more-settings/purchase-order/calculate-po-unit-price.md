# PO-Stückpreis berechnen

## **Übersicht**

Sie können wählen, den **Stückpreis** jeder Bestellposition automatisch aus dem **Betrag** und der **Menge** der Position zu berechnen, anstatt den Stückpreis zu verwenden, der mit der Bestellung mitgeliefert wurde. Dies ist besonders nützlich, wenn der Stückpreis in der Bestellung (in Infor ERP / SAP) vom Preis auf dem Dokument abweicht. Solche Abweichungen können entstehen, wenn ein Rabatt auf den Stückpreis in der Bestellung angewendet wird, während das Dokument den Rabatt nur auf den Nettobetrag anwendet.

## **Aktivierungsschritte**

1.  Navigieren Sie zu **Einstellungen** -> **Globale Einstellungen** -> **Dokumenttypen**.

    <figure><img src="../../../../../../.gitbook/assets/Calculate_PO_unit_price_1.png" alt=""><figcaption></figcaption></figure>
2.  Wählen Sie den gewünschten Dokumenttyp aus und klicken Sie auf **Weitere Einstellungen**.

    <figure><img src="../../../../../../.gitbook/assets/Calculate_PO_unit_price_2.png" alt=""><figcaption></figcaption></figure>
3.  Aktivieren Sie im Abschnitt **Bestellung** die Option **PO-Stückpreis berechnen**.

    <figure><img src="../../../../../../.gitbook/assets/Calculate_PO_unit_price_3.png" alt=""><figcaption></figcaption></figure>

## Wie der Preis berechnet wird

Sobald die Einstellung aktiviert ist, wird der Stückpreis einer Bestellposition wie folgt berechnet:

**`Stückpreis = Positionsbetrag ÷ Menge × Stückpreis pro`**

wobei der **Positionsbetrag** folgendermaßen gewählt wird:

| Die Bestellposition enthält                                                               | Verwendeter Positionsbetrag            |
| ----------------------------------------------------------------------------------------- | ------------------------------------- |
| einen **Nettobetrag** (`extended_amount`), der größer als 0 und nicht über dem Positionsgesamtbetrag liegt | der Nettobetrag                       |
| keinen Nettobetrag oder einen Nettobetrag über dem Positionsgesamtbetrag                  | der **Gesamtbetrag** der Position (`total_amount`) |
| keinen positiven Betrag oder keine positive Menge                                         | es wird nichts berechnet, der PO-Preis bleibt |

Warum der Nettobetrag zuerst kommt: ERP-Feeds (Infor BODs) senden den Netto-Positionsbetrag als `extended_amount` und führen **Steuern und Gebühren zusätzlich** im `total_amount`. Die Division eines steuerpflichtigen Gesamtbetrags durch die Menge ergibt einen Bruttostückpreis, und jede Rechnung, die netto bepreist ist, erscheint dann als _unterbewerteter Stückpreis_, obwohl sie korrekt ist. Beispiel aus einer realen Bestellposition: Menge 9, Nettobetrag 879,84, Gesamt 954,63 (8,5 % Steuer) — der netto-basierte Preis ist 97,76 und stimmt mit der Rechnung überein; der gesamtbasierte Preis wäre 106,07.

Ein Nettobetrag, der **größer** als der Positionsgesamtbetrag ist, kann kein Nettobetrag sein, daher wird in diesem Fall der Gesamtbetrag verwendet. Ein `Stückpreis pro` von 0 oder leer wird als 1 gezählt.

{% hint style="info" %}
Der berechnete Preis wird in den Bestell-Snapshot geschrieben, der im Dokument gespeichert ist, und er wird **jedes Mal neu berechnet, wenn das Dokument abgeglichen wird** (Auto PO Match, manueller Abgleich, Abgleich beim Speichern). Ein Dokument, das vor der Änderung der Einstellung abgeglichen wurde, übernimmt daher den neuen Preis beim nächsten Abgleich — ein Neuladen der Bestellung ist nicht erforderlich.
{% endhint %}

## Beispiel:

<figure><img src="../../../../../../.gitbook/assets/Calculate_PO_unit_price_4.png" alt="" width="563"><figcaption></figcaption></figure>

In diesem Fall wird der Stückpreis (ohne Rabatt) aus dem Dokument entnommen, während die Bestellung im ERP den Stückpreis mit angewendetem Rabatt speichert. Dies führt zu einer Abweichung im Stückpreis. Mit aktivierter Einstellung wird der Stückpreis stattdessen aus dem Positionsbetrag und der Menge entnommen, sodass beide Seiten übereinstimmen.

## Verwandte Einstellungen

* [Regeln für den Bestellabgleich](purchase-order-matching-rules.md) — die Regeln vergleichen den **effektiven** Stückpreis, der bei aktivierter Einstellung dieser berechnete Preis ist.
* [Toleranzeinstellungen für Bestellungen](purchase-order-tolerance-settings-additional-purchase-order-tolerance.md) — wie stark der Rechnungsbetrag vom berechneten Preis abweichen darf.