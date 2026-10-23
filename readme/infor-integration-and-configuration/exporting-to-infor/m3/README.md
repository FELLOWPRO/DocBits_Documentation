# M3

## Stap 1: Een Connection Point aanmaken

1. Navigeer naar **OS > ION > Connect > Connection Points**
2. Klik op **Add** en selecteer **IMS via API Gateway** als verbindingstype.
3. Configureer de volgende instellingen:
   * **Name**: Stel in op `DocBits_Export`.
   * **Description**: Stel in op `DocBits_Export`.
   * **Deselecteer**: _Applicatie heeft IMS Eindpunt_.
   * **ION API Client ID**:
     * Open het ION API bestand.
     * Zoek naar `"ci"` binnen het bestand.
     * Kopieer de waarde binnen de aanhalingstekens (zonder de aanhalingstekens).

![Infor Application Connection Point-pagina voor IMS via API Gateway met naam DocBits_Export, beschrijving en ION API Client ID-velden](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/export_to_m3_from_docbits_1.png)

4. Voeg onder **Documents** `Sync.CaptureDocument` toe.

![Connection Point-pagina DocBits_Export met de sectie Documents met daarin Sync.CaptureDocument ingesteld op Send from Application](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/export_to_m3_from_docbits_2.png)

5. Klik op **Save** om de configuratie te voltooien.

## Stap 2: Mappings uploaden

{% file src="../../../.gitbook/assets/CaptureDocument_to_ProcessSupplierInvoice.xml" %}

1. Download het M3 Mapping bestand.
2. Navigeer naar **Infor** > **OS** > **ION** > **Connect** > **Mappings**.
3. Klik op **Import** en selecteer het juiste mapping bestand voor **M3**.

![Toevoegen-knop in de werkbalk van de Infor ION Connect Mappings-pagina](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/export_to_m3_from_docbits_3.png)

4. Zodra de bestanden zijn geïmporteerd, keur de mappings goed om ze te activeren.

![Mapping-overzicht in ION Connect met de goedgekeurde koppeling van Sync.CaptureDocument naar ProcessSupplierInvoice](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/export_to_m3_from_docbits_4.png)

## Stap 3: De Data Flow aanmaken

1. Navigeer naar **OS** -> **ION** -> **Connect** -> **Data Flows**.
2. Klik op **Add** en selecteer **Document Flow**.
3. Vul de details in:
   * **Name**: `DocBits_Export_to_M3`
4. Voeg nodes toe aan de flow:

#### Applicatieknooppunt

1. Voeg een **Application Node** toe aan de flow.
   * **Name**: `DocBits` of `DocBits-Export`.
2. Klik op **Add** en selecteer het **Connection Point** dat in Stap 1 is aangemaakt.

![Data Flow-editor met open knooppuntpalet en het paneel Application Activity Properties dat het knooppunt DocBits-Dev-Demo-Export benoemt](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/export_to_m3_from_docbits_5.png)

3. Klik op het **Document Icon** naast de Application Node.
   * Klik op **Add** en selecteer `Sync.CaptureDocument`.

![Data Flow-editor met de lijst Documents van het applicatieknooppunt waaraan Sync.CaptureDocument is toegevoegd](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/export_to_m3_from_docbits_6.png)

#### Mappingknooppunt

1. Voeg een **Mapping Node** toe rechts van de Application Node.
   * **Name**: `Capt2process`.
   * **Mapping**: `CaptureDocument_to_ProcessSupplierInvoice`.

![Data Flow-editor met het paneel Mapping Properties dat de naam en de geselecteerde mapping voor het knooppunt toont](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/export_to_m3_from_docbits_7.png)

#### Applicatieknooppunt

1. Voeg een **Application Node** toe rechts van de vorige Mapping Node.
   * **Name**: `M3`.
2. Klik op **Add** en selecteer de **M3 Application** van de klant.

![Data Flow-editor met het paneel Application Activity Properties en het M3-applicatieknooppunt met de naam M3 BODs](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/export_to_m3_from_docbits_8.png)

3. Klik op het **Document Icon** naast de Application Node.
   * Klik op **Add** en selecteer `Acknowledge.SupplierInvoice`.

