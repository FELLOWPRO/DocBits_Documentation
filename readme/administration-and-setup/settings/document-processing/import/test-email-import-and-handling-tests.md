# Test: import i obsługa poczty e-mail

## Cel

Testy te zapewniają, że nasz system poprawnie obsługuje import poczty e-mail. Obejmuje to wysyłanie wiadomości e-mail, odbieranie i przenoszenie ich do określonych folderów, sprawdzanie, czy są przeczytane, czy nieprzeczytane, importowanie ich do systemu i późniejsze czyszczenie.

## Kroki testu

1. **Setup:**
   * **Pobierz ustawienia środowiska:** Załaduj niezbędne szczegóły, takie jak informacje o serwerze e-mail i dane uwierzytelniające ze zmiennych środowiskowych.
   * **Zaszyfruj hasło e-mail:** Bezpiecznie zaszyfruj hasło e-mail w celu bezpiecznego użytkowania.
2. **Wysyłanie i zarządzanie e-mailami:**
   * **Wyślij e-mail:** Użyj funkcji SMTP, aby wysłać wiadomość e-mail z określonym tematem i załącznikiem.
   * **Przenieś e-mail:** Użyj funkcji IMAP, aby przenieść e-mail do folderu docelowego.
   * **Lista folderów:** Upewnij się, że folder docelowy istnieje.
   * **Usuń wiadomość e-mail:** Posprzątaj, usuwając wiadomość e-mail z folderu.
   * **Sprawdź status e-maila:** Sprawdź, czy wiadomość e-mail jest oznaczona jako przeczytana czy nieprzeczytana.
3.  **Test Sequence**

    **Initial Setup:**

    * **Sprawdź połączenie:** Sprawdź połączenie z serwerem e-mail i uzyskaj identyfikator połączenia.
    * **Test logowania:** Potwierdź, że logowanie przy użyciu zapisanych danych uwierzytelniających działa.
    * **Sprawdzanie folderu:** Upewnij się, że folder docelowy istnieje na serwerze poczty elektronicznej.

    **Email Operations:**

    * **Wyślij e-mail testowy:** Wyślij e-mail z określonym tematem.
    * **Odzyskaj e-mail ID:** Pobierz ID wysłanego e-maila ze skrzynki odbiorczej.
    * **Przenieś e-mail:** Przenieś e-mail ze skrzynki odbiorczej do folderu docelowego.
    * **Sprawdź status wiadomości e-mail:** Upewnij się, że wiadomość e-mail w folderze docelowym jest oznaczona jako nieprzeczytana.

    **Email Importing:**

    * **Pobierz wiadomość e-mail:** Zaimportuj wiadomość e-mail z folderu docelowego do naszego systemu.
    * **Sprawdź zaimportowaną wiadomość e-mail:** Upewnij się, że zaimportowana wiadomość e-mail została poprawnie pobrana i zarejestrowana.

    **Log Verification:**

    * **Sprawdź dziennik importu:** Sprawdź, czy temat wysłanej wiadomości e-mail jest zapisany w dzienniku importu.

    **Cleanup:**

    * **Usuń zaimportowany dokument:** Usuń dokument, który został zaimportowany z wiadomości e-mail.
    * **Usuń wiadomość e-mail:** Usuń wysłaną i przeniesioną wiadomość e-mail z folderów, aby wszystko było czyste.

## Szczegółowe wyjaśnienie każdego testu

* **Konfiguracja i inicjalizacja:**
  * **Zainicjuj udostępnione dane:** Przygotuj udostępnione dane do testów.
* **Testy połączenia e-mailowego:**
  * **Uzyskaj identyfikator połączenia:** Sprawdź, czy możemy połączyć się z serwerem e-mail i uzyskaj ID dla połączenia.
  * **Weryfikacja logowania:** Upewnij się, że logowanie do serwera poczty elektronicznej działa prawidłowo.
* **Testy weryfikacji folderów:**
  * **Sprawdź folder docelowy:** Upewnij się, że folder docelowy istnieje na serwerze e-mail.
  * **Sprawdź listę folderów:** Upewnij się, że lista folderów z serwera odpowiada naszym oczekiwaniom.
* **Wysyłanie e-maili i ID Pobieranie:**
  * **Wyślij e-mail:** Wyślij testową wiadomość e-mail z określonym tematem i załącznikiem.
  * **Pobierz e-mail ID:** Pobierz unikalny ID tego wysłanego e-maila ze skrzynki odbiorczej.
* **Przenoszenie e-maili i sprawdzanie statusu:**
  * **Przenieś e-mail do folderu:** Przenieś testową wiadomość e-mail ze skrzynki odbiorczej do folderu docelowego.
  * **Sprawdź status nieprzeczytany:** Upewnij się, że po przeniesieniu wiadomość e-mail została oznaczona jako nieprzeczytana.
* **Pobieranie e-maili i sprawdzanie odpowiedzi:**
  * **Pobierz e-mail z folderu:** Zaimportuj e-mail z folderu docelowego do naszego systemu.
  * **Sprawdź pobrany e-mail:** Potwierdź, że pobrany e-mail znajduje się w odpowiedzi.
* **Weryfikacja dziennika importu:**
  * **Pobierz dziennik importu:** Pobierz dziennik zaimportowanych wiadomości e-mail.
  * **Sprawdź temat wiadomości e-mail w dzienniku:** Upewnij się, że temat wiadomości testowej znajduje się w dzienniku importu.
* **Cleanup:**
  * **Usuń zaimportowany dokument:** Usuń dokument, który został zaimportowany z wiadomości e-mail.
  * **Usuń wiadomość e-mail:** Usuń wiadomość testową ze skrzynki odbiorczej i folderu docelowego, aby wszystko było czyste.

\


