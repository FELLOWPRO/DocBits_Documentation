# Informacje o wersji DocBits — 14–23 lipca 2026

_Co zmieniło się w produkcyjnej aktualizacji DocBits z 23 lipca 2026
(aktualizacja kanału Nova), obejmującej wszystko od wydania z 14 lipca. Każda
usługa pokazuje wersję obecnie wdrożoną, a następnie opisuje nowości
i poprawki prostym językiem. Usługi niewymienione poniżej nie miały żadnych
zmian widocznych dla klientów._

---

## Najważniejsze zmiany

- **Zgłoszenia do wsparcia z ekranu błędu.** Gdy coś pójdzie nie tak, można
  teraz otworzyć zgłoszenie do wsparcia bezpośrednio z rekordu błędu.
  Zgłoszenie zawiera już kontekst techniczny, więc nie trzeba go opisywać.
- **Poczta przychodząca we właściwym regionie.** Organizacje z USA otrzymują
  adresy importu w swoim regionie, a skrzynki Microsoft 365 na tenantach
  chmur narodowych (GCC, 21Vianet i podobne) można teraz skonfigurować
  poprzez wybór Cloud Instance.
- **Czytelniejszy status dopasowania PO.** Faktury, których tabeli pozycji
  nie udało się zmapować, były dotąd oznaczane jako „nie znaleziono
  zamówienia”, co kierowało poszukiwania w złą stronę. Teraz otrzymują własny
  status „tabela niekompletna” wraz z informacją na poziomie kolumn, co
  dokładnie się nie zmapowało.
- **Mapowanie kodów podatkowych dla e-dokumentów.** Nowa strona ustawień
  mapuje kody podatkowe Państwa systemu ERP dla dokumentów elektronicznych,
  a eksport sprawdza mapowanie z wyprzedzeniem, zamiast kończyć się błędem
  dopiero w systemie ERP.
- **Zmiany skryptów chronione hasłem.** Skrypty niestandardowe mogą zmieniać
  sposób przetwarzania dokumentów, dlatego każda edycja skryptu wymaga teraz
  hasła zmieniającego się co godzinę. O aktualne hasło należy poprosić
  administratora.
- **Wycofanie modelu Turbo AI.** Model Turbo osiągnął koniec cyklu życia.
  Wszyscy, którzy mieli go wybranego, zostali automatycznie przeniesieni na
  Fast; nie trzeba nic robić.

---

## Web App — live: `10.45.1`

### Praca z dokumentami

- **Usunięte dokumenty:** otwarcie dokumentu, który został w międzyczasie
  usunięty, pokazuje czytelny komunikat zamiast błędów skryptu.
- **Walidacja pól:** pole numeru strony jest szersze i po naciśnięciu Enter
  przechodzi do wskazanej strony. Pole ustawione przez skrypt jako tylko do
  odczytu nadal pokazuje swoje powiązanie z polem.
- **Ekstrakcja tabel:** usunięcie kolumny zwalnia jej nazwę do ponownego
  użycia, a usunięte nagłówki nie pojawiają się ponownie w zapisanej tabeli.
- **Zatwierdzenia:** użytkownicy nie mogą już zatwierdzić kroku Sales Tax,
  do którego ich grupa nie ma uprawnień, a historia zatwierdzeń znów pokazuje
  wszystkie wpisy. Historia wskazuje też osobę, która faktycznie zatwierdziła
  dokument, łącznie z zatwierdzeniami wykonanymi przez administratora
  w imieniu osoby przypisanej.
- **Dostawcy:** strona Accounting nie pokazuje już fałszywego ostrzeżenia
  „Supplier is missing” (brak dostawcy), a usunięcie dostawcy istniejącego
  wyłącznie z ekstrakcji nie zawiesza już okna dialogowego.
- **Zadania i powiadomienia:** opcja usuwania jest ukryta przed użytkownikami
  bez uprawnień administratora.

### Pulpit i wyszukiwanie

- **Eksport:** eksport korzysta z faktycznie wybranego pulpitu, a aplikacja
  ostrzega przed eksportem pulpitu z niezapisanymi zmianami.
- **Wyszukiwanie:** Invoice Type jest dostępny jako pole wyszukiwania wraz
  ze swoją listą wartości.
