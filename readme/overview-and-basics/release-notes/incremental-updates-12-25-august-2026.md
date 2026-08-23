# Informacje o wersji DocBits — 12–25 sierpnia 2026

_Co zmienia się w produkcyjnej aktualizacji DocBits z 25 sierpnia 2026,
obejmującej wszystko od wydania z 12 sierpnia. Każda usługa pokazuje
wdrażaną wersję, a następnie opisuje nowości i poprawki prostym językiem.
Usługi niewymienione poniżej nie miały żadnych zmian widocznych dla
klientów._

---

## Najważniejsze zmiany

- **Ściślejsza izolacja organizacji.** Przegląd bezpieczeństwa zamknął kilka
  miejsc, w których dane jednej organizacji mogły być odczytywane lub
  zapisywane z innej: skrypty dokumentów, listy użytkowników podorganizacji,
  członkostwa w grupach oraz token przetwarzania, z którym dokument
  przechodzi przez potok, są teraz sprawdzane względem organizacji
  wywołującego. Zatwierdzenia egzekwują też poprawnie zasadę czterech oczu:
  drugi zatwierdzający musi być inną osobą niż pierwszy.
- **Dokumenty przestają utykać.** Naprawiono cztery niezależne przyczyny
  wiecznie wiszących dokumentów: eksporty pozostające w stanie „Exporting”
  po odrzuceniu, restarty zamrożone po awarii kroku przetwarzania, podziały
  po kodach kreskowych, które nigdy nie raportowały wyniku, oraz ekran
  księgowania zawieszony na „Preparing…”. W każdym z tych przypadków
  dokument teraz albo kończy przetwarzanie, albo pokazuje rzeczywisty błąd,
  na który można zareagować.
- **Faktury korygujące są rozpoznawane jako faktury korygujące.** Faktury korygujące
  XRechnung 3.0, 3.0.1 i 3.0.2 w składni CII, czyste faktury korygujące CII oraz
  dokumenty ZUGFeRD 2.4 / Factur-X 1.08 są teraz klasyfikowane poprawnie,
  z kwotą łączną odczytywaną z właściwego pola. W dokumentach skanowanych,
  które wspominają zarówno o „fakturze”, jak i „fakturze korygującej”,
  rozstrzyga słowo kluczowe położone bliżej typu dokumentu, a kwoty znów
  stają się dodatnie po przeklasyfikowaniu faktury korygującej z powrotem na
  fakturę.
- **Dopasowanie PO liczy w sposób, któremu można zaufać.** Tolerancje są
  porównywane jako dokładne wartości dziesiętne zamiast liczb
  zmiennoprzecinkowych i bazują na wartości zamówienia zakupu, a faktury
  odwołujące się do kilku zamówień są dopasowywane do wszystkich z nich.
  Kolumny, których nigdy nie zmapowano, nie zniekształcają już kontroli
  kwoty pozycji, a gdy brakuje wymaganych kolumn, błąd je wymienia.
- **Przebiegi workflow zachowują wykonaną pracę.** Workflow zapisujący
  wartość pola robi to teraz na dokumencie w taki sposób, że późniejszy
  eksport nie może jej po cichu cofnąć. Ponawiane wyzwalacze nie odrzucają
  już tego, co przebieg zdążył wykonać, a dwa wyzwalacze trafiające w ten
  sam dokument ustawiają się w kolejce, zamiast odbierać sobie nawzajem
  blokadę.
- **E-maile resetowania hasła znów się wysyłają.** Dotąd po cichu nigdy nie
  opuszczały serwera. Formularz resetowania pokazuje też rzeczywistą
  informację zwrotną po wysłaniu, a odpowiedź nie zdradza już, czy dane
  konto istnieje.

---

## Web App — `10.55.0`

### Logowanie i konta

- Resetowanie hasła działa znów od początku do końca: wiadomość dociera,
  formularz potwierdza wysłanie, a odpowiedź jest taka sama niezależnie od
  tego, czy dany adres ma konto.
- Jeśli organizacja wymaga rejestracji drugiego składnika, ekran logowania
  teraz o tym informuje, zamiast kończyć się bez komunikatu.
- Administratorzy nie mogą już włączyć wymuszania MFA dla całej organizacji,
  zanim rejestracja przy logowaniu stanie się dostępna — wcześniej mogło to
  odciąć użytkowników od systemu.

