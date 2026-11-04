# Invia richiesta HTTPS

<figure><img src="../../../../.gitbook/assets/image (4) (1) (1) (1) (1) (1) (1).png" alt="" width="563"><figcaption></figcaption></figure>

## **Scopo:**

Questa carta DocBits è progettata per facilitare l'interazione con sistemi esterni inviando richieste HTTPS a URL specificati. Consente ai flussi di lavoro di eseguire azioni come il recupero, l'aggiornamento o la cancellazione di dati effettuando chiamate API, garantendo una perfetta integrazione con i servizi esterni.

## **Funzionalità:**

* **Esecuzione della richiesta HTTPS:** La carta invia una richiesta a un URL specificato utilizzando il metodo HTTP configurato (ad esempio, GET, POST, PUT, DELETE).
* **Intestazioni e parametri:** Gli utenti possono includere intestazioni personalizzate e parametri di query per garantire che la richiesta soddisfi i requisiti dell'API esterna.
* **Dati della richiesta:** Consente agli utenti di definire il payload dei dati (se applicabile) da inviare con la richiesta, come JSON o dati codificati nel modulo.
* **Valutazione della risposta:** Il flusso di lavoro controlla se il codice di stato ricevuto corrisponde al valore atteso, garantendo una comunicazione corretta prima di procedere.
* **Metodi HTTP supportati:**
  * GET: Recupera i dati dall'URL specificato.
  * POST: Invia dati all'URL specificato per creare risorse.
  * PUT: Aggiorna le risorse esistenti all'URL specificato.
  * DELETE: Rimuove le risorse dall'URL specificato.

## **Utilizzo:**

Questa carta è particolarmente utile in scenari in cui i flussi di lavoro devono interagire con API esterne per lo scambio di dati, come l'invio di aggiornamenti a un CRM, il recupero degli stati degli ordini o l'invio di nuove voci a un database.

## **Esempio di scenario:**

* Un utente configura la carta per inviare una richiesta POST a un sistema di gestione degli ordini esterno con un payload contenente i dettagli del nuovo ordine. Vengono aggiunte intestazioni personalizzate per includere i token di autenticazione API. La carta è impostata per continuare solo se il codice di stato della risposta è 201 (Creato). Se il codice di stato differisce, il flusso di lavoro attiva una notifica di errore per l'intervento manuale.

Utilizzando la carta "Invia richiesta HTTPS", le organizzazioni possono automatizzare le integrazioni esterne, migliorare la comunicazione tra i sistemi e semplificare i flussi di lavoro complessi.
