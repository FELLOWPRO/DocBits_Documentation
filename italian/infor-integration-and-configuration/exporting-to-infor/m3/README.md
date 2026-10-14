# M3

## Passo 1: Creare un Connection Point

1. Navigare in **OS > ION > Connect > Connection Points**
2. Fare clic su **Add** e selezionare **IMS via API Gateway** come tipo di connessione.
3. Configurare le seguenti impostazioni:
   * **Name**: Impostare su `DocBits_Export`.
   * **Description**: Impostare su `DocBits_Export`.
   * **Uncheck**: _Application has IMS End Point_.
   * **ION API Client ID**:
     * Aprire il file ION API.
     * Cercare `"ci"` all'interno del file.
     * Copiare il valore tra le virgolette (senza le virgolette).

![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/export_to_m3_from_docbits_1.png)

4. In **Documents**, aggiungere `Sync.CaptureDocument`.

![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/export_to_m3_from_docbits_2.png)

5. Fare clic su **Save** per finalizzare la configurazione.

## Passo 2: Caricare i Mappings

{% file src="../../../.gitbook/assets/CaptureDocument_to_ProcessSupplierInvoice.xml" %}

1. Scaricare il file M3 Mapping.
2. Navigare in **Infor** > **OS** > **ION** > **Connect** > **Mappings**.
3. Fare clic su **Import** e selezionare il file di mapping appropriato per **M3**.

![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/export_to_m3_from_docbits_3.png)

4. Una volta importati i file, approvare i mappings per attivarli.

![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/export_to_m3_from_docbits_4.png)

## Passo 3: Creare il Data Flow

1. Navigare in **OS** -> **ION** -> **Connect** -> **Data Flows**.
2. Fare clic su **Add** e selezionare **Document Flow**.
3. Inserire i dettagli:
   * **Name**: `DocBits_Export_to_M3`
4. Aggiungere nodi al flusso:

#### Application Node

1. Aggiungere un **Application Node** al flusso.
   * **Name**: `DocBits` o `DocBits-Export`.
2. Fare clic su **Add** e selezionare il **Connection Point** creato nel Passo 1.

![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/export_to_m3_from_docbits_5.png)

3. Fare clic sull'**Document Icon** accanto all'Application Node.
   * Fare clic su **Add** e selezionare `Sync.CaptureDocument`.

![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/export_to_m3_from_docbits_6.png)

#### Mapping Node

1. Aggiungere un **Mapping Node** a destra dell'Application Node.
   * **Name**: `Capt2process`.
   * **Mapping**: `CaptureDocument_to_ProcessSupplierInvoice`.

![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/export_to_m3_from_docbits_7.png)

#### Application Node

1. Aggiungere un **Application Node** a destra del Mapping Node precedente.
   * **Name**: `M3`.
2. Fare clic su **Add** e selezionare l'**M3 Application** del cliente.

![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/export_to_m3_from_docbits_8.png)

3. Fare clic sull'**Document Icon** accanto all'Application Node.
   * Fare clic su **Add** e selezionare `Acknowledge.SupplierInvoice`.

![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/export_to_m3_from_docbits_9.png)

#### API Node

1. Aggiungere un **API Node** a destra dell'Application Node.
   * **Name**: `DocBits-Error`.
   * **ION API Connector**: `DocBits_Import`.
   * Se `DocBits_Import` non esiste, consultare il **Passo 1** e il **Passo 2** della documentazione Import from M3 per creare il Connection Point.

![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/export_to_m3_from_docbits_10.png)

#### Salvare e attivare il Flow

* Una volta aggiunti e configurati tutti i nodi, fare clic su **Save**.
* Attivare il flusso per completare la configurazione.

![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/export_to_m3_from_docbits_11%20\(1\).png)

## Passo 4: Configurare l'Export in DocBits

### On-Premise:

1. Aprire **DocBits**.
2.  Navigare in **Impostazioni > Elaborazione documenti > Esporta**.

    ![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/settings_export.png)
3. Creare una nuova esportazione:
   * **Seleziona**: **Infor IDM + ION BOD**.
   * **Titolo**: Scegliere un titolo significativo.
   * **Tipo di documento**: Impostare su **Fattura**.
   * **Sotto-organizzazione**: Può essere lasciato vuoto o impostato su una sotto-organizzazione specifica se necessario.
4. **Caricare i file richiesti**:
   * **ION Mapping File**: È possibile trovarlo in **Infor OS → API Gateway → Authorized Apps**. Cercare l'applicazione **DocBits**, aprirla e scaricare le credenziali.
   * **IDM Mapping File**: (Fornire il percorso del file o la posizione rilevante).
   * **BOD Mapping File**: (Fornire il percorso del file o la posizione rilevante).

### Cloud:

1. Aprire **DocBits**.
2.  Navigare in **Impostazioni > Elaborazione documenti > Esporta**.

    ![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/settings_export.png)
3. Creare una nuova esportazione:
   * **Seleziona**: **Infor IDM + M3 (API)**.
   * **Titolo**: Scegliere un titolo significativo.
   * **Tipo di documento**: Impostare su **Fattura**.
   * **Sotto-organizzazione**: Può essere lasciato vuoto o impostato su una sotto-organizzazione specifica se necessario.
4. **Caricare i file richiesti**:
   * **ION Mapping File**: È possibile trovarlo in **Infor OS → API Gateway → Authorized Apps**. Cercare l'applicazione **DocBits**, aprirla e scaricare le credenziali.
   * **IDM Mapping File**: (Fornire il percorso del file o la posizione rilevante).
   * **M3 Mapping File**: (Fornire il percorso del file o la posizione rilevante).

### Cloud con toml:

1. Aprire **DocBits**.
2.  Navigare in **Impostazioni > Elaborazione documenti > Esporta**.

    ![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/settings_export.png)
3. Creare una nuova esportazione:
   * **Seleziona**: **Infor IDM + M3 (API)**.
   * **Titolo**: Scegliere un titolo significativo.
   * **Tipo di documento**: Impostare su **Fattura**.
   * **Sotto-organizzazione**: Può essere lasciato vuoto o impostato su una sotto-organizzazione specifica se necessario.
4. **Caricare i file richiesti**:
   * **ION Mapping File**: È possibile trovarlo in **Infor OS → API Gateway → Authorized Apps**. Cercare l'applicazione **DocBits**, aprirla e scaricare le credenziali.
   * **IDM Mapping File**: (Fornire il percorso del file o la posizione rilevante).
   * **M3 toml Mapping File**: (Fornire il percorso del file o la posizione rilevante).
