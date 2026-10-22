# Przypadek 14: Pozycja opłaty - Opłata za jednostkę poza granicami tolerancji (Zatwierdzono)

Poniższy scenariusz ilustruje skonfigurowane mapowanie, a nie domyślny szablon o zweryfikowanym wdrożeniu. Rzeczywiste dane wyjściowe, kwoty, znaki i typy dokumentów zależą od aktywnych reguł i wyrażeń `conflict_resolution`, mapowania eksportu oraz decyzji zatwierdzających. Każda opisana nota obciążeniowa lub uznaniowa jest uzależniona od tej konfiguracji; przykład nie gwarantuje jej automatycznego wystawienia ani zgodności z prawem.

## Scenariusz:

Opłata za jednostkę wykracza poza tolerancję, ale została zatwierdzona.

## Działanie:

System akceptuje opłatę jednostkową i stosuje zatwierdzone opłaty, odpowiednio przetwarzając transakcję.

## Przykład:

* **Purchase Order (PO):**
  * Opłata za jednostkę: $4.50
  * Quantity: 1,000 units
  * Całkowita kwota opłaty: $4,500.00
* **Invoice Received:**
  * Opłata za jednostkę: $5.00 (zatwierdzona tolerancja zewnętrzna 11.11%)
  * Quantity: 1,000 units
  * Całkowita kwota opłaty: $5,000.00
* **Tolerance Levels:**
  * Tolerancja ładunku na jednostkę: ± 5%

Ponieważ opłata jednostkowa ($5.00) wykracza poza dopuszczalny zakres tolerancji wynoszący 5%, ale została zatwierdzona, system:

1. **Zaakceptuj zatwierdzoną opłatę za jednostkę:** System akceptuje zafakturowaną opłatę za jednostkę w wysokości $5.00, ponieważ została zatwierdzona pomimo przekroczenia limitu tolerancji.
2. **Przetwórz transakcję:** System przetwarza fakturę przy użyciu zatwierdzonej opłaty jednostkowej i ilości:
   * **Całkowita kwota opłaty = ilość × Zatwierdzona opłata za jednostkę**
   * **Całkowita kwota opłaty = 1,000 jednostek × $5.00 = $5,000.00**
3. **Sfinalizuj fakturę:** System przetwarza transakcję z zatwierdzonymi opłatami, odzwierciedlającymi łączną kwotę $5,000.00.

Takie podejście gwarantuje, że system będzie w stanie uwzględnić zatwierdzone różnice w opłatach, zapewniając elastyczność przy jednoczesnym zachowaniu dokładnych zapisów finansowych.
