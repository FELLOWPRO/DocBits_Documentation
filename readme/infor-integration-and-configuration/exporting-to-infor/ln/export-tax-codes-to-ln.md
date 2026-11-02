# Esporta Codici d’imposta in LN

## **Panoramica:**

\
Questa guida ti guiderà attraverso il processo di configurazione per preparare l’esportazione dei codici d’imposta da DocBits a LN e verificarne il risultato.

## **Codici d’imposta Singoli**

### **Passo 1: Configura Elenco di Valori**

1.  Vai su **Impostazioni** -> **Elaborazione Documenti** -> **Elenco di Valori**.

    <figure><img src="../../../.gitbook/assets/site-extra-list-of-values-it.png" alt="Elenco dei valori nell’interfaccia italiana. I nomi degli elenchi dell’organizzazione sono nascosti; nessun elenco è stato creato."><figcaption><p>Elenco dei valori nell’interfaccia italiana. I nomi degli elenchi dell’organizzazione sono nascosti; nessun elenco è stato creato.</p></figcaption></figure>
2.  Clicca su **Nuovo**.

    <figure><img src="../../../.gitbook/assets/TaxCodes_2.png" alt="Pagina List of Values con il pulsante New evidenziato nella barra degli strumenti"><figcaption></figcaption></figure>
3.  Crea un elenco con il nome `Tax_Country` e clicca su **Salva**.

    <figure><img src="../../../.gitbook/assets/TaxCodes_3.png" alt="Finestra di dialogo New List of Values con il nome Tax_Country inserito e il pulsante Save visibile" width="563"><figcaption></figcaption></figure>
4.  Crea i seguenti tre elenchi aggiuntivi:

    * `Tax_Code_Full`
    * `Tax_Code_Reduced`
    * `Tax_Code_Free`

    <div><figure><img src="../../../.gitbook/assets/TaxCodes_28.png" alt="Pagina List of Values con la voce Tax_Code_Full creata nell'elenco"><figcaption></figcaption></figure> <figure><img src="../../../.gitbook/assets/TaxCodes_29.png" alt="Pagina List of Values con la voce Tax_Code_Reduced creata nell'elenco"><figcaption></figcaption></figure> <figure><img src="../../../.gitbook/assets/TaxCodes_30.png" alt="Pagina List of Values con la voce Tax_Code_Free creata nell'elenco"><figcaption></figcaption></figure></div>
5.  Clicca su uno degli elenchi appena creati per aprirlo. Poi, premi il pulsante **Aggiungi riga** per aggiungere una nuova riga.

    <figure><img src="../../../.gitbook/assets/TaxCode_4.png" alt="Pagina List of Values per Tax_Country con il pulsante Add Row visibile nella barra degli strumenti"><figcaption></figcaption></figure>
6.  Inserisci i valori rispettivi desiderati da **LN** e premi **Salva** per salvare le modifiche.

    * Se hai più valori, puoi cliccare su **Aggiungi altri valori** per aggiungerli.

    <div><figure><img src="../../../.gitbook/assets/TaxCodes_5.png" alt="Elenco dei valori di Tax_Country con una nuova voce di riga e il pulsante Save"><figcaption></figcaption></figure> <figure><img src="../../../.gitbook/assets/site-extra-list-value-new-it.png" alt="Modulo italiano per creare un valore, con sotto-organizzazione, sinonimi e traduzioni. Nessun codice di imposta è stato inserito o salvato. Inglese indica la lingua di una traduzione, non quella dell’interfaccia."><figcaption><p>Modulo italiano per creare un valore, con sotto-organizzazione, sinonimi e traduzioni. Nessun codice di imposta è stato inserito o salvato. Inglese indica la lingua di una traduzione, non quella dell’interfaccia.</p></figcaption></figure></div>

    * **NOTA:** Puoi trovare i Codici d’imposta in LN sotto: **Common** → **Taxation** → **Master Data** → **Tax Codes** → **Tax Codes by Country**

    <figure><img src="../../../.gitbook/assets/TaxCodes_LN.png" alt="Schermata LN Tax Codes by Country in Common, Taxation, Master Data che mostra la panoramica dei codici IVA"><figcaption></figcaption></figure>

