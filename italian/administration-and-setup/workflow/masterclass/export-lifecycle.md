---
description: "P1: scegliere export, attività aperte e stato finale"
---

# P1: scegliere export, attività aperte e stato finale

**Start Export** usa il percorso di esportazione configurato. **Export with Export Configuration** esegue una configurazione scelta. La variante differita la accoda per l’export finale alla fine dell’esecuzione corrente. Accodare non significa inviare automaticamente dopo tutte le future approvazioni umane.

Le nuove versioni esaminate offrono `status=finished` o `status=exported`: finished chiude il documento, exported consente altre modifiche. La scelta è disponibile da v4 per Start Export e da v3 per export configurato e differito. Le versioni precedenti usano finished. Anche nelle nuove, l’assenza della scelta usa finished; un valore non valido è un errore di configurazione.

Con `ignore_pending_tasks=false` si controllano le attività aperte. Il servizio può quindi rifiutare l’export configurato immediato. Questa scheda non prova una ripresa automatica dopo la successiva chiusura delle attività. Definire un nuovo evento e verificare eventuali registrazioni di destinazione prima di reinviare. Ignorare attività non sostituisce l’approvazione.

Collegare l’export solo dopo una condizione di approvazione verificata esplicitamente. Il collaudo copre attività aperta, chiusa, approvazione assente, ricezione nel destinatario di test e ripetizione. Distinguere richiesta di export, ricezione ed elaborazione ERP. Il kit non contiene destinazioni reali e i suoi test non provano la consegna.

## Schede e parametri di esempio

I valori descrivono parametri delle schede, non un workflow completo importabile. Sostituire YOUR_* con selezioni proprie di test. Il designer gestisce l’ID nascosto del chiamante. Catalogo: Dev, DocFlow 2.10.38, 21 ottobre 2026; verificare versioni e abilitazioni della propria organizzazione.

### `export` · v4

Identità: `757f30ca-ed60-4e04-8131-2779df17f019`

| Parametro | Tipo / opzioni | Esempio |
| --- | --- | --- |
| `boolean` | `boolean:bool` | `true` |
| `status` | `finished / exported` | `"finished"` |

### `action_export_with` · v3

Identità: `ebcd854d-68b3-4b5f-8d45-1bcf8c675b21`

| Parametro | Tipo / opzioni | Esempio |
| --- | --- | --- |
| `export_configuration` | `export_configuration:int` | `"YOUR_TEST_EXPORT_CONFIGURATION_ID"` |
| `ignore_pending_tasks` | `ignore_pending_tasks:bool` | `false` |
| `status` | `finished / exported` | `"exported"` |

### `action_export_with_config_deferred` · v3

Identità: `060ef4c8-625f-447c-83c9-2ca3f680d88d`

| Parametro | Tipo / opzioni | Esempio |
| --- | --- | --- |
| `export_configuration` | `export_configuration:int` | `"YOUR_TEST_EXPORT_CONFIGURATION_ID"` |
| `ignore_pending_tasks` | `ignore_pending_tasks:bool` | `false` |
| `status` | `finished / exported` | `"finished"` |

## Casi di prova aziendali

| Caso | Input / configurazione | Risultato atteso |
| --- | --- | --- |
| EXPORT-01 | status=finished | chiuso |
| EXPORT-02 | status=exported | modificabile |
| EXPORT-03 | ignore_pending_tasks=false; pending_tasks>0 | rifiuto possibile; ripresa automatica non provata |
| EXPORT-04 | action_export_with_config_deferred | accodato ≠ ricevuto |
| EXPORT-05 | RUN-1 → RUN-2 | destination_records=1 |

## Prove e limiti

Parametri e comportamento sono stati confrontati con catalogo Dev e codice esaminato. I casi aziendali sono una procedura di collaudo. Per questo capitolo non sono state eseguite approvazioni personali, modifiche reali o consegne.

[Continuare il percorso](../workflow-learning-path.md) · [Kit di esercitazione](../workflow-training-kit.md)
