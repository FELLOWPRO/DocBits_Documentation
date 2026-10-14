# Funzioni di Logica Aziendale

Funzioni per ricerche, abbinamento OA, attivita, gestione utenti/gruppi e cambiamenti di stato.

**Sorgente:** `module/script/helper/document_script_functions.py`

---

## get\_lookup\_records()

Interroga i dati master dalle tabelle di ricerca (fornitori, articoli, conti contabili, ecc.).

```python
get_lookup_records(org_id, sub_org_id, lookup_name, filters, **kwargs)
```

**Parametri:**

| Nome | Tipo | Descrizione |
| ---- | ---- | ----------- |
| `org_id` | `str` | UUID dell'organizzazione |
| `sub_org_id` | `str/None` | UUID della sotto-organizzazione (o `None`) |
| `lookup_name` | `str` | Nome della ricerca (es. `"supplier"`, `"item"`, `"gl_account"`) |
| `filters` | `list` | Condizioni di filtro (vedi formati sotto) |
| `skip` | `int` | Offset per la paginazione (predefinito: 0) |
| `limit` | `int` | Risultati massimi (predefinito: 100) |
| `match_all` | `bool` | `True` = AND, `False` = OR (predefinito: `True`) |
| `sort_order` | `list` | Ordinamento (opzionale) |

### Formati di Filtro

Sono supportati tre formati:

```python
# Formato 1: Dict con field/operator/value
filters = [
    {"field": "VENDOR_ID", "operator": "exact", "value": "V001"},
    {"field": "NAME", "operator": "contains", "value": "ACME"},
]

# Formato 2: Tupla/Lista con 2 elementi (field, value) → operator = "exact"
filters = [
    ["VENDOR_ID", "V001"],
    ["CITY", "Munich"],
]

# Formato 3: Tupla/Lista con 3 elementi (field, operator, value)
filters = [
    ["VENDOR_ID", "exact", "V001"],
    ["NAME", "contains", "ACME"],
]
```

### Ordinamento

```python
# Formato 1: Dict
sort_order = [{"field": "NAME", "direction": "asc"}]

# Formato 2: Tupla/Lista
sort_order = [["NAME", "asc"], ["VENDOR_ID", "desc"]]
```

**Esempio — Ricerca fornitore per ID venditore:**

```python
# Trovare il fornitore per ID venditore
supplier_id = get_field_value(document_data, "supplier_id", "")
records = get_lookup_records(
    org_id, None, "supplier",
    [["VENDOR_ID", supplier_id]],
)
if records:
    supplier = records[0]
    set_field_value(document_data, "supplier_name", supplier.get("NAME", ""))
```

**Esempio — Cercare conti contabili con filtri multipli:**

```python
records = get_lookup_records(
    org_id, document_json.get("sub_org_id"), "gl_account",
    [
        {"field": "ACCOUNT_TYPE", "operator": "exact", "value": "EXPENSE"},
        {"field": "IS_ACTIVE", "operator": "exact", "value": "true"},
    ],
    limit=50,
    sort_order=[["ACCOUNT_NUMBER", "asc"]],
)
```

{% hint style="info" %}
Internamente utilizza `search_operator="SMART"` che supporta la corrispondenza approssimativa.
{% endhint %}

---

## is\_supplier\_valid()

Verifica se un fornitore esiste nei dati di ricerca.

```python
is_supplier_valid(user, filter_data_json, sub_org_id=None)
```

**Parametri:**

| Nome | Tipo | Descrizione |
| ---- | ---- | ----------- |
| `user` | `UserAuthentication` | L'oggetto di contesto `user` |
| `filter_data_json` | `dict` | Filtro nel formato `{"match_all": True, "filters": [...]}` |
| `sub_org_id` | `str/None` | Sotto-organizzazione |

**Restituisce:** `True` se almeno 1 corrispondenza, altrimenti `False`

**Esempio — Validare il fornitore:**

```python
supplier_id = get_field_value(document_data, "supplier_id", "")
is_valid = is_supplier_valid(user, {
    "match_all": True,
    "filters": [{"field": "VENDOR_ID", "operator": "exact", "value": supplier_id}]
})
if not is_valid:
    set_field_as_invalid(document_data, "supplier_id", "Fornitore non trovato nei dati master")
```

---

## auto\_po\_match\_for\_purchase\_orders()

Attiva l'abbinamento automatico OA tramite il microservizio po-match-service.

