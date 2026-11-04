# Structured Output dla tabel

Structured Output określa kolumny, które AI ma zwrócić, za pomocą schematu utworzonego z konfiguracji. Ogranicza to dowolne nazwy wymagające późniejszego mapowania. **Użyj ekstrakcji strukturalnej (AI)** steruje strukturą wyniku; model i Vision określają model oraz jego dane wejściowe.

## Dlaczego wynik strukturalny często działa lepiej

| Przykład | Bez stałego schematu | Korzyść ze Structured Output |
| --- | --- | --- |
| Zmienne nagłówki | „Art.-Nr.”, „SKU” i „Item Code” mogą dawać różne klucze. | Żądany klucz `ITEM_NUMBER` pozostaje taki sam dla różnych układów i ułatwia mapowanie. |
| Dwa numery artykułu | Wewnętrzny numer `00127` może zostać pomylony z numerem dostawcy `V-884`. | `ITEM_NUMBER` i `SUPPLIER_ITEM_NUMBER` są oddzielnymi celami. Nadal sprawdzaj wartości: schemat narzuca nazwy, a nie rozumienie treści. |
| Własna kolumna projektu | Wydrukowany kod może zostać pominięty lub zwrócony pod inną nazwą. | `PROJECT_CODE` z wyborem **Tak** jest żądany jawnie. Brakujące dane nadal muszą być traktowane jako brakujące. |

Pomaga też typ: kolumny `AMOUNT` mają w schemacie postać liczby lub `null`, z opisem znaczenia. Ułatwia to np. odróżnienie dzielnika ceny od jednostki miary. Inne typy nie stają się automatycznie ściśle typowanymi wartościami JSON. Zachowuj zera wiodące w identyfikatorach.

Nie ma gwarancji lepszej dokładności, krótszego czasu ani niższych kosztów. Nadal możliwe są błędne wartości i brakujące wiersze. Porównuj te same dokumenty przy tym samym modelu, Vision i treningu.

## 1. Wymagania i ustawienie organizacji

Otwórz [Klasyfikację i ekstrakcję](../../../administration-and-setup/settings/document-processing/classification-and-extraction/README.md), **Ogólne → Ekstrakcja**. Ustawienia organizacji wymagają odpowiednich uprawnień administratora i zapisują się natychmiast.

1. Właściwy typ dokumentu musi mieć tabelę i potrzebne [kolumny](../../../administration-and-setup/settings/global-settings/document-types/table-columns/README.md).
2. Włącz wymagane ścieżki. Ścieżka PDF z regułami i awaryjnym użyciem AI wymaga **Table Extraction** oraz **AI Table Extraction**. Sam Structured Output nie uruchamia ekstrakcji tabel przez AI.
3. Ustaw **Użyj ekstrakcji strukturalnej (AI)** jako wartość organizacji. Techniczny klucz to `USE_STRUCTURED_EXTRACTION`.
4. Sprawdź czytelny tekst lub wejście Vision. Zapisane klasyczne reguły mogą nadal określać faktyczną ścieżkę; sprawdź [użytą ścieżkę ekstrakcji](../../../overview-and-basics/faq/document-processing/which-extraction-path-was-used.md).

<figure><img src="../../../.gitbook/assets/structured-output-settings-pl-20261104.png" alt="Aktualne ustawienia ekstrakcji. Structured Output jest wyłączony w tej istniejącej konfiguracji, dlatego podgląd schematu nie jest widoczny. Nie zmieniono ustawień ekstrakcji."><figcaption><p>Aktualne ustawienia ekstrakcji. Structured Output jest wyłączony w tej istniejącej konfiguracji, dlatego podgląd schematu nie jest widoczny. Nie zmieniono ustawień ekstrakcji.</p></figcaption></figure>

## 2. Pierwszeństwo ustawień szablonu

Zakres to organizacja i bieżący szablon ekstrakcji, a nie wszystkie szablony dostawcy.

| Sytuacja | Faktyczne działanie |
| --- | --- |
| Szablon jawnie włączony | Używa Structured Output nawet przy wyłączonej wartości organizacji. |
| Szablon jawnie wyłączony | Nie używa go nawet przy włączonej wartości organizacji. |
| Brak nadpisania w szablonie | Obowiązuje właściwe ustawienie organizacji i jego wartości domyślne. |

