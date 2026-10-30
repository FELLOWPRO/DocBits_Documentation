# Reguły transformacji: pełny przegląd praktyczny

> Znane ograniczenie podglądu (sprawdzone 29 października 2026 r., wersja 11.15.2): podczas dodawania prefiksu `INV-` podgląd błędnie zmienia `INV-4711` na `INV-INV-4711`. Niezależny test serwera zachowuje `INV-4711`. Sprawdź również wielokrotne wykonanie za pomocą testu serwera; poprawny wynik podglądu sam w sobie nie potwierdza pełnego wykonania podczas zapisywania.

Stan weryfikacji: 28 października 2026. Przykłady zostały zweryfikowane z wykorzystaniem syntetycznych wartości szkoleniowych na Dev NOVA. Podgląd nie jest dowodem zapisanej zmiany dokumentu, uzgodnienia zamówienia ani eksportu ERP.


## Etykiety widoczne w edytorze

Niektóre etykiety w aktualnym interfejsie są przetłumaczone niedokładnie. Tabela podaje faktycznie wyświetlany tekst, aby ułatwić znalezienie właściwego kroku; opis działania używa terminologii technicznej. Zrzuty pokazują niezmieniony interfejs.

| Operacja | Widoczna etykieta |
| --- | --- |
| case | Zmień wielkość liter |
| trim | Przycinać |
| pad | Podkładka |
| truncate | Ścięty |
| affix | Afiks |
| sanitize | Oczyść |
| substring | Weź kawałek |
| regex_extract | Ekstrakt |
| regex_replace | Znajdź i zamień |
| value_map | Mapuj wartości |
| date_format | Data formatowania |
| number_format | Formatuj liczbę |
| fix_value | Ustal wartość |
| clear | Wyczyść |
| clear_rows | Wyczyść wszystkie wiersze |
| add_row | Dodaj wiersz |


## Cztery zakresy obowiązywania

| Zakres | Wejście i cel | Typowe zadanie |
| --- | --- | --- |
| Pole nagłówka | Jedno pole na dokument; źródłem może być inne pole nagłówka | Wyczyścić numer faktury, przejąć numer zamówienia |
| Kolumna tabeli | Wybrana kolumna dla każdego wiersza wybranej tabeli | Ujednolicić numery artykułów lub kody jednostek |
| Wiersze tabeli | Cała tabela | Usunąć wiersze lub dodać zdefiniowane pozycje |
| Routing | Atrybut dokumentu `sub_org_id` | Przypisać istniejącą jednostkę podrzędną |

Zakresy uruchamiają się w kolejności **Pole nagłówka → Routing → Wiersze tabeli → Kolumna tabeli**. W ramach jednego zakresu o priorytecie i kluczu reguły decyduje kolejność. Kroki reguły uruchamiają się od góry do dołu. Późniejsza reguła może zatem odczytywać już zmienione wartości. Kolejność zakresów nie jest odwracana przez priorytet pojedynczej reguły.

## Wszystkie kroki edytora

Zweryfikowany edytor oferuje 14 kroków wartości dla nagłówka/kolumny, dwa kroki dla całych tabel i jedno stałe przypisanie w routingu. `fix_value` i stałe przypisanie routingu używają po stronie serwera obu `set_value`. Dodatkowo interfejs rozpoznaje `default`; ten krok nie jest oferowany w zweryfikowanym normalnym menu kroków.

