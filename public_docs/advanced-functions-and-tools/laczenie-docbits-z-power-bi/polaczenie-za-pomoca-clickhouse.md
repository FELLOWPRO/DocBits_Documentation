# Połączenie za pomocą ClickHouse

Ten przewodnik prowadzi Cię przez połączenie **ClickHouse** z **Power BI Desktop** za pomocą sterownika **ODBC**. Obejmuje instalację sterownika, konfigurację ODBC, integrację z Power BI oraz ustawienie odświeżania danych.

{% embed url="https://youtu.be/O1MtuXf_R_M" %}
{% endembed %}


### 1. Zainstaluj sterownik ClickHouse ODBC

* Pobierz najnowszy **sterownik ClickHouse ODBC** z:
  * [ClickHouse GitHub - clickhouse-odbc](https://github.com/ClickHouse/clickhouse-odbc)
* Uruchom instalator i postępuj zgodnie z kreatora instalacji.

### 2. Skonfiguruj źródło danych ODBC

* Otwórz **Administrator źródeł danych ODBC (64-bit)** za pomocą Panelu sterowania lub wyszukiwarki systemu Windows.
* Przejdź do karty **DSN systemowy** i kliknij **Dodaj**.
* Wybierz **Sterownik ClickHouse ODBC** z listy i kliknij **Zakończ**.
*   Wypełnij wymagane pola. Potrzebne informacje znajdziesz w:

    **DocBits** → **Ustawienia** → **Przetwarzanie dokumentów** → **Moduł** → **Panel AI** → **Bezpośredni dostęp do ClickHouse**

    ![](https://docs.docbits.com/~gitbook/image?url=https%3A%2F%2F578966019-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FT2n2w4uDCJvv7CJ5zrdk%252Fuploads%252FNkgb8IJ4dQVRnJ4gpqH0%252Fimage.png%3Falt%3Dmedia%26token%3D27d97e71-dd81-488a-851f-e7d659ad4992\&width=768\&dpr=4\&quality=100\&sign=88a4a589\&sv=2)

    **Wymagane pola:**

    * **Nazwa**: Nazwa połączenia (np. `ClickHouse_Prod`)
    * **Opis**: Krótki opis dla Twojego odniesienia (opcjonalnie)
    * **Host**: Skopiuj wartość hosta z DocBits
    * **Port**: Skopiuj wartość portu z DocBits
    * **Baza danych**: Skopiuj nazwę bazy danych z DocBits
    * **Nazwa użytkownika**: Skopiuj nazwę użytkownika z DocBits
    * **Hasło**: Skopiuj hasło z DocBits

### 3. Połącz ClickHouse z Power BI

* Otwórz **Power BI Desktop**.
*   Wybierz **Pobierz dane** → **ODBC** → **Połącz**.

    ![](https://docs.docbits.com/~gitbook/image?url=https%3A%2F%2F578966019-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FT2n2w4uDCJvv7CJ5zrdk%252Fuploads%252F1aIDfi4Rj6WD9oXsvUjt%252FScreenshot%25202025-05-19%2520163621.png%3Falt%3Dmedia%26token%3D4ec15da7-fa79-4b9e-a83b-cb4b0a545cfd\&width=768\&dpr=4\&quality=100\&sign=59fba2e3\&sv=2)
*   Z listy DSN wybierz skonfigurowane źródło (np. `ClickHouse_Prod`).

    ![](https://docs.docbits.com/~gitbook/image?url=https%3A%2F%2F578966019-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FT2n2w4uDCJvv7CJ5zrdk%252Fuploads%252FgDWq5vmtqfAGAQEY0SAX%252FScreenshot%25202025-05-19%2520163823.png%3Falt%3Dmedia%26token%3D443435ac-82ba-40de-a4d1-17611afebb6a\&width=768\&dpr=4\&quality=100\&sign=c0c7d7ae\&sv=2)
* Kliknij **OK**. Wprowadź dane uwierzytelniające, jeśli zostaniesz poproszony.

### 4. Wczytaj i przekształć dane

* W panelu **Nawigator** przeglądaj i wybierz tabele lub widoki do importu.
* Wybierz:
  * **Wczytaj**: aby zaimportować bezpośrednio
  *   **Przekształć dane**: aby otworzyć Power Query do kształtowania danych

      ![](https://docs.docbits.com/~gitbook/image?url=https%3A%2F%2F578966019-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FT2n2w4uDCJvv7CJ5zrdk%252Fuploads%252F2lrWi9PduJgVQGHQMmhX%252FScreenshot%25202025-05-19%2520164134.png%3Falt%3Dmedia%26token%3D135c45ad-a7ca-4f01-a2f0-07998397f4d9\&width=768\&dpr=4\&quality=100\&sign=e27f4d93\&sv=2)

### 5. Wizualizuj swoje dane

* Użyj płótna raportu do budowania wizualizacji.
* Przeciągnij pola, dodaj przycinarki, wybierz typy wykresów i użyj wyrażeń **DAX** w razie potrzeby.
* Wykorzystaj **Edytor Power Query** do czyszczenia lub obracania danych ClickHouse przed budowaniem wizualizacji.
* Dokumentacja PowerBI: [https://learn.microsoft.com/en-us/power-bi/](https://learn.microsoft.com/en-us/power-bi/)

### 6. Włącz zaplanowane odświeżanie (opcjonalne)

**Uwaga:** **Wymaga Power BI Pro lub Premium + Gateway**

* Aby utrzymać zgodność raportów z ClickHouse:
* Opublikuj plik `.pbix` w **Usłudze Power BI**.
* Zainstaluj **Bramę Power BI** (tryb standardowy) na maszynie z dostępem sieciowym do ClickHouse.
* W Usłudze Power BI:
  * Przejdź do swojego zbioru danych → **Ustawienia** → **Zaplanowane odświeżanie**
  * Przyporządkuj swoje DSN i podaj dane uwierzytelniające
* Więcej informacji [tutaj](https://learn.microsoft.com/en-us/power-bi/connect-data/service-gateway-deployment-guidance).

### 7. Przykładowe pulpity nawigacyjne i widoki danych

![](<../../.gitbook/assets/example_4 (1).avif>) ![](<../../.gitbook/assets/example_3 (1).avif>) ![](<../../.gitbook/assets/example_2 (1).avif>) ![](<../../.gitbook/assets/example_1 (1).avif>)
