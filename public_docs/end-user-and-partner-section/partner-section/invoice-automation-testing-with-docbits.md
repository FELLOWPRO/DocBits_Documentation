# Automazione dei Test delle Fatture con DocBits

## Panoramica

Questo documento delinea il piano di test per l'automazione delle fatture utilizzando DocBits con Infor LN o M3. Include dettagli sui casi di test, preparazione ai test, passaggi di esecuzione e processi di supporto.

## Casi di Test

| ID | Caso di Test                                                                              | Descrizione                                                                                                                                                                                                         | Stato      |
| -- | ----------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------- |
| 1  | Fatture di Costo                                                                          | Fatture senza ordine di acquisto vengono elaborate con successo in DocBits ed esportate in LN come “fattura di costo”.                                                                                              | DA TESTARE |
| 2  | Fattura Relativa all'Ordine di Acquisto con Corrispondenza Perfetta                       | Fatture relative all'ordine di acquisto vengono elaborate con successo in DocBits con una corrispondenza perfetta tra fattura e PO, poiché il numero dell'articolo, la quantità e il prezzo unitario corrispondono. | DA TESTARE |
| 3  | Fatture Relative all'Ordine di Acquisto con Quantità Differente                           | Fatture relative all'ordine di acquisto vengono elaborate in DocBits, ma nel modulo di corrispondenza PO abbiamo una discrepanza sulla quantità.                                                                    | DA TESTARE |
| 4  | Fatture Relative all'Ordine di Acquisto con Prezzo Unitario Differente                    | Fatture relative all'ordine di acquisto vengono elaborate in DocBits, ma nel modulo di corrispondenza PO abbiamo una discrepanza sul prezzo unitario.                                                               | DA TESTARE |
| 5  | Fatture Relative all'Ordine di Acquisto con Numero di Articolo Differente o Non Esistente | Fatture relative all'ordine di acquisto vengono elaborate in DocBits, ma nel modulo di corrispondenza PO abbiamo una discrepanza o un numero di articolo non esistente.                                             | DA TESTARE |
| 6  | Fatture Relative all'Ordine di Acquisto con una Discrepanza entro i Limiti                | Fatture relative all'ordine di acquisto vengono elaborate in DocBits, ma nel modulo di corrispondenza PO abbiamo una discrepanza sulla quantità o sul prezzo unitario, ma è entro i limiti.                         | DA TESTARE |
| 7  | Note di Credito                                                                           | Le note di credito vengono elaborate con successo in DocBits ed esportate in LN. Chiarire se gli importi devono essere esportati con un segno positivo o negativo.                                                  | DA TESTARE |

## Piano per il Test con il Cliente

### 1. Impostazione

* **Incontro Iniziale**: Pianificare un incontro di avvio con il cliente per spiegare il processo di test e gli obiettivi.
* **Accesso e Permessi**: Assicurarsi che il cliente abbia tutto l'accesso necessario a DocBits e Infor LN o M3 per scopi di test.

### 2. Preparazione ai Test

* **Formazione**: Fornire una formazione completa al team del cliente su come utilizzare DocBits per l'elaborazione delle fatture.
* **Documentazione**: Condividere documentazione dettagliata sulle procedure di test, inclusi i risultati attesi per ciascun caso di test.

### 3. Esecuzione dei Casi di Test

* **Ambiente di Test**: Impostare un ambiente di test che replichi il sistema di produzione del cliente il più fedelmente possibile.
* **Test Passo-Passo**: Lavorare con il cliente per eseguire ciascun caso di test, assicurandosi che comprendano ogni passaggio:
  * Elaborare le fatture tramite DocBits.
  * Verificare l'output nel modulo di corrispondenza PO.
  * Controllare i risultati dell'esportazione in LN o M3.

### 4. Risoluzione dei Problemi

* **Tracciamento**: Utilizzare un sistema di tracciamento (come Jira o un semplice foglio di calcolo) per registrare eventuali problemi o discrepanze che si verificano durante i test.
* **Supporto**: Fornire supporto immediato per risolvere problemi e chiarire eventuali dubbi.

### 5. Verifica e Feedback

* **Verifica**: Dopo ciascun caso di test, verificare i risultati con il cliente per garantire l'accuratezza.
* **Ciclo di Feedback**: Raccogliere feedback dal cliente sul processo e su eventuali miglioramenti necessari.

### 6. Finalizzazione

* **Documentazione dei Risultati**: Documentare i risultati di ciascun caso di test e fornire un rapporto di sintesi al cliente.
* **Incontro di Revisione**: Condurre un incontro di revisione per discutere i risultati dei test e eventuali ulteriori passaggi richiesti prima di andare in produzione.

### 7. Preparazione al Go Live

* **Aggiornamento della Formazione**: Offrire una sessione di aggiornamento della formazione se necessario.
* **Piano di Supporto**: Sviluppare un piano di supporto per la fase iniziale di go-live per garantire una transizione fluida.
