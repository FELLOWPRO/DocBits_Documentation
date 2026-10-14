# Zasady transformacji

## Przegląd

Zasady transformacji automatycznie oczyszczają lub przepisują wyodrębnione dane — pole w nagłówku, kolumnę w tabeli, całe wiersze tabeli lub atrybut dokumentu — za każdym razem, gdy dokument jest przetwarzany i zapisywany. Zastępują małe skrypty, które wiele organizacji pisało dla „zawsze przytnij to pole”, „ustaw domyślnie tę kolumnę na 1”, „mapuj kody jednostek tego dostawcy” lub „zsumuj pozycje tego dostawcy do jednej linii łącznej”.

Reguła jest definiowana dla **typu dokumentu** i działa na każdym dokumencie tego typu. Reguły uruchamiają się **przed** walidacją, skryptami i dopasowaniem zamówienia, więc wszystko dalej widzi już przekształcone wartości.

## Jak uzyskać dostęp

1. Przejdź do **Ustawienia → Ustawienia globalne → Typy dokumentów**.
2. Otwórz typ dokumentu i wybierz **Zasady transformacji**. Lista pokazuje każdą regułę tego typu wraz z zakresem, celem, priorytetem i informacją, czy jest aktywna.
3. Kliknij **Nowa reguła**, aby otworzyć kreator reguł, lub otwórz istniejącą regułę, aby ją zmienić.

## Budowa reguły

| Część               | Co to jest                                                                                                                                                                                                                             |
| ------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Nazwa / klucz**   | Nazwa wyświetlana w listach, komunikatach i historii dopasowań oraz techniczny klucz, który pozostaje niezmienny po zmianie nazwy reguły.                                                                                              |
| **Zakres**          | Gdzie reguła zapisuje: **pole nagłówka**, **kolumna tabeli**, **tabela** (całe wiersze) lub **atrybut dokumentu**. Zobacz poniżej.                                                                                                     |
| **Cel**             | Pole, kolumna (razem z tabelą) lub tabela, do której reguła zapisuje.                                                                                                                                                                  |
| **Źródło**          | Opcjonalne. Skąd reguła pobiera dane wejściowe zamiast z samego celu: `header.<field>` dla pola nagłówka, `doc.<attribute>` dla atrybutu dokumentu, `row.<column>` dla innej kolumny tego samego wiersza (tylko zakres kolumny).       |
| **Kiedy**           | **Zawsze** lub **tylko gdy** warunek jest prawdziwy (zobacz Warunki).                                                                                                                                                                  |
| **Akcje**           | Lista transformacji, stosowanych kolejno; wynik jednej akcji jest wejściem dla następnej.                                                                                                                                              |
| **Priorytet**       | Reguły o tym samym zakresie uruchamiają się rosnąco według priorytetu (następnie według klucza). Używaj, gdy jedna reguła musi widzieć wynik innej.                                                                                    |
| **Uruchom raz**     | Reguła stosuje się do dokumentu **co najwyżej raz**. Potrzebne dla akcji, które zmieniałyby wartość przy każdym zapisie (substring, regex\_replace, regex\_extract) oraz dla reguł tabeli, które nie powinny ponownie budować wierszy. |
| **Loguj wykonanie** | Zapisuje jedną linię logu na zastosowanie — przydatne podczas dopracowywania nowej reguły.                                                                                                                                             |

### Zakresy

| Zakres                | Zapisuje do                                                 | Typowa reguła                                                                   |
| --------------------- | ----------------------------------------------------------- | ------------------------------------------------------------------------------- |
| **Pole nagłówka**     | jedno wyodrębnione pole nagłówka (numer faktury, waluta, …) | przytnij i zamień na wielkie litery numer faktury; zamapuj „EUR€” na „EUR”      |
| **Kolumna tabeli**    | jedną kolumnę w każdym wierszu tabeli                       | ustaw domyślnie `UNIT_PRICE_PER` na 1; usuń prefiks „Art.-Nr.” z numeru pozycji |
| **Tabela**            | wiersze tabeli                                              | wyczyść wiersze i dodaj jedną linię łączną dla dostawcy dopasowanego na sumę    |
| **Atrybut dokumentu** | atrybut samego dokumentu (obecnie podorganizacja)           | skieruj dokumenty dostawcy do podorganizacji                                    |

