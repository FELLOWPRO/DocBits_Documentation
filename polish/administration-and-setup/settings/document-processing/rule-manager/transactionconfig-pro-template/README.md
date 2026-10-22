# TransactionConfig Pro Template

## Konfigurowanie przetwarzania dokumentów finansowych

_TransactionConfig Pro Template_ opisuje przykładowe mapowania dla faktur oraz not obciążeniowych i uznaniowych. Menedżer reguł może wykorzystywać skonfigurowane reguły i wyrażenia `conflict_resolution` do określania działań przetwarzania. Dokumentacja nie potwierdza wdrożenia predefiniowanego szablonu w danym środowisku.

Mapowania pól, typy transakcji i decyzje procesu trzeba skonfigurować dla właściwej integracji Infor M3/LN. Przykłady wyjaśniają tę konfigurację; nie gwarantują poprawnych wyników, integracji bez dostosowań ani zgodności z międzynarodowymi standardami finansowymi.

### Obszary konfiguracji

* **Mapowanie:** Zdefiniuj pola źródłowe i docelowe dla każdego typu transakcji i sprawdź wynikowe dane.
* **Dostosowanie:** Skonfiguruj reguły procesu biznesowego i zatwierdzania.
* **Automatyzacja:** Automatyzuj tylko decyzje wyraźnie objęte aktywnymi regułami i wyrażeniami.
* **Integracja:** Sprawdź mapowanie eksportu i wymagania docelowego systemu Infor M3/LN.
* **Zgodność:** Osobno oceń wymagania księgowe i podatkowe; sama konfiguracja nie gwarantuje zgodności z prawem.

## Przykładowe przypadki rozwiązywania konfliktów

Poniższy scenariusz ilustruje skonfigurowane mapowanie, a nie domyślny szablon o zweryfikowanym wdrożeniu. Rzeczywiste dane wyjściowe, kwoty, znaki i typy dokumentów zależą od aktywnych reguł i wyrażeń `conflict_resolution`, mapowania eksportu oraz decyzji zatwierdzających. Każda opisana nota obciążeniowa lub uznaniowa jest uzależniona od tej konfiguracji; przykład nie gwarantuje jej automatycznego wystawienia ani zgodności z prawem.

### [Przypadki 1, 2, 3: Ilość i cena jednostkowa w tolerancji](case-1-2-3-quantity-and-unit-price-within-tolerance.md)

**Scenariusz:** Ilość i cena na fakturze mieszczą się w skonfigurowanych tolerancjach względem PO.

**Przykładowe działanie:** Przykładowe mapowanie akceptuje wartości faktury i oblicza ilość × cena jednostkowa.

### [Przypadki 4, 5: Ilość w tolerancji, cena poza tolerancją (zatwierdzona)](case-4-5-quantity-within-tolerance-unit-price-outside-tolerance-approved.md)

**Scenariusz:** Ilość mieści się w tolerancji; odchylenie ceny ją przekracza i zostało zatwierdzone.

**Przykładowe działanie:** Przykładowe mapowanie używa ceny z PO i ujmuje zatwierdzoną różnicę jako opłatę pozycji, jeśli tak skonfigurowano.

### [Przypadek 6: Ilość w tolerancji, cena poniżej limitu (odrzucona)](case-6-quantity-within-tolerance-unit-price-outside-negative-tolerance-rejected.md)

**Scenariusz:** Ilość mieści się w tolerancji; cena jest poniżej dozwolonego zakresu i została odrzucona.

**Przykładowe działanie:** Przykładowe mapowanie używa ceny z PO. Różnica ze znakiem nie jest automatycznie notą uznaniową; typ i znak korekty zależą od mapowania.

### [Przypadek 7: Ilość w tolerancji, cena powyżej limitu (odrzucona)](case-7-quantity-within-tolerance-unit-price-outside-tolerance-positive-rejected.md)

**Scenariusz:** Ilość mieści się w tolerancji; dodatnie odchylenie ceny zostało odrzucone.

**Przykładowe działanie:** Przykładowe mapowanie używa ceny z PO. Każda nota lub korekta różnicy zależy od mapowania eksportu.

### [Przypadki 8a, 9a: Ilość poza tolerancją (zatwierdzona), cena w tolerancji](case-8a-9a-quantity-outside-tolerance-approved-unit-price-within-tolerance.md)

**Scenariusz:** Odchylenie ilości zostało zatwierdzone, a cena pozostaje w tolerancji.

**Przykładowe działanie:** Przykładowe mapowanie używa zatwierdzonej ilości z faktury i ceny jednostkowej z faktury.

### [Przypadek 11a: Ilość powyżej limitu (odrzucona), cena w tolerancji](case-11a-quantity-outside-tolerance-positive-rejected-unit-price-within-tolerance.md)

**Scenariusz:** Ilość przekracza tolerancję i została odrzucona; cena mieści się w tolerancji.

