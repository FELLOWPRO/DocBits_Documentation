# Informacje o wersji DocBits — 15 września 2026

_Co zmienia się w produkcyjnym hotfixie DocBits z 15 września 2026 (wydanie
R1.0.13), obejmującym wszystko od wydania z 1 września. Każda usługa pokazuje
wdrażaną wersję, a następnie opisuje nowości i poprawki prostym językiem.
Usługi niewymienione poniżej nie miały żadnych zmian widocznych dla
klientów._

---

## Najważniejsze zmiany

- **Jeden zestaw reguł wyszukiwania na pulpicie.** `field=value` oznacza teraz
  dokładnie tę wartość w każdym silniku wyszukiwania, `field:value` oznacza
  „zawiera” (z `value*` i `*value` dla „zaczyna się od” i „kończy się na”),
  a `field!=value` zwraca także dokumenty, które w ogóle nie mają wartości.
  Wyszukiwanie bez chipa to wyszukiwanie fragmentu tekstu we wszystkich
  polach, włącznie z numerami zamówień zakupowych, kodami kreskowymi i
  numerami zapotrzebowań. Liczba wyników, kafelki statusów i stronicowanie
  opisują ten sam zbiór dokumentów, a wyszukiwanie, które dotarło do granicy
  okna wyników lub odbyło się bez indeksu pełnotekstowego, informuje o tym,
  zamiast raportować „kompletne”. Własne połączenie wyszukiwania pulpitu
  (WebSocket) nigdy wcześniej nie docierało do indeksu pełnotekstowego; teraz
  dociera.
- **Dostawcy są rozpoznawani częściej.** Gdy jedno pole wyszukiwania (numer
  podatkowy, IBAN, numer dostawcy) pasuje dokładnie do jednego dostawcy, ten
  dostawca jest używany nawet wtedy, gdy szerokie pole, takie jak nazwa,
  pasuje do kilku. Dokumenty XRechnung CII i Facturae znów niosą swoje pola
  dostawcy. Tam, gdzie dane podstawowe zastąpiły wyekstrahowaną wartość,
  ekran walidacji o tym informuje i pozwala przywrócić oryginał.
- **Dopasowywanie zamówień zakupowych tłumaczy się samo.** Ekran informuje,
  dlaczego nie ma dopasowania, dymek niezgodności podaje nazwę kolumny, która
  nie pasowała, historia dopasowań wymienia uruchomione reguły transformacji,
  a ceny jednostkowe PO są wyprowadzane z kwoty netto. Ręczne dopasowania
  znów działają w organizacjach bez reguły zapasowej, usunięte zamówienia
  zakupowe pozostają usunięte, a przerwane zadanie dopasowania oznacza
  dokument jako nieudany, zamiast zostawiać go na zawsze w „Queue”.
- **Zablokowane dokumenty i fałszywe błędy.** W organizacjach przesyłających
  dokumenty w sposób ciągły dokumenty były degradowane do priorytetu kolejki,
  który w godzinach pracy nigdy nie był obsługiwany (866 dokumentów
  utkniętych w stanie „new” u jednego klienta). Mechanizm ponawiania mógł
  po kilku godzinach nadpisać pomyślnie wyeksportowany dokument stanem
  „error” i wysłać dla niego e-mail o błędzie eksportu. Ta ścieżka została
  zamknięta.
- **Touchless Intelligence.** Zakładka Analityki, która mierzy, ile dokumentów
  przechodzi przez DocBits bez udziału człowieka, otrzymuje swoje pełne
  pierwsze wydanie: klastry problemów z poradami AI, analiza zbiorcza,
  propozycje zmian z podglądem, zastosowaniem i cofnięciem, strona dostawcy
  z trendem i przykładami, diagram przepływu przez potok dla każdego
  dokumentu oraz diagram zestawu reguł zamówień zakupowych, który informuje,
  dlaczego dokument nie przeszedł.
- **Szybciej tam, gdzie danych jest dużo.** Zimne logowania pomijają
  sumowanie księgi kredytów, które trwało do 33 s, lista rozwijana kont
  księgowych działa w organizacjach z ponad 2 000 kont, strona reguł
  E-Documents stronicuje swoje 1 600 reguł na serwerze, zamiast zamrażać
  przeglądarkę, a przycisk Odśwież na pulpicie zamówień zakupowych zwraca
  świeże dane zamiast listy z bufora.
- **Bezpieczeństwo.** Mapy źródłowe frontendu przestają być wysyłane z każdym
  wdrożeniem, filtry wyszukiwania danych podstawowych są przekazywane jako
  parametry SQL, a nie wstawiane do zapytania, wygasły token jest odrzucany
  nawet przy trafieniu w cache, a kontrola organizacji dla tokenu
  przetwarzania jest egzekwowana niezależnie od poprzedzającej ją warstwy.

