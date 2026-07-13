# Informacje o wersji DocBits — 9–13 lipca 2026

_Przegląd tego, co zmienia się dla Państwa w tym wydaniu DocBits. Każda usługa
poniżej pokazuje wersję obecnie wdrażaną, a następnie opisuje nowości lub
poprawki prostym językiem — bez numerów zgłoszeń i żargonu inżynierskiego.
Usługi niewymienione poniżej nie miały w tym okresie żadnych zmian widocznych
dla klientów._

---

## Najważniejsze zmiany

- **Logowanie do wielu organizacji.** Użytkownicy należący do kilku
  organizacji otrzymują teraz przy logowaniu prawdziwy ekran wyboru
  organizacji, przełącznik organizacji w nagłówku oraz ustawienie organizacji
  domyślnej. Sesje są bezpiecznie powiązane z jedną organizacją naraz,
  a aplikacja automatycznie podąża za regionem aktywnej organizacji.
  Logowanie do niewłaściwego regionu automatycznie ponawia teraz próbę we
  właściwym regionie zamiast kończyć się błędem.
- **Kanały wydań (frozen / latest).** Organizacje mogą być teraz przypięte do
  stabilnego („zamrożonego”) wydania, podczas gdy inne otrzymują najnowsze
  aktualizacje — co umożliwia kontrolowane wdrożenia. Okno dialogowe Wersje
  usług zawiera nową kolumnę *Release*, a administratorzy zarządzają kanałem
  z poziomu Informacji o firmie. Kilka usług wykazuje w tym okresie większe
  skoki wersji wyłącznie z powodu nowej numeracji wersji kanałów — skoki te
  nie niosą żadnych zmian funkcjonalnych.
- **Konfigurowalne silniki reguł.** W API pojawiają się trzy nowe systemy
  reguł (każdy domyślnie wyłączony, włączany per organizacja): **reguły
  walidacji**, które sprawdzają wyodrębnione wartości i oznaczają
  niepowodzenia bezpośrednio na dokumencie, **reguły transformacji**, które
  automatycznie porządkują lub przepisują wyodrębnione wartości pól i tabel,
  oraz **wybór układu oparty na regułach**, który dobiera właściwy układ
  dokumentu na podstawie reguł, a nie na podstawie źródła dokumentu.
- **Przejrzystość importu e-mail.** Dziennik importu e-mail pokazuje teraz
  jeden rozwijany wiersz na załącznik, informuje, które dokumenty zostały
  utworzone (z przyciskami przenoszącymi bezpośrednio do nich na pulpicie),
  oznacza elementy pominięte i podzielone oraz umożliwia pobranie oryginalnej
  wiadomości e-mail jako pliku `.eml`.
- **Ekstrakcja tabel z użyciem AI.** Nowy tryb ustrukturyzowanej ekstrakcji
  AI dla tabel, z polem wyboru „Use AI” dla każdej tabeli i każdej kolumny
  w ustawieniach typu dokumentu.
- **Stabilność Web App.** Naprawiono nieskończoną pętlę przeładowań po
  wygaśnięciu sesji, naprawiono niedziałający Layout Builder, a tabele
  ekstrakcji mają teraz przeciągany uchwyt zmiany wysokości.
- **Nowość: Auth Bridge Service.** Nowa usługa utrzymuje dane logowania
  w ciągłej synchronizacji między regionami UE i USA, z wbudowanym
  samonaprawianiem i monitoringiem.

---

## API Service — live: `12.57.8`

- **Reguły walidacji (nowość, per organizacja):** konfigurowalny przez
  administratora silnik reguł sprawdza wyodrębnione wartości (sumy, pola
  wymagane i inne) i oznacza niepowodzenia bezpośrednio na dokumencie, wraz
  z informacją, która reguła zadziałała. Reguły można przetestować „na sucho”
  przed włączeniem, można je włączać per typ dokumentu, a w zestawie dostępny
  jest startowy katalog reguł domyślnych (wszystkie wyłączone do momentu
  włączenia).
- **Reguły transformacji (nowość, per organizacja):** automatyczne
  porządkowanie lub przepisywanie wyodrębnionych wartości pól i tabel podczas
  przetwarzania — konfigurowalne per typ dokumentu lub dla całej organizacji.