![Data Flow-editor met de lijst Documents van het M3-applicatieknooppunt waaraan Acknowledge.SupplierInvoice is toegevoegd](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/export_to_m3_from_docbits_9.png)

#### API-knooppunt

1. Voeg een **API Node** toe rechts van de Application Node.
   * **Name**: `DocBits-Error`.
   * **ION API Connector**: `DocBits_Import`.
   * Als `DocBits_Import` niet bestaat, raadpleeg **Stap 1** en **Stap 2** van de Import from M3 documentatie om het Connection Point aan te maken.

![Data Flow-editor met het paneel ION API Activity Properties dat de connector DocBits-Dev-Demo-Import voor het API-knooppunt benoemt](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/export_to_m3_from_docbits_10.png)

#### Flow opslaan en activeren

* Zodra alle nodes zijn toegevoegd en geconfigureerd, klik op **Save**.
* Activeer de flow om de setup te voltooien.

![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/export_to_m3_from_docbits_11%20\(1\).png)

## Stap 4: Export configureren in DocBits

### Op locatie:

1. Open **DocBits**.
2.  Navigeer naar **Instellingen > Documentverwerking > Exporteren**.

    ![Instellingenpagina in DocBits met de Document Processing-navigatie open met Import, OCR Settings, Classification and Extraction en Module](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/settings_export.png)
3. Maak een nieuwe export aan:
   * **Selecteren**: **Infor IDM + ION BOD**.
   * **Titel**: Kies een betekenisvolle titel.
   * **Documenttype**: Stel in op **Factuur**.
   * **Suborganisatie**: Kan leeg gelaten worden of ingesteld worden op een specifieke suborganisatie indien nodig.
4. **Upload de vereiste bestanden**:
   * **ION Mapping File**: Deze kan worden gevonden in **Infor OS → API Gateway → Authorized Apps**. Zoek naar de **DocBits** app, open deze en download de credentials.
   * **IDM Mapping File**: (Geef het relevante bestandspad of locatie op).
   * **BOD Mapping File**: (Geef het relevante bestandspad of locatie op).

### Cloud:

1. Open **DocBits**.
2.  Navigeer naar **Instellingen > Documentverwerking > Exporteren**.

    ![Instellingenpagina in DocBits met de Document Processing-navigatie open met Import, OCR Settings, Classification and Extraction en Module](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/settings_export.png)
3. Maak een nieuwe export aan:
   * **Selecteren**: **Infor IDM + M3 (API)**.
   * **Titel**: Kies een betekenisvolle titel.
   * **Documenttype**: Stel in op **Factuur**.
   * **Suborganisatie**: Kan leeg gelaten worden of ingesteld worden op een specifieke suborganisatie indien nodig.
4. **Upload de vereiste bestanden**:
   * **ION Mapping File**: Deze kan worden gevonden in **Infor OS → API Gateway → Authorized Apps**. Zoek naar de **DocBits** app, open deze en download de credentials.
   * **IDM Mapping File**: (Geef het relevante bestandspad of locatie op).
   * **M3 Mapping File**: (Geef het relevante bestandspad of locatie op).

### Cloud met toml:

1. Open **DocBits**.
2.  Navigeer naar **Instellingen > Documentverwerking > Exporteren**.

    ![Instellingenpagina in DocBits met de Document Processing-navigatie open met Import, OCR Settings, Classification and Extraction en Module](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/settings_export.png)
3. Maak een nieuwe export aan:
   * **Selecteren**: **Infor IDM + M3 (API)**.
   * **Titel**: Kies een betekenisvolle titel.
   * **Documenttype**: Stel in op **Factuur**.
   * **Suborganisatie**: Kan leeg gelaten worden of ingesteld worden op een specifieke suborganisatie indien nodig.
4. **Upload de vereiste bestanden**:
   * **ION Mapping File**: Deze kan worden gevonden in **Infor OS → API Gateway → Authorized Apps**. Zoek naar de **DocBits** app, open deze en download de credentials.
   * **IDM Mapping File**: (Geef het relevante bestandspad of locatie op).
   * **M3 toml Mapping File**: (Geef het relevante bestandspad of locatie op).