---

## Web App — `10.66.3`

### Logowanie i konta

- Logowanie jest szybsze. Sprawdzenie subskrypcji przy logowaniu pytało o
  pełne saldo kredytów, co sumowało miliony wierszy księgi i często
  przekraczało 10-sekundowy limit czasu klienta. Logowanie pyta teraz tylko
  o to, czy subskrypcja istnieje; salda nadal są obliczane w Settings →
  Subscription.
- Po przełączeniu regionu (EU ↔ US) pozostajesz zalogowany. Region docelowy
  przez kilka sekund odpowiada „invalid token”, dopóki sesja się nie
  zreplikuje, a dwie ścieżki kodu odczytywały to jako martwą sesję.
- Naprawiono nakładkę „Updating DocBits v10.59.3.1 → v10.59.3.1”, która na
  sandboxie przeładowywała się bez końca. Przeładowanie do tej samej wersji
  nie pokazuje już nakładki, pętla jest ograniczona dla każdej karty
  przeglądarki, a baner oferuje ręczne odzyskanie, gdyby sytuacja się
  powtórzyła.
- Administratorzy mogą przyznać zakładkę Analytics Dashboard wybranym rolom,
  a zmiany ról zapisują się niezawodnie.
- Pole wyboru System Admin można zaznaczyć na istniejącym użytkowniku.
  Utworzenie administratora systemu z poziomu frontendu ma teraz skutek;
  wcześniej zadanie synchronizacji resetowało tę flagę przy każdym
  uruchomieniu.
- Settings → Roles: lista członków renderuje się, zamiast zawisać za
  wskaźnikiem ładowania, gdy serwer odpowie błędem.
- Logowanie do serwera DocBits MCP wymusza uwierzytelnianie dwuskładnikowe i
  jednorazową zgodę.

### Pulpit i wyszukiwanie

- Nowe reguły operatorów, opisane także w oknie pomocy wyszukiwania: `=` to
  dokładnie ta wartość (bez rozróżniania wielkości liter), `:` to „zawiera”,
  `: value*` to „zaczyna się od”, `: *value` to „kończy się na”, `!=` to
  wszystko, co nie jest dokładnie tą wartością, włącznie z dokumentami bez
  wartości. Cudzysłowy służą wyłącznie do grupowania wartości ze spacjami.
- Fraza w cudzysłowie, np. `"Johnson and Johnson"`, jest wyszukiwana jako
  jedna fraza. „and” i „or” wewnątrz cudzysłowu nie są już odczytywane jako
  spójniki.
- Gdy zwykłe wyszukiwanie niczego nie znajdzie, pulpit wyjaśnia regułę i
  oferuje chipy do wybrania jednym kliknięciem (`Invoice number : <term>`,
  `Purchase order : <term>`, `Supplier ID : <term>`).
- Wyszukiwanie z zerową liczbą wyników resetuje stronicowanie i każdą liczbę
  na stronie. Wcześniej paginacja zachowywała liczbę wyników poprzedniego
  wyszukiwania.
- Numery zamówień zakupowych, numery zamówień, kody kreskowe, typy faktur i
  numery zapotrzebowań można znaleźć bez chipa.

### Ekran walidacji

- Wartości zastąpione przez dane podstawowe są oznaczone. Bursztynowa
  plakietka pokazuje wartość oryginalną i bieżącą, zbiór danych i sposób
  dopasowania, a przycisk przywraca wyekstrahowaną wartość. Wartości
  potwierdzone przez dane podstawowe lub uzupełnione z zamówienia zakupowego
  otrzymują własne etykiety. Wcześniej wszystkie nosiły plakietkę „Extracted
  using saved rules”.
- Stempel zatwierdzenia jest zapisywany także wtedy, gdy strona ma już inną
  adnotację. Pobrane dokumenty z adnotacjami nie zawierały w takim przypadku
  stempla.
- „Hide non mapped columns” zachowuje kolumny wytrenowane ręcznie (na przykład
  Item Number i Purchase Order).
- Zapisywanie reguł ekstrakcji działa po wpisaniu numeru strony i następnie
  narysowaniu ramki dla pola. Ta sekwencja wcześniej powodowała awarię
  zapisu.
- Ekstrakcję strukturalną można włączyć dla poszczególnych dostawców — w
  oknie tfidf na ekranie walidacji oraz jako kolumnę tylko do odczytu w
  Settings → Classification & Extraction.
