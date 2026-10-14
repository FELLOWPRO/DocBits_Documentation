# Zasady Dopasowywania Zamówień Zakupu

## Wprowadzenie: Zamówienia Zakupu i Zarządzanie Zasadami PO

Dopasowywanie Zamówień Zakupu (PO) to kluczowy proces zapewniający spójność między Zamówieniami Zakupu (PO) a odpowiadającymi im przychodzącymi fakturami lub przyjęciami towarów. Solidny zestaw zasad jest niezbędny, aby osiągnąć wysoki wskaźnik automatycznego dopasowania, zapobiegać oszustwom i zapewnić prawidłowe płatności.

Ta strona konfiguracji służy do definiowania i zarządzania zasadami, które określają _jak_ pozycje zamówienia PO są dopasowywane do odpowiadającego dokumentu przychodzącego (Faktura, Potwierdzenie Zamówienia).

{% hint style="info" %}
**Wymaganie wstępne:** zasady dopasowywania są używane tylko wtedy, gdy **dopasowywanie PO po stronie serwera** jest włączone dla typu dokumentu (Ustawienia → Typy Dokumentów → Więcej Ustawień → Zamówienie Zakupu). Przy wyłączonym przełączniku DocBits dopasowuje za pomocą wbudowanego mechanizmu (ilość, cena jednostkowa, numer pozycji, numer zamówienia) i ignoruje zestaw zasad.
{% endhint %}

***

## Jak uzyskać dostęp

1.  Przejdź do **Ustawienia --> Ustawienia globalne --> Typy dokumentów**

    <figure><img src="../../../../../../.gitbook/assets/image (31).png" alt=""><figcaption></figcaption></figure>


2.  Wybierz żądany typ dokumentu i kliknij **Więcej ustawień**.

    <figure><img src="../../../../../../.gitbook/assets/image (40).png" alt=""><figcaption></figcaption></figure>


3.  Następnie przejdź do sekcji Zamówienie Zakupu i kliknij przycisk (dopasowywanie PO po stronie serwera), a następnie kliknij Konfiguruj zasady dopasowywania PO

    <figure><img src="../../../../../../.gitbook/assets/image (168).png" alt=""><figcaption></figcaption></figure>

***

<figure><img src="../../../../../../.gitbook/assets/Bildschirmfoto 2025-12-09 um 07.43.15.png" alt=""><figcaption></figcaption></figure>

## Ustawienia globalne (Zasady bazowe)

Te ustawienia ustanawiają ramy, które mają zastosowanie do wszystkich zasad dopasowywania:

* **Ustawienie:** Dopasuj ilość według
  * **Cel:** Określa, która ilość z pozycji zamówienia jest porównywana z linią dokumentu — na przykład zamówiona ilość lub **otwarta ilość na fakturze** (zamówiona minus już zafakturowana), co jest zwykłym wyborem dla faktur.
  * **Dopuszczalne wartości:** Ilość lub inne dostępne pola ilości w systemie, w zależności od struktury danych (np. alternatywne pole ilości znormalizowanej).
  * **Zależność:** Określa podstawę dla wszystkich zasad dopasowywania, które uwzględniają ilość w kryteriach porównania.
* **Ustawienie:** Standardowa tolerancja (domyślna tolerancja)
  * **Cel:** Określa, jak bardzo wartość numeryczna w dokumencie może się różnić od wartości zamówienia i nadal być uznana za dopasowanie. Kompensuje różnice zaokrągleń. Dotyczy **każdej kolumny numerycznej** z włączoną opcją "Zezwól na tolerancję" — zarówno ilości, jak i ceny jednostkowej.
  * **Dopuszczalna wartość:** Liczba dziesiętna. Czy jest odczytywana jako **wartość bezwzględna** (0.005 = odchylenie do 0.005 w porównywanej ilości lub cenie) czy jako **procent** (0.5 = 0,5 % wartości porównywanej) jest ustawiane przez **typ tolerancji** zestawu zasad (`value` lub `percent`; nowe zestawy używają `value`). Tolerancje dla poszczególnych pozycji (zobacz [Ustawienia tolerancji](purchase-order-tolerance-settings-additional-purchase-order-tolerance.md)) nadpisują standardową tolerancję dla tej pozycji.
  * **Zależność:** Dotyczy zasad używających pól numerycznych do dopasowania i mających włączoną opcję "Zezwól na tolerancję".

