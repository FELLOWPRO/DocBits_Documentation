# Przypadek 10a: Ilość za mała — odrzucenie; cena w tolerancji

Poniższy scenariusz ilustruje skonfigurowane mapowanie, a nie domyślny szablon o zweryfikowanym wdrożeniu. Rzeczywiste dane wyjściowe, kwoty, znaki i typy dokumentów zależą od aktywnych reguł i wyrażeń `conflict_resolution`, mapowania eksportu oraz decyzji zatwierdzających. Każda opisana nota obciążeniowa lub uznaniowa jest uzależniona od tej konfiguracji; przykład nie gwarantuje jej automatycznego wystawienia ani zgodności z prawem.

## Scenariusz:

Ilość jest poniżej dopuszczalnego zakresu (tolerancja ujemna) i nie jest zatwierdzona, choć cena jednostkowa mieści się w tolerancji.

## Działanie:

System dostosowuje ilość do zatwierdzonego poziomu, utrzymując stałą cenę jednostkową. Transakcja jest odpowiednio przetwarzana.

## Przykład:

* **Purchase Order (PO):**
  * Quantity: 150 units
  * Unit Price: $20.00 per unit
  * Total Amount: $3,000.00
* **Invoice Received:**
  * Quantity: 140 units — 6.67% below the PO value, outside the configured ±5% tolerance; rejected.
  * Unit Price: $20.00 per unit (within tolerance)
  * Total Amount: $2,800.00
* **Tolerance Levels:**
  * Quantity Tolerance: ±5%
  * Unit Price Tolerance: ±2%

Ponieważ ilość (140 jednostek) jest poniżej akceptowalnego limitu tolerancji (ujemna wariancja -6.67%) i nie została zatwierdzona, ale cena jednostkowa ($20.00) mieści się w granicach tolerancji, system:

1. **Odrzuć niższą ilość:** System nie akceptuje mniejszej ilości, ponieważ wykracza ona poza zatwierdzony zakres tolerancji.
2. **Dostosuj ilość:** System dostosowuje ilość, aby odpowiadała zatwierdzonemu poziomowi określonemu w zamówieniu.
   * Approved Quantity = 150 units (from PO)
3. **Utrzymaj cenę jednostkową:** Cena jednostkowa wynosząca $20.00 za jednostkę mieści się w granicach tolerancji i pozostaje niezmieniona.
4. **Przelicz kwotę całkowitą:** System oblicza całkowitą kwotę na podstawie zatwierdzonej ilości i zaakceptowanej ceny jednostkowej:
   * **Total Amount = Approved Quantity × Unit Price**
   * **Total Amount = 150 units × $20.00 per unit = $3,000.00**
5. **Przetwórz fakturę:** System przetwarza fakturę na skorygowaną łączną kwotę $3,000.00, odzwierciedlającą zatwierdzoną ilość i cenę jednostkową. Oczekuje się, że dostawca wystawi fakturę na całą zatwierdzoną ilość.

Takie podejście zapewnia zgodność transakcji finansowej z warunkami zamówienia i zapobiega zaniżaniu faktur przy jednoczesnym zachowaniu dokładnej dokumentacji finansowej.
