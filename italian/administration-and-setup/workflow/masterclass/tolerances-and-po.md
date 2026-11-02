---
description: "P1: definire riferimento delle tolleranze e confronto PO"
---

# P1: definire riferimento delle tolleranze e confronto PO

La tolleranza percentuale dipende dal **lato di riferimento**. Nella scheda PO v5 esaminata, `document_po` confronta il documento con l’ordine; l’ordine è la base percentuale. `po_document` inverte confronto e base. Le sei direzioni consentite includono anche il valore ricevuto. Impostare esplicitamente direzione, operatore e Any/All.

Esempio: ordine 100, documento 102.02, uguaglianza al 2 %. Con riferimento all’ordine, l’intervallo è 98–102: fuori. Con riferimento al documento è 99.9796–104.0604: l’ordine 100 rientra. Il documento 102 è esattamente sul limite superiore incluso della prima direzione. Una tolleranza assoluta di 2 usa l’unità del valore confrontato.

La scheda normalizza i prezzi per unità di prezzo e usa dati di ordine o ricezione secondo la direzione. Verificare abbinamenti, quantità e unità. Any richiede un confronto corrispondente; All tutti i confronti eseguiti. **Nessuna riga confrontabile** è un errore dati in v5, non un All automaticamente soddisfatto. Contare a parte le righe non abbinate.

Nei workflow esistenti, rileggere versione, direzione e operatore salvati: le migrazioni hanno modificato impostazioni. Le vecchie etichette non bastano per il collaudo. Registrare valori, riferimento, limite, minimo superamento, precisione, ordine assente e riga non abbinata. L’esempio non sostituisce il collaudo con le proprie anagrafiche PO.

## Schede e parametri di esempio

I valori descrivono parametri delle schede, non un workflow completo importabile. Sostituire YOUR_* con selezioni proprie di test. Il designer gestisce l’ID nascosto del chiamante. Catalogo: Dev, DocFlow 2.10.38, 21 ottobre 2026; verificare versioni e abilitazioni della propria organizzazione.

### `condition_docfield_operator_docfield_tolerances` · v2

Identità: `d0472648-d1a2-499d-83e3-b47306ae130a`

| Parametro | Tipo / opzioni | Esempio |
| --- | --- | --- |
| `field_name_left` | `field_name_left:str` | `"total_amount"` |
| `operator` | `eq / neq / gt / ge / lt / le` | `"eq"` |
| `field_name_right` | `field_name_right:str` | `"expected_amount"` |
| `tolerance_amount` | `tolerance_amount` | `"2"` |
| `tolerance_type` | `percent / value` | `"percent"` |

### `condition_doc_to_po_unit_price` · v5

Identità: `ed2cd0fe-ac87-4bae-9a86-0b0576159b28`

| Parametro | Tipo / opzioni | Esempio |
| --- | --- | --- |
| `operator_any_all` | `match_any / match_all` | `"match_all"` |
| `operator` | `eq / neq / gt / ge / lt / le` | `"eq"` |
| `tolerance_amount` | `tolerance_amount` | `"2"` |
| `tolerance_type` | `percent / value` | `"percent"` |
| `comparison_data` | `po_document / received_document / po_received / document_po / document_received / received_po` | `"document_po"` |

## Casi di prova aziendali

| Caso | Input / configurazione | Risultato atteso |
| --- | --- | --- |
| PO-01 | document_po; PO=100; DOC=102; eq; 2 percent | true |
| PO-02 | document_po; PO=100; DOC=102.02; eq; 2 percent | false |
| PO-03 | po_document; PO=100; DOC=102.02; eq; 2 percent | true |
| PO-04 | compared_rows=0 | errore dati |
| PO-05 | unmatched_rows>0 | verificare separatamente la copertura |

## Prove e limiti

Parametri e comportamento sono stati confrontati con catalogo Dev e codice esaminato. I casi aziendali sono una procedura di collaudo. Per questo capitolo non sono state eseguite approvazioni personali, modifiche reali o consegne.

[Continuare il percorso](../workflow-learning-path.md) · [Kit di esercitazione](../workflow-training-kit.md)
