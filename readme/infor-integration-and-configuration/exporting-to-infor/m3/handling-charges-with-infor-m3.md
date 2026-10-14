# Gestione dei costi accessori con Infor M3

## Panoramica

Questo documento fornisce informazioni dettagliate su come DocBits si integra con Infor M3 per gestire i costi accessori (charges) associati a fatture e ordini di acquisto (PO). Include scenari per i costi esterni e le relative soluzioni previste.

## Scenari di gestione dei costi accessori

| ID scenario | Descrizione                                                                                 | Caso aziendale                                                                                                                                | Soluzione prevista                                                                                                                                                                                                                                  |
| ----------- | ------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| 1           | Costi esterni non presenti nel PO ma presenti in fattura (accettati)                        | I costi esterni compaiono in fattura ma non sono elencati nel PO. Questi costi sono accettati.                                                | I costi verranno registrati secondo la regola contabile PP20-228, in base all'elemento di costo inviato da DocBits.                                                                                                                                 |
| 2           | Costi esterni non presenti nel PO ma presenti in fattura (non accettati)                    | I costi esterni compaiono in fattura ma non sono elencati nel PO. Questi costi non sono accettati né approvati.                               | Il valore totale della fattura viene registrato con un costo di testata per i costi non approvati. Inoltre, per tali costi viene creata una nota di debito.                                                                                          |
| 3           | Costi esterni in fattura superiori o inferiori al PO (entro la tolleranza)                  | I costi esterni in fattura sono superiori o inferiori a quelli del PO ma rientrano nella tolleranza accettata.                                | I costi aggiuntivi vengono registrati secondo la regola contabile PP20-228, in base all'elemento di costo inviato da DocBits.                                                                                                                       |
| 4           | Costi esterni in fattura superiori al PO (oltre la tolleranza, non approvati)               | I costi esterni in fattura sono superiori a quelli del PO e oltre la tolleranza accettata, e non sono approvati.                              | La fattura viene registrata con l'importo totale della fattura. Un ulteriore costo non approvato viene aggiunto come costo di testata e per questo costo aggiuntivo viene creata una nota di debito.                                                |
| 5           | Costi esterni in fattura superiori al PO (oltre la tolleranza, approvati in DocBits)        | I costi esterni in fattura sono superiori a quelli del PO e oltre la tolleranza accettata, e sono approvati in DocBits.                       | I costi aggiuntivi vengono registrati su PP20-228. Sono state considerate due opzioni:\<br>- Se la tolleranza APS900 > DocBits, i costi aggiuntivi vengono registrati automaticamente.\<br>- Se la tolleranza APS900 = DocBits, i costi aggiuntivi vengono registrati con nuovi elementi di costo non presenti nel PO. |
| 6           | Costi esterni in fattura inferiori al PO (oltre la tolleranza, non approvati)               | I costi esterni in fattura sono inferiori a quelli del PO e oltre la tolleranza accettata, e non sono approvati.                              | La fattura viene registrata come non approvata in APS110. Il team AP rettifica i costi tramite l'opzione Invoice Control in APS110, che richiama APS360.                                                                                             |
| 7           | Costi esterni nel PO e nessun costo in fattura                                              | I costi esterni sono elencati nel PO, ma in fattura non sono presenti costi.                                                                  | La fattura viene registrata come non approvata in APS110. Il team AP rettifica i costi tramite l'opzione Invoice Control in APS110, che richiama APS360.                                                                                             |

## Esempio per lo scenario 5

| Campo            | Valore PO | Valore fattura fornitore |
| ---------------- | --------- | ------------------------ |
| Riga 1           | $6000     | $6000                    |
| Trasporto (E001) | $1000     | $3000                    |
| **Totale**       | $7000     | $9000                    |

**Tolleranza del trasporto:** $100 approvati automaticamente in M3 (APS900) e in DocBits. Valore totale della fattura di $9000 approvato (con i costi accessori) manualmente.

**APS451 (riga fattura):**

* Line Type 1 (riga fattura): $9000
* Line Type 5 (costo di riga): $1000 (elemento: E001 per trasporto sul PO $1000)
* Line Type 5 (costo di riga): $2000 (elemento: E101 per trasporto sul PO $0)

### Campi e valori importanti per la gestione dei costi accessori in DocBits

| Campo                       | Descrizione                                                          |
| --------------------------- | -------------------------------------------------------------------- |
| Sequence Number             | Identificativo univoco per ciascuno scenario di costo                |
| Costing Element ID          | Identificativo dell'elemento di costo                                |
| Costing Element Description | Descrizione dell'elemento di costo                                   |
| Charge Type                 | Tipicamente "External"                                               |
| Charge Invoicing            | La rilevanza deve essere determinata                                 |
| Distribution Method         | Metodo utilizzato per la distribuzione dei costi                     |
| Gross Weight                | Applicabile se il peso lordo è disponibile in fattura                |
| Volume                      | I casi applicabili devono essere definiti                            |
| Net Amount                  | I casi applicabili devono essere definiti                            |
| 3rd Party Charge            | Presenza in fattura e requisiti di elaborazione                      |
| Invoice Charge Quantity     | Chiarimento necessario                                               |
| Markup                      | Si presume sia la differenza tra costo e sconto                      |
| Charge Category             | La rilevanza deve essere definita                                    |
| Costing Operator            | La rilevanza deve essere definita                                    |

\

