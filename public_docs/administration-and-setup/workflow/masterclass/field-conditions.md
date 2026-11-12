---
description: "Scegliere Field is, Docfield is o Compare two Fields"
---

# P1: scegliere Field is, Docfield is o Compare two Fields

Tre schede di condizione si somigliano nel designer, e la loro differenza decide che cosa una regola può davvero intercettare. Questa pagina aiuta a scegliere quella giusta e poi propone tre brevi esercizi che mostrano che cosa restituisce ciascuna scheda. Alla fine saprete distinguere «vuoto» da «zero», «falso» da «assente» e una condizione non soddisfatta da un errore.

Eseguite gli esercizi in Advanced Test, nella vostra organizzazione di test, con un documento sintetico. Qui non viene toccato alcun documento del cliente.

## Quale scheda serve?

| Se volete verificare... | Usate | Scheda e versione |
| --- | --- | --- |
| se un campo contiene un valore qualsiasi | **Field is** | `condition_docfield_status` v2 |
| un campo rispetto a un valore che inserite voi | **Docfield is** | `condition_docfield_operator_value` v2 |
| due campi dello stesso documento uno rispetto all’altro | **Compare two Fields** | `condition_compare_two_docfield_values` v2 |

Tutte e tre sono condizioni: restituiscono un risultato e non modificano nulla sul documento. Un controllo dello stato vuoto non dimostra che un campo esista nel layout né che il suo contenuto sia valido per l’azienda. Le pagine delle singole schede elencano ogni impostazione: [Field is](../and/document-field/field-is.md), [Docfield is](../and/document-field/docfield-is.md) e [Compare two Fields](../and/document-field/compare-two-fields.md).

## Esercizio 1: scoprire che cosa significa «vuoto»

**Obiettivo:** sapere quali valori Field is versione 2 considera vuoti.

1. Aggiungete **Field is** versione 2 a una regola della vostra organizzazione di test e scegliete un campo di testo del layout.
2. Impostate lo stato del campo su `field_empty` (Empty or missing).
3. Eseguite otto casi Advanced Test con dati di documento completi: campo assente, `null`, testo vuoto `""`, solo spazi `" "`, booleano `false`, numero `0`, testo `"0"` e testo `"false"`.

**Fatto quando:** i primi cinque casi restituiscono `field_empty=success` e gli ultimi tre `field_empty=failed_condition`. Questi otto casi sono stati provati in Dev con dati di documento completi.

Il numero `0`, il testo `"0"` e il testo `"false"` sono valori, non assenze. Se la vostra decisione aziendale è vero o falso, usate una condizione con casella di controllo esplicita invece di verificare il campo come vuoto.

## Esercizio 2: confrontare un campo con un valore

**Obiettivo:** vedere come operatore e tipo di campo cambiano la risposta.

1. Scegliete un campo numerico come `total_amount`, l’operatore `gt` e il valore `1000`.
2. Provate `1000`, `1000.01`, un campo assente e un valore non valido.

**Fatto quando:** `1000` restituisce `failed_condition`, perché `gt` significa strettamente maggiore, `1000.01` restituisce `success` e un input assente o non valido restituisce `error`.

## Esercizio 3: confrontare due campi

**Obiettivo:** sapere quando due valori vengono confrontati e quando la scheda non può confrontarli affatto.

1. Impostate campo sinistro, operatore e campo destro. Usate due campi con tipi compatibili.
2. Provate valori uguali, valori diversi e un input assente.

**Fatto quando:** valori uguali soddisfano `eq`, valori diversi restituiscono `failed_condition` e un input assente restituisce `error` invece di una disuguaglianza dimostrata.

## Che cosa significano i tre risultati

| Risultato | Che cosa vi dice |
| --- | --- |
| `success` | La scheda ha confrontato i valori e la condizione era soddisfatta. |
| `failed_condition` | La scheda ha confrontato i valori e la condizione non era soddisfatta. `0` e `"0"` finiscono qui in un controllo dello stato vuoto. |
| `error` | La scheda non ha potuto confrontare, per esempio perché un valore manca o non è valido. Un errore non è la stessa risposta di «diverso». |

## Il tipo fa parte del confronto

Un valore `"1000.01"` in un campo AMOUNT non è lo stesso dei medesimi caratteri in un campo di testo. Il kit di esercizi v2 usa AMOUNT e punti decimali nel JSON. Controllate insieme la chiave tecnica del campo, il layout e il tipo. Un’etichetta tradotta non è una chiave tecnica e un simbolo di valuta non è un valore numerico.

## Schede e parametri di esempio

Questi valori descrivono parametri di singole schede, non un workflow completo importabile. Sostituite YOUR\_\* con le vostre scelte di test. L’ID nascosto del chiamante è gestito dal designer. Catalogo: Dev, DocFlow 2.10.38, 21 ottobre 2026; verificate versioni disponibili e autorizzazioni nella vostra organizzazione.

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
| FIELD-01 | missing / null / "" / " " / false | field\_empty=success |
| FIELD-02 | 0 / "0" / "false" | field\_empty=failed\_condition |
| FIELD-03 | AMOUNT 1000; gt 1000 | failed\_condition |
| FIELD-04 | AMOUNT 1000.01; gt 1000 | success |
| FIELD-05 | AMOUNT missing / invalid; gt 1000 | error |

## Prove e limiti

Alcuni risultati di schede e nodi sono stati verificati con dati sintetici in Advanced Test. Le risposte sono nel kit di esercizi. Le azioni sul documento sono simulate; questi test non dimostrano un’esecuzione del documento salvata né una consegna esterna.

[Continuare il percorso](../workflow-learning-path.md) · [Kit di esercitazione](../workflow-training-kit.md)