- Train Model działa w tle. Ekran pokazuje „training started”, odpytuje o
  wynik i raportuje sukces lub niepowodzenie. Duże organizacje dostawały
  wcześniej błąd bramy (gateway error), podczas gdy trenowanie trwało dalej
  po stronie serwera.
- Tryb ciemny: kursor nożyczek na ekranie podziału i przełącznik trybu na
  ekranie Auto Accounting są znów czytelne.

### Dopasowywanie zamówień zakupowych

Zmiany zapowiedziane na stronie [Hotfixy 8 września 2026](incremental-updates-8-september-2026.md)
trafiają na produkcję wraz z tym wydaniem: dopasowanie przetrwa zapis,
dopasowywanie uruchamia się ponownie po poprawieniu numeru PO, ekran
informuje, dlaczego nie ma dopasowania i dlaczego dopasowanie nie zostało
zachowane, historia dopasowań pokazuje reguły transformacji, a cena
jednostkowa PO jest obliczana z kwoty netto. Dodatkowo:

- Dymek niezgodności podaje nazwę kolumny, która nie pasowała. Wcześniej był
  pusty, ponieważ rejestrowane były tylko dopasowane kolumny, a ekran mógł
  powiedzieć jedynie „Mismatched”.
- Przycisk Auto Match eksportuje też dokument, gdy włączona jest opcja „PO
  Auto Match and Export”. Wcześniej eksport następował tylko wtedy, gdy
  dokument został otwarty z pulpitu przez „PO Match”.
- Okno tolerancji ilości/ceny jednostkowej pozostaje otwarte, gdy serwer
  odrzuci zapis, więc wprowadzone wartości nie giną.
- Przycisk Odśwież na pulpicie zamówień zakupowych czyści bufor po stronie
  serwera przed ponownym załadowaniem. Zamówienie zakupowe zaimportowane z
  ERP pojawiało się dopiero po siedmiu–ośmiu minutach.
- Strona reguł dopasowywania PO rysuje zestaw reguł jako schemat blokowy, a
  historia dopasowań przeniosła się do paska narzędzi akcji.

### Księgowanie

- Organizacje z ponad 2 000 kont przeszukują listę kont na serwerze. W
  takich organizacjach lista rozwijana była na sandboxie pusta, a ładowanie
  strony trwało pięć sekund.
- Konta, do których odwołuje się dokument, są rozwiązywane w partiach:
  dokument ze 100 pozycjami i dwoma podziałami na pozycję potrzebuje 4
  żądań zamiast 403.
- Nagłówki tabel Auto Accounting i PO używają etykiety ustawionej w kreatorze
  layoutów zamiast tekstu wpisanego na stałe w kod.

### Ustawienia

- Settings → E-Documents → Rules stronicuje, przeszukuje i sortuje katalog
  1 600 reguł na serwerze. Zakładka renderowała wcześniej wszystkie reguły
  naraz i zamrażała przeglądarkę. „Reset all” to jedno wywołanie zamiast
  jednego na regułę.
- Ustawienia zaawansowane typu dokumentu pokazują zapisany stan każdego
  przełącznika. Zapisane `false`, tolerancja `0` lub pusta lista wyboru były
  zastępowane wartością domyślną, a przełączenie typu dokumentu pozostawiało
  wartości poprzedniego typu.
- Reguły transformacji: akcja „Set value” zapisuje się. Edytor wysyłał ją pod
  nazwą, którą serwer odrzuca.
- List of Values: pasek boczny pokazuje nową listę i usuwa skasowaną bez
  przeładowania; spóźnione odpowiedzi z poprzedniej listy nie nadpisują już
  bieżącej.
- Link do podtypów dokumentu jest pokazywany na standardowych typach
  dokumentów.
- Mapowanie JPL eksportu SMB pobiera się jako `.properties`, więc plik można
  ponownie przesłać. Był nazywany `.xml` i odrzucany przy ponownym
  przesyłaniu.

### Workflow

- Zmiana nazwy workflow zachowuje zmiany kart wykonane w tej samej sesji.
  Nowe workflow są tworzone jednym żądaniem zapisu, a zmiany nazw szablonów
  są utrwalane.
- Wyeksportowany plik workflow zawiera całą kopertę eksportu (wersja, nazwa,
  opis). Zaawansowane workflow można znów importować; wcześniej plik tracił
  wersję, był odczytywany jako standardowy workflow i odrzucany.
- Filtry kolumn na liście workflow łączą się operatorem AND. Przy aktywnym
  filtrze nazwy i daty do wyniku przedostawały się wiersze pasujące tylko
  nazwą.
- Terminy zadań używają formatu daty z ustawień użytkownika na liście, na
  tablicy i w widoku szczegółów.

