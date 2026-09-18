# Plan rozwoju DocBits

_Stan planowania na 18 września 2026. Każde wydanie podaje planowaną datę
udostępnienia na sandboxie (kiedy klienci mogą je testować) oraz planowaną
datę produkcyjną. Motywy opisują, co jest planowane na dane wydanie, a nie
to, co już zostało dostarczone; zakres i daty mogą się zmienić. Hotfixy
między wydaniami są udokumentowane w
[Informacjach o wersji](release-notes/README.md)._

| Wydanie | Sandbox | Produkcja |
|---|---|---|
| R1.1 | 5 października 2026 | 14 października 2026 |
| R1.2 | 23 listopada 2026 | 2 grudnia 2026 |
| R1.3 | 8 lutego 2027 | 17 lutego 2027 |
| R1.4 | 7 kwietnia 2027 | 15 kwietnia 2027 |
| R1.5 | 18 maja 2027 | 27 maja 2027 |
| R1.6 | 6 lipca 2027 | 15 lipca 2027 |
| R1.7 | 21 września 2027 | 30 września 2027 |
| R2.0 | do ogłoszenia | do ogłoszenia |

---

## R1.1 — Sandbox 5 października 2026 · Produkcja 14 października 2026

**Reguły transformacji i layouty**

- Silnik reguł dla wyekstrahowanych wartości pól i kolumn: ustawianie,
  zastępowanie lub wyprowadzanie wartości z zagnieżdżonymi grupami warunków,
  wraz z ekranem ustawień do zarządzania regułami. Reguły wyboru layoutu
  otrzymują te same zagnieżdżone warunki.
- Wybór layoutu działa niezależnie od tego, skąd pochodzi dokument.
- Jasne reguły pierwszeństwa dla etykiet pól nagłówka i kolumn tabeli.
- Kolumnę tabeli można ponownie przypisać po jej usunięciu, a tabela cen
  artykułów dostawcy pokazuje wszystkie swoje kolumny.

**Ekrany zatwierdzania i walidacji**

- Trzy tabele pozycji na ekranie zatwierdzania (pozycje faktury, pozycje
  porównania, dopasowywanie PO) mają jeden wspólny styl, a widok porównania
  pokazuje numer artykułu należący do danej pozycji.
- Ostatnio otwarty panel boczny (kanał aktywności lub historia zatwierdzeń)
  jest zapamiętywany dla każdego użytkownika.
- Scalanie dokumentów z ekranu zatwierdzania za pomocą modułu przesyłania
  dokumentów.
- Niestandardowe reguły walidacji obsługują koszty wysyłki w sposób ogólny,
  a reguły zgłaszające fałszywie negatywny wynik zostały poprawione.
- Pasek ładowania zastępuje zwykłą ikonę ładowania; przyjaźniejsze adresy
  URL stron.

**Wykrywanie duplikatów**

- Pola niestandardowe pojawiają się w wyniku wykrywania duplikatów, a
  ustawienia duplikatów można przeszukiwać.

**Workflow i zadania**

- Przycisk „Nowy workflow”, logi zaawansowanych workflow, czytelniejszy ekran
  logów watchdoga, a kroki workflow zmieniające pole lub pole wyboru są
  stosowane niezawodnie.
- Dodanie pozycji w drzewie decyzyjnym zachowuje nazwy użytkowników, zamiast
  pokazywać identyfikatory.
- Każda zmiana statusu dokumentu jest rejestrowana.
- Tworzenie nowego szablonu e-mail znów działa.

**Import**

- Import e-mail przenosi wiadomość ze skrzynki odbiorczej dopiero po
  potwierdzeniu przesłania, traktuje ponownie dostarczone przekazanie jako
  jedno dostarczenie, rejestruje, kto ostatnio zapisał, i akceptuje
  wiadomości podpisane S/MIME.
- Import FTP otrzymuje prawdziwą opcję usuwania po imporcie obok przenoszenia
  i archiwizowania.
- Przesyłanie z aplikacji skanera znów działa.
- Pliki BOD zamówień zakupowych przesłane w regionie USA pozostają w regionie
  USA.

**Przetwarzanie dokumentów i ekstrakcja**

- Gdy usługa kodów kreskowych zawiesza się, dokument pokazuje błąd, zamiast
  tkwić w nieskończoność w stanie „Processing”.
- Nowy, tańszy poziom modelu AI („Eco”) do ekstrakcji.
- Przy strukturalnej ekstrakcji AI wytrenowane numery artykułów dostawcy
  pozostają wytrenowane, a numer artykułu i numer artykułu dostawcy nie są
  już zamieniane miejscami.