Na ekranie walidacji odpowiedniego dokumentu otwórz **Więcej opcji** (trzy kropki). Jeśli istnieje kontekst szablonu, administrator może zmienić **Użyj ekstrakcji strukturalnej (AI)**. Potwierdzenie zapisuje nadpisanie i uruchamia dokument ponownie; Anuluj odrzuca zmianę. Inne szablony dostawcy i dokumenty historyczne nie są automatycznie zmieniane.

**Nowe szablony dostawców:** bez zapisanej reguły formatowania tabeli i bez własnej wartości Structured Output przetwarzanie może włączyć tę funkcję automatycznie i zapisać ją w szablonie, nawet gdy organizacja ma ją wyłączoną. Steruje tym `STRUCTURED_EXTRACTION_FOR_NEW_SUPPLIERS` (domyślnie włączone); opisany ekran nie ma dodatkowego przełącznika tej opcji. Istniejący jawny wybór zostaje zachowany.

Lista [Model AI](../../../administration-and-setup/settings/document-processing/classification-and-extraction/ai-model.md) pokazuje wartości szablonów; jej przełączniki Structured Output są wskaźnikami. Zmian dokonuj w menu dokumentu. **Usuń wpis** może usunąć jednocześnie nadpisania modelu, E-Text i innych opcji. Nie jest to selektywne wyłączenie Structured Output. Automatyczne włączenie może nastąpić ponownie, jeśli szablon znów zostanie uznany za nowy.

## 3. Use AI: Domyślne, Tak lub Nie

Otwórz [Kolumny tabeli](../../../administration-and-setup/settings/global-settings/document-types/table-columns/README.md) dla właściwego typu dokumentu i tabeli. **Użyj sztucznej inteligencji (Use AI)** jest listą trzech stanów, a nie polem wyboru. Zmiana zapisuje się natychmiast.

| Aktualna opcja | Wpływ na schemat bazowy |
| --- | --- |
| **Domyślne · żądane** lub **Domyślne · nie zażądano** | Przyjmuje ustawienie DocBits dla tego typu i nazwy kolumny. Domyślne nie oznacza zawsze włączone ani zawsze wyłączone. |
| **Tak · poproszono** | Jawnie żąda skonfigurowanej kolumny od AI. |
| **Nie · nie poproszono** | Wyklucza ją ze schematu bazowego, nawet jeśli normalnie jest żądana. |

Powrót do **Domyślne** usuwa jawny wybór. Nowa własna kolumna zwykle nie należy do domyślnego zestawu AI: wybierz **Tak**, aby AI ją zwracała. Domyślny zestaw AI nie oznacza wszystkich kolumn dostarczonych z DocBits. Sprawdź wskazany efekt i podgląd.

**Wymagana**, **Tylko do odczytu** i **Ukryta** sterują kompletnością, edycją i widocznością; nie zastępują wyboru AI. **Nie** nie usuwa kolumny ani jej wartości i nie blokuje reguł, skryptów lub innych źródeł danych. Trening dostawcy i dodatkowe tagi AI mogą rozszerzyć faktyczne żądanie: rozwiąż sprzeczności także tam. Przełącznik nie zastępuje automatycznie wyniku pochodzącego wyłącznie z reguł.

<figure><img src="../../../.gitbook/assets/structured-output-column-choice-pl-20261104.png" alt="Aktualna lista Use AI z opcjami Domyślne, Tak i Nie. Nie zmieniono żadnej opcji. Komórki tytułów ukryto w celu ochrony danych."><figcaption><p>Aktualna lista Use AI z opcjami Domyślne, Tak i Nie. Nie zmieniono żadnej opcji. Komórki tytułów ukryto w celu ochrony danych.</p></figcaption></figure>

## 4. Odczytywanie podglądu

Po włączeniu przełącznika organizacji poniżej pojawia się **O co prosi sztuczna inteligencja**. Wybierz fakturę, potwierdzenie zamówienia, dokument dostawy, zamówienie klienta lub ofertę. Linki edycji otwierają odpowiednie ustawienia pól i kolumn. Podgląd nie wykonuje ekstrakcji.

* **Żądane:** pola nagłówka i kolumny schematu bazowego; wskaźnik wartości domyślnej oznacza odziedziczoną selekcję AI.
* **Nieżądane:** skonfigurowane kolumny poza bieżącym zestawem.
* **Wyłączone wartości domyślne:** jawnie wykluczone pola i kolumny, które normalnie byłyby żądane.
* **Strict i licznik:** schemat bazowy jest ścisły do aktualnego limitu DocBits wynoszącego **100 właściwości**. Liczą się żądane pola nagłówka, kontener tabeli i różne żądane kolumny pozycji, nie liczba wierszy. Powyżej limitu schemat jest wskazówką bez ścisłego wymuszenia.