### **Passo 2: Aggiungi Campi in DocBits**

1.  Naviga su **Impostazioni** -> **Impostazioni Globali** -> **Tipi di Documento**.

    <figure><img src="../../../.gitbook/assets/native-document-types-it-20261023.png" alt="Tipi di documento e accesso alle impostazioni del tipo interessato. Contrarre è un’etichetta errata del tipo Contratto. La schermata documenta il punto di accesso, non i campi d’imposta o un layout già configurato. Nessun controllo è stato modificato."><figcaption><p>Tipi di documento e accesso alle impostazioni del tipo interessato. Contrarre è un’etichetta errata del tipo Contratto. La schermata documenta il punto di accesso, non i campi d’imposta o un layout già configurato. Nessun controllo è stato modificato.</p></figcaption></figure>
2.  Scegli il menu **Campi** corrispondente al Tipo di Documento dove desideri aggiungere i campi.

    <figure><img src="../../../.gitbook/assets/TaxCodes_7.png" alt="Pagina Document Types con l'opzione Fields aperta per un tipo di documento nel menu"><figcaption></figcaption></figure>
3.  Sotto **IVA & IMPORTI**, crea sei nuovi campi come segue:

    <figure><img src="../../../.gitbook/assets/TaxCodes_8.png" alt="Pagina delle impostazioni dei campi per un tipo di documento con la sezione VAT and Amounts espansa"><figcaption></figcaption></figure>

<table data-header-hidden><thead><tr><th width="306"></th><th width="139"></th><th width="119"></th><th></th></tr></thead><tbody><tr><td><strong>Nome</strong></td><td><strong>Titolo</strong></td><td><strong>Tipo di Campo</strong></td><td><strong>Elenco dei Valori</strong></td></tr><tr><td><code>tax_country</code></td><td>Paese fiscale</td><td>Dropdown</td><td>Tax_Country</td></tr><tr><td><code>tax_country_2</code></td><td>Paese fiscale ridotto</td><td>Dropdown</td><td>Tax_Country</td></tr><tr><td><code>tax_country_3</code></td><td>Paese esente da tasse</td><td>Dropdown</td><td>Tax_Country</td></tr><tr><td><code>tax_code_without_country</code></td><td>Codice d’imposta</td><td>Dropdown</td><td>Tax_Code_Full</td></tr><tr><td><code>tax_code_without_country_2</code></td><td>Codice d’imposta ridotta</td><td>Dropdown</td><td>Tax_Code_Reduced</td></tr><tr><td><code>tax_code_without_country_3</code></td><td>Codice d’imposta esente</td><td>Dropdown</td><td>Tax_Code_Free</td></tr></tbody></table>

<div><figure><img src="../../../.gitbook/assets/TaxCodes_10.png" alt="Pagina delle impostazioni dei campi con il nuovo campo a discesa Tax Country e l'elenco dei valori Tax_Country"><figcaption></figcaption></figure> <figure><img src="../../../.gitbook/assets/TaxCodes_11.png" alt="Pagina Fields settings con il nuovo campo a discesa Tax Country Reduced e la List of Values Tax_Country"><figcaption></figcaption></figure> <figure><img src="../../../.gitbook/assets/TaxCodes_12.png" alt="Pagina delle impostazioni dei campi con il nuovo campo a discesa Tax Country Free e la List of Values Tax_Country"><figcaption></figcaption></figure></div>

