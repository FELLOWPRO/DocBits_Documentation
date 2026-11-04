# Test: import pliku 1

## Cel

Testy te mają na celu zapewnienie prawidłowego działania naszego systemu importu plików. W szczególności testujemy import plików PDF i TIFF do systemu, upewniając się, że są one pomyślnie przetwarzane i przechowywane.

#### Przygotowanie i sprzątanie po testach

* **Setup:**
  * Przed każdym testem rejestrujemy komunikat konfiguracyjny.
  * **Oczyszczanie:** Po każdym teście sprzątamy, usuwając z bazy danych wszelkie dokumenty utworzone przez użytkownika testowego, aby mieć pewność, że żadne pozostałości danych nie będą miały wpływu na kolejne testy.

#### Scenariusze testowe

1. **Import PDF File:**
   * **Test importu PDF (`test_import_pdf`):**
     * Zaimportuj plik PDF (`FellowBananaInvoice.pdf`) do systemu.
     * **Oczekiwany wynik:** Plik powinien zostać pomyślnie zaimportowany, zwracając dokument ID.
2. **Import TIFF File:**
   * **Test importu TIFF (`test_import_tiff`):**
     * Zaimportuj plik TIFF (`TIFF_FILE.TIF`) do systemu.
     * **Oczekiwany wynik:** Plik powinien zostać pomyślnie zaimportowany, zwracając dokument ID.

## Szczegółowe wyjaśnienie każdego testu

* **Konfiguracja i czyszczenie:**
  * **Logowanie:** Dla każdego testu rejestrowany jest komunikat dotyczący konfiguracji i czyszczenia.
  * **Oczyszczanie bazy danych (`clean_documents`):** Usuwa z bazy danych wszelkie dokumenty utworzone przez użytkownika testowego, aby zachować czysty stan.
*   **Testy importu plików:**

    **Import PDF File:**

    * **Załaduj użytkownika:** Załaduj użytkownika testowego.
    * **Ścieżka pliku:** Określ ścieżkę do pliku PDF (`tests/files/pdfs/FellowBananaInvoice.pdf`).
    * **Importuj plik:** Użyj klasy `FileImporter`, aby zaimportować plik PDF.
    * **Sprawdź odpowiedź:** Upewnij się, że odpowiedzią jest lista zawierająca komunikat o powodzeniu i dokument ID.

    **Import TIFF File:**

    * **Załaduj użytkownika:** Załaduj użytkownika testowego.
    * **Ścieżka pliku:** Określ ścieżkę do pliku TIFF (`tests/files/pdfs/TIFF_FILE.TIF`).
    * **Importuj plik:** Użyj klasy `FileImporter`, aby zaimportować plik TIFF.
    * **Sprawdź odpowiedź:** Upewnij się, że odpowiedzią jest lista zawierająca komunikat o powodzeniu i dokument ID.

## Struktura kodu

* **Logger:** Służy do rejestrowania komunikatów debugowania podczas instalacji, czyszczenia i wykonywania testów.
* **Pomocnik bazy danych:** Wykonuje zapytania bez zwracania wyników w celu oczyszczenia.
* **Importer plików:** Obsługuje import plików do systemu.
* **Urządzenia:** `set_up`urządzenie do zarządzania konfiguracją i czyszczeniem na potrzeby testów.
* **Tests:**
  * `test_import_pdf`: Testuje import pliku PDF.
  * `test_import_tiff`: Testuje import pliku TIFF.

#### Podsumowanie

Testy te zapewniają, że nasza funkcja importowania plików działa zgodnie z oczekiwaniami zarówno w przypadku plików PDF, jak i TIFF. Stosując to podejście, sprawdzamy, czy pliki są importowane poprawnie i czy system może bez problemów obsługiwać różne typy plików.


