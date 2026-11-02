# Przypadek 14: Opłata w nagłówku - Opłata za jednostkę poza granicami tolerancji (Zatwierdzono)

Poniższy scenariusz ilustruje skonfigurowane mapowanie, a nie domyślny szablon o zweryfikowanym wdrożeniu. Rzeczywiste dane wyjściowe, kwoty, znaki i typy dokumentów zależą od aktywnych reguł i wyrażeń `conflict_resolution`, mapowania eksportu oraz decyzji zatwierdzających. Każda opisana nota obciążeniowa lub uznaniowa jest uzależniona od tej konfiguracji; przykład nie gwarantuje jej automatycznego wystawienia ani zgodności z prawem.

## Scenariusz:

Opłata za głowicę za jednostkę wykracza poza tolerancję, ale została zatwierdzona.

## Działanie:

System przetwarza zatwierdzoną opłatę jednostkową i stosuje ją do transakcji.

## Przykład:

* **Purchase Order (PO):**
  * Opłata za nagłówek za jednostkę: $2.50
  * Quantity: 2,000 units
  * Całkowita kwota opłaty za nagłówek: $5,000.00
* **Invoice Received:**
  * Opłata za nagłówek za jednostkę: $3.00 (zatwierdzona tolerancja poza 20%)
  * Quantity: 2,000 units
  * Całkowita kwota opłaty za nagłówek: $6,000.00
* **Tolerance Levels:**
  * Tolerancja opłaty za głowicę na jednostkę: ±5%

Ponieważ opłata za jednostkę nagłówka ($3.00) przekracza dopuszczalny zakres tolerancji wynoszący 5%, ale została zatwierdzona, system:

1. **Zaakceptuj zatwierdzoną opłatę za nagłówek za jednostkę:** System akceptuje zafakturowaną opłatę za nagłówek za jednostkę w wysokości $3.00, ponieważ została zatwierdzona pomimo przekroczenia limitu tolerancji.
2. **Przetwórz opłatę nagłówkową:** System przetwarza fakturę przy użyciu zatwierdzonej opłaty jednostkowej i ilości:
   * **Całkowita kwota opłaty za głowicę = ilość × Zatwierdzona opłata za głowicę na jednostkę**
   * **Całkowita kwota opłaty za nagłówek = 2,000 jednostek × $3.00 = $6,000.00**
3. **Sfinalizuj fakturę:** System przetwarza transakcję z zatwierdzonymi opłatami, odzwierciedlającymi łączną kwotę $6,000.00.

Takie podejście umożliwia systemowi uwzględnienie zatwierdzonych różnic w opłatach nagłówkowych, zapewniając, że transakcja zostanie przetworzona zgodnie z zatwierdzeniem, przy jednoczesnym zachowaniu dokładnej dokumentacji finansowej.
