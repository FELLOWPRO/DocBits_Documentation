# Przypadek 6: Ilość w tolerancji, cena poniżej limitu (odrzucona)

Poniższy scenariusz ilustruje skonfigurowane mapowanie, a nie domyślny szablon o zweryfikowanym wdrożeniu. Rzeczywiste dane wyjściowe, kwoty, znaki i typy dokumentów zależą od aktywnych reguł i wyrażeń `conflict_resolution`, mapowania eksportu oraz decyzji zatwierdzających. Każda opisana nota obciążeniowa lub uznaniowa jest uzależniona od tej konfiguracji; przykład nie gwarantuje jej automatycznego wystawienia ani zgodności z prawem.

## Scenariusz

Ilość mieści się w tolerancji, ale cena jednostkowa na fakturze jest niższa od dozwolonego zakresu, a odchylenie ceny nie zostało zatwierdzone.

## Przykładowe działanie

Mapowanie skonfigurowane tak, aby po odrzuceniu używać ceny z PO, zachowałoby ilość i zastąpiło cenę jednostkową z faktury ceną z PO. To, czy różnica spowoduje korektę, notę obciążeniową, notę uznaniową czy brak osobnego dokumentu, zależy od aktywnego mapowania i decyzji zatwierdzających. Dodatkowe opłaty nagłówka stosuje się tylko wtedy, gdy zostały wyraźnie skonfigurowane.

## Przykład

* **Zamówienie zakupu (PO):**
  * Ilość: 100 sztuk
  * Cena jednostkowa: $10.00 za sztukę
  * Suma: $1,000.00
* **Otrzymana faktura:**
  * Ilość: 100 sztuk — rzeczywiste odchylenie 0%, w skonfigurowanej tolerancji ±2%.
  * Cena jednostkowa: $9.00 — rzeczywiste odchylenie -10%, poza skonfigurowaną tolerancją ±1%; odrzucona.
  * Suma: $900.00
* **Skonfigurowane tolerancje:**
  * Ilość: ±2%
  * Cena jednostkowa: ±1%

W tym przykładowym mapowaniu:

1. Odrzuć cenę jednostkową z faktury wynoszącą $9.00, ponieważ odchylenie przekracza tolerancję i nie zostało zatwierdzone.
2. Użyj ceny jednostkowej z PO wynoszącej $10.00.
3. Przelicz sumę przykładu: **100 sztuk × $10.00 = $1,000.00**.
4. Oblicz różnicę ze znakiem jako sumę faktury minus przeliczoną sumę: **$900.00 - $1,000.00 = -$100.00**.
5. Zastosuj skonfigurowane mapowanie eksportu i decyzję zatwierdzającą. Wartość -$100.00 jest różnicą ze znakiem, a nie bezwarunkowym poleceniem wystawienia noty uznaniowej. Mapowanie określa kwotę, znak i typ dokumentu każdej korekty.

Przykład nie oznacza, że nota uznaniowa automatycznie odwraca zaniżenie należności. Przed użyciem reguły sprawdź oczekiwane ujęcie księgowe w aktywnym mapowaniu eksportu.
