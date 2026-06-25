# Informacje o wersji DocBits — 21–25 czerwca 2026

_Co przyniosła ta aktualizacja produkcyjna, w prostych słowach. Przy każdej usłudze
podano wersję obecnie działającą na produkcji. Usługi niewymienione poniżej nie
miały w tym okresie żadnych zmian widocznych dla klientów._

---

## Najważniejsze zmiany

- **Inteligentniejsze wyszukiwanie na pulpicie.** Niezawodne wyszukiwanie
  dokumentów po kwotach i numerach — znajdź faktury powyżej określonej wartości
  lub szukaj po **numerze zapotrzebowania** — z zakresami kwot, które porównują
  rzeczywiste liczby, a nie tekst. Podtypy faktur można wyszukiwać po ich
  przetłumaczonych nazwach.
- **Niezawodne powiadomienia e-mail.** Alerty o zmianie statusu są teraz wysyłane
  dla każdego statusu (koniec z cicho pomijanymi e-mailami), a potwierdzenia
  importu przychodzącego oraz powiadomienia o błędach mają teraz właściwy branding
  DocBits z możliwością sterowania na poziomie poszczególnych odbiorców.
- **Płynniejsze logowanie w różnych regionach (EU/US).** Przełączanie regionu to
  teraz mały baner zamiast pełnoekranowego przerwania, logowanie jednokrotne
  trafia do właściwego regionu, a pozostawanie zalogowanym w wielu kartach
  przeglądarki jest bardziej niezawodne.
- **Poprawki uprawnień.** Użytkownicy otrzymują dostęp przyznany im przez ich
  grupę — otwieranie, edytowanie, zatwierdzanie i ponowne uruchamianie dokumentów
  działa teraz poprawnie nawet wtedy, gdy grupy i uprawnienia są skonfigurowane
  w mniej typowy sposób.
- **Stabilniejsze przetwarzanie dokumentów.** Dokumenty, które wcześniej zacinały
  się po przesłaniu, są automatycznie ponownie podejmowane do przetwarzania,
  a nagły wzrost ruchu od jednego klienta nie spowalnia już pozostałych.

---

## Web App — live: `10.32.4`

- **Szybkie wyszukiwanie ze skokiem (Cmd/Ctrl + K)** bezpośrednio do ustawienia
  **walidacji e-faktur**.
- **Region i logowanie:** przełączanie regionu pokazywane jako trwały baner zamiast
  blokującego ekranu; logowanie jednokrotne przekierowuje teraz do właściwego
  regionu (EU/US); pozostawanie zalogowanym w wielu kartach jest bardziej
  niezawodne.
- **Uprawnienia:** naprawiono przypadki, w których użytkownicy nie mogli
  **zatwierdzać**, **edytować**, **otwierać** ani **ponownie uruchamiać**
  dokumentów mimo posiadania właściwych uprawnień grupowych.
- **Ustawienia poczty przychodzącej:** nowe przełączniki „Powiadom nadawcę” oraz
  „Odpowiedz nadawcy po odebraniu”.
- **Użyteczność:** ostrzeżenie o zduplikowanym dokumencie trzeba teraz zamknąć
  przed kontynuowaniem; baner „backend niedostępny” pojawia się tylko podczas
  rzeczywistych awarii; liczniki zadań aktualizują się natychmiast po zakończeniu
  zadań; poprawka trybu ciemnego na ekranie walidacji tabeli AI.
- **Wydajność:** naprawiono zawieszanie się ekranu e-dokumentów podczas walidacji
  pól i dopasowywania zamówień zakupu.
- **Wyszukiwanie podtypów faktur po ich przetłumaczonych nazwach.**

## API Service — live: `12.41.9`

- **Gruntowna przebudowa wyszukiwania na pulpicie:** numer zapotrzebowania
  i osoba zgłaszająca są teraz wyszukiwalne; wyszukiwanie po kwotach i numerach
  zwraca poprawne wyniki (rzeczywiste porównanie numeryczne); łączna kwota netto
  oraz kolumny wyliczane wyświetlają się poprawnie.
