# Opłata za jednostkę w granicach tolerancji

Poniższy scenariusz ilustruje skonfigurowane mapowanie, a nie domyślny szablon o zweryfikowanym wdrożeniu. Rzeczywiste dane wyjściowe, kwoty, znaki i typy dokumentów zależą od aktywnych reguł i wyrażeń `conflict_resolution`, mapowania eksportu oraz decyzji zatwierdzających. Każda opisana nota obciążeniowa lub uznaniowa jest uzależniona od tej konfiguracji; przykład nie gwarantuje jej automatycznego wystawienia ani zgodności z prawem.

## Scenariusz:

Charge Per Unit na fakturze mieści się w dopuszczalnym zakresie tolerancji w porównaniu do zamówienia.

## Działanie:

System przyjmuje Charge Per Unit zgodnie z fakturą i przetwarza transakcję bez korekt.

## Przykład:

* **Purchase Order (PO):**
  * Charge Per Unit: $5.00
  * Quantity: 500 units
  * Total Charge Amount: $2,500.00
* **Invoice Received:**
  * Charge Per Unit: $5.10 (variance 2%, within the ±3% tolerance)
  * Quantity: 500 units
  * Total Charge Amount: $2,550.00
* **Tolerance Levels:**
  * Charge Per Unit Tolerance: ±3%

Ponieważ Charge Per Unit ($5.10) mieści się w akceptowalnym przedziale tolerancji wynoszącym 3% w porównaniu z zamówieniem, system:

1. **Accept the Charge Per Unit:** System akceptuje zafakturowany Charge Per Unit w wysokości $5.10, ponieważ mieści się on w zdefiniowanym limicie tolerancji.
2. **Process the Transaction:** System przetwarza fakturę z Total Charge Amount w oparciu o zafakturowany Charge Per Unit i Quantity:
   * **Total Charge Amount = Quantity × Charge Per Unit**
   * **Total Charge Amount = 500 units × $5.10 = $2,550.00**
3. **Finalize the Invoice:** System przetwarza transakcję bez żadnych korekt, akceptując fakturę taką, jaka jest.

Takie podejście umożliwia systemowi uwzględnienie niewielkich, akceptowalnych różnic w opłatach, zapewniając płynne i wydajne przetwarzanie transakcji bez zbędnych odrzuceń i opóźnień.
