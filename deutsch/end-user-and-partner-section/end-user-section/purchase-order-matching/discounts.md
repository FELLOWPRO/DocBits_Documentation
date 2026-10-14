# Rabatte

## **Übersicht**

Wenn Ihre extrahierte Tabelle die **Rabatt**- oder **Rabattprozentsatz**-Spalte enthält, wird **DocBits** automatisch den entsprechenden Rabatt auf den Einzelpreis während der Verarbeitung im [**Bestellnummer-Abgleichsbildschirm**](../../../end-user-section/purchase-order-matching/) anwenden.

## Ausnahmen

Rabatte werden nicht automatisch angewendet, wenn die Mehrfachabgleiche-Funktion verwendet wird. Weitere Informationen zur Mehrfachabgleiche-Funktion finden Sie [hier](../../../end-user-section/purchase-order-matching/#mehrfachabgleiche).

## Rabattberechnung

Wenn ein **Rabatt** vorhanden ist, wird der rabattierte Einzelpreis berechnet, indem der Rabattbetrag vom Einzelpreis subtrahiert wird:

```
UNIT_PRICE_DISCOUNTED = UNIT_PRICE - DISCOUNT
```

## Rabattprozentsatzberechnung

Wenn ein **Rabattprozentsatz** vorhanden ist, wird der rabattierte Einzelpreis mit der folgenden Formel berechnet:

```
UNIT_PRICE_DISCOUNTED = UNIT_PRICE * (1 - DISCOUNT_PERCENT / 100)
```

## Rundung

Alle rabattierten Einzelpreise werden auf vier Dezimalstellen gerundet, um Konsistenz in der nachgelagerten Verarbeitung zu gewährleisten.