Reguły uruchamiają się kolejno według zakresu: nagłówek → dokument → tabela → kolumna. Reguła kolumny widzi więc już wiersze dodane przez regułę tabeli.

### Warunki („tylko gdy”)

Warunek porównuje wartość dokumentu z wartością stałą. Wartość pochodzi z pola nagłówka (`header.<field>`), atrybutu dokumentu (`doc.<attribute>`) lub, dla reguł kolumn, z kolumny bieżącego wiersza (`row.<column>`).

| Operator                                   | Znaczenie              |
| ------------------------------------------ | ---------------------- |
| is / is not                                | dokładne porównanie    |
| is one of / is not one of                  | wartość na liście      |
| contains, starts with, ends with           | porównanie tekstu      |
| is empty / is not empty                    | brak potrzeby wartości |
| greater than, less than, at least, at most | porównanie numeryczne  |
| matches                                    | wyrażenie regularne    |

Warunki można grupować za pomocą **all of** (i) oraz **any of** (lub) i negować przez **not**. Przykład: _tylko gdy `header.supplier_id` jest `20723`_ — reguła działa tylko dla jednego dostawcy.

### Akcje

Akcje dla pól nagłówka i kolumn tabeli (tworzą potok; wartość wchodzi na górze i wychodzi na dole):

| Akcja           | Efekt                                                                                                                  |
| --------------- | ---------------------------------------------------------------------------------------------------------------------- |
| `trim`          | usuń spacje (lub podane znaki) z lewej, prawej lub obu stron                                                           |
| `case`          | wielkie, małe, tytułowe lub kapitalizacja                                                                              |
| `pad`           | dopełnij do długości podanym znakiem, z lewej lub prawej                                                               |
| `truncate`      | obetnij do maksymalnej długości                                                                                        |
| `affix`         | dodaj prefiks lub sufiks albo usuń jeden                                                                               |
| `sanitize`      | zachowaj tylko klasę znaków (alfanumeryczne, alfabetyczne, numeryczne, alfanumeryczne + spacja) lub usuń zestaw znaków |
| `substring`     | pobierz część wartości według startu i długości lub końca                                                              |
| `regex_replace` | zamień to, co pasuje do wyrażenia regularnego                                                                          |
| `regex_extract` | zachowaj to, co wyrażenie regularne przechwytuje                                                                       |
| `value_map`     | mapuj wartości na inne wartości (opcjonalnie bez rozróżniania wielkości liter, z wartością domyślną)                   |
| `date_format`   | zmień format daty (wejście musi być datą ISO przechowywaną przez DocBits w `value`)                                    |
| `number_format` | zmień format liczby                                                                                                    |
| `default`       | ustaw wartość tylko, gdy pole jest puste                                                                               |
| `set_value`     | ustaw stałą wartość, niezależnie od zawartości pola                                                                    |
| `clear`         | wyczyść pole                                                                                                           |

Akcje dla zakresu **tabela** (działają na wierszach, nie na wartościach, i nie można ich mieszać z powyższymi):

| Akcja        | Efekt                                                                                                                                                               |
| ------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `clear_rows` | usuń wszystkie wiersze tabeli                                                                                                                                       |
| `add_row`    | dodaj jeden wiersz na końcu lub początku; każda kolumna otrzymuje wartość stałą lub wartość pobraną z nagłówka (`header.<field>`) lub dokumentu (`doc.<attribute>`) |

{% hint style="info" %}
`substring`, `regex_replace` i `regex_extract` zmieniają wartość ponownie, gdy działają na już przekształconej wartości. Połącz je z **Uruchom raz** lub napisz wyrażenie regularne tak, aby drugie uruchomienie nie miało nic do zmiany.
{% endhint %}

## Kiedy reguły działają

* Podczas przetwarzania, po ekstrakcji i przed walidacją, skryptami i dopasowaniem zamówienia.
* Przy **każdym zapisie** dokumentu, w którym zmieniły się wyodrębnione dane. Reguły bez **Uruchom raz** stosują się ponownie przy każdym zapisie; ponieważ każda akcja poza trzema powyższymi jest idempotentna, wartość już w docelowej formie pozostaje bez zmian.

