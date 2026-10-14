# Informacje o wersji DocBits — 14 października 2026

_Co zmienia się w produkcyjnym hotfixie DocBits z 14 października 2026 (wydanie
R1.0.15), obejmującym wszystko od [hotfixu z 15 września](incremental-updates-15-september-2026.md).
Każda usługa pokazuje wdrażaną wersję, a następnie opisuje nowości i poprawki
prostym językiem. Usługi niewymienione poniżej nie miały żadnych zmian
widocznych dla klientów._

{% embed url="https://docbits-videos.fra1.cdn.digitaloceanspaces.com/release-notes/2026-10-14/pl.mp4" %}

---

## Najważniejsze zmiany

- **Settings Assistant.** Pasek czatu na każdej stronie ustawień odpowiada na
  pytania o konfigurację Twojej organizacji, w Twoim języku i na podstawie
  dokumentacji DocBits. Odczytuje aktualny stan ustawień i go wyjaśnia
  (uprawnienia grup, kanały importu, przełączniki zamówień zakupowych,
  księgowanie). Gdy poprosisz o włączenie lub wyłączenie czegoś, najpierw
  pokazuje podgląd, czeka na Twoje potwierdzenie i oferuje cofnięcie.
  „Otwórz ustawienie” przenosi bezpośrednio do ustawienia, nawet w zwiniętej
  sekcji, i je podświetla. Administratorzy organizacji włączają i wyłączają
  asystenta w Informacjach o firmie. Odpowiada wyłącznie na pytania o DocBits
  i nigdy nie zmienia niczego bez potwierdzenia.
- **Nowe poziomy AI.** Poziomy Fast i Full działają na nowych modelach. Nowy
  poziom Auto wybiera Fast lub Full dla każdego dokumentu, a Nexus Flash
  dołącza do Nexus. Tryb wizyjny (hybrydowy lub automatyczny) decyduje, kiedy
  razem z tekstem wysyłany jest obraz strony. Zapisane preferencje modeli AI
  same przechodzą na nowe poziomy, a ekrany pokazują wyłącznie nazwy poziomów.
  „Użyj AI” to lista rozwijana (Standard, Tak, Nie) z podglądem tego, o co
  zapyta ekstrakcja strukturalna.
- **Kontrola pól nagłówka.** Ekran walidacji ma przycisk „Kontrola pól
  nagłówka” obok Zapisz. Jego raport wymienia każde pole nagłówka wraz ze
  źródłem wartości (AI, reguła, skrypt lub dane podstawowe), w zwartej tabeli
  z filtrem źródła, wyszukiwaniem i sortowaniem, z tymi samymi etykietami pól
  co ekran walidacji. Okno pochodzenia pokazuje źródło każdej wartości w
  jednym pasku.
- **Bezpieczeństwo logowania i organizacji.** Wyzwanie MFA można wykorzystać
  tylko raz na każdej ścieżce logowania, a zarejestrowanie aplikacji
  uwierzytelniającej wymaga kodu z e-maila. Organizacje posiadają listę
  zweryfikowanych domen e-mail; logowanie społecznościowe (na przykład
  przez Microsoft) dołącza do organizacji, która wymienia daną domenę, i
  nigdy samo nie tworzy organizacji, użytkownika ani subskrypcji. Tylko
  administratorzy organizacji zmieniają preferencje organizacji oraz
  zapisują lub zatwierdzają reguły dopasowywania zamówień zakupowych.
  Odpowiedzi z pamięci podręcznej nie mogą już wyciekać między
  organizacjami.
- **Dopasowywanie zamówień zakupowych i opłaty.** Opłaty, które zamówienie
  zakupowe przewiduje jako zerowe, mają bezwzględny próg, tolerancja opłat
  obejmuje także opłaty, których zamówienie nie budżetuje, a jedno pole może
  wymieniać kilka elementów kosztowych, których kwoty są dzielone
  proporcjonalnie do zamówienia zakupowego. Kolumna dopasowania może mieć
  flagę „zezwól na niezgodność”. Karty workflow porównują opłaty dla każdej
  listy, a limit wykonań workflow rośnie z 30 do 50.