- **Wybór układu oparty na regułach (nowość):** układy dokumentów mogą być
  teraz wybierane na podstawie konfigurowalnych reguł, a nie powiązania ze
  źródłem dokumentu. Dotychczasowe zachowanie oparte na źródle jest migrowane
  automatycznie, szablonom układów można zmieniać nazwy, a zduplikowane
  tytuły układów są blokowane.
- **Szybsze eksporty z pulpitu:** eksporty uruchamiane z pulpitu są teraz
  przekazywane do dedykowanego procesu roboczego zamiast czekać na cykl
  odpytywania, dzięki czemu startują natychmiast.
- **Naprawiono blok eksportu wykrywania duplikatów:** blok eksportu dla
  podejrzewanych duplikatów działa ponownie.
- **Ustawienia, które się nie zapisywały:** naprawiono sporadyczne
  niezapisywanie preferencji, gdy istniała starsza, usunięta kopia tego
  samego ustawienia.
- **Dokumenty z nietypowymi znakami:** naprawiono błędy zapisu powodowane
  przez niewidoczne znaki NUL w wyodrębnionych danych.
- **Poprawne pole „Updated by”:** dokumenty przesyłane automatycznie jako
  e-dokumenty nie pokazują już użytkownika systemowego jako ostatniego
  edytora — pole pozostaje puste, dopóki dokumentu faktycznie nie edytuje
  osoba.
- **Zeskanowane pliki PDF z dobrą warstwą tekstową:** nowa opcja pozwala
  DocBits zaufać tekstowi już osadzonemu na zeskanowanej stronie zamiast
  ponownie uruchamiać OCR — szybciej i często dokładniej.
- **E-faktury:** bardziej niezawodne wykrywanie osadzonego XML, gdy oryginalny
  plik wymaga ponownego sprawdzenia.
- **Zadania:** nowy przełącznik organizacji pozwalający użytkownikom
  niebędącym administratorami korzystać z filtra „All” na liście zadań.
- **Dopasowywanie pozycji:** zachowanie dopasowania rozmytego można teraz
  konfigurować dla każdej linii.
- **Stabilność:** połączenia WebSocket zamykają się czysto w przypadku błędów
  zamiast zgłaszać wyjątki serwera; synchronizacja pamięci podręcznej
  uprawnień sama się weryfikuje i naprawia; wersja usługi jest teraz widoczna
  w punkcie końcowym kondycji.

## Auth Service — live: `1.71.1`

- **Logowanie do wielu organizacji:** logowanie pyta teraz, do której
  organizacji wejść, gdy użytkownik należy do kilku; sesje są powiązane z tą
  organizacją, a nowe punkty końcowe obsługują wybieranie, przełączanie
  i ustawianie organizacji domyślnej. Zduplikowane lub konfliktowe
  członkostwa w organizacjach zostały uporządkowane i są teraz blokowane na
  poziomie bazy danych, a wyszukiwanie członkostw jest szybsze.
- **Poprawki organizacji domyślnej:** logowanie automatycznie wybiera
  organizację domyślną użytkownika (a nie dowolną), a zmiana organizacji
  domyślnej działa natychmiast, zamiast pokazywać nieaktualne dane profilu.
- **Naprawiono wylogowanie:** rozwiązano błąd serwera (HTTP 500) przy
  wylogowaniu i przywrócono punkt końcowy unieważniania tokenów.
- **Bezpieczeństwo tokenów:** weryfikacja i buforowanie tokenów uwzględniają
  teraz organizację, dla której token został wydany, a unieważnianie tokenów
  jest scentralizowane.
- **Kanały wydań:** kanał wydań organizacji jest przechowywany w tej usłudze,
  zarządzany przez administratorów organizacji i udostępniany aplikacji oraz
  warstwie routingu.

## Auth Bridge Service — live: `0.2.4.2` _(nowa usługa)_

- **Czym jest:** nowa usługa, która w sposób ciągły replikuje dane
  uwierzytelniania między regionami UE i USA, dzięki czemu konta i logowania
  pozostają spójne między regionami.
