# Przypadek 7: Ilość w granicach tolerancji, cena jednostkowa poza tolerancją (odrzucenie — tolerancja dodatnia)

Poniższy scenariusz to przykładowe skonfigurowane mapowanie, a nie zweryfikowany, wdrożony szablon domyślny. Rzeczywiste dane wyjściowe, kwoty, znaki i typy dokumentów zależą od aktywnych reguł i wyrażeń `conflict_resolution`, mapowania eksportu oraz decyzji zatwierdzających. Opisana poniżej nota obciążeniowa lub uznaniowa jest uzależniona od tej konfiguracji; przykład nie gwarantuje automatycznego wystawienia ani zgodności z przepisami.

## Scenariusz:

Ilość mieści się w tolerancji, ale cena jednostkowa przekracza dopuszczalny zakres (tolerancja dodatnia) i nie zostaje zatwierdzona.

## Działanie:

System odrzuca cenę jednostkową faktury, dostosowuje ją do zamówienia zakupu i może wygenerować notę obciążeniową w celu rozliczenia zawyżonej kwoty.

## Przykład:

* **Purchase Order (PO):**
  * Quantity: 200 jednostek
  * Unit Price: $15.00 za jednostkę
  * Total Amount: $3,000.00
* **Invoice Received:**
  * Quantity: 198 jednostek — 1% poniżej wartości PO, w ramach skonfigurowanej tolerancji ±2%.
  * Unit Price: $17.00 za jednostkę — 13.33% powyżej wartości PO, poza skonfigurowaną tolerancją ±1%; odrzucona.
  * Total Amount: $3,366.00
* **Tolerance Levels:**
  * Quantity Tolerance: ±2%
  * Unit Price Tolerance: ±1%

Ponieważ ilość (198 jednostek) mieści się w dopuszczalnym zakresie tolerancji, ale cena jednostkowa ($17.00) przekracza dopuszczalną tolerancję i nie zostaje zatwierdzona, system:

1. **Odrzuca cenę jednostkową faktury:** System nie akceptuje zafakturowanej ceny jednostkowej wynoszącej $17.00.
2. **Dostosowuje cenę jednostkową:** System dostosowuje cenę jednostkową do ceny jednostkowej z pierwotnego zamówienia zakupu.
   * Skorygowana cena jednostkowa = $15.00 (z PO)
3. **Oblicza skorygowaną kwotę całkowitą:** Na podstawie skorygowanej ceny jednostkowej system ponownie oblicza kwotę całkowitą.
   * **Corrected Total Amount = Quantity × Adjusted Unit Price**
   * **Corrected Total Amount = 198 units × $15.00 per unit = $2,970.00**
4. **Generuje notę obciążeniową:** System generuje notę obciążeniową w celu rozliczenia różnicy wynikającej z zawyżenia.
   * **Debit Note Amount = Original Invoice Total - Corrected Total Amount**
   * **Debit Note Amount = $3,366.00 - $2,970.00 = $396.00**
   * Ta nota obciążeniowa odpowiada kwocie zawyżonej przez dostawcę.
5. **Przetwarza fakturę:** System przetwarza fakturę ze skorygowaną kwotą całkowitą $2,970.00 i wystawia notę obciążeniową na $396.00 w celu wyrównania zawyżenia.

Takie podejście zapewnia korektę każdego zawyżenia, zgodność transakcji z warunkami zamówienia zakupu oraz ochronę interesów finansowych firmy.
