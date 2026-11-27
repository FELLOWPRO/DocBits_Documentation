# Przypadek 1, 2, 3: Ilość i cena jednostkowa w granicach tolerancji

Poniższy scenariusz ilustruje skonfigurowane mapowanie, a nie domyślny szablon o zweryfikowanym wdrożeniu. Rzeczywiste dane wyjściowe, kwoty, znaki i typy dokumentów zależą od aktywnych reguł i wyrażeń `conflict_resolution`, mapowania eksportu oraz decyzji zatwierdzających. Każda opisana nota obciążeniowa lub uznaniowa jest uzależniona od tej konfiguracji; przykład nie gwarantuje jej automatycznego wystawienia ani zgodności z prawem.

## Scenariusz:

Zarówno ilość, jak i cena jednostkowa na fakturze mieszczą się w akceptowalnym przedziale tolerancji w porównaniu do zamówienia.

## Działanie:

System akceptuje wartości faktur i oblicza łączną kwotę na podstawie podanej ilości i ceny jednostkowej.

## Przykład:

**Purchase Order (PO):**

Quantity: 100 units

Unit Price: $10.00 per unit

Total Amount: $1,000.00

**Invoice Received:**

Quantity: 101 units — 1% above the PO value, within the configured ±2% tolerance.

Unit Price: $10.05 per unit — 0.5% above the PO value, within the configured ±1% tolerance.

Total Amount: $1,015.05

**Tolerance Levels:**

Quantity Tolerance: ±2%

Unit Price Tolerance: ±1%


Ponieważ ilość (101 sztuk) i cena jednostkowa ($10.05) mieszczą się w dopuszczalnych poziomach tolerancji w porównaniu z zamówieniem, system:


1\. **Zaakceptuj wartości z faktury:** Ilość i cena jednostkowa na fakturze są akceptowane jako ważne, ponieważ mieszczą się w zdefiniowanych granicach tolerancji.

2\. **Oblicz kwotę całkowitą:** Całkowita kwota jest obliczana przy użyciu zaakceptowanych wartości:

• Total Amount = Quantity × Unit Price

• Total Amount = 101 units × $10.05 per unit = $1,015.05

3\. **Przetwórz fakturę:** Faktura zostanie przetworzona na łączną kwotę $1,015.05, a zapisy finansowe zostaną odpowiednio zaktualizowane.

Takie podejście gwarantuje, że drobne rozbieżności mieszczące się w akceptowalnych granicach tolerancji nie doprowadzą do odrzucenia faktury lub opóźnień w płatnościach, co usprawnia proces finansowy.