<div><figure><img src="../../../.gitbook/assets/TaxCodes_13.png" alt="Pagina Fields settings con il nuovo campo a discesa Tax Code e la List of Values Tax_Code_Full"><figcaption></figcaption></figure> <figure><img src="../../../.gitbook/assets/TaxCodes_14.png" alt="Pagina delle impostazioni Fields con un nuovo campo a discesa Tax Code Reduced e la List of Values Tax_Code_Reduced"><figcaption></figcaption></figure> <figure><img src="../../../.gitbook/assets/TaxCodes_15.png" alt="Pagina Fields settings con un nuovo campo a discesa Tax Code Free e la List of Values Tax_Code_Free"><figcaption></figcaption></figure></div>

4.  Dopo aver salvato ogni campo, clicca su **Salva Impostazioni** per applicare le modifiche.

    <figure><img src="../../../.gitbook/assets/TaxCodes_20.png" alt="Pagina Fields settings con i campi fiscali appena creati e il pulsante Save Settings evidenziato"><figcaption></figcaption></figure>

### **Passo 3: Modifica Layout**

1.  Vai su **Impostazioni** -> **Impostazioni Globali** -> **Tipi di Documento**.

    <figure><img src="../../../.gitbook/assets/native-document-types-it-20261023.png" alt="Tipi di documento e accesso alle impostazioni del tipo interessato. Contrarre è un’etichetta errata del tipo Contratto. La schermata documenta il punto di accesso, non i campi d’imposta o un layout già configurato. Nessun controllo è stato modificato."><figcaption><p>Tipi di documento e accesso alle impostazioni del tipo interessato. Contrarre è un’etichetta errata del tipo Contratto. La schermata documenta il punto di accesso, non i campi d’imposta o un layout già configurato. Nessun controllo è stato modificato.</p></figcaption></figure>
2.  Apri il menu **Modifica layout** per il Tipo di Documento che desideri modificare.

    <figure><img src="../../../.gitbook/assets/TaxCodes_19.png" alt="Pagina Document Types con l'opzione Edit Layout aperta per un tipo di documento nel menu"><figcaption></figcaption></figure>
3.  Seleziona l'**Origine Documento** appropriata per la quale desideri applicare i Codici d’imposta

    <figure><img src="../../../.gitbook/assets/TaxCodes_26.png" alt="Editor di layout con il menu a discesa Document Origin aperto per selezionare l'origine appropriata"><figcaption></figcaption></figure>
4.  Scorri verso il basso fino alla sezione **Tax Details**.

    <figure><img src="../../../.gitbook/assets/TaxCodes_21.png" alt="Editor del layout scorriuto verso il basso fino alla sezione Tax Details del modello del documento"><figcaption></figcaption></figure>
5. Espandi il menu a discesa **Elementi del modulo**.
6.  Nella sezione **Tax Details**, utilizza lo strumento **Horizontal Separator**. Trascinalo e rilascialo tra le sottosezioni all'interno della sezione fiscale per separarle chiaramente e ridurre la confusione.

    <figure><img src="../../../.gitbook/assets/TaxCodes_22.png" alt="Editor di layout con il menu a discesa Form Elements espanso e lo strumento Horizontal Separator evidenziato"><figcaption></figcaption></figure>
7. Espandi il menu a discesa **Campi**.
8.  Cerca **Tax Country** e trascina e rilascia il campo nella sua area rispettiva.

    <figure><img src="../../../.gitbook/assets/TaxCodes_23.png" alt="Editor di layout con il menu a discesa Form Fields espanso e il campo Tax Country in fase di ricerca"><figcaption></figcaption></figure>
9.  Cerca **Tax Code** e trascina e rilascia il campo nella sua area corrispondente.

    <figure><img src="../../../.gitbook/assets/TaxCodes_24.png" alt="Editor del layout con il menu a discesa Form Fields espanso e la ricerca del campo Tax Code in corso"><figcaption></figcaption></figure>
10. Salva il modello.

    <figure><img src="../../../.gitbook/assets/TaxCodes_25.png" alt="Editor del layout con il pulsante Save evidenziato dopo il posizionamento dei campi fiscali"><figcaption></figcaption></figure>

