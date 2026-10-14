# Informacje o wersji DocBits — 26–30 czerwca 2026

_Co przyniosła ta aktualizacja produkcyjna, w prostych słowach. Przy każdej usłudze
podano wersję obecnie działającą na produkcji. Usługi niewymienione poniżej nie
miały w tym okresie żadnych zmian widocznych dla klientów._

---

## Najważniejsze zmiany

- **Jedno połączenie dla asystentów AI ([DocBits MCP](https://docs.docbits.com/advanced-functions-and-tools/docbits-mcp)).** Pojedyncza, ujednolicona
  brama obsługuje teraz wszystkie narzędzia DocBits — w tym DocFlow — poprzez główne
  API, dzięki czemu asystenci AI (Claude, Gemini CLI, Codex) łączą się przez jeden
  niezawodny punkt końcowy zamiast przez kilka.
- **Inteligentniejsze wielojęzyczne wyszukiwanie na pulpicie.** Łączniki
  wyszukiwania (**AND / OR**) pojawiają się teraz w Twoim języku z kolorowym
  wyróżnieniem, podtypy faktur oferują listę rozwijaną wartości, a komunikaty
  o składni wyszukiwania są zlokalizowane — a wszystko to przy płynniejszej obsłudze
  klawiatury.
- **Płynniejsze zatwierdzenia i uprawnienia.** Zatwierdzanie nie jest już wyzwalane,
  gdy jednostka opakowaniowa z potwierdzenia zamówienia jest pusta, zwykli
  użytkownicy mogą ponownie zatwierdzać elementy kosztowe po migracji kontroli
  dostępu, a uprawnienia na poziomie dokumentu są stosowane poprawnie nawet wtedy,
  gdy kolumna tabeli już istnieje.
- **Aplikacja aktualizuje się sama.** Gdy pojawia się nowa wersja, DocBits odświeża
  się teraz automatycznie, zamiast przerywać pracę wyskakującym okienkiem
  „Odśwież teraz”.
- **Bardziej odporne dopasowywanie zamówień zakupu.** Przekształcenia wartości
  kolumn, zabezpieczenia przed awariami dla pozycji bez ceny lub ilości oraz
  automatyczne ponawianie przy zerwanych połączeniach z bazą danych sprawiają, że
  dopasowywanie jest stabilniejsze.
- **Mniej błędów w całej aplikacji.** Wykryto i naprawiono wiele rzadkich błędów
  serwera na pulpitach, fakturach dostawców, rekordach zamówień zakupu oraz zadaniach
  OCR.

---

## Web App — live: `10.34.4`

- **Szybkie wyszukiwanie na pulpicie:** zlokalizowane łączniki **AND / OR** (de/fr)
  z kolorowym wyróżnianiem składni; lista rozwijana wartości podtypu faktury;
  zlokalizowane komunikaty o błędach składni wyszukiwania; płynniejsza obsługa
  klawiatury; ostrzeżenie „wymagane wyszukiwanie pełnotekstowe” jest teraz renderowane
  w treści, dzięki czemu układ już nie skacze.
- **Zatwierdzenia i uprawnienia:** naprawiono błędne wyzwalanie zatwierdzania, gdy
  jednostka opakowaniowa z potwierdzenia zamówienia jest pusta; zwykli użytkownicy
  mogą ponownie zatwierdzać elementy kosztowe po migracji kontroli dostępu;
  uprawnienia na poziomie dokumentu są teraz stosowane, gdy kolumna tabeli już
  istnieje.
- **Automatyczna aktualizacja:** aplikacja odświeża się automatycznie przy nowej
  wersji zamiast wyświetlać wyskakujące okienko „Odśwież teraz”; usunięto stare okno
  dialogowe z informacją o wersji.
- **Ustawienia poczty przychodzącej:** nowy przełącznik i pole odbiorców powiadomień
  o błędach; dziennik importu pokazuje teraz aktywność wychodzącą oraz przyczynę
  błędu; adres przychodzący kopiuje się niezawodnie.
- **Podział dokumentu:** ekran podziału dokumentu można teraz przewijać.
- **Tryb ciemny:** poprawki dla ekstrakcji tabel, licznika zadań oraz oznaczeń
  zamkniętych dokumentów na pulpicie.
- **Użyteczność i stabilność:** poprawki interfejsu eksportu z pulpitu; przyklejone
  nagłówki tabel nie przebijają już przez okna dialogowe; pulpit DocNet nie ulega już
  awarii przy nieudanym żądaniu statystyk; skrypty pól nie przywracają już
  opróżnionych pól do ich poprzednich wartości; poprawki pól wyboru i układu
  w ustawieniach zamówień zakupu; poprawki wyświetlania listy klasyfikacji.
- **Dostawcy:** organizacje dostawców mogą się teraz rejestrować za pomocą magicznego
  linku.

## API Service — live: `12.46.8`

- **Brama DocBits MCP:** ujednolicona brama pośredniczy teraz w narzędziach DocFlow
  poprzez główne API, dzięki czemu asystenci AI docierają do każdego narzędzia
  DocBits przez jeden punkt końcowy; punkt końcowy MCP jest udostępniany bez
  przekierowania, które mogłoby zrywać połączenia.
- **Księgowość:** dodano walidację centrum kosztów dla identyfikatora księgowania.
- **Kierowanie do OCR:** dokumenty są wysyłane do pełnego ponownego OCR, gdy e-text
  dostawcy jest wyłączony, dzięki czemu tekst pozostaje wiarygodny.
- **Infor ERP / SAP:** dodatkowe opłaty są kierowane poprawnie, gdy system ERP
  przechowuje już opłatę z zerową kwotą.
- **Niezawodność (mniej błędów serwera):** wzmocniono zapytania pulpitu, faktur
  dostawców, rekordów zamówień zakupu oraz menedżera zadań, dzięki czemu nie zwracają
  już rzadkich błędów 500; bardziej odporna synchronizacja pamięci podręcznej
  organizacji oraz czyszczenie zapisanych plików.
- **Czytelniejsze filtry pulpitu:** usunięto zbędne pole filtra numeru faktury;
  poprawiono ilość dopasowaną w zamówieniu zakupu.
- **Dokumentacja API dla deweloperów:** interfejs Swagger UI oferuje teraz listę
  rozwijaną specyfikacji (OpenAPI 3.0 oraz widok Infor Swagger 2.0) z brandingiem
  DocBits.

## Auth Service — live: `1.68.0`

- **Szybsze wylogowywanie / unieważnianie tokenów:** zbiorcze unieważnianie tokenów
  nie trwa już wiele minut i nie zrywa połączenia.
- **Naprawiono e-maile do ustawiania hasła**, dzięki czemu wyświetlają się poprawnie.
- **Dostawcy:** organizacje dostawców mogą rejestrować się za pomocą magicznego
  linku.
- **Stabilność logowania:** członek nie jest już blokowany przy przejściowym
  niepowodzeniu wyszukiwania organizacji, a nieprawidłowy identyfikator organizacji
  zwraca teraz czytelny komunikat zamiast błędu.

## Docflow Service — live: `2.4.1`

- **Niezawodna brama AI:** naprawiono zawieszenia i przekroczenia limitu czasu na
  punkcie końcowym DocFlow MCP (uzgadnianie połączenia, rozłączenia klientów,
  zduplikowane odpowiedzi) — strona DocFlow ujednoliconej bramy DocBits MCP.

## OCR Service — live: `1.7.1`

- **Stabilniejsze przetwarzanie OCR:** kolejki odpowiedzi działające w tle wygasają
  automatycznie, a przejściowe błędy połączeń są ponawiane, dzięki czemu mniej zadań
  OCR utyka.

## PO Match Service — live: `1.55.7`

- **Przekształcenia wartości** są teraz stosowane w kolumnach item-id, unit-code
  i static-value podczas dopasowywania według reguł.
- **Zabezpieczenia przed awariami:** pozycja bez ceny lub ilości, nietypowa
  kombinacja kluczy ważonych lub niemożliwe dzielenie nie powodują już awarii
  dopasowywania.
- **Niezawodność:** zapisy do bazy danych są automatycznie ponawiane przy zerwanych
  lub zamkniętych przez SSL połączeniach.
- **Infor ERP / SAP:** dodatkowe opłaty są kierowane poprawnie, gdy system ERP
  przechowuje opłatę z zerową kwotą.

## Fulltext Service — live: `1.35.6`

- **Szybsze ponowne indeksowanie:** wszystkie fazy synchronizacji są teraz
  rozdzielane, dzięki czemu uruchamia się autoskalowanie, co eliminuje wolne
  szeregowe ponowne indeksowanie oraz zawieszony widżet postępu na 0%.
- **Stabilniejsze statystyki:** żądania statystyk dokumentów między regionami są
  ograniczane, dzięki czemu nie przekraczają już limitu czasu.

---

## Brak zmian widocznych dla klientów w tym okresie

Stabilne, bez istotnych zmian produktowych między 26 a 30 czerwca: Auto Accounting
(`1.18.6`), Barcode (`1.15.6`), Docnet (`1.54.6`), Email (`1.36.4`), Extraction
(`1.48.7`), FTP (`1.30.1`), Operator (`1.39.5`). Auto Accounting i FTP otrzymały
wyłącznie wewnętrzną konserwację.

<!-- Generated by the docbits-changelog skill (prod-delta mode). Versions read live
     from prod (do-fra1-polydocs/prod); window 2026-06-26 → 2026-06-30. -->