- **Samonaprawianie:** usługa wykrywa i naprawia rozbieżności danych między
  regionami — w tym dba o propagację usunięć — oraz automatycznie odzyskuje
  sprawność po utracie połączenia zamiast gubić dane.
- **Bezpieczeństwo i monitoring:** wcześniejsza pętla replikacji
  dwukierunkowej została zatrzymana i jest teraz aktywnie wykrywana
  i blokowana; podłączono śledzenie błędów i alerty; usługa raportuje swoją
  wersję w oknie dialogowym Wersje usług.

## Docflow Service — live: `2.6.1`

- **Karty przepływu pracy akceptują puste wartości:** karty pól wyboru
  i karty partnerów nie kończą się już błędem, gdy pole jest zgodnie
  z prawdą puste; kontrole typów kart są bardziej rygorystyczne
  i przewidywalne.
- **Przepływy pracy uruchamiają się ponownie przy rzeczywistych zmianach:**
  blokada przepływu pracy ponownie respektuje status dokumentu z wyzwalacza,
  a dodatkowo śledzi teraz wersję dokumentu — dzięki czemu dokument, którego
  dane rzeczywiście się zmieniły, może ponownie przejść przez przepływ pracy
  nawet przy tym samym statusie, podczas gdy prawdziwe duplikaty pozostają
  zablokowane.
- **Większe zaawansowane przepływy pracy:** limit węzłów przepływu pracy
  został podniesiony i można go teraz konfigurować dla każdego środowiska.
- **Eksport alternatywny:** eksporty alternatywne wyzwalane przez przepływ
  pracy są teraz odpowiednio oznaczane, aby systemy docelowe mogły je
  rozróżnić.
- **Odporność:** usługa automatycznie łączy się ponownie, gdy połączenie
  z bazą danych zostanie zerwane w trakcie użycia, toleruje wolniejszego
  brokera komunikatów zamiast kończyć się błędem, a nieudane żądania API są
  teraz rejestrowane z pełnym kontekstem i możliwymi do prześledzenia
  identyfikatorami wykonania.

## Email Service — live: `1.38.4`

- **Dziennik importu przebudowany pod kątem identyfikowalności:** każda
  zaimportowana wiadomość e-mail rejestruje teraz, które dokumenty zostały
  z niej utworzone, wraz ze szczegółowymi wierszami dla poszczególnych
  załączników.
- **Pobieranie oryginalnej wiadomości e-mail:** oryginalną wiadomość można
  pobrać jako plik `.eml` bezpośrednio z dziennika importu.
- **Odzyskiwanie załączników:** ścieżka odzyskiwania po uszkodzeniu obsługuje
  teraz także wiadomości w formacie zwykłego tekstu, dzięki czemu więcej
  uszkodzonych wiadomości przychodzących jest odzyskiwanych zamiast
  pomijanych.

## Extraction Service — live: `1.51.6`

- **Podatek i netto już niezamieniane:** naprawiono przypadek na dokumentach
  z USA, w którym kwota podatku mogła zostać przypisana jako większa niż
  kwota netto, gdy znaleziono kilka kandydujących par.
- **Wiele stawek podatku u jednego dostawcy:** ekstrakcja obsługuje teraz
  dostawców, których faktury zawierają różne stawki podatku na jednym
  dokumencie.
- **Ekstrakcja tabel z użyciem AI (nowość, opcjonalna):** ustrukturyzowane
  punkty końcowe ekstrakcji AI dla tabel, aktywowane per organizacja za
  pomocą flagi funkcji.
- **Szybsze wywołania AI:** dostrojono konfigurację modelu AI używanego
  podczas ekstrakcji, aby uniknąć zbędnego czasu przetwarzania.
- **Naprawiono awarię:** rozwiązano błąd na dokumentach, które podczas
  ekstrakcji generowały pustą listę kandydatów.

## Fulltext Service — live: `1.37.2`

- **Naprawiono migracje indeksu wyszukiwania:** przywrócono definicje
  migracji, które uległy rozsynchronizowaniu, dzięki czemu aktualizacje
  indeksu wyszukiwania pozostają niezawodne.
- Wewnętrzne prace nad routingiem dla nowej infrastruktury kanałów wydań.

## PO Match Service — live: `1.58.2`

