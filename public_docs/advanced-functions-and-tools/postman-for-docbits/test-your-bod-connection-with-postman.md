# Przetestuj swoje połączenie BOD za pomocą Postman

## Przegląd

Ta strona wyjaśnia, jak sprawdzić pomyślne przetworzenie dokumentu BOD (Business Object Document) za pomocą Postman. Przetestujesz właściwy punkt końcowy API, wysyłając żądanie z plikiem mapowania BOD. Wykonaj poniższe kroki po kolei.

## Uzyskiwanie dostępu do klucza API i pliku mapowania BOD

### Pobieranie klucza API

1.  Przejdź do **Ustawienia → System i administracja → Integracja i SSO**.

    <figure><img src="../../.gitbook/assets/test-bod-connection-integration-sso-pl-20261113.png" alt="Tabela Klucze API na stronie Integracja i SSO. Każdy wiersz pokazuje zamaskowany prefiks klucza, nazwę, termin wygaśnięcia w kolumnie Wygasa, ostatnie użycie w kolumnie Ostatnio Używany, status, ikonę kopiowania i trzy-kropkowe menu Akcje."><figcaption><p>Tabela <strong>Klucze API</strong> na stronie <strong>Integracja i SSO</strong>. Każdy wiersz pokazuje zamaskowany prefiks klucza, nazwę, termin wygaśnięcia (kolumna <strong>Wygasa</strong>), ostatnie użycie (kolumna <strong>Ostatnio Używany</strong>) i status.</p></figcaption></figure>
2.  Możesz skopiować swój **Klucz API** ręcznie albo kliknąć ikonę kopiowania, aby skopiować go do schowka.

    <figure><img src="../../.gitbook/assets/test-bod-connection-api-key-copy-pl-20261113.png" alt="Zbliżenie wiersza tabeli Klucze API: zamaskowany prefiks klucza, jego ikona kopiowania, nazwa klucza i trzy-kropkowe menu Akcje."><figcaption><p>Kliknij ikonę kopiowania obok klucza, aby skopiować jego wartość. Ze względów bezpieczeństwa tabela pokazuje tylko prefiks klucza, po którym następuje <code>****</code>; pełny klucz jest wyświetlany jednorazowo, przy tworzeniu klucza. Jeśli nie masz już pełnego klucza, utwórz nowy, jak opisano w sekcji <a href="../../administration-and-setup/settings/global-settings/integration/api-key-management.md">Zarządzanie kluczami API</a>.</p></figcaption></figure>

    Lista kluczy, ikona kopiowania i trzy-kropkowe menu **Akcje** są w pełni opisane na stronie [Zarządzanie kluczami API](../../administration-and-setup/settings/global-settings/integration/api-key-management.md).

### Pobieranie pliku mapowania BOD

1.  Przejdź do **Ustawienia → Przetwarzanie dokumentów → Eksport**.

    <figure><img src="../../.gitbook/assets/test-bod-connection-export-list-pl-20261113.png" alt="Lista Eksport z dwiema przykładowymi konfiguracjami eksportu i kolumnami Typ, Podorganizacje, Tytuł, Metoda Eksportu i Akcje."><figcaption><p>Lista <strong>Eksport</strong>. Każdy wiersz to jedna konfiguracja eksportu; kolumna <strong>Metoda Eksportu</strong> pokazuje, jak dokumenty są wysyłane.</p></figcaption></figure>
2.  W kolumnie **Akcje** odpowiedniego wpisu eksportu kliknij menu z trzema kropkami i wybierz **Redagować**.

    <figure><img src="../../.gitbook/assets/test-bod-connection-export-list-pl-20261113.png" alt="Lista Eksport z otwartym trzy-kropkowym menu Akcje w pierwszym wierszu i pozycjami Dezaktywować, Redagować i Usuwać."><figcaption><p>Menu <strong>Akcje</strong> wiersza jest otwarte i pozycja <strong>Redagować</strong> jest dostępna. <strong>Redagować</strong> otwiera konfigurację eksportu; strona <a href="../../administration-and-setup/settings/document-processing/export.md">Eksport</a> opisuje każdą kolumnę i każdą akcję.</p></figcaption></figure>
3.  Znajdź pole **Plik mapowania BOD** i kliknij **Pobierać**, aby zapisać plik.

    <figure><img src="../../.gitbook/assets/test-bod-connection-bod-mapping-pl-20261113.png" alt="Konfiguracja eksportu Infor IDM + ION BOD w widoku edycji: sekcja Informacje podstawowe z tytułem, podorganizacją i typem dokumentu, sekcja Eksportuj konfigurację z wybranym typem wdrożenia CHMURA oraz polami Plik API ION, Plik mapowania IDM i Plik mapowania BOD, każde z przyciskiem Pobierać."><figcaption><p>Konfiguracja eksportu w widoku edycji. W sekcji <strong>Informacje podstawowe</strong> widzisz tytuł konfiguracji, podorganizację i typ dokumentu. W sekcji <strong>Eksportuj konfigurację</strong> wybrany jest typ wdrożenia <strong>CHMURA</strong>, a pole <strong>Plik mapowania BOD</strong> ma przycisk <strong>Pobierać</strong>, który zapisuje plik mapowania (BOD-Mapping.properties) na Twoim komputerze. Jak edytować ten plik, przeczytasz w sekcji <a href="../../infor-integration-and-configuration/exporting-to-infor/creating-a-bod-mapping-file.md">Tworzenie pliku mapowania BOD</a>.</p></figcaption></figure>