### Passo 4: Verifica che Tutto Funzioni

Dopo aver caricato un nuovo documento in DocBits con le impostazioni di documento corrette selezionate, ora dovresti essere in grado di selezionare i codici d’imposta che hai aggiunto agli elenchi nel Passo 1.

<figure><img src="../../../.gitbook/assets/TaxCodes_31.png" alt="Schermata di validazione di un documento caricato con i valori del menu a discesa del codice IVA aperti"><figcaption></figcaption></figure>

## Codice d’imposta Multiplo

### **Passo 1: Configura Elenco di Valori**

1.  Vai su **Impostazioni** -> **Elaborazione Documenti** -> **Elenco di Valori**.

    <figure><img src="../../../.gitbook/assets/site-extra-list-of-values-it.png" alt="Elenco dei valori nell’interfaccia italiana. I nomi degli elenchi dell’organizzazione sono nascosti; nessun elenco è stato creato."><figcaption><p>Elenco dei valori nell’interfaccia italiana. I nomi degli elenchi dell’organizzazione sono nascosti; nessun elenco è stato creato.</p></figcaption></figure>
2.  Clicca su **Nuovo**.

    <figure><img src="../../../.gitbook/assets/TaxCodes_2.png" alt="Pagina List of Values con il pulsante New evidenziato nella barra degli strumenti"><figcaption></figcaption></figure>
3.  Crea un elenco con il nome `Tax_Country` e clicca su **Salva**.

    <figure><img src="../../../.gitbook/assets/TaxCodes_3.png" alt="Finestra di dialogo New List of Values con il nome Tax_Country inserito e il pulsante Save visibile" width="563"><figcaption></figcaption></figure>
4.  Crea i seguenti tre elenchi aggiuntivi:

    * `Tax_Code_Full`
    * `Tax_Code_Reduced`
    * `Tax_Code_Free`

    <div><figure><img src="../../../.gitbook/assets/TaxCodes_28.png" alt="Pagina List of Values con la voce Tax_Code_Full creata nell'elenco"><figcaption></figcaption></figure> <figure><img src="../../../.gitbook/assets/TaxCodes_29.png" alt="Pagina List of Values con la voce Tax_Code_Reduced creata nell'elenco"><figcaption></figcaption></figure> <figure><img src="../../../.gitbook/assets/TaxCodes_30.png" alt="Pagina List of Values con la voce Tax_Code_Free creata nell'elenco"><figcaption></figcaption></figure></div>
5.  Clicca su uno degli elenchi appena creati per aprirlo. Poi, premi il pulsante **Aggiungi riga** per aggiungere una nuova riga.

    <figure><img src="../../../.gitbook/assets/TaxCode_4.png" alt="Pagina List of Values per Tax_Country con il pulsante Add Row visibile nella barra degli strumenti"><figcaption></figcaption></figure>
6.  Inserisci i valori rispettivi desiderati da **LN** e premi **Salva** per salvare le modifiche.

    * Se hai più valori, puoi cliccare su **Aggiungi altri valori** per aggiungerli.

    <div><figure><img src="../../../.gitbook/assets/TaxCodes_5.png" alt="Elenco dei valori di Tax_Country con una nuova voce di riga e il pulsante Save"><figcaption></figcaption></figure> <figure><img src="../../../.gitbook/assets/site-extra-list-value-new-it.png" alt="Modulo italiano per creare un valore, con sotto-organizzazione, sinonimi e traduzioni. Nessun codice di imposta è stato inserito o salvato. Inglese indica la lingua di una traduzione, non quella dell’interfaccia."><figcaption><p>Modulo italiano per creare un valore, con sotto-organizzazione, sinonimi e traduzioni. Nessun codice di imposta è stato inserito o salvato. Inglese indica la lingua di una traduzione, non quella dell’interfaccia.</p></figcaption></figure></div>

    * **NOTA:** Puoi trovare i Codici d’imposta in LN sotto: **Common** → **Taxation** → **Master Data** → **Tax Codes** → **Tax Codes by Country**

    <figure><img src="../../../.gitbook/assets/TaxCodes_LN.png" alt="Schermata LN Tax Codes by Country in Common, Taxation, Master Data che mostra la panoramica dei codici IVA"><figcaption></figcaption></figure>