- **Mniej błędnych liczb.** Kwoty są wyświetlane w osobistym formacie każdego
  użytkownika (w tym w Szwajcarii i Słowenii), wartości zawierające tylko datę
  zachowują dzień kalendarzowy w każdej strefie czasowej, równanie sumy dla USA
  uwzględnia kwoty dodatkowe i faktury z wieloma podatkami, a dokumenty z
  kwotami nagłówka 0,00 nie trafiają już do niewłaściwego przebiegu
  kandydatów.

---

## Naprawiono również w tym wydaniu

- Pulpit nie pozostaje już pusty, gdy wyścig ustawia filtr podorganizacji na
  identyfikator organizacji i tym samym wyklucza wszystkie dokumenty.
- Wartości wymiarów można znów wybierać dla każdego użytkownika.
- Naprawiono błąd przesyłania zgłoszony przez klienta.
- „Dopasuj na podstawie sumy” działa dla dostawców, których faktura ma jedną
  pozycję, oraz dla konfiguracji dostawców, które to zgłosiły.
- E-dokumenty SPS: dostosowano opłaty 810, zaktualizowano układ opłat 855 i
  poprawiono logo klienta w podglądzie e-dokumentu.

---

## Web App — `10.78.9.4`

**Settings Assistant**
- Wysuwany panel czatu po prawej stronie z przełącznikiem znajduje się na
  wszystkich stronach ustawień. Rozmowa przetrwa zmianę strony, jest
  ograniczona do 20 wiadomości i pokazuje wprowadzone zmiany wraz z
  możliwością cofnięcia.
- Wita pytaniami pasującymi do bieżącej strony ustawień i pokazuje karty
  ustawień z przełącznikiem włącz/wyłącz. Esc najpierw zamyka menu, Stop
  przerywa trwającą odpowiedź, a zrzuty ekranu w odpowiedziach otwierają się w
  powiększeniu.
- Zastosowanie zmiany otwiera okno z podglądem, potwierdzeniem i cofnięciem.
- Każde ustawienie można wyszukać z paska bocznego, a znalezione ustawienie
  jest podświetlane innym kolorem. „Otwórz ustawienie” przewija do celu
  wewnątrz zwiniętego akordeonu.
- Przełącznik asystenta dla administratora organizacji znajduje się w
  Informacjach o firmie.
- Porady AI są przypisane do Nova, a pojawiają się wyłącznie nazwy poziomów,
  nigdy identyfikatory modeli.

**Ekran walidacji i obsługa dokumentów**
- Nowy przycisk „Kontrola pól nagłówka” z raportem, pochodzeniem każdego pola
  i stroną pomocy (zob. Najważniejsze zmiany). Etykiety źródeł i znaczniki
  statusu mieszczą się w swoich komórkach.
- Tekstowe znaczniki „z danych podstawowych” obok etykiet pól zniknęły;
  informację tę zawiera okno pochodzenia.
- Wszędzie działa jedna wspólna walidacja pól, co usuwa ogólny błąd „Jedno lub
  więcej pól wymaga walidacji” po Auto Accounting.
- Podpowiedzi na przyciskach okna pola (Usuń, Wyczyść, Potwierdź) mówią, co
  każdy z nich robi, zanim klikniesz.
- Wiersz optymistyczny pokazuje teraz to, co zostało zapisane, a nie to, co
  wpisano. Ponowne przypisanie kolumny prosi o potwierdzenie tylko wtedy, gdy
  widoczna kolumna traci swoje przypisanie.
- Strony poza limitem stron OCR są tylko do odczytu i oznaczone, także w
  podglądzie Auto Accounting. Stary panel ograniczeń stron importu został
  wycofany.
- Tabela PO pojawia się dla każdego numeru zamówienia zakupowego w polu
  nagłówka z wieloma PO, a Layout Builder nazywa karty PO według klucza
  tabeli PO i nie zgłasza już modułu jako wyłączonego, gdy tabela PO jest
  włączona.
- Karta propozycji wypisuje tolerancję zamiast `[object Object]`, a ekran
  porównania zatwierdzania przestaje zaokrąglać skonfigurowane kolumny
  porównania (numery artykułów).

**Konta, ustawienia i błędy**
- Każdy komunikat o błędzie i błąd logowania pokazuje identyfikator śledzenia
  nieudanego żądania, dzięki czemu wsparcie może go znaleźć. Błędy WebSocket
  pulpitu odrzucają dokładnie to żądanie, które nazywają.
