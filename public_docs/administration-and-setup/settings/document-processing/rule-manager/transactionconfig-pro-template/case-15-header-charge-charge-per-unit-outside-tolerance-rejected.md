# Przypadek 15: Opłata w nagłówku - Opłata za jednostkę poza granicami tolerancji (Odrzucono)

Poniższy scenariusz ilustruje skonfigurowane mapowanie, a nie domyślny szablon o zweryfikowanym wdrożeniu. Rzeczywiste dane wyjściowe, kwoty, znaki i typy dokumentów zależą od aktywnych reguł i wyrażeń `conflict_resolution`, mapowania eksportu oraz decyzji zatwierdzających. Każda opisana nota obciążeniowa lub uznaniowa jest uzależniona od tej konfiguracji; przykład nie gwarantuje jej automatycznego wystawienia ani zgodności z prawem.

## Scenariusz:

Opłata za głowicę za jednostkę wykracza poza tolerancję i nie została zatwierdzona.

## Działanie:

System dostosowuje opłatę nagłówkową do zamówienia, odpowiednio przetwarza transakcję i generuje niezbędne dokumenty korygujące.

## Przykład:

* **Purchase Order (PO):**
  * Header Charge Per Unit: $4.00
  * Quantity: 1,500 units
  * Total Header Charge Amount: $6,000.00
* **Invoice Received:**
  * Header Charge Per Unit: $5.00 — 25% above the PO value, outside the configured ±5% tolerance; rejected.
  * Quantity: 1,500 units
  * Total Header Charge Amount: $7,500.00
* **Tolerance Levels:**
  * Header Charge Per Unit Tolerance: ±5%

Ponieważ opłata za jednostkę ($5.00) przekracza dopuszczalny zakres tolerancji wynoszący 5% i nie została zatwierdzona, system:

1. **Reject the Invoiced Header Charge Per Unit:** System nie akceptuje zafakturowanej opłaty nagłówkowej za jednostkę w wysokości $5.00 ze względu na odchylenie przekraczające limit tolerancji.
2. **Adjust the Header Charge Per Unit:** System dostosowuje opłatę za jednostkę, aby odpowiadała pierwotnemu zamówieniu lub zatwierdzonej opłacie za jednostkę:
   * Adjusted Header Charge Per Unit = $4.00 (from PO)
3. **Recalculate the Total Header Charge Amount:** System ponownie oblicza całkowitą kwotę opłaty w oparciu o skorygowaną opłatę jednostkową:
   * **Corrected Total Header Charge Amount = Quantity × Adjusted Header Charge Per Unit**
   * **Corrected Total Header Charge Amount = 1,500 units × $4.00 = $6,000.00**
4. **Generate a Credit Note:** Ponieważ pierwotna suma faktury była wyższa niż suma skorygowana, system generuje notę kredytową na zawyżoną kwotę:
   * **Credit Note Amount = Original Invoice Total - Corrected Total Header Charge Amount**
   * **Credit Note Amount = $7,500.00 - $6,000.00 = $1,500.00**
5. **Process the Invoice:** System przetwarza fakturę zawierającą skorygowaną łączną kwotę obciążenia wynoszącą $6,000.00 i wystawia notę kredytową na kwotę $1,500.00 w celu rozliczenia nadmiernej kwoty.

Takie podejście gwarantuje, że transakcja jest zgodna z pierwotnymi warunkami zamówienia, zachowując dokładne przetwarzanie finansowe i korygując wszelkie nadmierne obciążenia.
