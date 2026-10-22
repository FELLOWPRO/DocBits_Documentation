# Esporta Codici Fiscali in LN

## **Panoramica:**

\
Questa guida ti guiderà attraverso il processo di configurazione per garantire che i codici fiscali siano correttamente esportati da DocBits a LN.

## **Codici Fiscali Singoli**

### **Passo 1: Configura Elenco di Valori**

1.  Vai su **Impostazioni** -> **Elaborazione Documenti** -> **Elenco di Valori**.

    <figure><img src="../../../.gitbook/assets/site-extra-list-of-values-it.png" alt="Elenco dei valori nell’interfaccia italiana. I nomi degli elenchi dell’organizzazione sono nascosti; nessun elenco è stato creato."><figcaption><p>Elenco dei valori nell’interfaccia italiana. I nomi degli elenchi dell’organizzazione sono nascosti; nessun elenco è stato creato.</p></figcaption></figure>
2.  Clicca su **Nuovo**.

    <figure><img src="../../../.gitbook/assets/TaxCodes_2.png" alt="Pagina Elenco di Valori con gli elenchi esistenti e il pulsante Nuovo"><figcaption>Elenco di Valori con gli elenchi esistenti</figcaption></figure>
3.  Crea un elenco con il nome `Tax_Country` e clicca su **Salva**.

    <figure><img src="../../../.gitbook/assets/TaxCodes_3.png" alt="Finestra Nuovo elenco con il nome Tax_Country" width="563"><figcaption>Creare l'elenco Tax_Country</figcaption></figure>
4.  Crea i seguenti tre elenchi aggiuntivi:

    * `Tax_Code_Full`
    * `Tax_Code_Reduced`
    * `Tax_Code_Free`

    <div><figure><img src="../../../.gitbook/assets/TaxCodes_28.png" alt="Finestra Nuovo elenco con il nome Tax_Code_Full"><figcaption>Creare l'elenco Tax_Code_Full</figcaption></figure> <figure><img src="../../../.gitbook/assets/TaxCodes_29.png" alt="Finestra Nuovo elenco con il nome Tax_Code_Reduced"><figcaption>Creare l'elenco Tax_Code_Reduced</figcaption></figure> <figure><img src="../../../.gitbook/assets/TaxCodes_30.png" alt="Finestra Nuovo elenco con il nome Tax_Code_Free"><figcaption>Creare l'elenco Tax_Code_Free</figcaption></figure></div>
5.  Clicca su uno degli elenchi appena creati per aprirlo. Poi, premi il pulsante **Aggiungi riga** per aggiungere una nuova riga.

    <figure><img src="../../../.gitbook/assets/TaxCode_4.png" alt="Pagina Elenco di Valori con il pulsante Aggiungi riga sotto l'elenco aperto"><figcaption>Aggiungere una riga all'elenco aperto</figcaption></figure>
6.  Inserisci i valori rispettivi desiderati da **LN** e premi **Salva** per salvare le modifiche.

    * Se hai più valori, puoi cliccare su **Aggiungi altri valori** per aggiungerli.

    <div><figure><img src="../../../.gitbook/assets/TaxCodes_5.png" alt="Finestra Crea valori con un codice fiscale LN inserito nel campo Nome"><figcaption>Inserire il codice fiscale LN nel campo Nome</figcaption></figure> <figure><img src="../../../.gitbook/assets/site-extra-list-value-new-it.png" alt="Modulo italiano per creare un valore, con sotto-organizzazione, sinonimi e traduzioni. Nessun codice di imposta è stato inserito o salvato. Inglese indica la lingua di una traduzione, non quella dell’interfaccia."><figcaption><p>Modulo italiano per creare un valore, con sotto-organizzazione, sinonimi e traduzioni. Nessun codice di imposta è stato inserito o salvato. Inglese indica la lingua di una traduzione, non quella dell’interfaccia.</p></figcaption></figure></div>

    * **NOTA:** Puoi trovare i Codici Fiscali in LN sotto: **Common** → **Taxation** → **Master Data** → **Tax Codes** → **Tax Codes by Country**

    <figure><img src="../../../.gitbook/assets/TaxCodes_LN.png" alt="Infor LN, sessione Codici fiscali per paese per l'Austria con le colonne Codice fiscale e Tipo di imposta"><figcaption>LN: Common > Taxation > Master Data > Tax Codes > Tax Codes by Country</figcaption></figure>

