# Przypadek 11b: Ilość za duża i cena poza tolerancją — odrzucenie

Poniższy scenariusz ilustruje skonfigurowane mapowanie, a nie domyślny szablon o zweryfikowanym wdrożeniu. Rzeczywiste dane wyjściowe, kwoty, znaki i typy dokumentów zależą od aktywnych reguł i wyrażeń `conflict_resolution`, mapowania eksportu oraz decyzji zatwierdzających. Każda opisana nota obciążeniowa lub uznaniowa jest uzależniona od tej konfiguracji; przykład nie gwarantuje jej automatycznego wystawienia ani zgodności z prawem.

## Scenariusz:

Ilość przekracza dopuszczalny zakres (dodatni) i zostaje odrzucona, a cena jednostkowa również znajduje się poza tolerancją i zostaje odrzucona.

## Działanie:

System dostosowuje ilość i cenę jednostkową do zatwierdzonych poziomów z zamówienia, odrzucając ewentualne nadwyżki i realizuje transakcję.

## Przykład:

* **Purchase Order (PO):**
  * Quantity: 200 units
  * Unit Price: $50.00 per unit
  * Total Amount: $10,000.00
* **Invoice Received:**
  * Quantity: 220 units — 10% above the PO value, outside the configured ±5% tolerance; rejected.
  * Unit Price: $55.00 per unit — 10% above the PO value, outside the configured ±2% tolerance; rejected.
  * Total Amount: $12,100.00
* **Tolerance Levels:**
  * Quantity Tolerance: ±5%
  * Unit Price Tolerance: ±2%

Ponieważ zarówno ilość (220 sztuk), jak i cena jednostkowa ($55.00) przekraczają dopuszczalne granice tolerancji i żadna z nich nie została zatwierdzona, system:

1. **Reject the Excess Quantity:** System nie akceptuje zafakturowanej ilości 220 sztuk i dostosowuje ją tak, aby odpowiadała pierwotnemu zamówieniu.
   * Adjusted Quantity = 200 units (from PO)
2. **Reject the Invoice Unit Price:** System nie akceptuje zafakturowanej ceny jednostkowej wynoszącej $55.00 i dostosowuje ją do pierwotnego zamówienia.
   * Adjusted Unit Price = $50.00 per unit (from PO)
3. **Recalculate the Total Amount:** System oblicza kwotę całkowitą na podstawie skorygowanej ilości i ceny jednostkowej:
   * **Corrected Total Amount = Adjusted Quantity × Adjusted Unit Price**
   * **Corrected Total Amount = 200 units × $50.00 per unit = $10,000.00**
4. **Process the Invoice:** System przetwarza fakturę ze skorygowaną kwotą całkowitą $10,000.00, odrzucając nadmierną ilość i wyższą cenę jednostkową.

Takie podejście gwarantuje, że transakcja jest zgodna z pierwotnymi warunkami zamówienia, zachowując spójną kontrolę cen i ilości, jednocześnie odrzucając niezatwierdzone odchylenia.
