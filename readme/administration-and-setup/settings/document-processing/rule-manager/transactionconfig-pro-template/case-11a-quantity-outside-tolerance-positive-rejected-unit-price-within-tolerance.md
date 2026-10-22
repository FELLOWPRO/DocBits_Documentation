# Przypadek 11a: Ilość za duża — odrzucenie; cena w tolerancji

Poniższy scenariusz ilustruje skonfigurowane mapowanie, a nie domyślny szablon o zweryfikowanym wdrożeniu. Rzeczywiste dane wyjściowe, kwoty, znaki i typy dokumentów zależą od aktywnych reguł i wyrażeń `conflict_resolution`, mapowania eksportu oraz decyzji zatwierdzających. Każda opisana nota obciążeniowa lub uznaniowa jest uzależniona od tej konfiguracji; przykład nie gwarantuje jej automatycznego wystawienia ani zgodności z prawem.

## Scenariusz:

Ilość na fakturze przekracza dopuszczalny zakres (dodatnia) i zostaje odrzucona, ale cena jednostkowa mieści się w tolerancji.

## Działanie:

System dostosowuje ilość do zatwierdzonego poziomu, zachowując cenę jednostkową i realizuje transakcję. Jakakolwiek nadwyżka jest odrzucana i nie fakturowana.

## Przykład:

* **Purchase Order (PO):**
  * Quantity: 100 units
  * Cena jednostkowa: $8.00 za sztukę
  * Total Amount: $800.00
* **Invoice Received:**
  * Ilość: 110 sztuk (poza tolerancją 10%, odrzucona)
  * Cena jednostkowa: $8.00 za sztukę (w granicach tolerancji)
  * Total Amount: $880.00
* **Tolerance Levels:**
  * Quantity Tolerance: ±5%
  * Tolerancja ceny jednostkowej: ±2%

Ponieważ ilość (110 sztuk) przekracza akceptowalny limit tolerancji (dodatnie odchylenie 10%) i nie została zatwierdzona, ale cena jednostkowa ($8.00) mieści się w tolerancji, system:

1. **Odrzuć nadmiarową ilość:** System odrzuca ilość przekraczającą zatwierdzony poziom tolerancji.
2. **Dostosuj ilość:** System dostosowuje ilość, aby odpowiadała zatwierdzonemu poziomowi określonemu w zamówieniu.
   * Zatwierdzona ilość = 100 jednostek (od PO)
3. **Utrzymaj cenę jednostkową:** Cena jednostkowa wynosząca $8.00 za jednostkę mieści się w granicach tolerancji i pozostaje niezmieniona.
4. **Przelicz kwotę całkowitą:** System oblicza całkowitą kwotę na podstawie zatwierdzonej ilości i zaakceptowanej ceny jednostkowej:
   * **Kwota całkowita = Zatwierdzona ilość × Cena jednostkowa**
   * **Kwota całkowita = 100 jednostek × $8.00 za jednostkę = $800.00**
5. **Przetwórz fakturę:** System przetwarza fakturę na skorygowaną łączną kwotę $800.00, uwzględniającą jedynie zatwierdzoną ilość i cenę jednostkową. Nadwyżka wynosząca 10 sztuk jest odrzucana i nie fakturowana.

Takie podejście gwarantuje, że zafakturowana kwota jest zgodna z warunkami uzgodnionymi w zamówieniu, nawet jeśli dostawca próbuje wystawić fakturę za nadwyżkę.
