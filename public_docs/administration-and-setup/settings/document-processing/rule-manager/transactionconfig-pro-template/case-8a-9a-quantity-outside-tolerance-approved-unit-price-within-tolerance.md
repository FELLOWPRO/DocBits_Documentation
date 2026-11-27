# Przypadek 8a, 9a: Ilość poza tolerancją — zatwierdzenie; cena w tolerancji

Poniższy scenariusz ilustruje skonfigurowane mapowanie, a nie domyślny szablon o zweryfikowanym wdrożeniu. Rzeczywiste dane wyjściowe, kwoty, znaki i typy dokumentów zależą od aktywnych reguł i wyrażeń `conflict_resolution`, mapowania eksportu oraz decyzji zatwierdzających. Każda opisana nota obciążeniowa lub uznaniowa jest uzależniona od tej konfiguracji; przykład nie gwarantuje jej automatycznego wystawienia ani zgodności z prawem.

## Scenariusz:

Ilość na fakturze wykracza poza dopuszczalną tolerancję, ale została zatwierdzona, a cena jednostkowa mieści się w tolerancji.

## Działanie:

System akceptuje zatwierdzoną ilość oraz cenę jednostkową z faktury i zgodnie z nią realizuje transakcję.

## Przykład:

* **Purchase Order (PO):**
  * Quantity: 150 units
  * Unit Price: $12.00 per unit
  * Total Amount: $1,800.00
* **Invoice Received:**
  * Quantity: 160 units — 6.67% above the PO value, outside the configured ±5% tolerance; approved.
  * Unit Price: $12.00 per unit (within tolerance)
  * Total Amount: $1,920.00
* **Tolerance Levels:**
  * Quantity Tolerance: ±5%
  * Unit Price Tolerance: ±2%

Ponieważ ilość (160 sztuk) przekracza dopuszczalny limit tolerancji, ale została zatwierdzona, a cena jednostkowa ($12.00) mieści się w akceptowalnym przedziale, system:

1. **Zaakceptuj zatwierdzoną ilość:** System potwierdza, że ilość została zatwierdzona, mimo że wykracza poza normalny zakres tolerancji.
2. **Zaakceptuj cenę jednostkową:** Cena jednostkowa wynosząca $12.00 za jednostkę mieści się w dopuszczalnej tolerancji, dlatego jest akceptowana jako zafakturowana.
3. **Przetwórz transakcję:** System oblicza całkowitą kwotę na podstawie zatwierdzonej ilości i ceny jednostkowej:
   * **Total Amount = Quantity × Unit Price**
   * **Total Amount = 160 units × $12.00 per unit = $1,920.00**
4. **Sfinalizuj fakturę:** System przetwarza fakturę na łączną kwotę $1,920.00, odzwierciedlającą zatwierdzoną ilość i zaakceptowaną cenę jednostkową.

Takie podejście pozwala systemowi uwzględnić zatwierdzone różnice w ilości, zapewniając jednocześnie, że cena jednostkowa pozostanie w oczekiwanym przedziale, co ułatwia płynne przetwarzanie transakcji.
