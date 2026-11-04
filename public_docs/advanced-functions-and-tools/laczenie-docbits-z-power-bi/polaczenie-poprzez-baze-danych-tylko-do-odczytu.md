# Połączenie poprzez bazę danych tylko do odczytu

Ten przewodnik prowadzi Cię przez połączenie **Bazy danych tylko do odczytu DocBits z programem Power BI Desktop** przy użyciu sterownika **PostgreSQL ODBC**. Obejmuje instalację sterownika, konfigurację ODBC, integrację z Power BI oraz zaplanowane odświeżanie.

{% embed url="https://youtu.be/O1MtuXf_R_M" %}
{% endembed %}


### 1. Instalacja sterownika PostgreSQL ODBC

* Pobierz najnowszy sterownik PostgreSQL ODBC (**psqlODBC**) ze strony oficjalnej:
  * [https://www.postgresql.org/ftp/odbc/releases/](https://www.postgresql.org/ftp/odbc/releases/)
* Uruchom instalator i postępuj zgodnie z kreatora instalacji.

### 2. Konfiguracja źródła danych ODBC

* Otwórz **Administrator źródła danych ODBC (64-bit)** za pomocą Panelu sterowania lub wyszukiwania w systemie Windows.
* Przejdź do karty **DSN systemowy** i kliknij **Dodaj**.
* Wybierz sterownik **PostgreSQL Unicode(x64)** z listy i kliknij **Zakończ**.
* Wypełnij wymagane pola danymi dostępowymi z: **DocBits → Ustawienia → Przetwarzanie dokumentów → Moduł → Panel AI → Dostęp do bazy danych tylko do odczytu**

![](https://docs.docbits.com/~gitbook/image?url=https%3A%2F%2F578966019-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FT2n2w4uDCJvv7CJ5zrdk%252Fuploads%252FupCHowPUuMJ8hO9Y36EY%252Fconnect_read_only_4.png%3Falt%3Dmedia%26token%3D3eb69744-6696-41e2-90be-63295b9b6f6d\&width=768\&dpr=4\&quality=100\&sign=647db68c\&sv=2)

**Wymagane pola:**

* **Nazwa:** Nazwa połączenia (np. `Piaskownica-Tylko_do_odczytu`)
* **Serwer:** Skopiuj wartość hosta z DocBits
* **Port:** Skopiuj wartość portu z DocBits
* **Baza danych:** Skopiuj nazwę bazy danych z DocBits
* **Nazwa użytkownika:** Skopiuj nazwę użytkownika z DocBits
* **Hasło:** Skopiuj hasło z DocBits
* **Tryb SSL:** Ustaw na **Wymagane** (zapewnia zaszyfrowaną komunikację)

### 3. Połączenie bazy danych tylko do odczytu z programem Power BI

* Otwórz **Power BI Desktop**.
*   Wybierz **Pobierz dane** → **ODBC** → **Połącz**.

    ![](https://docs.docbits.com/~gitbook/image?url=https%3A%2F%2F578966019-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FT2n2w4uDCJvv7CJ5zrdk%252Fuploads%252F1aIDfi4Rj6WD9oXsvUjt%252FScreenshot%25202025-05-19%2520163621.png%3Falt%3Dmedia%26token%3D4ec15da7-fa79-4b9e-a83b-cb4b0a545cfd\&width=768\&dpr=4\&quality=100\&sign=59fba2e3\&sv=2)
* Z listy DSN wybierz skonfigurowane źródło (np. `Piaskownica-Tylko_do_odczytu`).

![](https://docs.docbits.com/~gitbook/image?url=https%3A%2F%2F578966019-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FT2n2w4uDCJvv7CJ5zrdk%252Fuploads%252FKPDLjfDw2SRYvzvFKWXq%252Fconnect_read_only_3.png%3Falt%3Dmedia%26token%3Dc67c1362-7f63-479e-a373-974d198f5eb7\&width=768\&dpr=4\&quality=100\&sign=f001e759\&sv=2)

* Kliknij **OK**. Wprowadź ponownie dane uwierzytelniające, jeśli zostaniesz poproszony.
  * **Uwaga:** Jeśli zobaczysz błąd **“uwierzytelnianie hasłem nie powiodło się dla użytkownika”**, spróbuj wprowadzić hasło w **klamry** `**{}**`.

### 4. Ładowanie i przekształcanie danych

* W panelu **Nawigator** rozwini schemat listy.
* Otwórz schemat `**public**`.
* Wybierz tabele, które chcesz zaimportować.

![](https://docs.docbits.com/~gitbook/image?url=https%3A%2F%2F578966019-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FT2n2w4uDCJvv7CJ5zrdk%252Fuploads%252FSmtEspL1H6ieOJhtDwYb%252Fconnect_read_only_1.png%3Falt%3Dmedia%26token%3Dd402a928-175e-4904-bd21-592ff114fad7\&width=300\&dpr=4\&quality=100\&sign=464e3a3d\&sv=2) ![](https://docs.docbits.com/~gitbook/image?url=https%3A%2F%2F578966019-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FT2n2w4uDCJvv7CJ5zrdk%252Fuploads%252F3Phea1Pf3ZBJtMzw3rxi%252Fconnect_read_only_2.png%3Falt%3Dmedia%26token%3D94037886-57e3-440d-bf08-61cd37c65b98\&width=300\&dpr=4\&quality=100\&sign=5ead9fe9\&sv=2)

* Wybierz:
  * **Załaduj** → Importuj bezpośrednio do Power BI
  * **Przekształć dane** → Otwórz Power Query, aby kształtować i filtrować przed załadowaniem

### 5. Wizualizacja danych

* Użyj płótna raportu Power BI do budowania pulpitów nawigacyjnych.
* Przeciągnij pola, dodaj przycinarki, wybierz typy wykresów i zastosuj obliczenia DAX.
* Użyj **Edytora Power Query** do czyszczenia lub łączenia danych przed utworzeniem wizualizacji.
* Odniesienie: [Dokumentacja Power BI](https://learn.microsoft.com/en-us/power-bi/?utm_source=chatgpt.com)

### 6. Włącz zaplanowane odświeżanie (opcjonalne)

**Uwaga:** **Wymaga Power BI Pro lub Premium + Gateway**

* Aby utrzymać zgodność raportów z ClickHouse:
* Opublikuj plik `.pbix` w **Usłudze Power BI**.
* Zainstaluj **Bramę Power BI** (tryb standardowy) na maszynie z dostępem sieciowym do ClickHouse.
* W Usłudze Power BI:
  * Przejdź do swojego zestawu danych → **Ustawienia** → **Zaplanowane odświeżanie**
  * Przyporządkuj swoje DSN i podaj dane uwierzytelniające
* Więcej informacji [tutaj](https://learn.microsoft.com/en-us/power-bi/connect-data/service-gateway-deployment-guidance).

### 7. Przykładowe pulpity nawigacyjne i widoki danych

![](<../../.gitbook/assets/example_4 (1).avif>)![](<../../.gitbook/assets/example_3 (1).avif>)![](<../../.gitbook/assets/example_2 (1).avif>)![](<../../.gitbook/assets/example_1 (1).avif>)