- Informacje o firmie wymieniają domeny e-mail organizacji.
- Administratorzy mogą ponownie wysłać e-mail „Ustaw hasło” ze strony
  użytkownika.
- Administratorzy globalni ustawiają początek umowy w tabeli subskrypcji.
- Administratorzy organizacji widzą zakładkę Executive Dashboard oraz
  przyciski dodawania i usuwania XSLT. Członkowie zapisują layouty jako
  własną preferencję.
- Sesja bez organizacji otrzymuje czytelny komunikat o błędzie i wybór
  organizacji zamiast pustego pulpitu.
- Kwoty podążają za osobistym formatem liczb użytkownika, a wartości
  zawierające tylko datę zachowują swój dzień w każdej strefie czasowej.
- Dane podstawowe wysyłają identyfikatory podorganizacji tylko wtedy, gdy
  różnią się od identyfikatora organizacji, a niestandardowe nagłówki danych
  podstawowych są wysyłane jako nagłówki.
- Maska Tabele nie przycina już listy rozwijanej „Użyj AI”, tekst podpowiedzi
  AI nie zasłania już wiersza treningu, a tabela AI zachowuje swój
  bezpośredni przycisk Zastosuj, z ikoną kontroli nagłówka w samym nagłówku i
  komunikatem o licencji.
- Ikony ekstrakcji tabel znów się wyświetlają po usunięciu starej czcionki
  ikon.

**Tablica zadań**
- Tablica ładuje pierwszą stronę z mniejszą liczbą zduplikowanych żądań,
  Enter od razu uruchamia wyszukiwanie, spóźnione odpowiedzi są przypisywane
  do właściwego wyszukiwania, stopka pokazuje rzeczywistą liczbę trafień
  zamiast pojemności strony, a usuwanie rozpoczęte w jednej organizacji jest
  anulowane przed wysłaniem, gdy zmienisz organizację.

---

## API Service — `12.83.293`

**Settings Assistant i MCP**
- Punkt końcowy czatu z zabezpieczeniami: tylko pytania o DocBits, żadnych
  zmian bez potwierdzenia, niejasne pytania lub pytania ogólne otrzymują
  pomoc zamiast odmowy, a odpowiedzi są strumieniowane: najpierw karty, potem
  tekst.
- Elementy tylko do odczytu dla każdego obszaru ustawień (uprawnienia grup,
  kanały importu, dopasowywanie PO, księgowanie, domeny e-mail), katalog
  linków bezpośrednich z narzędziem wyszukiwania ustawień oraz wyszukiwanie w
  dokumentacji DocBits z obrazami.
- Przepływ zastosowania, fala 1: podgląd, potwierdzenie i cofnięcie dla
  obsługiwanych ustawień, jedna reguła zakresu dla wszystkich trzech,
  zabezpieczona przed podwójnym potwierdzeniem i wygaśnięciem.
- Narzędzia MCP nigdy nie odczytują plików z serwera w trybie zdalnym, a
  narzędzia fixture i lab działają tylko na dev.

**AI**
- Nowe modele za poziomami Fast i Full, poziom Auto, Nexus Flash oraz
  preferencja trybu wizyjnego. Zapisane preferencje `AI_MODEL` są przenoszone
  na nowe poziomy.
- „Użyj AI” dokumentuje, o co prosi ekstrakcja strukturalna.

**Bezpieczeństwo i izolacja**
- Tylko administratorzy organizacji zmieniają preferencje organizacji.
- Wywołanie `/accounting/rebuild` trenuje wyłącznie organizację
  wywołującego, przy nieudanym wyszukaniu organizacji kończy się odmową i
  odpowiada 400 dla błędnego identyfikatora.
- Renderowanie XSLT, XML i PDF odmawia dostępu do plików i sieci, nie
  rozwiązuje zewnętrznych dołączeń, a bajty faktury są oczyszczane, zanim
  trafią do transformatora. Renderowane podglądy PDF dopuszczają wyłącznie
  zaufane hosty obrazów.
