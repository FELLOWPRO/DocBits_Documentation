---
description: "P1: calcolare colonne e verificare dipendenze regex"
---

# P1: calcolare colonne e verificare dipendenze regex

**Calculate Columns** calcola due colonne della stessa riga e scrive il risultato. **Calculate in / CALC_COLUMNS_REGEX** aggiunge una condizione regex su una terza colonna. La regex decide qui se calcolare; non estrae né sostituisce testo. La precedente spiegazione delle sostituzioni non descrive questa scheda.

Esempio: `QTY=2`, `PRICE=10`, operazione `*`, risultato `TOTAL=20.0`. Per la variante regex usare `TYPE` e modello `^A$`. Una riga A viene calcolata. Per una riga B non corrispondente il codice scrive un risultato vuoto; un TOTAL esistente non viene conservato automaticamente.

La funzione aritmetica arrotonda i risultati a quattro decimali. Un operando vuoto può diventare 0; due testi vuoti restituiscono vuoto. `+` può concatenare testi non numerici. Nella funzione esaminata, `10/0` genera un errore. Validare numeri e celle necessarie prima del calcolo e predisporre un percorso di errore.

Conservare una tabella prima/dopo completa: due righe corrispondenti, una non corrispondente, input vuoto, testo non valido e divisione per zero. Per calcoli dipendenti A→B, collegare esplicitamente le schede e controllare il valore aggiornato letto da B. Confrontare ogni riga e le altre colonne esistenti, oltre allo stato documentale.

## Schede e parametri di esempio

I valori descrivono parametri delle schede, non un workflow completo importabile. Sostituire YOUR_* con selezioni proprie di test. Il designer gestisce l’ID nascosto del chiamante. Catalogo: Dev, DocFlow 2.10.38, 21 ottobre 2026; verificare versioni e abilitazioni della propria organizzazione.

### `calc_columns` · v2

Identità: `92d7a634-736a-4e1f-80b3-2b521efcd81c`

| Parametro | Tipo / opzioni | Esempio |
| --- | --- | --- |
| `result_column_name` | `result_column_name:str` | `"TOTAL"` |
| `table_column_name_left` | `table_column_name_left:str` | `"QTY"` |
| `math_operator` | `+ / - / / / *` | `"*"` |
| `table_column_name_right` | `table_column_name_right:str` | `"PRICE"` |
| `table_name` | `table_name:str` | `"LINE_ITEMS"` |

### `calc_columns_regex` · v2

Identità: `dbf035c8-927b-444a-9e5a-18555f5deacf`

| Parametro | Tipo / opzioni | Esempio |
| --- | --- | --- |
| `table_name` | `table_name:str` | `"LINE_ITEMS"` |
| `result_column_name` | `result_column_name:str` | `"TOTAL"` |
| `regex_pattern` | `regex_pattern:str` | `"^A$"` |
| `column_name_dependency` | `column_name_dependency:str` | `"TYPE"` |
| `table_column_name_right` | `table_column_name_right:str` | `"PRICE"` |
| `math_operator` | `+ / - / / / *` | `"*"` |
| `table_column_name_left` | `table_column_name_left:str` | `"QTY"` |

## Casi di prova aziendali

| Caso | Input / configurazione | Risultato atteso |
| --- | --- | --- |
| CALC-01 | QTY=2; PRICE=10; TYPE=A; ^A$ | TOTAL=20.0 |
| CALC-02 | QTY=2; PRICE=10; TYPE=B; ^A$; TOTAL=99 | TOTAL="" |
| CALC-03 | 10 / 3 | 3.3333 |
| CALC-04 | 10 / 0 | error |
| CALC-05 | "" + 2 | 2.0 |
| CALC-06 | x + y | "x y" |

## Prove e limiti

Parametri e comportamento sono stati confrontati con catalogo Dev e codice esaminato. I casi aziendali sono una procedura di collaudo. Per questo capitolo non sono state eseguite approvazioni personali, modifiche reali o consegne.

[Continuare il percorso](../workflow-learning-path.md) · [Kit di esercitazione](../workflow-training-kit.md)