### **Passo 2: Aggiungi Campi in DocBits**

1.  Naviga su **Impostazioni** -> **Impostazioni Globali** -> **Tipi di Documento**.

    <figure><img src="../../../.gitbook/assets/site-extra-document-types-it.png" alt="Tipi di documento nell’interfaccia italiana: scegliere Campi nella scheda del tipo interessato. Nessun interruttore è stato modificato; alcune etichette del prodotto restano in inglese."><figcaption><p>Tipi di documento nell’interfaccia italiana: scegliere Campi nella scheda del tipo interessato. Nessun interruttore è stato modificato; alcune etichette del prodotto restano in inglese.</p></figcaption></figure>
2.  Scegli il menu **Campi** corrispondente al Tipo di Documento dove desideri aggiungere i campi.

    <figure><img src="../../../.gitbook/assets/TaxCodes_7.png" alt="Pagina Tipi di documento con il menu Campi sotto ogni tipo di documento"><figcaption>Aprire il menu Campi del tipo di documento</figcaption></figure>
3.  Sotto **IVA & IMPORTI**, crea sei nuovi campi come segue:

    <figure><img src="../../../.gitbook/assets/TaxCodes_8.png" alt="Scheda Campi con il gruppo IVA e importi e il pulsante Crea nuovo"><figcaption>Scheda Campi: gruppo IVA e importi</figcaption></figure>

<table data-header-hidden><thead><tr><th width="306"></th><th width="139"></th><th width="119"></th><th></th></tr></thead><tbody><tr><td><strong>Nome</strong></td><td><strong>Titolo</strong></td><td><strong>Tipo di Campo</strong></td><td><strong>Elenco dei Valori</strong></td></tr><tr><td><code>tax_country</code></td><td>Paese fiscale</td><td>Dropdown</td><td>Tax_Country</td></tr><tr><td><code>tax_country_2</code></td><td>Paese fiscale ridotto</td><td>Dropdown</td><td>Tax_Country</td></tr><tr><td><code>tax_country_3</code></td><td>Paese esente da tasse</td><td>Dropdown</td><td>Tax_Country</td></tr><tr><td><code>tax_code_without_country</code></td><td>Codice Fiscale</td><td>Dropdown</td><td>Tax_Code_Full</td></tr><tr><td><code>tax_code_without_country_2</code></td><td>Codice Fiscale Ridotto</td><td>Dropdown</td><td>Tax_Code_Reduced</td></tr><tr><td><code>tax_code_without_country_3</code></td><td>Codice Fiscale Libero</td><td>Dropdown</td><td>Tax_Code_Free</td></tr></tbody></table>

<div><figure><img src="../../../.gitbook/assets/TaxCodes_10.png" alt="Finestra Dettagli campo documento per tax_country con tipo Dropdown ed elenco Tax_Country"><figcaption>Campo tax_country: Dropdown, elenco Tax_Country</figcaption></figure> <figure><img src="../../../.gitbook/assets/TaxCodes_11.png" alt="Finestra Dettagli campo documento per tax_country_2 con titolo Tax Country Reduced"><figcaption>Campo tax_country_2: Dropdown, elenco Tax_Country</figcaption></figure> <figure><img src="../../../.gitbook/assets/TaxCodes_12.png" alt="Finestra Dettagli campo documento per tax_country_3 con titolo Tax Country Free"><figcaption>Campo tax_country_3: Dropdown, elenco Tax_Country</figcaption></figure></div>

