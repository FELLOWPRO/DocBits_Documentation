# Opłata za jednostkę poza granicami tolerancji (Odrzucono)

Poniższy scenariusz ilustruje skonfigurowane mapowanie, a nie domyślny szablon o zweryfikowanym wdrożeniu. Rzeczywiste dane wyjściowe, kwoty, znaki i typy dokumentów zależą od aktywnych reguł i wyrażeń `conflict_resolution`, mapowania eksportu oraz decyzji zatwierdzających. Każda opisana nota obciążeniowa lub uznaniowa jest uzależniona od tej konfiguracji; przykład nie gwarantuje jej automatycznego wystawienia ani zgodności z prawem.

## Scenariusz:

Opłata za jednostkę wykracza poza tolerancję i nie została zatwierdzona.

## Działanie:

System dostosowuje opłatę jednostkową do zamówienia lub zatwierdzonych poziomów, generując wszelkie niezbędne noty debetowe lub kredytowe.

## Przykład:

* **Purchase Order (PO):**
  * Opłata za jednostkę: $6.00
  * Quantity: 800 units
  * Całkowita kwota opłaty: $4,800.00
* **Invoice Received:**
  * Opłata za jednostkę: $7.00 (poza tolerancją 16.67%, odrzucona)
  * Quantity: 800 units
  * Całkowita kwota opłaty: $5,600.00
* **Tolerance Levels:**
  * Tolerancja ładunku na jednostkę: ± 5%

Ponieważ opłata jednostkowa ($7.00) przekracza dopuszczalny zakres tolerancji wynoszący 5% i nie została zatwierdzona, system:

1. **Odrzuć zafakturowaną opłatę jednostkową:** System nie akceptuje zafakturowanej opłaty jednostkowej w wysokości $7.00 ze względu na odchylenie przekraczające limit tolerancji.
2. **Dostosuj opłatę jednostkową:** System dostosowuje opłatę jednostkową, aby odpowiadała zamówieniu lub zatwierdzonej opłacie jednostkowej:
   * Skorygowana opłata za jednostkę = $6.00 (od PO)
3. **Przelicz całkowitą kwotę opłaty:** System ponownie przeliczy całkowitą kwotę opłaty w oparciu o skorygowaną opłatę jednostkową:
   * **Skorygowana całkowita kwota opłaty = ilość × skorygowana opłata za jednostkę**
   * **Skorygowana całkowita kwota opłaty = 800 jednostek × $6.00 = $4,800.00**
4. **Wygeneruj notę debetową:** Ponieważ pierwotna suma faktury była wyższa niż suma skorygowana, system generuje notę debetową na zawyżoną kwotę:
   * **Kwota noty debetowej = Suma oryginalnej faktury – Skorygowana całkowita kwota obciążenia**
   * **Kwota noty debetowej = $5,600.00 - $4,800.00 = $800.00**
5. **Przetwórz fakturę:** System przetwarza fakturę zawierającą skorygowaną łączną kwotę obciążenia wynoszącą $4,800.00 i wystawia notę debetową na kwotę $800.00 w celu rozliczenia nadmiernej kwoty.

Takie podejście zapewnia zgodność transakcji finansowych z warunkami zamówienia zakupu, odrzucając niezatwierdzone rozbieżności i zachowując dokładne praktyki rozliczeniowe.