### **Passo 2: Aggiungi Campi in DocBits**

1.  Naviga su **Impostazioni** -> **Impostazioni Globali** -> **Tipi di Documento**.

    <figure><img src="../../../.gitbook/assets/native-document-types-it-20261023.png" alt="Tipi di documento e accesso alle impostazioni del tipo interessato. Contrarre è un’etichetta errata del tipo Contratto. La schermata documenta il punto di accesso, non i campi d’imposta o un layout già configurato. Nessun controllo è stato modificato."><figcaption><p>Tipi di documento e accesso alle impostazioni del tipo interessato. Contrarre è un’etichetta errata del tipo Contratto. La schermata documenta il punto di accesso, non i campi d’imposta o un layout già configurato. Nessun controllo è stato modificato.</p></figcaption></figure>
2.  Scegli il menu **Campi** corrispondente al Tipo di Documento dove desideri aggiungere i campi.

    <figure><img src="../../../.gitbook/assets/TaxCodes_7.png" alt="Pagina Document Types con l'opzione Fields aperta per un tipo di documento nel menu"><figcaption></figcaption></figure>
3.  Sotto **IVA & IMPORTI**, crea sei nuovi campi come segue:

    <figure><img src="../../../.gitbook/assets/TaxCodes_8.png" alt="Pagina delle impostazioni dei campi per un tipo di documento con la sezione VAT and Amounts espansa"><figcaption></figcaption></figure>

<table data-header-hidden><thead><tr><th width="306"></th><th width="139"></th><th width="119"></th><th></th></tr></thead><tbody><tr><td><strong>Nome</strong></td><td><strong>Titolo</strong></td><td><strong>Tipo di Campo</strong></td><td><strong>Elenco dei Valori</strong></td></tr><tr><td><code>tax_country</code></td><td>Paese fiscale</td><td>Dropdown</td><td>Tax_Country</td></tr><tr><td><code>tax_country_2</code></td><td>Paese fiscale ridotto</td><td>Dropdown</td><td>Tax_Country</td></tr><tr><td><code>tax_country_3</code></td><td>Paese esente da tasse</td><td>Dropdown</td><td>Tax_Country</td></tr><tr><td><code>tax_code_without_country</code></td><td>Codice d’imposta</td><td>Dropdown</td><td>Tax_Code_Full</td></tr><tr><td><code>tax_code_without_country_2</code></td><td>Codice d’imposta ridotta</td><td>Dropdown</td><td>Tax_Code_Reduced</td></tr><tr><td><code>tax_code_without_country_3</code></td><td>Codice d’imposta esente</td><td>Dropdown</td><td>Tax_Code_Free</td></tr></tbody></table>

<div><figure><img src="../../../.gitbook/assets/TaxCodes_10.png" alt="Pagina delle impostazioni dei campi con il nuovo campo a discesa Tax Country e l'elenco dei valori Tax_Country"><figcaption></figcaption></figure> <figure><img src="../../../.gitbook/assets/TaxCodes_11.png" alt="Pagina Fields settings con il nuovo campo a discesa Tax Country Reduced e la List of Values Tax_Country"><figcaption></figcaption></figure> <figure><img src="../../../.gitbook/assets/TaxCodes_12.png" alt="Pagina delle impostazioni dei campi con il nuovo campo a discesa Tax Country Free e la List of Values Tax_Country"><figcaption></figcaption></figure></div>

