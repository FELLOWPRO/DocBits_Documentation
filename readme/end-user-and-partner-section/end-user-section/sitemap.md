# Mappa del Sito

La Mappa del Sito è l'indice completo e ricercabile di tutto ciò che DocBits espone — ogni pagina, finestra, voce della barra laterale, azione e funzione interna alla pagina, raggruppata per categoria. È il complemento esteso della [Ricerca Rapida Globale](global-quick-search.md).

## Come accedere

Apri la Mappa del Sito dalla barra laterale (voce in fondo) o premi <kbd>Cmd</kbd>/<kbd>Ctrl</kbd> + <kbd>K</kbd> e scegli **Vedi tutti i risultati**. L'URL diretto è `/sitemap`.

<figure><img src="../../.gitbook/assets/sitemap-overview.png" alt="Panoramica della Mappa del Sito"><figcaption><p>Mappa del Sito con panoramica per categorie e intestazione di ricerca.</p></figcaption></figure>

## Sfogliare il catalogo

La Mappa del Sito è raggruppata per categorie che rispecchiano la struttura dell'applicazione — Impostazioni, Elaborazione documenti, Workflow, Validazione e così via. Ogni categoria elenca prima le sue pagine e poi le funzioni interne raggruppate per sottocategoria.

Le voci sono colorate per tipo:

* **Pagina** — un percorso navigabile completo.
* **Finestra** — un modale aperto da un altro punto dell'applicazione.
* **Barra laterale / Pannello / Menu** — un'area di navigazione o di contesto.
* **Azione** — un pulsante o una scorciatoia che esegue qualcosa senza navigare.

Clicca su qualsiasi voce per saltarvi direttamente. Le voci che richiedono un parametro (un tipo di documento o un identificativo) includono un selettore incorporato — scegli il valore prima di cliccare.

## Cerca e filtra

L'intestazione fissa in alto contiene la casella di ricerca e i filtri a forma di pillola. Digita pochi caratteri per filtrare la lista in tempo reale per nome e descrizione. Usa le pillole di tipo per restringere a un singolo tipo di voce — per esempio solo **Finestra**.

La ricerca e il filtro correnti vengono aggiunti all'URL, così una vista filtrata può essere salvata o condivisa.

<mark>La Mappa del Sito rispetta gli stessi permessi del resto di DocBits. Le pagine a cui non hai accesso non compaiono.</mark>

## Modalità sviluppatore

Un interruttore **Utente / Dev** nell'intestazione attiva informazioni aggiuntive per gli sviluppatori partner:

* Il percorso interno di ogni voce.
* I tag dei parametri (`:docType`, `:docId`, chiavi di deep link).

La modalità sviluppatore viene ricordata nel browser. Torna in modalità Utente per la normale lettura.

## Torna su

La Mappa del Sito è lunga. Una volta superata la prima schermata, in basso a destra appare un pulsante Torna su.
