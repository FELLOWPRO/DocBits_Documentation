# Calcolo della Data di Scadenza

## Cosa fa questo script?

Calcola la data di scadenza del pagamento basandosi sulla data della fattura, aggiungendo un numero configurabile di giorni (es. 30). I fine settimana vengono automaticamente saltati in modo che la data di scadenza cada sempre in un giorno lavorativo.

## Trigger

`AFTER_FORMATTING` sul tipo di documento **INVOICE**

## Script Completo

```python
# Leggere la data della fattura
inv_date = get_field_value(document_data, "invoice_date")

if inv_date:
    # Calcolare la data di scadenza: 30 giorni dopo la data fattura, salta i fine settimana
    set_date_value(document_data, "due_date", inv_date,
                   add_days=30, skip_weekend=True)

    # Impostare anche la data contabile = data fattura
    set_date_value(document_data, "accounting_date", inv_date)
```

## Variazioni

### 14 giorni, escludendo i lunedi

```python
set_date_value(document_data, "due_date", inv_date,
               add_days=14, skip_weekend=True, exclude_final_days="MONDAY")
```

### 60 giorni, senza salto dei fine settimana

```python
set_date_value(document_data, "due_date", inv_date, add_days=60)
```

### Impostare la data di consegna a oggi

```python
set_date_value(document_data, "delivery_date", None)  # None = oggi
```

## Spiegazione Passo dopo Passo

1. **Leggere la data della fattura** dal documento
2. **Calcolare la data di scadenza** usando `set_date_value()` con `add_days=30` e `skip_weekend=True`
3. **La formattazione della data** e automatica — usa il `date_format_pattern` del documento (es. `%d.%m.%Y`)
4. **Il salto dei fine settimana** assicura che la data di scadenza cada dal lunedi al venerdi

## Codici Giorno per `exclude_final_days`

`MONDAY`, `TUESDAY`, `WEDNESDAY`, `THURSDAY`, `FRIDAY`, `SATURDAY`, `SUNDAY`

## Funzioni Utilizzate

- [get\_field\_value()](../field-functions.md#get\_field\_value) — Leggere la data della fattura
- [set\_date\_value()](../field-functions.md#set\_date\_value) — Calcolare e impostare la data di scadenza