## Testowanie punktu końcowego w Postman

1.  **Wklej polecenie cURL w Postman**

    Otwórz Postman i wklej poniższe polecenie cURL w sekcji **Import**. Postman automatycznie skonfiguruje żądanie.

    ```bash
    curl -X 'POST' \
      'https://api.docbits.com/prod-api/import/purchase_order_bod' \
      -H 'accept: application/json' \
      -H 'X-API-KEY:' \
      -H 'Content-Type: multipart/form-data' \
      -F 'org_id=' \
      -F 'sub_org_id=' \
      -F 'file=@file.xml;type=text/xml' \
      -F 'custom_fields_mapping='
    ```

    <figure><img src="https://raw.githubusercontent.com/FELLOWPRO/DocBits_Documentation/refs/heads/main/public_docs/.gitbook/assets/test_bod_connection_postman_4.png" alt="Ekran startowy Postman z przyciskami Import i New w górnym pasku."><figcaption><p>W Postman przycisk <strong>Import</strong> znajduje się w górnym pasku okna.</p></figcaption></figure>

    <figure><img src="https://raw.githubusercontent.com/FELLOWPRO/DocBits_Documentation/refs/heads/main/public_docs/.gitbook/assets/test_bod_connection_postman_5.png" alt="Okno Import w Postman z polem Paste cURL to import."><figcaption><p>W oknie <strong>Import</strong> wklej polecenie cURL z góry w pole <strong>Paste cURL to import</strong>. Postman utworzy z niego gotowe żądanie.</p></figcaption></figure>
2.  **Ustaw klucz API**\
    Przejdź do zakładki **Headers**, znajdź nagłówek `X-API-KEY` i wklej swój klucz API do kolumny **Value**.

    <figure><img src="https://raw.githubusercontent.com/FELLOWPRO/DocBits_Documentation/refs/heads/main/public_docs/.gitbook/assets/test_bod_connection_postman_6.png" alt="Zaimportowane żądanie w Postman z otwartą zakładką Headers i wierszem nagłówka X-API-KEY."><figcaption><p>Zakładka <strong>Headers</strong> zaimportowanego żądania. Wklej klucz API skopiowany w DocBits do kolumny <strong>Value</strong> w wierszu <code>X-API-KEY</code>.</p></figcaption></figure>
3.  **Prześlij plik BOD**\
    Przejdź do zakładki **Body**, znajdź klucz `file`, a następnie kliknij **Select Files** w kolumnie **Value** i prześlij swój plik XML BOD.

    <figure><img src="https://raw.githubusercontent.com/FELLOWPRO/DocBits_Documentation/refs/heads/main/public_docs/.gitbook/assets/test_bod_connection_postman_7.png" alt="Żądanie w Postman z otwartą zakładką Body w trybie form-data i przyciskiem Select Files w wierszu file."><figcaption><p>Zakładka <strong>Body</strong> w trybie <strong>form-data</strong>. W wierszu <code>file</code> kliknij <strong>Select Files</strong> i wybierz plik XML BOD, który chcesz przetestować.</p></figcaption></figure>
4.  **Wyślij żądanie**\
    Kliknij **Send**, aby wykonać wywołanie API.

    <figure><img src="https://raw.githubusercontent.com/FELLOWPRO/DocBits_Documentation/refs/heads/main/public_docs/.gitbook/assets/test_bod_connection_postman_8.png" alt="Kompletne żądanie w Postman z przyciskiem Send w pasku żądania."><figcaption><p>Gdy klucz i plik są ustawione, kliknij <strong>Send</strong>, aby wykonać żądanie do API DocBits.</p></figcaption></figure>
5.  **Sprawdź odpowiedź**\
    Sprawdź odpowiedź, aby potwierdzić, że Twój BOD został pomyślnie przetworzony.

    <figure><img src="https://raw.githubusercontent.com/FELLOWPRO/DocBits_Documentation/refs/heads/main/public_docs/.gitbook/assets/test_bod_connection_postman_9.png" alt="Okno odpowiedzi Postman ze statusem 200 OK i treścią JSON z wartością success true."><figcaption><p>Udane wywołanie zwraca <strong>200 OK</strong> i treść JSON z <code>"success": true</code> — BOD został przetworzony.</p></figcaption></figure>
