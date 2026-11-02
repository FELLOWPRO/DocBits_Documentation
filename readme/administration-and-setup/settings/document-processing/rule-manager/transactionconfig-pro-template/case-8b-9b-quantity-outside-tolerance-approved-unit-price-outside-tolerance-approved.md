# Przypadek 8b, 9b: Ilość i cena poza tolerancją — zatwierdzenie

Poniższy scenariusz ilustruje skonfigurowane mapowanie, a nie domyślny szablon o zweryfikowanym wdrożeniu. Rzeczywiste dane wyjściowe, kwoty, znaki i typy dokumentów zależą od aktywnych reguł i wyrażeń `conflict_resolution`, mapowania eksportu oraz decyzji zatwierdzających. Każda opisana nota obciążeniowa lub uznaniowa jest uzależniona od tej konfiguracji; przykład nie gwarantuje jej automatycznego wystawienia ani zgodności z prawem.

## Scenariusz:

Zarówno ilość, jak i cena jednostkowa znajdują się poza zakresem tolerancji, ale zostały zatwierdzone.

## Działanie:

System przetwarza transakcję, wykorzystując wartości faktury zarówno pod względem ilości, jak i ceny jednostkowej, stosując wszelkie niezbędne korekty lub opłaty za pozycje.

## Przykład:

* **Purchase Order (PO):**
  * Quantity: 200 units
  * Cena jednostkowa: $25.00 za sztukę
  * Total Amount: $5,000.00
* **Invoice Received:**
  * Ilość: 220 jednostek (tolerancja zewnętrzna 10%, zatwierdzona)
  * Cena jednostkowa: $27.00 za sztukę (tolerancja zewnętrzna 8%, zatwierdzona)
  * Total Amount: $5,940.00
* **Tolerance Levels:**
  * Quantity Tolerance: ±5%
  * Tolerancja ceny jednostkowej: ±2%

Ponieważ zarówno ilość (220 jednostek), jak i cena jednostkowa ($27.00) wykraczają poza dopuszczalne granice tolerancji, ale zostały zatwierdzone, system:

1. **Zaakceptuj zatwierdzoną ilość:** System akceptuje zafakturowaną ilość 220 jednostek, ponieważ została zatwierdzona pomimo wykraczania poza zakres tolerancji.
2. **Zaakceptuj zatwierdzoną cenę jednostkową:** System akceptuje zafakturowaną cenę jednostkową wynoszącą $27.00 za jednostkę, ponieważ została ona zatwierdzona pomimo wykraczania poza zakres tolerancji.
3. **Oblicz kwotę całkowitą:** System oblicza całkowitą kwotę na podstawie zatwierdzonych wartości faktury:
   * **Kwota całkowita = Ilość × Cena jednostkowa**
   * **Kwota całkowita = 220 jednostek × $27.00 za jednostkę = $5,940.00**
4. **Zastosuj niezbędne korekty lub opłaty za pozycje:** Jeśli ma to zastosowanie, system może zastosować dodatkowe opłaty za pozycje lub korekty w oparciu o zasady organizacji dotyczące postępowania z zatwierdzonymi odchyleniami.
5. **Przetwórz fakturę:** System przetwarza fakturę, korzystając z zatwierdzonych wartości zarówno ilości, jak i ceny jednostkowej, finalizując transakcję na łączną kwotę $5,940.00.

Takie podejście gwarantuje, że transakcja zostanie przeprowadzona zgodnie z zatwierdzonymi odchyleniami, co pozwala na elastyczność przy jednoczesnym zachowaniu dokładnych zapisów finansowych.
