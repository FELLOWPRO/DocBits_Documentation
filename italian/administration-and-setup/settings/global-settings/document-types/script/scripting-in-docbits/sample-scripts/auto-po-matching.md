# Corrispondenza Automatica OA

## Cosa fa questo script?

Attiva automaticamente l'abbinamento OA (Ordine di Acquisto) quando un numero OA e presente sulla fattura. Il microservizio po-match-service confronta le voci della fattura con l'OA e popola i risultati dell'abbinamento.

## Trigger

`AFTER_FORMATTING` sul tipo di documento **INVOICE**

## Script Completo

```python
# Leggere il numero OA dal documento
po_nr = get_field_value(document_data, "purchase_order", "")

if po_nr:
    # Pulire il numero OA: rimuovere prefisso e spazi
    po_nr = po_nr.strip()
    if po_nr.upper().startswith("PO"):
        po_nr = po_nr[2:].strip()
    if po_nr.startswith("-") or po_nr.startswith(" "):
        po_nr = po_nr[1:].strip()

    # Aggiornare il numero OA pulito
    set_field_value(document_data, "purchase_order", po_nr)

    # Attivare l'abbinamento automatico OA
    auto_po_match_for_purchase_orders(user, document_data, po_nr)
```

## Spiegazione Passo dopo Passo

1. **Leggere il numero OA** dalla fattura
2. **Pulire** il numero OA rimuovendo prefissi comuni come "PO-" o "PO "
3. **Aggiornare** il numero OA pulito nel documento
4. **Attivare l'abbinamento OA** che chiama il po-match-service per confrontare le righe della fattura con le righe dell'OA

## Cosa succede dopo l'abbinamento?

Il `document_data` viene aggiornato con:
- `po_items` — Voci OA abbinate
- `po_match_status` — Risultato dell'abbinamento (`"matched"`, `"partially_matched"`, ecc.)
- `po_multi_matched` — Se sono stati abbinati piu OA

## Funzioni Utilizzate

- [get\_field\_value()](../field-functions.md#get\_field\_value) — Leggere il valore del campo
- [set\_field\_value()](../field-functions.md#set\_field\_value) — Scrivere il numero OA pulito
- [auto\_po\_match\_for\_purchase\_orders()](../business-logic-functions.md#auto\_po\_match\_for\_purchase\_orders) — Attivare l'abbinamento OA
