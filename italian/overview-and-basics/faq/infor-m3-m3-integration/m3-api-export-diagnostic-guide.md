# Guida diagnostica all'esportazione dell'API M3

### 1. Configurazione iniziale

Prima di iniziare la risoluzione dei problemi, assicurati di essere familiare con gli input attesi per il punto finale M3 con cui stai lavorando.

#### 1.1 Accesso alla documentazione dell'API M3

* Accedi a **M3**.
* Vai alla sezione **API → Documentazione API**.
* Trova e seleziona il punto finale rilevante (ad es. `APS450MI` per le esportazioni relative alle fatture).
* Scegli la funzione appropriata (ad es. `Aggiungi`).

#### 1.2 Comprendere i requisiti dell'API

* Controlla tutti i **campi obbligatori** nella documentazione dell'API.
* Presta attenzione a campi importanti come:
  * `DIVI`
  * `ACDT` (data contabile)
  * `CUCD` (codice valuta)
  * `SINO` (numero fattura fornitore)
* Conferma i **tipi di dati** dei campi, la **casing**, e le **regole di formattazione** (ad es. `YYYY-MM-DD` per le date).

### 2. Test delle chiamate API direttamente in M3

Questo passaggio verifica che l'API M3 si comporti come previsto utilizzando input manuali.

#### 2.1 Generare una richiesta di test in M3

* Nel tool di Documentazione dell'API M3:
  * Compila i dati di test per i campi obbligatori.
  * Clicca su **Esegui** per eseguire la richiesta.
  * Copia il **cURL** risultante e il **corpo JSON**.

#### 2.2 Debug tramite Postman

* Apri **Postman** e crea una nuova richiesta **POST**.
* Incolla il corpo JSON o il cURL.
* Aggiungi gli header necessari (ad es. autorizzazione).
* Clicca su **Invia** e osserva il risultato:
  * `200 OK`: La richiesta è stata eseguita con successo.
  * Errore: Controlla il messaggio per i dettagli su cosa è andato storto.

### 3. Confronto tra l'API M3 e il mapping di DocBits

Una volta confermato che l'API funziona con i dati di test, confrontala con ciò che DocBits sta effettivamente inviando.

#### 3.1 Esporta dati di esempio da DocBits

*   Apri la **documentazione dell'API di DocBits**:

    Utilizza il punto finale **/export/get\_infor\_export\_api\_json**.
* Inserisci l'**ID del documento** di un documento problematico.
* Esegui l'esportazione per visualizzare il **payload JSON** che DocBits invierà a M3.

#### 3.2 Confronta i payload dell'API

* Metti a confronto il **JSON di test di M3** e il **JSON di esportazione di DocBits** uno accanto all'altro.
* Controlla:
  * **Nomi dei campi**: Assicurati che i nomi corrispondano _esattamente_, incluso il caso (`DIVI` ≠ `divi`).
  * **Tipi di dati**: Verifica che le stringhe, i numeri e le date siano formattati correttamente.
  * **Campi mancanti**: Identifica eventuali campi presenti nella richiesta di M3 ma mancanti in DocBits.

### 4. Risoluzione dei problemi comuni

| Problema                                  | Causa probabile                                | Soluzione                                                                      |
| ----------------------------------------- | ---------------------------------------------- | ------------------------------------------------------------------------------ |
| Errore campo mancante                     | Un campo obbligatorio non è mappato in DocBits | Aggiungi il campo mancante nella configurazione di esportazione di DocBits.    |
| Discrepanza nel casing del campo (`DIVI`) | M3 è sensibile al case                         | Utilizza il casing corretto nel mapping del campo.                             |
| Formato `accountingDate` non valido       | Data errata o mancante                         | Adatta al formato previsto da M3 (ad es. `YYYY-MM-DD`).                        |
| Errore API inaspettato                    | Campi extra o non riconosciuti                 | Confronta con i payload funzionanti conosciuti e pulisci i dati non necessari. |

### 5. Se i problemi persistono

Se il problema non è risolto dopo aver seguito i passaggi precedenti:

1. **Documenta** il problema:
   * Messaggio di errore e codice di stato
   * Richiesta di M3 di esempio e JSON di esportazione di DocBits
2. **Sintetizza** la tua risoluzione dei problemi:
   * Cosa hai provato
   * Differenze chiave osservate tra i dati di test e i payload non riusciti
3. **Segnala** a uno sviluppatore:
   * Includi tutti i dati e le scoperte
   * Evidenzia le aree del problema sospettate