- Klucze pamięci podręcznej zawierają organizację, a ten sam identyfikator
  zawsze daje ten sam klucz, więc obcy identyfikator organizacji nie może już
  odczytać danych z pamięci podręcznej. Czyszczenie pamięci podręcznej
  pulpitu całej organizacji przy każdej zmianie dokumentu zostało usunięte.
- Lista domen e-mail organizacji jest przekazywana do Auth.

**Dopasowywanie zamówień zakupowych i eksport**
- Pole może wymieniać kilka elementów kosztowych, których kwoty są dzielone
  proporcjonalnie do PO.
- Zastępcy w zatwierdzaniu łączą się z aktywnym wnioskiem o zatwierdzenie,
  zapisy naprawionych zatwierdzeń już nie blokują, a dokument oczekujący na
  zatwierdzenie jest odrzucany przy eksporcie.
- Adnotacja PDF/A zachowuje katalog i osadzony XML, dzięki czemu e-faktury po
  adnotacji zachowują swój XML. Faktury UBL z samym identyfikatorem
  CustomizationID EN 16931 są klasyfikowane (sieć e-faktur).
- GRPR zaokrągla do 6 miejsc po przecinku, które akceptuje M3. Współczynniki
  konwersji podstawowej jednostki miary są dodawane do zamrożonej pozycji.
- Usunięte miękko treningi i reguły formatowania są respektowane, a
  `update_document_fields` w MCP nie potwierdza już zapisu, który został
  utracony. `get_table_rules` odpowiada typowanym brakiem trafienia, a pusty
  ładunek tłumaczeń używa swojej wartości zastępczej.
- Słoweńskie kwoty używają `sl_SI`, a zapisane preferencje są migrowane.
  Niestandardowe etykiety klasyfikacji wysyłane jako identyfikatory UUID są
  rozpoznawane. Udostępnione pulpity zachowują `created_by` i listę
  udostępnień przy aktualizacji.
- Ramki błędów pulpitu zawierają `request_id` żądania, a każda nieudana
  odpowiedź JSON zawiera identyfikator śledzenia.
- System restartuje tylko niezdrowe workery zamiast całej floty API i
  poprawnie sprawdza zarejestrowaną listę zadań. Kolejka monitora zawieszeń
  jest znów konsumowana.

---

## Auth Service — `1.78.49`

- Wyzwanie uwierzytelniania wieloskładnikowego jest jednorazowe na każdej
  ścieżce logowania, nie tylko w przepływie MCP. Rejestracja wymaga kodu z
  e-maila, po logowaniu ze wspólnym hasłem nie jest wydawany token
  rejestracji, a użytkownicy są powiadamiani o zarejestrowaniu składnika.
- Organizacje posiadają listę domen e-mail, z których każdą można przypisać
  tylko raz. Logowanie społecznościowe dołącza do organizacji, która wymienia
  zweryfikowaną domenę, nigdy nie tworzy organizacji, użytkownika ani
  subskrypcji i odmawia bez wskazywania kogokolwiek, a administratorzy są
  zamiast tego informowani. Obsługiwane są domeny zwracane przez Microsoft.
- Każde odrzucone logowanie zawiera identyfikator śledzenia. Administratorzy
  mogą ponownie wysłać e-mail „Ustaw hasło”. Saldo umowy ma znak, a początek
  umowy jest audytowany.

## Auth Bridge — `0.5.7`

- Replikacja kont EU i US utrzymuje zasilanie połączenia podczas uzgadniania,
  sama ponownie podłącza porzucony slot replikacji, używa ograniczonej
  pamięci i traktuje istniejące źródło replikacji jako sukces. Logowanie
  między regionami jest bardziej niezawodne.

## Docflow Service — `2.10.22`

- Oddzielna karta ceny jednostkowej odczytuje domyślne definicje pól
  organizacji dla opłat i porównuje każdy element kosztowy wymieniony w
  polu.
- Limit wykonań workflow rośnie z 30 do 50, a wyszukiwania w logach workflow
  odrzucają identyfikator, który nie jest UUID.

## Docnet Service — `1.56.15`

- `list_document_fields` raportuje każdą skonfigurowaną kolumnę tabeli, także
  puste.

## Extraction Service — `1.56.0.1`

