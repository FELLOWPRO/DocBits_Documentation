# Debug Collector

Il Debug Collector cattura un'istantanea completa della tua sessione DocBits — attività di rete, errori, ambiente del browser e metriche di prestazione — la confeziona come un report JSON e, se vuoi, apre direttamente un ticket di supporto dalla stessa finestra.

## Come accedere

Premi <kbd>Ctrl</kbd> + <kbd>Shift</kbd> + <kbd>P</kbd> su Windows e Linux, oppure <kbd>Cmd</kbd> + <kbd>Shift</kbd> + <kbd>P</kbd> su macOS. La finestra Performance Report si apre subito.

<figure><img src="../../.gitbook/assets/debug-collector-dialog.png" alt="Finestra Debug Collector"><figcaption><p>La finestra Performance Report mostra l'istantanea catturata e un modulo integrato per creare il ticket.</p></figcaption></figure>

## Cosa viene catturato

* **Chiamate API** — le ultime 60 chiamate REST e WebSocket, con tempi, codici di stato e URL contattati. Le chiamate oltre i due secondi sono segnalate a parte.
* **Errori** — errori JavaScript recenti e promesse rifiutate non gestite dalla console del browser.
* **Log di console** — i messaggi di log più recenti dell'applicazione.
* **Ambiente** — versione del browser, sistema operativo, dimensione dello schermo e feature flag attivi.
* **Contesto utente** — il tuo ruolo, organizzazione e la pagina in cui ti trovavi quando l'istantanea è stata acquisita.
* **Metriche di prestazione** — tempi di caricamento della pagina (LCP, FCP), uso della memoria e dimensione del DOM.
* **Trace ID** — identificativi di correlazione che collegano l'istantanea ai log del backend.

## Creare un ticket di supporto dalla finestra

Non devi scaricare né allegare nulla manualmente — la finestra contiene il modulo **Create Support Ticket**.

1. Inserisci la tua email, lascia l'oggetto suggerito o modificalo, scegli una priorità e aggiungi qualche nota che spieghi cosa stavi facendo quando si è verificato il problema.
2. Clicca su **Send Report**. L'istantanea JSON viene allegata e il ticket viene creato in un unico passaggio.

Tutto qui — il supporto riceve il ticket con tutti i dati necessari per riprodurre il caso.

Se vuoi una copia locale dell'istantanea, usa **Copy Debug Data** per copiare il JSON negli appunti, oppure la funzione Salva con nome del browser per conservare il report come file `.json`.

## Privacy e gestione dei dati

* I token di autenticazione e gli header sensibili vengono mascherati dalle chiamate API catturate prima della costruzione dell'istantanea.
* Nulla esce dal browser finché non clicchi su **Send Report** — la scorciatoia si limita ad aprire la finestra.

<mark>Rivedi l'istantanea prima di inviarla se stavi lavorando con documenti che contengono dati cliente. Gli identificativi di documento visibili negli URL compariranno nel report.</mark>
