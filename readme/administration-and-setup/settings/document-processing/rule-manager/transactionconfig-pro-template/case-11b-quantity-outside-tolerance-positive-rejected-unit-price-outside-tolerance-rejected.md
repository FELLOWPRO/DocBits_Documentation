# Przypadek 11b: Ilość za duża i cena poza tolerancją — odrzucenie

Poniższy scenariusz ilustruje skonfigurowane mapowanie, a nie domyślny szablon o zweryfikowanym wdrożeniu. Rzeczywiste dane wyjściowe, kwoty, znaki i typy dokumentów zależą od aktywnych reguł i wyrażeń `conflict_resolution`, mapowania eksportu oraz decyzji zatwierdzających. Każda opisana nota obciążeniowa lub uznaniowa jest uzależniona od tej konfiguracji; przykład nie gwarantuje jej automatycznego wystawienia ani zgodności z prawem.

## Scenariusz:

Ilość przekracza dopuszczalny zakres (dodatni) i zostaje odrzucona, a cena jednostkowa również znajduje się poza tolerancją i zostaje odrzucona.

## Działanie:

System dostosowuje ilość i cenę jednostkową do zatwierdzonych poziomów z zamówienia, odrzucając ewentualne nadwyżki i realizuje transakcję.

## Przykład:

* **Purchase Order (PO):**
  * Quantity: 200 units
  * Cena jednostkowa: $50.00 za sztukę
  * Total Amount: $10,000.00
* **Invoice Received:**
  * Ilość: 220 sztuk (poza tolerancją 10%, odrzucona)
  * Cena jednostkowa: $55.00 za sztukę (poza tolerancją 10%, odrzucona)
  * Total Amount: $12,100.00
* **Tolerance Levels:**
  * Quantity Tolerance: ±5%
  * Tolerancja ceny jednostkowej: ±2%

Ponieważ zarówno ilość (220 sztuk), jak i cena jednostkowa ($55.00) przekraczają dopuszczalne granice tolerancji i żadna z nich nie została zatwierdzona, system:

1. **Odrzuć nadwyżkę:** System nie akceptuje zafakturowanej ilości 220 sztuk i dostosowuje ją tak, aby odpowiadała pierwotnemu zamówieniu.
   * Skorygowana ilość = 200 jednostek (od PO)
2. **Odrzuć fakturowaną cenę jednostkową:** System nie akceptuje zafakturowanej ceny jednostkowej wynoszącej $55.00 i dostosowuje ją do pierwotnego zamówienia.
   * Skorygowana cena jednostkowa = $50.00 za jednostkę (od PO)
3. **Przelicz kwotę całkowitą:** System oblicza kwotę całkowitą na podstawie skorygowanej ilości i ceny jednostkowej:
   * **Skorygowana kwota całkowita = skorygowana ilość × skorygowana cena jednostkowa**
   * **Skorygowana kwota całkowita = 200 sztuk × $50.00 za jednostkę = $10,000.00**
4. **Przetwórz fakturę:** System przetwarza fakturę ze skorygowaną kwotą całkowitą $10,000.00, odrzucając nadmierną ilość i wyższą cenę jednostkową.

Takie podejście gwarantuje, że transakcja jest zgodna z pierwotnymi warunkami zamówienia, zachowując spójną kontrolę cen i ilości, jednocześnie odrzucając niezatwierdzone odchylenia.
