# Test: połączenie importu FTP

#### Cel

Testy te zapewniają, że nasz system importu FTP działa poprawnie. Sprawdzamy, czy możemy dodać nowe połączenie importowe FTP, przetestować połączenie, aktywować/dezaktywować je, a następnie wyczyścić.



{% embed url="https://grafana.polydocs.io/d-solo/b6ad3a9c-260c-46a3-9ade-47691e743d4d/docbits?from=1715746603760&orgId=1&panelId=84&refresh=1m&to=1715768203760" %}

## Scenariusze testowe

1. **Setup:**
   * **Zmienne środowiskowe:** Załaduj niezbędne szczegóły, takie jak informacje o serwerze FTP i dane uwierzytelniające ze zmiennych środowiskowych.
2.  **FTP Connection Tests:**

    **Dodaj nowe połączenie:**

    * **Testuj dodanie nowego FTP Połączenie importowe (`test_add_new_ftp_import_connection`):**
      * Dodaj nowe połączenie importowe FTP z podanymi poświadczeniami i szczegółami serwera.
      * **Oczekiwany wynik:** Połączenie powinno zostać pomyślnie dodane.

    **Deactivate Connection:**

    * **Test Dezaktywuj FTP Importuj połączenie (`test_deactivate_ftp_import_connection`):**
      * Dezaktywuj nowo dodane połączenie importowe FTP.
      * **Oczekiwany wynik:** Połączenie powinno zostać pomyślnie dezaktywowane.

    **Test Connection:**

    * **Test połączenia FTP (`test_test_ftp_connection`):**
      * Sprawdź, czy połączenie importowe FTP może pomyślnie połączyć się z serwerem FTP.
      * **Oczekiwany wynik:** Połączenie powinno zostać pomyślnie przetestowane.

    **Sprawdź połączenie na liście:**

    * **Sprawdzanie testu FTP Połączenie na liście (`test_check_ftp_connection_in_list`):**
      * Sprawdź, czy nowo dodane połączenie importowe FTP znajduje się na liście połączeń.
      * **Oczekiwany wynik:** Połączenie powinno znaleźć się na liście.

    **Sprawdź połączenie dezaktywowane:**

    * **Kontrola testowa FTP Połączenie dezaktywowane (`test_check_ftp_connection_deactivated`):**
      * Sprawdź, czy połączenie importowe FTP jest zaznaczone na liście jako nieaktywne.
      * **Oczekiwany wynik:** Połączenie powinno być nieaktywne.

    **Dodaj folder testowy:**

    * **Test Dodaj folder testowy do połączenia (`test_add_test_folder_to_connection`):**
      * Dodaj domyślny katalog (folder testowy) do połączenia importowego FTP.
      * **Oczekiwany wynik:** Domyślny katalog powinien zostać pomyślnie dodany.

    **Reactivate Connection:**

    * **Testuj ponownie FTP Importuj połączenie (`test_reactivate_ftp_import_connection`):**
      * Aktywuj ponownie wcześniej dezaktywowane połączenie importowe FTP.
      * **Oczekiwany wynik:** Połączenie powinno zostać pomyślnie ponownie aktywowane.

    **Sprawdź, czy połączenie zostało ponownie aktywowane:**

    * **Kontrola testowa FTP Połączenie ponownie aktywowane (`test_check_ftp_connection_reactivated`):**
      * Sprawdź, czy połączenie importowe FTP jest zaznaczone na liście jako aktywne.
      * **Oczekiwany wynik:** Połączenie powinno być aktywne.

    **Cleanup:**

    * **Oczyszczanie testu FTP Import (`test_cleanup_ftp_import`):**
      * Usuń połączenie importowe FTP, aby wyczyścić po testach.
      * **Oczekiwany wynik:** Połączenie powinno zostać pomyślnie usunięte.

## Szczegółowe wyjaśnienie każdego testu

* **Konfiguracja i inicjalizacja:**
  * **Zainicjuj udostępnione dane:** Przygotuj udostępnione dane do testów.
* **FTP Connection Tests:**
  * **Dodaj nowe połączenie:** Dodaj nowe połączenie importowe FTP z podanymi poświadczeniami i szczegółami serwera.
  * **Dezaktywuj połączenie:** Dezaktywuj nowo dodane połączenie importowe FTP.
  * **Testuj połączenie:** Sprawdź, czy połączenie importowe FTP może pomyślnie połączyć się z serwerem FTP.
  * **Sprawdź połączenie na liście:** Sprawdź, czy nowe połączenie importowe FTP znajduje się na liście połączeń.
  * **Sprawdź połączenie dezaktywowane:** Potwierdź, że połączenie importowe FTP jest zaznaczone na liście jako nieaktywne.
  * **Dodaj folder testowy:** Dodaj domyślny katalog (folder testowy) do połączenia importowego FTP.
  * **Reaktywuj połączenie:** Reaktywuj wcześniej dezaktywowane połączenie importowe FTP.
  * **Sprawdź połączenie ponownie aktywowane:** Upewnij się, że połączenie importowe FTP jest zaznaczone na liście jako aktywne.
  * **Czyszczenie:** Usuń połączenie importowe FTP w celu oczyszczenia po testach.

\