- **Dziennik importu:** dokumenty powstałe z podziału można odnaleźć poprzez
  dokument nadrzędny, a kolumna Failed Filenames wymienia tylko pliki, które
  faktycznie zakończyły się błędem lub zostały pominięte.

### Logowanie

- **Usunięte konta:** logowanie na usunięte konto informuje o tym wprost,
  zamiast kończyć się ogólnym błędem.
- **SSO:** naprawiono błąd przy logowaniu z wybranym innym regionem.

### Ustawienia i administracja

- **Zgłoszenia do wsparcia:** zgłoszenie można utworzyć bezpośrednio
  z rekordu błędu. Zgłoszenia zawierają środowisko i kanał wydania,
  a przechwytywanie zrzutu ekranu już się nie zawiesza.
- **Workflow Builder:** nowo utworzone lub przemianowane karty, szablony
  e-mail i inne pozycje list rozwijanych pojawiają się natychmiast, bez
  przeładowania strony.
- **Typy dokumentów:** nowe ustawienie Structured Extraction w sekcji
  ekstrakcji.
- **Kody podatkowe E-Doc:** nowa strona ustawień do mapowania kodów
  podatkowych ERP dla dokumentów elektronicznych (zob. Najważniejsze
  zmiany).
- **Wybór modelu AI:** wycofany model Turbo zniknął z listy rozwijanej;
  istniejące wybory pokazują Fast.
- **Okno Service Versions:** można je teraz przewijać, obejmuje usługę Auth
  Bridge i pokazuje nazwy kanałów wydań Vesta i Nova.
- **Strona importu:** nie zawiesza się już dla organizacji z pustym wpisem
  subskrypcji.

### Drobniejsze poprawki

Puste powiadomienia toast są wyciszone, okno dialogowe nowego/edytowanego
pomysłu daje się przewijać, przesunięte pola wyboru w ustawieniach pól są
znów wyrównane, zablokowane usunięcia dokumentów wyjaśniają przyczynę,
a ustawienia E-Document poprawnie obsługują przełączenie z Default na Custom.

## API Service — live: `12.64.3`

- **Bezpieczeństwo skryptów:** zmiany skryptów wymagają hasła czasowego
  (zob. Najważniejsze zmiany).
- **Kody podatkowe E-Doc:** mapowanie kodów podatkowych ERP dla dokumentów
  elektronicznych, z centralną kontrolą przed eksportem, dzięki której
  brakujące kody wychodzą na jaw wcześnie.
- **Kontrola dostępu:** administratorzy mogą nadać użytkownikom bez
  uprawnień administratora wgląd w dokumenty niesklasyfikowane.
- **Pulpity osobiste:** naprawiono ustawienia udostępniania, które się nie
  zapisywały.
- **Wyszukiwanie na pulpicie:** Invoice Type dołącza do rozszerzonych pól
  wyszukiwania, a dokumenty utworzone przez podział po kodzie kreskowym lub
  QR można odnaleźć poprzez dokument nadrzędny.
- **Przesyłanie plików:** wielokrotne przesłanie tego samego pliku podczas
  ponawiania połączenia nie tworzy już zduplikowanych dokumentów.
- **Wyszukiwanie dostawcy:** wyniki pojawiają się, gdy tylko dane są gotowe,
  zamiast po sztywnym czasie oczekiwania.
- **Eksport Infor:** ceny jednostkowe zachowują cztery miejsca po przecinku.
  Eksporty M3 mogą zawierać pozycje kosztowe o zerowej kwocie, a ujemne
  pozycje kosztowe LN są przesyłane jako dodatnie uznania.
- **Zatwierdzenia:** zatwierdzenie jest wiązane z wnioskiem o zatwierdzenie
  tylko wtedy, gdy zatwierdzający jest osobą do niego przypisaną.
- **Stabilność logowania:** chwilowy błąd wewnątrz walidacji tokenu nie
  wylogowuje już użytkowników; aplikacja ponawia próbę.
- **Klasyfikacja:** reguły źródła dopasowują się teraz do każdego pola źródła
  dokumentu, a nie do stałych pozycji.
- **Stabilność walidacji:** pole bez nazwy nie powoduje już awarii walidacji
  dokumentu.
