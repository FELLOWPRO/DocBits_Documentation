# Auto-Esportazione per Condizioni

## Cosa fa questo script?

Imposta automaticamente lo stato del documento su "pronto per l'esportazione" quando vengono soddisfatte condizioni specifiche: il fornitore e un venditore conosciuto/affidabile E l'importo della fattura e inferiore a una soglia. Questo salta la validazione manuale per le fatture a basso rischio.

## Trigger

`AFTER_FORMATTING` sul tipo di documento **INVOICE**

## Script Completo

```python
# Leggere i campi rilevanti
net = get_field_value(document_data, "net_amount", "0")
supplier = get_field_value(document_data, "supplier_name", "", is_clean=True)

try:
    net_float = float(net)
except ValueError:
    net_float = 0

# Definire i fornitori affidabili per l'auto-esportazione
auto_export_suppliers = ["OFFICEDEPOT", "STAPLES", "AMAZON"]

# Auto-esportazione per fornitori conosciuti con importi bassi
if any(s in supplier for s in auto_export_suppliers) and net_float < 500:
    doc_id = document_json["doc_id"]
    update_document_status_with_doc_id(
        doc_id, user, org_id, "ready_for_export",
        message="Auto-esportato (importo basso, fornitore conosciuto)"
    )
```

## Spiegazione Passo dopo Passo

1. **Leggere l'importo netto e il nome del fornitore** dal documento (fornitore con `is_clean=True` per il confronto)
2. **Definire i fornitori affidabili** — lista di nomi di venditori conosciuti (puliti/maiuscolo)
3. **Verificare le condizioni** — il fornitore deve essere nella lista affidabile E l'importo deve essere inferiore a 500
4. **Cambiare lo stato** a `"ready_for_export"` con un messaggio descrittivo

{% hint style="warning" %}
**Attenzione:** I cambiamenti di stato attivano workflow a valle (DocFlow, hook di esportazione). Assicurarsi che le condizioni siano sufficientemente restrittive per evitare esportazioni non volute.
{% endhint %}

## Funzioni Utilizzate

- [get\_field\_value()](../field-functions.md#get\_field\_value) — Leggere i valori dei campi
- [update\_document\_status\_with\_doc\_id()](../business-logic-functions.md#update\_document\_status\_with\_doc\_id) — Cambiare lo stato del documento