### Ekran walidacji

- Suwak powiększenia sięga teraz 150% (wcześniej kończył się na 80%),
  a powiększanie tabeli działa poza szerokość kontenera, zamiast nie robić
  nic.
- Puste pola kwotowe liczą się jako 0, zamiast wywoływać komunikat o
  błędzie, a podwójne kliknięcie na obrazie dokumentu jest ignorowane, gdy
  żadne pole nie jest wybrane.
- Baner pokazywany, gdy inna sesja trzyma blokadę dokumentu, nie miał
  treści; teraz wyjaśnia, o co chodzi. Tagowanie tabeli nie wywołuje już
  fałszywego ostrzeżenia „dokument został zmodyfikowany zewnętrznie”
  dotyczącego własnej zmiany.
- W tabeli AI przemapowanie kolumny, które odmapowałoby inną kolumnę, prosi
  najpierw o potwierdzenie, a wartości niebędące liczbami są oznaczane
  w kolumnach AMOUNT i NUMBER.
- Zakładka „Extracted table” znów linkuje do ręcznego trenowania tabel, gdy
  jest pusta.
- Numery pozycji w tabeli porównania pozycji (Compare) są pokazywane jako
  identyfikatory, a nie zaokrąglane jak kwoty.
- Pola zatwierdzających tłumaczą identyfikatory użytkowników i grup na
  nazwy, więc nigdy nie pokazują surowego id ani nie pozostają puste.
  Terminy zadań są przeliczane jedną ścieżką uwzględniającą UTC, więc każdy
  widzi tę samą datę.
- Dokumenty cofnięte do walidacji pokazują wskaźnik ładowania zamiast
  martwego ekranu, gdy są przygotowywane.

### Księgowanie

- Podzielone pozycje zachowują znak % po naciśnięciu Enter, a 0 % jest
  akceptowane jako wartość.
- W filtrze kont Enter zatwierdza pierwsze pasujące konto, zamiast nie robić
  nic.
- Znaki flexdimension są mapowane po identyfikatorze wymiaru, więc wymiary
  trafiają do właściwej kolumny nawet przy innej kolejności.
- Nieudane przygotowanie księgowania kończy się komunikatem o błędzie,
  zamiast wisieć w nieskończoność na „Preparing…”, a ponowne otwarcie
  dokumentu nie podaje już nieaktualnych danych z poprzedniego.

### Dopasowanie PO

- Otwarcie PO Matching bez zmapowania wszystkich obowiązkowych kolumn jest
  znów możliwe; gdy czegoś brakuje, komunikat wymienia dokładnie te kolumny.
- Kolumny niezmapowane do niczego są ukrywane przy otwarciu ekranu — po
  jednorazowym pytaniu — i nie wpływają już na obliczenie kwoty pozycji.
- Dopasowana ilość odświeża się po zapisaniu, a okno o brakujących kolumnach
  kieruje do walidacji pól (Field Validation), gdzie można to naprawić.

### Pulpit i wyszukiwanie

- Kolumny oparte na listach rozwijanych (typ faktury, status i podobne)
  pokazują etykietę w języku interfejsu zamiast surowej zapisanej wartości.
- Wyszukiwanie pełnotekstowe akceptuje nawiasy jako zwykły tekst; wcześniej
  odrzucało takie zapytanie. Operator filtra „różne od” pozostaje wybrany,
  a ręczna edycja filtra nie psuje już nazwy pola.
- Wybranie podorganizacji w szybkim wyszukiwaniu wstawia jej nazwę, a nie
  uuid, a autouzupełnianie podorganizacji nie pokazuje już duplikatów.
- Pulpit może teraz pobrać do 10 000 dokumentów na okno wyszukiwania, więc
  duże zbiory wyników stronicują się poprawnie.
- Panel duplikatów dokumentów pokazuje te same rozwiązane kolumny co lista
  główna, a wielowyrazowe wartości filtra dostawcy nie giną po naciśnięciu
  Enter.

### Zadania

- E-mail o przypisaniu wychodzi przy przypisaniu zadania — jeden raz. Edycja
  zadania ani oznaczenie go jako wykonane nie wysyłają go ponownie, a data
  „przypisano” pozostaje datą przypisania. E-maile zadań renderują się też
  poprawnie w Outlooku.

### Workflow Builder

- Wyszukiwanie, kolejność sortowania i stronicowanie na liście workflow
  pozostają spójne podczas filtrowania.
