# Test: import i obsługa poczty e-mail

## Co jest testowane?

Testy te zapewniają, że nasz system importu poczty e-mail działa poprawnie. Główne cele to:

1. **Wyślij e-maile** z załącznikami.
2. **Odbieraj i przenoś e-maile** do określonych folderów.
3. **Sprawdź, czy e-maile są przeczytane, czy nieprzeczytane.**
4. **Importuj e-maile do naszego systemu.**
5. **Wyczyść**, usuwając później e-maile i zaimportowane dokumenty.

## Wymagane kroki

1. **Setup:**
   * **Pobierz ustawienia środowiska:** Załaduj szczegóły serwera e-mail i dane uwierzytelniające ze zmiennych środowiskowych.
   * **Zaszyfruj hasło e-mail:** Bezpiecznie zaszyfruj hasło e-mail.
2. **Wysyłaj i zarządzaj e-mailami:**
   * **Wyślij e-maile:** Użyj funkcji SMTP, aby wysyłać e-maile z określonymi tematami i załącznikami.
   * **Przenieś e-maile:** Użyj funkcji IMAP, aby przenieść e-maile do folderu docelowego.
   * **Lista folderów:** Sprawdź, czy folder docelowy istnieje.
   * **Usuń e-maile:** Oczyść e-maile, usuwając je z folderów.
   * **Sprawdź status e-maila:** Sprawdź, czy e-maile są oznaczone jako nieprzeczytane lub przeczytane.
3.  **Test Sequence**

    **Initial Setup:**

    * **Sprawdź połączenie:** Sprawdź połączenie z serwerem e-mail i uzyskaj identyfikator połączenia.
    * **Test logowania:** Potwierdź, że logowanie przy użyciu zapisanych danych uwierzytelniających działa.
    * **Sprawdzanie folderu:** Upewnij się, że folder docelowy istnieje na serwerze poczty elektronicznej.

    **Email Operations:**

    * **Wyślij e-maile testowe:** Wyślij trzy e-maile z unikalnymi tematami.
    * **Pobierz identyfikatory e-maili:** Pobierz identyfikatory wysłanych e-maili ze skrzynki odbiorczej.
    * **Przenieś e-maile:** Przenieś te e-maile ze skrzynki odbiorczej do folderu docelowego.
    * **Sprawdź status wiadomości e-mail:** Upewnij się, że wiadomości e-mail w folderze docelowym są oznaczone jako nieprzeczytane.

    **Email Importing:**

    * **Pobierz e-maile:** Importuj e-maile z folderu docelowego do naszego systemu.
    * **Sprawdź zaimportowane wiadomości e-mail:** Upewnij się, że zaimportowane wiadomości e-mail zostały poprawnie pobrane i zarejestrowane.

    **Log Verification:**

    * **Sprawdź dzienniki importu:** Sprawdź, czy tematy wysłanych wiadomości e-mail są zapisane w dziennikach importu.

    **Cleanup:**

    * **Usuń zaimportowane dokumenty:** Usuń dokumenty zaimportowane z wiadomości e-mail.
    * **Usuń e-maile:** Posprzątaj, usuwając wysłane i przeniesione e-maile z folderów.

### Szczegółowe wyjaśnienie każdego testu

* **Konfiguracja i inicjalizacja:**
  * **Zainicjuj udostępnione dane:** Przygotuj udostępnione dane do testów.
* **Testy połączenia e-mailowego:**
  * **Uzyskaj identyfikator połączenia:** Sprawdź, czy możemy połączyć się z serwerem e-mail i uzyskaj ID dla połączenia.
  * **Weryfikacja logowania:** Upewnij się, że logowanie do serwera poczty elektronicznej działa prawidłowo.
* **Testy weryfikacji folderów:**
  * **Sprawdź folder docelowy:** Upewnij się, że folder docelowy istnieje na serwerze e-mail.
  * **Sprawdź listę folderów:** Upewnij się, że lista folderów z serwera odpowiada naszym oczekiwaniom.
* **Wysyłanie e-maili i ID Pobieranie:**
  * **Wyślij e-maile:** Wyślij trzy e-maile testowe z określonymi tematami i załącznikami.
  * **Pobierz identyfikatory e-maili:** Pobierz unikalne identyfikatory wysłanych e-maili ze skrzynki odbiorczej.
* **Przenoszenie e-maili i sprawdzanie statusu:**
  * **Przenieś e-maile do folderu:** Przenieś testowe e-maile ze skrzynki odbiorczej do folderu docelowego.
  * **Sprawdź status nieprzeczytany:** Upewnij się, że po przeniesieniu wiadomości e-mail zostały oznaczone jako nieprzeczytane.
* **Pobieranie e-maili i sprawdzanie odpowiedzi:**
  * **Pobierz e-maile z folderu:** Zaimportuj e-maile z folderu docelowego do naszego systemu.
  * **Sprawdź pobrane wiadomości e-mail:** Potwierdź, że pobrane wiadomości e-mail odpowiadają wiadomościom wysłanym.
* **Weryfikacja dziennika importu:**
  * **Pobierz dziennik importu:** Pobierz dziennik zaimportowanych wiadomości e-mail.
  * **Sprawdź tematy wiadomości e-mail w dzienniku:** Upewnij się, że tematy wiadomości testowych znajdują się w dzienniku importu.
* **Cleanup:**
  * **Usuń zaimportowane dokumenty:** Usuń dokumenty zaimportowane z wiadomości e-mail.
  * **Usuń e-maile:** Usuń e-maile testowe ze skrzynki odbiorczej i folderu docelowego, aby wszystko było czyste.

\


