# Informacje o wersji DocBits — 30 czerwca – 3 lipca 2026

_Co przyniosła ta aktualizacja produkcyjna, w prostych słowach. Przy każdej usłudze
podano wersję obecnie działającą na produkcji. Usługi niewymienione poniżej nie
miały w tym okresie żadnych zmian widocznych dla klientów._

---

## Najważniejsze zmiany

- **Czat AI w Dziennikach aktywności.** Nowy panel czatu AI na stronie Dzienników
  aktywności pozwala zadawać pytania dotyczące aktywności w dziennikach
  bezpośrednio, bez przekopywania się przez surowe wpisy.
- **Śledzenie importu poczty wychodzącej.** Dziennik importu rejestruje teraz
  pocztę wychodzącą obok przychodzącej, z etykietami szybkiego filtrowania
  Errors / Inbound / Outbound (Błędy / Przychodzące / Wychodzące) — skrzynki,
  które wielokrotnie zawodzą, są automatycznie dezaktywowane, administratorzy
  mogą otrzymywać powiadomienie e-mail o niepowodzeniu importu, a ponowne próby
  są teraz wykonywane maksymalnie 15 razy w ciągu około 5 godzin, zanim system
  się podda.
- **Czytelniejsze błędy importu poczty.** Niepowodzenia logowania pokazują teraz
  rzeczywistą przyczynę, z dedykowanymi komunikatami dla nieprawidłowego
  certyfikatu lub błędnego hasła aplikacji Gmail.
- **Naprawiono pętlę logowania.** Niektórzy użytkownicy mogli utknąć
  w powtarzającej się pętli logowania podczas odświeżania tokenu — problem
  został rozwiązany.
- **Stabilniejsze przetwarzanie dokumentów.** Naprawiono awarię podczas
  ekstrakcji danych spowodowaną niezaokrąglonymi wartościami współrzędnych,
  odczyt kodów kreskowych ponawia teraz próby przy błędach możliwych do
  naprawienia zamiast po cichu się poddawać, a rzadki przypadek, w którym
  dokument mógł zostać wyeksportowany dwukrotnie w tym samym czasie, został
  naprawiony.
- **Usprawnienia ekranu walidacji.** Można teraz przybliżać dokumenty na
  większą skalę, pola nie są już czyszczone przez skrypty, gdy ich wartość
  faktycznie się nie zmieniła, a pulpit zapamiętuje pozycję strony po powrocie
  do niego.

---

## Web App — live: `10.35.7`

