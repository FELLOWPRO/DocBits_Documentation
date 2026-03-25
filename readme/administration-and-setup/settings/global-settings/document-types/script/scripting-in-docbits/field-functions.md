# Funzioni di Campo

Funzioni per leggere, scrivere e controllare i campi del documento.

**Sorgente:** `module/script/helper/document_script_functions.py`

---

## get\_field\_value()

Legge il valore di un campo dal documento.

```python
get_field_value(document_data, field_name, default_value=None, is_clean=False)
```

**Parametri:**

| Nome | Tipo | Descrizione |
| ---- | ---- | ----------- |
| `document_data` | `dict` | L'oggetto di contesto `document_data` |
| `field_name` | `str` | Nome del campo (es. `"invoice_id"`) |
| `default_value` | `any` | Valore restituito se il campo e vuoto/mancante (predefinito: `None`) |
| `is_clean` | `bool` | Se `True`: il valore viene convertito in MAIUSCOLO con gli spazi rimossi |

**Restituisce:** Il valore del campo come stringa, oppure `default_value`

**Esempio — Leggere il numero fattura con valore di riserva:**

```python
# Leggere il campo con valore predefinito
inv_id = get_field_value(document_data, "invoice_id", "UNKNOWN")

# Con is_clean=True: "INV 001" diventa "INV001"
inv_id = get_field_value(document_data, "invoice_id", "", is_clean=True)
```

**Cosa succede:** Restituisce il valore del campo. Quando `is_clean=True`, il valore viene trasformato tramite `value.upper().replace(" ", "").strip()` — utile per i confronti.

---

## set\_field\_value()

Imposta il valore di un campo. Crea automaticamente il campo se non esiste.

```python
set_field_value(document_data, field_name, value, remove_link=False)
```

**Parametri:**

| Nome | Tipo | Descrizione |
| ---- | ---- | ----------- |
| `document_data` | `dict` | L'oggetto di contesto `document_data` |
| `field_name` | `str` | Nome del campo |
| `value` | `any` | Nuovo valore |
| `remove_link` | `bool` | Se `True`: rimuove coords, confidence, rule, ecc. |

**Restituisce:** `True` se il valore e cambiato, `False` se identico