<div><figure><img src="../../../.gitbook/assets/TaxCodes_13.png" alt="Finestra Dettagli campo documento per tax_code_without_country con elenco Tax_Code_Full"><figcaption>Campo tax_code_without_country: Dropdown, elenco Tax_Code_Full</figcaption></figure> <figure><img src="../../../.gitbook/assets/TaxCodes_14.png" alt="Finestra Dettagli campo documento per tax_code_without_country_2 con elenco Tax_Code_Reduced"><figcaption>Campo tax_code_without_country_2: Dropdown, elenco Tax_Code_Reduced</figcaption></figure> <figure><img src="../../../.gitbook/assets/TaxCodes_15.png" alt="Finestra Dettagli campo documento per tax_code_without_country_3 con elenco Tax_Code_Free"><figcaption>Campo tax_code_without_country_3: Dropdown, elenco Tax_Code_Free</figcaption></figure></div>

4.  Dopo aver salvato ogni campo, clicca su **Salva Impostazioni** per applicare le modifiche.

    <figure><img src="../../../.gitbook/assets/TaxCodes_20.png" alt="Scheda Campi con il pulsante Salva impostazioni sopra l'elenco dei campi"><figcaption>Salva impostazioni per applicare i nuovi campi</figcaption></figure>

### **Passo 3: Modifica Layout**

1.  Vai su **Impostazioni** -> **Impostazioni Globali** -> **Tipi di Documento**.

    <figure><img src="../../../.gitbook/assets/site-extra-document-types-it.png" alt="Tipi di documento nell’interfaccia italiana: scegliere Campi nella scheda del tipo interessato. Nessun interruttore è stato modificato; alcune etichette del prodotto restano in inglese."><figcaption><p>Tipi di documento nell’interfaccia italiana: scegliere Campi nella scheda del tipo interessato. Nessun interruttore è stato modificato; alcune etichette del prodotto restano in inglese.</p></figcaption></figure>
2.  Apri il menu **Modifica layout** per il Tipo di Documento che desideri modificare.

    <figure><img src="../../../.gitbook/assets/TaxCodes_19.png" alt="Pagina Tipi di documento con il link Modifica layout sotto ogni tipo di documento"><figcaption>Aprire Modifica layout del tipo di documento</figcaption></figure>
3.  Seleziona l'**Origine Documento** appropriata per la quale desideri applicare i Codici Fiscali

    <figure><img src="../../../.gitbook/assets/TaxCodes_26.png" alt="Layout Builder con il selettore dell'origine documento e la barra degli strumenti del modello"><figcaption>Layout Builder: selezionare l'origine documento</figcaption></figure>
4.  Scorri verso il basso fino alla sezione **Tax Details**.

    <figure><img src="../../../.gitbook/assets/TaxCodes_21.png" alt="Layout Builder con il gruppo Dettagli imposta e i suoi campi nell'albero degli elementi"><figcaption>Scorrere fino al gruppo Dettagli imposta</figcaption></figure>
5. Espandi il menu a discesa **Elementi del modulo**.
6.  Nella sezione **Tax Details**, utilizza lo strumento **Horizontal Separator**. Trascinalo e rilascialo tra le sottosezioni all'interno della sezione fiscale per separarle chiaramente e ridurre la confusione.

    <figure><img src="../../../.gitbook/assets/TaxCodes_22.png" alt="Layout Builder con l'elenco Elementi modulo aperto"><figcaption>Aprire Elementi modulo</figcaption></figure>
7. Espandi il menu a discesa **Campi**.
8.  Cerca **Tax Country** e trascina e rilascia il campo nella sua area rispettiva.

    <figure><img src="../../../.gitbook/assets/TaxCodes_23.png" alt="Layout Builder con il campo Tax Country trascinato nell'area Dettagli imposta"><figcaption>Trascinare Tax Country nell'area Dettagli imposta</figcaption></figure>
9.  Cerca **Tax Code** e trascina e rilascia il campo nella sua area corrispondente.

    <figure><img src="../../../.gitbook/assets/TaxCodes_24.png" alt="Layout Builder con il campo Tax Code inserito sotto Tax Country"><figcaption>Trascinare Tax Code nell'area Dettagli imposta</figcaption></figure>
10. Salva il modello.

    <figure><img src="../../../.gitbook/assets/TaxCodes_25.png" alt="Layout Builder con il modello salvato e i due campi imposta nel gruppo Dettagli imposta"><figcaption>Modello salvato con i due campi imposta</figcaption></figure>