- Przełącznik „run workflow on change” w kreatorze layoutów faktycznie
  steruje uruchomieniem, a jego włączenie wymaga wybrania workflow.

### Ustawienia i administracja

- Link pobierania WatchDog i polecenie konfiguracji wskazują środowisko,
  w którym się pracuje, a nie zawsze produkcję.
- Drzewa decyzyjne: wybrane pole dokumentu pozostaje podświetlone po
  ponownym otwarciu selektora, przycięte etykiety otrzymują podpowiedź
  (tooltip), a przy dodawaniu linii pokazywane są nazwy użytkowników
  (a nie surowe id).
- Pole wyboru System Admin można edytować podczas edycji użytkownika.
- Analityka: Core Web Vitals renderują się z rzeczywistych danych
  pomiarowych, a widok usługi logów działa.
- „Use Default Template” w menedżerze layoutów kopiuje domyślny layout
  zgodnie z przeznaczeniem.
- Niestandardowe etykiety pól nie nadpisują już wbudowanych tłumaczeń pól
  standardowych.
- Oferty w portalu dostawców: wysłanie oferty z wartością REF1 spoza
  dozwolonej listy jest blokowane.
- MediOrder otrzymuje wykrywanie duplikatów dokumentów na swoim ekranie
  walidacji.

## API Service — `12.82.3`

### Bezpieczeństwo i izolacja organizacji

- Przełączenie organizacji, w imieniu której się działa, jest weryfikowane
  względem rzeczywistego członkostwa i w razie wątpliwości kończy się
  odmową, a wewnętrzny endpoint testowy, który dawał się nadużyć do
  przekraczania granic organizacji, został zamknięty.
- Skryptów dokumentów nie można już odczytywać ani nadpisywać między
  organizacjami — ani przez wywołanie zastosowania skryptu na dokumencie,
  ani przez obcy identyfikator wersji przy zapisie.
- Listy użytkowników podorganizacji i listy członków grup zwracają wyłącznie
  osoby z organizacji wywołującego, a dodanie kilku użytkowników do grupy
  naraz nie gubi już wszystkich poza pierwszym.
- Poświadczenie z niewłaściwej organizacji jest odrzucane, zanim stanie się
  tokenem przetwarzania dokumentu, a zapytania wyszukiwania pełnotekstowego
  działają w kontekście wywołującego użytkownika, a nie tożsamości
  usługowej.
- Zatwierdzanie na zasadzie czterech oczu jest egzekwowane: drugi
  zatwierdzający musi być kimś innym niż osoba, która zatwierdziła jako
  pierwsza.
- Lista live PO Dashboard jest ograniczona do podorganizacji użytkownika.

### Potok przetwarzania dokumentów

- Dokumenty, którym odmówiono eksportu, nie tkwią już wiecznie w stanie
  „Exporting”, a błędy eksportu zawsze niosą komunikat zamiast pustego.
- Gdy krok przetwarzania ulegnie awarii, dokument przechodzi w stan błędu,
  zamiast utknąć w „restart in progress” bez wyjścia.
- Podział po kodzie kreskowym, który nie powiedzie się lub przekroczy limit
  czasu, oznacza dokument jako Error, zamiast po cichu pokazywać „Running”,
  a podział, który nie wytworzy dokumentów potomnych, zachowuje dokument
  nadrzędny i oznacza go, zamiast usuwać wszystko.
- Nieudane ponowienie nie może już nadpisać dokumentu, który w międzyczasie
  zakończył przetwarzanie.
- Dokumenty restartowane bez udziału użytkownika oraz dokumenty potomne
  z podziału działają teraz na trwałym tokenie organizacji, więc
  długotrwałe przetwarzanie nie kończy się z powodu wygasłej sesji.
- Pusta odpowiedź szablonu layoutu nie jest już buforowana przez sześć
  godzin — wcześniej powodowało to znikanie layoutów aż do wygaśnięcia
  bufora.

### Ekstrakcja i e-dokumenty

- Kwoty zapisane z minusem na końcu („100,00-”) są interpretowane jako
  ujemne, zamiast być pomijane.
- Dokumenty szwajcarskie są rozpoznawane jako szwajcarskie (CHF, numery VAT
  CHE, IBAN-y CH), zamiast domyślnie podlegać konwencjom niemieckim, a daty
  zapisane z myślnikami typograficznymi parsują się poprawnie.
