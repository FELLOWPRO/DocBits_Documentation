# M3

## Krok 1: Utwórz Connection Point

1. Przejdź do **OS > ION > Connect > Connection Points**
2. Kliknij **Add** i wybierz **IMS via API Gateway** jako typ połączenia.
3. Skonfiguruj następujące ustawienia:
   * **Name**: Ustaw na `DocBits_Export`.
   * **Description**: Ustaw na `DocBits_Export`.
   * **Odznacz**: _Aplikacja ma IMS Punkt końcowy_.
   * **ION API Client ID**:
     * Otwórz plik ION API.
     * Wyszukaj `"ci"` w pliku.
     * Skopiuj wartość w cudzysłowach (bez cudzysłowów).

![Strona Infor Application Connection Point dla IMS przez API Gateway z nazwą DocBits_Export, opisem i polami ION API Client ID](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/export_to_m3_from_docbits_1.png)

4. W sekcji **Documents** dodaj `Sync.CaptureDocument`.

![Strona Connection Point DocBits_Export z sekcją Documents zawierającą Sync.CaptureDocument ustawione na Send from Application](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/export_to_m3_from_docbits_2.png)

5. Kliknij **Save**, aby sfinalizować konfigurację.

## Krok 2: Prześlij Mappings

{% file src="../../../.gitbook/assets/CaptureDocument_to_ProcessSupplierInvoice.xml" %}

1. Pobierz plik M3 Mapping.
2. Przejdź do **Infor** > **OS** > **ION** > **Connect** > **Mappings**.
3. Kliknij **Import** i wybierz odpowiedni plik mapping dla **M3**.

![Przycisk dodawania na pasku narzędzi strony Mappings w Infor ION Connect](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/export_to_m3_from_docbits_3.png)

4. Po zaimportowaniu plików zatwierdź mappings, aby je aktywować.

![Przegląd mapowań w ION Connect z zatwierdzonym mapowaniem z Sync.CaptureDocument na ProcessSupplierInvoice](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/export_to_m3_from_docbits_4.png)

## Krok 3: Utwórz Data Flow

1. Przejdź do **OS** -> **ION** -> **Connect** -> **Data Flows**.
2. Kliknij **Add** i wybierz **Document Flow**.
3. Wypełnij szczegóły:
   * **Name**: `DocBits_Export_to_M3`
4. Dodaj węzły do przepływu:

#### Węzeł aplikacji

1. Dodaj **Application Node** do przepływu.
   * **Name**: `DocBits` lub `DocBits-Export`.
2. Kliknij **Add** i wybierz **Connection Point** utworzony w Kroku 1.

![Edytor Data Flow z otwartą paletą węzłów i panelem Application Activity Properties nazywającym węzeł DocBits-Dev-Demo-Export](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/export_to_m3_from_docbits_5.png)

3. Kliknij **Document Icon** obok Application Node.
   * Kliknij **Add** i wybierz `Sync.CaptureDocument`.

![Edytor Data Flow pokazujący listę Documents węzła aplikacji z dodanym Sync.CaptureDocument](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/export_to_m3_from_docbits_6.png)

#### Węzeł mapowania

1. Dodaj **Mapping Node** po prawej stronie Application Node.
   * **Name**: `Capt2process`.
   * **Mapping**: `CaptureDocument_to_ProcessSupplierInvoice`.

![Edytor Data Flow z panelem Mapping Properties pokazującym nazwę i wybrane mapowanie dla węzła](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/export_to_m3_from_docbits_7.png)

#### Węzeł aplikacji

1. Dodaj **Application Node** po prawej stronie poprzedniego Mapping Node.
   * **Name**: `M3`.
2. Kliknij **Add** i wybierz **M3 Application** klienta.

![Edytor Data Flow z panelem Application Activity Properties i węzłem aplikacji M3 o nazwie M3 BODs](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/export_to_m3_from_docbits_8.png)

3. Kliknij **Document Icon** obok Application Node.
   * Kliknij **Add** i wybierz `Acknowledge.SupplierInvoice`.

![Edytor Data Flow pokazujący listę Documents węzła aplikacji M3 z dodanym Acknowledge.SupplierInvoice](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/export_to_m3_from_docbits_9.png)

#### Węzeł API

