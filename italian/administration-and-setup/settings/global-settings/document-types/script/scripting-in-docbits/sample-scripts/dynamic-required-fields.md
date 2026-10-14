# Campi Obbligatori Dinamici

## Cosa fa questo script?

Imposta dinamicamente i requisiti dei campi in base al contenuto del documento. In questo esempio: quando la valuta della fattura non e EUR, il campo del tasso di cambio diventa obbligatorio e visibile. Per le fatture in EUR, il campo del tasso di cambio e nascosto e opzionale.

## Trigger

`ON_FIELD_CHANGE` sul tipo di documento **INVOICE**

## Script Completo

```python
# Leggere la valuta corrente
currency = get_field_value(document_data, "currency", "EUR")

# Valuta estera: il tasso di cambio e obbligatorio e visibile
if currency and currency != "EUR":
    set_is_required(document_data, "exchange_rate", True)
    set_is_hidden(document_data, "exchange_rate", False)
else:
    # EUR: il tasso di cambio e opzionale e nascosto
    set_is_required(document_data, "exchange_rate", False)
    set_is_hidden(document_data, "exchange_rate", True)
```

## Variazione: Fattura di acquisto vs. fattura di costo

```python
po = get_field_value(document_data, "purchase_order", "")

if po and po.strip():
    # Fattura di acquisto: il numero OA e obbligatorio
    set_field_value(document_data, "invoice_category", "PURCHASE_INVOICE")
    set_is_required(document_data, "purchase_order", True)
else:
    # Fattura di costo: il numero OA non e necessario, nascondere la tabella
    set_field_value(document_data, "invoice_category", "COST_INVOICE")
    set_is_required(document_data, "purchase_order", False)
    delete_tables(document_data)
```

## Spiegazione Passo dopo Passo

1. **Leggere il campo di controllo** (la valuta in questo caso)
2. **Applicare le regole aziendali** — requisiti di campo diversi in base al valore
3. **Impostare la visibilita** — nascondere i campi irrilevanti per mantenere l'interfaccia pulita
4. **Impostare i requisiti** — rendere obbligatori i campi pertinenti

{% hint style="info" %}
**Scelta del trigger:** `ON_FIELD_CHANGE` viene eseguito ogni volta che un utente modifica un campo, quindi i requisiti si aggiornano in tempo reale. `AFTER_FORMATTING` viene eseguito solo una volta dopo l'estrazione iniziale.
{% endhint %}

## Funzioni Utilizzate

- [get\_field\_value()](../field-functions.md#get\_field\_value) — Leggere il campo di controllo
- [set\_is\_required()](../field-functions.md#set\_is\_required) — Impostare il campo come obbligatorio/opzionale
- [set\_is\_hidden()](../field-functions.md#set\_is\_hidden) — Mostrare/nascondere i campi
- [set\_field\_value()](../field-functions.md#set\_field\_value) — Impostare il campo categoria
- [delete\_tables()](../table-functions.md#delete\_tables) — Rimuovere le tabelle per le fatture di costo
