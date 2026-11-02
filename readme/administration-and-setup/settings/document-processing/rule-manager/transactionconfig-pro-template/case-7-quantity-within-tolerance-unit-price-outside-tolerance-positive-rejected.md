# Przypadek 7: Ilość w tolerancji; cena za wysoka — odrzucenie

Poniższy scenariusz ilustruje skonfigurowane mapowanie, a nie domyślny szablon o zweryfikowanym wdrożeniu. Rzeczywiste dane wyjściowe, kwoty, znaki i typy dokumentów zależą od aktywnych reguł i wyrażeń `conflict_resolution`, mapowania eksportu oraz decyzji zatwierdzających. Każda opisana nota obciążeniowa lub uznaniowa jest uzależniona od tej konfiguracji; przykład nie gwarantuje jej automatycznego wystawienia ani zgodności z prawem.

## Scenariusz:

Ilość mieści się w tolerancji, ale cena jednostkowa przekracza dopuszczalny zakres (tolerancja dodatnia) i nie jest zatwierdzana.

## Działanie:

System odrzuca cenę jednostkową faktury, dostosowuje ją do zamówienia i może wygenerować notę obciążeniową w celu rozliczenia zawyżonej kwoty.

## Przykład:

* **Purchase Order (PO):**
  * Quantity: 200 units
  * Cena jednostkowa: $15.00 za sztukę
  * Total Amount: $3,000.00
* **Invoice Received:**
  * Ilość: 198 szt. (w tolerancji 1%)
  * Cena jednostkowa: $17.00 za sztukę (poza dodatnią tolerancją 13.33%)
  * Total Amount: $3,366.00
* **Tolerance Levels:**
  * Quantity Tolerance: ±2%
  * Tolerancja ceny jednostkowej: ±1%

Ponieważ ilość (198 jednostek) mieści się w dopuszczalnym zakresie tolerancji, ale cena jednostkowa ($17.00) przekracza dopuszczalną tolerancję i nie jest zatwierdzona, system:

1. **Odrzuć fakturowaną cenę jednostkową:** System nie akceptuje zafakturowanej ceny jednostkowej wynoszącej $17.00.
2. **Dostosuj cenę jednostkową:** System dostosowuje cenę jednostkową, aby odpowiadała cenie jednostkowej pierwotnego zamówienia zakupu.
   * Skorygowana cena jednostkowa = $15.00 (od PO)
3. **Oblicz skorygowaną kwotę całkowitą:** Korzystając ze skorygowanej ceny jednostkowej, system ponownie oblicza całkowitą kwotę.
   * **Skorygowana kwota całkowita = ilość × skorygowana cena jednostkowa**
   * **Skorygowana kwota całkowita = 198 jednostek × $15.00 za jednostkę = $2,970.00**
4. **Wygeneruj notę debetową:** System generuje notę debetową w celu uwzględnienia różnicy wynikającej z nadmiernego obciążenia.
   * **Kwota noty debetowej = Suma oryginalnej faktury – Skorygowana kwota całkowita**
   * **Kwota noty debetowej = $3,366.00 - $2,970.00 = $396.00**
   * Niniejsza nota debetowa przedstawia kwotę zawyżoną przez dostawcę.
5. **Przetwórz fakturę:** System przetwarza fakturę na skorygowaną łączną kwotę $2,970.00 i wystawia notę debetową na kwotę $396.00 w celu skompensowania nadmiernego obciążenia.

Takie podejście gwarantuje skorygowanie wszelkich nadmiernych opłat, dostosowanie transakcji do warunków zamówienia i ochronę interesów finansowych firmy.