- Szablony e-dokumentów UBL są dostosowane; poprawki ekstrakcji kwot, stawek
  podatku, cen jednostkowych i numerów zamówień zakupowych na określonych
  layoutach dostawców.
- Rozpoznawane są dodatkowe formaty dat.

**Dopasowywanie zamówień zakupowych**

- Dopasowywanie wymaga kolumny ilości, używa ceny za ilość w jednostce
  bazowej, a rezerwowe dopasowanie do ostatniej pozycji można włączać lub
  wyłączać dla każdego klienta.
- Pozycje dowodu dostawy można wybierać pojedynczo.
- Ekran e-dokumentu nie zawiesza się już na fakturach z ponad 250 pozycjami.

**Touchless Intelligence**

- Więcej szczegółów w raporcie Touchless, a pole wyboru Touchless
  odzwierciedla zapisane ustawienie.

**Pulpit**

- Pulpit może pomieścić do 10 000 dokumentów na wyszukiwanie.
- Termin płatności ze skontem i termin płatności faktury są dostępne jako
  pola layoutu i wypełniane przy imporcie.
- Użytkownicy, którym udostępniono pulpit, są zachowywani przy zapisie
  pulpitu, a „Updated by” pokazuje właściwą osobę.
- Zarchiwizowane dokumenty można z powrotem przenieść ze statusu „Archived”.

**Eksport i EDI**

- Dodatkowy krok eksportu do Infor M3 dla dodatkowych informacji o fakturze.
- Lista pakunkowa z kilkoma numerami kontenerów jest eksportowana jako jeden
  rekord na kontener.
- Ponowny import przyjęcia dostawy nie kończy się już błędem zduplikowanego
  klucza, a dokumenty BOD przyjęcia dostawy są stosowane we właściwej
  kolejności.
- Zaktualizowano mapowania EDI dla faktury, zamówienia zakupowego i
  potwierdzenia zamówienia.

**Bezpieczeństwo**

- Kontrola organizacji dla kluczy API jest egzekwowana w każdym środowisku.

---

## R1.2 — Sandbox 23 listopada 2026 · Produkcja 2 grudnia 2026

**Zatwierdzanie i dopasowywanie zamówień zakupowych**

- Stan „Pending input” wstrzymuje dokument, dopóki ktoś nie odpowie, bez
  naruszania workflow ani historii audytu, a osoby zatwierdzające mogą
  zadawać pytania bez przerywania procesu zatwierdzania.
- Faktury zaliczkowe można dopasowywać przed przyjęciem towaru, podczas gdy
  opcja „Match on received quantity” pozostaje aktywna.
- Flaga dostępności przyjęcia porównuje ilości zafakturowane i przyjęte.
- Potwierdzenia zamówień: elementy kosztowe pokazywane w trakcie oczekiwania
  na zatwierdzenie, oznaczone kolorami pozycje dopłat w dopasowywaniu PO oraz
  kolumna numeru artykułu w pozycjach faktury.
- Kolumny, które nie są zmapowane, nie wchodzą już do obliczania kwoty
  tabeli.
- Obsługiwane są pozycje RMA dostawcy.

**Import i klasyfikacja**

- Adres nadawcy jest dostępny z importu e-mail.
- Typ dostawcy jest wyprowadzany z pozycji dokumentu.

**Ustawienia i automatyzacja**

- Skrypt „Set sub-organisation” staje się regułą transformacji.
- Standardowe kolumny można usuwać z typu dokumentu.

**Eksport**

- Historia eksportu znów wymienia wyeksportowane dokumenty.
- Faktury frachtowe są eksportowane do Infor LN.

---

## R1.3 — Sandbox 8 lutego 2027 · Produkcja 17 lutego 2027

**Auto Accounting Rule Manager**

- Reguły automatycznie przypisują konta i wymiary, w zakresie podorganizacji
  i typu dokumentu, wraz z ekranem audytu, który pokazuje, która reguła
  zadziałała.
- Reguła może wypełnić wartość z kolumny pozycji tabeli.
- Pola i wymiary można czyścić pojedynczo, pozycje można usuwać (także
  pozycje bez kwoty), a reguły działają dalej na polach, które zmieniły się
  z tekstu na listę rozwijaną.

**Dopasowywanie zamówień zakupowych**

- Ikona dopasowania nawiguje, przewija i podświetla między zakładkami,
  włącznie z dopasowaniami jeden-do-wielu.
- Konwersja jednostek z aliasami (na przykład KG i TO), konfigurowalna
  tolerancja zaokrągleń z kontem zaokrągleń oraz obliczenia z czterema
  miejscami po przecinku wyświetlane jako trzy.

**Eksport**

