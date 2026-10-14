# Send HTTPS Request

<figure><img src="../../../../.gitbook/assets/image (4) (1) (1) (1) (1) (1).png" alt="" width="563"><figcaption></figcaption></figure>

## **Scopo:**

Questa scheda DocBits è progettata per facilitare l'interazione con i sistemi esterni inviando richieste HTTPS a URL specificati. Consente ai workflow di eseguire azioni come il recupero, l'aggiornamento o l'eliminazione di dati effettuando chiamate API, garantendo un'integrazione fluida con i servizi esterni.

## **Funzionalità:**

* **Esecuzione della richiesta HTTPS:** La scheda invia una richiesta a un URL specificato utilizzando il metodo HTTP configurato (es. GET, POST, PUT, DELETE).
* **Header e parametri:** Gli utenti possono includere header personalizzati e parametri di query per garantire che la richiesta soddisfi i requisiti dell'API esterna.
* **Dati della richiesta:** Consente agli utenti di definire il payload di dati (se applicabile) da inviare con la richiesta, come dati JSON o form-encoded.
* **Valutazione della risposta:** Il workflow verifica se il codice di stato ricevuto corrisponde al valore atteso, garantendo una comunicazione riuscita prima di proseguire.
* **Metodi HTTP supportati:**
  * GET: Recupera dati dall'URL specificato.
  * POST: Invia dati all'URL specificato per creare risorse.
  * PUT: Aggiorna risorse esistenti all'URL specificato.
  * DELETE: Rimuove risorse dall'URL specificato.

## **Utilizzo:**

Questa scheda è particolarmente utile negli scenari in cui i workflow devono interagire con API esterne per lo scambio di dati, come l'invio di aggiornamenti a un CRM, il recupero degli stati degli ordini o la pubblicazione di nuove voci in un database.

## **Scenario di esempio:**

* Un utente configura la scheda per inviare una richiesta POST a un sistema esterno di gestione degli ordini con un payload contenente i dettagli di un nuovo ordine. Vengono aggiunti header personalizzati per includere i token di autenticazione dell'API. La scheda è impostata per proseguire solo se il codice di stato della risposta è 201 (Created). Se il codice di stato è diverso, il workflow attiva una notifica di errore per l'intervento manuale.

Utilizzando la scheda "Send HTTPS Request", le organizzazioni possono automatizzare le integrazioni esterne, migliorare la comunicazione tra i sistemi e semplificare i workflow complessi.