<div><figure><img src="../../../.gitbook/assets/TaxCodes_13.png" alt="Pagina Fields settings con il nuovo campo a discesa Tax Code e la List of Values Tax_Code_Full"><figcaption></figcaption></figure> <figure><img src="../../../.gitbook/assets/TaxCodes_14.png" alt="Pagina delle impostazioni Fields con un nuovo campo a discesa Tax Code Reduced e la List of Values Tax_Code_Reduced"><figcaption></figcaption></figure> <figure><img src="../../../.gitbook/assets/TaxCodes_15.png" alt="Pagina Fields settings con un nuovo campo a discesa Tax Code Free e la List of Values Tax_Code_Free"><figcaption></figcaption></figure></div>

4.  Dopo aver salvato ogni campo, clicca su **Salva Impostazioni** per applicare le modifiche.

    <figure><img src="../../../.gitbook/assets/TaxCodes_20.png" alt="Pagina Fields settings con i campi fiscali appena creati e il pulsante Save Settings evidenziato"><figcaption></figcaption></figure>

### **Passo 3: Modifica Layout**

1.  Vai su **Impostazioni** -> **Impostazioni Globali** -> **Tipi di Documento**.

    <figure><img src="../../../.gitbook/assets/native-document-types-it-20261023.png" alt="Tipi di documento e accesso alle impostazioni del tipo interessato. Contrarre è un’etichetta errata del tipo Contratto. La schermata documenta il punto di accesso, non i campi d’imposta o un layout già configurato. Nessun controllo è stato modificato."><figcaption><p>Tipi di documento e accesso alle impostazioni del tipo interessato. Contrarre è un’etichetta errata del tipo Contratto. La schermata documenta il punto di accesso, non i campi d’imposta o un layout già configurato. Nessun controllo è stato modificato.</p></figcaption></figure>
2.  Apri il menu **Modifica layout** per il Tipo di Documento che desideri modificare.

    <figure><img src="../../../.gitbook/assets/TaxCodes_19.png" alt="Pagina Document Types con l'opzione Edit Layout aperta per un tipo di documento nel menu"><figcaption></figcaption></figure>
3.  Seleziona l'**Origine Documento** appropriata per la quale desideri applicare i Codici d’imposta

    <figure><img src="../../../.gitbook/assets/TaxCodes_26.png" alt="Editor di layout con il menu a discesa Document Origin aperto per selezionare l'origine appropriata"><figcaption></figcaption></figure>
4.  Scorri verso il basso fino alla sezione **Tax Details**.

    <figure><img src="../../../.gitbook/assets/TaxCodes_21.png" alt="Editor del layout scorriuto verso il basso fino alla sezione Tax Details del modello del documento"><figcaption></figcaption></figure>
5. Espandi il menu a discesa **Elementi del modulo**.
6.  Nella sezione Tax Details utilizza lo strumento **Sub Group**. Trascina e rilascia accanto a un campo esistente.

    <figure><img src="../../../.gitbook/assets/TaxCodesMulti_1.png" alt="Editor del layout con il menu a discesa Form Elements espanso e lo strumento Sub Group evidenziato"><figcaption></figcaption></figure>
7.  Per nominare il tuo subgroup, clicca sul subgroup e inserisci il nome desiderato nel campo **Etichetta**.

    <div><figure><img src="../../../.gitbook/assets/TaxCodesMulti_2.png" alt="Editor del layout con un elemento Sub Group appena aggiunto e selezionato nella sezione Tax Details"><figcaption></figcaption></figure> <figure><img src="../../../.gitbook/assets/TaxCodesMulti_3.png" alt="Editor del layout con il campo Label della Sub Group selezionata aperto per l'assegnazione del nome"><figcaption></figcaption></figure></div>
8.  Trascina e rilascia i campi che corrispondono a questo gruppo nel campo **Sub Group**.

    <figure><img src="../../../.gitbook/assets/TaxCodeMulti_4.png" alt="Editor del layout con un campo trascinato nel nuovo Sub Group nella sezione Tax Details"><figcaption></figcaption></figure>