***

## Lista zasad

Lista zasad wyświetla wszystkie dostępne zasady dopasowywania i zarządza ich kolejnością wykonywania.

#### Struktura i wykonanie

* **Priorytet:** To pole liczbowe (np. 1, 2, 3) określa kolejność wykonywania zasad. Zasady o niższym numerze priorytetu są próbowane jako pierwsze. Pozwala to administratorom na stworzenie hierarchii, zwykle zaczynając od najbardziej specyficznych i rygorystycznych zasad (np. dopasowanie według numeru linii i numeru części) i przechodząc do szerszych lub mniej restrykcyjnych zasad.
* **Nazwa i opis:** Zapewnia jasną identyfikację i kontekst zasady, wyjaśniając główne kryteria użyte (np. "Standardowa zasada nr 1: Dopasowanie według numeru linii, ID części i ilości").
* **Aktywna:** Prosty przełącznik umożliwiający natychmiastowe włączenie lub wyłączenie zasady bez konieczności usuwania jej konfiguracji.

**Przebieg wykonania:** System wykonuje dopasowywanie w sekwencji kaskadowej. Jeśli zasada (np. priorytet 1) pomyślnie dopasuje pozycję, proces dla tej pozycji się zatrzymuje. Jeśli nie znaleziono dopasowania, system przechodzi do następnej zasady w kolejności priorytetu (np. priorytet 2). Każde uruchomienie jest rejestrowane w dokumencie; **historia dopasowań** na ekranie Dopasowywania Zamówień Zakupu pokazuje, która zasada była próbowana, która dopasowała oraz które zostały pominięte i dlaczego.

***

## Konfiguracja zasady (Ustawienia szczegółowe)

Ten szczegółowy obszar konfiguracji definiuje konkretną logikę i kryteria dla pojedynczej zasady.

#### Parametry bazowe

* **Typ zasady:** Określa krotność dopasowania.

| Typ zasady          | Co robi                                                                                                                                                                                             | Typowe zastosowanie                                                             |
| ------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------- |
| **Pojedyncze dopasowanie** | Jedna pozycja zamówienia do jednej linii dokumentu. Każda skonfigurowana kolumna musi się zgadzać (w granicach tolerancji tam, gdzie jest dozwolone).                                             | Standardowy przypadek.                                                           |
| **Wielokrotne dopasowanie** | Kilka pozycji zamówienia do jednej linii dokumentu lub kilka linii dokumentu do jednej pozycji zamówienia. Ilości są **sumowane**, cena jednostkowa porównywana jako **średnia**, pozostałe kolumny muszą się zgadzać. | Dostawy podzielone, jedna linia faktury obejmująca kilka linii zamówienia.       |
| **Dopasowanie do sumy** | Porównuje jedną **kwotę** — zwykle netto linii dokumentu z **sumą** zamówienia — i dopasowuje całe zamówienie naraz.                                                                              | Dostawcy fakturujący ryczałtowo, faktury usługowe, faktury jednolinijkowe.      |

* **Automatyczne dopasowanie:** Jeśli włączone, system spróbuje zastosować tę zasadę całkowicie automatycznie. Wymagana jest wysoka pewność kryteriów do automatycznego przetwarzania.
* **Ręczne dopasowanie:** Jeśli włączone, zasada może być prezentowana lub stosowana przez użytkownika podczas ręcznego etapu uzgadniania, oferując mu predefiniowany zestaw kryteriów porównania do rozwiązania wyjątków.
* **Zapasowa:** Zasada oznaczona jako zapasowa działa w późniejszej fazie, tylko dla par linii, które pozostają niedopasowane po wykonaniu wszystkich zwykłych zasad. Używaj jej dla "luźniejszej" zasady, która ma złapać to, co przegapiły zasady rygorystyczne.