### Passo 4: Verifica che Tutto Funzioni

Dopo aver caricato un nuovo documento in DocBits con le impostazioni di documento corrette selezionate, ora dovresti essere in grado di selezionare i codici fiscali che hai aggiunto agli elenchi nel Passo 1.

<figure><img src="../../../.gitbook/assets/TaxCodes_31.png" alt="Vista di validazione campi di una fattura con gli elenchi Tax Country e Tax Code compilati"><figcaption>I nuovi elenchi nella vista di validazione</figcaption></figure>

## Codice Fiscale Multiplo

### **Passo 1: Configura Elenco di Valori**

1.  Vai su **Impostazioni** -> **Elaborazione Documenti** -> **Elenco di Valori**.

    <figure><img src="../../../.gitbook/assets/site-extra-list-of-values-it.png" alt="Elenco dei valori nell’interfaccia italiana. I nomi degli elenchi dell’organizzazione sono nascosti; nessun elenco è stato creato."><figcaption><p>Elenco dei valori nell’interfaccia italiana. I nomi degli elenchi dell’organizzazione sono nascosti; nessun elenco è stato creato.</p></figcaption></figure>
2.  Clicca su **Nuovo**.

    <figure><img src="../../../.gitbook/assets/TaxCodes_2.png" alt="Pagina Elenco di Valori con gli elenchi esistenti e il pulsante Nuovo"><figcaption>Elenco di Valori con gli elenchi esistenti</figcaption></figure>
3.  Crea un elenco con il nome `Tax_Country` e clicca su **Salva**.

    <figure><img src="../../../.gitbook/assets/TaxCodes_3.png" alt="Finestra Nuovo elenco con il nome Tax_Country" width="563"><figcaption>Creare l'elenco Tax_Country</figcaption></figure>
4.  Crea i seguenti tre elenchi aggiuntivi:

    * `Tax_Code_Full`
    * `Tax_Code_Reduced`
    * `Tax_Code_Free`

    <div><figure><img src="../../../.gitbook/assets/TaxCodes_28.png" alt="Finestra Nuovo elenco con il nome Tax_Code_Full"><figcaption>Creare l'elenco Tax_Code_Full</figcaption></figure> <figure><img src="../../../.gitbook/assets/TaxCodes_29.png" alt="Finestra Nuovo elenco con il nome Tax_Code_Reduced"><figcaption>Creare l'elenco Tax_Code_Reduced</figcaption></figure> <figure><img src="../../../.gitbook/assets/TaxCodes_30.png" alt="Finestra Nuovo elenco con il nome Tax_Code_Free"><figcaption>Creare l'elenco Tax_Code_Free</figcaption></figure></div>
5.  Clicca su uno degli elenchi appena creati per aprirlo. Poi, premi il pulsante **Aggiungi riga** per aggiungere una nuova riga.

    <figure><img src="../../../.gitbook/assets/TaxCode_4.png" alt="Pagina Elenco di Valori con il pulsante Aggiungi riga sotto l'elenco aperto"><figcaption>Aggiungere una riga all'elenco aperto</figcaption></figure>
6.  Inserisci i valori rispettivi desiderati da **LN** e premi **Salva** per salvare le modifiche.

    * Se hai più valori, puoi cliccare su **Aggiungi altri valori** per aggiungerli.

    <div><figure><img src="../../../.gitbook/assets/TaxCodes_5.png" alt="Finestra Crea valori con un codice fiscale LN inserito nel campo Nome"><figcaption>Inserire il codice fiscale LN nel campo Nome</figcaption></figure> <figure><img src="../../../.gitbook/assets/site-extra-list-value-new-it.png" alt="Modulo italiano per creare un valore, con sotto-organizzazione, sinonimi e traduzioni. Nessun codice di imposta è stato inserito o salvato. Inglese indica la lingua di una traduzione, non quella dell’interfaccia."><figcaption><p>Modulo italiano per creare un valore, con sotto-organizzazione, sinonimi e traduzioni. Nessun codice di imposta è stato inserito o salvato. Inglese indica la lingua di una traduzione, non quella dell’interfaccia.</p></figcaption></figure></div>

    * **NOTA:** Puoi trovare i Codici Fiscali in LN sotto: **Common** → **Taxation** → **Master Data** → **Tax Codes** → **Tax Codes by Country**

    <figure><img src="../../../.gitbook/assets/TaxCodes_LN.png" alt="Infor LN, sessione Codici fiscali per paese per l'Austria con le colonne Codice fiscale e Tipo di imposta"><figcaption>LN: Common > Taxation > Master Data > Tax Codes > Tax Codes by Country</figcaption></figure>

