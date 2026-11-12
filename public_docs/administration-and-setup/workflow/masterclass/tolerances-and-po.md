---
description: "Definire riferimento delle tolleranze e confronto PO"
---

# P1: definire riferimento delle tolleranze e confronto PO

Una tolleranza del 2 per cento non è un importo fisso. È il 2 per cento del lato con cui confrontate, quindi la stessa riga di fattura può fallire in una direzione e passare nell’altra. Questa pagina lo mostra su una coppia di valori, vi dà tre esercizi per riprodurlo e poi elenca le sei direzioni di confronto e i parametri di scheda che potete copiare nel vostro test.

Eseguite gli esercizi in Advanced Test, nella vostra organizzazione di test, con un documento sintetico e un ordine abbinato.

## Il lato di riferimento è la base

Nella scheda PO versione 5 esaminata, `document_po` confronta il valore del documento con quello dell’ordine, quindi l’ordine è la base di una tolleranza percentuale. `po_document` inverte sia il confronto sia la base. Le sei direzioni consentite includono anche il lato ricevuto. Impostate direzione, operatore e Any/All in modo esplicito, invece di affidarvi a ciò che una scheda salvata contiene ancora.

## Esercizio 1: stessi valori, due direzioni

**Obiettivo:** vedere due risultati diversi uscire dagli stessi numeri.

1. Preparate un ordine abbinato da `100` e un prezzo unitario di documento di `102.02`.
2. Confrontate con l’operatore `eq` e una tolleranza di `2` per cento, prima con `document_po`. Aspettatevi `false`: il 2 per cento di 100 è 2, quindi l’intervallo chiuso va da 98 a 102 e 102.02 sta 0.02 sopra.
3. Ripetete lo stesso caso con `po_document`. Aspettatevi `true`: il 2 per cento di 102.02 è 2.0404, l’intervallo va da 99.9796 a 104.0604 e il valore d’ordine 100 cade dentro.

**Fatto quando:** entrambi i risultati ed entrambi gli intervalli sono annotati e sapete dire da quale valore è stata calcolata la percentuale in ciascuna direzione.

Una tolleranza assoluta di `2` si comporta diversamente: usa l’unità del valore confrontato e non si sposta con il riferimento.

## Esercizio 2: trovare il confine esatto

**Obiettivo:** sapere se il bordo dell’intervallo conta.

1. Mantenete `document_po`, `eq` e la tolleranza del 2 per cento e portate il valore del documento a `102`.
2. Eseguite il caso, poi ripetetelo con `102.01`.

**Fatto quando:** `102` restituisce `true` e `102.01` restituisce `false`. Il limite è incluso: 102 sta esattamente sul bordo superiore dell’intervallo da 98 a 102.

## Esercizio 3: Any, All e le righe confrontate

**Obiettivo:** sapere che cosa fa la scheda con più righe e che cosa succede quando non c’è nulla da confrontare.

1. Costruite un documento con due righe sullo stesso ordine abbinato: una dentro la tolleranza e una fuori.
2. Eseguite la scheda con `match_any`, poi con `match_all`.
3. Eseguite un documento che non ha alcuna riga confrontabile.

**Fatto quando:** `match_any` passa sull’unica riga corrispondente, `match_all` fallisce appena un confronto fallisce e il documento senza riga confrontabile restituisce un errore dati. Nella versione 5 è un errore, non un All soddisfatto automaticamente.

## Quale lato è la base?

| Opzione salvata | Lato confrontato | Lato di riferimento (base percentuale) |
| --- | --- | --- |
| `po_document` | Ordine | Documento |
| `received_document` | Dati ricevuti | Documento |
| `po_received` | Ordine | Dati ricevuti |
| `document_po` | Documento | Ordine |
| `document_received` | Documento | Dati ricevuti |
| `received_po` | Dati ricevuti | Ordine |

## Controllate prima di fidarvi di un workflow esistente

La scheda normalizza i prezzi per unità di prezzo e usa i dati d’ordine o di ricezione secondo la direzione: controllate quindi prima abbinamento, quantità e unità. Any ha bisogno di un confronto corrispondente; All di tutti i confronti realmente eseguiti. Le righe non abbinate si rilevano a parte.

Sui workflow esistenti rileggete versione salvata, direzione e operatore: le migrazioni hanno modificato le impostazioni di confronto, quindi le etichette storiche non bastano come prova di collaudo. Annotate valori e riferimento, confine esatto, superamento minimo, precisione di arrotondamento, ordine mancante e riga non abbinata. Questo calcolo non sostituisce il collaudo con i vostri dati anagrafici PO.

## Schede e parametri di esempio

Questi valori descrivono parametri di singole schede, non un workflow completo importabile. Sostituite YOUR\_\* con le vostre scelte di test. L’ID nascosto del chiamante è gestito dal designer. Catalogo: Dev, DocFlow 2.10.38, 21 ottobre 2026; verificate versioni disponibili e autorizzazioni nella vostra organizzazione.

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
| PO-01 | document\_po; PO=100; DOC=102; eq; 2 percent | true |
| PO-02 | document\_po; PO=100; DOC=102.02; eq; 2 percent | false |
| PO-03 | po\_document; PO=100; DOC=102.02; eq; 2 percent | true |
| PO-04 | compared\_rows=0 | errore dati |
| PO-05 | unmatched\_rows>0 | verificare la copertura a parte |

## Prove e limiti

Parametri e comportamento sono stati verificati contro il catalogo Dev e la revisione del codice esaminata. I casi di prova aziendali sono una procedura di collaudo. Per questo capitolo non sono state eseguite approvazioni personali, modifiche a dati reali né consegne.

[Continuare il percorso](../workflow-learning-path.md) · [Kit di esercitazione](../workflow-training-kit.md)