- **Panel czatu AI** dodany do strony Dzienników aktywności (#15512).
- **Dziennik importu:** nowe etykiety szybkiego filtrowania Errors / Inbound /
  Outbound (Błędy / Przychodzące / Wychodzące); przełącznik i pole odbiorców
  powiadomień o błędach w ustawieniach poczty przychodzącej.
- **Ekran walidacji:** przybliżenie dokumentu wykracza teraz poza poprzedni
  domyślny rozmiar; pola opróżniane przez skrypty walidacyjne poprawnie
  zachowują teraz swoją wartość, gdy skrypt zwraca tę samą wartość.
- **Pulpit:** pozycja strony jest zachowywana przy powrocie do tabeli; uchwyt
  zmiany szerokości kolumny nie wychodzi już poza nagłówek tabeli.
- **Ekran Auto Accounting:** naprawiono błąd walidacji.
- **DocBits Tasks:** naprawiono problem z uprawnieniami.
- **Dzienniki Watchdog:** dodano filtr zakresu czasu oraz regulowany wybór
  liczby wierszy na stronę.
- **Poprawki:** błąd wykresu („Element not found") na stronie Boards; uszkodzony
  link usuwania eksportu w Dziennikach aktywności; poprawki układu na ekranie
  Layout Builder; brakujące tłumaczenie w filtrze zakresu czasu w Dziennikach
  aktywności.
- **Automatyczna aktualizacja:** dalsze wzmocnienie mechanizmu automatycznej
  aktualizacji aplikacji (szybsze czyszczenie przy starcie, bardziej niezawodne
  wykrywanie wersji, czyszczenie pamięci podręcznej przed ponownym załadowaniem
  naprawczym).

## API Service — live: `12.48.1`

- **Szybsze ładowanie skryptów dokumentów:** skrypty walidacyjne są teraz
  buforowane po stronie serwera (bufor na 6 godzin) zamiast być pobierane za
  każdym razem.
- **Dokładniejsza pewność kwoty:** ocena pewności uwzględnia teraz dokumenty
  korzystające z różnych konwencji separatora dziesiętnego.
- **Niezawodność:** walidacja dokumentu zawsze uruchamia jedną aktywną wersję
  skryptu, a informacja o tym, która wersja została uruchomiona, jest teraz
  rejestrowana w logach; naprawiono rzadki przypadek, w którym dokument mógł
  zostać wyeksportowany dwukrotnie w tym samym czasie; reguły ekstrakcji
  specyficzne dla dostawcy ponownie stosują się poprawnie po wymuszonym
  ponownym OCR.
- **Import poczty:** dodano wsparcie backendowe dla rejestrowania poczty
  wychodzącej oraz e-maili z powiadomieniem o błędzie (zob. Email Service
  poniżej).

## Auth Service — live: `1.68.5`

- **Naprawiono pętlę logowania**, w którą mogli wpaść niektórzy użytkownicy
  podczas odświeżania tokenu sesji.
- **Szybsze ekrany administracji organizacją:** dane użytkowników i subskrypcji
  są teraz ładowane zbiorczo zamiast rekord po rekordzie.
- **Naprawiono rzadki konflikt bazy danych** występujący przy łączeniu
  użytkownika z organizacją.

## Email Service — live: `1.37.4`

- **Dziennik importu śledzi teraz pocztę wychodzącą** obok przychodzącej,
  z filtrem pozwalającym pokazać wyłącznie import przychodzący, wychodzący lub
  nieudany.
- **Skrzynki, które wielokrotnie zawodzą, są teraz automatycznie
  dezaktywowane** po powtarzających się błędach, a administratorzy mogą
  otrzymywać powiadomienie e-mail przy niepowodzeniu importu; ponowne próby są
  teraz wykonywane maksymalnie 15 razy w ciągu około 5 godzin, zanim system się
  podda.
- **Czytelniejsze komunikaty o niepowodzeniu logowania:** pokazują rzeczywistą
  przyczynę, dedykowany komunikat dla nieprawidłowego certyfikatu oraz odrębny
  komunikat dla błędnego hasła aplikacji Gmail.
- **Naprawiono routing poczty przychodzącej**, które nieprawidłowo przepisywało
  adresy serwerów dla kont z regionu UE.
- Większa odporność na krótkotrwałe zerwania połączenia z Redis.

## Extraction Service — live: `1.49.0`

- **Naprawiono awarię podczas ekstrakcji** spowodowaną niezaokrąglonymi
  wartościami współrzędnych.
- **Dokładniejsza pewność kwoty** dla dokumentów z mieszanymi formatami
  separatora dziesiętnego; drobne różnice zaokrągleń w sumie podatku nie
  blokują już dopasowania.

## Docflow Service — live: `2.4.2`

- **Przebudowano uwierzytelnianie dla zaawansowanych przepływów pracy (opartych
  na Celery)**, dodając zabezpieczenia, dzięki którym nieudane sprawdzenie
  uwierzytelnienia nie może już spowodować awarii uruchomienia przepływu pracy.
- **Czytelniejsza odpowiedź**, gdy krok przepływu pracy próbuje uruchomić się
  względem przepływu pracy, który już nie istnieje.

## Barcode Service — live: `1.15.7`

- **Odczyt kodów kreskowych automatycznie ponawia teraz próby** przy błędach
  możliwych do naprawienia, zamiast po cichu się poddawać.

## OCR Service — live: `1.7.3`

- **Naprawiono błąd OCR** spowodowany problemem z wyszukiwaniem nazwy hosta
  Redis.
- Rozłączenia Redis podczas kontroli stanu (health-check) nie są już
  rejestrowane jako błędy, co ogranicza liczbę fałszywych alertów.

## PO Match Service — live: `1.55.8`

- **Naprawiono brak wyświetlania notatek** w rekordach PO Match.

---

## Brak zmian widocznych dla klientów w tym okresie

Stabilne, bez istotnych zmian produktowych między 30 czerwca a 3 lipca: Auto
Accounting (`1.18.7`), Docnet (`1.54.6`), FTP (`1.30.2`), Fulltext (`1.35.7`),
Operator (`1.39.5`). Auto Accounting otrzymał wyłącznie wewnętrzną konserwację
konfiguracji wdrożenia. Nie udało się nawiązać połączenia z Ideas Service w celu
sprawdzenia wersji w tym okresie.

<!-- Generated by the docbits-changelog skill (version-boundary mode, resolved
     from the prod version table supplied by the user). Window 2026-06-30 →
     2026-07-03. -->