#### Warunki aktywacji

Zasada może mieć **warunki aktywacji** — wyrażenia, które muszą być prawdziwe, zanim zasada zostanie w ogóle uruchomiona. Jeśli warunek jest fałszywy, zasada jest **pomijana dla tego dokumentu** (historia dopasowań pokazuje ją jako "nie uruchomioną" z podanym powodem). Wyrażenia używają liczby linii, które są dopasowywane:

| Wyrażenie                | Znaczenie                                                         |
| ------------------------ | ----------------------------------------------------------------- |
| `[[count(po_lines)]]`    | liczba linii zamówienia dostępnych do dopasowania                 |
| `[[count(table_lines)]]` | liczba pozycji w dokumencie, które są mapowane do dopasowania     |

Porównuj je za pomocą `==`, `!=`, `>`, `>=`, `<`, `<=` i łącz kilka warunków za pomocą `&` (i). Przykłady:

* `([[count(po_lines)]] > 1) & ([[count(table_lines)]] > 1)` — tylko dla dokumentów z wieloma liniami po obu stronach (typowe dla zasady wielokrotnego dopasowania).
* `([[count(po_lines)]] == 1) & ([[count(table_lines)]] == 1)` — tylko dla dokumentów jednolinijkowych przeciwko jednolinijkowemu zamówieniu.
* `([[count(po_lines)]] >= 1) & ([[count(table_lines)]] >= 1)` — zawsze, gdy jest cokolwiek do dopasowania.

{% hint style="warning" %}
Warunki aktywacji są najczęstszym powodem, dla którego zasada "nic nie robi". Zasada dopasowania do sumy z warunkiem `[[count(table_lines)]] > 1` nigdy nie uruchamia się dla faktury jednolinijkowej — a [zasada transformacji](../../transformation-rules.md), która redukuje fakturę do jednej linii sumarycznej, generuje dokładnie taki dokument. Sprawdź liczby w historii dopasowań przed zmianą samej zasady.
{% endhint %}

#### Porównanie kolumn (Kryteria dopasowania)

To jest podstawowa definicja logiki zasady, określająca, które pola muszą się zgadzać między dokumentami.

1. Definiowanie kolumn do porównania:
   * **Kolumny PO:** Pole pobierane z danych Zamówienia Zakupu (np. numer linii).
   * **Wyodrębnione kolumny tabeli:** Odpowiadające pole wyodrębnione lub sparsowane z dokumentu przychodzącego (Faktura/Potwierdzenie Zamówienia) (np. `POSITION`).