- **Modele AI:** wycofany model Turbo jest wszędzie mapowany na Fast, łącznie
  z wariantami dostrojonymi, z zabezpieczeniem gwarantującym, że wycofany
  model nigdy się nie uruchomi.

## Auth Service — live: `1.72.8`

- **Historia logowań:** logowania przez SSO/SAML pojawiają się teraz
  w historii logowań, a znacznik czasu ostatniego logowania jest zapisywany
  niezawodnie dla każdego typu logowania. Podgląd historii logowań innego
  użytkownika wymaga odpowiedniego poziomu uprawnień administratora.
- **Konta starszego typu:** usunięcie konta użytkownika starszego typu znów
  działa, zamiast po cichu nie przynosić żadnego efektu.
- **Masowa administracja użytkownikami:** istniejących użytkowników można
  dodawać do organizacji podrzędnych i grup zbiorczo przez CSV,
  z dopasowaniem po adresie e-mail. Naprawiono też awarię przy nierówno
  wypełnionych wierszach CSV oraz błąd serwera przy dodawaniu dwóch lub
  więcej nowych użytkowników naraz.
- **Listy członków:** usunięci użytkownicy nie pojawiają się już na listach
  członków organizacji podrzędnych.
- **Single sign-on:** seria poprawek wzmacniających. Wygasłe tokeny zwracają
  teraz jednoznaczną odpowiedź „wygasł”, organizacje bez konfiguracji SAML
  otrzymują poprawną odpowiedź „nie znaleziono” zamiast błędnego przebiegu
  logowania, wylogowanie zawsze dochodzi do skutku, nawet gdy żądania
  wylogowania nie da się zweryfikować, a kilka awarii związanych z brakującą
  konfiguracją dostawcy tożsamości zostało usuniętych.
- **Tokeny sesji:** naprawiono odrzucanie krótkotrwałych tokenów sesji jako
  nieważnych, mimo że nie wygasły.
- **Narzędzia zarządzania:** region organizacji jest widoczny w API
  zarządzania, użytkownika systemowego organizacji można zmienić,
  a administracja planami i zużyciem otrzymała dedykowane punkty końcowe.
  Te zmiany dotyczą narzędzi zespołu DocBits, nie aplikacji klienta.

## Email Service — live: `1.39.9`

- **Import we właściwym regionie:** domeny poczty przychodzącej istnieją per
  region, a wiadomości trafiające do niewłaściwego regionu są przekazywane do
  właściwego. Organizacje z USA nie zależą już od europejskiej ścieżki
  przychodzącej.
- **Microsoft 365:** tenanty chmur narodowych konfiguruje się poprzez wybór
  Cloud Instance, co naprawia importy O365 dla klientów z USA. Nieprawidłowy
  tenant zwraca teraz czytelny błąd logowania zamiast błędu serwera,
  a niekompletne dane uwierzytelniające tenanta kończą się natychmiast
  komunikatem, zamiast zawodzić po cichu.
- **Porządek w skrzynce:** e-maile bez załączników są przenoszone poza
  skrzynkę odbiorczą, zamiast się w niej gromadzić.
- **Brak duplikatów przy ponowieniu:** przesyłki do API dokumentów niosą
  klucz idempotencji, więc ponowione doręczenie nie może utworzyć tego samego
  dokumentu dwa razy.
- **Nazwy źródeł:** źródła O365 ze skonfigurowanym folderem zawierają
  w nazwie adres e-mail konta, dzięki czemu podobne źródła można od siebie
  odróżnić.
- **Porządkowanie dziennika importu:** wpisy dziennika importu są
  przechowywane przez 90 dni, a po tym czasie automatycznie usuwane.

## PO Match Service — live: `1.59.1`

- **Status „tabela niekompletna”:** faktury, których tabeli pozycji nie udało
  się zmapować, otrzymują własny status zamiast mylącego „nie znaleziono
  zamówienia” (zob. Najważniejsze zmiany). Pulpit pokazuje go ikoną braku
  dopasowania.
- **Lepsze szczegóły błędów:** niepowodzenia mapowania tabeli wskazują
  konkretną kolumnę, której nie udało się zmapować.
