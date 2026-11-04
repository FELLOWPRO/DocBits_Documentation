---
description: "P1: scegliere Field is, Docfield is o Compare two Fields"
---

# P1: scegliere Field is, Docfield is o Compare two Fields

Usare **Field is** per lo stato vuoto, **Docfield is** per confrontare un valore configurato e **Compare two Fields** per due valori del documento corrente. Un controllo del vuoto non prova l’esistenza del campo nel layout né la sua validità aziendale.

In Field is v2, campo assente, `null`, testo vuoto, soli spazi e booleano `false` sono vuoti. Il numero `0`, il testo `"0"` e il testo `"false"` non lo sono. Questi otto casi sono stati provati in Dev con dati documentali completi. Per una decisione vero/falso, usare una condizione esplicita per checkbox.

`"1000.01"` in un campo AMOUNT differisce dagli stessi caratteri in un campo testo. Il kit v2 usa AMOUNT e punti decimali nel JSON. Controllare insieme chiave tecnica, layout e tipo. Un’etichetta tradotta non è una chiave tecnica; un simbolo di valuta non è un valore numerico.

Per Compare two Fields, definire campo sinistro, operatore e campo destro. Verificare tipi compatibili ed entrambe le entrate: dati assenti o non confrontabili sono un errore, non una disuguaglianza provata. Ripetere caso positivo, negativo, input assente e limite esatto. Registrare valore, tipo e uscita scelta.

## Schede e parametri di esempio

I valori descrivono parametri delle schede, non un workflow completo importabile. Sostituire YOUR_* con selezioni proprie di test. Il designer gestisce l’ID nascosto del chiamante. Catalogo: Dev, DocFlow 2.10.38, 21 ottobre 2026; verificare versioni e abilitazioni della propria organizzazione.

### `condition_docfield_status` · v2

Identità: `6f346541-faa0-42bd-b1a5-b23282157da1`

| Parametro | Tipo / opzioni | Esempio |
| --- | --- | --- |
| `field_name` | `field_name:str` | `"total_amount"` |
| `field_status` | `field_empty / field_not_empty` | `"field_empty"` |

### `condition_docfield_operator_value` · v2

Identità: `1c35a5a0-1592-446c-9a61-6abb14d27450`

| Parametro | Tipo / opzioni | Esempio |
| --- | --- | --- |
| `operator` | `eq / neq / gt / ge / lt / le` | `"gt"` |
| `field_name` | `field_name:str` | `"total_amount"` |
| `field_value` | `field_value:str` | `"1000"` |

### `condition_compare_two_docfield_values` · v2

Identità: `3b3cdc55-6afe-4797-ae8b-9480ec3a8a30`

| Parametro | Tipo / opzioni | Esempio |
| --- | --- | --- |
| `field_name_right` | `field_name_right:str` | `"expected_amount"` |
| `field_name_left` | `field_name_left:str` | `"total_amount"` |
| `operator` | `eq / neq / gt / ge / lt / le` | `"eq"` |

## Casi di prova aziendali

| Caso | Input / configurazione | Risultato atteso |
| --- | --- | --- |
| FIELD-01 | missing / null / "" / "   " / false | field_empty=success |
| FIELD-02 | 0 / "0" / "false" | field_empty=failed_condition |
| FIELD-03 | AMOUNT 1000; gt 1000 | failed_condition |
| FIELD-04 | AMOUNT 1000.01; gt 1000 | success |
| FIELD-05 | AMOUNT missing / invalid; gt 1000 | error |

## Prove e limiti

Risultati selezionati di schede e nodi sono stati verificati con dati sintetici in Advanced Test. Le risposte sono nel kit. Le azioni documentali sono simulate e non provano esecuzione persistente o consegna esterna.

[Continuare il percorso](../workflow-learning-path.md) · [Kit di esercitazione](../workflow-training-kit.md)
