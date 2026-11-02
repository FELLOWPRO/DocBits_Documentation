# Pozycje podatkowe

Poniższy scenariusz ilustruje skonfigurowane mapowanie, a nie domyślny szablon o zweryfikowanym wdrożeniu. Rzeczywiste dane wyjściowe, kwoty, znaki i typy dokumentów zależą od aktywnych reguł i wyrażeń `conflict_resolution`, mapowania eksportu oraz decyzji zatwierdzających. Każda opisana nota obciążeniowa lub uznaniowa jest uzależniona od tej konfiguracji; przykład nie gwarantuje jej automatycznego wystawienia ani zgodności z prawem.

## Scenariusz:

Rozwiązuje rozbieżności w kwotach podatku pomiędzy fakturą a zamówieniem.

## Działanie:

System dostosowuje linie podatkowe zgodnie z zatwierdzonymi stawkami i kwotami podatku, zapewniając zgodność z obowiązującymi przepisami podatkowymi.

## Przykład:

* **Purchase Order (PO):**
  * Subtotal Amount: $10,000.00
  * Tax Rate: 8%
  * Oczekiwana kwota podatku: $800.00
  * Total Amount with Tax: $10,800.00
* **Invoice Received:**
  * Subtotal Amount: $10,000.00
  * Stawka podatku: 10% (rozbieżność)
  * Zafakturowana kwota podatku: $1,000.00
  * Total Amount with Tax: $11,000.00

Ponieważ stawka podatku na fakturze (10%) różni się od oczekiwanej stawki podatku (8%) i nie została zatwierdzona, system:

1. **Odrzuć zafakturowaną stawkę podatku:** System nie akceptuje 10% stawki podatku, ponieważ nie jest ona zgodna ze stawką zatwierdzoną w zamówieniu.
2. **Dostosuj stawkę podatku:** System dostosowuje stawkę podatku, aby odpowiadała zatwierdzonej stawce z zamówienia zakupu.
   * Skorygowana stawka podatku = 8% (od PO)
3. **Przelicz kwotę podatku:** System przelicza kwotę podatku w oparciu o skorygowaną stawkę podatku:
   * **Skorygowana kwota podatku = kwota sumy częściowej × skorygowana stawka podatku**
   * **Skorygowana kwota podatku = $10,000.00 × 8% = $800.00**
4. **Przelicz kwotę całkowitą:** System ponownie przeliczy kwotę całkowitą, łącznie z podatkiem:
   * **Skorygowana kwota całkowita z podatkiem = kwota sumy częściowej + skorygowana kwota podatku**
   * **Skorygowana kwota całkowita z podatkiem = $10,000.00 + $800.00 = $10,800.00**
5. **Wygeneruj notę kredytową:** System generuje notę kredytową w celu skorygowania zawyżonej kwoty podatku:
   * **Kwota noty kredytowej = pierwotna kwota podatku na fakturze – skorygowana kwota podatku**
   * **Kwota noty kredytowej = $1,000.00 - $800.00 = $200.00**
6. **Przetwórz fakturę:** System przetwarza fakturę ze skorygowaną kwotą podatku $800.00 i kwotą całkowitą $10,800.00 oraz wystawia notę uznaniową na różnicę podatku $200.00.

Takie podejście gwarantuje, że faktura VAT jest zgodna z zamówieniem i zgodna z obowiązującymi przepisami podatkowymi, zapobiegając nadpłatom i zapewniając prawidłowość ksiąg finansowych.
