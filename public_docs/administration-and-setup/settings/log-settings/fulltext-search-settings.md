# Impostazioni della Ricerca a testo completo

<figure><img src="../../../.gitbook/assets/fulltext_search_settings.png" alt="Impostazioni della Ricerca a testo completo nella sandbox, con una finestra che spiega che il modulo è necessario e i pulsanti Go to Modules ed Enable Now"><figcaption><p>Quando la Ricerca a testo completo è disattivata, questa finestra spiega i passaggi successivi.</p></figcaption></figure>

Le Impostazioni della Ricerca a testo completo stabiliscono cosa DocBits indicizza e come rende tali contenuti ricercabili nei documenti, nei dati anagrafici ERP e nei modelli. La pagina delle impostazioni mostra una finestra di requisito finché il **Fulltext Search module** non è attivato — vedi [Ricerca a testo completo](../document-processing/module/fulltext-search.md) per il linguaggio di interrogazione destinato all'utente.

## Prerequisiti

Il modulo Fulltext Search deve essere attivato in **Settings → Module → Dashboards & Analytics → Full text search**. Se il modulo non è attivato, la finestra offre tre azioni:

* **Help (?)** — apre la documentazione della Ricerca a testo completo in una nuova scheda prima di modificare qualsiasi impostazione.
* **Go to Modules** — apre le impostazioni del modulo Dashboards & Analytics per verificare la configurazione.
* **Enable Now** — apre la finestra dell'abbonamento. Esamina e conferma quella finestra prima che il modulo venga attivato; il solo clic su questo pulsante non lo attiva.

La pagina delle impostazioni stessa diventa disponibile quando il modulo è attivo.

## Struttura della pagina

La pagina delle impostazioni è organizzata in tre schede: **Documents**, **ERP** e **Templates**. Ogni scheda delimita un diverso tipo di contenuto che la Ricerca a testo completo può indicizzare.

### Scheda Documents

La scheda Documents copre tutto ciò che riguarda l'indicizzazione dei documenti elaborati:

* **Indexing statistics** — totali dei documenti indicizzati e in attesa, aggiornati su richiesta.
* **Vector preferences** — tre interruttori a livello di organizzazione che stabiliscono se l'indicizzazione vettoriale viene eseguita parallelamente all'indice testuale per i documenti. L'indicizzazione vettoriale alimenta la modalità di interrogazione `vector:` e la funzione "Find Similar".
* **Reindex actions** — avvia una reindicizzazione completa o incrementale. Mentre una reindicizzazione è in corso, vedi il progresso in tempo reale (documenti al minuto, ETA), lo stato del flusso corrente e l'ultimo errore (se presente).
* **Sync diagnostics** — diagnostica su richiesta per i casi in cui l'indice sembra non essere sincronizzato con l'archivio dei documenti sottostante.

<mark>La reindicizzazione non è distruttiva — la ricerca esistente continua a funzionare mentre il nuovo indice viene ricostruito.</mark>

### Scheda ERP

La scheda ERP controlla l'indicizzazione dei dati anagrafici ERP — fornitori, clienti, articoli ed entità simili. Ogni entità ha il proprio interruttore:

* **Indexing** — indicizza testualmente l'entità in modo che sia ricercabile dalla dashboard.
* **Vector** — indicizza vettorialmente l'entità in modo che possa essere trovata tramite query semantiche.

Usa l'azione **Toggle all** in cima all'elenco per applicare lo stesso stato attivo/disattivo a tutte le entità contemporaneamente. L'indicizzazione parte in background; un indicatore su ogni riga mostra quando è in corso.

### Scheda Templates

La scheda Templates elenca le versioni dei modelli note all'indice della Ricerca a testo completo. Usa questa vista per confermare che le versioni dei modelli da cui dipendi siano presenti nell'indice dopo un nuovo rilascio.

## Cosa viene indicizzato

Una volta attivata e configurata, la Ricerca a testo completo consente agli utenti di:

* Cercare in tutto il contenuto dei documenti (non solo nei campi dei metadati).
* Trovare documenti tramite il testo contenuto nei file caricati.
* Usare operatori di ricerca avanzati per query precise.
* Accedere ai risultati di ricerca direttamente dalla dashboard.
* Usare la ricerca semantica (prefisso `vector:`) quando l'indicizzazione vettoriale è attiva per quel tipo di contenuto.

Consulta la pagina del modulo [Ricerca a testo completo](../document-processing/module/fulltext-search.md) per il riferimento completo del linguaggio di interrogazione, comprese le query per intervalli, i filtri intelligenti e la modalità di ricerca AI.