Podgląd nie obejmuje treningu i tagów dostawcy. Dodatkowe instrukcje mogą zezwalać na otwarty wynik przed nauczeniem mapowań; wyuczone kolumny źródłowe mogą ponownie umożliwić wynik zamknięty. „Strict” nie dowodzi więc trybu każdego wykonania. Jeśli włączony jest tylko szablon, podgląd organizacji może być niedostępny: nie zmieniaj wartości globalnej tylko po to, aby go zobaczyć.

Bez użytecznej konfiguracji pól nagłówka nie powstanie pełny schemat. Sam włączony przełącznik nie potwierdza jego użycia. Sprawdź wykonanie przez **Wyjaśnij ekstrakcję** i dostępne logi; [Tabela AI](README.md) opisuje te widoki i uprawnienia.

## 5. Przykład: faktura z dwoma numerami i projektem

To syntetyczny przykład oczekiwanego wyniku do sprawdzenia, a nie wykonana ekstrakcja.

| Artykuł | Artykuł dostawcy | Ilość | Cena jednostkowa | Kwota pozycji | Projekt |
| --- | --- | --- | --- | --- | --- |
| `00127` | `V-884` | 2 | 12,50 | 25,00 | `PRJ-42` |
| `00208` | `V-990` | 1 | 7,00 | 7,00 | `PRJ-42` |

1. Wybierz **Faktura** i sprawdź wybór AI dla `ITEM_NUMBER`, `SUPPLIER_ITEM_NUMBER`, `QUANTITY`, `UNIT_PRICE` i `TOTAL_AMOUNT`.
2. W tej samej tabeli utwórz kolumnę tekstową z dosłownym tytułem `Project Code`, który daje nazwę techniczną `PROJECT_CODE`. Wybierz **Tak · poproszono**. Używaj **Nie · nie poproszono** świadomie; wymagana kolumna musi zachować źródło.
3. Sprawdź organizację i bieżący szablon. W podglądzie faktury, jeśli dostępny, `PROJECT_CODE` musi być żądany. Przy Domyślne ta własna kolumna zwykle nie byłaby żądana.
4. Prześlij ponownie zatwierdzony dokument testowy lub uruchom go ponownie. Zmiana nie przekształca już wyodrębnionych tabel wstecznie. Sprawdź też zapisane mapowania i instrukcje.
5. Oczekuj dwóch wierszy: `ITEM_NUMBER` = `00127`/`00208`, `SUPPLIER_ITEM_NUMBER` = `V-884`/`V-990`, a `PROJECT_CODE` = `PRJ-42` w obu. Sprawdź zera wiodące, ilości, ceny i kwoty; 25,00 + 7,00 = 32,00 netto. Poprawna suma nie dowodzi poprawności każdej wartości.
6. Powtórz z nagłówkiem „SKU” i dokumentem bez projektu. Kolumny docelowe powinny pozostać stałe, bez wymyślonych danych. Jeśli numery zostaną zamienione, dodaj i przetestuj jednoznaczne mapowanie lub instrukcję, a potem sprawdź obie kolumny.

Korzyścią jest stała żądana struktura dla różnych układów. Osobno sprawdzaj poprawność danych, pola wymagane, dopasowanie zamówień i eksport.

## 6. Typowe problemy

| Obserwacja | Co sprawdzić |
| --- | --- |
| Brak własnej kolumny | Właściwy typ i tabela, wybór Tak, podgląd, wartość szablonu i tagi; ponów ekstrakcję. |
| Pusta kolumna domyślna | Jawny wybór Nie? Jeśli żądana, lecz nieobecna na dokumencie, traktuj wartość jako brakującą. |
| Zachowanie inne niż ustawienie globalne | Nadpisanie szablonu, automatyczne włączenie i faktyczna ścieżka. |
| Inne lub dodatkowe kolumny | Wyuczone mapowania, tagi, wynik otwarty i limit faktycznego wykonania. |
| Stare dokumenty bez zmian | Przetwórz ponownie; wcześniej sprawdź wpływ na poprawki ręczne. |

Dalej: [Edycja kolumn](../../../administration-and-setup/settings/global-settings/document-types/table-columns/editing-and-deleting-columns.md), [Tagi i instrukcje](ai-table-tags.md), [Model AI i wartości szablonu](../../../administration-and-setup/settings/document-processing/classification-and-extraction/ai-model.md).