### **Passo 2: Aggiungi Campi in DocBits**

1.  Naviga su **Impostazioni** -> **Impostazioni Globali** -> **Tipi di Documento**.

    <figure><img src="../../../.gitbook/assets/site-extra-document-types-it.png" alt="Tipi di documento nell’interfaccia italiana: scegliere Campi nella scheda del tipo interessato. Nessun interruttore è stato modificato; alcune etichette del prodotto restano in inglese."><figcaption><p>Tipi di documento nell’interfaccia italiana: scegliere Campi nella scheda del tipo interessato. Nessun interruttore è stato modificato; alcune etichette del prodotto restano in inglese.</p></figcaption></figure>
2.  Scegli il menu **Campi** corrispondente al Tipo di Documento dove desideri aggiungere i campi.

    <figure><img src="../../../.gitbook/assets/TaxCodes_7.png" alt="Pagina Tipi di documento con il menu Campi sotto ogni tipo di documento"><figcaption>Aprire il menu Campi del tipo di documento</figcaption></figure>
3.  Sotto **IVA & IMPORTI**, crea sei nuovi campi come segue:

    <figure><img src="../../../.gitbook/assets/TaxCodes_8.png" alt="Scheda Campi con il gruppo IVA e importi e il pulsante Crea nuovo"><figcaption>Scheda Campi: gruppo IVA e importi</figcaption></figure>

<table data-header-hidden><thead><tr><th width="306"></th><th width="139"></th><th width="119"></th><th></th></tr></thead><tbody><tr><td><strong>Nome</strong></td><td><strong>Titolo</strong></td><td><strong>Tipo di Campo</strong></td><td><strong>Elenco dei Valori</strong></td></tr><tr><td><code>tax_country</code></td><td>Paese fiscale</td><td>Dropdown</td><td>Tax_Country</td></tr><tr><td><code>tax_country_2</code></td><td>Paese fiscale ridotto</td><td>Dropdown</td><td>Tax_Country</td></tr><tr><td><code>tax_country_3</code></td><td>Paese esente da tasse</td><td>Dropdown</td><td>Tax_Country</td></tr><tr><td><code>tax_code_without_country</code></td><td>Codice Fiscale</td><td>Dropdown</td><td>Tax_Code_Full</td></tr><tr><td><code>tax_code_without_country_2</code></td><td>Codice Fiscale Ridotto</td><td>Dropdown</td><td>Tax_Code_Reduced</td></tr><tr><td><code>tax_code_without_country_3</code></td><td>Codice Fiscale Libero</td><td>Dropdown</td><td>Tax_Code_Free</td></tr></tbody></table>

<div><figure><img src="../../../.gitbook/assets/TaxCodes_10.png" alt="Finestra Dettagli campo documento per tax_country con tipo Dropdown ed elenco Tax_Country"><figcaption>Campo tax_country: Dropdown, elenco Tax_Country</figcaption></figure> <figure><img src="../../../.gitbook/assets/TaxCodes_11.png" alt="Finestra Dettagli campo documento per tax_country_2 con titolo Tax Country Reduced"><figcaption>Campo tax_country_2: Dropdown, elenco Tax_Country</figcaption></figure> <figure><img src="../../../.gitbook/assets/TaxCodes_12.png" alt="Finestra Dettagli campo documento per tax_country_3 con titolo Tax Country Free"><figcaption>Campo tax_country_3: Dropdown, elenco Tax_Country</figcaption></figure></div>