1. Dodaj **API Node** po prawej stronie Application Node.
   * **Name**: `DocBits-Error`.
   * **ION API Connector**: `DocBits_Import`.
   * Jeśli `DocBits_Import` nie istnieje, zapoznaj się z **Krokiem 1** i **Krokiem 2** dokumentacji Import from M3, aby utworzyć Connection Point.

![Edytor Data Flow z panelem ION API Activity Properties nazywającym konektor DocBits-Dev-Demo-Import dla węzła API](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/export_to_m3_from_docbits_10.png)

#### Zapisz i aktywuj Flow

* Po dodaniu i skonfigurowaniu wszystkich węzłów kliknij **Save**.
* Aktywuj przepływ, aby zakończyć konfigurację.

![Data Flow editor with the connection point panel open showing the flow name DocBits_Demo_to_M3](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/export_to_m3_from_docbits_11%20\(1\).png)

## Krok 4: Skonfiguruj Export w DocBits

### Lokalnie:

1. Otwórz **DocBits**.
2.  Przejdź do **Ustawienia > Przetwarzanie dokumentów > Eksportuj**.

    ![Strona ustawień w DocBits z otwartą nawigacją Document Processing zawierającą Import, OCR Settings, Classification and Extraction i Module](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/settings_export.png)
3. Utwórz nowy eksport:
   * **Wybierz**: **Infor IDM + ION BOD**.
   * **Tytuł**: Wybierz znaczący tytuł.
   * **Typ dokumentu**: Ustaw na **Faktura**.
   * **Podorganizacja**: Może być pozostawione puste lub ustawione na konkretną podorganizację, jeśli jest to wymagane.
4. **Prześlij wymagane pliki**:
   * **ION Mapping File**: Można go znaleźć w **Infor OS → API Gateway → Authorized Apps**. Wyszukaj aplikację **DocBits**, otwórz ją i pobierz dane uwierzytelniające.
   * **IDM Mapping File**: (Podaj odpowiednią ścieżkę pliku lub lokalizację).
   * **BOD Mapping File**: (Podaj odpowiednią ścieżkę pliku lub lokalizację).

### Chmura:

1. Otwórz **DocBits**.
2.  Przejdź do **Ustawienia > Przetwarzanie dokumentów > Eksportuj**.

    ![Strona ustawień w DocBits z otwartą nawigacją Document Processing zawierającą Import, OCR Settings, Classification and Extraction i Module](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/settings_export.png)
3. Utwórz nowy eksport:
   * **Wybierz**: **Infor IDM + M3 (API)**.
   * **Tytuł**: Wybierz znaczący tytuł.
   * **Typ dokumentu**: Ustaw na **Faktura**.
   * **Podorganizacja**: Może być pozostawione puste lub ustawione na konkretną podorganizację, jeśli jest to wymagane.
4. **Prześlij wymagane pliki**:
   * **ION Mapping File**: Można go znaleźć w **Infor OS → API Gateway → Authorized Apps**. Wyszukaj aplikację **DocBits**, otwórz ją i pobierz dane uwierzytelniające.
   * **IDM Mapping File**: (Podaj odpowiednią ścieżkę pliku lub lokalizację).
   * **M3 Mapping File**: (Podaj odpowiednią ścieżkę pliku lub lokalizację).

### Cloud z toml:

1. Otwórz **DocBits**.
2.  Przejdź do **Ustawienia > Przetwarzanie dokumentów > Eksportuj**.

    ![Strona ustawień w DocBits z otwartą nawigacją Document Processing zawierającą Import, OCR Settings, Classification and Extraction i Module](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/settings_export.png)
3. Utwórz nowy eksport:
   * **Wybierz**: **Infor IDM + M3 (API)**.
   * **Tytuł**: Wybierz znaczący tytuł.
   * **Typ dokumentu**: Ustaw na **Faktura**.
   * **Podorganizacja**: Może być pozostawione puste lub ustawione na konkretną podorganizację, jeśli jest to wymagane.
4. **Prześlij wymagane pliki**:
   * **ION Mapping File**: Można go znaleźć w **Infor OS → API Gateway → Authorized Apps**. Wyszukaj aplikację **DocBits**, otwórz ją i pobierz dane uwierzytelniające.
   * **IDM Mapping File**: (Podaj odpowiednią ścieżkę pliku lub lokalizację).
   * **M3 toml Mapping File**: (Podaj odpowiednią ścieżkę pliku lub lokalizację).
