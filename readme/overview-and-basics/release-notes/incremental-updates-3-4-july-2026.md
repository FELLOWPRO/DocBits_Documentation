# Informacje o wersji DocBits — 3–4 lipca 2026

_Przegląd tego, co zmienia się dla Państwa w tym wydaniu DocBits. Każda usługa
poniżej pokazuje wersję obecnie działającą na produkcji, a następnie opisuje
nowości lub poprawki prostym językiem — bez numerów zgłoszeń i żargonu
inżynierskiego. Usługi niewymienione poniżej nie miały w tym okresie żadnych
zmian widocznych dla klientów._

---

## Najważniejsze zmiany

- **Wdrożenia bez przestojów w całej flocie.** API, Auto Accounting, Docflow,
  Extraction, OCR i PO Match zamykają się teraz czysto podczas wydania nowej
  wersji. Wcześniej żądanie będące w toku podczas wdrożenia mogło zostać
  przerwane; teraz każde żądanie w toku jest kończone, zanim stara wersja
  zostanie zatrzymana, dzięki czemu wydania nie powodują już krótkich
  zakłóceń dla użytkowników.
- **Usprawnienia eksportu e-faktur.** Eksport dokumentu do wielu konfiguracji
  eksportu jednocześnie jest teraz bardziej niezawodny — sprawdzanie
  duplikatów eksportu odbywa się raz na całą partię zamiast raz na każdy
  element, a nowy punkt końcowy eksportu zapobiega migotaniu statusu eksportu,
  gdy kilka eksportów jest uruchamianych razem. Dokumenty XRechnung/ZUGFeRD
  otrzymują też bardziej spójne mapowanie pól.
- **Stabilniejsze przetwarzanie dokumentów.** Naprawiono awarię, która mogła
  zatrzymać cały dokument OCR w przypadku błędu pojedynczej strony, naprawiono
  synchronizację dostaw zamówień zakupu pobierającą wcześniej tylko pierwsze
  100 rekordów, oraz wzmocniono odporność kilku usług na krótkotrwałe zerwania
  połączenia z bazą danych.
- **Odzyskane załączniki e-mail.** Naprawiono przypadek, w którym załączniki
  e-mail mogły docierać uszkodzone lub z brakującymi bajtami podczas importu
  poczty przychodzącej.
- **Niezawodność przepływów pracy.** Naprawiono utykanie przepływów pracy
  spowodowane blokadą, która nie zwalniała się poprawnie, oraz naprawiono
  logikę ponownego planowania, dzięki czemu pominięte kroki przepływu pracy są
  teraz poprawnie obsługiwane i rejestrowane w logach.
- **Nowość: Ideas Service.** Nowa usługa backendowa (Ideas, wersja 0.3.0)
  dołączyła do floty produkcyjnej.

---

## API Service — live: `12.52.4`

- **Niezawodność OCR:** awaria pojedynczej strony nie powoduje już
  niepowodzenia całego dokumentu.
- **Eksport:** sprawdzanie duplikatów eksportu odbywa się teraz raz na całą
  partię zamiast raz na każdy element; nowy punkt końcowy eksportu zapobiega
  migotaniu statusu eksportu, gdy kilka eksportów jest uruchamianych
  jednocześnie; dokumenty XRechnung/ZUGFeRD otrzymują bardziej spójne
  kanoniczne mapowanie pól.
- **Zamówienia zakupu:** naprawiono synchronizację dostaw pobierającą tylko
  pierwsze 100 rekordów na zamówienie.
- **Dzienniki aktywności:** naprawiono przycisk „Dalej”, który przenosił do
  niepowiązanego okresu czasu.
- **Wyszukiwanie danych podstawowych:** naprawiono błąd serwera (HTTP 500).
- **Indeksowanie wyszukiwania:** dodano znacznik potwierdzenia dostarczenia
  oraz ponowne próby, dzięki czemu dokumenty są niezawodnie kolejkowane do
  wyszukiwania pełnotekstowego.
- **Wdrożenia bez przestojów:** żądania w toku są teraz kończone, zanim
  wydanie ponownie uruchomi usługę.
- Ogólne poprawki stabilności rozwiązujące kilka powtarzających się błędów
  w tle.

## Auth Service — live: `1.68.7`

- W tym okresie wyłącznie wewnętrzna konserwacja i utrzymanie niezawodności.