<div><figure><img src="../../../.gitbook/assets/TaxCodes_13.png" alt="Finestra Dettagli campo documento per tax_code_without_country con elenco Tax_Code_Full"><figcaption>Campo tax_code_without_country: Dropdown, elenco Tax_Code_Full</figcaption></figure> <figure><img src="../../../.gitbook/assets/TaxCodes_14.png" alt="Finestra Dettagli campo documento per tax_code_without_country_2 con elenco Tax_Code_Reduced"><figcaption>Campo tax_code_without_country_2: Dropdown, elenco Tax_Code_Reduced</figcaption></figure> <figure><img src="../../../.gitbook/assets/TaxCodes_15.png" alt="Finestra Dettagli campo documento per tax_code_without_country_3 con elenco Tax_Code_Free"><figcaption>Campo tax_code_without_country_3: Dropdown, elenco Tax_Code_Free</figcaption></figure></div>

4.  Dopo aver salvato ogni campo, clicca su **Salva Impostazioni** per applicare le modifiche.

    <figure><img src="../../../.gitbook/assets/TaxCodes_20.png" alt="Scheda Campi con il pulsante Salva impostazioni sopra l'elenco dei campi"><figcaption>Salva impostazioni per applicare i nuovi campi</figcaption></figure>

### **Passo 3: Modifica Layout**

1.  Vai su **Impostazioni** -> **Impostazioni Globali** -> **Tipi di Documento**.

    <figure><img src="../../../.gitbook/assets/site-extra-document-types-it.png" alt="Tipi di documento nell’interfaccia italiana: scegliere Campi nella scheda del tipo interessato. Nessun interruttore è stato modificato; alcune etichette del prodotto restano in inglese."><figcaption><p>Tipi di documento nell’interfaccia italiana: scegliere Campi nella scheda del tipo interessato. Nessun interruttore è stato modificato; alcune etichette del prodotto restano in inglese.</p></figcaption></figure>
2.  Apri il menu **Modifica layout** per il Tipo di Documento che desideri modificare.

    <figure><img src="../../../.gitbook/assets/TaxCodes_19.png" alt="Pagina Tipi di documento con il link Modifica layout sotto ogni tipo di documento"><figcaption>Aprire Modifica layout del tipo di documento</figcaption></figure>
3.  Seleziona l'**Origine Documento** appropriata per la quale desideri applicare i Codici Fiscali

    <figure><img src="../../../.gitbook/assets/TaxCodes_26.png" alt="Layout Builder con il selettore dell'origine documento e la barra degli strumenti del modello"><figcaption>Layout Builder: selezionare l'origine documento</figcaption></figure>
4.  Scorri verso il basso fino alla sezione **Tax Details**.

    <figure><img src="../../../.gitbook/assets/TaxCodes_21.png" alt="Layout Builder con il gruppo Dettagli imposta e i suoi campi nell'albero degli elementi"><figcaption>Scorrere fino al gruppo Dettagli imposta</figcaption></figure>
5. Espandi il menu a discesa **Elementi del modulo**.
6.  Nella sezione Tax Details utilizza lo strumento **Sub Group**. Trascina e rilascia accanto a un campo esistente.

    <figure><img src="../../../.gitbook/assets/TaxCodesMulti_1.png" alt="Layout Builder con lo strumento Sottogruppo nell'elenco Elementi modulo"><figcaption>Selezionare lo strumento Sottogruppo</figcaption></figure>
7.  Per nominare il tuo subgroup, clicca sul subgroup e inserisci il nome desiderato nel campo **Etichetta**.

    <div><figure><img src="../../../.gitbook/assets/TaxCodesMulti_2.png" alt="Layout Builder con un nuovo sottogruppo vuoto accanto a un campo esistente"><figcaption>Rilasciare il sottogruppo accanto a un campo</figcaption></figure> <figure><img src="../../../.gitbook/assets/TaxCodesMulti_3.png" alt="Pannello proprietà con il campo Etichetta del nuovo sottogruppo"><figcaption>Assegnare un nome al sottogruppo nel campo Etichetta</figcaption></figure></div>
