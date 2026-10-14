# Call Api

<figure><img src="../../../../.gitbook/assets/Then_Call_API.png" alt="" width="563"><figcaption></figcaption></figure>

## Scopo:

La scheda di workflow **"Call API"** consente agli utenti di effettuare richieste HTTP a endpoint API specificati direttamente dal workflow. Questa scheda supporta vari metodi HTTP e consente un'interazione dinamica con sistemi esterni inviando parametri e dati. Semplifica l'integrazione con servizi di terze parti e API personalizzate, garantendo una comunicazione fluida.

## Componenti della scheda:

1. **API Endpoint**
   * **Descrizione:** L'endpoint di destinazione della **DocBits API** con cui questa scheda interagirà.
   * **Dettaglio:** Un campo di testo in cui gli utenti specificano l'endpoint per la richiesta API.
2. **HTTP Method**
   * **Descrizione:** Il tipo di richiesta HTTP da effettuare.
   * **Opzioni:**
     1. **GET:** Recupera dati dall'endpoint specificato.
     2. **POST:** Invia dati all'endpoint.
     3. **PUT:** Aggiorna dati esistenti all'endpoint.
     4. **DELETE:** Rimuove dati all'endpoint.
3. **Parameters**
   * **Descrizione:** Parametri di query da includere nella richiesta API.
   * **Dettaglio:** Un campo di testo o un elenco per inserire coppie chiave-valore per l'URL della richiesta.
4. **Data**
   1. **Descrizione:** Il payload da inviare nel corpo della richiesta API (applicabile ai metodi POST e PUT).
   2. **Dettaglio:** Un campo per inserire i dati in formato JSON.

## Funzionalità:

**Valutazione della condizione:** Il sistema valuta le condizioni definite nelle sezioni "Where" e "And":

* Se entrambe le condizioni sono **vere**, la richiesta API viene eseguita come configurata.
* Se una delle condizioni è **falsa**, la scheda non viene eseguita e non viene effettuata alcuna chiamata API.

**Esecuzione della richiesta API:**

* La scheda invia la richiesta HTTP all'endpoint specificato utilizzando il metodo selezionato.
* Eventuali parametri forniti vengono aggiunti all'URL e i dati vengono inclusi nel corpo della richiesta (se applicabile).

## Configurazione e impostazione:

1. **Definisci l'API Endpoint:**\
   Inserisci l'URL dell'API che desideri chiamare.
2. **Seleziona il metodo HTTP:**\
   Scegli uno dei metodi supportati (GET, POST, PUT, DELETE) in base ai requisiti della tua API.
3. **Fornisci i parametri:**\
   Aggiungi eventuali parametri di query richiesti come coppie chiave-valore.
4. **Includi i dati (se applicabile):**\
   Per i metodi POST o PUT, specifica i dati da inviare nel corpo della richiesta.
5. **Configurazione delle condizioni:**\
   Configura le sezioni "Where" e "And" per definire quando la chiamata API deve avvenire.

## Conclusione:

La scheda di workflow **"Call API"** migliora l'automazione del workflow consentendo un'interazione diretta con sistemi esterni. Fornendo configurazioni flessibili per endpoint, metodi e dati, garantisce che i workflow possano integrarsi senza problemi con API di terze parti o backend personalizzati. La possibilità di eseguire condizionatamente le chiamate API garantisce precisione ed efficienza nell'automazione delle comunicazioni esterne.

***
