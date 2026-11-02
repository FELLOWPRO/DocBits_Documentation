# Przypadek 15: Opłata w nagłówku - Opłata za jednostkę poza granicami tolerancji (Odrzucono)

Poniższy scenariusz ilustruje skonfigurowane mapowanie, a nie domyślny szablon o zweryfikowanym wdrożeniu. Rzeczywiste dane wyjściowe, kwoty, znaki i typy dokumentów zależą od aktywnych reguł i wyrażeń `conflict_resolution`, mapowania eksportu oraz decyzji zatwierdzających. Każda opisana nota obciążeniowa lub uznaniowa jest uzależniona od tej konfiguracji; przykład nie gwarantuje jej automatycznego wystawienia ani zgodności z prawem.

## Scenariusz:

Opłata za głowicę za jednostkę wykracza poza tolerancję i nie została zatwierdzona.

## Działanie:

System dostosowuje opłatę nagłówkową do zamówienia, odpowiednio przetwarza transakcję i generuje niezbędne dokumenty korygujące.

## Przykład:

* **Purchase Order (PO):**
  * Opłata za nagłówek za jednostkę: $4.00
  * Quantity: 1,500 units
  * Całkowita kwota opłaty za nagłówek: $6,000.00
* **Invoice Received:**
  * Opłata za nagłówek za jednostkę: $5.00 (poza tolerancją 25%, odrzucona)
  * Quantity: 1,500 units
  * Całkowita kwota opłaty za nagłówek: $7,500.00
* **Tolerance Levels:**
  * Tolerancja opłaty za głowicę na jednostkę: ±5%

Ponieważ opłata za jednostkę ($5.00) przekracza dopuszczalny zakres tolerancji wynoszący 5% i nie została zatwierdzona, system:

1. **Odrzuć zafakturowaną opłatę nagłówkową za jednostkę:** System nie akceptuje zafakturowanej opłaty nagłówkowej za jednostkę w wysokości $5.00 ze względu na odchylenie przekraczające limit tolerancji.
2. **Dostosuj opłatę za jednostkę w nagłówku:** System dostosowuje opłatę za jednostkę, aby odpowiadała pierwotnemu zamówieniu lub zatwierdzonej opłacie za jednostkę:
   * Skorygowana opłata za nagłówek za jednostkę = $4.00 (od PO)
3. **Oblicz ponownie całkowitą kwotę opłaty za nagłówek:** System ponownie oblicza całkowitą kwotę opłaty w oparciu o skorygowaną opłatę jednostkową:
   * **Skorygowana całkowita kwota opłaty za głowicę = ilość × Skorygowana opłata za głowicę na jednostkę**
   * **Skorygowana całkowita kwota opłaty za nagłówek = 1,500 jednostek × $4.00 = $6,000.00**
4. **Wygeneruj notę kredytową:** Ponieważ pierwotna suma faktury była wyższa niż suma skorygowana, system generuje notę kredytową na zawyżoną kwotę:
   * **Kwota noty kredytowej = Suma oryginalnej faktury – Skorygowana łączna kwota opłaty nagłówkowej**
   * **Kwota noty kredytowej = $7,500.00 - $6,000.00 = $1,500.00**
5. **Przetwórz fakturę:** System przetwarza fakturę zawierającą skorygowaną łączną kwotę obciążenia wynoszącą $6,000.00 i wystawia notę kredytową na kwotę $1,500.00 w celu rozliczenia nadmiernej kwoty.

Takie podejście gwarantuje, że transakcja jest zgodna z pierwotnymi warunkami zamówienia, zachowując dokładne przetwarzanie finansowe i korygując wszelkie nadmierne obciążenia.