### Analityka: Touchless Intelligence

Zakładka Touchless (Analityka → Touchless) mierzy, ile dokumentów przechodzi
przez DocBits bez udziału człowieka, i dlaczego pozostałe nie przeszły. To
wydanie ją kompletuje:

- **Klastry problemów z dowodami.** Dokumenty, które wymagały interwencji,
  są grupowane według przyczyny. Każda karta klastra wymienia pola, kody
  walidacji i komunikaty błędów, na których dokumenty przepadają, oraz
  dostawcę — lub informuje, że go nie ma. Klastry, które DocBits może
  naprawić (reguła, ustawienie pola), są oddzielone od tych, które może
  naprawić tylko dostawca, a budżet analizy AI trafia najpierw do tych
  naprawialnych.
- **Analiza AI, oznaczona jako taka.** Karta klastra informuje, czy poradę
  napisał model językowy, czy reguła, co analiza policzyła i kiedy przestała
  być aktualna oraz czy kliknięcie użyje ponownie zbuforowanej analizy. Jeśli
  doradca AI nie może działać w tym środowisku, zakładka podaje powód.
- **Analiza zbiorcza.** Analizuj wiele klastrów w jednym przebiegu, obserwuj
  klaster po klastrze, co przebieg robi, i znajdź wyniki później. Lista
  wyników przetrwa nawigację i przeładowanie, a przebieg nie zawiesza się już
  na „Running · 0/6 done” w widoku podorganizacji.
- **Propozycje zmian.** Rekomendacja staje się czymś, na czym można działać:
  karta wyjaśnia proponowaną zmianę w czterech pytaniach, pozwala ją
  dostosować, pokazuje podgląd tego, co by zrobiła (nic nie jest
  zapisywane), stosuje ją, mierzy efekt i może ją cofnąć. Kroki naprawy
  linkują bezpośrednio do wskazanej strony ustawień, wstępnie przefiltrowanej
  według typu dokumentu, pola lub reguły.
- **Strona dostawcy.** Wybierz dostawcę z zakładki lub przeszukaj kolejkę
  szans według nazwy lub numeru. Strona pokazuje wskaźnik touchless dostawcy
  w czasie (od 30 dni do 1 roku), jego problematyczne dokumenty i dokumenty,
  które przeszły dobrze, oraz oferuje diagnozę AI dla danego dostawcy. Można
  porównać obok siebie do pięciu dostawców. Zamiast wewnętrznego hasha
  pokazywany jest numer dostawcy.
- **Przepływ przez potok.** Diagram dla każdego dokumentu i klastra pokazuje
  drogę przez przyjęcie, klasyfikację, kontrolę e-dokumentu, dostawcę, OCR,
  ekstrakcję, walidację, dopasowanie PO, zatwierdzenie i eksport, wraz z
  etapem, który ją zatrzymał.
- **Dopasowywanie zamówień zakupowych, wyjaśnione.** Zestaw reguł PO jest
  rysowany jako schemat blokowy na stronie ustawień i w Touchless, wraz ze
  ścieżką, którą przeszedł dany dokument, i podanym prostym językiem
  powodem, dlaczego nie przeszedł. Kody powodów rozróżniają „nie znaleziono
  zamówienia zakupowego” od „niezgodności pozycji” i „braku wymaganego
  pola”.
- **Segmentacja.** KPI, klastry i propozycje można podzielić według pola
  dokumentu, na przykład Order Type = Direct / Indirect.
- **Poprawne liczby.** Kafelki KPI respektują filtr podorganizacji i liczą
  tylko dokumenty, które widok szczegółowy potrafi wyświetlić. Sesja
  przeglądarkowa użytkownika systemowego organizacji liczy się jako człowiek,
  więc dokumenty poprawione ręcznie nie są już zaliczane jako touchless.
- Pasek narzędzi raportu mieści swoje kontrolki na szerokich ekranach, a
  kolory trybu ciemnego pochodzą z motywu.

### DocNet

- Kanał Aktywności, widżet Ostatnia aktywność i oś czasu misji są
  przetłumaczone. Podsumowania audytu były po angielsku we wszystkich 22
  językach.
- Agenci widzą pola zdefiniowane przez typ dokumentu, które ekstrakcja
  pozostawiła puste. Wcześniej uznawali, że takie pola nie istnieją, i
  pomijali wymagane aktualizacje bez próby zapisu.

### Bezpieczeństwo

- Mapy źródłowe frontendu są usuwane z każdego wdrożenia. Serwowało je każde
  środowisko, włącznie z produkcją.

---

## API Service — `12.83.156`

### Rozpoznawanie dostawców i dane podstawowe

