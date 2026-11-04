# Gestore delle Regole

\


Questo documento fornisce una spiegazione approfondita delle regole di risoluzione dei conflitti utilizzate nel sistema di fatturazione DocBits. Queste regole sono progettate per gestire automaticamente le discrepanze tra i dettagli della fattura e i dati dell'ordine di acquisto (PO), garantendo una riconciliazione finanziaria accurata. Il sistema applica queste regole per elaborare le righe delle fatture, le spese e le tasse, e genera aggiustamenti o note appropriate quando necessario.

## Struttura delle Regole

### &#x20;1. Metadati

• versione: Identifica la versione del file di mapping.

• revisione: Numero di revisione per il tracciamento delle modifiche.

• autore: Indica il creatore del file di mapping.

• descrizione: Una breve descrizione dello scopo del file.

• created\_at & updated\_at: Timestamp per quando il file è stato creato e aggiornato l'ultima volta.

### &#x20;2. Configurazione dell'Esportazione

La sezione di configurazione dell'esportazione definisce il mapping tra i campi dati nel sistema e i campi corrispondenti nei file di esportazione.

• Intestazione: Definisce i campi di intestazione per i dati della fattura esportata.

• Righe Fiscali: Specifica i campi per gli articoli delle righe fiscali nell'esportazione.

• Spese di Intestazione Ordine: Mappa i campi relativi a spese aggiuntive a livello di intestazione dell'ordine.

• Righe di Ricevuta: Mappa i campi per singoli articoli in una ricevuta.

• Spese di Riga Ordine: Definisce i campi per le spese relative a righe specifiche dell'ordine.

• Righe di Costo: Specifica i campi per le righe di allocazione dei costi.

• Nota di Debito & Nota di Credito: Definisce i campi per generare note di debito e di credito in caso di discrepanze.

### 3. Regole di Risoluzione dei Conflitti

Queste regole gestiscono le discrepanze tra i dati della fattura e i dati corrispondenti del PO. Ogni regola è composta da diversi componenti:

• Nome: Il nome descrittivo della regola, che indica il tipo di discrepanza che affronta.

• Sezione: Indica quale parte della fattura (ad es., receipt\_lines, line\_charges) la regola si applica.

• Attivo: Valore booleano (true o false) che indica se la regola è attualmente attiva.

• Criteri di Corrispondenza: Condizioni che attivano la regola in base ai confronti tra i dati effettivi della fattura e i dati attesi del PO.

• Azioni: Definisce cosa dovrebbe fare il sistema quando la regola viene attivata, inclusi aggiustamenti dei valori, applicazione di spese o generazione di note di credito/debito.

## Elementi Comuni nelle Regole

### Operatori di Confronto

Questi operatori definiscono come i valori effettivi della fattura vengono confrontati con i valori attesi del PO:

• uguale

• maggiore di

• maggiore o uguale a

• minore di

• minore o uguale a

• entro tolleranza

• fuori tolleranza

\


### Stato di Approvazione

Indica se una discrepanza è approvata o meno:

• approvato

• rifiutato

• qualsiasi

\


### Tipi di Azione

Definisce azioni specifiche da intraprendere quando viene rilevata una discrepanza:

\
• riga di ricevuta

• riga di costo

• spesa di intestazione

• spesa di riga

• riga fiscale

• riga di ricevuta nota di debito

• riga di costo nota di debito

• spesa di intestazione nota di debito

• spesa di riga nota di debito

• riga di ricevuta nota di credito

• riga di costo nota di credito

• spesa di intestazione nota di credito

• spesa di riga nota di credito

• riga fiscale nota di credito

\


### Esempi di Regole

#### [Caso 1, 2, 3: Quantità e Prezzo Unitario Entro Tolleranza](transactionconfig-pro-template/case-1-2-3-quantity-and-unit-price-within-tolerance.md)

\
• Scopo: Gestisce scenari in cui sia la quantità che il prezzo unitario sulla fattura sono entro i limiti di tolleranza accettati rispetto al PO.

