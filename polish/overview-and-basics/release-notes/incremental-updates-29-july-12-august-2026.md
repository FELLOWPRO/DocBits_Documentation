# Informacje o wersji DocBits — 29 lipca – 12 sierpnia 2026

_Co zmieniło się w produkcyjnej aktualizacji DocBits wdrożonej 10–12 sierpnia
2026, obejmującej wszystko od wydania z 29 lipca. Każda usługa pokazuje
wersję, która trafiła na produkcję, a następnie opisuje nowości i poprawki
prostym językiem. Usługi niewymienione poniżej (Auto Accounting `1.21.1`,
Ideas `0.3.1`, OCR `1.10.3`, Operator `1.42.1`, PO Match `1.59.3`,
FTP `1.32.4`) nie miały żadnych zmian widocznych dla klientów._

---

## Najważniejsze zmiany

- **Obsługa FacturaE.** Hiszpańskie e-faktury FacturaE 3.1 są klasyfikowane
  i ekstrahowane od razu po wdrożeniu, z pełnymi mapowaniami pól. W tej samej
  fali mapowania ebInterface (Austria) stały się wierne wersjom, domyślne
  mapowania Factur-X i ZUGFeRD otrzymały ścieżkę nazwy firmy, a kilka
  błędnych domyślnych mapowań rabatów, VAT i cen jednostkowych zostało
  poprawionych.
- **Naprawione wyszukiwanie i sortowanie na pulpicie.** Sortowanie nie zależy
  już od tego, które kolumny akurat są widoczne, filtr OR połączony
  z warunkiem zakresu lub równości nie kasuje już fraz wyszukiwania, nazwy
  dostawców znów pokazują się w szybkim wyszukiwaniu, a daty w formacie ISO
  są odczytywane poprawnie.
- **Ekstrakcja AI koryguje się sama.** Możliwa do udowodnienia zamiana kwoty
  netto i kwoty łącznej dokonana przez AI jest cofana automatycznie, pola
  skanowane przez AI nie wracają już błędne po restarcie dokumentu,
  a ekstrakcja tabel AI przetwarza dokumenty w partiach stron, więc długie
  tabele docierają w całości.
- **Workflow przeżywają chwilową awarię uwierzytelniania.** Chwilowo
  nieosiągalna usługa uwierzytelniania jest ponawiana, zamiast oblewać
  przebieg, a wyzwalacz workflow, który nie może się uwierzytelnić, raportuje
  błąd, zamiast zostawiać dokument w zawieszeniu.
- **Trudne do odczytania pliki PDF znów się ekstrahują.** Gdy standardowy
  dekoder tekstu PDF nie może odczytać strony (częste w plikach wytworzonych
  przez Ghostscript), ekstrakcja przełącza się na drugi silnik, zamiast nie
  zwracać niczego.
- **MFA działa między regionami.** Dane rejestracji drugiego składnika są
  replikowane między regionami UE i USA, więc drugi składnik skonfigurowany
  w jednym regionie jest honorowany w drugim.

---

## Web App — `10.49.4`

### Logowanie i konta

- Wylogowanie w jednej karcie przeglądarki wylogowuje też pozostałe karty —
  bez komunikatów o błędach, które pojawiały się wcześniej, gdy karty nie
  zgadzały się co do stanu sesji.
- Zmiana własnego hasła w profilu przechodzi przez dedykowany endpoint
  samoobsługowy, więc działa bez uprawnień administratora.
- Logowanie kluczem dostępu (passkey) z regionu innego niż macierzysty
  pokazuje przetłumaczone komunikaty o błędach, a jego przycisk wysłania
  jest widoczny.

### Ekran walidacji

- Zakładka „Extracted table” nie kręci się już w nieskończoność, gdy tabela
  AI już istnieje.
- Dokumenty, którym brakuje danych kodów kreskowych, nie psują już widoku
  przypisywania kodów kreskowych.
- Wielopodatkowe linie M3 oferują kod podatkowy jako listę rozwijaną
  zasilaną z listy wartości zamiast pola tekstowego.
- Otwieranie dużych faktur dostawców jest zauważalnie szybsze.

### Zadania

- Kolumny Kanban doładowują się podczas przewijania, więc tablice z wieloma
  zadaniami wczytują się szybko.
- Licznik otwartych zadań na pasku bocznym liczy zadania w kontekście
  bieżącej podorganizacji, a nie w kontekście akurat otwartego dokumentu.

### Workflow Builder

- Lista workflow zachowuje wyszukiwanie, kolejność sortowania, stronę
  i rozmiar strony po otwarciu workflow i powrocie, także przez ścieżkę
  nawigacyjną (breadcrumb), a strona otwiera się domyślnie na zakładce List.

### Ustawienia i administracja

