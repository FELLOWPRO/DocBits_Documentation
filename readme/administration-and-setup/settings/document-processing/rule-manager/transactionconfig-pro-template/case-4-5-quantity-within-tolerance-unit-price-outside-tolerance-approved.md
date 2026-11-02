# Przypadek 4, 5: Ilość w tolerancji; cena poza tolerancją — zatwierdzenie

Poniższy scenariusz ilustruje skonfigurowane mapowanie, a nie domyślny szablon o zweryfikowanym wdrożeniu. Rzeczywiste dane wyjściowe, kwoty, znaki i typy dokumentów zależą od aktywnych reguł i wyrażeń `conflict_resolution`, mapowania eksportu oraz decyzji zatwierdzających. Każda opisana nota obciążeniowa lub uznaniowa jest uzależniona od tej konfiguracji; przykład nie gwarantuje jej automatycznego wystawienia ani zgodności z prawem.

## Scenariusz:

Ilość na fakturze mieści się w tolerancji, ale cena jednostkowa wykracza poza dopuszczalny zakres tolerancji. Jednakże ta różnica w cenie jednostkowej została sprawdzona i zatwierdzona przez uprawnione osoby.

## Działanie:

System dostosowuje cenę jednostkową do zamówienia i stosuje wszelkie niezbędne opłaty za pozycje w celu uwzględnienia różnicy.

## Przykład:

**Purchase Order (PO):**

Quantity: <mark style="color:green;">100</mark> units

Cena jednostkowa: $10.00 za sztukę

Total Amount: <mark style="color:purple;">$1,000.00</mark>

**Invoice Received:**

Ilość: <mark style="color:green;">100</mark> jednostek (w granicach tolerancji)

Cena jednostkowa: <mark style="color:red;">$11.00</mark> za sztukę (tolerancja zewnętrzna ±5%)

Total Amount: <mark style="color:red;">$1,100.00</mark>

**Tolerance Levels:**

Quantity Tolerance: ±2%

Tolerancja ceny jednostkowej: ±5% (oczekiwany zakres: $9.50–$10.50)

**Approval:**

• Cena jednostkowa $11.00 wykracza poza zakres tolerancji, ale została ręcznie zatwierdzona przez odpowiedni dział.

Ponieważ ilość mieści się w tolerancji, ale cena jednostkowa wykracza poza tolerancję (mimo to zatwierdzona), system:

1\. **Dostosuj cenę jednostkową**: System dostosowuje cenę jednostkową z powrotem do ceny jednostkowej PO, ponieważ rozbieżność została zatwierdzona:

• **skorygowana cena jednostkowa = $10.00 za jednostkę**

• **Skorygowana kwota całkowita = 100 jednostek × $10.00 za jednostkę = $1,000.00**

2\. **Zastosuj opłatę za pozycję za różnicę**: Ponieważ zatwierdzona cena jednostkowa wynosząca $11.00 jest wyższa niż cena jednostkowa PO wynosząca $10.00, system nalicza opłatę za pozycję w celu uwzględnienia tej różnicy:

• **Kwota opłaty za pozycjej = (Zatwierdzona cena jednostkowa na fakturze - PO Cena jednostkowa) × Ilość**

• **Kwota opłaty za linię = ($11.00 - $10.00) × 100 jednostek = $100.00**

3\. **Przetwórz fakturę**: System przetwarza fakturę za pomocą:

• **Base Amount:** $1,000.00

• **Line Charge:** $100.00

• **Całkowita przetworzona kwota:** $1,100.00

Zapewnia to, że chociaż podstawowe wartości PO zostaną zachowane w celu zapewnienia spójności, zatwierdzona różnica w cenie jednostkowej zostanie uwzględniona w dodatkowej opłacie za pozycję, co skutkuje dokładnym przetwarzaniem finansowym i prowadzeniem rejestrów.