```python
auto_po_match_for_purchase_orders(user, document_data, po_numbers)
```

**Parametri:**

| Nome | Tipo | Descrizione |
| ---- | ---- | ----------- |
| `user` | `UserAuthentication` | Deve essere un oggetto utente reale |
| `document_data` | `dict` | Contesto del documento |
| `po_numbers` | `str/list` | Numeri OA (separati da virgola o lista) |

**Restituisce:** `document_data` aggiornato con `po_items`, `po_match_status`, `po_multi_matched`

**Esempio — Abbinamento automatico OA:**

```python
po_nr = get_field_value(document_data, "purchase_order", "")
if po_nr:
    auto_po_match_for_purchase_orders(user, document_data, po_nr)
```

{% hint style="warning" %}
**Protezione dai duplicati:** I numeri OA gia verificati sono memorizzati in `already_verified_po_numbers` e non verranno abbinati di nuovo.
{% endhint %}

---

## get\_next\_sequence\_number()

Ottiene e incrementa atomicamente un numero di sequenza nel database.

```python
get_next_sequence_number(org_id, sequence_name, default_value=1)
```

**Parametri:**

| Nome | Tipo | Descrizione |
| ---- | ---- | ----------- |
| `org_id` | `str` | UUID dell'organizzazione |
| `sequence_name` | `str` | Deve contenere `"sequence"` (es. `"invoice_sequence"`) |
| `default_value` | `int` | Valore iniziale quando la sequenza viene creata |

**Restituisce:** `int` — il numero successivo, oppure `None` se il nome non e valido

**Esempio — Generare un numero documento interno:**

```python
seq_nr = get_next_sequence_number(org_id, "invoice_sequence", 1000)
set_field_value(document_data, "internal_number", str(seq_nr))
```

{% hint style="danger" %}
**Regola di denominazione:** Il `sequence_name` deve iniziare o terminare con "sequence", o contenere "SEQUENCE\_". Altrimenti la funzione restituisce `None`.
{% endhint %}

---

## create\_document\_task()

Crea un'attivita per il documento corrente.

```python
create_document_task(user, document_data, title, description, priority,
                     assigned_to_user_id, assigned_to_group_id, send_email)
```

**Parametri:**

| Nome | Tipo | Descrizione |
| ---- | ---- | ----------- |
| `user` | `UserAuthentication` | Contesto utente |
| `title` | `str` | Titolo dell'attivita |
| `description` | `str` | Descrizione |
| `priority` | `str/int` | Priorita |
| `assigned_to_user_id` | `str/None` | Utente assegnato |
| `assigned_to_group_id` | `str/None` | Gruppo assegnato |
| `send_email` | `bool` | Inviare notifica email |

**Esempio — Creare un'attivita per fatture con importo elevato:**

```python
amount = float(get_field_value(document_data, "total_amount", "0"))
if amount > 50000:
    create_document_task(
        user, document_data,
        title="Importo fattura elevato - revisione necessaria",
        description=f"Importo fattura: {amount} supera la soglia di 50.000",
        priority="HIGH",
        assigned_to_user_id=None,
        assigned_to_group_id="uuid-of-finance-group",
        send_email=True
    )
```

---

## set\_document\_sub\_org\_id()

Assegna una sotto-organizzazione a un documento.

```python
set_document_sub_org_id(document_data, sub_org_id)
```

**Effetti collaterali:**
- Imposta `sub_org_id` in `document_json`
- Salva direttamente nel database (se `doc_id` e presente)

**Esempio — Instradamento basato sul fornitore:**

```python
supplier = get_field_value(document_data, "supplier_name", "", is_clean=True)
sub_org_map = {
    "ACMECORP": "uuid-acme-sub-org",
    "WIDGETSINC": "uuid-widgets-sub-org",
}
for key, sub_org in sub_org_map.items():
    if key in supplier:
        set_document_sub_org_id(document_data, sub_org)
        break
```

---

## update\_document\_status\_with\_doc\_id()

Cambia lo stato di un documento.

```python
update_document_status_with_doc_id(doc_id, user, org_id, status, message=None,
                                    doc_classification_class=None)
```

**Parametri:**

| Nome | Tipo | Descrizione |
| ---- | ---- | ----------- |
| `doc_id` | `str` | UUID del documento |
| `status` | `str` | Nuovo stato (es. `"error"`, `"ready_for_validation"`) |
| `message` | `str/None` | Messaggio di stato |
| `doc_classification_class` | `str/None` | Per lo stato `CLASSIFIED`: nuovo tipo di documento |

