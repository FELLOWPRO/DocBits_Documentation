# Send HTTPS request to

<figure><img src="../../../../.gitbook/assets/Then_Send_HTTPS_1.png" alt="" width="563"><figcaption></figcaption></figure>

## Scopo:

La scheda di workflow **"Send HTTPS Request"** consente agli utenti di inviare richieste HTTPS a un URL specificato con header, parametri e payload di dati personalizzabili. Questa scheda è ideale per integrare API esterne o servizi web direttamente nel workflow.

## Componenti della scheda:

1. **URL**
   * **Descrizione:** Specifica l'endpoint a cui verrà inviata la richiesta HTTPS.
   * **Dettaglio:** Inserisci l'URL completo dell'API o del servizio web con cui connettersi.
2. **Headers**
   * **Descrizione:** Definisce gli header da includere nella richiesta HTTPS.
   * **Dettaglio:** Fornisci **coppie chiave-valore** in un **formato JSON valido** per specificare header come token di autenticazione o tipi di contenuto. Esempio: {"Authorization": "Bearer example\_value"}
3. **Method**
   * **Descrizione:** Specifica il metodo HTTP da utilizzare per la richiesta.
   * **Opzioni:**
     * **GET:** Recupera dati dall'endpoint.
     * **POST:** Invia dati all'endpoint per creare o aggiornare risorse.
     * **PUT:** Aggiorna risorse esistenti all'endpoint.
     * **DELETE:** Rimuove risorse dall'endpoint.
4. **Parameters**
   * **Descrizione:** Coppie chiave-valore da includere nell'URL come parametri di query.
   * **Dettaglio:** Utilizzalo per inviare filtri o dati aggiuntivi richiesti dall'endpoint in un formato JSON valido. Vedi l'esempio per gli Headers.
5. **Data**
   * **Descrizione:** Il corpo della richiesta HTTPS.
   * **Dettaglio:** Fornisci il payload in un formato JSON valido. Vedi l'esempio per gli Headers.

## Funzionalità:

* **Valutazione della condizione:** La scheda invia la richiesta HTTPS solo se le sezioni **"Where"** e **"And"** risultano vere.&#x20;
  * Se una delle condizioni è falsa, la richiesta non viene inviata.
* **Esecuzione della richiesta:**
  * Quando le condizioni sono soddisfatte, il sistema invia la richiesta HTTPS con le configurazioni specificate.

## Configurazione e impostazione:

1. **Definisci l'URL:** Inserisci l'endpoint a cui inviare la richiesta HTTPS.
2. **Imposta gli Headers:** Fornisci gli header richiesti come coppie chiave-valore.
3. **Seleziona il metodo HTTP:** Scegli il metodo appropriato (**GET**, **POST**, **PUT** o **DELETE**) in base all'azione da eseguire.
4. **Aggiungi i parametri:** Specifica eventuali parametri di query richiesti dall'endpoint.
5. **Fornisci il payload di dati:** Inserisci il corpo della richiesta nel formato richiesto (es. JSON) se necessario.
6. **Configura le condizioni:** Definisci le sezioni **"Where"** e **"And"** per garantire che la richiesta venga inviata solo quando determinate condizioni sono soddisfatte.

## Scheda di esempio:

<figure><img src="../../../../.gitbook/assets/Then_Send_HTTPS_2.png" alt="" width="375"><figcaption></figcaption></figure>

## Conclusione:

La scheda di workflow **"Send HTTPS Request"** semplifica l'integrazione delle API consentendo agli utenti di effettuare richieste personalizzate a servizi esterni direttamente dai loro workflow. Automatizzando il processo di invio delle richieste HTTPS e di gestione delle risposte, questa scheda migliora la flessibilità e la funzionalità del workflow.
