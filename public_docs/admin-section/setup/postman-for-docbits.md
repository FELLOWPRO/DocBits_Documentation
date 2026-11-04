# Postman dla DocBits

Ten przewodnik pokaże Ci, jak wysyłać żądania HTTP do Twojej organizacji DocBits za pomocą Postmana. Jest łatwy w użyciu i bardzo przydatny dla administratorów organizacji.

## Konfiguracja

Najpierw pobierz Postmana na swój system i zaloguj się/zarejestruj.

Teraz postępuj zgodnie z tym przewodnikiem krok po kroku, aby dowiedzieć się, jak działają żądania HTTP w Postmanie.

Autoryzacja w Postmanie

Zanim będziesz mógł tworzyć żądania HTTP, musisz wprowadzić swój klucz API z DocBits, aby je autoryzować.

* Kliknij zakładkę \`Authorization\` i wybierz \`Klucz API\` jako typ autoryzacji.

![](https://lh7-us.googleusercontent.com/L3GaBZJvReeINaKbkq3VYQ9UHTBoKUA3nJkfyLqk61q5xaOJnmMLhbrEbgUgLEyYRkewHuLIAVzoYCZ6quHq0pwx\_69FEYJjzYllivB8WzdAtTFSrzl8VeFthbMsEB9sGjcGlVN38DXEXUwuNEPL6hg)

* Wypełnij wartości. Wprowadź “X-API-key” w polu \`Klucz\` oraz Twój klucz API jako wartość (znaleziony w menu Ustawienia DocBits pod Integracją). Wybierz Dodaj do \`Nagłówka\`.

&#x20;

* Powinno to wyglądać tak:

![](https://lh7-us.googleusercontent.com/SmNfci4z8ECTeXzFPE9YQ8nCzCRHglc\_7RR1cN8a8F7KvYWjJcBnY5wpl7q0AV8bfNLkMk8F4F4aw8j4xMK50HJweBRBPo8EasTn-FG-fmlUJQ41aUX-dvTeWP\_xJQThi8A6EwJl3qIc-Dw1B5W9fVE)

### API DocBits

Dostępne pod adresem https://api.polydocs.io

* Kliknij na Autoryzuj w prawym górnym rogu

![](https://lh7-us.googleusercontent.com/kuztHpkmRWlOYSU27r97KH15SJHPF\_hn\_eX3C1DYLVYCwMHXfLjYSyFubUCvlQiBt5q3xY0XBPmkcP6AnKF2C0Mdtx3tg\_dU\_qxqAmI6axYIsXR36\_YBz6j455K3-c2SBu4YzmYIXq8VXQxzgL-0j90)

* Wprowadź swój klucz API i potwierdź, klikając \`Autoryzuj\`

![](https://lh7-us.googleusercontent.com/zLhgpdjMnxqNBdjgtDxFEKglICIZul7dgmfFFm2hSnsDQ-HsZHRKRikZ0lcanGYkkZj4waC85mEUFO951ydVnY\_\_m\_TrMrsK3vrDv9FKL-adgWL4lJqp3cSxPeClBm9IHG2cXinRsv12xTeh3psQfO4)

### Utwórz nową Przestrzeń Roboczą w Postmanie

* Kliknij na Przestrzenie Robocze i utwórz nową przestrzeń roboczą (możesz nazwać ją jak chcesz)

![](https://lh7-us.googleusercontent.com/3rZw7jhOgVpkZuer58fPEKqDspJjK3S1lp3XpQuvE4c9212a0ALB-p7oLRwPqEbj10MpoCWsb7V9fPqiAdVvigE00x9mN5-lHFXZVVxlkeroBJd2ratgkJVJDM4LJkUJsycyl6tnFKazcFPY-vWtH2Q)

* Musisz wybrać widoczność, która określa, kto może uzyskać dostęp do tej przestrzeni roboczej.

![](https://lh7-us.googleusercontent.com/ZajvDtMvfM5J\_Go3n\_PgzD3RXTMQAlST8\_3WnsTQ4-iw7e0QdAa3wqFk7Y0gt78IJVjNTN-5E72c1127CpXJWb8WbfDolxENLqxg5VZLPEK7-hxsNwbAyMceSHfeVy6v-b9QT0kFwnMibWndEAJ2lXA)

* Po dokonaniu wyboru i kliknięciu \`Utwórz Przestrzeń Roboczą\` wybierz Kolekcje po lewej stronie aplikacji i utwórz nową kolekcję dla Twoich żądań HTTP, klikając \`+\`.

![](https://lh7-us.googleusercontent.com/mbC5t86vaB2G7FQp-40XN-SHc019LKitfUeXRzbcG4HpNai5FPapShx9swHX3mz0va8QFsUQiYn-bhjvER0XYOEDRJpI9x3wG4NgRZCd4beU1NyKJd86bSGubxVbRCtz8HkTDZd28Z7Ice3rmscFMMo)

W tej kolekcji możesz dodać wiele żądań HTTP. Aby to zrobić, kliknij na 3 kropki kolekcji i wybierz \`Dodaj żądanie\`.

![](https://lh7-us.googleusercontent.com/S5W75clJz7JqoIWPbKBjrJqpTAwjS51Pu4dTU160Q7i6oW-HPnb7aN8WRK2AyAb6-HEqTYMZTy9563P0sq53MAjGpVg1JivZX2ATHa6GeFbTX2UCjud7ot8Y\_ksBuUbUfyEfxIDziV8TN3zDfX9Se58)

## Przykład metody "GET"

Metoda GET jest bardzo przydatna do uzyskiwania informacji o użytkownikach, suborganizacjach, przetworzonych dokumentach i wiele więcej.

* Wybierz metodę GET w swoim żądaniu HTTP.
* Autoryzuj się, jak opisano powyżej.
* Otwórz https://api.polydocs.io i dodaj ścieżkę funkcji za adresem URL Polydocs. Na przykład:

![](https://lh7-us.googleusercontent.com/pIdgyqP7g1UwZbY5yaz1KAnKe\_ESs\_kQyiWAXXM-ukRKakS\_\_OL\_LS9J-07hZnZDf8QqtoN\_lKyuhvOIIIF-4Wp0dkofZYQwXZ0hu2RM0YogRxJah-zf8W\_cDNFf8xsec1tYIsfe0SpBuvdCG4WHMU0)

* Teraz wklej ten link do pola tekstowego obok metody GET w Postmanie.

Kliknij \`Wyślij\` i powinieneś otrzymać wszystkie informacje o każdym użytkowniku w Twojej organizacji.

## Przykład metody "POST"

Metoda POST jest zazwyczaj używana do tworzenia użytkowników lub organizacji, na przykład. Ta metoda wstawia informacje do bazy danych.

Utwórz Użytkownika

* Wybierz metodę POST.
* Autoryzuj się, jak opisano powyżej.
* Otwórz https://api.polydocs.io i dodaj ścieżkę funkcji za adresem URL Polydocs. W tym przypadku:

![](https://lh7-us.googleusercontent.com/Gwabl4pN0k0NanHsFOzJj9s2H7ExS-JcWr-Y4EW0FLUYHfnaOZoMWvldJ6yDI33p\_DThVx0Rd5bi59XdOK11l1knc5rd-E5HXMw6v5E3qvHvKVWHlp21S728SVye6KU2W5ZeXtCIOzxBAcMlA2UNFfQ)

* Teraz wklej ten link do pola tekstowego obok metody POST w Postmanie.
* Wybierz zakładkę \`Body\` w swoim żądaniu HTTP i wprowadź klucze i wartości dla każdej poświadczenia, które ma czerwoną gwiazdkę obok swojej nazwy.

Po zakończeniu powinno to wyglądać tak:

![](https://lh7-us.googleusercontent.com/lSExzZSbTcSRvuLDw0HNYE62yI7xs0eUewKuOcABCGYfsRBRbGz1lJxopR4QdUEoniCnZ83FKpz-AHLORP5cXGPrPhgouzE6zO920jA7A3r-Y14wY\_Gc3C98R2fcxXsWRMcle9qT981YWhCnjlUukPE)

Jeśli chcesz utworzyć konto administratora, ustaw wartość \`is\_admin\` na true.

&#x20;Wreszcie, kliknij \`Wyślij\` i zobaczysz wszystkie poświadczenia, które ustawiłeś w odpowiedzi poniżej. Oznacza to, że użytkownik został utworzony.
### Prześlij dokument

Możesz również użyć metody POST do przesłania dokumentu do DocBits.

* Wybierz metodę POST.
* Autoryzuj się, jak opisano powyżej.
* Otwórz https://api.polydocs.io i dodaj ścieżkę funkcji za adresem URL Polydocs.&#x20;

W tym przypadku:

![](https://lh7-us.googleusercontent.com/-EwhMeH\_WXYVmMKus1-IZKLZNyTcYktcf\_YUT\_m2nfStfKXuBxKBb1MZfUIQCN4ZxNKQkNhvO\_pgnt1EUhNB34qG5AOe4wM0OxGRMQsV9a8h0XUgabqq8mLQhza\_AE7gxBetmb9bJmaWBQqEXrWT0VI)

* Teraz wklej ten link do pola tekstowego obok metody POST w Postmanie.
* Wybierz zakładkę \`Body\` w żądaniu HTTP i wybierz \`form-data\`

![](https://lh7-us.googleusercontent.com/TNrKlyorn\_5YrIu5r4vcfyYgAnfhsl-SRVqWg9RoN0X1pUjXtn6J0EI7aeQ-oc2ZtFeTj8POcMXy6CwXzI1jhv-ufb2u7d80SC-lbGXmnx\_jVDunAbRw1jqAsB4PPsEzcFIOPeH5PJZvytUW2kIDYZ4)

![](https://lh7-us.googleusercontent.com/scAJpTSCqYSKYNNGPIrEsL0zDJIa7Dhe9tpqv\_zDjdLyAydugzdGA1s93njbFOOVbVbQf7oDEtRc14Kt4p1TXX8A--WjvRgeXWsAxDNWdrCN2-QDeya6-FFEG4\_-dhYgrj4yrVYllJs8eZsUgKOPvzo)

Wprowadź plik do pola \`KEY\`, gdzie znajdziesz ukryty rozwijany przycisk Plik. Wybierz \`Plik\` i przejdź do pola \`VALUE\`, gdzie możesz wybrać swój plik, klikając \`Wybierz pliki\`.

Po kliknięciu przycisku \`Send\`, powinieneś zobaczyć "success": true w odpowiedzi.

Powinno to wyglądać tak:

![](https://lh7-us.googleusercontent.com/hNtG\_uTWgxww7iOmHLhnDqdrTlHCI1rk31LozG4l2DLPqxzSn9HoKn8CQIjeBgJLV4bxrGCjWOMRykJ3qBdZLYwxrZJGq\_S3tjVwSZmGTiMgVoqM97TTQjmW8CegEL2FV309NBmV0Fv\_vciSdQRFiOI)

## Przykład metody "DELETE"

Metoda DELETE służy do usuwania, na przykład użytkowników, organizacji itp.

* Wybierz metodę DELETE.
* Autoryzuj się, jak opisano powyżej.
* Otwórz https://api.polydocs.io i dodaj ścieżkę funkcji za adresem URL Polydocs.

&#x20;Na przykład:

![](https://lh7-us.googleusercontent.com/-QqSVIELl1IkxYK\_gGDa7nIv\_B1IvO3OjT3Ge6bAXwPl6jVDETuzXwtYJdRSmqLEP2d6B0L6MuwZvgJpI968pzp1APmJmuQ\_qlqYgZZhesocYCJVMCHhIZAKmlvMybUkUGXYZtySrnEbRTwWTritvKo)

* Teraz wklej ten link do pola tekstowego obok metody DELETE w Postmanie.
* Zamień {user\_id} na końcu adresu URL na rzeczywiste ID użytkownika, którego chcesz usunąć. (Możesz uzyskać user\_id, używając metody GET).
* Jeśli zawarłeś user\_id w adresie URL, nie musisz dodawać klucza i wartości ciała.
* Po kliknięciu przycisku \`Send\`, powinieneś zobaczyć "success": true w odpowiedzi.

&#x20;Powinno to wyglądać tak:

![](https://lh7-us.googleusercontent.com/X8WNtsC9v7jqDIiaVhauJUgZK0yTC1GVz9rBptdiCxyLUiEEfbpIoYHpK7NvlDMTkhgiPyBb22H9GOfDdvmL-dakouTjuRDPwX4YX0Jz5IIo6eHu-wnw1S4jJd5ylHyffUXWKwX6ovDnp\_2WEAtSha4)

## Przykład metody "PUT"

Metoda PUT jest głównie używana do aktualizacji danych użytkownika lub organizacji. Jest bardzo łatwa do zrozumienia i użycia.

* Wybierz metodę PUT.
* Autoryzuj się, jak opisano powyżej.
* Otwórz https://api.polydocs.io i dodaj ścieżkę funkcji za adresem URL Polydocs.

&#x20;Na przykład:

![](https://lh7-us.googleusercontent.com/tC3qtPbFb1GsK6dBmB5Jrv5HqFOYLxNR1XB0PEuA8ipkHnH2ZQ6xrrkImNgbGSMoA6aAGvLr6K3cI4u\_qM96BOvR7AnQzmX17HBMBneNpLBc6RIzspfTYgrCWSj0fSE9mSWLIex3hc\_R-m-PI6zT6Rs)

* Teraz wklej ten link do pola tekstowego obok metody PUT w Postmanie.
* Zamień {user\_id} na końcu adresu URL na rzeczywiste ID użytkownika, którego chcesz usunąć. (Możesz uzyskać user\_id, używając metody GET).

## Zmiana adresu e-mail użytkownika

* W ciele wpisz „email” jako klucz i nowy adres e-mail jako wartość.
* Następnie po prostu naciśnij przycisk \`Send\` i powinieneś zobaczyć „success” w odpowiedzi.