## Zasady transformacji a dopasowanie zamówienia

Reguły tabeli i kolumn zmieniają to, co widzi dopasowujący zamówienia:

* Reguła tabeli, która **odbudowuje** wiersze (np. czyści wszystkie wiersze i dodaje jedną linię łączną), zachowuje istniejące dopasowanie zamówienia, o ile produkuje **te same wiersze ponownie** — wartości porównywane są znaczeniowo, więc `1.0` i `1.00` to ten sam wiersz. Wiersze zachowują swoją tożsamość, a dopasowanie przetrwa każdy zapis.
* Jeśli reguła **zastępuje lub usuwa wiersze, które były dopasowane**, dopasowanie nie może zostać zachowane. Dokument wtedy zapisuje, która reguła je usunęła, ekran Dopasowania Zamówienia pokazuje to jako powód („_Dopasowanie PO nie mogło zostać zapisane: reguła transformacji „…” odbudowała tabelę_”), a administratorzy otrzymują link do reguły. **Historia dopasowań** dokumentu pokazuje krok _Zasady transformacji_ przed pierwszym etapem dopasowania z uruchomionymi regułami.
* Liczba wierszy po regułach to to, co liczą [warunki aktywacji](https://github.com/Fellow-Consulting-AG/docbits/tree/pl/readme/administration-and-setup/settings/global-settings/document-types/more-settings/purchase-order/purchase-order-matching-rules.md#activation-conditions) reguł dopasowania. Reguła, która redukuje fakturę do **jednego** wiersza, ma sens tylko razem z regułą dopasowania na sumę, aktywną dla dokumentów z jednym wierszem (`[[count(table_lines)]] >= 1`).

## Przykłady

**Oczyść numer faktury** — pole nagłówka `invoice_id`, zawsze: `trim` → `case` upper.

**Domyślna podstawa ceny** — kolumna tabeli `UNIT_PRICE_PER` tabeli pozycji, zawsze: `default` `1`.

**Mapuj kody jednostek dostawcy** — kolumna tabeli `UNIT` tabeli pozycji, tylko gdy `header.supplier_id` jest `10040`: `value_map` `{ "STK": "PCE", "KG": "KGM" }`.

**Jedna linia łączna dla dostawcy dopasowanego na sumę** — zakres tabela na tabeli pozycji, tylko gdy `header.supplier_id` jest `20723`: `clear_rows`, potem `add_row` z `POSITION` = `001`, `UNIT_PRICE` = `1.0`, `QUANTITY` = `header.total_net_amount`, `NET_AMOUNT` = `header.total_net_amount`. Połącz z regułą dopasowania na sumę, której warunek aktywacji akceptuje dokument z jednym wierszem.

**Skieruj dostawcę do podorganizacji** — atrybut dokumentu `sub_org_id`, tylko gdy `header.supplier_id` jest jednym z `[…]`: `set_value` `<id podorganizacji>`.

## Rozwiązywanie problemów

| Objaw                                                       | Co sprawdzić                                                                                                                                                                                              |
| ----------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Reguła nic nie zmieniła                                     | Czy jest aktywna? Czy typ dokumentu się zgadza? Czy warunek jest prawdziwy dla tego dokumentu (porównaj dokładną wartość, łącznie ze spacjami)? Czy reguła z **Uruchom raz** nie została już zastosowana? |
| Wartość zmienia się ponownie przy każdym zapisie            | Potok zawiera `substring`, `regex_replace` lub `regex_extract`. Włącz **Uruchom raz** lub spraw, by wyrażenie było idempotentne.                                                                          |
| Dopasowanie zamówienia znika po zapisie                     | Reguła tabeli zastąpiła dopasowane wiersze. Powód w dokumencie wskazuje regułę; spraw, by reguła odtwarzała te same wiersze lub ustaw ją na **Uruchom raz**.                                              |
| Reguła dopasowania nigdy się nie uruchamia po transformacji | Reguła zmieniła liczbę wierszy; dostosuj warunek aktywacji reguły dopasowania.                                                                                                                            |