- **Bardziej tolerancyjne dopasowywanie:** dopasowywanie PO nie kończy się już
  błędem przy nietypowych danych — nietekstowe numery pozycji, brakujące
  ilości i nietekstowe wartości kwot są teraz obsługiwane poprawnie zamiast
  powodować błędy.

## Web App — live: `10.41.8`

- **Obsługa wielu organizacji:** nowa strona wyboru organizacji przy
  logowaniu, dedykowana ikona przełącznika organizacji w nagłówku, ustawienia
  organizacji domyślnej, a aplikacja podąża za regionem aktywnej organizacji.
  Logowanie do niewłaściwego regionu po cichu ponawia próbę we właściwym
  regionie i w razie potrzeby kieruje do strony wyboru organizacji.
- **Koniec z niekończącymi się przeładowaniami:** naprawiono nieskończoną
  pętlę przeładowań, która mogła wystąpić, gdy serwer odrzucił zapisany token
  sesji — aplikacja wymusza teraz rzeczywiste odświeżenie tokenu zamiast
  przeładowywać się w nieskończoność.
- **Naprawiono Layout Builder:** Layout Builder znów działa, a wybór układu
  został oddzielony od źródła dokumentu (zgodnie z nowym wyborem opartym na
  regułach w API).
- **Tabele ekstrakcji:** tabele pozycji mają teraz przeciągany uchwyt zmiany
  rozmiaru, dzięki czemu podczas walidacji można dać tabeli więcej miejsca.
- **Dziennik importu e-mail:** nowy status pominięcia i oznaczenia podziału,
  rozwijane wiersze dla poszczególnych załączników, pobieranie oryginalnej
  wiadomości e-mail oraz przyciski z identyfikatorami dokumentów przenoszące
  bezpośrednio na pulpit przefiltrowany do danego dokumentu.
- **Wyszukiwanie na pulpicie:** lista rozwijana wartości zapytania pokazuje
  teraz zlokalizowaną etykietę dla pól typu lista wartości, a przykłady
  w pomocy wyszukiwania zostały przebudowane.
- **Niezawodność ustawień:** preferencje użytkownika ładują się teraz
  niezawodnie przy logowaniu przez SSO, a potwierdzenie zapisu jest
  wyświetlane tylko wtedy, gdy zapis faktycznie się powiódł.
- **Zadania:** filtr „All” można przywrócić użytkownikom niebędącym
  administratorami za pomocą nowego przełącznika organizacji.
- **Logi Watchdog:** nie są już ograniczone do 10 000 wpisów, plus ogólne
  usprawnienia użyteczności.
- **Zgłoszenia do pomocy technicznej:** formularz pomocy technicznej wstępnie
  wypełnia adres e-mail z profilu użytkownika.
- **Ustawienia typu dokumentu:** nowe pole wyboru „Use AI” na tabelach
  i kolumnach do sterowania ekstrakcją tabel wspomaganą przez AI.
- **Okno dialogowe Wersje usług:** nowa kolumna *Release* pokazująca kanał
  każdej usługi (frozen/latest), z routingiem zapewniającym szybkość
  działania dla przypiętych organizacji.
- **Walidacja pól:** naprawiono błąd przy powrocie do Walidacji pól z innego
  ekranu, a przycisk „Scripts” nie prowadzi już do strony 404.

---

## Wyłącznie zmiana numeracji wersji (bez zmian funkcjonalnych)

**Auto Accounting** (`1.20.1`), **Barcode Service** (`1.17.1`), **OCR
Service** (`1.9.1`), **FTP Service** (`1.31.1`), **Operator Service**
(`1.40.2`) oraz **Ideas Service** (`0.3.1`) otrzymały nowe numery wersji
w ramach nowej infrastruktury kanałów wydań. Ich pozornie większe skoki
wersji nie niosą w tym okresie żadnych zmian funkcji ani zachowania.
**Docnet Service** (`1.54.6`) pozostaje bez zmian od 19 czerwca.

<!-- Generated by the docbits-changelog skill (version-boundary mode: exact
     git ranges between the ALT (2026-07-03/04) and NEU (2026-07-09..13)
     version-bump commits supplied by the user, per service). -->
