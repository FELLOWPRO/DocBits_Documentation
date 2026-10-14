# Eksport

## Przegląd

Strona Eksport wyświetla wszystkie skonfigurowane ustawienia eksportu, w tym informację czy są aktywne czy nieaktywne. Stąd użytkownicy mogą:

* Przeglądać i zarządzać istniejącymi konfiguracjami eksportu
* Tworzyć nowe połączenia eksportu (np. do **Infor**, **Infor & IDM**, **Webhook** lub **SFTP**)
* Edytować lub usuwać istniejące konfiguracje eksportu

## Gdzie znaleźć

Możesz to znaleźć w: **Ustawienia** → **Przetwarzanie dokumentów** → **Eksport**

![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/export_settings_menu_access.png)

## **Korzystanie ze strony Eksportu**

Po otwarciu strony Eksport zobaczysz listę wszystkich istniejących konfiguracji eksportu.

Każdy wiersz na liście pokazuje:

* **Wskaźnik statusu**
  * **Zielony** oznacza, że eksport jest aktywny
  * **Czerwony** oznacza, że eksport jest dezaktywowany
* **Nazwa** – nazwa konfiguracji eksportu
* **Typ dokumentu** – typ dokumentu, dla którego skonfigurowano eksport
* **Podorganizacja** – jeśli eksport jest ograniczony do określonej podorganizacji
* **Metoda eksportu** – gdzie dokument zostanie wysłany (np. Infor, IDM, SFTP)
* **Akcje** – przyciski do **edycji, usuwania** lub **aktywowania/dezaktywowania** konfiguracji

![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/export_list_view.png)

#### **Ważne zasady konfiguracji eksportu**

Dla każdego **typu dokumentu** **w ramach danej organizacji lub podorganizacji** obowiązują następujące zasady:

* Możesz mieć **tylko jeden aktywny eksport Infor**
* Możesz mieć **tylko jeden aktywny eksport nie-Infor** (np. Webhook, SFTP)

Jednak możliwe jest posiadanie:

* **Jednego aktywnego eksportu Infor** _i_ **jednego aktywnego eksportu nie-Infor** jednocześnie dla tego samego typu dokumentu
* **Różnych konfiguracji eksportu dla różnych podorganizacji** — na przykład jeden eksport Infor dla Pod-Org A i inny eksport Infor dla Pod-Org B

## **Tworzenie nowego eksportu**

Aby utworzyć nowy eksport:

1. Kliknij przycisk **"Nowy"**. ![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/export_create_new_button.png)
2. Wybierz **Typ eksportu**, który chcesz skonfigurować (np. Infor, IDM, SFTP).
3. Wypełnij wymagane pola w zależności od typu eksportu.
4. Zapisz konfigurację.

## Opcje eksportu

#### Webhook

<details>

<summary>Webhook</summary>

![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/export_webhook_configuration.png)

**Opisy pól**

* **Title** Nazwa konfiguracji eksportu. Pojawi się na liście eksportów.
* **Sub-Organization** _(opcjonalnie)_ Lista rozwijana ze wszystkimi dostępnymi podorganizacjami.
  * Jeśli pozostawione puste: dotyczy głównej organizacji.
  * Jeśli wybrane: eksport będzie dotyczył tylko wybranej podorganizacji.
* **Document Type** Lista rozwijana zawierająca wszystkie dostępne typy dokumentów. Określa, do jakiego typu dokumentu odnosi się ta konfiguracja eksportu.
* **Export URL** Docelowy URL, gdzie dokument powinien zostać wyeksportowany.

</details>

#### SFTP

<details>

<summary>SFTP</summary>

![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/export_sftp_configuration.png)

**Opisy pól**

* **Title** Nazwa konfiguracji eksportu. Pojawi się na liście eksportów.
* **Sub-Organization** _(opcjonalnie)_ Lista rozwijana ze wszystkimi dostępnymi podorganizacjami.
  * Jeśli pozostawione puste: dotyczy głównej organizacji.
  * Jeśli wybrane: eksport będzie dotyczył tylko wybranej podorganizacji.