| Krok | Warianty i parametry | Przykład | Granica i próba kontrolna |
| --- | --- | --- | --- |
| Zmiana wielkości liter (`case`) | upper, lower, title, capitalize | `inv-4711` → `INV-4711` | Title: `acme gmbh` → `Acme Gmbh`; capitalize: `aCME GMBH` → `Acme gmbh`. Nazwy własne/skróty mogą ulegać niepożądanym zmianom merytorycznym. Przy `capitalize` zweryfikowany podgląd przeglądarki pozostawia resztę niezmienioną, podczas gdy serwer zapisuje ją małymi literami; wartość serwerowa weryfikować osobno. |
| Przycięcie (`trim`) | obie / lewa / prawa; znak pusty = odstęp | `  4711  ` → `4711` | `47 11` pozostaje zachowane. Znaki z lewej `0`: `004711` → `4711`, ale `000` → puste. Znaki to zbiór, nie pełny tekst prefiksu. |
| Wypełnienie (`pad`) | minimalna długość, jeden znak wypełniający, lewa/prawa | Długość 10, lewa `0`: `4711` → `0000004711` | Już 11 znaków pozostaje 11 znaków. Prawa `_`, długość 6: `ABC` → `ABC___`. |
| Skrócenie (`truncate`) | maksymalna długość | Długość 10: `ABCDEFGHIJKL` → `ABCDEFGHIJ` | `ABC` pozostaje `ABC`. Obcięcie traci informacje i może powodować zlewanie się numerów. |
| Afiks (`affix`) | dodanie/usunięcie prefiksu/sufiksu | `INV-` + `4711` → `INV-4711` | Istniejący dokładny afiks nie jest dodawany podwójnie. Usunięcie działa tylko na odpowiedniej krawędzi i uwzględnia wielkość liter. |
| Oczyszczenie znaków (`sanitize`) | zachowaj alfanumeryczne / litery / cyfry / alfanumeryczne + spacje; alternatywnie usuń klasę znaków | `DE 123.456.789` → `DE123456789` | Znaki mogą mieć znaczenie merytoryczne. Przy usuwaniu wejście to klasa znaków wyrażenia regularnego; myślnik należy prawidłowo zabezpieczyć, np. `.\-/`. |
| Fragment (`substring`) | początek + długość **lub** początek + koniec; dozwolone indeksy ujemne | Początek 3, koniec 7: `DE-4711-X` → `4711` | Początek liczony od 0, koniec jest wyłączny. Początek −4: ostatnie cztery znaki. Wymagane oddzielne źródło oryginalne. |
| Wydobycie (`regex_extract`) | wyrażenie regularne, grupa przechwytująca | `PO[- ]?(\d+)`, grupa 1: `Order PO-45001234` → `45001234` | Pierwsze dopasowanie; grupa 0 = pełne dopasowanie. Bez dopasowania: puste. Wymagane oddzielne źródło. |
| Znajdź i zamień (`regex_replace`) | wzorzec, zamiennik, liczba | `\s+` → odstęp: `ACME    GmbH` → `ACME GmbH` | Liczba 0 = wszystkie, 1 = pierwsze dopasowanie. Wymagane oddzielne źródło. Wyrażenia regularne przeglądarki/serwera przy złożonych wzorcach weryfikować osobno. |
| Mapowanie wartości (`value_map`) | pełne pary z→do; ignoruj wielkość liter; zamiennik bez dopasowania | `stk` → `PCE` z `STK→PCE` i ignorowaną wielkością liter | Pusty zamiennik oznacza **zachowaj wejście**. `BOX` pozostaje `BOX`; stały zamiennik `C62` nadpisałby `BOX`. Przycięcie nie następuje automatycznie. |
| Formatowanie daty (`date_format`) | wzorzec wyjściowy, np. `%d.%m.%Y`, `%m/%d/%Y`, `%Y-%m-%d`, `%d %b %Y` | `2026-10-28` → `28.10.2026` w celu tekstowym | Przy polach nagłówka DATE zapisana wartość może pozostać w formacie ISO, a zmienić się tylko wyświetlanie. Nieczytelny tekst pozostaje niezmieniony; test serwerowy podaje przyczynę. |
| Formatowanie liczby (`number_format`) | de_DE / en_US / en_GB / fr_FR; min./maks. miejsca dziesiętne | `1234.5` → `1234,50` lub `1234.50` w zweryfikowanym wyniku serwerowym | Brak separatora tysięcy w zweryfikowanym wyniku serwerowym. Brak przeliczenia walutowego lub jednostkowego. Zaokrąglenie i ponowne przetwarzanie weryfikować osobno. |
| Wartość stała (`fix_value` w edytorze, `set_value` w API) | jedna stała wartość | `USD` → `EUR` | Nadpisuje również istniejące wartości. Nie mylić z wartością domyślną. |
| Opróżnienie (`clear`) | brak parametrów | `Altwert` → `""` | Opróżnia wartość; nie usuwa definicji pola ani dokumentu. |
| Usuń wszystkie wiersze (`clear_rows`) | tylko wiersze tabeli | 2 pozycje → 0 | Może unieważnić odniesienia wierszowe i istniejące uzgodnienie PO. |
| Dodaj wiersz (`add_row`) | początek/koniec; dla każdej kolumny stała wartość lub źródło nagłówka | Ilość `1`, kwota netto z `header.total_net_amount` | Bez wcześniejszego usunięcia tylko z odpowiednim wykonaniem jednorazowym. Brak automatycznej agregacji istniejących pozycji. |
| Stała jednostka podrzędna (`set_value`, Routing) | istniejący cel z wyboru jednostek podrzędnych | Dostawca A → Jednostka podrzędna Północ | Nie dowolny atrybut statusu/użytkownika/uprawnień. Alternatywnie przypisanie przez `value_map` i źródło. |

### Wartość domyślna przez interfejs

