# Rabaty

## **Przegląd**

Jeśli twoja wyodrębniona tabela zawiera kolumnę **Rabat** lub **Procent rabatu**, **DocBits** automatycznie zastosuje odpowiedni rabat do Ceny jednostkowej podczas przetwarzania w [**ekranie dopasowywania zamówienia zakupu**](./).

## Wyjątki

Rabaty nie będą automatycznie stosowane, gdy używana jest funkcja wiele dopasowań. Więcej informacji na temat funkcji Wiele dopasowań można znaleźć [tutaj](./#wiele-dopasowan).

## Obliczanie rabatu

Gdy obecny jest **Rabat**, cena jednostkowa po rabacie jest obliczana poprzez odjęcie kwoty rabatu od ceny jednostkowej:

```
UNIT_PRICE_DISCOUNTED = UNIT_PRICE - DISCOUNT
```

## Obliczanie procentu rabatu

Gdy obecny jest **Procent rabatu**, cena jednostkowa po rabacie jest obliczana za pomocą następującego wzoru:

```
UNIT_PRICE_DISCOUNTED = UNIT_PRICE * (1 - DISCOUNT_PERCENT / 100)
```

## Zaokrąglanie

Wszystkie wyniki ceny jednostkowej po rabacie są zaokrąglane do czterech miejsc po przecinku dla zachowania spójności w dalszym przetwarzaniu.
