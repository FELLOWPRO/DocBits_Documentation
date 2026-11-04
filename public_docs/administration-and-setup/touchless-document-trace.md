# Touchless Intelligence: Ślad dokumentu

Wpisz identyfikator dokumentu w polu **Document ID** albo otwórz dokument przykładowy z klastra, aby zobaczyć, **co stało się z tym jednym dokumentem**.

Nagłówek pokazuje plik, jego status (na przykład **W toku**), przeglądane uruchomienie i jego pierwszą blokadę oraz przycisk **Dokument** z identyfikatorem dokumentu.

<figure><img src="../.gitbook/assets/touchless-nova-trace-overview-pl.png" alt="Dev NOVA: ścieżka procesu i wartości zapisane w pierwszym przebiegu testowym"><figcaption><p>Nowe nagranie ekranu z Dev NOVA 11.0.3, 4 listopada 2026 r. Fikcyjna faktura zatrzymuje się na walidacji pól. Klasyfikacja, wyszukiwanie dostawcy i odczyt nagłówka oraz tabeli zawierają rzeczywiście zapisane wartości. Karty pokazują dokument i historię przebiegów. To działający interfejs produktu. W tej wersji nazwy etapów na ścieżce pozostają angielskie. Podręcznik oznacza tutaj ręcznie wskazany typ dokumentu, a Scena w porównaniu oznacza etap procesu; są to błędy tłumaczenia interfejsu.</p></figcaption></figure>

**Ścieżka rurociągu** pokazuje 14 etapów: Intake, Classification, E-Document Validation, Supplier Identification, Text Recognition, Header Extraction, Table Extraction, Field Validation, PO Lookup, PO Line Match, Approval, Workflow Routing, Export, ERP Acknowledgement. Każdy etap ma jeden stan:

| Stan | Znaczenie |
| --- | --- |
| **Przeszedł** (zielony) | Etap przebiegł bez problemów |
| **Zatrzymany tutaj** (pomarańczowy) | Etap zablokował dokument |
| **Nie osiągnięto** | Etap za pierwszą blokadą na ścieżce; sprawdź dziennik pod kątem dodatkowych zapisanych wykonań |
| **Nic nie nagrano** (przerywany) | Dla tego etapu nie zapisano żadnych danych |
| **Nie dotyczy** | Etap nie ma zastosowania do tego dokumentu |

### Dziennik etapów

**Dziennik etapów** pod ścieżką wymienia te same etapy wraz z tym, co każdy z nich zapisał. Kropka statusu i słowo statusu znajdują się po lewej i prawej stronie każdego wiersza.

* Każda wartość to **żeton wartości**: liczba wraz z jednostką, na przykład **Pewność 100 %**, **Próg 60 %**, **Nieudane reguły 0**, **8 brakujących pól** lub **0 luk w mapowaniu**. Wartości procentowe pokazywane są jako `97 %`, nigdy jako `0.97`.
* **Szczegóły** otwierają pełną listę wartości zapisanych przez etap, łącznie z rozważanymi alternatywami.
* Etap, który zablokował dokument, podaje przyczynę, na przykład **Walidacja pola nie powiodła się**.
* Wartość, której żaden etap nie zapisał, pokazywana jest jako **Nie zarejestrowano**, nigdy jako wartość wymyślona. Wartości to liczby i ustalone terminy, nigdy tekst dokumentu.
* **Pokaż surową diagnostykę** włącza dane surowe, gdy poprosi o nie wsparcie.

<figure><img src="../.gitbook/assets/touchless-nova-trace-stage-log-pl.png" alt="Dev NOVA: dziennik z pewnością klasyfikacji, wynikami odczytu i zablokowaną walidacją"><figcaption><p>Rzeczywisty pierwszy przebieg: pewność klasyfikacji 100 %, 0 kandydatów na dostawcę, 1 wiersz i 7 luk w mapowaniu. Zaliczony etap potwierdza wykonanie, nie dopasowanie dostawcy ani poprawność wszystkich wartości. Walidacja zgłasza brak wymaganego pola.</p></figcaption></figure>

### Uruchomienia i zmiany

Wybierz próbę w selektorze; historia pokazuje wynik i pierwszą blokadę. Zapisane różnice porównują wybrany przebieg z jego poprzednikiem, a nie automatycznie z bieżącym przebiegiem. Każda różnica zawiera jednostkę; identyczne wartości pozostają bez zmian.

Karta Dokument zawiera typ, dostawcę, numer faktury, zamówienie, strony i zapisaną metodę analizy. Ręczna metoda oznacza tutaj typ podany podczas importu testowego. Wartość 100 % nie stanowi więc niezależnego dowodu dokładności automatycznej klasyfikacji.

### Jak czytać szczegóły dostawcy i tabeli

<figure><img src="../.gitbook/assets/touchless-nova-trace-supplier-pl.png" alt="Dev NOVA: znalezione identyfikatory, wyszukiwanie w danych podstawowych i przypisanie dostawcy"><figcaption><p>Nazwę znaleziono na fakturze i wyszukano w danych podstawowych, lecz nie przypisano dostawcy. Faktura testowa nie zawiera numeru VAT, IBAN, adresu e-mail ani GLN. Brak dopasowania w danych podstawowych różni się od nieznalezienia wartości na fakturze.</p></figcaption></figure>

