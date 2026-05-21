# Impostazioni della Ricerca a Testo Completo

<figure><img src="../../../.gitbook/assets/fulltext_search_settings.png" alt="Impostazioni della Ricerca a Testo Completo"><figcaption><p>Impostazioni della Ricerca a Testo Completo — Finestra "Modulo richiesto"</p></figcaption></figure>

Le Impostazioni della Ricerca a Testo Completo controllano cosa DocBits indicizza e come quel contenuto diventa ricercabile su documenti, dati anagrafici ERP e modelli. La pagina delle impostazioni si apre solo quando il **modulo Ricerca a Testo Completo** è attivo — consulta [Ricerca a Testo Completo](../document-processing/module/fulltext-search.md) per il linguaggio di interrogazione utente.

## Prerequisiti

Il modulo Ricerca a Testo Completo deve essere attivato in **Impostazioni → Elaborazione Documenti → Modulo → Dashboard → Ricerca a testo completo**. Se il modulo non è attivo, una finestra ti propone:

* **Vai ai Moduli** — Apri la pagina di configurazione dei Moduli per controllare le impostazioni.
* **Attiva ora** — Attiva direttamente il modulo Ricerca a Testo Completo (avvia un abbonamento DocSearch).

La pagina delle impostazioni stessa diventa accessibile non appena il modulo è attivo.

## Layout della pagina

La pagina delle impostazioni è organizzata in tre schede, ognuna che copre un diverso tipo di contenuto che la Ricerca a Testo Completo può indicizzare.

### Scheda "Documenti"

La scheda Documenti copre tutto ciò che riguarda l'indicizzazione dei documenti elaborati:

* **Statistiche di indicizzazione** — totali per documenti indicizzati e in attesa, aggiornabili su richiesta.
* **Preferenze vettoriali** — tre interruttori a livello di organizzazione che decidono se l'indicizzazione vettoriale gira in parallelo all'indice testuale per i documenti. L'indicizzazione vettoriale alimenta la modalità di interrogazione `vector:` e la funzione "Trova simili".
* **Azioni di reindicizzazione** — avvia una reindicizzazione completa o incrementale. Durante l'esecuzione vedi il progresso in tempo reale (documenti al minuto, tempo stimato), lo stato attuale del flusso e l'ultimo errore (se presente).
* **Diagnostica di sincronizzazione** — diagnostica su richiesta per i casi in cui l'indice sembra disallineato dal magazzino dei documenti sottostante.

<mark>La reindicizzazione non è distruttiva — la ricerca esistente continua a funzionare mentre il nuovo indice viene ricostruito.</mark>

### Scheda "ERP"

La scheda ERP controlla l'indicizzazione dei dati anagrafici ERP — fornitori, clienti, articoli ed entità simili. Ogni entità ha il proprio interruttore:

* **Indicizzazione** — indicizza testualmente l'entità in modo che sia ricercabile dal dashboard.
* **Vettore** — indicizza vettorialmente l'entità in modo che possa essere abbinata da query semantiche.

Usa l'azione **Commuta tutto** in cima alla lista per applicare lo stesso stato a tutte le entità contemporaneamente. L'indicizzazione parte in background; un indicatore su ogni riga mostra quando è in corso.

### Scheda "Modelli"

La scheda Modelli elenca le versioni dei modelli note all'indice di Ricerca a Testo Completo. Usa questa vista per confermare dopo un nuovo rilascio che le versioni di modello da cui dipendi siano presenti nell'indice.

## Cosa viene indicizzato

Una volta attivata e configurata, la Ricerca a Testo Completo permette agli utenti di:

* Cercare in tutto il contenuto del documento (non solo nei campi di metadati).
* Trovare documenti tramite il testo contenuto nei file caricati.
* Usare operatori di ricerca avanzati per query precise.
* Accedere ai risultati direttamente dal dashboard.
* Usare la ricerca semantica (prefisso `vector:`) quando l'indicizzazione vettoriale è attiva per quel tipo di contenuto.

Consulta la pagina del modulo [Ricerca a Testo Completo](../document-processing/module/fulltext-search.md) per il riferimento completo del linguaggio di interrogazione, incluse query per intervalli, filtri intelligenti e la modalità di ricerca AI.