- Dostawca jest identyfikowany, gdy jedno pole wyszukiwania jest
  jednoznaczne. Przy kilku przeszukiwalnych polach wyniki były łączone jako
  suma, więc szerokie dopasowanie nazwy z czterema dostawcami zagłuszało
  numer podatkowy pasujący dokładnie do jednego. Pola, które do niczego nie
  pasują, nie blokują już pól, które pasowały. Zobacz
  [Ustawienia danych głównych](../../administration-and-setup/settings/global-settings/document-types/fields/master-data-settings.md),
  aby dowiedzieć się, jak pola współdziałają.
- Zastąpienia z danych podstawowych są rejestrowane wraz z pochodzeniem:
  zbiór danych, konfiguracja, pole źródłowe, operator i rodzaj dopasowania.
  Ekran walidacji to pokazuje i może przywrócić wyekstrahowaną wartość.
- Cash Discount Term jest importowany z BOD dostawcy; u dostawców
  synchronizowanych z ERP był pusty. Discount Term Overwrite wprowadzone jako
  pełny kod („143”, „012”, „X08”) jest stosowane; wcześniej brany był pod
  uwagę tylko prefiks procentowy.
- Wyszukiwania w danych podstawowych są ograniczone do 1 000 wierszy na
  stronę i przestawiane (pivot) w SQL. Wyszukiwanie w 19 000 rekordów
  trwało pięć sekund na wywołanie i blokowało API.
- Nazwy właściwości filtrów i typy danych w wyszukiwaniu danych podstawowych
  są przekazywane jako parametry SQL. Wcześniej były wstawiane bezpośrednio
  do zapytania.

### Przetwarzanie dokumentów

- Dokumenty z organizacji przesyłającej w sposób ciągły były degradowane do
  priorytetu 9, który kolejka obsługuje tylko wtedy, gdy każdy wyższy
  priorytet jest pusty. Degradacja jest teraz ograniczona do 3. Mechanizm
  uzgadniania, który powinien ponownie kolejkować zablokowane dokumenty, nie
  miał działających poświadczeń na produkcji; teraz ma.
- Zakończony, wyeksportowany dokument nigdy nie jest nadpisywany stanem
  „error”. Flaga workflow, która nigdy nie była czyszczona, sprawiała, że
  mechanizm ponawiania co minutę podejmował pomyślnie wyeksportowany
  dokument, aż limit ponowień oznaczył go jako „error” i wysłał klientowi
  e-mail o błędzie eksportu — 2 h 17 min po eksporcie.
- Scalanie i dołączanie akceptuje pliki `.PDF` i `.Pdf`. Plik ze skanera o
  nazwie `SCAN0001.PDF` był odrzucany z komunikatem „Only PDF files are
  allowed.”
- Unieważnianie bufora skanuje przestrzeń kluczy raz zamiast dwa razy i
  czyści tylko te typy danych wyszukiwania, które zmienił BOD. Wcześniej każdy
  BOD czyścił cały bufor wyszukiwania organizacji, blokując API na czas
  przechodzenia po kluczach wszystkich użytkowników.
- Ponowne trenowanie modelu działa jako zadanie w tle i natychmiast zwraca
  status, który UI odpytuje.
- Token przetwarzania z innej organizacji jest odrzucany niezależnie od
  poprzedzającego go sprawdzenia członkostwa w podorganizacji.
- Synchronizacja użytkowników nie rusza flagi użytkownika systemowego,
  zamiast resetować ją przy każdym uruchomieniu.

### Eksport

- Pozycje przyjęć M3 łączą eksportowaną cenę jednostkową z własną podstawą
  ceny pozycji faktury. Cena wędrowała z dzielnikiem pozycji PO, a ERP
  przeliczał pozycję na 1 000-krotność fakturowanej kwoty.
- Eksport tabeli przetrwa pozycję, której zamówienie zakupowe zostało
  usunięte; pozycja jest eksportowana bez podstawy ceny.
- Eksport IDM: pole wielowartościowe zmapowane na pole liczbowe (na przykład
  ilość) powodowało awarię ładunku eksportu. Wartość jest najpierw
  konwertowana na tekst.

### E-dokumenty

- Faktury XRechnung CII, których kwota do zapłaty wynosi 0,00, ponieważ
  przedpłata równoważy sumę, pokazują sumę końcową (BT-112) jako kwotę
  łączną. Klient widział „kwota łączna 0,00”.
- Dokumenty XRechnung CII i Facturae znów dostarczają swoje pola dostawcy.
  Nieaktualne nadpisania na poziomie organizacji przesłaniały poprawne
  mapowanie domyślne, więc rozpoznawanie dostawcy nigdy nie mogło znaleźć
  dopasowania.