* **Document Type** Lista rozwijana zawierająca wszystkie dostępne typy dokumentów. Określa, do jakiego typu dokumentu odnosi się ta konfiguracja eksportu.
* **Username** Nazwa użytkownika używana do uwierzytelniania na serwerze SFTP.
* **Password** Odpowiednie hasło do konta SFTP. Upewnij się, że konto ma dostęp do zapisu w określonym folderze.
* **Server URL** Nazwa hosta lub adres IP docelowego serwera SFTP.
* **Port** Port używany do połączenia z serwerem SFTP.
* **Folder** Ścieżka na serwerze SFTP, gdzie dokumenty powinny być przesyłane (np. `/incoming/invoices/`). Musi istnieć i być zapisywalny.
*   **XSLT File (Opcjonalnie)**

    **Plik XSLT** umożliwia transformację domyślnego formatu eksportu DocBits.

    * **Kiedy używać:** Tylko jeśli system odbierający wymaga innej struktury lub specyficznego formatowania, które różni się od domyślnego formatu DocBits.
    * **Pozostaw puste** jeśli domyślny format eksportu spełnia wymagania.



**Ustawienia zaawansowane:**

* **Filename Export Mode** Określa, czy wyeksportowany plik zachowuje oryginalną nazwę pliku, czy jest zmieniany na ID dokumentu DocBits.
* **Include Document History** Po włączeniu wyeksportowany plik będzie zawierał historię dokumentu na podstawie logów dostępnych w panelu.

![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/export_sftp_2.png)

![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/export_sftp_3.png)

</details>

#### Eksport Infor do SFTP

<details>

<summary>Eksport Infor do SFTP</summary>

![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/export_infor_sftp_configuration.png)

**Opisy pól**

* **Title** Nazwa konfiguracji eksportu. Pojawi się na liście eksportów.
* **Sub-Organization** _(opcjonalnie)_ Lista rozwijana ze wszystkimi dostępnymi podorganizacjami.
  * Jeśli pozostawione puste: dotyczy głównej organizacji.
  * Jeśli wybrane: eksport będzie dotyczył tylko wybranej podorganizacji.
* **Document Type** Lista rozwijana zawierająca wszystkie dostępne typy dokumentów. Określa, do jakiego typu dokumentu odnosi się ta konfiguracja eksportu.
* **IDM Mapping File** Wybierz plik mapowania z menedżera plików. [Potrzebujesz pomocy przy tworzeniu? Zobacz Przewodnik Mapowania IDM](../../../infor-integration-and-configuration/exporting-to-infor/creating-an-idm-mapping-file.md)
* **BOD Mapping File** Wybierz plik mapowania z menedżera plików. [Potrzebujesz pomocy przy tworzeniu? Zobacz Przewodnik Mapowania BOD](../../../infor-integration-and-configuration/exporting-to-infor/creating-a-bod-mapping-file.md)
* **Folder** Ścieżka na serwerze SFTP, gdzie dokumenty powinny być przesyłane (np. `/incoming/invoices/`). Musi istnieć i być zapisywalny.

</details>

#### **SMB**

<details>

<summary>SMB</summary>

![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/export_smb_configuration.png)

**Opisy pól**

* **Title** Nazwa konfiguracji eksportu. Pojawi się na liście eksportów.
* **Sub-Organization** _(opcjonalnie)_ Lista rozwijana ze wszystkimi dostępnymi podorganizacjami.
  * Jeśli pozostawione puste: dotyczy głównej organizacji.
  * Jeśli wybrane: eksport będzie dotyczył tylko wybranej podorganizacji.
* **Document Type** Lista rozwijana zawierająca wszystkie dostępne typy dokumentów. Określa, do jakiego typu dokumentu odnosi się ta konfiguracja eksportu.
* **Username** Nazwa użytkownika używana do połączenia z udziałem SMB.
* **Password** Odpowiednie hasło do uwierzytelniania SMB.
* **Server URL** Adres serwera SMB.
* **Port** Numer portu używany do dostępu do udziału SMB.
* **Folder** Ścieżka folderu w udziale SMB, gdzie dokumenty powinny być zapisywane (np. `/incoming/invoices/`). Musi istnieć i być zapisywalny.
*   **JPL Mapping File (Opcjonalnie)**

    **Plik JPL** służy do definiowania transformacji eksportowanych danych przed ich zapisaniem w udziale SMB.

    * **Kiedy używać:** Tylko gdy eksportowane dane dokumentu muszą być dostosowane do zewnętrznego formatowania lub oczekiwań systemu.
    * **Pozostaw puste** jeśli nie jest wymagana żadna transformacja.

