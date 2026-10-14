# Activity Logging

<figure><img src="../../../.gitbook/assets/activity_logging.png" alt="Activity Logging"><figcaption><p>La pagina Activity Logging</p></figcaption></figure>

Activity Logging offre una vista in tempo reale degli eventi di sistema di tutti i servizi DocBits. Usalo per monitorare l'attività di elaborazione, risolvere gli errori e verificare il comportamento del sistema.

## Analytics Banner

In cima alla pagina, un banner rimanda alla **Analytics Dashboard** per grafici, metriche e monitoraggio in tempo reale.

## Filtri

| Filtro | Descrizione |
|--------|-------------|
| **Time Range** | Seleziona un intervallo di tempo (ad es. Today, Last 7 Days, Last 30 Days). |
| **Severity** | Attiva o disattiva i livelli di gravità da includere o escludere: **Debug**, **Info**, **Warning**, **Error**. Ogni chip mostra il conteggio attuale. |
| **Service** | Filtra i log per servizio (ad es. api, auth, api-service). |
| **Search logs** | Ricerca a testo libero nei messaggi di log. |

## Tabella dei Log

| Colonna | Descrizione |
|--------|-------------|
| **Timestamp** | Data e ora in cui si è verificato l'evento. Ordinabile. |
| **Severity** | Badge colorato: Info (blu), Warning (giallo), Error (rosso), Debug (grigio). |
| **Component** | Il servizio o il modulo che ha generato il log (ad es. api, auth, api-service). |
| **Message** | Il messaggio di log completo con i dettagli dell'evento. |

I risultati sono paginati — usa i controlli in basso per scorrere le pagine.

## Azioni a piè di pagina

| Azione | Descrizione |
|--------|-------------|
| **Auto-refresh** | Attiva per aggiornare automaticamente la vista dei log a intervalli regolari. |
| **Refresh Now** | Aggiorna manualmente i dati dei log. |
| **Export JSON** | Esporta i log filtrati correnti come file JSON. |
| **Download Logs** | Scarica i dati completi dei log. |
