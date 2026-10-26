# Postman dla DocBits

W tym przewodniku dowiesz się, jak wysyłać żądania HTTP do swojej organizacji DocBits za pośrednictwem Postman. Jest łatwy w użyciu i bardzo przydatny dla administratorów organizacji.

## Konfiguracja

Najpierw pobierz Postman do swojego systemu i zaloguj się/zarejestruj się.

Teraz postępuj zgodnie z tym przewodnikiem krok po kroku, aby dowiedzieć się, jak żądania HTTP działają w Postman.

Authorization in Postman

Zanim będziesz mógł utworzyć swoje żądania HTTP, musisz wprowadzić klucz API z DocBits, aby je autoryzować.

* Kliknij zakładkę \`Authorization\` i jako typ autoryzacji wybierz \`API Key\`.

![Żądanie Postman z otwartą kartą Authorization i listą Type z pozycjami Inherit auth from parent, Bearer Token, Basic Auth, Digest Auth, OAuth 1.0 i OAuth 2.0](https://lh7-us.googleusercontent.com/L3GaBZJvReeINaKbkq3VYQ9UHTBoKUA3nJkfyLqk61q5xaOJnmMLhbrEbgUgLEyYRkewHuLIAVzoYCZ6quHq0pwx\_69FEYJjzYllivB8WzdAtTFSrzl8VeFthbMsEB9sGjcGlVN38DXEXUwuNEPL6hg)

* Wypełnij wartości. Wpisz “X-API-key” w polu \`Key\` i swój klucz API jako wartość (znaleziony w menu Ustawienia DocBits w obszarze Integracja). Wybierz opcję Dodaj do \`Header\`.

&#x20;

* Powinno to wyglądać tak:

![Karta Authorization w Postmanie z typem API Key, kluczem x-api-key, polem Value dla klucza API i wyborem Header w Add to](https://lh7-us.googleusercontent.com/SmNfci4z8ECTeXzFPE9YQ8nCzCRHglc\_7RR1cN8a8F7KvYWjJcBnY5wpl7q0AV8bfNLkMk8F4F4aw8j4xMK50HJweBRBPo8EasTn-FG-fmlUJQ41aUX-dvTeWP\_xJQThi8A6EwJl3qIc-Dw1B5W9fVE)

### API DocBits

Available at https://api.polydocs.io

* Kliknij Autoryzuj w prawym górnym rogu

![Przycisk Authorize w prawym górnym rogu widoku API w Postmanie](https://lh7-us.googleusercontent.com/kuztHpkmRWlOYSU27r97KH15SJHPF\_hn\_eX3C1DYLVYCwMHXfLjYSyFubUCvlQiBt5q3xY0XBPmkcP6AnKF2C0Mdtx3tg\_dU\_qxqAmI6axYIsXR36\_YBz6j455K3-c2SBu4YzmYIXq8VXQxzgL-0j90)

* Wprowadź swój klucz API i potwierdź, klikając \`Authorize\`

![Okno Available authorizations z pozycją APIKeyHeader typu apiKey, nazwą X-API-KEY, In header, pustym polem Value i przyciskiem Authorize](https://lh7-us.googleusercontent.com/zLhgpdjMnxqNBdjgtDxFEKglICIZul7dgmfFFm2hSnsDQ-HsZHRKRikZ0lcanGYkkZj4waC85mEUFO951ydVnY\_\_m\_TrMrsK3vrDv9FKL-adgWL4lJqp3cSxPeClBm9IHG2cXinRsv12xTeh3psQfO4)

### Tworzenie nowej przestrzeni roboczej w Postman

* Kliknij Obszary robocze i utwórz nowy obszar roboczy (możesz nadać mu dowolną nazwę

![Przegląd obszarów roboczych w Postmanie z przyciskiem Create Workspace i listą ostatnio odwiedzonych obszarów](https://lh7-us.googleusercontent.com/3rZw7jhOgVpkZuer58fPEKqDspJjK3S1lp3XpQuvE4c9212a0ALB-p7oLRwPqEbj10MpoCWsb7V9fPqiAdVvigE00x9mN5-lHFXZVVxlkeroBJd2ratgkJVJDM4LJkUJsycyl6tnFKazcFPY-vWtH2Q)

* Musisz wybrać widoczność, która określa, kto może uzyskać dostęp do tego obszaru roboczego.

![Okno Create workspace z polami Name i Summary, opcjami widoczności Personal, Private, Team, Partner i Public oraz przyciskami Create Workspace i Cancel](https://lh7-us.googleusercontent.com/ZajvDtMvfM5J\_Go3n\_PgzD3RXTMQAlST8\_3WnsTQ4-iw7e0QdAa3wqFk7Y0gt78IJVjNTN-5E72c1127CpXJWb8WbfDolxENLqxg5VZLPEK7-hxsNwbAyMceSHfeVy6v-b9QT0kFwnMibWndEAJ2lXA)

* Po dokonaniu wyboru i kliknięciu \`Create Workspace\` wybierz Kolekcje po lewej stronie aplikacji i utwórz nową kolekcję dla swoich żądań HTTP, klikając \`+\`.

![Panel boczny Postmana z grupą Collections i pozycją New Collection do tworzenia kolekcji](https://lh7-us.googleusercontent.com/mbC5t86vaB2G7FQp-40XN-SHc019LKitfUeXRzbcG4HpNai5FPapShx9swHX3mz0va8QFsUQiYn-bhjvER0XYOEDRJpI9x3wG4NgRZCd4beU1NyKJd86bSGubxVbRCtz8HkTDZd28Z7Ice3rmscFMMo)

W tej kolekcji możesz dodać wiele żądań HTTP. Aby to zrobić, kliknij 3 punkty kolekcji i wybierz \`Add request\`.

![Menu kontekstowe kolekcji w Postmanie z pozycjami Share, Move, Run collection, Edit, Add request, Add folder, Monitor collection, Mock collection, Create a fork, Create pull request, Merge changes i Pull changes](https://lh7-us.googleusercontent.com/S5W75clJz7JqoIWPbKBjrJqpTAwjS51Pu4dTU160Q7i6oW-HPnb7aN8WRK2AyAb6-HEqTYMZTy9563P0sq53MAjGpVg1JivZX2ATHa6GeFbTX2UCjud7ot8Y\_ksBuUbUfyEfxIDziV8TN3zDfX9Se58)

## Przykład metody "GET"

Metoda GET jest bardzo przydatna do uzyskiwania informacji o użytkownikach, podorganizacjach, przetwarzanych dokumentach i wielu innych.

* Wybierz metodę GET w swoim żądaniu HTTP.
* Autoryzuj się w sposób opisany powyżej.
* Otwórz https://api.polydocs.io i dodaj ścieżkę funkcji za Polydocs URL. Na przykład:

![Dokumentacja API dla operacji GET /users/get_users o tytule Get Users z sekcją Parameters bez pozycji i sekcją Responses z kodem 200 Successful Response](https://lh7-us.googleusercontent.com/pIdgyqP7g1UwZbY5yaz1KAnKe\_ESs\_kQyiWAXXM-ukRKakS\_\_OL\_LS9J-07hZnZDf8QqtoN\_lKyuhvOIIIF-4Wp0dkofZYQwXZ0hu2RM0YogRxJah-zf8W\_cDNFf8xsec1tYIsfe0SpBuvdCG4WHMU0)

* Teraz wklej ten link w polu tekstowym obok metody GET w Postman.

Kliknij \`Send\`, a powinieneś otrzymać wszystkie informacje o każdym użytkowniku w Twojej organizacji.

## Przykład metody "POST"

Metoda POST jest zwykle używana na przykład do tworzenia użytkowników lub organizacji. Ta metoda wstawia informacje do bazy danych.

Create User

* Wybierz metodę POST.
* Autoryzuj się w sposób opisany powyżej
* Otwórz https://api.polydocs.io i dodaj ścieżkę funkcji za Polydocs URL. W tym przypadku:

![Dokumentacja API dla operacji POST /users/create o tytule Create User z wymaganymi polami first_name, last_name, email i password w treści żądania oraz polem logicznym is_admin](https://lh7-us.googleusercontent.com/Gwabl4pN0k0NanHsFOzJj9s2H7ExS-JcWr-Y4EW0FLUYHfnaOZoMWvldJ6yDI33p\_DThVx0Rd5bi59XdOK11l1knc5rd-E5HXMw6v5E3qvHvKVWHlp21S728SVye6KU2W5ZeXtCIOzxBAcMlA2UNFfQ)

* Teraz wklej ten link w polu tekstowym obok metody POST w Postman.
* Wybierz zakładkę \`Body\` w swoim żądaniu HTTP i wprowadź klucze oraz wartości dla każdego uwierzytelnienia, którego nazwa jest oznaczona czerwoną gwiazdką.

Kiedy skończysz, powinno to wyglądać tak:

![Karta Body w Postmanie z wybranym form-data i wierszami first_name z First_Name, lastname z Last_Name, email z test@test.com, password oraz is_admin z False](https://lh7-us.googleusercontent.com/lSExzZSbTcSRvuLDw0HNYE62yI7xs0eUewKuOcABCGYfsRBRbGz1lJxopR4QdUEoniCnZ83FKpz-AHLORP5cXGPrPhgouzE6zO920jA7A3r-Y14wY\_Gc3C98R2fcxXsWRMcle9qT981YWhCnjlUukPE)

Jeśli chcesz utworzyć konto administratora, ustaw wartość \`is\_admin\` na true.

Na koniec kliknij \`Send\`, aby zobaczyć wszystkie dane uwierzytelniające ustawione w odpowiedzi poniżej. Oznacza to, że użytkownik został utworzony.

### Prześlij dokument

Możesz także użyć metody POST, aby przesłać dokument do DocBits.

* Wybierz metodę POST.
* Autoryzuj się w sposób opisany powyżej.
* Otwórz https://api.polydocs.io i dodaj ścieżkę funkcji za Polydocs URL.

W tym przypadku:

![Dokumentacja API dla operacji POST /document/process o tytule Process z opcjonalnymi polami source, org_id, priority, sub_org_id i metadata w treści żądania oraz wymaganym polem file typu string binary](https://lh7-us.googleusercontent.com/-EwhMeH\_WXYVmMKus1-IZKLZNyTcYktcf\_YUT\_m2nfStfKXuBxKBb1MZfUIQCN4ZxNKQkNhvO\_pgnt1EUhNB34qG5AOe4wM0OxGRMQsV9a8h0XUgabqq8mLQhza\_AE7gxBetmb9bJmaWBQqEXrWT0VI)

* Teraz wklej ten link w polu tekstowym obok metody POST w Postman.
* Wybierz zakładkę \`Body\` w swoim żądaniu HTTP i wybierz \`form-data\`

![Żądanie Postman POST https://api.polydocs.io/document/process z otwartą kartą Body, wybranym form-data i pustym wierszem KEY dla pliku](https://lh7-us.googleusercontent.com/TNrKlyorn\_5YrIu5r4vcfyYgAnfhsl-SRVqWg9RoN0X1pUjXtn6J0EI7aeQ-oc2ZtFeTj8POcMXy6CwXzI1jhv-ufb2u7d80SC-lbGXmnx\_jVDunAbRw1jqAsB4PPsEzcFIOPeH5PJZvytUW2kIDYZ4)

![Żądanie Postman POST https://api.polydocs.io/document/process z otwartą kartą Body, wybranym form-data i wierszem file o wartości Mango_invoice.pdf](https://lh7-us.googleusercontent.com/scAJpTSCqYSKYNNGPIrEsL0zDJIa7Dhe9tpqv\_zDjdLyAydugzdGA1s93njbFOOVbVbQf7oDEtRc14Kt4p1TXX8A--WjvRgeXWsAxDNWdrCN2-QDeya6-FFEG4\_-dhYgrj4yrVYllJs8eZsUgKOPvzo)

Wpisz plik w polu \`KEY\`, gdzie znajdziesz ukryte menu rozwijane Plik. Wybierz \`File\` i przejdź do pola \`VALUE\`, w którym możesz wybrać plik, klikając \`Select Files\`.

Po kliknięciu \`Send\` w odpowiedzi powinieneś zobaczyć “success”: true.

Powinno to wyglądać tak:

![Żądanie Postman POST https://api.polydocs.io/document/process ze statusem 200 OK i odpowiedzią JSON zawierającą success true, doc_id oraz nazwę pliku Mango_invoice.pdf](https://lh7-us.googleusercontent.com/hNtG\_uTWgxww7iOmHLhnDqdrTlHCI1rk31LozG4l2DLPqxzSn9HoKn8CQIjeBgJLV4bxrGCjWOMRykJ3qBdZLYwxrZJGq\_S3tjVwSZmGTiMgVoqM97TTQjmW8CegEL2FV309NBmV0Fv\_vciSdQRFiOI)

## Przykład metody "DELETE"

Metoda DELETE służy do usuwania np. użytkowników, organizacji i tak dalej.

* Wybierz metodę DELETE
* Autoryzuj się w sposób opisany powyżej.
* Otwórz https://api.polydocs.io i dodaj ścieżkę funkcji za Polydocs URL.

Na przykład:

![Dokumentacja API dla operacji DELETE /users/delete/{user_id} o tytule Delete User z parametrem ścieżki user_id](https://lh7-us.googleusercontent.com/-QqSVIELl1IkxYK\_gGDa7nIv\_B1IvO3OjT3Ge6bAXwPl6jVDETuzXwtYJdRSmqLEP2d6B0L6MuwZvgJpI968pzp1APmJmuQ\_qlqYgZZhesocYCJVMCHhIZAKmlvMybUkUGXYZtySrnEbRTwWTritvKo)

* Teraz wklej ten link w polu tekstowym obok metody DELETE w Postman.
* Zastąp {user\_id} na końcu URL rzeczywistym identyfikatorem użytkownika, którego chcesz usunąć. (Możesz uzyskać user\_id za pomocą metody GET).
* Jeśli umieściłeś user\_id w URL, nie musisz dodawać do niego klucza treści ani wartości.
* Po kliknięciu \`Send\` w odpowiedzi powinieneś zobaczyć “success”: true.

Powinno to wyglądać tak:

![Żądanie Postman DELETE https://api.polydocs.io/users/delete/508 ze statusem 200 OK i odpowiedzią JSON success true](https://lh7-us.googleusercontent.com/X8WNtsC9v7jqDIiaVhauJUgZK0yTC1GVz9rBptdiCxyLUiEEfbpIoYHpK7NvlDMTkhgiPyBb22H9GOfDdvmL-dakouTjuRDPwX4YX0Jz5IIo6eHu-wnw1S4jJd5ylHyffUXWKwX6ovDnp\_2WEAtSha4)

## Przykład metody "PUT"

Metoda PUT stosowana jest głównie do aktualizacji danych użytkownika lub organizacji. Jest bardzo łatwy do zrozumienia i użycia.

* Wybierz metodę PUT.
* Autoryzuj się w sposób opisany powyżej.
* Otwórz https://api.polydocs.io i dodaj ścieżkę funkcji za Polydocs URL.

Na przykład:

![Dokumentacja API dla operacji PUT /users/update/{user_id} o tytule Update User z parametrem ścieżki user_id oraz polami first_name, last_name, email, is_organisation_admin i password w treści żądania](https://lh7-us.googleusercontent.com/tC3qtPbFb1GsK6dBmB5Jrv5HqFOYLxNR1XB0PEuA8ipkHnH2ZQ6xrrkImNgbGSMoA6aAGvLr6K3cI4u\_qM96BOvR7AnQzmX17HBMBneNpLBc6RIzspfTYgrCWSj0fSE9mSWLIex3hc\_R-m-PI6zT6Rs)

* Teraz wklej ten link w polu tekstowym obok metody PUT w Postman.
* Zastąp {user\_id} na końcu URL rzeczywistym identyfikatorem użytkownika, którego chcesz usunąć. (Możesz uzyskać user\_id za pomocą metody GET).

## Zmiana adresu e-mail użytkownika

* W treści wpisz “email” jako klucz i nowy adres e-mail jako wartość.
* Następnie naciśnij \`Send\`, a w odpowiedzi powinieneś zobaczyć “success”.