**Effetti collaterali:**
- Imposta `highlight_field = True` (indicatore visivo nell'interfaccia)
- Imposta `extraction_method = "SCRIPT"`
- Imposta `formatted_value = value`

**Esempio — Assegnazione condizionale del valore:**

```python
# Impostare l'ID fattura
set_field_value(document_data, "invoice_id", "INV-2026-001")

# Con remove_link: rimuove il collegamento OCR (coords, confidence ecc.)
set_field_value(document_data, "custom_field", "Calculated", remove_link=True)
```

**Cosa succede:** Il valore del campo viene aggiornato e contrassegnato come modificato dallo script. Se il campo non esiste, viene creato automaticamente con `extraction_method: "SCRIPT"` e aggiunto sia a `fields` che a `fields_dict`.

---

## set\_date\_value()

Imposta un valore data con formattazione automatica e aritmetica delle date opzionale.

```python
set_date_value(document_data, field_name, value, add_days=0, skip_weekend=False,
               remove_link=False, exclude_final_days=None)
```

**Parametri:**

| Nome | Tipo | Descrizione |
| ---- | ---- | ----------- |
| `value` | `str` | Data ISO: `"2026-03-25"`. Se vuoto: data odierna |
| `add_days` | `int` | Giorni da aggiungere (es. `30` per termini di pagamento) |
| `skip_weekend` | `bool` | Salta i fine settimana quando si aggiungono giorni |
| `exclude_final_days` | `str/list` | Giorni aggiuntivi da escludere (es. `"MONDAY,FRIDAY"`) |

**Esempio — Calcolare la data di scadenza del pagamento (30 giorni, senza fine settimana):**

```python
# Data di scadenza: 30 giorni dopo la data fattura, salta i fine settimana
inv_date = get_field_value(document_data, "invoice_date")
set_date_value(document_data, "due_date", inv_date,
               add_days=30, skip_weekend=True)

# Impostare la data di consegna a oggi
set_date_value(document_data, "delivery_date", None)  # None = oggi

# 14 giorni, escludendo sabato e lunedi
set_date_value(document_data, "delivery_date", "2026-04-01",
               add_days=14, skip_weekend=True, exclude_final_days="MONDAY")
```

**Cosa succede:** La data viene calcolata aggiungendo giorni (opzionalmente saltando fine settimana/giorni specifici) e formattata automaticamente secondo il `date_format_pattern` del documento (es. `%d.%m.%Y` per la Germania).

**Codici giorno per `exclude_final_days`:**
`MONDAY`, `TUESDAY`, `WEDNESDAY`, `THURSDAY`, `FRIDAY`, `SATURDAY`, `SUNDAY`

---

## set\_amount\_value()

Imposta un valore importo con formattazione automatica della localizzazione.

```python
set_amount_value(document_data, field_name, value, remove_link=False)
```

**Parametri:**

| Nome | Tipo | Descrizione |
| ---- | ---- | ----------- |
| `value` | `str/number` | Importo in formato inglese (es. `"1234.56"`) |

**Esempio — Impostare l'importo netto:**

```python
set_amount_value(document_data, "net_amount", "1234.56")
# formatted_value diventa ad es. "1.234,56" per la localizzazione de_DE
```

**Cosa succede:** L'importo viene formattato secondo `amount_format_locale` da `document_json` (es. `de_DE`, `en_US`).

---

## create\_new\_field()

Crea un nuovo dizionario campo (senza aggiungerlo al documento).

```python
create_new_field(field_name, value="")
```

**Restituisce:** Dict con `name`, `value`, `formatted_value`, `extraction_method: "SCRIPT"`

**Esempio:**

```python
new_field = create_new_field("custom_reference", "REF-001")
document_json["fields"].append(new_field)
fields_dict["custom_reference"] = new_field
```

{% hint style="success" %}
**Alternativa piu semplice:** Usa `set_field_value()` — crea automaticamente il campo se non esiste. `create_new_field()` e necessario solo quando si vuole manipolare manualmente il dizionario del campo.
{% endhint %}

---

## delete\_field()

Rimuove un campo dal documento.

```python
delete_field(document_data, field_name)
```

**Restituisce:** Tupla `(doc_json, fields_dict)` dopo l'eliminazione

**Esempio:**

```python
delete_field(document_data, "unnecessary_field")
```

---

## set\_field\_as\_invalid()

Contrassegna un campo come non valido con un messaggio di errore.

```python
set_field_as_invalid(document_data, field_name, message, code=None)
```

**Parametri:**

| Nome | Tipo | Descrizione |
| ---- | ---- | ----------- |
| `message` | `str` | Messaggio di errore (visualizzato nell'interfaccia) |
| `code` | `str` | Codice di errore (predefinito: `INVALID_VALUE`) |

**Effetti collaterali:**
- `is_valid = False`
- `invalidated_by_script = True`
- `highlight_field = True`
- `validation_message = message`
- `validation_code = code`

**Esempio — Validazione IBAN:**

```python
iban = get_field_value(document_data, "iban", "")
if len(iban) < 15:
    set_field_as_invalid(document_data, "iban",
                         "L'IBAN deve essere di almeno 15 caratteri",
                         "IBAN_TOO_SHORT")
```

**Cosa succede:** Il campo viene evidenziato in rosso nella schermata di validazione con il messaggio di errore visualizzato all'utente.

---

## set\_field\_as\_valid()

Rimuove lo stato di non validita da un campo.

```python
set_field_as_valid(document_data, field_name, message, code=None)
```

**Esempio:**

```python
set_field_as_valid(document_data, "iban", "IBAN valido")
```

**Cosa succede:** Rimuove `invalidated_by_script`, `validation_message`, `validation_code` e imposta `is_valid = True`.

---

## set\_field\_attribute()

Imposta un attributo arbitrario su un campo.

```python
set_field_attribute(document_data, field_name, attribute_name, value)
```

**Esempio:**

```python
set_field_attribute(document_data, "invoice_id", "highlight_field", True)
set_field_attribute(document_data, "supplier_name", "custom_flag", "reviewed")
```

Vedi l'elenco completo degli [Attributi Supportati](#attributi-supportati) qui sotto.

---

## set\_is\_required()

Rende un campo obbligatorio o rimuove il requisito.

```python
set_is_required(document_data, field_name, value)
```

**Esempio — Numero OA obbligatorio per fatture di acquisto:**

```python
doc_type_detail = get_field_value(document_data, "document_type_detail", "")
if doc_type_detail == "PURCHASE_INVOICE":
    set_is_required(document_data, "purchase_order", True)
else:
    set_is_required(document_data, "purchase_order", False)
```

---

## set\_is\_readonly()

Rende un campo di sola lettura o modificabile.

```python
set_is_readonly(document_data, field_name, value)
```

**Parametri:**

| Nome | Tipo | Descrizione |
| ---- | ---- | ----------- |
| `value` | `bool/None` | `True` = sola lettura, `False` = modificabile, `None` = rimuovi attributo |

**Esempio:**

```python
set_is_readonly(document_data, "total_amount", True)
```

---

## set\_is\_hidden()

Nasconde o mostra un campo nell'interfaccia.

```python
set_is_hidden(document_data, field_name, value)
```

**Esempio — Mostrare i campi sotto-organizzazione solo quando pertinenti:**

```python
if not document_json.get("sub_org_id"):
    set_is_hidden(document_data, "sub_org_reference", True)
```

---

## set\_force\_validation()

Forza la validazione manuale per un campo.

```python
set_force_validation(document_data, field_name, value, reset_validation=False)
```

**Parametri:**

| Nome | Tipo | Descrizione |
| ---- | ---- | ----------- |
| `value` | `bool` | `True` = forza validazione, `False` = rimuovi |
| `reset_validation` | `bool` | Se `True`: reimposta `is_validated` a `False` |

**Effetti collaterali quando `value=True`:**
- `force_validation = True`
- `is_valid = False` (se non ancora validato)
- `validation_code = "FORCED_VALIDATION"`

**Esempio — Forzare la validazione per importi elevati:**

```python
amount = get_field_value(document_data, "total_amount", "0")
try:
    if float(amount) > 10000:
        set_force_validation(document_data, "total_amount", True)
except ValueError:
    pass
```

---

## Attributi Supportati

### Attributi Campo Principali

| Attributo | Tipo | Descrizione |
| --------- | ---- | ----------- |
| `value` | any | Il valore grezzo del campo |
| `formatted_value` | string | Valore formattato per la visualizzazione |
| `content` | string | Contenuto estratto originale |
| `is_required` | bool | Se il campo e obbligatorio |
| `is_valid` | bool | Stato di validazione |
| `is_validated` | bool | Se il campo e stato validato dall'utente |
| `is_readonly` | bool | Se il campo e di sola lettura |
| `is_hidden` | bool | Se il campo e nascosto nell'interfaccia |
| `force_validation` | bool | Forza l'utente a validare questo campo |
| `highlight_field` | bool | Evidenzia il campo nell'interfaccia |
| `extraction_method` | string | Come e stato estratto il valore (es. `"SCRIPT"`) |

### Attributi di Validazione

| Attributo | Tipo | Descrizione |
| --------- | ---- | ----------- |
| `validation_message` | string | Messaggio di errore mostrato all'utente |
| `validation_code` | string | Codice di errore (es. `"FORCED_VALIDATION"`, `"INVALID_VALUE"`) |
| `invalidated_by_script` | bool | Contrassegna il campo come invalidato dallo script |

### Attributi di Estrazione/OCR

| Attributo | Tipo | Descrizione |
| --------- | ---- | ----------- |
| `coords` | object | Coordinate del riquadro di delimitazione sul documento |
| `confidence` | float | Punteggio di confidenza OCR/estrazione |
| `score` | float | Punteggio di corrispondenza/validazione |
| `score_description` | string | Descrizione del punteggio |
| `page` | int | Numero di pagina dove e stato trovato il campo |
| `rule` | string | Regola di estrazione applicata |
