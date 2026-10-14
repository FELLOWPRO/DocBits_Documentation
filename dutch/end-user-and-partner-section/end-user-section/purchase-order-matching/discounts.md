# Korting

## **Overzicht**

Als uw geëxtraheerde tabel de **Korting** of **Kortingspercentage** kolom bevat, zal **DocBits** automatisch de bijbehorende korting toepassen op de eenheidsprijs tijdens de verwerking in het [**Inkooporder Matching scherm**.](./)

## Uitzonderingen

Kortingen worden niet automatisch toegepast wanneer de Meerdere Matches functie wordt gebruikt. Meer informatie over de Meerdere Matches functie is [hier](./#meerdere-matches) te vinden.

## Korting Berekening

Wanneer er een **Korting** aanwezig is, wordt de verlaagde eenheidsprijs berekend door het kortingsbedrag van de eenheidsprijs af te trekken:

```
UNIT_PRICE_DISCOUNTED = UNIT_PRICE - DISCOUNT
```

## Kortingspercentage Berekening

Wanneer er een **Kortingspercentage** aanwezig is, wordt de verlaagde eenheidsprijs berekend met behulp van de volgende formule:

```
UNIT_PRICE_DISCOUNTED = UNIT_PRICE * (1 - DISCOUNT_PERCENT / 100)
```

## Afronding

Alle verlaagde eenheidsprijsresultaten worden afgerond op vier decimalen voor consistentie in downstream verwerking.