- **Czystsze zachowanie API:** żądania o nieistniejące reguły PO zwracają
  poprawną odpowiedź „nie znaleziono”, a uszkodzone wpisy pamięci podręcznej
  są usuwane, zamiast powodować powtarzające się błędy.
- **Dopasowanie po sumie:** naprawiono błąd w dopasowywaniu względem sumy
  zamówienia zakupu.

## Fulltext Service — live: `1.38.3`

- **Europejskie formaty liczb:** kwoty zapisane z przecinkiem dziesiętnym
  (`1.234,56`) są normalizowane przed indeksowaniem, więc wyszukiwanie
  i filtrowanie po kwotach działa niezależnie od formatu liczby.
- **Liczniki ERP:** naprawiono błąd tokenu, który mógł przerywać strumień
  liczników na żywo na pulpicie.
- **Odporność indeksowania:** indeksowanie przetrzymuje teraz chwilowe
  zakłócenia bazy danych i usługi uwierzytelniania (automatyczne ponawianie,
  przełączenie na bazę główną) i odrzuca zniekształcone komunikaty z kolejki,
  zamiast ponawiać je w nieskończoność.

## OCR Service — live: `1.9.9`

- **Duże dokumenty:** budżet czasowy OCR skaluje się z rozmiarem dokumentu,
  więc bardzo duże pliki nie kończą się już przekroczeniem limitu czasu.
- **Nietypowe znaki:** mechanizm czyszczący usuwa znaki, których silnik OCR
  nie potrafi odwzorować, co naprawia błędy na dokumentach z egzotycznymi
  symbolami.
- **Mniej chwilowych błędów:** przejściowe błędy połączenia z magazynem są
  ponawiane automatycznie.

## Extraction Service — live: `1.52.0`

- **Faktury z USA z zerowym podatkiem:** naprawiono przypadek, w którym
  poprawna para netto/podatek była odrzucana, gdy kwota podatku wynosi zero.
- **Ekstrakcja tabel:** tabele pozostają edytowalne, gdy skonfigurowane
  mapowanie oczekuje więcej kolumn, niż zawiera dokument, a awaria na
  nietypowych danych wierszy została naprawiona.
- **Modele AI:** wycofanie modelu Turbo, odzwierciedlone z API Service.

## Docflow Service — live: `2.7.2`

- **Dopasowanie PO w przepływach pracy:** brakujące wartości porównania są
  traktowane jako brak danych, a nie jako niezgodność.
- **Karty potwierdzeń zamówień:** kupujący i osoba odpowiedzialna są ustalani
  niezawodnie.
- **Koszty frachtu:** gdy żadna ze stron nie ma kosztów, przypadek jest
  rozstrzygany przez kartę operatora, zamiast utykać.
- **Bezpieczeństwo:** tokeny API przepływów pracy są weryfikowane względem
  organizacji, do której należą.
- **Szybsze wyzwalanie:** sprawdzanie aktywnych przepływów pracy korzysta
  z pamięci podręcznej, a procesy robocze w tle restartują się czysto,
  zamiast pozostawiać po sobie zawieszone procesy.

## Barcode Service — live: `1.17.4`

- **Długotrwałe podziały:** połączenie z kolejką zadań jest podtrzymywane
  podczas długich zadań kodów kreskowych, więc podział dużych partii nie
  utyka już pod koniec.

## FTP Service — live: `1.31.2`

- **Porządkowanie dziennika importu:** ta sama 90-dniowa retencja
  i automatyczne czyszczenie co w Email Service.

---

## Bez zmian w tym wydaniu

**Auth Bridge** (`0.3.6`), **Auto Accounting** (`1.20.1`), **Docnet**
(`1.55.1`), **Operator** (`1.40.2`) i **Ideas** (`0.3.1`) nie zawierają
zmian w tym okresie.

<!-- Generated by the docbits-changelog skill (version-boundary mode), then
     reconciled on 23 Jul 2026 against the Nova versions actually deployed
     (Web App 10.45.1, API 12.64.3, Auth 1.72.8, Email 1.39.9, PO Match
     1.59.1, OCR 1.9.9, Docflow 2.7.2, FTP 1.31.2). Manage Layouts and
     Custom Validation Rules were removed from this page: DOCB-13719 gated
     both behind a beta query parameter, so they are not generally available
     in 10.45.1. -->