**Esempio — Impostare lo stato del documento su errore:**

```python
doc_id = document_json["doc_id"]
update_document_status_with_doc_id(
    doc_id, user, org_id, "error",
    message="Campo obbligatorio mancante: numero fornitore"
)
```

{% hint style="warning" %}
**Attenzione:** I cambiamenti di stato attivano azioni a valle (workflow DocFlow, hook di cambio stato). Usare solo quando necessario.
{% endhint %}

---

## get\_document\_content()

Restituisce il testo OCR completo del documento.

```python
get_document_content(document_data)
```

**Restituisce:** `str` — Testo concatenato di tutte le pagine

**Esempio — Cercare parole chiave nel testo completo:**

```python
content = get_document_content(document_data)
if "REVERSE CHARGE" in content.upper():
    set_field_value(document_data, "tax_code", "RC")

# Ricerca regex nel testo completo
match = re_search(r"Order number:\s*(\S+)", content)
if match:
    set_field_value(document_data, "purchase_order", match.group(1))
```

{% hint style="info" %}
Il risultato viene memorizzato nella cache per 60 secondi (cache TTL con massimo 128 voci).
{% endhint %}

---

## get\_user\_by\_id() / get\_user\_by\_email()

Cerca un utente per ID o email.

```python
get_user_by_id(user_id)
get_user_by_email(email)
```

**Restituisce:** Oggetto `UsersCache` con attributi come `.email`, `.first_name`, `.last_name`, `.user_id`

**Esempio — Assegnare un'attivita a un utente specifico:**

```python
user_obj = get_user_by_email("manager@company.com")
if user_obj:
    create_document_task(user, document_data,
        title="Revisione necessaria",
        description="...",
        priority="MEDIUM",
        assigned_to_user_id=str(user_obj.user_id),
        assigned_to_group_id=None,
        send_email=True)
```

---

## get\_group\_by\_id() / get\_group\_by\_name()

Cerca un gruppo utenti per ID o nome.

```python
get_group_by_id(group_id)
get_group_by_name(org_id, group_name)
```

**Restituisce:** Oggetto `GroupCache`

**Esempio — Trovare un gruppo per l'assegnazione dell'attivita:**

```python
finance_group = get_group_by_name(org_id, "Finance")
if finance_group:
    create_document_task(user, document_data,
        title="Approvazione necessaria",
        description="...",
        priority="HIGH",
        assigned_to_user_id=None,
        assigned_to_group_id=str(finance_group.id),
        send_email=True)
```

---

## compare\_values()

Confronto intelligente di valori con conversione di tipo.

```python
compare_values(value1, value2)
```

**Logica di confronto:**
1. `None == None` → `True`
2. `None != non-None` → `False`
3. Stringhe che sono numeri → confronto numerico (`"1.0" == "1.00"` → `True`)
4. Stringhe → senza distinzione maiuscole/minuscole, senza distinzione spazi (`"ABC " == " abc"` → `True`)
5. Bool vs Stringa → confronto stringa (`True == "true"` → `True`)
6. Confronto Decimal come fallback

**Esempio — Verificare la corrispondenza degli importi:**

```python
if compare_values(get_field_value(document_data, "net_amount"),
                  get_field_value(document_data, "calculated_net")):
    set_field_as_valid(document_data, "net_amount", "Gli importi corrispondono")
```

---

## get\_lov\_values()

Recupera le voci della Lista di Valori (LOV).

```python
get_lov_values(org_id, key, return_type="list_of_objects", sub_org_id=None, language_code="")
```

**Parametri:**

| Nome | Tipo | Descrizione |
| ---- | ---- | ----------- |
| `org_id` | `str` | UUID dell'organizzazione |
| `key` | `str` | Chiave LOV |
| `return_type` | `str` | `"list_of_objects"` o `"list_of_values"` |
| `sub_org_id` | `str/None` | Filtro sotto-organizzazione opzionale |
| `language_code` | `str` | Codice lingua (es. `"en"`, `"de"`) |

**Restituisce:** Valori LOV come lista di oggetti o come lista semplice.

**Esempio — Ottenere i codici fiscali configurati:**

```python
tax_codes = get_lov_values(org_id, "tax_codes", return_type="list_of_values")
```
