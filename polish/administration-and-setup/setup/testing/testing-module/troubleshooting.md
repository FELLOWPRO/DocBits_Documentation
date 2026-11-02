# Rozwiązywanie problemów

## Nie mogę znaleźć Testing w Ustawieniach

Strona jest widoczna tylko dla administratorów organizacji. Zwróć się do administratora organizacji w Twojej organizacji.

## Strona informuje, że Testing jest wyłączony

Administrator organizacji musi włączyć **Włącz moduł Testing dla organizacji** u góry strony.
Do tego czasu nic nie jest uruchamiane, także z asystenta AI ani z zewnątrz.

## Mój przebieg się nie powiódł

Otwórz dziennik w zakładce **Dziennik** i sprawdź pierwszy nieudany krok oraz jego kod błędu:

| Co widzisz | Zwykle oznacza | Co zrobić |
|---|---|---|
| Element nie znajduje się na stronie lub nie jest widoczny | Strona wygląda inaczej w Twojej organizacji lub ładuje się wolno | Otwórz stronę samodzielnie i sprawdź ją; dostosuj własny szablon lub sprawdź wartości danych wejściowych |
| Pole lub status się nie zgadza | Dokument ma inną wartość, niż oczekują dane wejściowe | Sprawdź dokument; popraw oczekiwaną wartość w danych wejściowych |
| Nie udało się otworzyć strony | Błędny identyfikator dokumentu lub brak uprawnień | Sprawdź identyfikator w danych wejściowych oraz uprawnienia użytkownika, który uruchomił kartę |
| Przekroczono limit czasu | Krok lub cały test trwał za długo | Uruchom ponownie; jeśli problem się powtarza, sprawdź wydajność strony |
| Zablokowane przez środowisko | Test zapisuje dane w środowisku klienta | Potwierdź uruchomienie lub uruchom test w środowisku testowym |

## Mój przebieg jest „Zablokowany”

Przebiegu nie dało się ocenić: niektóre kroki zostały pominięte (na przykład krok ze zrzutem ekranu, którego przeglądarka nie może wykonać)
albo brakuje potwierdzenia. Zablokowany przebieg nigdy nie jest liczony jako zaliczony. Usuń krok z własnego szablonu lub
uruchom test ponownie z potwierdzeniem.

## „Zarejestruj sesję przeglądarki, aby rozpocząć” / żadna karta nie przyjmuje uruchomień

Uruchamianie z asystenta AI lub z zewnątrz wymaga karty przeglądarki z włączoną opcją **Zezwól na uruchamianie z zewnątrz**. Otwórz
zakładkę Dane wejściowe w karcie, która pozostaje otwarta, włącz tę opcję i użyj jej identyfikatora sesji. Przeładowanie kończy rejestrację.

## Przebieg zatrzymał się lub pokazuje Anulowany / Niedostarczony

Karta, która wykonywała test, została przeładowana, zamknięta lub utraciła połączenie albo żadna karta nie odpowiedziała na czas. Pozostaw kartę otwartą
i na pierwszym planie do końca przebiegu, a potem uruchom test ponownie. Test z krokiem **Załaduj stronę ponownie** kończy się w ten sam sposób także wtedy, gdy strona nie wróci w ciągu około dwóch minut
(zobacz [Ponowne załadowanie i wznowienie](reload-and-resume.md)).

## „Szablonów Playwright nie można jeszcze tutaj uruchomić”

Szablony, których **Wykonawca** to **Playwright**, są uruchamiane przez Twoją automatyzację testów. Możesz dla nich zapisywać dane wejściowe, ale
nie możesz ich uruchomić z tej strony.

## Nie mogę usunąć szablonu

Usunąć można tylko własne szablony Twojej organizacji (**Niestandardowy**). Szablonów wbudowanych i domyślnych nie można usunąć; użyj
**Edytuj kopię**, aby uzyskać własną wersję.
