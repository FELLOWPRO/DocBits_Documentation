# Opłata za jednostkę poza granicami tolerancji (Odrzucono)

Poniższy scenariusz ilustruje skonfigurowane mapowanie, a nie domyślny szablon o zweryfikowanym wdrożeniu. Rzeczywiste dane wyjściowe, kwoty, znaki i typy dokumentów zależą od aktywnych reguł i wyrażeń `conflict_resolution`, mapowania eksportu oraz decyzji zatwierdzających. Każda opisana nota obciążeniowa lub uznaniowa jest uzależniona od tej konfiguracji; przykład nie gwarantuje jej automatycznego wystawienia ani zgodności z prawem.

## Scenariusz:

Opłata za jednostkę wykracza poza tolerancję i nie została zatwierdzona.

## Działanie:

System dostosowuje opłatę jednostkową do zamówienia lub zatwierdzonych poziomów, generując wszelkie niezbędne noty debetowe lub kredytowe.

## Przykład:

* **Purchase Order (PO):**
  * Charge Per Unit: $6.00
  * Quantity: 800 units
  * Total Charge Amount: $4,800.00
* **Invoice Received:**
  * Charge Per Unit: $7.00 (odchylenie 16.67%, poza tolerancją ±5%, odrzucona)
  * Quantity: 800 units
  * Total Charge Amount: $5,600.00
* **Tolerance Levels:**
  * Charge Per Unit Tolerance: ±5%

Ponieważ opłata jednostkowa ($7.00) przekracza dopuszczalny zakres tolerancji wynoszący 5% i nie została zatwierdzona, system:

1. **Reject the Invoiced Charge Per Unit:** System nie akceptuje zafakturowanej opłaty jednostkowej w wysokości $7.00 ze względu na odchylenie przekraczające limit tolerancji.
2. **Adjust the Charge Per Unit:** System dostosowuje opłatę jednostkową, aby odpowiadała zamówieniu lub zatwierdzonej opłacie jednostkowej:
   * Adjusted Charge Per Unit = $6.00 (od PO)
3. **Recalculate the Total Charge Amount:** System ponownie przeliczy całkowitą kwotę opłaty w oparciu o skorygowaną opłatę jednostkową:
   * **Corrected Total Charge Amount = Quantity × Adjusted Charge Per Unit**
   * **Corrected Total Charge Amount = 800 units × $6.00 = $4,800.00**
4. **Generate a Debit Note:** Ponieważ pierwotna suma faktury była wyższa niż suma skorygowana, system generuje notę debetową na zawyżoną kwotę:
   * **Debit Note Amount = Original Invoice Total - Corrected Total Charge Amount**
   * **Debit Note Amount = $5,600.00 - $4,800.00 = $800.00**
5. **Process the Invoice:** System przetwarza fakturę zawierającą skorygowaną łączną kwotę obciążenia wynoszącą $4,800.00 i wystawia notę debetową na kwotę $800.00 w celu rozliczenia nadmiernej kwoty.

Takie podejście zapewnia zgodność transakcji finansowych z warunkami zamówienia zakupu, odrzucając niezatwierdzone rozbieżności i zachowując dokładne praktyki rozliczeniowe.