</details>

#### **Infor IDM**

<details>

<summary>Infor IDM</summary>

![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/export_infor_idm_configuration.png)

**Opisy pól**

* **Title** Nazwa konfiguracji eksportu. Pojawi się na liście eksportów.
* **Sub-Organization** _(opcjonalnie)_ Lista rozwijana ze wszystkimi dostępnymi podorganizacjami.
  * Jeśli pozostawione puste: dotyczy głównej organizacji.
  * Jeśli wybrane: eksport będzie dotyczył tylko wybranej podorganizacji.
* **Document Type** Lista rozwijana zawierająca wszystkie dostępne typy dokumentów. Określa, do jakiego typu dokumentu odnosi się ta konfiguracja eksportu.
* **ION Mapping File** Wybierz plik mapowania z menedżera plików.
* **IDM Mapping File** Wybierz plik mapowania z menedżera plików. [Potrzebujesz pomocy przy tworzeniu? Zobacz Przewodnik Mapowania IDM](../../../infor-integration-and-configuration/exporting-to-infor/creating-an-idm-mapping-file.md)
* **Cloud / On-Prem Toggle** Przełącznik wskazujący typ wdrożenia Infor:
  * **Cloud**: Wybierz to, jeśli jesteś klientem Infor CloudSuite.
  * **On-Prem**: Wybierz to, jeśli Infor jest hostowany samodzielnie.

</details>

#### **Infor ION**

<details>

<summary>Infor ION</summary>

![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/export_infor_ion_configuration.png)

**Opisy pól**

* **Title** Nazwa konfiguracji eksportu. Pojawi się na liście eksportów.
* **Sub-Organization** _(opcjonalnie)_ Lista rozwijana ze wszystkimi dostępnymi podorganizacjami.
  * Jeśli pozostawione puste: dotyczy głównej organizacji.
  * Jeśli wybrane: eksport będzie dotyczył tylko wybranej podorganizacji.
* **Document Type** Lista rozwijana zawierająca wszystkie dostępne typy dokumentów. Określa, do jakiego typu dokumentu odnosi się ta konfiguracja eksportu.
* **ION Mapping File** Wybierz plik mapowania z menedżera plików.
* **BOD Mapping File** Wybierz plik mapowania z menedżera plików. [Potrzebujesz pomocy przy tworzeniu? Zobacz Przewodnik Mapowania BOD](../../../infor-integration-and-configuration/exporting-to-infor/creating-a-bod-mapping-file.md)
* **Cloud / On-Prem Toggle** Przełącznik wskazujący typ wdrożenia Infor:
  * **Cloud**: Wybierz to, jeśli jesteś klientem Infor CloudSuite.
  * **On-Prem**: Wybierz to, jeśli Infor jest hostowany samodzielnie.

</details>

#### Infor IDM + ION BOD

<details>

<summary>Infor IDM + ION BOD</summary>

![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/export_infor_idm_ion_bod_configuration.png)

**Opisy pól**

* **Title** Nazwa konfiguracji eksportu. Pojawi się na liście eksportów.
* **Sub-Organization** _(opcjonalnie)_ Lista rozwijana ze wszystkimi dostępnymi podorganizacjami.
  * Jeśli pozostawione puste: dotyczy głównej organizacji.
  * Jeśli wybrane: eksport będzie dotyczył tylko wybranej podorganizacji.
* **Document Type** Lista rozwijana zawierająca wszystkie dostępne typy dokumentów. Określa, do jakiego typu dokumentu odnosi się ta konfiguracja eksportu.
* **ION Mapping File** Wybierz plik mapowania z menedżera plików.
* **IDM Mapping File** Wybierz plik mapowania z menedżera plików. [Potrzebujesz pomocy przy tworzeniu? Zobacz Przewodnik Mapowania IDM](../../../infor-integration-and-configuration/exporting-to-infor/creating-an-idm-mapping-file.md)
* **BOD Mapping File** Wybierz plik mapowania z menedżera plików. [Potrzebujesz pomocy przy tworzeniu? Zobacz Przewodnik Mapowania BOD](../../../infor-integration-and-configuration/exporting-to-infor/creating-a-bod-mapping-file.md)
* **Cloud / On-Prem Toggle** Przełącznik wskazujący typ wdrożenia Infor:
  * **Cloud**: Wybierz to, jeśli jesteś klientem Infor CloudSuite.
  * **On-Prem**: Wybierz to, jeśli Infor jest hostowany samodzielnie.

