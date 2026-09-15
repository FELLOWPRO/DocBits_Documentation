# Kolumny tabeli

Kolumny tabeli określają, jakie kolumny ma tabela pozycji danego typu dokumentu: co DocBits wyodrębnia do każdej kolumny, co użytkownik widzi na ekranie walidacji i co jest wysyłane do systemu ERP podczas eksportu.

**Gdzie:** Ustawienia → Ustawienia globalne → Typy dokumentów → Kolumny tabeli

<figure><img src="../../../../.gitbook/assets/table-columns_list.png" alt="Lista kolumn tabeli z flagami Wymagana, Tylko do odczytu, Ukryta i Użyj AI dla każdej kolumny"><figcaption><p>Kolumny tabeli: jeden wiersz na kolumnę, flagi przełącza się bezpośrednio na liście</p></figcaption></figure>

## Co widzisz

Każdy wiersz to jedna kolumna jednej tabeli. Lista pokazuje:

| Kolumna | Znaczenie |
|---|---|
| **Nazwa kolumny** (*Column name*) | Nazwa techniczna, generowana z tytułu (wielkie litery, podkreślenia). Używana w skryptach, mapowaniach eksportu i API. Nie można jej później zmienić. |
| **Tytuł** (*Title*) | Etykieta wyświetlana na ekranie walidacji. Zmienia się ją ikoną tłumaczenia w kolumnie *Akcje* (*Update translation key*). |
| **Typ kolumny** (*Column Type*) | `AMOUNT`, `STRING`, `DATE`, `NUMBER`, `BOOLEAN` lub `CURRENCY`. Decyduje o walidacji i formatowaniu. |
| **Nazwa tabeli** (*Table name*) | Tabela, do której należy kolumna, na przykład `INVOICE_TABLE`. |
| **Wymagana** (*Is Required*) | Dokumentu nie można zatwierdzić, dopóki ta kolumna jest pusta w którymkolwiek wierszu. |
| **Tylko do odczytu** (*Read Only*) | Użytkownicy widzą wartość, ale nie mogą jej edytować. |
| **Ukryta** (*Hidden*) | Kolumna nie jest ani wyświetlana, ani eksportowana. Służy do wyłączania kolumn domyślnych, których nie potrzebujesz. |
| **Użyj AI** (*Use AI*) | Tę kolumnę wypełnia ekstrakcja tabeli AI, nawet jeśli dostawca ma wytrenowane reguły. |
| **Akcje** (*Actions*) | Ikona tłumaczenia: zmiana tytułu. Ikona informacji: skąd pochodzi wyświetlana etykieta (Twoje tłumaczenie, wartość domyślna, klucz). Menu z trzema kropkami: *Usuń*, tylko dla kolumn utworzonych przez Twoją organizację; kolumny domyślne można jedynie ukryć. |

Nad listą znajdują się dwa przyciski:

