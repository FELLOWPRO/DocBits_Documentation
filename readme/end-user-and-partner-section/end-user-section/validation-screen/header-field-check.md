---
description: >-
  Skąd pochodzi wartość pola nagłówka i jak powstaje — wyjaśnienie funkcji
  Kontrola pól nagłówka na ekranie walidacji.
---

# Kontrola pól nagłówka: skąd pochodzą dane

Przycisk **Kontrola pól nagłówka** znajduje się obok przycisku **Zapisz** na ekranie walidacji. Otwiera raport *Skąd pochodzi każda wartość?*: dla każdego pola nagłówka pokazuje, co było na dokumencie, co zmieniło wartość po drodze, co DocBits wyświetla teraz i dlaczego.

Ta strona wyjaśnia, jak powstaje wartość i co oznacza każde źródło. Nie jest potrzebna wiedza ekspercka.

{% hint style="info" %}
Kontrola pól nagłówka jest częścią modułu **Analytics**. Jeśli przycisk jest wyszarzony, administrator może przyznać go Twojej roli w **Ustawienia › Role**.
{% endhint %}

## Wartość zawsze powstaje w tej kolejności

| Krok | Co się dzieje |
| --- | --- |
| **1. Odczyt** | Wartość jest odczytywana z dokumentu — przez wytrenowaną regułę, przez AI lub bezpośrednio z e-faktury. |
| **2. Przekształcenie** | Skrypty i reguły transformacji klienta zmieniają odczytaną wartość: skracają ją, uzupełniają, dostosowują format. |
| **3. Wyszukiwanie** | Wartość jest wyszukiwana w danych głównych. Jeśli coś zostanie znalezione, rekord danych głównych zastępuje odczytaną wartość. |
| **4. Wyświetlenie** | Użytkownik widzi tylko wynik. To, co stało się po drodze, pokazuje Kontrola pól nagłówka. |

Kroki 2 i 3 nie zawsze się wykonują — ale gdy się wykonują, zmieniają wartość. Właśnie stąd pochodzi większość zgłaszanych przypadków.

## Źródła — co oznacza każde z nich

Ikony są takie same jak w raporcie w kolumnie **Akcja** i na pasku filtrów u góry.

### Wytrenowana reguła

DocBits zapamiętuje, gdzie na tym typie dokumentu znajduje się pole, ponieważ ktoś kiedyś je tam zaznaczył.

* **Przykład:** dostawca „Bornemann” — zawsze w tym samym miejscu w lewym górnym rogu.
* **Jeśli jest błędne:** zaznacz właściwe miejsce na dokumencie i zapisz — reguła uczy się na tej podstawie.

### AI

Brak stałego wzorca. AI czyta dokument jak człowiek i samo decyduje, który tekst należy do którego pola.

* **Przykład:** data faktury, kwoty, warunki płatności.
* **Jeśli jest błędne:** popraw je. Włączyć i wyłączyć można w **Ustawienia › Pola nagłówka OCR**.

### E-faktura

W przypadku XRechnung lub ZUGFeRD nic nie jest rozpoznawane: wartość jest już polem danych w dokumencie i zostaje przejęta bezpośrednio.

* **Przykład:** numer faktury z pola XML nadawcy.
* **Jeśli jest błędne:** błąd leży po stronie nadawcy. DocBits pokazuje dokładnie, z którego pola XML pochodzi wartość.

### Skrypt / reguła transformacji

Po odczycie wkracza logika klienta i przekształca wartość. Dokument pozostaje taki sam — wartość nie.

* **Przykład:** `1001 / LS 206776` staje się `1001`.
* **Jeśli jest błędne:** nie szukaj na dokumencie. Sprawdź **Ustawienia › Skrypty** lub **Zasady transformacji**.

### Dane główne

Odczytana wartość jest wyszukiwana w Twoich własnych danych — zamówieniach, dostawcach. Dopasowanie zastępuje wartość i pociąga za sobą kolejne pola.

* **Przykład:** `1001` znajduje zamówienie `06O051001` — a dostawca i nabywca pochodzą wtedy również stamtąd.
* **Jeśli jest błędne:** sprawdź **Ustawienia › Konfiguracja Lookup**. Jest tam podane, czy wyszukiwanie jest dokładne, czy akceptuje także dopasowania częściowe.

### Obliczone

Nie odczytane, lecz obliczone z innych pól.

* **Przykład:** termin płatności z daty faktury plus warunków płatności.
* **Jeśli jest błędne:** zwykle błędne jest jedno z pól, z których wartość jest obliczana.

### Kod kreskowy

Odczytane z kodu kreskowego lub kodu QR na dokumencie.

* **Przykład:** numer faktury jest zakodowany w kodzie QR.
* **Jeśli jest błędne:** sprawdź ustawienia kodów kreskowych typu dokumentu.

## Najczęściej niezrozumiana rzecz

{% hint style="warning" %}
Gdy pole nagle zawiera wartość, która w takiej postaci nie występuje na dokumencie, prawie nigdy nie zrobiło tego AI — lecz krok 2 lub krok 3. Najczęściej jest to dopasowanie w danych głównych, które akceptuje także dopasowania częściowe: `1001` pasuje do `06O051001`, a wraz ze znalezionym zamówieniem zmienia się również dostawca.
{% endhint %}

W raporcie takie pole jest oznaczone na czerwono. Kolumna **Akcja** pokazuje rekord danych głównych wraz z czerwonym znacznikiem *tylko dopasowanie częściowe*, a pasująca część wartości jest podświetlona.

## Jak czytać raport

* **Znaczniki statusu** u góry zliczają pola, które pochodziły z dokumentu bez zmian, zostały zmienione po drodze lub nie występują na dokumencie w wyświetlanej postaci. Kliknij znacznik, aby pokazać tylko te pola; kliknij ponownie, aby pokazać wszystkie.
* **Filtr źródeł:** rząd ikon pokazuje każdą metodę ekstrakcji. Kliknij jedną, aby pokazać tylko pola, które przez nią przeszły.
* **Akcja:** każdy krok, przez który przeszła wartość, z ikoną jego źródła. Krok, z którego pochodzi bieżąca wartość, jest podświetlony. Najedź kursorem, aby zobaczyć, co zrobił każdy krok — z jakiej wartości na jaką.
* **Powód:** status pola. Ikona (i) wyjaśnia, dlaczego wartość jest taka, jaka jest. Jeśli widnieje *Pole nie istniało*, pola nie było na dokumencie.
* Długie wartości są skracane znakiem … — najedź kursorem, aby zobaczyć pełną wartość.