</details>

### Dla klientów Infor CloudSuite

#### Infor IDM + LN

<details>

<summary>Infor IDM + LN</summary>

![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/export_infor_idm_ln_configuration.png)

**Opisy pól**

* **Title** Nazwa konfiguracji eksportu. Pojawi się na liście eksportów.
* **Sub-Organization** _(opcjonalnie)_ Lista rozwijana ze wszystkimi dostępnymi podorganizacjami.
  * Jeśli pozostawione puste: dotyczy głównej organizacji.
  * Jeśli wybrane: eksport będzie dotyczył tylko wybranej podorganizacji.
* **Document Type** Lista rozwijana zawierająca wszystkie dostępne typy dokumentów. Określa, do jakiego typu dokumentu odnosi się ta konfiguracja eksportu.
* **ION Mapping File** Wybierz plik mapowania z menedżera plików.
* **IDM Mapping File** Wybierz plik mapowania z menedżera plików. [Potrzebujesz pomocy przy tworzeniu? Zobacz Przewodnik Mapowania IDM](../../../infor-integration-and-configuration/exporting-to-infor/creating-an-idm-mapping-file.md)
* **LN Mapping File** Wybierz plik mapowania z menedżera plików. [Potrzebujesz pomocy przy tworzeniu? Zobacz Przykład Mapowania LN](../../../infor-integration-and-configuration/exporting-to-infor/ln/example-export-ln/)

</details>

#### Infor IDM + M3

<details>

<summary>Infor IDM + M3</summary>

![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/export_infor_idm_m3_configuration.png)

**Opisy pól**

* **Title** Nazwa konfiguracji eksportu. Pojawi się na liście eksportów.
* **Sub-Organization** _(opcjonalnie)_ Lista rozwijana ze wszystkimi dostępnymi podorganizacjami.
  * Jeśli pozostawione puste: dotyczy głównej organizacji.
  * Jeśli wybrane: eksport będzie dotyczył tylko wybranej podorganizacji.
* **Document Type** Lista rozwijana zawierająca wszystkie dostępne typy dokumentów. Określa, do jakiego typu dokumentu odnosi się ta konfiguracja eksportu.
* **ION Mapping File** Wybierz plik mapowania z menedżera plików.
* **IDM Mapping File** Wybierz plik mapowania z menedżera plików. [Potrzebujesz pomocy przy tworzeniu? Zobacz Przewodnik Mapowania IDM](../../../infor-integration-and-configuration/exporting-to-infor/creating-an-idm-mapping-file.md)
* **M3 Mapping File** Wybierz plik mapowania z menedżera plików. [Potrzebujesz pomocy przy tworzeniu? Zobacz Przykład Mapowania M3](../../../infor-integration-and-configuration/exporting-to-infor/m3/example-export-m3.md)

</details>

#### Infor IDM + M3 (toml)

<details>

<summary>Infor IDM + M3 (toml)</summary>

![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/export_infor_idm_m3_toml_configuration.png)

**Opisy pól**

* **Title** Nazwa konfiguracji eksportu. Pojawi się na liście eksportów.
* **Sub-Organization** _(opcjonalnie)_ Lista rozwijana ze wszystkimi dostępnymi podorganizacjami.
  * Jeśli pozostawione puste: dotyczy głównej organizacji.
  * Jeśli wybrane: eksport będzie dotyczył tylko wybranej podorganizacji.
* **Document Type** Lista rozwijana zawierająca wszystkie dostępne typy dokumentów. Określa, do jakiego typu dokumentu odnosi się ta konfiguracja eksportu.
* **ION Mapping File** Wybierz plik mapowania z menedżera plików.
* **IDM Mapping File** Wybierz plik mapowania z menedżera plików. [Potrzebujesz pomocy przy tworzeniu? Zobacz Przewodnik Mapowania IDM](../../../infor-integration-and-configuration/exporting-to-infor/creating-an-idm-mapping-file.md)
* **M3 toml Mapping File** Wybierz plik mapowania z menedżera plików lub użyj opcji wybierz Toml, aby użyć pliku toml utworzonego za pomocą menedżera reguł. [Potrzebujesz pomocy przy tworzeniu? Zobacz Przewodnik Menedżera Reguł](rule-manager/)

</details>