Sprawdź osobno, czy identyfikator był na dokumencie, czy go wyszukano i czy przypisano dostawcę. Zielony etap sam w sobie nie odpowiada na te trzy pytania.

<figure><img src="../.gitbook/assets/touchless-nova-trace-table-pl.png" alt="Dev NOVA: szczegóły pierwszego przebiegu z siedmioma lukami w mapowaniu"><figcaption><p>Szczegóły pokazują 7 luk w mapowaniu dla 1 tabeli i 1 wiersza. Przed stwierdzeniem błędu odczytu sprawdź mapowanie kolumn. Stopka porównania nie jest prawidłową podstawą dla wybranego pierwszego przebiegu, który nie ma poprzednika. Nagłówek Państwo oznacza tutaj stan kolumny, nie kraj.</p></figcaption></figure>

### Jak rozpoznać rzeczywiste ponowne uruchomienie

<figure><img src="../.gitbook/assets/touchless-nova-trace-runs-pl.png" alt="Dev NOVA: porównanie dwóch rzeczywistych przebiegów z niezmienionymi wartościami etapów"><figcaption><p>Ta sama faktura po rzeczywistym ręcznym ponownym uruchomieniu, bez korekty pól. Nowy przebieg dowodzi kolejnej próby, nie poprawy. Identyczne wartości pozostają bez zmian; nie dodano wymyślonych różnic.</p></figcaption></figure>

Ręczne ponowne uruchomienie jest ingerencją człowieka. Ten przypadek zostanie zaliczony do AP Assisted dopiero po ewentualnym późniejszym pomyślnym zakończeniu. Dopóki przetwarzanie trwa, nie wchodzi do mianownika dokumentów zakończonych.

Granice dowodów. Ten przypadek nie potwierdza akceptacji biznesowej, udanego eksportu ani potwierdzenia ERP. Starszy mechanizm dopasowania zamówień nie udostępnia tu zapisanej ścieżki decyzji; nie dowodzi to porównania z Infor. W NOVA 11.0.3 dziennik może pokazać udane wyszukiwanie zamówienia po zablokowanej walidacji, podczas gdy ścieżka przedstawia je jako następny etap. Sprawdź obie prezentacje. Podsumowanie pokazuje też numer faktury jako niezapisany, mimo że jest w odczytanych danych; porównuj oryginał i odczytane pola.

## Oddziel odczyt od danych źródłowych

Porównaj oryginał i pola/pozycje sprzed korekt. Następnie porównaj importowane zamówienie z aktualnym Infor, jednostką, jednostką ceny i czasem importu. Brak dowodów pozostawia przyczynę otwartą.

**Przykład:** oryginał i odczyt mają 10 €, a importowane zamówienie 9 €. To rozbieżność z zamówieniem, nie udowodniony błąd odczytu. Potwierdź uzgodnioną cenę. Ręczny restart i późniejszy sukces oznaczają AP Assisted. Zobacz [obliczenia](touchless-metrics.md). Powtarzający się brak pola nie dowodzi brakującej wartości domyślnej; sprawdź oryginał, odczyt, walidację i konfigurację.

## Dowody pierwotnego odczytu i kolejnych blokad

Porównaj właściwy oryginał i wykonanie: zamówienie, walutę, ilości, jednostki, jednostki ceny, ceny i sumy. Oddziel wartości bieżące od wartości sprzed korekt. Zmiana wykonania nie gwarantuje odzyskania każdej dawnej komórki. Bez wartości początkowej wynik jest **nieocenialny**. Zdefiniuj zakres i wielkość próby. Porównaj import, jego datę i aktualne Infor.

Pierwsze wykonanie może czekać na zamówienie, a kolejne ujawnić różnicę ceny. Pierwsze nie dowodzi przejścia późniejszej kontroli. Ręczny restart pozostaje po sukcesie AP Assisted; ostateczny błąd ERP ma pierwszeństwo. Brak zapisu to brak dowodu.

Narzędzia i klasyfikację działań opisuje [Touchless przez MCP](touchless-mcp.md).

## Powiązane strony

* [Touchless Intelligence](touchless-intelligence.md)
* [Diagnoza dostawcy i klastry problemów](touchless-supplier-diagnosis.md)
* [Diagnoza dopasowania PO](touchless-po-matching-diagnosis.md)

Zrzuty ekranu na tej stronie pokazują interfejs w języku polskim.

<!-- Alignment 2026-11-04: correct extraction is distinct from process Touchless; KPI numerator and denominator verified. -->

<!-- Completion 2026-11-04: localized MCP examples, AP actions, original-value evidence and owned synthetic PO cards. -->

Pięć nowych obrazów pokazuje zlokalizowany interfejs Dev NOVA 11.0.3 i tę samą fakturę utworzoną na potrzeby dokumentacji. Ewentualny osobny obraz oryginału i pól ilustruje wyłącznie takie porównanie.