2. **Typ porównania:** Określa charakter wymaganego dopasowania (np. Tt dla porównania tekstowego/stringowego, wymagającego dokładnego dopasowania znak po znaku; # dla porównania numerycznego).
3. **Zezwól na tolerancję:** Dla pól numerycznych (ilość, cena) włączenie tej opcji nakazuje systemowi zastosować wcześniej zdefiniowaną globalną standardową tolerancję. Jeśli ta opcja _nie_ jest włączona dla pola numerycznego, wartości muszą się dokładnie zgadzać.
4. **Ignoruj w ręcznym dopasowaniu:** Jeśli zaznaczone, to kryterium jest łagodniejsze podczas ręcznej interwencji. Przydatne dla pól takich jak opisy lub odniesienia wewnętrzne, które mogą się nieznacznie różnić, pozwalając użytkownikowi na pominięcie drobnych, niekrytycznych rozbieżności.

**Które kolumny można porównywać**

| Kolumna                         | Strona dokumentu                         | Strona zamówienia                       | Uwagi                                                                                                                                                                                                                          |
| ------------------------------- | --------------------------------------- | ------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| Numer linii                    | `POSITION`                              | `line_number`                         | Tekst, dokładne. Przydatne tylko, gdy dostawca drukuje numery linii zamówienia na dokumencie.                                                                                                                                  |
| Identyfikator pozycji          | `ITEM_IDENTIFIER`                       | `item_identifier`                     | Tekst, dokładne. Numer pozycji lub numer pozycji dostawcy, także przez [Mapę numerów pozycji dostawcy](supplier-item-number-map-admin-documentation.md).                                                                     |
| Efektywna znormalizowana ilość | `QUANTITY_EFFECTIVE_NORMALIZED`         | `quantity_effective_normalized`       | Numeryczne. Ilość wybrana przez **Dopasuj ilość według**, przeliczona na tę samą jednostkę po obu stronach (konwersja kodu jednostki, ilości „na”).                                                                          |
| Efektywna znormalizowana cena jednostkowa | `UNIT_PRICE_EFFECTIVE_NORMALIZED`       | `unit_price_effective_normalized`     | Numeryczne. Cena jednostkowa za pojedynczą jednostkę po rabatach i po **Cena jednostkowa za** — oraz, jeśli jest włączone [Obliczanie ceny jednostkowej PO](calculate-po-unit-price.md), cena wyliczona z kwoty i ilości linii zamówienia. |
| Kwota netto                   | `NET_AMOUNT`                            | `total_amount`                        | Numeryczne. Używane przez zasady dopasowania do sumy.                                                                                                                                                                         |

**Przykład: Rygorystyczna zasada dopasowania PO (`DefaultRule#1`)**

Typowa rygorystyczna zasada łączy obowiązkowe kontrole tożsamości z kontrolami wartości:

* **Obowiązkowa tożsamość:** Numer linii i identyfikator pozycji muszą się dokładnie zgadzać (porównanie tekstowe, bez tolerancji).
* **Kontrole wartości:** Efektywna znormalizowana ilość i efektywna znormalizowana cena jednostkowa muszą się zgadzać (porównanie numeryczne, tolerancja dozwolona). Dopiero jeśli wszystkie cztery kryteria są spełnione (z tolerancją dla wartości), wykonywane jest automatyczne dopasowanie.

***

## Domyślny zestaw zasad

Każda organizacja zaczyna z tym samym domyślnym zestawem zasad. Jest to dobre odniesienie przy tworzeniu własnego:

| Zasada                     | Typ / priorytet                 | Porównywane kolumny                                                      | Warunek aktywacji                                      |
| -------------------------- | ------------------------------ | ----------------------------------------------------------------------- | ----------------------------------------------------- |
| `DefaultRule#1`            | pojedyncze dopasowanie, priorytet 1 | numer linii, identyfikator pozycji, ilość (tolerancja), cena jednostkowa (tolerancja) | zawsze                                                |
| `DefaultMultiMatchRules#1` | wielokrotne dopasowanie, priorytet 1, zapasowa | identyfikator pozycji, ilość (tolerancja), cena jednostkowa (tolerancja) | `count(po_lines) > 1` i `count(table_lines) > 1`      |
| `DefaultTotalMatchRules#1` | dopasowanie do sumy, priorytet 1  | kwota netto ↔ suma zamówienia (bez tolerancji)                          | `count(po_lines) >= 1` i `count(table_lines) > 1`     |
| `DefaultRule#2`            | pojedyncze dopasowanie, priorytet 2, zapasowa | identyfikator pozycji, ilość (tolerancja), cena jednostkowa (tolerancja) | zawsze                                                |
| `DefaultRule#3`            | pojedyncze dopasowanie, priorytet 2, zapasowa | ilość (tolerancja), cena jednostkowa (tolerancja)                      | `count(po_lines) == 1` i `count(table_lines) == 1`    |

Czytając od góry: najpierw zasada rygorystyczna (numer linii i pozycja muszą być wydrukowane na dokumencie), potem zapasowe bez numeru linii, na końcu ostateczność dla dokumentów jednolinijkowych porównująca tylko ilość i cenę.

***

## Wpływ na proces dopasowywania PO

Zdefiniowany zestaw zasad bezpośrednio wpływa na efektywność i integralność procesu dopasowywania PO:

* **Priorytety i zapasowe:** Określony priorytet zapewnia, że system najpierw próbuje najbardziej wiarygodnej metody dopasowania. Jeśli rygorystyczne zasady o wysokim priorytecie zawiodą, system przechodzi do szerszych zasad, dążąc do minimalizacji liczby wyjątków kierowanych do użytkowników.
* **Kontrola jakości dopasowania:** Bardziej rygorystyczne zasady (wymagające dokładniejszych dopasowań i mniejszej tolerancji) skutkują mniejszą, ale bardzo wiarygodną liczbą automatycznych dopasowań. Luźniejsze zasady zwiększają wskaźnik automatycznego dopasowania, ale podnoszą ryzyko fałszywych trafień.
* **Obsługa wyjątków (ręczne dopasowanie):** Włączając zasady do ręcznego dopasowania, system oferuje użytkownikom ustrukturyzowane opcje. Jeśli transakcja nie spełnia kryteriów automatycznego dopasowania, staje się wyjątkiem. Użytkownik może wtedy spróbować rozwiązać wyjątek, stosując predefiniowaną zasadę ręczną, która może mieć złagodzone kryteria (np. ignorowanie drobnej rozbieżności tekstowej zgodnie z ustawieniem "Ignoruj w ręcznym dopasowaniu").

## Co jeszcze wpływa na wynik

* **Kiedy uruchamiane jest dopasowanie:** podczas przetwarzania dokumentu, gdy użytkownik kliknie **Auto PO Match**, oraz **przy każdym zapisie**, w którym numer zamówienia został zmieniony lub nigdy wcześniej nie był wyszukiwany (np. gdy dane podstawowe wypełniły go po przetwarzaniu). Zapis nigdy nie nadpisuje istniejącego dopasowania.
* **[Zasady transformacji](../../transformation-rules.md)** uruchamiane są przed dopasowaniem i mogą zmieniać pozycje linii — a wraz z nimi liczby linii, które sprawdzają warunki aktywacji. Zasada tabeli, która przebudowuje linie, zachowuje istniejące dopasowanie, o ile linie pozostają takie same; jeśli zastępuje dopasowane linie, dopasowanie jest usuwane, a nazwa zasady jest podawana jako powód.
* **[Obliczanie ceny jednostkowej PO](calculate-po-unit-price.md)** zmienia, którą cenę jednostkową zasady porównują po stronie zamówienia.
* **[Ustawienia tolerancji](purchase-order-tolerance-settings-additional-purchase-order-tolerance.md)** oraz **[wyłączone statusy](purchase-order-disable-statuses.md)** decydują o rygorze porównania i które linie zamówienia są w ogóle oferowane.

## Rozwiązywanie problemów

| Objaw                                                           | Co sprawdzić                                                                                                                                                                                      |
| ----------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| "Brak dopasowania", chociaż wszystkie wartości się zgadzają      | Otwórz historię dopasowań: która zasada działała, na której kolumnie zawiodła (odchylenie jest pokazane dla każdej kolumny), czy zasada została pominięta przez warunek aktywacji?                 |
| Cena jednostkowa niedopasowana dokładnie o stawkę podatku         | Suma zamówienia zawiera podatek; włącz [Obliczanie ceny jednostkowej PO](calculate-po-unit-price.md) (najpierw kwota netto) lub porównaj kwotę netto linii.                                         |
| Zasada dopasowania do sumy nigdy się nie uruchamia                | Jej warunek aktywacji wymaga więcej niż jednej linii dokumentu. Ustaw `[[count(table_lines)]] >= 1` lub nie redukuj linii za pomocą zasady transformacji.                                         |
| Zestaw zasad nie ma żadnego efektu                                | **Dopasowywanie PO po stronie serwera** jest wyłączone dla typu dokumentu lub zmieniony zestaw zasad jest nadal wersją roboczą — aktywuj wersję.                                                  |

***

## Dostosowywanie zasad dopasowywania PO

Aby edytować zasady dopasowywania PO, domyślną wersję można sklonować, klikając **"Konfiguruj wersjonowanie"** i używając opcji **"Klonuj jako wersję roboczą"** z dostępnych opcji karty.

<figure><img src="../../../../../../.gitbook/assets/image (197).png" alt=""><figcaption></figcaption></figure>