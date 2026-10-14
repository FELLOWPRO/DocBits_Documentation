# Plan rozwoju DocBits

_Stan planowania na 7 października 2026. Każde wydanie podaje planowaną datę
udostępnienia na sandboxie (kiedy klienci mogą je testować) oraz planowaną
datę produkcyjną. Motywy opisują, co jest planowane na dane wydanie, a nie
to, co już zostało dostarczone; zakres i daty mogą się zmienić. Hotfixy
między wydaniami są udokumentowane w
[Informacjach o wersji](release-notes/README.md)._

| Wydanie | Sandbox | Produkcja |
|---|---|---|
| R1.1 | 16 października 2026 | 4 listopada 2026 |
| R1.2 | 16 lutego 2027 | 3 marca 2027 |
| R1.3 | 1 czerwca 2027 | 16 czerwca 2027 |
| R1.4 | 5 października 2027 | 20 października 2027 |

---

## R1.1 — Sandbox 16 października 2026 · Produkcja 4 listopada 2026

**Reguły transformacji i layouty**

- Silnik reguł dla wyekstrahowanych wartości pól i kolumn: ustawianie,
  zastępowanie lub wyprowadzanie wartości z zagnieżdżonymi grupami warunków,
  wraz z ekranem ustawień do zarządzania regułami. Warunek „jest jednym z”
  przyjmuje kilka wartości, listę reguł można przeszukiwać według
  identyfikatora reguły, a reguły działają także po wyszukaniu w danych
  podstawowych.
- Reguły wyboru layoutu otrzymują te same zagnieżdżone warunki oraz opcjonalny
  log wykonania. Wybór layoutu działa niezależnie od tego, skąd pochodzi
  dokument.
- Zarządzanie layoutami, niestandardowe reguły walidacji i reguły
  transformacji nie wymagają już przełącznika beta.
- Jasne reguły pierwszeństwa dla etykiet pól nagłówka i kolumn tabeli.
  Użytkownicy mogą tworzyć własne klucze tłumaczeń dla ustawień pól i kolumn
  tabeli.
- Kolumnę tabeli można ponownie przypisać po jej usunięciu, a tabela cen
  artykułów dostawcy pokazuje wszystkie swoje kolumny.

**Ekrany zatwierdzania i walidacji**

- Trzy tabele pozycji na ekranie zatwierdzania (pozycje faktury, pozycje
  porównania, dopasowywanie PO) mają jeden wspólny styl.
- Ostatnio otwarty panel boczny (kanał aktywności lub historia zatwierdzeń)
  jest zapamiętywany dla każdego użytkownika.
- Scalanie dokumentów z ekranu zatwierdzania za pomocą modułu przesyłania
  dokumentów.
- Niestandardowe reguły walidacji obsługują koszty wysyłki w sposób ogólny,
  pokazują komunikat przy polu zamiast ogólnego błędu, gdy wymagane pole jest
  puste, a reguły zgłaszające fałszywie negatywny wynik zostały poprawione.
  Domyślne reguły systemowe można duplikować.
- Niezgodność między ilością a kwotą netto w tabeli wyekstrahowanej przez AI
  jest zgłaszana, faktura z dopasowanym zamówieniem zakupowym nie jest już
  klasyfikowana jako faktura kosztowa, a data przeformatowana przez regułę
  jest akceptowana.
- Naprawiono ekran zatwierdzania, który po zatwierdzeniu lub odrzuceniu
  zawieszał się na nakładce ładowania. Pasek ładowania zastępuje zwykłą ikonę
  ładowania, a adresy URL stron są przyjaźniejsze.
- Otwarcie linku do dokumentu po wygaśnięciu sesji prowadzi do strony
  logowania zamiast do błędu 404.

**Wykrywanie duplikatów**

- Pola niestandardowe pojawiają się w wyniku wykrywania duplikatów, a
  ustawienia duplikatów można przeszukiwać.
- „Block Duplicate Document Export” blokuje eksport wykrytego duplikatu.

**Workflow i zadania**

- Przycisk „Nowy workflow”, logi zaawansowanych workflow, czytelniejszy ekran
  logów watchdoga, a kroki workflow zmieniające pole lub pole wyboru są
  stosowane niezawodnie.
- Dodanie pozycji w drzewie decyzyjnym zachowuje nazwy użytkowników, zamiast
  pokazywać identyfikatory.
- Każda zmiana statusu dokumentu jest rejestrowana.
- Tworzenie nowego szablonu e-mail znów działa.
- Lista zadań pokazuje swoje zadania przy pierwszym załadowaniu.

**Import**