- Konfigurowalne nazwy plików eksportu.
- Niekompletny dokument w Infor LN jest usuwany po nieudanym eksporcie.
- Konektor bazy danych obejmuje wszystkie istotne tabele.

---

## R1.4 — Sandbox 7 kwietnia 2027 · Produkcja 15 kwietnia 2027

**Import**

- Mechanizm ponawiania dla importu FTP, e-mail i przychodzących wiadomości
  e-mail, z automatycznym i ręcznym ponownym przetwarzaniem.

**DocNet Agents**

- Przyjmowanie zamówień: zamówienie klienta staje się zleceniem sprzedaży w
  Infor M3 lub Infor LN (pierwsza wersja, dokumenty tekstowe).

**Zatwierdzanie**

- Ulepszony proces zatwierdzania, delegowanie do innego użytkownika w trakcie
  zatwierdzania oraz przycisk „Export & Next”.

**Dopasowywanie zamówień zakupowych**

- Na ekranie dopasowywania oferowane są tylko pozycje PO, które mogą pasować.
- Faktury z nadmiernym dopasowaniem, w których zafakturowana ilość przekracza
  ilość przyjętą, są rozpoznawane na ekranie dopasowywania, a jednostki miary
  są konwertowane podczas dopasowywania faktury.

**Pozostałe**

- Runda opinii na temat Rule Manager.
- Formularz zgłoszenia do wsparcia przyjmuje załączniki i automatycznie
  przypisuje organizację.
- Rozszerzona integracja podatkowa z Vertex.

---

## R1.5 — Sandbox 18 maja 2027 · Produkcja 27 maja 2027

**Auto Accounting**

- Akcja wyszukiwania (lookup) w Rule Manager: dopasowanie do danych
  podstawowych i przypisanie kilku pól naraz.
- Predykcje obsługują wiele kodów podatkowych i wymiarów, vouchery oraz
  referencje księgowań.
- Ekrany Auto Accounting w kilku językach.

**Zatwierdzanie i dopasowywanie zamówień zakupowych**

- Ponowne przypisanie dokumentu do innego użytkownika.
- Kolejność kolumn na ekranie dopasowywania PO jest zapisywana dla każdego
  użytkownika.
- Kody opłat (myto, transport, energia) są rozpoznawane, a ich koszt jest
  rozdzielany.

**Zabezpieczenia eksportu**

- Eksport jest blokowany z ostrzeżeniem, gdy dopasowana ilość przekracza
  przyjętą ilość lub zbyt mocno się od niej różni, albo gdy data księgowania
  jest wcześniejsza niż data wpisu magazynowego.

**Użyteczność**

- Kolejność wykonywania skryptów dokumentu jest widoczna we frontendzie.
- Klawisze Enter i Tab przenoszą między polami.

---

## R1.6 — Sandbox 6 lipca 2027 · Produkcja 15 lipca 2027

**Ustawienia**

- Ustawienia można przeszukiwać we wszystkich przełącznikach i podstronach.
- Konfiguracja serwera e-mail pozwala zastąpić wygasły sekret OAuth lub
  sekret klienta bez ponownego konfigurowania skrzynki pocztowej.
- Mapę numerów artykułów dostawcy (tabelę konwersji numerów artykułów) można
  wypełnić z importu CSV.

**Auto Accounting**

- Wymiary są przechowywane w nowej strukturze, dzięki czemu duże zestawy
  wymiarów ładują się szybciej.

---

## R1.7 — Sandbox 21 września 2027 · Produkcja 30 września 2027

**Auto Accounting na ekranie zatwierdzania**

- Osoby zatwierdzające mogą korzystać z Auto Accounting bezpośrednio na
  ekranie zatwierdzania.
- Zatwierdzenie może być uzależnione od pól księgowych, takich jak kod konta
  księgowego lub kraj, z korektą po stronie AP, gdy dokument zostaje
  zwrócony.
- Lista rozwijana kodów podatkowych w Auto Accounting bez konieczności
  konfigurowania wielu pozycji podatkowych.

---

## R2.0 — Sandbox do ogłoszenia · Produkcja do ogłoszenia

**Auto Accounting**

- Pola oparte na liście akceptują także dowolny tekst.
- Pola wymagane są walidowane.
- Predykcje modelu automatycznie wypełniają pola księgowe (tryb hybrydowy z
  wytrenowanym modelem predykcyjnym), ze ścieżką audytu pokazującą, co model
  wypełnił.

<!-- Generated from Jira "Release No." (customfield_10392) on 2026-09-18 by the
     docbits-roadmap skill. Themes only; ticket keys, customer names and
     internal work are deliberately left out. Rerun the skill to refresh. -->