9. Espandi il menu a discesa **Campi**.
10. Cerca **Tax** e trascina e rilascia i rispettivi campi, come **Tax Country** e **Tax Code**, nel corrispondente sottogruppo.

    <figure><img src="../../../.gitbook/assets/TaxCodeMulti_5.png" alt="Editor del layout con il menu a discesa Fields espanso e il campo Tax Country in fase di ricerca"><figcaption></figcaption></figure>
11. Ripeti i passaggi 5 fino a 10 2 volte per raggiungere il seguente stato:

    <figure><img src="../../../.gitbook/assets/TaxCodeMulti_6.png" alt="Editor del layout con il sottogruppo fiscale posizionato nella sezione Tax Details dopo aver ripetuto i passaggi"><figcaption></figcaption></figure>
12. Salva il modello.

    <figure><img src="../../../.gitbook/assets/TaxCodeMulti_7.png" alt="Editor del layout con il pulsante Save evidenziato dopo aver disposto i sottogruppi fiscali"><figcaption></figcaption></figure>

### Passo 4: Verifica che Tutto Funzioni e le modifiche risultanti

Dopo aver caricato un nuovo documento in DocBits con le impostazioni di documento corrette selezionate, sarai in grado di selezionare i codici d’imposta che hai aggiunto nel Passo 1 e aggiungere più codici d’imposta configurati nel Passo 3.

* Il documento inizierà con tre sezioni distinte: una per gli importi Fiscali Completi, una per gli importi Fiscali Ridotti e una per gli importi Fiscali Esenti.
* Cliccando il pulsante più all'interno di una sezione verrà creato un duplicato, consentendo più invii alla tariffa fiscale selezionata.

<figure><img src="../../../.gitbook/assets/TaxCodeMulti_8.png" alt="Schermata di validazione di un documento caricato che mostra le sezioni fiscali con il pulsante più"><figcaption></figcaption></figure>

* Le sezioni possono essere eliminate cliccando il pulsante di rimozione.

<figure><img src="../../../.gitbook/assets/TaxCodeMulti_9.png" alt="Schermata di validazione di un documento caricato con una sezione fiscale e il pulsante di rimozione evidenziato"><figcaption></figcaption></figure>

* Gli Importi Totali saranno calcolati come somma di tutte le sezioni
* La Validazione dell'Importo Totale sarà modificata in base a tutte le sezioni fiscali
* Gli script per le nuove sezioni possono essere applicati solo dopo che i campi sono stati aggiunti alla vista.

### Nota per LN:

In **LN** la posizione USt sarà compilata in base al numero di posizione dal menu a discesa Tax Code/Tax Country. Solo il numero di posizione sarà inviato per l'esportazione.

<figure><img src="../../../.gitbook/assets/TaxCodesLN_2.png" alt="Schermata LN che mostra il campo USt Position compilato in base al numero di posizione del codice fiscale"><figcaption></figcaption></figure>

<figure><img src="../../../.gitbook/assets/TaxCodesLN_3.png" alt="Schermata LN che mostra la fattura esportata con il valore USt Position compilato"><figcaption></figcaption></figure>

#### **Mappatura Esportazione**

Per collegare la Linea Fiscale con la Linea di Costo:

1. Aggiungi `TaxLine` all'elenco **InvoiceCostFields**.
2. Aggiungi la seguente voce, seguendo l'esempio qui sotto:\
   `ICF_TaxLine = TF_position`

<figure><img src="../../../.gitbook/assets/TaxCodeMulti_10.png" alt="List of Values di InvoiceCostFields con la voce TaxLine e il mapping ICF_TaxLine"><figcaption></figcaption></figure>

Le immagini native aggiornate mostrano soltanto i punti di accesso e i moduli vuoti. Le illustrazioni storiche dei dettagli vanno confrontate con la versione in uso; questa revisione non ha configurato campi d’imposta, modificato layout o eseguito un’esportazione LN.
