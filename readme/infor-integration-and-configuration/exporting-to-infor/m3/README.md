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

![Venster Infor Application Connection Point IMS via API Gateway met de tabbladen Usage, Connection en Documents, de naam DocBits_Export, de niet aangevinkte optie Application has IMS End Point, het veld ION API Client ID en de Logical ID inforims.docbits_export](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/export_to_m3_from_docbits_1.png)

4. Voeg onder **Documents** `Sync.CaptureDocument` toe.

![Tabblad Connection van het toepassingspunt met de naam DocBits_Export, het document sync.captureDocument als Send from Application en de Logical ID inforims.docbits_export](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/export_to_m3_from_docbits_2.png)

5. Klik op **Save** om de configuratie te voltooien.

## Stap 2: Mappings uploaden

{% file src="../../../.gitbook/assets/CaptureDocument_to_ProcessSupplierInvoice.xml" %}

1. Download het M3 Mapping bestand.
2. Navigeer naar **Infor** > **OS** > **ION** > **Connect** > **Mappings**.
3. Klik op **Import** en selecteer het juiste mapping bestand voor **M3**.

![Pagina Mappings in ION Desk met het zoekveld, de filterbediening en de knop Add](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/export_to_m3_from_docbits_3.png)

4. Zodra de bestanden zijn geïmporteerd, keur de mappings goed om ze te activeren.

![Geïmporteerde toewijzing met de bron Sync.CaptureDocument en het doel Process.SupplierInvoice](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/export_to_m3_from_docbits_4.png)

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

![Gegevensstroom in ION Desk met de knooppuntkeuze boven en het paneel Application Activity Properties rechts met de naam DocBits-Dev-Demo-Export](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/export_to_m3_from_docbits_5.png)

3. Klik op het **Document Icon** naast de Application Node.
   * Klik op **Add** en selecteer `Sync.CaptureDocument`.

![Gegevensstroom in ION Desk met het toepassingsknooppunt geselecteerd en het paneel Documents open met de vermelding Sync.CaptureDocument](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/export_to_m3_from_docbits_6.png)

#### Mappingknooppunt

1. Voeg een **Mapping Node** toe rechts van de Application Node.
   * **Name**: `Capt2process`.
   * **Mapping**: `CaptureDocument_to_ProcessSupplierInvoice`.

![Gegevensstroom in ION Desk met het toewijzingsknooppunt geselecteerd en het paneel Mapping Properties rechts met de naam en de toewijzing SyncCaptDoc_SyncSuppInv](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/export_to_m3_from_docbits_7.png)

#### Applicatieknooppunt

1. Voeg een **Application Node** toe rechts van de vorige Mapping Node.
   * **Name**: `M3`.
2. Klik op **Add** en selecteer de **M3 Application** van de klant.

![Gegevensstroom in ION Desk met het M3-toepassingsknooppunt geselecteerd en het paneel Application Activity Properties rechts met de vermelding M3 BODs](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/export_to_m3_from_docbits_8.png)

3. Klik op het **Document Icon** naast de Application Node.
   * Klik op **Add** en selecteer `Acknowledge.SupplierInvoice`.

![Gegevensstroom in ION Desk met het M3-toepassingsknooppunt geselecteerd en het paneel Documents open met de vermelding Acknowledge.SupplierInvoice](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/export_to_m3_from_docbits_9.png)

#### API-knooppunt

1. Voeg een **API Node** toe rechts van de Application Node.
   * **Name**: `DocBits-Error`.
   * **ION API Connector**: `DocBits_Import`.
   * Als `DocBits_Import` niet bestaat, raadpleeg **Stap 1** en **Stap 2** van de Import from M3 documentatie om het Connection Point aan te maken.

![Gegevensstroom in ION Desk met het API-knooppunt geselecteerd en het paneel ION API Activity Properties rechts met de ION API Connector DocBits Dev Demo-Import](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/export_to_m3_from_docbits_10.png)

#### Flow opslaan en activeren

* Zodra alle nodes zijn toegevoegd en geconfigureerd, klik op **Save**.
* Activeer de flow om de setup te voltooien.

![Gegevensstroom in ION Desk met de knooppunten DocBits_Demo_to_M3, het toewijzingsknooppunt, het M3-knooppunt en het foutknooppunt in een rij verbonden en de knop REMOVE CONNECTION POINTS boven het werkvlak](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/export_to_m3_from_docbits_11%20\(1\).png)

## Stap 4: Export configureren in DocBits

### Op locatie:

1. Open **DocBits**.
2.  Navigeer naar **Instellingen > Documentverwerking > Exporteren**.

    ![Instellingenpagina in DocBits met de uitgeklapte navigatiegroep Document Processing en de items Documents, Expiry, Import, Rule Management, OCR Settings, Classification and Extraction, Master Data Lookup, List of Values en Module](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/settings_export.png)
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

    ![Instellingenpagina in DocBits met de uitgeklapte navigatiegroep Document Processing en de items Documents, Expiry, Import, Rule Management, OCR Settings, Classification and Extraction, Master Data Lookup, List of Values en Module](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/settings_export.png)
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

    ![Instellingenpagina in DocBits met de uitgeklapte navigatiegroep Document Processing en de items Documents, Expiry, Import, Rule Management, OCR Settings, Classification and Extraction, Master Data Lookup, List of Values en Module](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/settings_export.png)
3. Maak een nieuwe export aan:
   * **Selecteren**: **Infor IDM + M3 (API)**.
   * **Titel**: Kies een betekenisvolle titel.
   * **Documenttype**: Stel in op **Factuur**.
   * **Suborganisatie**: Kan leeg gelaten worden of ingesteld worden op een specifieke suborganisatie indien nodig.
4. **Upload de vereiste bestanden**:
   * **ION Mapping File**: Deze kan worden gevonden in **Infor OS → API Gateway → Authorized Apps**. Zoek naar de **DocBits** app, open deze en download de credentials.
   * **IDM Mapping File**: (Geef het relevante bestandspad of locatie op).
   * **M3 toml Mapping File**: (Geef het relevante bestandspad of locatie op).
