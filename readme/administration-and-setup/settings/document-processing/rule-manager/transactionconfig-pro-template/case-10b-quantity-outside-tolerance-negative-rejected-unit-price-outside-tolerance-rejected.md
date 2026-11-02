# Przypadek 10b: Ilość za mała i cena poza tolerancją — odrzucenie

Poniższy scenariusz ilustruje skonfigurowane mapowanie, a nie domyślny szablon o zweryfikowanym wdrożeniu. Rzeczywiste dane wyjściowe, kwoty, znaki i typy dokumentów zależą od aktywnych reguł i wyrażeń `conflict_resolution`, mapowania eksportu oraz decyzji zatwierdzających. Każda opisana nota obciążeniowa lub uznaniowa jest uzależniona od tej konfiguracji; przykład nie gwarantuje jej automatycznego wystawienia ani zgodności z prawem.

## Scenariusz:

Zarówno ilość, jak i cena jednostkowa wykraczają poza tolerancję i żadna z nich nie została zatwierdzona.

## Działanie:

System odrzuca dane do faktury, dostosowuje wartości do zamówienia i generuje niezbędne noty debetowe lub kredytowe.

## Przykład:

* **Purchase Order (PO):**
  * Quantity: 150 units
  * Cena jednostkowa: $30.00 za sztukę
  * Total Amount: $4,500.00
* **Invoice Received:**
  * Ilość: 140 sztuk (poza tolerancją -6.67%, odrzucona)
  * Cena jednostkowa: $33.00 za sztukę (poza tolerancją 10%, odrzucona)
  * Total Amount: $4,620.00
* **Tolerance Levels:**
  * Quantity Tolerance: ±5%
  * Tolerancja ceny jednostkowej: ±2%

Ponieważ zarówno ilość (140 jednostek), jak i cena jednostkowa ($33.00) wykraczają poza dopuszczalne granice tolerancji i żadna z nich nie została zatwierdzona, system:

1. **Odrzuć dane do faktury:** System nie akceptuje zafakturowanej ilości lub ceny jednostkowej ze względu na ich odchylenie od granic tolerancji.
2. **Dostosuj ilość:** System dostosowuje ilość, aby odpowiadała pierwotnej ilości zamówienia.
   * Skorygowana ilość = 150 jednostek (od PO)
3. **Dostosuj cenę jednostkową:** System dostosowuje cenę jednostkową, aby odpowiadała cenie jednostkowej pierwotnego zamówienia zakupu.
   * Skorygowana cena jednostkowa = $30.00 za jednostkę (od PO)
4. **Przelicz kwotę całkowitą:** System przelicza całkowitą kwotę na podstawie skorygowanej ilości i ceny jednostkowej:
   * **Skorygowana kwota całkowita = skorygowana ilość × skorygowana cena jednostkowa**
   * **Skorygowana kwota całkowita = 150 jednostek × $30.00 za jednostkę = $4,500.00**
5. **Wygeneruj notę debetową:** Ponieważ pierwotna suma faktury była wyższa niż suma skorygowana, system generuje notę debetową na zawyżoną kwotę.
   * **Kwota noty debetowej = Suma oryginalnej faktury – Skorygowana kwota całkowita**
   * **Kwota noty debetowej = $4,620.00 - $4,500.00 = $120.00**
6. **Przetwórz fakturę:** System przetwarza fakturę na skorygowaną łączną kwotę $4,500.00 i wystawia notę debetową na kwotę $120.00 w celu skompensowania zawyżonej kwoty.

Takie podejście gwarantuje, że transakcja finansowa zostanie skorygowana w celu dopasowania do warunków zamówienia, przy zachowaniu dokładnych i uczciwych praktyk rozliczeniowych.