- Faktury korygujące XRechnung 3.0, 3.0.1 i 3.0.2 w składni CII są klasyfikowane
  jako faktury korygujące z kwotą łączną odczytywaną z pola sumy końcowej; to
  samo dotyczy czystych faktur korygujących CII. Zadeklarowana wersja
  ZUGFeRD 2.4 / Factur-X 1.08 wygrywa z ogólnym identyfikatorem profilu,
  a same typy XRechnung rozwiązują się do swojego odpowiednika UBL lub CII,
  zamiast kończyć się błędem.
- Pola typu lista wartości (dropdown), takie jak Tax Country i Tax Code,
  zachowują wartość podczas transformacji pól; wcześniej były opróżniane.
- Ekstrakcja tabel: błąd w kolumnie wyłącznie liczbowej pozostaje w tej
  kolumnie, zamiast unieważniać całą tabelę, ekstrakcja tabel AI ma limit
  czasu obejmujący przebiegi wielopartiowe, a dwie awarie na nietypowych
  kształtach tabel (wiersze bez pozycji na stronie, nierówna liczba kolumn)
  zostały naprawione.
- Wzorce reguł źródłowych dopasowują się bez rozróżniania wielkości liter.

### Eksport

- Kontrola podatkowa, która nie powiedzie się podczas podglądu eksportu,
  zwraca czytelny błąd zamiast błędu serwera — na obu endpointach podglądu.
- Eksport SFTP może wysłać oryginalny dokument obok skonwertowanego.
- Gdy konfiguracje eksportu istnieją na kilku poziomach, konsekwentnie
  wygrywa najbardziej szczegółowa.
- Eksporty BOD mogą przenosić atrybuty typów kolumn poprzez mapowanie.

### Import i dane podstawowe

- Dziennik importu e-mail jest kompletny: odrzucone i nieudane wiadomości
  przychodzące zawsze otrzymują wpis w dzienniku z dokładnym powodem. Koniec
  z cichym gubieniem.
- Importy BOD zamówień zakupu utrzymują podlinie przy właściwej linii;
  przenoszona flaga przypinała je wcześniej do niewłaściwej.
- Import CSV z kilkoma nowymi dostawcami działa (ich generowane
  identyfikatory już nie kolidują), aliasy warunków skonta importują się
  i respektują ustawienie „on conflict”, a wybór IGNORE przy konflikcie
  działa nie tylko dla dostawców.
- Sugestia dostawcy (TF-IDF) zachowuje identyfikator dostawcy przy
  aktualizacji preferencji, więc sugestie nie wskazują już donikąd.

### Pozostałe poprawki

- Wiersze pulpitu tłumaczą etykiety list rozwijanych na język użytkownika,
  nie blokując żądania.
- Po edycji pól status dopasowania PO aktualizuje się, zamiast pokazywać
  stan sprzed edycji.
- Dokumenty Purchase Order Change otrzymują pięć pól odpowiadających
  Purchase Order oraz domyślny layout walidacji pól.
- Odpowiedzi błędów w 152 endpointach zwracają czytelne komunikaty zamiast
  surowych obiektów wyjątków, a strona analityki logów nie odpowiada już
  kodem 502 dla organizacji bez indeksu logów.

## Auth Service — `1.77.9`

- E-maile resetowania hasła po cichu nigdy się nie wysyłały; naprawiono to
  razem z leżącym u podstaw problemem bezpieczeństwa wątków.
- Powtórnie użyty token odświeżania jest odrzucany: rozstrzygające
  sprawdzenie w bazie danych wykonuje się teraz za każdym razem, zamiast być
  pomijane przy trafieniu w cache.
- Uwierzytelnianie dwuskładnikowe: aplikację uwierzytelniającą można
  zarejestrować obok kodów e-mail, a usunięcie ostatniego klucza dostępu lub
  ponowne wygenerowanie kodów zapasowych wymaga najpierw świeżego drugiego
  składnika.
- Poprawny identyfikator podorganizacji nie jest już odrzucany komunikatem
  „Organization not found”, a klucz API utworzony w podorganizacji
  rozwiązuje swojego użytkownika technicznego z tej podorganizacji.
- Edycja organizacji waliduje identyfikator partnera i nie resetuje już typu
  organizacji jako efektu ubocznego.
