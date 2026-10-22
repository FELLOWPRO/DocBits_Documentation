# Przypadek 1, 2, 3: Ilość i cena jednostkowa w granicach tolerancji

Poniższy scenariusz ilustruje skonfigurowane mapowanie, a nie domyślny szablon o zweryfikowanym wdrożeniu. Rzeczywiste dane wyjściowe, kwoty, znaki i typy dokumentów zależą od aktywnych reguł i wyrażeń `conflict_resolution`, mapowania eksportu oraz decyzji zatwierdzających. Każda opisana nota obciążeniowa lub uznaniowa jest uzależniona od tej konfiguracji; przykład nie gwarantuje jej automatycznego wystawienia ani zgodności z prawem.

## Scenariusz:

Zarówno ilość, jak i cena jednostkowa na fakturze mieszczą się w akceptowalnym przedziale tolerancji w porównaniu do zamówienia.

## Działanie:

System akceptuje wartości faktur i oblicza łączną kwotę na podstawie podanej ilości i ceny jednostkowej.

## Przykład:

**Purchase Order (PO):**

Quantity: 100 units

Cena jednostkowa: $10.00 za sztukę

Total Amount: $1,000.00

**Invoice Received:**

Ilość: 101 szt. (w granicach tolerancji 1%)

Cena jednostkowa: $10.05 za sztukę (w granicach tolerancji 0.5%)

Total Amount: $1,015.05

**Tolerance Levels:**

Quantity Tolerance: ±2%

Tolerancja ceny jednostkowej: ±1%\


Ponieważ ilość (101 sztuk) i cena jednostkowa ($10.05) mieszczą się w dopuszczalnych poziomach tolerancji w porównaniu z zamówieniem, system:\


1\. **Zaakceptuj wartości z faktury:** Ilość i cena jednostkowa na fakturze są akceptowane jako ważne, ponieważ mieszczą się w zdefiniowanych granicach tolerancji.

2\. **Oblicz kwotę całkowitą:** Całkowita kwota jest obliczana przy użyciu zaakceptowanych wartości:

• Całkowita kwota = ilość × cena jednostkowa

• Całkowita kwota = 101 jednostek × $10.05 za jednostkę = $1,015.05

3\. **Przetwórz fakturę:** Faktura zostanie przetworzona na łączną kwotę $1,015.05, a zapisy finansowe zostaną odpowiednio zaktualizowane.

Takie podejście gwarantuje, że drobne rozbieżności mieszczące się w akceptowalnych granicach tolerancji nie doprowadzą do odrzucenia faktury lub opóźnień w płatnościach, co usprawnia proces finansowy.