- **Niezawodne e-maile z alertami o statusie** dla dowolnego statusu dokumentu,
  bez ukrywania błędów wysyłki.
- **Uprawnienia:** użytkownicy bez grupy mogą otwierać i zatwierdzać własne
  dokumenty; przywrócono widoczność dokumentów dla użytkowników bez grupy.
- **Niezawodność przetwarzania dokumentów:** dokumenty utknięte w stanie „nowy” są
  automatycznie kolejkowane ponownie; sprawiedliwy podział przetwarzania, dzięki
  któremu duży wzrost ruchu od jednej organizacji nie zagładza pozostałych;
  samonaprawa w przypadku rzadkich problemów z sekwencjami w bazie danych.
- **Zeskanowane pliki PDF z uszkodzoną warstwą tekstową są kierowane do OCR**
  zamiast generować niewiarygodny tekst.
- **Dokładność ekstrakcji i zamówień zakupu:** nazwa dostawcy uzupełniana
  z powiązanego zamówienia zakupu; usunięto zduplikowane kolumny numerów pozycji;
  lepsza obsługa znaków specjalnych (spacji nierozdzielających).
- **Eksport do Infor ERP / SAP:** naprawiono uwierzytelnianie eksportu SFTP.
- **E-fakturowanie:** udoskonalenia ścieżki ekstrakcji ZUGFeRD / e-dokumentów.

## Auth Service — live: `1.66.0`

- **Naprawiono brakujące przypisanie organizacji** dla niektórych użytkowników
  (pusty identyfikator organizacji).

## Docflow Service — live: `2.3.4`

- **Czas oczekiwania wyzwalacza workflow** jest teraz konfigurowalny dla każdego
  środowiska.

## Email Service — live: `1.35.9`

- **E-maile z brandingiem:** potwierdzenia importu przychodzącego i powiadomienia
  o błędach używają teraz prawdziwego logo i kolorów DocBits.
- **Sterowanie na poziomie organizacji:** e-mail potwierdzający odebranie,
  „powiadom nadawcę” w razie błędu oraz opcje odpowiedzi do nadawcy.
- **Bardziej niezawodny import przychodzący:** wyniki importu są zapisywane
  poprawnie, częściowe niepowodzenia są raportowane jako błędy (a nie ciche
  sukcesy), a problematyczne znaki w treści e-maili nie psują już importu.
- **Routing EU/US:** kierowanie ruchu na poziomie organizacji do właściwego
  regionalnego API.

## Fulltext Service — live: `1.34.5`

- **Wyszukiwanie po kwotach i numerach** działa teraz niezawodnie, w tym separatory
  tysięcy oraz zakresy kwot (silnik stojący za przebudową wyszukiwania na pulpicie).
- **Stabilniejsza infrastruktura wyszukiwania:** osierocone kolejki działające
  w tle są usuwane, więc nie blokują już współdzielonych zasobów.

## PO Match Service — live: `1.54.7`

- **Bardziej odporne dopasowywanie zamówień zakupu:** tekstowe kody
  opakowań/jednostek pakowania nie blokują już dopasowania, a ręczne dopasowywanie
  pozycji bezpiecznie obsługuje puste wyniki.

---

## Brak zmian widocznych dla klientów w tym okresie

Stabilne, bez istotnych zmian produktowych między 21 a 25 czerwca: Auto Accounting
(`1.18.5`), Barcode (`1.15.6`), Docnet (`1.54.6`), Extraction (`1.48.6`), FTP
(`1.30.0`), OCR (`1.6.8`), Operator (`1.39.5`).

<!-- Generated by the docbits-changelog skill (prod-delta mode). Versions read live
     from prod (do-fra1-polydocs/prod); window 2026-06-21 → 2026-06-25. -->