`default` uzupełnia swoją wartość tylko przy brakującym/pustym wejściu. Przy domyślnym `1` wartości `null` i `""` dają wartość `1`; `0` pozostaje `0`, `100` pozostaje `100`. Jest to zweryfikowane po stronie serwera. Zweryfikowany normalny edytor nie ma dla tego własnego kroku. Odpowiedni merytorycznie prosty przypadek można często odwzorować jako **Cel jest pusty → Wartość stała**. Jest to warunek reguły z przypisaniem, nie ukryty punkt menu.

## Dziewięć szczegółowych sekwencji praktycznych

- [01 · Podstawy, zakresy obowiązywania i bezpieczne testy](01-foundations.md)
- [02 · Czyszczenie tekstu: wielkość liter, przycinanie i znaki](02-text-cleaning.md)
- [03 · Kształtowanie numerów: wypełnienie, skrócenie, prefiks i sufiks](03-numbers-and-affixes.md)
- [04 · Fragmenty i wzorce: wycinanie, wydobywanie, zamiana](04-substrings-and-patterns.md)
- [05 · Mapowania wartości i reguły na wiersz tabeli](05-value-mapping.md)
- [06 · Prawidłowe formatowanie dat i liczb](06-dates-and-numbers.md)
- [07 · Przejmowanie pól, wartości stałe, opróżnianie i wartości domyślne](07-field-copy-and-defaults.md)
- [08 · Odbudowa wierszy tabeli](08-table-rows.md)
- [09 · Routing, kolejność, dane podstawowe i powtórzenia](09-routing-and-execution.md)

| Sekwencja | Treść | Konkretny punkt kontrolny |
| --- | --- | --- |
| 01 Podstawy | Cel, źródło, cztery zakresy, potok, warunki, podgląd, zapisanie | Odpowiedni przypadek, przypadek przeciwny, ponowne otwarcie zapisanej reguły |
| 02 Czyszczenie tekstu | Wszystkie cztery rodzaje wielkości liter, przycinanie, wszystkie tryby oczyszczania | Wewnętrzne odstępy, czysty ciąg zer, znaki o znaczeniu merytorycznym |
| 03 Numery | Wypełnienie, skrócenie, wszystkie cztery warianty afiksu | Zbyt długi numer, już istniejący prefiks, podwójne prefiksy |
| 04 Wzorce | Fragment, indeksy ujemne, wydobywanie/grupy, zamiana/liczba | Oddzielne źródło, brak dopasowania, wiele dopasowań |
| 05 Mapowanie | Pary, wielkość liter, zamiennik, zastosowanie na wiersz | `STK→PCE`, nieznany `BOX`, ponowne zastosowanie na `PCE` |
| 06 Formaty | Data, DATE vs. tekst, nieczytelna data, formaty liczb | Rzeczywista wartość serwerowa zamiast zakładanej reprezentacji przeglądarki |
| 07 Przejmowanie pól | Inne źródło, pusty cel, wartość stała, opróżnienie, wartość domyślna API | Chronić istniejący prawidłowy numer zamówienia; zero pozostaje zerem |
| 08 Tabele | Usuwanie, dodawanie, statyczne i dynamiczne wartości kolumn | Kolejność, powtórzenie, liczba wierszy i odniesienia PO |
| 09 Współdziałanie | Routing, fazy, lookup, wykonanie jednorazowe, protokoły | Wyczyszczone źródło nagłówka, pominięty warunek, drugie zapisanie |

## Warunki i źródła

Przy opcji „Zawsze" reguła obowiązuje bez ograniczenia merytorycznego dla typu dokumentu. „Tylko gdy…" ogranicza ją warunkami. Wartości nagłówka dostępne są w kontekście `header.*`, cechy dokumentu w `doc.*`; `row.*` dostępne jest tylko w kontekście wiersza reguły kolumnowej. Zagnieżdżone grupy I/LUB umożliwiają łączone kryteria. Dla poszczególnych operatorów obowiązuje oddzielna dokumentacja warunków reguły.

**Przykład przejmowania pola:** Cel `purchase_order`, źródło `header.invoice_id`, warunek `header.purchase_order` jest puste, kroki Przycięcie → Wielkie litery. `  po-4711  ` daje `PO-4711`. Już prawidłowo wypełniony numer zamówienia powinien pozostać niezmieniony. Nie opróżniać błędnego źródła: kopiowanie z przetwarzaniem nie przenosi źródła.

**Przykład numeru artykułu:** Tabela `INVOICE_TABLE`, kolumna `ITEM_NUMBER`, usuń prefiks `Art.-Nr. ` → zachowaj alfanumeryczne → wielkie litery. `Art.-Nr. ab-12/3` daje `AB123`. Odpowiednie tylko, gdy system docelowy oczekuje dokładnie tej formy.