- Strona danych podstawowych (Master Data) nie otwiera się już pusta
  z powodu wyścigu sortowania, a sortowanie po plakietkach nie zawiesza już
  strony.
- Subskrypcję w stanie „cancelling” można wznowić.
- Strona szczegółów XSLT raportuje błędy wczytywania, zamiast nie pokazywać
  nic, a ustawienia powiadomień e-mail wykorzystują pełną szerokość strony
  z działającym panelem logów.
- Selektor organizacji dla użytkowników pracujących w wielu organizacjach ma
  poprawny układ wierszy, rozmiary i kolory motywu, przewija się prawidłowo
  i oferuje filtr dla kont z wieloma organizacjami.
- Analityka: nieudane żądanie metryk pokazuje stan błędu, zamiast renderować
  zera, a widżety zużycia raportują uczciwie, gdy brak danych pomiarowych.
- Przestarzałe opcje bufora zostały usunięte ze strony zarządzania buforem,
  a strony Users i Groups pozbyły się zagnieżdżonych podwójnych pasków
  przewijania.
- „Use Default Template” w menedżerze layoutów nie kończy się już awarią ani
  nie pozostaje martwe; przestaje też twierdzić, że domyślny layout nie
  istnieje.
- Reguły wyboru zachowują operatory dopasowania tekstu, obecności i wyrażeń
  regularnych po ponownym otwarciu reguły.
- Typy dokumentów obsługują reguły transformacji per typ, a interfejs listy
  reguł zyskał akcję ustawiania stałej wartości (fix value).
- Plakietki statusu zamówień zakupu mapują się poprawnie dla wartości
  statusów pisanych w konwencji ERP.
- Ekrany DocNet (AI Workforce), łącznie z Agent Wizard, są przetłumaczone,
  a okno dodawania/edycji pomysłu przewija się poziomo.
- Oferty w portalu dostawców: zarządzane jednostki miary pokazują się
  w tabeli pozycji, stylowanie zatwierdzeń dotyczy wyłącznie ofert
  kontraktowych, a linia porównania nie pojawia się już, gdy obie wartości
  są identyczne.
- Awaryjny widok JSON na stronie błędu jest czytelny w trybie ciemnym,
  a raporty używają poprawnej etykiety „ostatnie 7 dni” zamiast samotnego
  „7”.

## API Service — `12.74.0`

### Pulpit i wyszukiwanie

- Sortowanie działa niezależnie od tego, które kolumny są widoczne, a słowo
  kluczowe delegowane przez wyszukiwanie do wyszukiwania pełnotekstowego nie
  zostawia już po sobie uszkodzonego fragmentu SQL.
- Nazwy dostawców znów pojawiają się w szybkim wyszukiwaniu dla organizacji
  bez indeksowania pełnotekstowego.
- Daty w formacie ISO (2026-08-12) nie są już błędnie odczytywane przez
  normalizator dat zaczynający od dnia.
- Eksporty pulpitu kierują surowe wartości tekstowe, takie jak numery
  faktur, do właściwej kolumny.

### E-faktury

- FacturaE 3.1 (Hiszpania): reguła klasyfikacji i kompletne mapowania pól.
- Reguły klasyfikacji XRechnung są zakotwiczone w swojej rodzinie składni,
  więc dokument UBL nie jest już dopasowywany przez reguły CII i odwrotnie.
- Akceptowana wersja „3.0” obejmuje całą swoją rodzinę poprawek (3.0.1,
  3.0.2).
- Faktury CII przyjmują prawną nazwę dostawcy, używając nazwy handlowej
  tylko jako zapasowej.
- Mapowania ebInterface (Austria) są wierne wersjom, z poprawioną regułą
  zbiorczą (catch-all) i przebudowanymi zestawami danych testowych.
- Domyślne mapowania Factur-X i ZUGFeRD otrzymały ścieżkę ekstrakcji nazwy
  firmy, poprawiono domyślne transformacje nagłówka dla stawki podatku, typu
  faktury i pól trzeciego poziomu, a także semantykę rabatów, VAT i cen
  jednostkowych w całej rodzinie.
- Źródłowe kody kategorii podatkowych nie są już ślepo mapowane na kody
  Twojego ERP.
- Dokumenty wspominające zarówno o „fakturze”, jak i „fakturze korygującej”
  preferują klasyfikację jako faktura korygująca.

### Dokumenty i ekstrakcja

- Gdy standardowy dekoder PDF nie może odczytać osadzonego tekstu strony,
  ekstrakcja przełącza się na drugi silnik, więc dotknięte pliki PDF
  ekstrahują się, zamiast wracać puste.
- Główny przełącznik kodów kreskowych to teraz `BARCODE_EXTRACTION`; stare
  ustawienie kodów QR nadal działa jako alias.
- Zatkano wyciek pamięci w harmonogramie zadań w tle; powoli degradował on
  przetwarzanie w miarę dni działania usługi.