- Katalog reguł walidacji jest stronicowany, przeszukiwany i sortowany na
  serwerze, z fasetami dla paska filtrów.

### Klasyfikacja

- Dokumenty szwajcarskie są klasyfikowane jako `de_CH`, `fr_CH` lub `it_CH`
  na podstawie treści (kwoty w CHF, numery VAT CHE, IBAN CH). Ustawienia
  regionalne były brane z domyślnych ustawień organizacji i dokumenty
  szwajcarskie dostawały `de_DE`.

### Wyszukiwanie na pulpicie

- Jedna semantyka operatorów na Postgres i ClickHouse: `=` dokładnie, `:`
  zawiera z symbolami wieloznacznymi na brzegach, `!=` dopełnienie włącznie z
  pustymi wartościami. Na Postgres `=` było wcześniej dopasowaniem prefiksu,
  więc `invoice_id=911892112` zwracało również 911892112333.
- Zwykłe wyszukiwanie to wyszukiwanie fragmentu tekstu we wszystkich polach,
  włącznie z identyfikatorami biznesowymi. Zamówienie zakupowe, numer
  zamówienia, kod kreskowy, typ faktury, podtyp faktury i numer
  zapotrzebowania nie miały w ogóle gałęzi wyszukiwania zwykłym tekstem.
- Chip numeru faktury jest dokładny na Postgres, tak jak już był na indeksie.
  Zera wiodące, formy zmiennoprzecinkowe i wielkość liter są traktowane tak
  samo w wolnym tekście i w chipach.
- Wyszukiwanie WebSocket pulpitu przekazuje poświadczenie wywołującego do
  usługi pełnotekstowej. Wcześniej każde delegowanie było odrzucane, więc
  pulpit po cichu przeszukiwał wyłącznie Postgres i prezentował odpowiedź
  jako kompletną.
- Kafelki statusów, liczba wyników i lista wyników działają na jednym
  zestawie predykatów. Kafelki opisywały wcześniej całą organizację podczas
  każdego wyszukiwania.
- Uprawnienia do podorganizacji i typów dokumentów są stosowane przed oknem
  wyników, więc dozwolone dokumenty nie wypadają już poza limit 500 / 10 000.
- Wyszukiwanie wektorowe zatrzymuje się na rzeczywistym oknie wyników i
  raportuje ten limit, zamiast pokazywać „(50)” jako dokładną sumę.
- Wyszukiwanie, które odbyło się bez indeksu pełnotekstowego (brak indeksu,
  indeks opóźniony o minuty, nieudane sprawdzenie możliwości, zdegradowane
  rozwiązywanie pól), raportuje status okna zamiast „kompletne”.
- Eksporty z pulpitu dla obciętego wyszukiwania zawierają wiersz z uwagą w
  pliku CSV/XLSX i w e-mailu z powiadomieniem.
- Skrypty dokumentów wywołujące wyszukiwanie pełnotekstowe uwierzytelniają
  się poprawnie i ujawniają błędy, zamiast zwracać pusty wynik.

### Dopasowywanie zamówień zakupowych (mechanizm wbudowany w API)

Dla organizacji, które dopasowują w API, a nie w PO Match Service:

- Każde porównanie kolumn jest rejestrowane, włącznie z ceną jednostkową i
  ilością, więc dymek niezgodności może podać nazwę kolumny, która nie
  pasowała.
- Zamówienia zakupowe usunięte przez użytkownika pozostają usunięte w
  dopasowywaniu automatycznym.
- Poprawiony numer PO jest dopasowywany w tym samym zapisie, który go
  poprawia.

### Analityka

- Touchless: wszystkie zmiany backendu stojące za powyższą sekcją Web App,
  w tym dowody etapów rejestrowane przez każdy etap potoku, ślad dopasowania
  PO, propozycje zmian z podglądem, zastosowaniem i cofnięciem, segmentacja,
  status zbiorczy w jednym wywołaniu na cykl oraz punkt końcowy trendu
  przyjmujący dowolne okno i dostawcę.
- Naprawiono trzy zadania w tle analityki, które zawodziły przy każdym
  zaplanowanym uruchomieniu.

---

## PO Match Service — `1.59.34`

- Cena jednostkowa pozycji PO jest wyprowadzana z jej kwoty netto, a nie z
  sumy z podatkiem, a migawka PO dokumentu ponownie wyprowadza swoje ceny
  jednostkowe w momencie dopasowania.
- Usługa rejestruje, skąd pochodził każdy kandydat na numer PO i które numery
  przebieg wyszukał. Własny numer faktury dokumentu nigdy nie jest kandydatem
  na PO. Odrzucone dopasowanie zostawia na dokumencie swój powód dla ekranu.
