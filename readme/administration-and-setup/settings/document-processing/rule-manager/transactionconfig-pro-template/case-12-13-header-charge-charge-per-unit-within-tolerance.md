# Opłata za jednostkę w granicach tolerancji

Poniższy scenariusz ilustruje skonfigurowane mapowanie, a nie domyślny szablon o zweryfikowanym wdrożeniu. Rzeczywiste dane wyjściowe, kwoty, znaki i typy dokumentów zależą od aktywnych reguł i wyrażeń `conflict_resolution`, mapowania eksportu oraz decyzji zatwierdzających. Każda opisana nota obciążeniowa lub uznaniowa jest uzależniona od tej konfiguracji; przykład nie gwarantuje jej automatycznego wystawienia ani zgodności z prawem.

## Scenariusz:

Opłata za nagłówek za jednostkę mieści się w dopuszczalnym zakresie tolerancji w porównaniu do zamówienia.

## Działanie:

System przetwarza opłatę nagłówkową zgodnie z fakturą, stosując ją bez korekt.

## Przykład:

* **Purchase Order (PO):**
  * Opłata za nagłówek za jednostkę: $3.50
  * Quantity: 1,200 units
  * Całkowita kwota opłaty za nagłówek: $4,200.00
* **Invoice Received:**
  * Opłata za nagłówek za jednostkę: $3.55 (w granicach tolerancji 1.43%)
  * Quantity: 1,200 units
  * Całkowita kwota opłaty za nagłówek: $4,260.00
* **Tolerance Levels:**
  * Tolerancja ładunku nagłówka na jednostkę: ±2%

Ponieważ opłata za jednostkę ($3.55) mieści się w dopuszczalnym zakresie tolerancji wynoszącym 2% w porównaniu z zamówieniem, system:

1. **Zaakceptuj opłatę za nagłówek za jednostkę:** System akceptuje zafakturowaną opłatę za jednostkę w wysokości $3.55, ponieważ mieści się ona w zdefiniowanym limicie tolerancji.
2. **Przetwórz opłatę nagłówkową:** System przetwarza fakturę z całkowitą kwotą opłaty nagłówkowej w oparciu o zafakturowaną opłatę jednostkową i ilość:
   * **Całkowita kwota opłaty za nagłówek = ilość × Opłata za nagłówek na jednostkę**
   * **Całkowita kwota opłaty za nagłówek = 1,200 jednostek × $3.55 = $4,260.00**
3. **Sfinalizuj fakturę:** System przetwarza transakcję bez żadnych korekt, akceptując fakturę taką, jaka jest.

Takie podejście zapewnia płynne i wydajne przetwarzanie transakcji, gdy opłaty nagłówkowe mieszczą się w akceptowalnym przedziale tolerancji, unikając niepotrzebnych odrzuceń i opóźnień.