## Auto Accounting — live: `1.18.8`

- **Wdrożenia bez przestojów:** żądania w toku są teraz kończone, zanim
  wydanie ponownie uruchomi usługę.

## Barcode Service — live: `1.15.8`

- W tym okresie wyłącznie wewnętrzna poprawka konfiguracji wdrożenia.

## Docflow Service — live: `2.5.3`

- **Nowa opcja eksportu** umożliwiająca wysłanie dokumentu do wielu
  konfiguracji eksportu jednocześnie.
- **Naprawiono utykanie przepływów pracy** spowodowane blokadą, która nie
  zwalniała się poprawnie niezależnie od statusu.
- **Naprawiono ponowne planowanie przepływu pracy**, dzięki czemu pominięte
  kroki są teraz poprawnie obsługiwane i rejestrowane w logach zamiast być po
  cichu pomijane.
- **Szybszy start:** bazy danych są teraz wstępnie „rozgrzewane” w tle.
- Większa odporność na krótkotrwałe zerwania połączenia z bazą danych.
- Usprawnione parsowanie pól daty w kartach przepływu pracy.
- **Wdrożenia bez przestojów:** żądania w toku są teraz kończone, zanim
  wydanie ponownie uruchomi usługę.

## Email Service — live: `1.37.9`

- **Naprawiono załączniki poczty przychodzącej**, które mogły docierać
  uszkodzone lub z brakującymi bajtami.
- **Czytelniejsze błędy**, gdy nie można pobrać folderu skrzynki pocztowej,
  zamiast ogólnego niepowodzenia.

## Extraction Service — live: `1.49.6`

- **Naprawiono awarie** dla dokumentów z nierozpoznanym typem dokumentu oraz
  dla tabel o nietypowym lub zniekształconym kształcie.
- Większa odporność na krótkotrwałe zerwania połączenia z bazą danych
  w trakcie zapytania.
- **Wdrożenia bez przestojów:** żądania w toku są teraz kończone, zanim
  wydanie ponownie uruchomi usługę.

## FTP Service — live: `1.30.3`

- W tym okresie wyłącznie wewnętrzna aktualizacja frameworka.

## Fulltext Service — live: `1.36.3`

- **Indeksowanie wyszukiwania:** okresowe sprawdzanie naprawia teraz wszelkie
  dokumenty, które nie trafiły do indeksu wyszukiwania, dla dowolnej
  organizacji.
- **Synchronizacja z ERP:** naprawiono zablokowaną blokadę, która mogła
  wstrzymywać synchronizację z ERP po nieudanej ponownej próbie.

## OCR Service — live: `1.7.8`

- **Naprawiono uwierzytelnianie OCR**, dzięki czemu klucze API organizacji
  ponownie działają poprawnie.
- **Wdrożenia bez przestojów:** żądania w toku są teraz kończone, zanim
  wydanie ponownie uruchomi usługę.

## Operator Service — live: `1.39.7`

- W tym okresie wyłącznie wewnętrzne poprawki niezawodności wdrożenia.

## PO Match Service — live: `1.56.0`

- **Naprawiono awarię** podczas sortowania ilości PO Match zawierających
  puste wartości.
- **Wdrożenia bez przestojów:** żądania w toku są teraz kończone, zanim
  wydanie ponownie uruchomi usługę.

## Web App — live: `10.36.9`

- **Naprawiono błąd** przy powrocie do ekranu Walidacji pól z innego ekranu.
- **Naprawiono przycisk „Scripts”**, który przekierowywał do strony 404.
- **Dzienniki aktywności:** naprawiono nieprawidłowe wyświetlanie „Page 2 of
  1” oraz naprawiono filtr poziomu WARN, który nie dopasowywał żadnych
  wyników.

---

## Brak zmian widocznych dla klientów w tym okresie

Auth Service, Barcode Service, FTP Service, Operator Service oraz Docnet
Service (`1.54.6`, bez zmian) otrzymały w tym okresie wyłącznie wewnętrzną
konserwację lub poprawki konfiguracji wdrożenia.

<!-- Generated by the docbits-changelog skill (version-boundary mode: exact
     git ranges between the ALT and NEU version-bump commits supplied by the
     user, per service). Window ~2026-07-01 → 2026-07-04. -->
