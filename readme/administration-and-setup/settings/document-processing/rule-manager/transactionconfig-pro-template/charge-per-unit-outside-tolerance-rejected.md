# Przypadek 15: Opłata pozycji za jednostkę poza tolerancją (odrzucona)

Poniższy scenariusz ilustruje skonfigurowane mapowanie, a nie domyślny szablon o zweryfikowanym wdrożeniu. Rzeczywiste dane wyjściowe, kwoty, znaki i typy dokumentów zależą od aktywnych reguł i wyrażeń `conflict_resolution`, mapowania eksportu oraz decyzji zatwierdzających. Każda opisana nota obciążeniowa lub uznaniowa jest uzależniona od tej konfiguracji; przykład nie gwarantuje jej automatycznego wystawienia ani zgodności z prawem.

## Scenariusz

Opłata za jednostkę w pozycji jest poza tolerancją, a odchylenie nie zostało zatwierdzone. Ten przypadek dotyczy opłaty pozycji, a nie opłaty nagłówka.

## Przykładowe działanie

Mapowanie skonfigurowane tak, aby po odrzuceniu używać opłaty z PO, zastąpiłoby opłatę jednostkową z faktury wartością z PO. Każda osobna korekta, nota obciążeniowa lub uznaniowa zależy od mapowania eksportu i decyzji zatwierdzających.

## Przykład

* **Zamówienie zakupu (PO):**
  * Opłata pozycji za jednostkę: $4.00
  * Ilość: 1,500 sztuk
  * Łączna opłata pozycji: $6,000.00
* **Otrzymana faktura:**
  * Opłata pozycji za jednostkę: $5.00 — o 25% wyższa od wartości PO, poza skonfigurowaną tolerancją ±5%; odrzucona.
  * Ilość: 1,500 sztuk
  * Łączna opłata pozycji: $7,500.00
* **Skonfigurowana tolerancja:** Opłata za jednostkę ±5%.

W tym przykładowym mapowaniu:

1. Odrzuć zafakturowaną opłatę $5.00 za jednostkę, ponieważ odchylenie 25% przekracza ±5% i nie zostało zatwierdzone.
2. Użyj opłaty z PO wynoszącej $4.00 za jednostkę.
3. Przelicz łączną opłatę pozycji: **1,500 sztuk × $4.00 = $6,000.00**.
4. Oblicz nadwyżkę na fakturze: **$7,500.00 - $6,000.00 = $1,500.00**.
5. Zastosuj skonfigurowaną obsługę różnicy. Nota uznaniowa na $1,500.00 jest jednym z możliwych wyników mapowania, a nie gwarantowanym działaniem systemu. Jej kwota, znak, typ dokumentu i wystawienie zależą od aktywnych reguł, mapowania eksportu i zatwierdzeń.

Sprawdź mapowanie opłat pozycji oraz wynikowe dokumenty księgowe przed użyciem scenariusza w środowisku produkcyjnym.