- Import e-mail przenosi wiadomość ze skrzynki odbiorczej dopiero po
  potwierdzeniu przesłania, traktuje ponownie dostarczone przekazanie jako
  jedno dostarczenie, rejestruje, kto ostatnio zapisał, i wymienia załącznik
  raz, z podaniem powodu, gdy się nie powiedzie.
- Import FTP i SFTP otrzymuje prawdziwą opcję usuwania po imporcie obok
  przenoszenia i archiwizowania. Hasła nie ulegają już uszkodzeniu przy
  edycji konfiguracji, test połączenia działa dla nowych połączeń SFTP, a
  nieudane połączenie SFTP lub błędne logowanie pokazuje konkretny komunikat
  zamiast ogólnego błędu.
- Administratorzy są informowani w Settings Assistant, gdy skonfigurowany
  import FTP lub e-mail przestaje działać.
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
- Faktura kosztowa z dwiema stawkami VAT zachowuje obie pozycje księgowe.

**Dopasowywanie zamówień zakupowych**

- Dopasowywanie wymaga kolumny ilości, używa ceny za ilość w jednostce
  bazowej, a rezerwowe dopasowanie do ostatniej pozycji można włączać lub
  wyłączać dla każdego klienta.
- Pozycje dowodu dostawy można wybierać pojedynczo.
- Ekran e-dokumentu nie zawiesza się już na fakturach z ponad 250 pozycjami.

**Touchless Intelligence**

- Więcej szczegółów w raporcie Touchless, a pole wyboru Touchless
  odzwierciedla zapisane ustawienie.

**Pulpit, konta i subskrypcja**

- Pulpit może pomieścić do 10 000 dokumentów na wyszukiwanie, a niestandardowy
  filtr daty jest stosowany poprawnie.
- Termin płatności ze skontem i termin płatności faktury są dostępne jako
  pola layoutu i wypełniane przy imporcie.
- Użytkownicy, którym udostępniono pulpit, są zachowywani przy zapisie
  pulpitu, a „Updated by” pokazuje właściwą osobę.
- Zarchiwizowane dokumenty można z powrotem przenieść ze statusu „Archived”.
- Użytkownicy mogą znów się logować po zresetowaniu hasła.
- Strona planu subskrypcji pokazuje wykorzystanie planu i jego funkcji.

**Eksport i EDI**

- Dodatkowy krok eksportu do Infor M3 dla dodatkowych informacji o fakturze.
- Lista pakunkowa z kilkoma numerami kontenerów jest eksportowana jako jeden
  rekord na kontener.
- Ponowny import przyjęcia dostawy nie kończy się już błędem zduplikowanego
  klucza, a dokumenty BOD przyjęcia dostawy są stosowane we właściwej
  kolejności.
- Zaktualizowano mapowania EDI dla faktury, zamówienia zakupowego i
  potwierdzenia zamówienia.
- Test połączenia nowej konfiguracji eksportu Infor IDM lub Infor LN działa.

**Bezpieczeństwo**

- Kontrola organizacji dla kluczy API jest egzekwowana w każdym środowisku.

---

## R1.2 — Sandbox 16 lutego 2027 · Produkcja 3 marca 2027

**Zatwierdzanie i dopasowywanie zamówień zakupowych**

- Stan „Pending input” wstrzymuje dokument, dopóki ktoś nie odpowie, bez
  naruszania workflow ani historii audytu, a osoby zatwierdzające mogą
  zadawać pytania bez przerywania procesu zatwierdzania.
- Dokument można przypisać ponownie do innego użytkownika (pierwsza faza).
- Faktury zaliczkowe można dopasowywać przed przyjęciem towaru, podczas gdy
  opcja „Match on received quantity” pozostaje aktywna.
- Ekran dopasowywania oferuje tylko pozycje PO, które mogą pasować, a
  dopasowania wielu pozycji z pominięciem porównania cen nadal pokazują cenę
  jednostkową na ekranie zatwierdzania.
- Flaga dostępności przyjęcia porównuje ilości zafakturowane i przyjęte.
- Potwierdzenia zamówień: elementy kosztowe pokazywane w trakcie oczekiwania
  na zatwierdzenie, oznaczone kolorami pozycje dopłat w dopasowywaniu PO oraz
  kolumna numeru artykułu w pozycjach faktury.
- Obsługiwane są pozycje RMA dostawcy.

**Import i klasyfikacja**

- Typ dostawcy jest wyprowadzany z pozycji dokumentu.
- Formularz zgłoszenia do wsparcia przyjmuje załączniki i automatycznie
  przypisuje organizację.

**Ustawienia i automatyzacja**

- Skrypt „Set sub-organisation” staje się regułą transformacji.
- Standardowe kolumny można usuwać z typu dokumentu.

**Eksport**

