# M3

## Passo 1: Creare un Punto di Connessione

1. Navigare in **OS > ION > Connect > Connection Points**
2. Fare clic su **Add** e selezionare **IMS via API Gateway** come tipo di connessione.
3. Configurare le seguenti impostazioni:
   * **Name**: Impostare su `DocBits_Export`.
   * **Description**: Impostare su `DocBits_Export`.
   * **Deseleziona**: _L'applicazione ha IMS Punto finale_.
   * **ION API Client ID**:
     * Aprire il file ION API.
     * Cercare `"ci"` all'interno del file.
     * Copiare il valore tra le virgolette (senza le virgolette).

![Finestra Infor Application Connection Point IMS via API Gateway con le schede Usage, Connection e Documents, il nome DocBits_Export, l'opzione Application has IMS End Point non selezionata, il campo ION API Client ID e il Logical ID inforims.docbits_export](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/export_to_m3_from_docbits_1.png)

4. In **Documents**, aggiungere `Sync.CaptureDocument`.

![Scheda Connection del punto applicazione con il nome DocBits_Export, il documento sync.captureDocument come Send from Application e il Logical ID inforims.docbits_export](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/export_to_m3_from_docbits_2.png)

5. Fare clic su **Save** per finalizzare la configurazione.

## Passo 2: Caricare i Mappings

{% file src="../../../.gitbook/assets/CaptureDocument_to_ProcessSupplierInvoice.xml" %}

1. Scaricare il file M3 Mapping.
2. Navigare in **Infor** > **OS** > **ION** > **Connect** > **Mappings**.
3. Fare clic su **Import** e selezionare il file di mapping appropriato per **M3**.

![Pagina Mappings di ION Desk con il campo di ricerca, i controlli di filtro e il pulsante Add](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/export_to_m3_from_docbits_3.png)

4. Una volta importati i file, approvare i mappings per attivarli.

![Mappatura importata con l'origine Sync.CaptureDocument e la destinazione Process.SupplierInvoice](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/export_to_m3_from_docbits_4.png)

## Passo 3: Creare il Data Flow

1. Navigare in **OS** -> **ION** -> **Connect** -> **Data Flows**.
2. Fare clic su **Add** e selezionare **Document Flow**.
3. Inserire i dettagli:
   * **Name**: `DocBits_Export_to_M3`
4. Aggiungere nodi al flusso:

#### Nodo applicazione

1. Aggiungere un **Application Node** al flusso.
   * **Name**: `DocBits` o `DocBits-Export`.
2. Fare clic su **Add** e selezionare il **Connection Point** creato nel Passo 1.

![Flusso di dati in ION Desk con la tavolozza dei nodi in alto e il pannello Application Activity Properties a destra con il nome DocBits-Dev-Demo-Export](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/export_to_m3_from_docbits_5.png)

3. Fare clic sull'**Document Icon** accanto all'Application Node.
   * Fare clic su **Add** e selezionare `Sync.CaptureDocument`.

![Flusso di dati in ION Desk con il nodo applicazione selezionato e il pannello Documents aperto con la voce Sync.CaptureDocument](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/export_to_m3_from_docbits_6.png)

#### Nodo di mappatura

1. Aggiungere un **Mapping Node** a destra dell'Application Node.
   * **Name**: `Capt2process`.
   * **Mapping**: `CaptureDocument_to_ProcessSupplierInvoice`.

![Flusso di dati in ION Desk con il nodo di mappatura selezionato e il pannello Mapping Properties a destra con il nome e la mappatura SyncCaptDoc_SyncSuppInv](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/export_to_m3_from_docbits_7.png)

#### Nodo applicazione

1. Aggiungere un **Application Node** a destra del Mapping Node precedente.
   * **Name**: `M3`.
2. Fare clic su **Add** e selezionare l'**M3 Application** del cliente.

![Flusso di dati in ION Desk con il nodo applicazione M3 selezionato e il pannello Application Activity Properties a destra con la voce M3 BODs](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/export_to_m3_from_docbits_8.png)

3. Fare clic sull'**Document Icon** accanto all'Application Node.
   * Fare clic su **Add** e selezionare `Acknowledge.SupplierInvoice`.

![Flusso di dati in ION Desk con il nodo applicazione M3 selezionato e il pannello Documents aperto con la voce Acknowledge.SupplierInvoice](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/export_to_m3_from_docbits_9.png)

#### Nodo API

1. Aggiungere un **API Node** a destra dell'Application Node.
   * **Name**: `DocBits-Error`.
   * **ION API Connector**: `DocBits_Import`.
   * Se `DocBits_Import` non esiste, consultare il **Passo 1** e il **Passo 2** della documentazione Import from M3 per creare il Connection Point.

![Flusso di dati in ION Desk con il nodo API selezionato e il pannello ION API Activity Properties a destra con l'ION API Connector DocBits Dev Demo-Import](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/export_to_m3_from_docbits_10.png)

#### Salvare e attivare il Flow

* Una volta aggiunti e configurati tutti i nodi, fare clic su **Save**.
* Attivare il flusso per completare la configurazione.

![Flusso di dati in ION Desk con i nodi DocBits_Demo_to_M3, il nodo di mappatura, il nodo M3 e il nodo di errore collegati in fila e il pulsante REMOVE CONNECTION POINTS sopra l'area di lavoro](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/export_to_m3_from_docbits_11%20\(1\).png)

## Passo 4: Configurare l'Export in DocBits

### In locale:

1. Aprire **DocBits**.
2.  Navigare in **Impostazioni > Elaborazione documenti > Esporta**.

    ![Pagina delle impostazioni di DocBits con il gruppo di navigazione Document Processing espanso e le voci Documents, Expiry, Import, Rule Management, OCR Settings, Classification and Extraction, Master Data Lookup, List of Values e Module](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/settings_export.png)
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

    ![Pagina delle impostazioni di DocBits con il gruppo di navigazione Document Processing espanso e le voci Documents, Expiry, Import, Rule Management, OCR Settings, Classification and Extraction, Master Data Lookup, List of Values e Module](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/settings_export.png)
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

    ![Pagina delle impostazioni di DocBits con il gruppo di navigazione Document Processing espanso e le voci Documents, Expiry, Import, Rule Management, OCR Settings, Classification and Extraction, Master Data Lookup, List of Values e Module](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/settings_export.png)
3. Creare una nuova esportazione:
   * **Seleziona**: **Infor IDM + M3 (API)**.
   * **Titolo**: Scegliere un titolo significativo.
   * **Tipo di documento**: Impostare su **Fattura**.
   * **Sotto-organizzazione**: Può essere lasciato vuoto o impostato su una sotto-organizzazione specifica se necessario.
4. **Caricare i file richiesti**:
   * **ION Mapping File**: È possibile trovarlo in **Infor OS → API Gateway → Authorized Apps**. Cercare l'applicazione **DocBits**, aprirla e scaricare le credenziali.
   * **IDM Mapping File**: (Fornire il percorso del file o la posizione rilevante).
   * **M3 toml Mapping File**: (Fornire il percorso del file o la posizione rilevante).