- Rejestrowana jest kolumna, która nie pasowała, a kolumny usunięte przez
  regułę zapasową są mierzone.
- Zamówienia zakupowe usunięte przez użytkownika są respektowane, a
  nieaktualne dopasowania w tle są czyszczone po ostatecznym wykluczeniu.
- Ręczne dopasowywanie działa w organizacjach, których reguły nie mają flagi
  `is_fallback`. Użytkownicy wybierali pozycje, naciskali dopasuj i nic nie
  wracało.
- Koniec z dokumentami osieroconymi w „Queue”: limity czasu instrukcji bazy
  danych, sygnały keepalive i jawna obsługa miękkiego limitu czasu oznaczają
  zadanie jako nieudane, zamiast polegać na zabiciu procesu, które nie
  zostawiało śladu.
- Dwa błędy produkcyjne (cena jednostkowa `NaN`, grupa bez ilości) nie
  powodują już niepowodzenia całego dopasowania.
- Zmiany tolerancji są odczytywane przy każdym żądaniu dopasowania, więc
  tolerancja zapisana przed chwilą jest używana przez następne dopasowanie.
- Pięcioetapowy ślad decyzji jest utrwalany dla każdego dokumentu na potrzeby
  Touchless.

---

## Auth Service — `1.78.27`

- `/organisation/subscriptions` może pominąć saldo kredytów, a obliczanie
  kredytów uruchamia wszystkie okna roku kontraktowego w jednej instrukcji
  zamiast jednego zapytania na okno (32 zapytania po około 700 ms każde dla
  największej organizacji). Dzienne podsumowanie zużycia jest przygotowane
  do dalszego użytku.
- Liczby pozostałych tokenów w odczytach organizacji są obliczane dla
  każdego roku kontraktowego.
- Wygaśnięcie tokenu jest egzekwowane przy trafieniach w cache. Zbuforowany
  wpis mógł uwierzytelniać nawet do dziewięciu godzin po wygaśnięciu tokenu.
- Weryfikacja tokenu przestaje zapisywać niezmieniony `org_id` z powrotem do
  wiersza użytkownika przy każdym żądaniu, co generowało jeden UPDATE na
  wywołanie.
- Kontrole stanu (health checks) pomijają operacje I/O na Redis, a klient
  Redis korzysta z puli połączeń. Naprawiono wyciek pamięci, który wpychał
  autoskaler na maksymalną liczbę replik, a usługa wróciła do dwóch workerów.
- Powtórna rejestracja dostawcy (magic link otwarty dwukrotnie) używa
  ponownie istniejącego członkostwa, zamiast kończyć się błędem
  zduplikowanego klucza.
- Wątek e-maila resetowania hasła używa jedynej zarejestrowanej aplikacji
  Flask; reset zawodził od 25 sierpnia z komunikatem „current Flask app is
  not registered”.
- Flagę użytkownika systemowego można zmienić na istniejącym użytkowniku, gdy
  żaden inny członek jej nie ma.
- Logowanie MCP: MFA powiązane z transakcją, jednorazowa zgoda i wymuszony
  wybór konta, gdy przeglądarka przechowuje dwie tożsamości sesji.

---

## Auth Bridge Service — `0.5.7`

Replikacja uwierzytelniania EU ↔ US:

- Okresowe uzgadnianie utrzymuje strumień replikacji przy życiu. Trwało
  około 95 s, podczas gdy limit czasu nadawcy wynosił 60 s, więc każde
  sześciogodzinne uzgadnianie zrywało strumień zgodnie z harmonogramem.
- Gdy strumień umiera, slot replikacji jest podłączany ponownie w miejscu,
  zamiast przebudowywać most i ponownie uruchamiać pełne uzgadnianie
  startowe.
- Uzgadnianie porównuje klucze główne stronami, zamiast ładować obie strony
  do pamięci, co przestało się mieścić, odkąd tabela tokenów dołączyła do
  replikacji.
- Istniejące źródło replikacji (replication origin) jest traktowane jako
  sukces, a nie degradacja.

---

## Extraction Service — `1.55.33`

- Ekstrakcja strukturalna jest rozstrzygana dla każdego dostawcy: ustawienie
  wytrenowanego layoutu wygrywa z preferencją organizacji, tak samo jak
  model AI.
- Wyuczone mapowanie kolumn nie może zabronić kolumn, które faktura ma.
- Ekstrakcja tabel AI: kolumny kwotowe są typowane jako liczby z opisem, a
  zmyślone wartości nieliczbowe w kolumnach kwotowych („St.” skopiowane z
  sąsiedniej komórki do ceny jednostkowej za) są odrzucane, zamiast
  zapisywane.