* **Utwórz nową tabelę** (*Create new table*): druga tabela pozycji dla typu dokumentu (na przykład tabela opłat obok tabeli pozycji).
* **Dodaj nową kolumnę tabeli** (*Add new table column*): otwiera okno dialogowe opisane w sekcji [Dodawanie nowej kolumny](#adding-a-new-column).

## Kolumny domyślne i kolumny własne

Każdy typ dokumentu ma zestaw kolumn domyślnych (dla faktur: numer pozycji, opis, ilość, cena jednostkowa, kwota całkowita, podatek, …). Należą one do DocBits, a nie do Twojej organizacji, dlatego nie można ich usunąć, można je jedynie ukryć. Kolumny dodane przez Ciebie należą do Twojej organizacji i można je usuwać.

{% hint style="info" %}
**Zmiany dotyczą tylko nowych dokumentów.** Kolumna, którą dodasz, ukryjesz lub usuniesz, pojawia się na dokumentach przesłanych lub uruchomionych ponownie po zmianie. Dokumenty znajdujące się już na pulpicie zachowują tabelę w takiej postaci, w jakiej została wyodrębniona. Uruchom dokument ponownie, aby zastosować nową konfigurację.
{% endhint %}

## Przeznaczenie i zastosowanie <a href="#purpose-and-use" id="purpose-and-use"></a>

Kolumna tabeli to jedno pole tabeli pozycji. Wszystko, co DocBits robi z tabelą (ekstrakcja, walidacja, dopasowanie PO, eksport), działa na kolumnach skonfigurowanych w tym miejscu.

### Gdzie kolumna jest widoczna

| Miejsce | Co kolumna tam robi |
|---|---|
| **Ekran walidacji** | Jedna kolumna w tabeli pozycji. *Tytuł* jest nagłówkiem, *Typ kolumny* decyduje o edytorze (kwota, data, tekst, tak/nie). Ukryte kolumny nie są wyświetlane. |
| **Szkolenie tabeli** | Podczas szkolenia tabeli dostawcy każdą wykrytą kolumnę tabeli mapujesz na jedną ze skonfigurowanych kolumn. Mapować można tylko skonfigurowane kolumny. |
| **Ekstrakcja tabeli AI** | AI wypełnia skonfigurowane kolumny. Kolumnę oznaczoną *Użyj AI* wypełnia AI nawet u dostawców z wytrenowanymi regułami. |
| **Reguły walidacji** | Kontrole pozycji, takie jak *ilość × cena jednostkowa = suma pozycji*, działają na kolumnach domyślnych `QUANTITY`, `UNIT_PRICE`, `TOTAL_AMOUNT`, `CHARGES`, `DISCOUNT`. |
| **Dopasowanie PO** | Wymaga kolumn domyślnych: numer pozycji, cena jednostkowa, ilość i kwota całkowita. Bez nich dokument pokazuje komunikat *Line Item Table is missing Mandatory column for PO*. |
| **Eksport** | Każda nieukryta kolumna jest częścią danych pozycji wysyłanych do systemu ERP. Mapowanie eksportu odwołuje się do *nazwy kolumny*. |
| **Skrypty** | Skrypty odczytują i zapisują kolumny po *nazwie kolumny*, na przykład `row["TOTAL_AMOUNT"]`. |

### Zakres

* Kolumny tabeli konfiguruje się **dla każdej tabeli**, a tabela należy do **typu dokumentu**. Kolumny faktur nie wpływają na dokumenty dostawy.
* Konfiguracja obowiązuje **dla całej organizacji**. Suborganizacje ją dziedziczą.
* O tym, które kolumny są *wypełniane* u danego dostawcy, decyduje szkolenie tego dostawcy lub AI; konfiguracja kolumn określa tylko, jakie kolumny istnieją.

### Typowe powody zmiany konfiguracji

* Dla każdej pozycji trzeba przechwycić wartość specyficzną dla klienta (centrum kosztów, numer projektu, wewnętrzny numer artykułu) → dodaj kolumnę.
* Kolumna domyślna nigdy nie jest używana i zaśmieca ekran walidacji → ukryj ją.
* Kolumna musi być zawsze wypełniona przed eksportem → oznacz ją jako *Wymagana*.
* Wartość pochodzi z wyszukiwania w ERP i użytkownicy nie mogą jej edytować → oznacz ją jako *Tylko do odczytu*.
* AI przechwytuje kolumnę lepiej niż wytrenowane reguły (na przykład opisy tekstowe) → oznacz ją jako *Użyj AI*.

## Dodawanie nowej kolumny <a href="#adding-a-new-column" id="adding-a-new-column"></a>

Dodaj kolumnę, gdy dla każdej pozycji trzeba przechwycić wartość, której nie obejmują kolumny domyślne: centrum kosztów, numer projektu, wewnętrzny numer artykułu.

### Zanim zaczniesz

* Zdecyduj, do której **tabeli** ma należeć kolumna. Większość typów dokumentów ma jedną tabelę (na przykład `INVOICE_TABLE`). Jeśli lista jest pusta, najpierw kliknij **Utwórz nową tabelę**; okno dialogowe pyta tylko o nazwę tabeli.
* Zdecyduj o **typie**: `AMOUNT` dla kwot pieniężnych, `NUMBER` dla ilości, `DATE`, `BOOLEAN` dla tak/nie, `CURRENCY` dla kodu waluty ISO, `STRING` dla wszystkiego innego. Typu nie można zmienić po zapisaniu.
* Sprawdź, czy nie istnieje już **kolumna domyślna** o tym samym znaczeniu, która jest ukryta. Ukryte kolumny są na liście z ustawioną flagą *Ukryta*; odkryj ją zamiast tworzyć duplikat.

### Kroki

1. Otwórz **Ustawienia → Ustawienia globalne → Typy dokumentów → Kolumny tabeli**.
2. Kliknij **Dodaj nową kolumnę tabeli**.

<figure><img src="../../../../.gitbook/assets/table-columns_add-dialog.png" alt="Okno dialogowe Dodaj nową kolumnę tabeli z polami Tytuł, Czy kolumna jest wymagana, Wybierz typ kolumny i Wybierz tabelę"><figcaption><p>Dodaj nową kolumnę tabeli</p></figcaption></figure>

3. Wypełnij okno dialogowe:

| Pole | Co wpisać |
|---|---|
| **Tytuł** (*Title*) | Etykieta, którą użytkownik widzi na ekranie walidacji, na przykład `Cost Centre`. Tylko litery i cyfry. DocBits tworzy z niej techniczną *nazwę kolumny* (`COST_CENTRE`). |
| **Czy kolumna jest wymagana?** (*Is column required?*) | Zaznacz, gdy dokumentu nie wolno zatwierdzić, dopóki kolumna jest pusta w którymkolwiek wierszu. |
| **Wybierz typ kolumny** (*Select column type*) | Patrz lista typów powyżej. |
| **Wybierz tabelę** (*Select Table*) | Tabela, która otrzyma kolumnę. |

4. Kliknij **Kontynuuj** (*Proceed*). Kolumna pojawia się na liście z wyłączonymi flagami *Tylko do odczytu*, *Ukryta* i *Użyj AI*. W razie potrzeby przełącz te flagi na liście, patrz [Edytowanie i usuwanie kolumn](#editing-and-deleting-columns).

### Po dodaniu

* Kolumna jest **pusta na istniejących dokumentach**. Wypełniana jest na dokumentach przesłanych lub uruchomionych ponownie po zmianie.
* U dostawców z **wytrenowanymi regułami** otwórz jeden z ich dokumentów w szkoleniu tabeli i zmapuj nową kolumnę, w przeciwnym razie kolumna pozostanie pusta dla tego dostawcy. Patrz [Definiowanie tabel i kolumn](../../../setup/document-training/training-line-fields-table-training/defining-tables-and-columns.md).
* Przy **ekstrakcji tabeli AI** AI wypełnia kolumnę, jeśli wartość jest rozpoznawalna na dokumencie. Oznacz kolumnę jako *Użyj AI*, jeśli dostawca ma wytrenowane reguły, ale ta kolumna ma mimo to pochodzić z AI.
* Dodaj kolumnę do **mapowania eksportu**, jeśli system ERP ma ją otrzymywać, patrz [Eksport](../../document-processing/export.md).

### Komunikaty

| Komunikat | Znaczenie |
|---|---|
| *Column name already exists* | Kolumna o tej nazwie technicznej już istnieje w tabeli. Wybierz inny tytuł. |
| *Column name already exists – Please activate it in Table Column settings* | Ukryta kolumna domyślna ma tę nazwę. Wyłącz jej flagę *Ukryta* zamiast tworzyć nową kolumnę. |
| *No table exists. Please create table before creating columns.* | Typ dokumentu nie ma jeszcze tabeli: najpierw kliknij **Utwórz nową tabelę**. |

## Edytowanie i usuwanie kolumn <a href="#editing-and-deleting-columns" id="editing-and-deleting-columns"></a>

Wszystko poza tytułem zmienia się bezpośrednio na liście; nie ma osobnego okna edycji.

**Gdzie:** Ustawienia → Ustawienia globalne → Typy dokumentów → Kolumny tabeli

### Przełączanie flagi

Zaznacz lub odznacz pole wyboru w wierszu. Zmiana jest zapisywana natychmiast (*Successfully saved*).

| Flaga | Włączona | Wyłączona |
|---|---|---|
| **Wymagana** (*Is Required*) | Zatwierdzenie jest zablokowane, dopóki kolumna jest pusta w którymkolwiek wierszu; ekran walidacji oznacza komórkę. | Puste komórki są dozwolone. |
| **Tylko do odczytu** (*Read Only*) | Wartość jest wyświetlana, ale nie można jej nadpisać. Używaj dla wartości pochodzących z wyszukiwania lub skryptu. | Użytkownicy mogą edytować komórkę. |
| **Ukryta** (*Hidden*) | Kolumna znika z ekranu walidacji i z eksportu. Jej dane są zachowywane. | Kolumna jest wyświetlana i eksportowana. |
| **Użyj AI** (*Use AI*) | Tę kolumnę wypełnia ekstrakcja tabeli AI, także u dostawców z wytrenowanymi regułami. | Kolumnę wypełniają wytrenowane reguły, a gdy reguł nie ma, AI. |

{% hint style="info" %}
Flagi działają na dokumentach przesłanych lub uruchomionych ponownie **po** zmianie. Otwarte dokumenty zachowują bieżącą tabelę do czasu ponownego uruchomienia.
{% endhint %}

### Zmiana tytułu

Kliknij ikonę tłumaczenia w kolumnie *Akcje* (*Update translation key*), wpisz nową etykietę i potwierdź. Ikona informacji obok pokazuje, która etykieta aktualnie obowiązuje i skąd pochodzi. Zmienia się tylko etykieta; techniczna *nazwa kolumny* pozostaje bez zmian, dzięki czemu skrypty, mapowania eksportu i wytrenowane reguły nadal działają.

### Zmiana typu lub tabeli

Niemożliwa. Ukryj kolumnę (lub usuń ją, jeśli jest Twoja własna) i dodaj nową z właściwym typem.

### Usuwanie kolumny

Akcja usuwania jest dostępna tylko dla kolumn utworzonych przez Twoją organizację. Kolumn domyślnych nie można usunąć, można je ukryć.

1. Otwórz menu z trzema kropkami w kolumnie *Akcje* i wybierz **Usuń**. Dla kolumn domyślnych ta pozycja nie występuje.
2. Potwierdź.

Co się dzieje:

* Kolumna zostaje usunięta z konfiguracji. Dokumenty przetwarzane **od tej chwili** już jej nie mają.
* Dokumenty już wyodrębnione zachowują kolumnę i jej wartości do czasu ponownego uruchomienia.
* Wytrenowane reguły, które mapowały tę kolumnę, nadal działają dla pozostałych kolumn; mapowanie usuniętej kolumny jest ignorowane.
* Jeśli kolumna jest używana w mapowaniu eksportu lub w skrypcie, usuń to odwołanie; w przeciwnym razie eksport lub skrypt zakończy się błędem brakującej kolumny.

### Cofanie usunięcia

Usuniętej kolumny nie można przywrócić z listy. Dodaj ją ponownie z tym samym tytułem: nazwa techniczna jest tworzona z tytułu, więc kolumna utworzona z tym samym tytułem otrzymuje tę samą *nazwę kolumny* i istniejące mapowania znów pasują.

## Najlepsze praktyki <a href="#best-practices" id="best-practices"></a>

### Zachowaj kolumny domyślne dla kwot i ilości

Kontrole pozycji (*ilość × cena jednostkowa = suma pozycji*) oraz dopasowanie PO szukają kolumn domyślnych `QUANTITY`, `UNIT_PRICE`, `TOTAL_AMOUNT`, `ITEM_NUMBER`. Jeśli zamiast nich utworzysz własne kolumny dla tych wartości, kontrole nie zadziałają, a dopasowanie PO zgłosi brak kolumn obowiązkowych. Zmień *tytuł*, jeśli nazwa Ci nie odpowiada; kolumnę zachowaj.

### Ukrywaj, nie usuwaj

Niepotrzebne kolumny domyślne ukrywa się, a nie usuwa; i tak nie da się ich usunąć. W przypadku własnych kolumn ukrycie jest również bezpieczniejszym wyborem, dopóki nie masz pewności, czy skrypt lub mapowanie eksportu nadal się do kolumny odwołuje.

### Oznaczaj jako wymagane tylko to, co blokuje eksport

Każda wymagana kolumna musi być wypełniona w każdym wierszu, zanim użytkownik będzie mógł zatwierdzić dokument. Używaj tej flagi dla wartości, które system ERP odrzuca, gdy ich brakuje (na przykład centrum kosztów w eksporcie księgowym), a nie dla wartości jedynie przydatnych.

### Używaj *Tylko do odczytu* dla wartości wyszukiwanych

Wartości, które skrypt lub wyszukiwanie danych podstawowych zapisuje do tabeli (opis artykułu z indeksu materiałowego, kod podatkowy dostawcy), powinny być tylko do odczytu, aby użytkownicy poprawiali źródło, a nie kopię.

### Używaj AI dla pojedynczych kolumn, nie dla całego dostawcy

U dostawcy z wytrenowanymi regułami większość kolumn wychodzi z reguł poprawnie. Jeśli jedna kolumna jest niewiarygodna (długie opisy zawijane do kolejnych wierszy, rabat, który czasem znajduje się w innym miejscu), ustaw *Użyj AI* tylko dla tej kolumny. Reguły obsługują resztę.

### Nazywaj kolumny pod kątem ERP, nie dokumentu

*Nazwa kolumny* trafia do mapowań eksportu i skryptów. `COST_CENTRE` łatwiej zmapować niż `KST` i nie zmienia się, gdy dostawca drukuje tę wartość inaczej.

### Testuj na ponownie uruchomionym dokumencie

Po zmianie uruchom ponownie jeden istniejący dokument danego typu i otwórz go: nowa kolumna jest widoczna, ukryta zniknęła, wymagane komórki są oznaczone. Dopiero wtedy udostępnij zmianę użytkownikom.

### Jedna tabela na strukturę pozycji

Drugą tabelę twórz tylko wtedy, gdy typ dokumentu rzeczywiście ma dwie niezależne tabele (na przykład pozycje i osobną tabelę opłat). Dodatkowe puste tabele pojawiają się na każdym dokumencie danego typu.

## Rozwiązywanie problemów <a href="#troubleshooting" id="troubleshooting"></a>

### Nowa kolumna nie pojawia się na ekranie walidacji

* Dokument został przetworzony przed dodaniem kolumny. Zmiany dotyczą dokumentów przesłanych lub uruchomionych ponownie później, **uruchom dokument ponownie** (Pulpit → menu dokumentu → Uruchom ponownie).
* Kolumna jest **ukryta**. Sprawdź flagę na liście Kolumny tabeli.
* Kolumna została dodana do **innej tabeli** niż wyświetlana. Ekran walidacji pokazuje tabele danego typu dokumentu; porównaj kolumnę *Nazwa tabeli*.
* Dokument nie jest tego typu, który skonfigurowano.

### Kolumna jest, ale zawsze pusta

* Dostawca ma **wytrenowane reguły**, a nowa kolumna nie jest w nich zmapowana. Otwórz jeden z dokumentów dostawcy w szkoleniu tabeli i zmapuj kolumnę albo ustaw dla niej *Użyj AI*.
* Przy ekstrakcji AI wartość nie jest rozpoznawalna na dokumencie (brak nagłówka, skrót, inny język). Dodaj [tag tabeli AI](../../../../end-user-and-partner-section/end-user-section/ai-table/ai-table-tags.md), który nazywa kolumnę, albo zmapuj ją w szkoleniu.

### "Column name already exists"

Kolumna o tej samej nazwie technicznej już istnieje w tabeli. Jeśli nie ma jej na liście, jest to ukryta kolumna domyślna: komunikat brzmi wtedy *Please activate it in Table Column settings*. Wyłącz flagę *Ukryta* tej kolumny zamiast tworzyć nową.

### Zatwierdzenie jest blokowane przez wymaganą kolumnę

Komunikat na tabeli wskazuje kolumnę. Wypełnij komórkę w każdym wierszu albo (jeśli wartość nie występuje na tym dokumencie) odznacz *Wymagana* dla kolumny, uruchom dokument ponownie i spróbuj jeszcze raz. Zastanów się, czy kolumna w ogóle powinna być wymagana (patrz [Najlepsze praktyki](#best-practices)).

### AI wypełnia kolumnę niewłaściwą wartością

Typowy przypadek: `CHARGES` otrzymuje sumę pozycji, a wtedy każdy wiersz nie przechodzi kontroli sumy pozycji z komunikatem *Line total does not match quantity x unit price (expected …, got …)*, ponieważ opłaty są częścią wzoru `ilość × cena jednostkowa + opłaty`.

* Odznacz *Użyj AI* dla kolumny, jeśli wytrenowane reguły przechwytują ją poprawnie.
* Jeśli dostawca nie ma reguł, wytrenuj tabelę raz (Szkolenie tabeli), aby kolumna została powiązana z właściwą pozycją, albo ukryj kolumnę, jeśli dostawca nigdy nie drukuje tej wartości.
* W ostateczności opcja *Pomiń walidację tabeli* w Więcej ustawień typu dokumentu wyłącza wszystkie kontrole tabeli dla całego typu dokumentu; niezgodność nie jest wtedy wykrywana, podobnie jak puste wymagane kolumny.

### Dopasowanie PO: "Line Item Table is missing Mandatory column"

Dopasowanie PO wymaga kolumn domyślnych: numer pozycji, cena jednostkowa, ilość i kwota całkowita. Jedna z nich jest ukryta lub została zastąpiona kolumną własną. Odkryj kolumnę domyślną albo zmapuj wartość na nią w szkoleniu tabeli.

### Skrypt lub eksport kończy się błędem po usunięciu kolumny

Skrypt lub mapowanie eksportu nadal odwołuje się do usuniętej *nazwy kolumny*. Usuń odwołanie albo dodaj kolumnę ponownie z tym samym tytułem; nazwa techniczna jest tworzona z tytułu i znów będzie pasować.

### Gdzie szukać dalej

* [Rozwiązywanie problemów z ekstrakcją tabeli](../../../../overview-and-basics/faq/document-processing/table-extraction-troubleshoot.md): jakość ekstrakcji, OCR, E-Text
* [Szkolenie pól linii / Szkolenie tabeli](../../../setup/document-training/training-line-fields-table-training/README.md): naucz DocBits, gdzie znajduje się tabela dostawcy
* [Tabela AI](../../../../end-user-and-partner-section/end-user-section/ai-table/README.md): co użytkownik widzi na ekranie walidacji
