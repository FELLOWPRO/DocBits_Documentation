# Ekran błędu odrzuconej e-faktury

> W tej wersji niektóre teksty interfejsu mogą nadal być po angielsku lub mieć błędne tłumaczenie. Instrukcja wyjaśnia ich znaczenie; zrzuty pokazują niezmieniony interfejs.

Gdy wgrasz błędną e-fakturę, DocBits jej nie gubi. Dokument dostaje status **Błąd**, a ekran błędu pokazuje, co jest nie tak, gdzie i co zrobić dalej. Ta strona pokazuje dwa przykłady: plik XML, który nie jest poprawnie sformułowany, oraz fakturę, która łamie regułę biznesową.

> Faktura dostaje status **Błąd** tylko wtedy, gdy walidacja jest **włączona** i **blokująca** dla jej typu dokumentu. Zobacz [Walidacja dla każdego typu dokumentu](validation-per-document-type.md).

## Przykład 1: plik XML jest uszkodzony

Dostawca wysyła plik XML, w którym znacznik zamykający nie pasuje do znacznika otwierającego. Pliku nie można odczytać, więc DocBits zatrzymuje się na pierwszej kontroli, **L1 · Poprawność składni XML**.

<figure><img src="../../../../.gitbook/assets/einvoice-error-xml-malformed-pl-20261104-v2.png" alt="Ekran błędu fikcyjnego pliku XML z celowo uszkodzonym znacznikiem zamykającym. W tej wersji niektóre teksty interfejsu mogą nadal być po angielsku lub mieć błędne tłumaczenie. Instrukcja wyjaśnia ich znaczenie; zrzuty pokazują niezmieniony interfejs."><figcaption><p>Ekran błędu fikcyjnego pliku XML z celowo uszkodzonym znacznikiem zamykającym. W tej wersji niektóre teksty interfejsu mogą nadal być po angielsku lub mieć błędne tłumaczenie. Instrukcja wyjaśnia ich znaczenie; zrzuty pokazują niezmieniony interfejs.</p></figcaption></figure>

Ekran ma dwie strony:

* **Po lewej: plik XML.** DocBits pokazuje plik z numerami linii. Linia z problemem jest zaznaczona na czerwono. Przyciskami nad plikiem skopiujesz XML lub otworzysz go w nowej karcie.
* **Po prawej: wyjaśnienie.** Karta **Odrzucony przez** wskazuje kontrolę, która zatrzymała plik (tutaj **L1 · Poprawność składni XML**), oraz kod reguły (tutaj `XML-PARSE`). Poniżej widzisz tytuł (*Plik XML ma niepoprawną składnię*), krótkie wyjaśnienie i blok **Następny krok**.

Wybierz **Wyświetl szczegóły walidacji**, aby otworzyć pełny [raport walidacyjny](validation-report.md).

<figure><img src="../../../../.gitbook/assets/einvoice-report-xml-malformed-pl-20261104-v2.png" alt="Raport uszkodzonego fikcyjnego pliku XML."><figcaption><p>Raport uszkodzonego fikcyjnego pliku XML.</p></figcaption></figure>

Raport podaje dokładną pozycję (wiersz i kolumna są podane w raporcie) i techniczny komunikat parsera XML. Wybierz **Pokaż w XML**, aby przejść do tej linii. Wskazówka **Jak naprawić** mówi, że należy poprosić nadawcę o poprawiony plik.

## Przykład 2: faktura łamie regułę biznesową

XML jest poprawny, ale brakuje wymaganego pola. Na przykład nie można zidentyfikować sprzedawcy, ponieważ brak identyfikatora sprzedawcy, identyfikatora rejestracyjnego lub identyfikatora VAT (reguła `BR-CO-26`).

<figure><img src="../../../../.gitbook/assets/einvoice-error-view-pl-20261104-v2.png" alt="Ekran błędu całkowicie fikcyjnej przykładowej faktury. W tej wersji niektóre teksty interfejsu mogą nadal być po angielsku lub mieć błędne tłumaczenie. Instrukcja wyjaśnia ich znaczenie; zrzuty pokazują niezmieniony interfejs."><figcaption><p>Ekran błędu całkowicie fikcyjnej przykładowej faktury. W tej wersji niektóre teksty interfejsu mogą nadal być po angielsku lub mieć błędne tłumaczenie. Instrukcja wyjaśnia ich znaczenie; zrzuty pokazują niezmieniony interfejs.</p></figcaption></figure>

Karta pokazuje pierwszy wynik blokujący. Pełny raport zawiera również kod `BR-CO-26` i pozostałe wyniki faktury.

## Przyciski pod kartą

| Przycisk | Co robi |
| --- | --- |
| **Ponowne uruchomienie przetwarzania** | Uruchamia przetwarzanie dokumentu ponownie, na przykład po zmianie ustawienia. Kontrola używa bieżących ustawień. |
| **Wyświetl DocFlow** | Pokazuje przepływ pracy dokumentu. |
| **Kopiuj szczegóły** | Kopiuje szczegóły błędu, na przykład do wiadomości dla administratora. |
| **Utwórz zgłoszenie do pomocy technicznej** | Otwiera zgłoszenie do wsparcia ze szczegółami błędu. |

Wybierz **Pokaż szczegóły techniczne** na karcie, aby zobaczyć surowe informacje techniczne.

## Co zrobić dalej

* **Błędy:** poproś nadawcę o poprawioną fakturę lub [odrzuć dokument](validation-next-step-and-reject.md). Poprawiona faktura to nowy dokument.
* **Tylko ostrzeżenia:** dokument nie jest blokowany. Możesz kontynuować.

## Powiązane strony

* [Raport walidacyjny](validation-report.md): wszystkie wyniki, poziom po poziomie.
* [Następny krok i odrzucenie dokumentu](validation-next-step-and-reject.md)
* [Walidacja dla każdego typu dokumentu](validation-per-document-type.md): włącz walidację i ustaw blokowanie.