• Azione: Il sistema accetta i valori della fattura e calcola l'importo totale.



#### [Caso 4, 5: Quantità Entro Tolleranza, Prezzo Unitario Fuori Tolleranza (Approvato)](./#case-4-5-quantity-within-tolerance-unit-price-outside-tolerance-approved)

• Scopo: Si applica quando la quantità è entro tolleranza ma il prezzo unitario è fuori tolleranza ed è stato approvato.

• Azione: Il sistema aggiusta il prezzo unitario per corrispondere al PO e applica eventuali spese di riga necessarie.

\


#### [Caso 6: Quantità Entro Tolleranza, Prezzo Unitario Fuori Tolleranza Negativa (Rifiutato)](transactionconfig-pro-template/case-6-quantity-within-tolerance-unit-price-outside-negative-tolerance-rejected.md)&#x20;

• Scopo: Si occupa di casi in cui il prezzo unitario è inferiore a quanto previsto e fuori dal range di tolleranza, portando al rifiuto.

• Azione: Il sistema aggiusta il prezzo unitario per corrispondere al PO, genera una nota di credito per la differenza e applica le spese di intestazione secondo necessità.



### Gestione delle Spese e delle Tasse

### Spesa per Tolleranza per Unità

• Le regole sotto questa categoria gestiscono le discrepanze nelle spese per unità, con azioni specifiche basate sul fatto che la spesa sia entro o fuori tolleranza e se sia approvata o rifiutata.

### Aggiustamenti delle Righe Fiscali

• Queste regole gestiscono le discrepanze fiscali aggiustando le righe fiscali o generando note di credito o debito corrispondenti in base alle differenze tra i dati fiscali della fattura e del PO.

### Enums e Opzioni

• Enums: Elenchi predefiniti di valori che garantiscono coerenza tra le regole (ad es., operatori di confronto, tipi di approvazione).

• Opzioni: Scelte predefinite per gestire quantità o prezzi unitari, offrendo flessibilità nelle definizioni delle regole.

## Spiegazione degli Screenshot

### Screenshot 1: Interfaccia di Gestione delle Regole

<figure><img src="../../../../.gitbook/assets/docbits_rule_manager_interface.png" alt="Docbits Rule Manager Interface"><figcaption></figcaption></figure>

Questo screenshot mostra l'interfaccia di Gestione delle Regole dove gli amministratori possono visualizzare e gestire tutte le regole di risoluzione dei conflitti. Gli elementi chiave includono:

• Pulsante Aggiungi Regola: Consente di aggiungere nuove regole.

• Elenco delle Regole: Mostra tutte le regole attive con dettagli come nome, sezione e stato attivo.

• Menu a Discesa Sezione: Filtra le regole in base alla sezione a cui si applicano (ad es., Righe di Ricevuta, Spese di Riga).

### Screenshot 2: Modifica Dettagliata della Regola

<figure><img src="../../../../.gitbook/assets/docbits_rule_editing_detail.png" alt="Docbits Rule Editing Detail"><figcaption></figcaption></figure>

Questo screenshot illustra la vista dettagliata di una specifica regola in fase di modifica. Gli elementi chiave includono:

• Sezione Criteri: Definisce le condizioni sotto le quali la regola viene attivata. Ad esempio, i criteri potrebbero specificare che se la quantità e il prezzo unitario differiscono dal PO ma sono entro tolleranza, la regola dovrebbe essere applicata.

• Sezione Azioni: Specifica quali azioni dovrebbero essere intraprese quando i criteri sono soddisfatti. Questo può includere l'aggiustamento delle righe della fattura, la generazione di note di credito o debito, o l'applicazione di spese aggiuntive.

• Tipo di Documento ed Elementi di Costo: Consente all'amministratore di mappare azioni specifiche a tipi di documento ed elementi di costo, fornendo flessibilità nella gestione di diversi scenari.