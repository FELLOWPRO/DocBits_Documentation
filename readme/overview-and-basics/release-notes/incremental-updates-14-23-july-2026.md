# Informacje o wersji DocBits — 14–23 lipca 2026

_Co zmieniło się w produkcyjnej aktualizacji DocBits z 23 lipca 2026
(aktualizacja kanału Nova), obejmującej wszystko od wydania z 14 lipca. Każda
usługa pokazuje wersję obecnie wdrożoną, a następnie opisuje nowości
i poprawki prostym językiem. Usługi niewymienione poniżej nie miały żadnych
zmian widocznych dla klientów._

---

## Najważniejsze zmiany

- **Manage Layouts i reguły walidacji trafiają do aplikacji.** Silniki reguł
  wprowadzone po stronie serwera w poprzednim wydaniu mają teraz pełny
  interfejs użytkownika. Można zarządzać układami dokumentów bezpośrednio,
  definiować własne reguły walidacji i pozwolić, by to reguły dobierały
  właściwy układ — a nie źródło dokumentu. Obie funkcje pozostają wyłączone,
  dopóki nie włączą Państwo opcji **Custom Validation Rules** na typie
  dokumentu, więc do tego momentu nic się nie zmienia.
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
- **Zmiany skryptów chronione hasłem.** Skrypty niestandardowe mogą zmieniać
  sposób przetwarzania dokumentów, dlatego każda edycja skryptu wymaga teraz
  hasła zmieniającego się co godzinę. O aktualne hasło należy poprosić
  administratora.
- **Wycofanie modelu Turbo AI.** Model Turbo osiągnął koniec cyklu życia.
  Wszyscy, którzy mieli go wybranego, zostali automatycznie przeniesieni na
  Fast; nie trzeba nic robić.

---

## Web App — live: `10.44.4`

### Manage Layouts i reguły walidacji

Silniki reguł, które w poprzednim wydaniu trafiły na serwer, mają teraz swój
interfejs użytkownika — w Settings → Document Types → Manage Layouts.

Układy to rozmieszczenia pól wielokrotnego użytku, niezwiązane już ze źródłem
dokumentu. O tym, który układ otrzyma dokument, decydują reguły wyboru:
oceniane według priorytetu, wygrywa pierwsze dopasowanie, z układem domyślnym
jako rozwiązaniem awaryjnym.

<figure><img src="../../.gitbook/assets/manage-layouts-selection-rules-en.png" alt="Ekran Layouts &#x26; Selection Rules z kartami układów i nowym przełącznikiem reguł wyboru"><figcaption><p>Layouts &#x26; Selection Rules: układy wielokrotnego użytku z wyborem opartym na regułach</p></figcaption></figure>

Reguły walidacji pozwalają definiować własne kontrole wyodrębnionych wartości
i widzieć niepowodzenia oznaczone na dokumencie, wraz z informacją, która
reguła zadziałała. Wydanie zawiera katalog systemowych reguł domyślnych;
każda reguła pozostaje wyłączona, dopóki jej Państwo nie aktywują. Funkcję
włącza się per typ dokumentu w sekcji Custom Validation Rules.

<figure><img src="../../.gitbook/assets/custom-validation-rules-en.png" alt="Ekran Custom Validation Rules z listą systemowych reguł domyślnych, ich wagą i przełącznikami statusu"><figcaption><p>Custom Validation Rules: systemowe reguły domyślne, aktywowane per typ dokumentu</p></figcaption></figure>

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
  wszystkie wpisy.
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

## API Service — live: `12.61.8`

- **Dojrzalsze reguły walidacji:** nowe operatory warunków (zawiera, zaczyna
  się od, kończy się na), wartości ze źródeł typu lista wartości, aktywacja
  per typ dokumentu oraz ślad audytowy pokazujący, kto utworzył lub zmienił
  każdą regułę. Po zmianie reguł dokumenty są automatycznie walidowane
  ponownie.
- **Reguły transformacji:** mogą teraz ustawiać lub czyścić wartości w całym
  dokumencie, są aktywowane per typ dokumentu i mają ten sam ślad audytowy.
- **Reguły wyboru układu:** aktywacja przeniesiona na typ dokumentu,
  a szablony układów zapisują, kto i kiedy je zmienił.
- **Bezpieczeństwo skryptów:** zmiany skryptów wymagają hasła czasowego
  (zob. Najważniejsze zmiany).
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
  Eksporty M3 mogą zawierać pozycje kosztowe o zerowej kwocie.
- **Zatwierdzenia:** zatwierdzenie jest wiązane z wnioskiem o zatwierdzenie
  tylko wtedy, gdy zatwierdzający jest osobą do niego przypisaną.
- **Stabilność logowania:** chwilowy błąd wewnątrz walidacji tokenu nie
  wylogowuje już użytkowników; aplikacja ponawia próbę.
- **Klasyfikacja:** reguły źródła dopasowują się teraz do każdego pola źródła
  dokumentu, a nie do stałych pozycji.
- **Modele AI:** wycofany model Turbo jest wszędzie mapowany na Fast, łącznie
  z wariantami dostrojonymi, z zabezpieczeniem gwarantującym, że wycofany
  model nigdy się nie uruchomi.

## Auth Service — live: `1.72.5`

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

## Email Service — live: `1.39.8`

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

## PO Match Service — live: `1.58.6`

- **Status „tabela niekompletna”:** faktury, których tabeli pozycji nie udało
  się zmapować, otrzymują własny status zamiast mylącego „nie znaleziono
  zamówienia” (zob. Najważniejsze zmiany). Pulpit pokazuje go ikoną braku
  dopasowania.
- **Lepsze szczegóły błędów:** niepowodzenia mapowania tabeli wskazują
  konkretną kolumnę, której nie udało się zmapować.
- **Czystsze zachowanie API:** żądania o nieistniejące reguły PO zwracają
  poprawną odpowiedź „nie znaleziono”, a uszkodzone wpisy pamięci podręcznej
  są usuwane, zamiast powodować powtarzające się błędy.

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

## OCR Service — live: `1.9.8`

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

## Docflow Service — live: `2.6.5`

- **Dopasowanie PO w przepływach pracy:** brakujące wartości porównania są
  traktowane jako brak danych, a nie jako niezgodność.
- **Karty potwierdzeń zamówień:** kupujący i osoba odpowiedzialna są ustalani
  niezawodnie.
- **Koszty frachtu:** gdy żadna ze stron nie ma kosztów, przypadek jest
  rozstrzygany przez kartę operatora, zamiast utykać.
- **Bezpieczeństwo:** tokeny API przepływów pracy są weryfikowane względem
  organizacji, do której należą.

## Barcode Service — live: `1.17.4`

- **Długotrwałe podziały:** połączenie z kolejką zadań jest podtrzymywane
  podczas długich zadań kodów kreskowych, więc podział dużych partii nie
  utyka już pod koniec.

---

## Bez zmian w tym wydaniu

**Auth Bridge** (`0.3.6`), **Auto Accounting** (`1.20.1`), **Docnet**
(`1.55.1`), **FTP** (`1.31.1`), **Operator** (`1.40.2`) i **Ideas**
(`0.3.1`) nie zawierają zmian w tym okresie.

<!-- Generated by the docbits-changelog skill (version-boundary mode: exact git
     ranges between the LATEST (2026-07-09..15) and NOVA (2026-07-15..21)
     version-bump commits supplied by the user, per service). -->