**Przykładowe działanie:** Przykładowe mapowanie używa zatwierdzonej ilości i zachowuje cenę. Obsługa nadwyżki zależy od skonfigurowanych reguł.

### [Przypadek 10a: Ilość poniżej limitu (odrzucona), cena w tolerancji](case-10a-quantity-outside-tolerance-negative-rejected-unit-price-within-tolerance.md)

**Scenariusz:** Ilość jest poniżej tolerancji i została odrzucona; cena mieści się w tolerancji.

**Przykładowe działanie:** Przykładowe mapowanie używa zatwierdzonej ilości i zachowuje cenę jednostkową.

### [Przypadki 8b, 9b: Ilość i cena poza tolerancją (zatwierdzone)](case-8b-9b-quantity-outside-tolerance-approved-unit-price-outside-tolerance-approved.md)

**Scenariusz:** Oba odchylenia, ilości i ceny, zostały zatwierdzone.

**Przykładowe działanie:** Przykładowe mapowanie używa zatwierdzonych wartości faktury oraz wyraźnie skonfigurowanych opłat pozycji lub korekt.

### [Przypadek 10b: Ilość poniżej limitu i cena poza tolerancją (odrzucone)](case-10b-quantity-outside-tolerance-negative-rejected-unit-price-outside-tolerance-rejected.md)

**Scenariusz:** Nie zatwierdzono ani ujemnego odchylenia ilości, ani odchylenia ceny.

**Przykładowe działanie:** Przykładowe mapowanie używa wartości PO lub wartości zatwierdzonych. Noty obciążeniowe i uznaniowe wymagają odpowiedniego mapowania oraz decyzji zatwierdzającej.

### [Przypadek 11b: Ilość powyżej limitu i cena poza tolerancją (odrzucone)](case-11b-quantity-outside-tolerance-positive-rejected-unit-price-outside-tolerance-rejected.md)

**Scenariusz:** Dodatnie odchylenie ilości i odchylenie ceny zostały odrzucone.

**Przykładowe działanie:** Przykładowe mapowanie używa zatwierdzonych wartości PO; obsługa nadwyżek zależy od aktywnej konfiguracji.

### [Przypadki 12, 13: Opłata pozycji za jednostkę w tolerancji](charge-per-unit-within-tolerance.md)

**Scenariusz:** Opłata pozycji za jednostkę mieści się w skonfigurowanej tolerancji względem PO.

**Przykładowe działanie:** Przykładowe mapowanie akceptuje opłatę pozycji z faktury bez korekty.

### [Przypadek 14: Opłata pozycji za jednostkę poza tolerancją (zatwierdzona)](charge-per-unit-outside-tolerance-approved-1.md)

**Scenariusz:** Opłata pozycji za jednostkę przekracza tolerancję i została zatwierdzona.

**Przykładowe działanie:** Przykładowe mapowanie stosuje zatwierdzoną opłatę pozycji.

### [Przypadek 15: Opłata pozycji za jednostkę poza tolerancją (odrzucona)](charge-per-unit-outside-tolerance-rejected.md)

**Scenariusz:** Opłata pozycji za jednostkę przekracza tolerancję i została odrzucona.

**Przykładowe działanie:** Przykładowe mapowanie używa opłaty pozycji z PO lub wartości zatwierdzonej. Każda nota dotycząca różnicy zależy od mapowania eksportu.

### [Przypadki 12, 13: Opłata nagłówka za jednostkę w tolerancji](case-12-13-header-charge-charge-per-unit-within-tolerance.md)

**Scenariusz:** Opłata nagłówka za jednostkę mieści się w skonfigurowanej tolerancji względem PO.

**Przykładowe działanie:** Przykładowe mapowanie stosuje opłatę nagłówka z faktury bez korekty.

### [Przypadek 14: Opłata nagłówka za jednostkę poza tolerancją (zatwierdzona)](charge-per-unit-outside-tolerance-approved.md)

**Scenariusz:** Opłata nagłówka za jednostkę przekracza tolerancję i została zatwierdzona.

**Przykładowe działanie:** Przykładowe mapowanie stosuje zatwierdzoną opłatę nagłówka.

### [Przypadek 15: Opłata nagłówka za jednostkę poza tolerancją (odrzucona)](case-15-header-charge-charge-per-unit-outside-tolerance-rejected.md)

**Scenariusz:** Opłata nagłówka za jednostkę przekracza tolerancję i została odrzucona.

**Przykładowe działanie:** Przykładowe mapowanie używa opłaty nagłówka z PO lub wartości zatwierdzonej. Każda osobna nota zależy od skonfigurowanej obsługi.

### [Pozycje podatkowe](tax-lines.md "mention")

**Scenariusz:** Kwoty podatku na fakturze i w PO różnią się.

**Przykładowe działanie:** Przykładowe mapowanie używa zatwierdzonych stawek i kwot podatku. Konfigurację należy sprawdzić pod kątem obowiązujących wymagań podatkowych; przykład nie gwarantuje zgodności z prawem.