- Historia eksportu znów wymienia wyeksportowane dokumenty.
- Faktury frachtowe są eksportowane do Infor LN.
- Konfigurowalne nazwy plików eksportu.
- Rozszerzona integracja podatkowa z Vertex.

---

## R1.3 — Sandbox 1 czerwca 2027 · Produkcja 16 czerwca 2027

**Auto Accounting Rule Manager**

- Reguły automatycznie przypisują konta i wymiary, w zakresie podorganizacji
  i typu dokumentu, wraz z ekranem audytu, który pokazuje, która reguła
  zadziałała.
- Reguła może wyszukiwać dane podstawowe i przypisywać kilka pól naraz albo
  wypełniać wartość z kolumny pozycji tabeli.
- Pola i wymiary można czyścić pojedynczo, pozycje można usuwać (także
  pozycje bez kwoty), a reguły działają dalej na polach, które zmieniły się
  z tekstu na listę rozwijaną.
- Predykcje obsługują wiele kodów podatkowych i wymiarów, vouchery oraz
  referencje księgowań. Ekrany Auto Accounting są dostępne w kilku językach.

**Dopasowywanie zamówień zakupowych**

- Ikona dopasowania nawiguje, przewija i podświetla między zakładkami,
  włącznie z dopasowaniami jeden-do-wielu.
- Konwersja jednostek z aliasami (na przykład KG i TO), konfigurowalna
  tolerancja zaokrągleń z kontem zaokrągleń oraz obliczenia z czterema
  miejscami po przecinku wyświetlane jako trzy.

**Użyteczność**

- Kolejność wykonywania skryptów dokumentu jest widoczna we frontendzie.
- Klawisze Enter i Tab przenoszą między polami.

**Eksport**

- Niekompletny dokument w Infor LN jest usuwany po nieudanym eksporcie.
- Konektor bazy danych obejmuje wszystkie istotne tabele.

---

## R1.4 — Sandbox 5 października 2027 · Produkcja 20 października 2027

**Auto Accounting na ekranie zatwierdzania**

- Osoby zatwierdzające mogą korzystać z Auto Accounting bezpośrednio na
  ekranie zatwierdzania.
- Zatwierdzenie może być uzależnione od pól księgowych, takich jak kod konta
  księgowego lub kraj, z korektą po stronie AP, gdy dokument zostaje
  zwrócony.
- Lista rozwijana kodów podatkowych w Auto Accounting bez konieczności
  konfigurowania wielu pozycji podatkowych.
- Wymiary są przechowywane w nowej strukturze, dzięki czemu duże zestawy
  wymiarów ładują się szybciej, a Rule Manager otrzymuje rundę opinii.

**Zatwierdzanie**

- Ulepszony proces zatwierdzania, delegowanie do innego użytkownika w trakcie
  zatwierdzania oraz przycisk „Export & Next”.

**Dopasowywanie zamówień zakupowych i zabezpieczenia eksportu**

- Faktury z nadmiernym dopasowaniem, w których zafakturowana ilość przekracza
  ilość przyjętą, są rozpoznawane na ekranie dopasowywania, a jednostki miary
  są konwertowane podczas dopasowywania faktury.
- Kody opłat (myto, transport, energia) są rozpoznawane, a ich koszt jest
  rozdzielany.
- Eksport jest blokowany z ostrzeżeniem, gdy dopasowana ilość przekracza
  przyjętą ilość lub zbyt mocno się od niej różni, albo gdy data księgowania
  jest wcześniejsza niż data wpisu magazynowego.

**Import i ustawienia**

- Mechanizm ponawiania dla importu FTP, e-mail i przychodzących wiadomości
  e-mail, z automatycznym i ręcznym ponownym przetwarzaniem; adres nadawcy
  jest dostępny z importu e-mail.
- Ustawienia można przeszukiwać we wszystkich przełącznikach i podstronach.
- Konfiguracja serwera e-mail pozwala zastąpić wygasły sekret OAuth lub
  sekret klienta bez ponownego konfigurowania skrzynki pocztowej.
- Mapę numerów artykułów dostawcy (tabelę konwersji numerów artykułów) można
  wypełnić z importu CSV.
- Historię zatwierdzeń można eksportować przez eksport SFTP.

**DocNet Agents**

- Przyjmowanie zamówień: zamówienie klienta staje się zleceniem sprzedaży w
  Infor M3 lub Infor LN (pierwsza wersja, dokumenty tekstowe).

<!-- Generated from Jira "Release No." (customfield_10392) on 2026-10-07 by the
     docbits-roadmap skill. Releases up to R1.4 only; R1.5 and later are not
     published yet. Themes only; ticket keys, customer names and internal work
     are deliberately left out. Rerun the skill to refresh. -->
