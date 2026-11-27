# Przypadek 10b: Ilość za mała i cena poza tolerancją — odrzucenie

Poniższy scenariusz ilustruje skonfigurowane mapowanie, a nie domyślny szablon o zweryfikowanym wdrożeniu. Rzeczywiste dane wyjściowe, kwoty, znaki i typy dokumentów zależą od aktywnych reguł i wyrażeń `conflict_resolution`, mapowania eksportu oraz decyzji zatwierdzających. Każda opisana nota obciążeniowa lub uznaniowa jest uzależniona od tej konfiguracji; przykład nie gwarantuje jej automatycznego wystawienia ani zgodności z prawem.

## Scenariusz:

Zarówno ilość, jak i cena jednostkowa wykraczają poza tolerancję i żadna z nich nie została zatwierdzona.

## Działanie:

System odrzuca dane do faktury, dostosowuje wartości do zamówienia i generuje niezbędne noty debetowe lub kredytowe.

## Przykład:

* **Purchase Order (PO):**
  * Quantity: 150 units
  * Unit Price: $30.00 per unit
  * Total Amount: $4,500.00
* **Invoice Received:**
  * Quantity: 140 units — 6.67% below the PO value, outside the configured ±5% tolerance; rejected.
  * Unit Price: $33.00 per unit — 10% above the PO value, outside the configured ±2% tolerance; rejected.
  * Total Amount: $4,620.00
* **Tolerance Levels:**
  * Quantity Tolerance: ±5%
  * Unit Price Tolerance: ±2%

Ponieważ zarówno ilość (140 jednostek), jak i cena jednostkowa ($33.00) wykraczają poza dopuszczalne granice tolerancji i żadna z nich nie została zatwierdzona, system:

1. **Reject the Invoice Data:** System nie akceptuje zafakturowanej ilości lub ceny jednostkowej ze względu na ich odchylenie od granic tolerancji.
2. **Adjust the Quantity:** System dostosowuje ilość, aby odpowiadała pierwotnej ilości zamówienia.
   * Adjusted Quantity = 150 units (from PO)
3. **Adjust the Unit Price:** System dostosowuje cenę jednostkową, aby odpowiadała cenie jednostkowej pierwotnego zamówienia zakupu.
   * Adjusted Unit Price = $30.00 per unit (from PO)
4. **Recalculate the Total Amount:** System przelicza całkowitą kwotę na podstawie skorygowanej ilości i ceny jednostkowej:
   * **Corrected Total Amount = Adjusted Quantity × Adjusted Unit Price**
   * **Corrected Total Amount = 150 units × $30.00 per unit = $4,500.00**
5. **Generate a Debit Note:** Ponieważ pierwotna suma faktury była wyższa niż suma skorygowana, system generuje notę debetową na zawyżoną kwotę.
   * **Debit Note Amount = Original Invoice Total - Corrected Total Amount**
   * **Debit Note Amount = $4,620.00 - $4,500.00 = $120.00**
6. **Process the Invoice:** System przetwarza fakturę na skorygowaną łączną kwotę $4,500.00 i wystawia notę debetową na kwotę $120.00 w celu skompensowania zawyżonej kwoty.

Takie podejście gwarantuje, że transakcja finansowa zostanie skorygowana w celu dopasowania do warunków zamówienia, przy zachowaniu dokładnych i uczciwych praktyk rozliczeniowych.