- Faktury amerykańskie: gdy kwota netto już równa się sumie, podatek
  rozstrzyga się na 0, zamiast zachowywać fałszywy wyekstrahowany podatek.
  Szum zmiennoprzecinkowy poniżej centa nie rozstrzyga już między
  kandydującymi parami netto/podatek (268.28 + 22.13 przegrywało z netto =
  suma, podatek = 0).
- Tabela, której wiersz nagłówka nigdy nie został zmapowany na rzeczywiste
  nazwy, jest ekstrahowana, zamiast całkowicie zawodzić.

---

## Fulltext Service — `1.42.35`

- Bufor wyników wyszukiwania jest włączony w każdym środowisku; produkcja,
  sandbox i stage działały bez niego od czasu utworzenia aktywnych plików
  środowiskowych. Przesłanie i usunięcie go unieważniają, więc wyszukiwanie
  po przesłaniu widzi nowy dokument.
- Dokładne `=` na dynamicznym polu tekstowym porównuje wyłącznie całą
  wartość. Symbol wieloznaczny na analizowanej ścieżce sprawiał, że
  `note_field=53173` pasowało do „PO 53173 / 2024”.
- Sam identyfikator z myślnikiem, taki jak `2026-003`, to jeden literał, a
  nie zbiór tokenów.
- Numery zamówień zakupowych są znajdowane w każdej postaci przechowywania,
  włącznie z identyfikatorami składającymi się wyłącznie z cyfr, których
  klauzula dokładna była po cichu pomijana.
- Ścieżki odczytu przestają tworzyć indeks, który czytają. Brakujący lub
  pusty indeks raportował „kompletne, 0 wyników”; każda odpowiedź z zerową
  liczbą trafień niesie teraz status okna i powód.
- Zapisane wartości walutowe, starsze mapowania boolowskie, daty i flagi
  podatkowe przetrwają odchudzoną przebudowę indeksu, a wpisy indeksu bez pól
  są wykrywane i odtwarzane z ekstrakcji.

---

## Docflow Service — `2.10.11`

- Importy zaawansowanych workflow są uzależnione od uprawnień organizacji, a
  partia jest sprawdzana, zanim cokolwiek zostanie zapisane. Organizacja bez
  modułu zaawansowanego mogła zaimportować zaawansowany workflow, którego
  potem nie miała jak otworzyć.
- Zmiana nazwy workflow odbywa się w ramach zapisu, a zmiany nazw szablonów
  są utrwalane.
- Aktualizacja „pending workflow execution” jest ponawiana przy zerwanych
  połączeniach. Pojedyncze nieudane żądanie zostawiało flagę bez zmian i
  trzymało dokument poza eksportem, dopóki ktoś go nie zrestartował.

---

## Docnet Service — `1.56.12`

- Wykrywanie pól zwraca każde pole nagłówka zdefiniowane w layoucie,
  wypełnione lub nie, i odpowiada temu, co sprawdza kontrola zapisu. Agenci
  pomijali wymagane aktualizacje pól, ponieważ puste pola wyglądały na
  nieistniejące.
- Tożsamości są buforowane pod tym samym kluczem w zakresie organizacji,
  którego używa API, więc granica klucza API organizacji obowiązuje w obu
  usługach.

---

## Email Service — `1.41.6`

- Współdzielone skrzynki Office 365 z więcej niż dziesięcioma podfolderami
  rozwiązują każdy folder. Microsoft Graph stronicuje foldery po dziesięć;
  konfiguracje od 11. wzwyż zawodziły przy każdym odpytaniu z komunikatem
  „unable to find the selected Folder”.

---

## FTP Service — `1.32.18`

- Harmonogram SFTP startuje w każdym procesie roboczym, a nie przed
  rozwidleniem procesu (fork). Okresowe importy SFTP po cichu zawodziły z
  uszkodzonym stanem harmonogramu, podczas gdy świeży proces działał
  poprawnie.

---

## Auto Accounting `1.21.7`, Barcode `1.18.14`, OCR `1.10.11`, Operator `1.42.12`, Ideas `0.3.6`

Wyłącznie zmiany w budowaniu i wdrażaniu (aktualizacja obrazu bazowego,
poświadczenia CI). Brak zmian w zachowaniu.

<!-- Release R1.0.13. Everything in the prod->sandbox code delta is announced.
     Held back because Jira "Release No." names the later release R1.1:
     DRFS-778 (discount due dates on import), DRFS-712, MEF-165, MEF-166,
     DOCB-14389. Announce them with R1.1. -->
