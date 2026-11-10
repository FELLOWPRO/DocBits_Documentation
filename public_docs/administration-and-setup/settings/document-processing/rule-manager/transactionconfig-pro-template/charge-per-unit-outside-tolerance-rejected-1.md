# Opłata za jednostkę poza granicami tolerancji (Odrzucono)

Poniższy scenariusz ilustruje skonfigurowane mapowanie, a nie domyślny szablon o zweryfikowanym wdrożeniu. Rzeczywiste dane wyjściowe, kwoty, znaki i typy dokumentów zależą od aktywnych reguł i wyrażeń `conflict_resolution`, mapowania eksportu oraz decyzji zatwierdzających. Każda opisana nota obciążeniowa lub uznaniowa jest uzależniona od tej konfiguracji; przykład nie gwarantuje jej automatycznego wystawienia ani zgodności z prawem.

## Scenariusz:

Charge Per Unit wykracza poza tolerancję i nie został zatwierdzony.

## Działanie:

System dostosowuje Charge Per Unit do zamówienia lub zatwierdzonych poziomów, generując wszelkie niezbędne noty debetowe lub kredytowe.

## Przykład:

* **Purchase Order (PO):**
  * Charge Per Unit: $6.00
  * Quantity: 800 units
  * Total Charge Amount: $4,800.00
* **Invoice Received:**
  * Charge Per Unit: $7.00 — 16.67% above the PO value, outside the configured ±5% tolerance; rejected.
  * Quantity: 800 units
  * Total Charge Amount: $5,600.00
* **Tolerance Levels:**
  * Charge Per Unit Tolerance: ±5%

Ponieważ Charge Per Unit ($7.00) przekracza dopuszczalny zakres tolerancji wynoszący 5% i nie został zatwierdzony, system:

1. **Reject the Invoiced Charge Per Unit:** System nie akceptuje zafakturowanego Charge Per Unit w wysokości $7.00 ze względu na odchylenie przekraczające limit tolerancji.
2. **Adjust the Charge Per Unit:** System dostosowuje Charge Per Unit, aby odpowiadał zamówieniu lub zatwierdzonemu Charge Per Unit:
   * Adjusted Charge Per Unit = $6.00 (from PO)
3. **Recalculate the Total Charge Amount:** System ponownie przeliczy Total Charge Amount w oparciu o skorygowany Charge Per Unit:
   * **Corrected Total Charge Amount = Quantity × Adjusted Charge Per Unit**
   * **Corrected Total Charge Amount = 800 units × $6.00 = $4,800.00**
4. **Generate a Debit Note:** Ponieważ pierwotna suma faktury była wyższa niż skorygowana Total Charge Amount, system generuje notę debetową na zawyżoną kwotę:
   * **Debit Note Amount = Original Invoice Total - Corrected Total Charge Amount**
   * **Debit Note Amount = $5,600.00 - $4,800.00 = $800.00**
5. **Process the Invoice:** System przetwarza fakturę ze skorygowaną Total Charge Amount w wysokości $4,800.00 i wystawia notę debetową na kwotę $800.00 w celu rozliczenia nadmiernej kwoty.

Takie podejście zapewnia zgodność transakcji finansowych z warunkami zamówienia zakupu, odrzucając niezatwierdzone rozbieżności i zachowując dokładne praktyki rozliczeniowe.