- Poziomy: nowe modele za Fast i Full, Auto, Nexus Flash oraz tryb wizyjny.
  Żądania wizyjne do hosta wnioskowania mieszczą się w jego limicie rozmiaru.
- Ekstrakcja tabel z Nexus grupuje strony w partie (po dwie), uruchamia partie
  równolegle z zmierzonym limitem czasu, ponawia przejściowe błędy i dzieli
  partię, która przekroczyła limit czasu. Pola nagłówka są odczytywane ze
  wszystkich partii.
- Sumy dla USA: kwoty dodatkowe wchodzą do równania sumy, para 1 liczy się w
  zabezpieczeniu pary 2, kandydaci z niskim wynikiem są pomijani, gdy podatki
  nie są zerowe, a „above” i „below” pasują do etykiet wielowyrazowych.
- Pola identyfikatorów naprawiają znaki, które naprawdę występują, a znaki
  niewidoczne są traktowane według tego, co oznaczają, więc „O” nie zamienia
  się już w dziwny znak.

## Fulltext Service — `1.42.41`

- Nowy indeks dokumentacji DocBits z punktami końcowymi wczytywania i
  wyszukiwania, obrazami w odpowiedziach i limitem czasu dla całego
  wyszukiwania. Zasila Settings Assistant.

## PO Match Service — `1.59.48`

- Bezwzględny próg dla opłat, które zamówienie zakupowe przewiduje jako
  zerowe, oraz tolerancja opłat dla opłat, których zamówienie nie budżetuje.
- Kolumna może mieć flagę „zezwól na niezgodność”. Kilka elementów
  kosztowych na pole jest dzielonych proporcjonalnie.
- Tylko administratorzy organizacji zapisują lub zatwierdzają reguły
  dopasowywania, a warunki reguł akceptują wyłącznie gramatykę wyrażeń z białej
  listy.
- Zmiany reguł można symulować względem nadpisanego zestawu reguł bez
  zapisywania, dla propozycji zmian Touchless. Dodatkowe kolumny PO do
  dopasowania są odczytywane z atrybutu typu dokumentu, wraz z migracją
  starej preferencji.

---

_Nie dotyczy tego wydania: Auto Accounting, Barcode, E-Mail, FTP, Ideas,
OCR, Operator. FTP i Operator zawierają wyłącznie wewnętrzne prace
utrzymaniowe._

<!-- Release R1.0.15 (sandbox 02-10-26, planned prod 14-10-26, deployed Wednesday 14 Oct 2026).
Versions on prod before this deploy: API 12.83.222, Auth 1.78.38, Auth Bridge 0.4.2,
Docflow 2.10.18, Docnet 1.56.13, Extraction 1.55.50.1, Fulltext 1.42.38, PO Match 1.59.39,
Web App 10.70.6.
Held back (Release No. names a later release; announce with that release):
R1.1: CORE-6145, CORE-6148 (import failure notice and card per channel), CORE-6127 and
CORE-6136 (run transformation rules after master data lookup), CORE-6117, CORE-6072, CORE-6071,
CORE-2452, CORE-2444, DRFS-779, CORE-554 (rule execution logs from the dashboard), CORE-550, CORE-6278,
CORE-6180, CORE-6168, DMB-431, OBO-160, DRFS-806 (date tolerance for PO matching and approval).
R1.0.16: CORE-6103 (assistant drafts transformation rules), DRFS-822 (charge cards use only
matched POs, trigger status filter), DPG-170 (cost invoice export gate), OBO-159 (the "x" on a
field stores "leave empty" on its own; field suppression).
R1.2 / R1.4: DRFS-535 (receipt availability flag), DOP-53 (UOM conversion).
Added from the Ready for Production Release list: DRFS-742, DU-220, MAR-67, DRFS-708, DRFS-820,
DRFS-723, DRFS-724, DRFS-726. Not on the page (no matching code in the delta, check by hand):
MEF-169 (S/MIME invoices from one supplier not arriving, Email Service version unchanged), DMB-391.
Shipped although Release No. is empty or stale: OBO-156, CORE-6102, CORE-6154, CORE-6155,
CORE-6150, CORE-6169, CORE-6181, CORE-6183, CORE-6185, CORE-6187, CORE-2606, CORE-2461,
CORE-2457, CORE-6092 (R1.0.14 labels). -->
