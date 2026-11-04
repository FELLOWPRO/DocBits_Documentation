# Validazione Fornitore tramite Lookup

## Cosa fa questo script?

Valida il numero fornitore dalla fattura rispetto ai dati master nella tabella di ricerca. Se il fornitore viene trovato, il nome e i termini di pagamento vengono compilati automaticamente. Se non viene trovato, il campo viene contrassegnato come non valido in modo che l'utente possa correggerlo.

## Trigger

`AFTER_FORMATTING` sul tipo di documento **INVOICE**

## Script Completo

```python
# Leggere l'ID fornitore dal documento
supplier_id = get_field_value(document_data, "supplier_id", "")

if supplier_id:
    # Interrogare la tabella di ricerca fornitori
    records = get_lookup_records(
        org_id,                                    # Organizzazione corrente
        document_json.get("sub_org_id"),           # Sotto-org (se applicabile)
        "supplier",                                # Nome tabella di ricerca
        [["VENDOR_ID", supplier_id]],              # Filtro: corrispondenza esatta su VENDOR_ID
        limit=1                                    # Serve solo la prima corrispondenza
    )

    if records:
        # Fornitore trovato — compilare automaticamente i campi correlati
        supplier = records[0]
        set_field_value(document_data, "supplier_name", supplier.get("NAME", ""))
        set_field_value(document_data, "payment_terms", supplier.get("PAYMENT_TERMS", ""))
    else:
        # Fornitore non trovato — contrassegnare come non valido
        set_field_as_invalid(document_data, "supplier_id",
                             f"Fornitore '{supplier_id}' non trovato nei dati master")
```

## Spiegazione Passo dopo Passo

1. **Leggere l'ID fornitore** dal documento usando `get_field_value()`
2. **Interrogare la tabella di ricerca** con `get_lookup_records()` usando l'ID venditore come filtro
3. **In caso di corrispondenza**: Compilare automaticamente il nome fornitore e i termini di pagamento dai dati master
4. **In caso di nessuna corrispondenza**: Contrassegnare il campo ID fornitore come non valido con un messaggio di errore descrittivo

## Funzioni Utilizzate

- [get\_field\_value()](../field-functions.md#get\_field\_value) — Leggere il valore del campo
- [get\_lookup\_records()](../business-logic-functions.md#get\_lookup\_records) — Interrogare i dati master
- [set\_field\_value()](../field-functions.md#set\_field\_value) — Scrivere il valore del campo
- [set\_field\_as\_invalid()](../field-functions.md#set\_field\_as\_invalid) — Mostrare errore di validazione