- Dostawcy importowani bez kraju pozostają z pustym polem, zamiast domyślnie
  otrzymywać Niemcy.

### Eksport i dane podstawowe

- Save Rules raportuje niepowodzenie, gdy niczego nie zapisze, zamiast
  twierdzić, że się udało.
- Linie z kwotą zero nie są już pomijane w eksportach automatycznego
  księgowania, a filtr, który pasował do każdego przedziału, został
  naprawiony.
- Eksporty M3 obsługują post-hooki informacji dodatkowych.
- Jedna nieudana sonda zbioru danych nie wygasza już całego ekranu danych
  podstawowych (Master Data).
- Bufory PO są unieważniane, gdy ERP aktualizuje status zamówienia zakupu,
  więc pulpit przestaje pokazywać nieaktualny stan.

### Administracja

- Każda preferencja pokazuje, który użytkownik zmienił ją jako ostatni.
- Reguły ekstrakcji można usuwać według dostawcy i klonować przez nowe
  endpointy.
- Adresaci e-maili alertów statusu są porównywani w sposób odporny na NULL,
  co naprawia awarię w dostarczaniu powiadomień.

## Auth Service — `1.75.9`

- Klucz API organizacji użyty wobec niepowiązanej organizacji jest
  odrzucany.
- Tworzenie organizacji zwracało błąd, choć faktycznie zapisywało wiersz;
  teraz odpowiada poprawnie.
- Logowanie kluczem dostępu, gdy żaden nie jest zarejestrowany, zwraca
  własny kod błędu, więc ekran logowania może powiedzieć, co jest nie tak.

## Auth Bridge Service — `0.4.2`

- Tabele rejestracji drugiego składnika są replikowane między regionami UE
  i USA, a wiersze są identyfikowane po swoim rzeczywistym kluczu głównym.

## Docflow Service — `2.8.7`

- Wyzwalacz workflow, który nie może się uwierzytelnić, raportuje
  niepowodzenie, zamiast zostawiać dokument w zawieszeniu, a chwilowo
  nieosiągalna usługa uwierzytelniania jest ponawiana, zamiast być
  traktowana jak zły token.
- Karty porównania ofert: numery pozycji są porównywane tylko dla linii
  opisanych przez macierz cen pozycji, a linie bez jednostki miary lub bez
  ceny są pomijane, zamiast oblewać porównanie.
- Karta porównania cen kontraktowych zyskała opcję operatora any/all,
  a bufory kart są unieważniane poprawnie po migracjach i aktualizacjach
  kodu.
- Zerwane połączenia SSL są traktowane jako przejściowe i ponawiane, zamiast
  oblewać przebieg.

## Docnet Service — `1.56.4`

- Endpointy stanu i wersji nie blokują się już na kontrolach na żywo, co
  wcześniej zawieszało okno Service Versions.

## Email Service — `1.40.6`

- Gdy przychodzący e-mail zostaje pominięty, powód jest pokazywany w wierszu
  zdarzenia importu, zamiast pozostawać niewidoczny.
- Załączone pliki kontenerowe `.eml` nie są już importowane jako dokumenty.
- Nieudane logowanie Microsoft Office daje czytelny komunikat o błędzie,
  a błąd transportu z usługi AI liczy się jako „niejednoznaczne”, a nie jako
  odrzucenie.

## Extraction Service — `1.53.8`

- Możliwa do udowodnienia zamiana kwoty netto i kwoty łącznej dokonana przez
  AI jest cofana po ekstrakcji pól, a niepowodzenia tej kontroli są
  logowane, zamiast przechodzić po cichu.
- Pola skanowane przez AI nie wracają już błędne po restarcie dokumentu.
- Ekstrakcja tabel AI dzieli pracę na partie stron i kumuluje wszystkie
  partie, więc długie tabele docierają w całości.
- Dokumenty wspominające zarówno o „fakturze”, jak i „fakturze korygującej”
  preferują klasyfikację jako faktura korygująca.
- Powtarzalne czyszczenie nagłówków i stopek jest buforowane, co przyspiesza
  ekstrakcję dokumentów wielostronicowych.

## Fulltext Service — `1.41.7`

- Filtr OR połączony z warunkiem zakresu lub równości nie kasuje już fraz
  wyszukiwania.
- Sortowanie używa poprawnych ścieżek indeksu i pokazuje rzeczywisty powód,
  gdy backend wyszukiwania odrzuci zapytanie; regresję sortowania, która
  całkowicie zepsuła wyszukiwanie raw-query, naprawiono w tym samym
  tygodniu, w którym się pojawiła.
- Wyszukiwanie dokumentów działa na starszych indeksach z mapowaniem
  tekstowym.
- Bufor tokenów jest zakresowany do pary token–organizacja, więc
  przełączenie organizacji nie może podać wyników z poprzedniego kontekstu.
