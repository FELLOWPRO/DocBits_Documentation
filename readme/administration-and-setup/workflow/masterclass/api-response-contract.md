---
description: "P1: verificare chiamate API e uso successivo delle risposte"
---

# P1: verificare chiamate API e uso successivo delle risposte

**Call API** v2 aggiunge il percorso configurato alla base API DocBits e usa il contesto organizzativo corrente. **Send HTTPS Request** v2 usa un URL esterno e intestazioni proprie. Un URL esterno completo non sostituisce un percorso Call API. Entrambe le schede simulano l’invio in Advanced Test.

L’azione HTTPS esaminata registra stato e testo della risposta ma non offre alle schede successive un archivio JSON liberamente nominabile. Call API converte il testo di risposta in booleano. HTTP 200, JSON valido ed elaborazione aziendale successiva riuscita richiedono prove distinte. Non inventare sintassi come `api.response.cost_center`.

Per una risposta esterna `{"cost_center":"4711"}`, concordare una scrittura o callback esplicitamente supportata in un campo documentale. Verificare il campo salvato e leggerlo nell’esecuzione successiva prevista. Il trasferimento diretto richiede una scheda o estensione con contratto di uscita documentato. JSON nella configurazione non prova automaticamente i byte JSON effettivamente inviati.

Usare un proprio destinatario di test e controllare metodo, intestazioni, corpo reale, stato e schema. Coprire 4xx, 5xx, timeout, JSON non valido e doppia attivazione. Ripetere scritture solo dopo aver verificato il primo ricevimento. L’URL di esempio è un segnaposto riservato e non è stato provato come servizio accessibile.

## Schede e parametri di esempio

I valori descrivono parametri delle schede, non un workflow completo importabile. Sostituire YOUR_* con selezioni proprie di test. Il designer gestisce l’ID nascosto del chiamante. Catalogo: Dev, DocFlow 2.10.38, 21 ottobre 2026; verificare versioni e abilitazioni della propria organizzazione.

### `call_api` · v2

Identità: `6ca5e621-af72-4f55-aa2e-b3caa288722a`

| Parametro | Tipo / opzioni | Esempio |
| --- | --- | --- |
| `params` | `params:str` | `"{}"` |
| `api_endpoint` | `api_endpoint:str` | `"YOUR_RELATIVE_API_PATH"` |
| `data` | `data:str` | `"{}"` |
| `method` | `put / post / delete / get` | `"get"` |

### `action_https_request` · v2

Identità: `18d06ca4-3aca-4e49-b75c-566ade2fcb10`

| Parametro | Tipo / opzioni | Esempio |
| --- | --- | --- |
| `data` | `data` | `"{}"` |
| `params` | `params` | `"{}"` |
| `url` | `url:str` | `"https://training.example.invalid/status"` |
| `headers` | `headers:str` | `"{}"` |
| `method` | `put / post / delete / get` | `"get"` |

## Casi di prova aziendali

| Caso | Input / configurazione | Risultato atteso |
| --- | --- | --- |
| API-01 | Advanced Test | simulato; nessuna prova di consegna |
| API-02 | HTTPS: 4xx / 5xx | error |
| API-03 | timeout | verificare ricezione prima di ripetere |
| API-04 | {"cost_center":"4711"} | nessun api.response.cost_center automatico |
| API-05 | POST × 2 | verificare duplicati a destinazione |

## Prove e limiti

Parametri e comportamento sono stati confrontati con catalogo Dev e codice esaminato. I casi aziendali sono una procedura di collaudo. Per questo capitolo non sono state eseguite approvazioni personali, modifiche reali o consegne.

[Continuare il percorso](../workflow-learning-path.md) · [Kit di esercitazione](../workflow-training-kit.md)