- „Pozostałe tokeny” w widoku subskrypcji są zakotwiczone w roku
  kontraktowym, a nie kalendarzowym.

## Auth Bridge Service — `0.5.7`

- Replikacja kont między regionami UE i USA odzyskuje sprawność
  samodzielnie. Zerwany strumień replikacji podłącza się ponownie w miejscu
  przerwania, replikacja płynie dalej w trakcie uzgadniania, a pamięć
  uzgadniania jest ograniczona, więc usługa nie wpada już w pętlę awarii na
  dużych tabelach.

## Barcode Service — `1.18.7`

- Odczyt kodów kreskowych działa z limitem czasu i raportuje jego
  przekroczenie, zamiast się zawieszać — wcześniej dokument pozostawał
  uwięziony w przetwarzaniu.

## Docflow Service — `2.9.8`

- Wartości pól zapisywane przez kartę workflow trafiają na dokument w obu
  przechowywanych reprezentacjach, więc późniejszy eksport już ich nie cofa.
- Ponowiony wyzwalacz zachowuje pracę już wykonaną w przebiegu, rywalizujące
  wyzwalacze na tym samym dokumencie ustawiają się w kolejce, zamiast
  odbierać sobie blokadę, a eskalowane ponowienie trafia na początek
  kolejki.
- Karty porównania zamówień zakupu: tolerancje porównują się jako dokładne
  wartości dziesiętne i bazują na wartości zamówienia zakupu, odwrócone
  kierunki porównania są dostępne jako opcje, przypisana grupa jest
  raportowana jako grupa, zamiast oblewać porównanie z identyfikatorem
  użytkownika, identyfikatory przypisań porównują się poprawnie jako
  UUID-y, linie z pustymi wartościami liczbowymi są pomijane, a porównanie
  „received” bez żadnych danych przyjęcia raportuje brak danych, zamiast
  udawać zgodność.
- Karta Apply Decision Table została wycofana.

## Email Service — `1.41.0`

- Importy z Gmaila pobierają każdy załącznik dokładnie raz; duplikaty
  z nakładających się pobrań zniknęły.
- Kursor odczytu importu przesuwa się dopiero po potwierdzeniu importu, więc
  awaria w trakcie importu nie może już pominąć e-maili.
- Gdy konfiguracja importu zostaje dezaktywowana, ponieważ istnieje podobna,
  ta dezaktywacja jest widoczna i zgłaszana powiadomieniem, a nie cicha.

## Extraction Service — `1.54.5`

- O tym, czy dokument jest fakturą korygującą czy fakturą, rozstrzyga słowo
  kluczowe położone bliżej wzmianki o typie dokumentu, a nie zasada
  „pierwsze trafienie wygrywa”.
- Gdy kilka interpretacji podatkowych mieści się w tolerancji, preferowane
  jest dokładne uzgodnienie zamiast bliskiego przybliżenia.
- Po wymuszonym ponownym OCR przywracane są typ dokumentu i ustawienia
  regionalne, więc ekstrakcja tabel i trenowanie znów działają na takich
  dokumentach.
- Dokumenty bez typu dokumentu nie powodują już awarii wyszukiwania reguł
  tabel.

## FTP Service — `1.32.8`

- Skanowanie folderów wykonuje jedno odpytanie na folder z ograniczoną
  głębokością, więc importy z dużych katalogów FTP są znacznie szybsze
  i przestają przekraczać limity czasu.

## Fulltext Service — `1.42.3`

- Dokumenty, których zapisane dane wyszukiwania nie zawierały
  wyekstrahowanych pól, są ponownie indeksowane z bazy danych, więc znów
  pojawiają się w wyszukiwaniu na pulpicie.
- Okno wyszukiwania pulpitu obsługuje do 10 000 dokumentów.
- Wyszukiwania fasetowe nie kończą się już błędem przy aktywnym
  wyszukiwaniu semantycznym.

## OCR Service — `1.10.7`

- Budżet czasu OCR jest wyliczany według rzeczywistego kosztu na stronę,
  więc długie dokumenty kończą przetwarzanie, zamiast trafiać na limit
  potoku.

## PO Match Service — `1.59.8`

- Linie tabeli z zerową ilością są pomijane w kontrolach niezgodności,
  zamiast generować fałszywe niezgodności.
- Gdy brakuje wymaganych kolumn dopasowania PO, wynik je wymienia.
