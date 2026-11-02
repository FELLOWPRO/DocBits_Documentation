# Opłata za jednostkę w granicach tolerancji

Poniższy scenariusz ilustruje skonfigurowane mapowanie, a nie domyślny szablon o zweryfikowanym wdrożeniu. Rzeczywiste dane wyjściowe, kwoty, znaki i typy dokumentów zależą od aktywnych reguł i wyrażeń `conflict_resolution`, mapowania eksportu oraz decyzji zatwierdzających. Każda opisana nota obciążeniowa lub uznaniowa jest uzależniona od tej konfiguracji; przykład nie gwarantuje jej automatycznego wystawienia ani zgodności z prawem.

## Scenariusz:

Opłata jednostkowa na fakturze mieści się w dopuszczalnym zakresie tolerancji w porównaniu do zamówienia.

## Działanie:

System przyjmuje opłatę jednostkową zgodnie z fakturą i przetwarza transakcję bez korekt.

## Przykład:

* **Purchase Order (PO):**
  * Opłata za jednostkę: $5.00
  * Quantity: 500 units
  * Całkowita kwota opłaty: $2,500.00
* **Invoice Received:**
  * Opłata za jednostkę: $5.10 (w granicach tolerancji 2%)
  * Quantity: 500 units
  * Całkowita kwota opłaty: $2,550.00
* **Tolerance Levels:**
  * Tolerancja ładunku na jednostkę: ±3%

Ponieważ opłata za jednostkę ($5.10) mieści się w akceptowalnym przedziale tolerancji wynoszącym 3% w porównaniu z zamówieniem, system:

1. **Zaakceptuj opłatę jednostkową:** System akceptuje zafakturowaną opłatę jednostkową w wysokości $5.10, ponieważ mieści się ona w zdefiniowanym limicie tolerancji.
2. **Przetwórz transakcję:** System przetwarza fakturę z całkowitą kwotą opłaty w oparciu o zafakturowaną opłatę za jednostkę i ilość:
   * **Całkowita kwota opłaty = ilość × opłata za jednostkę**
   * **Całkowita kwota opłaty = 500 jednostek × $5.10 = $2,550.00**
3. **Sfinalizuj fakturę:** System przetwarza transakcję bez żadnych korekt, akceptując fakturę taką, jaka jest.

Takie podejście umożliwia systemowi uwzględnienie niewielkich, akceptowalnych różnic w opłatach, zapewniając płynne i wydajne przetwarzanie transakcji bez zbędnych odrzuceń i opóźnień.