**Przykład wiersza ogółem:** Dla wyraźnie określonego dostawcy najpierw `clear_rows`, potem `add_row`; `POSITION=001`, `QUANTITY=1`, `NET_AMOUNT` z kwoty netto nagłówka. Czy uzgodnienie zamówienia na kwotę ogółem jest merytorycznie prawidłowe, decyduje dodatkowa konfiguracja PO i oddzielny test uzgodnienia.

## Powtórzenie i wykonanie jednorazowe

Reguły mogą uruchamiać się wielokrotnie w przebiegach przetwarzania i przy zapisywaniu. Zawsze weryfikuj **cały potok**, nie tylko stabilność pojedynczego kroku.

* `substring`, `regex_extract` i `regex_replace` nie mogą w zweryfikowanej umowie serwerowej odczytywać własnej wartości docelowej. Wymagane jest oddzielne źródło; `run_once` nie uchyla tego wymogu.
* Uzupełnienie już istniejącego dokładnego afiksu jest stabilne. Usunięcie wielokrotnie występującego prefiksu może natomiast przy każdym przebiegu usuwać dalej.
* `A→B` i `B→C` w tym samym mapowaniu wartości przy dwóch przebiegach mogą z `A` ostatecznie uczynić `C`. Testuj wyjścia ponownie jako wejścia.
* `clear_rows → add_row` odbudowuje tabelę w ograniczonym zakresie. `add_row` bez wcześniejszego usunięcia wymaga odpowiedniego wykonania jednorazowego, w przeciwnym razie tabela rośnie przy każdym zapisaniu.
* „Tylko raz na dokument" oznacza faktycznie zastosowaną regułę. Niespełnione warunki nie zużywają zastosowania. Bez wiarygodnie odczytywalnego dowodu dokumentu/zastosowania wykonanie reguły jednorazowej zostaje odroczone.

## Po wyszukiwaniu i przed uzgodnieniem zamówienia

„Wykonaj również po wyszukiwaniu danych podstawowych" dodaje fazę po uzupełnieniu lookup i przed uzgodnieniem PO. Tylko odpowiednio oznaczone reguły uruchamiają się w tej fazie dodatkowej. Pozostałe przebiegi pozostają bez zmian. W połączeniu z wykonaniem jednorazowym reguła czeka przy pierwszym przebiegu ekstrakcji na późniejszą fazę; jeśli faza lookup nie nastąpi, wchodzi w grę późniejszy zwykły przebieg. Wskaźnik faz bieżącego edytora pokazuje te różnice.

## Solidny test odbiorczy

1. Określić cel merytoryczny, format systemu docelowego i zakres obowiązywania.
2. Przygotować odpowiednią wartość surową, przypadek przeciwny, pustą wartość i już przetworzony wynik.
3. Weryfikować warunki i wszystkie wartości pośrednie w podglądzie.
4. Wykonać test po stronie serwera na tym samym przykładzie; szczególnie porównać złożone wzorce i formaty liczb/dat.
5. Zapisać regułę i ponownie otworzyć. Aktywną regułę stosować tylko w przewidzianym zakresie testowym.
6. Przy izolowanym dokumencie zapisać, ponownie załadować i weryfikować wartość oraz wyświetlanie; przy tabelach również liczbę wierszy i wartości kolumn.
7. Zapisać jeszcze raz. Wynik nie może być niechcący dalej zmieniany ani zwielokrotniany.
8. Jeśli merytorycznie wymagane, dodatkowo weryfikować uzgodnienie PO i faktyczny odbiór w systemie docelowym. Sam protokół transformacji nie dowodzi tych wyników.

## Czego transformacja nie wykonuje automatycznie

Brak nowego rozpoznawania OCR, brak matematycznego przeliczenia jednostek lub walut, brak dowolnej agregacji tabel i brak pełnego księgowania ERP. Routing jest ograniczony do oferowanego atrybutu dokumentu. Dostępność i dokładne wyświetlanie zależą od używanej wersji, typu dokumentu i konfiguracji organizacyjnej.

## Przez cały dokument ćwiczeniowy

{% file src="../../../../../.gitbook/assets/transformation-training-invoice-pl-20261028.pdf" %}
Pobierz fakturę szkoleniową
{% endfile %}

Fikcyjny dokument zawiera dwie pozycje, różne zapisy jednostki i odniesienie do zamówienia w tekście swobodnym. Dla powtarzalnych testów reguł wartości wyjściowe są celowo przygotowane; nie jest to dowód automatycznie bezbłędnej ekstrakcji OCR.
