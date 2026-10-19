# Gestione della cache

<figure><img src="../../.gitbook/assets/cache_management.png" alt="Gestione della cache"><figcaption><p>Pagina Gestione della cache</p></figcaption></figure>

La Gestione della cache controlla la cancellazione automatica della cache per i dati a cui si accede di frequente. L'attivazione della cache migliora le prestazioni riducendo le chiamate API ripetute.

## Svuota cache

Clicca sul pulsante **Clear Cache** (in alto a destra) per invalidare immediatamente e manualmente tutti i dati nella cache.

## Tabella della cache

| Colonna | Descrizione |
|--------|-------------|
| **Object** | Il tipo di dati nella cache (ad es. Receive Delivery Cache, Purchase Order Cache). |
| **Status** | Interruttore per attivare o disattivare la cache per questo oggetto. |
| **TTL** | Time to Live in minuti: per quanto tempo i dati nella cache restano validi prima di essere aggiornati automaticamente. Imposta `0` per disattivare la scadenza automatica. |

## Cache disponibili

| Cache | Descrizione |
|-------|-------------|
| **Receive Delivery Cache** | Memorizza nella cache i dati delle ricevute di consegna utilizzati durante il PO matching. |
| **Purchase Order Cache** | Memorizza nella cache i dati degli ordini di acquisto per una ricerca più rapida durante l'elaborazione dei documenti. |
| **Task and Notification Cache** | Memorizza nella cache il numero di attività e i dati delle notifiche mostrati nella dashboard. |