8.  Trascina e rilascia i campi che corrispondono a questo gruppo nel campo **Sub Group**.

    <figure><img src="../../../.gitbook/assets/TaxCodeMulti_4.png" alt="Layout Builder con i campi imposta spostati nel nuovo sottogruppo"><figcaption>Spostare i campi imposta nel sottogruppo</figcaption></figure>
9. Espandi il menu a discesa **Campi**.
10. Cerca **Tax** e trascina e rilascia i rispettivi campi, come **Tax Country** e **Tax Code**, nel corrispondente sottogruppo.

    <figure><img src="../../../.gitbook/assets/TaxCodeMulti_5.png" alt="Layout Builder con Tax Country e Tax Code nel sottogruppo"><figcaption>Tax Country e Tax Code nel sottogruppo</figcaption></figure>
11. Ripeti i passaggi 5 fino a 10 2 volte per raggiungere il seguente stato:

    <figure><img src="../../../.gitbook/assets/TaxCodeMulti_6.png" alt="Layout Builder con tre sottogruppi imposta per aliquota ordinaria, ridotta ed esente"><figcaption>Tre sottogruppi: ordinaria, ridotta ed esente</figcaption></figure>
12. Salva il modello.

    <figure><img src="../../../.gitbook/assets/TaxCodeMulti_7.png" alt="Layout Builder con il modello multi codici fiscali salvato"><figcaption>Salvare il modello multi codici fiscali</figcaption></figure>

### Passo 4: Verifica che Tutto Funzioni e le modifiche risultanti

Dopo aver caricato un nuovo documento in DocBits con le impostazioni di documento corrette selezionate, sarai in grado di selezionare i codici fiscali che hai aggiunto nel Passo 1 e aggiungere più codici fiscali configurati nel Passo 3.

* Il documento inizierà con tre sezioni distinte: una per gli importi Fiscali Completi, una per gli importi Fiscali Ridotti e una per gli importi Fiscali Esenti.
* Cliccando il pulsante più all'interno di una sezione verrà creato un duplicato, consentendo più invii alla tariffa fiscale selezionata.

<figure><img src="../../../.gitbook/assets/TaxCodeMulti_8.png" alt="Vista di validazione con tre sezioni imposta separate e i pulsanti aggiungi e rimuovi"><figcaption>Tre sezioni imposta nella vista di validazione</figcaption></figure>

* Le sezioni possono essere eliminate cliccando il pulsante di rimozione.

<figure><img src="../../../.gitbook/assets/TaxCodeMulti_9.png" alt="Vista di validazione con una sezione imposta duplicata con il pulsante più"><figcaption>Aggiungere un'altra sezione con il pulsante più</figcaption></figure>

* Gli Importi Totali saranno calcolati come somma di tutte le sezioni
* La Validazione dell'Importo Totale sarà modificata in base a tutte le sezioni fiscali
* Gli script per le nuove sezioni possono essere applicati solo dopo che i campi sono stati aggiunti alla vista.

### Nota per LN:

In **LN** la posizione USt sarà compilata in base al numero di posizione dal menu a discesa Tax Code/Tax Country. Solo il numero di posizione sarà inviato per l'esportazione.

<figure><img src="../../../.gitbook/assets/TaxCodesLN_2.png" alt="Infor LN, sessione Righe imposta per fattura esterna con la colonna posizione imposta"><figcaption>LN: Tax Lines by External Invoice</figcaption></figure>

<figure><img src="../../../.gitbook/assets/TaxCodesLN_3.png" alt="Infor LN, sessione Righe imposta per fattura esterna con il numero di posizione"><figcaption>LN: il numero di posizione viene esportato come USt Position</figcaption></figure>

#### **Mappatura Esportazione**

Per collegare la Linea Fiscale con la Linea di Costo:

1. Aggiungi `TaxLine` all'elenco **InvoiceCostFields**.
2. Aggiungi la seguente voce, seguendo l'esempio qui sotto:\
   `ICF_TaxLine = TF_position`

<figure><img src="../../../.gitbook/assets/TaxCodeMulti_10.png" alt="File di mappatura export con la voce ICF_TaxLine accanto ai campi costo fattura"><figcaption>Mappatura export: ICF_TaxLine = TF_position</figcaption></figure>
