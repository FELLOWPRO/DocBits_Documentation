# Funzioni di Ricerca Fulltext e Vettoriale

{% hint style="info" %}
**Disponibile dalla versione 11.48.0**

Queste funzioni richiedono che la licenza/preferenza **OPENSEARCH\_ENABLED** sia attivata per la vostra organizzazione. Senza di essa, tutte le funzioni generano un `RuntimeError("Fulltext search license is missing")`.
{% endhint %}

Funzioni per la ricerca negli archivi documentali, il rilevamento di documenti simili e l'interrogazione dei dati master ERP. Queste ricercano su **tutti i documenti** dell'organizzazione — a differenza di `get_document_content()` che legge solo il testo del documento corrente.

**Sorgente:** `module/script/helper/document_script_functions.py`

---

## fulltext\_search()

Cerca nel testo OCR completo di **tutti i documenti** dell'organizzazione. Trova testo nei campi `pages.pageText`, `tfidfCustomPageText` e `ai_text` tramite il microservizio fulltextsearch.

```python
fulltext_search(org_id, query, **kwargs)
```

**Parametri:**

| Nome | Tipo | Default | Descrizione |
| ---- | ---- | ------- | ----------- |
| `org_id` | `str` | obbligatorio | UUID dell'organizzazione (usare la variabile di contesto `org_id`) |
| `query` | `str` | obbligatorio | Termine di ricerca (cercato nel testo OCR di tutti i documenti) |
| `search_type` | `str` | `"match_phrase"` | `"match_phrase"` (frase esatta), `"fuzzy"` (tollerante agli errori, fino a 2 caratteri di differenza), `"prefix"` (inizia con) |
| `doc_type` | `str` | `None` | Filtra per tipo di documento (separato da virgola, es. `"INVOICE,CREDIT_NOTE"`) |
| `status` | `str` | `None` | Filtra per stato del documento (separato da virgola, es. `"ready_for_validation,exported"`) |
| `vendor_name` | `str` | `None` | Filtra per nome del fornitore |
| `date_range` | `str` | `None` | `"last_30_days"`, `"last_90_days"`, `"last_180_days"`, `"last_365_days"` |
| `size` | `int` | `10` | Risultati massimi (limitato a 50) |

**Restituisce:** `list[dict]` — Ogni dict contiene:

| Campo | Descrizione |
| ----- | ----------- |
| `doc_id` | UUID del documento |
| `name` | Nome del file (es. `"INV-2026-001.pdf"`) |
| `doc_type` | Tipo di documento (`"INVOICE"`, `"ORDER_CONFIRMATION"`, ecc.) |
| `vendor_name` | Nome del fornitore |
| `status` | Stato del documento |
| `total_amount` | Importo totale |
| `ocr_content` | Estratto del testo corrispondente dal documento |
| `highlights` | Dict con le corrispondenze evidenziate per campo |

**Esempio — Ricerca frase esatta:**

```python
results = fulltext_search(org_id, "REVERSE CHARGE",
                          doc_type="INVOICE", size=10)
for doc in results:
    print(doc["name"], doc["ocr_content"])
```

**Esempio — Ricerca fuzzy (tollerante agli errori OCR):**

```python
# Trova "REVERSE CHARGE" anche con errori OCR come "REVERS CHARG"
results = fulltext_search(org_id, "REVERSE CHARGE",
                          search_type="fuzzy",
                          vendor_name="ACME Corp")
```

**Esempio — Ricerca per prefisso:**

```python
# Trova tutti i documenti contenenti parole che iniziano con "Rechn"
results = fulltext_search(org_id, "Rechn", search_type="prefix",
                          date_range="last_90_days")
```

{% hint style="warning" %}
**Query vuota:** Passare una stringa vuota restituisce `[]` immediatamente senza effettuare una chiamata HTTP.
{% endhint %}

{% hint style="info" %}
**Gestione errori:** Se il servizio fulltextsearch non e raggiungibile, la funzione restituisce `[]` e registra un avviso. **Non** genera un'eccezione.
{% endhint %}

---

## vector\_search()

Trova documenti semanticamente simili utilizzando embedding vettoriali (ricerca k-NN con vettori a 384 dimensioni). Utile per trovare documenti con contenuto simile indipendentemente dalle parole esatte.

```python
vector_search(org_id, doc_id, **kwargs)
```

**Parametri:**

| Nome | Tipo | Default | Descrizione |
| ---- | ---- | ------- | ----------- |
| `org_id` | `str` | obbligatorio | UUID dell'organizzazione |
| `doc_id` | `str` | obbligatorio | UUID del documento sorgente (il documento per cui trovare corrispondenze simili) |
| `k` | `int` | `5` | Numero di documenti simili da restituire (limitato a 50) |

**Restituisce:** `list[dict]` — Ogni dict contiene:

| Campo | Descrizione |
| ----- | ----------- |
| `doc_id` | UUID del documento simile |
| `name` | Nome del file |
| `doc_type` | Tipo di documento |
| `similarity_score` | Punteggio di similarita grezzo (0-1) |
| `similarity_percent` | Similarita in percentuale (0-100) |

**Esempio — Trovare documenti simili:**

```python
doc_id = document_json["doc_id"]
similar = vector_search(org_id, doc_id, k=5)
for doc in similar:
    print(f"{doc['name']}: {doc['similarity_percent']}% similar")
```

{% hint style="info" %}
**Come funziona:** Ogni documento viene convertito in un vettore a 384 dimensioni quando viene indicizzato. La ricerca vettoriale trova i vicini piu prossimi in questo spazio vettoriale, che corrispondono a documenti semanticamente simili.
{% endhint %}

---

## fulltext\_search\_erp()

Cerca nei dati master ERP (fornitori, ordini di acquisto, clienti, materiali) indicizzati in OpenSearch.

```python
fulltext_search_erp(org_id, query, **kwargs)
```

**Parametri:**

| Nome | Tipo | Default | Descrizione |
| ---- | ---- | ------- | ----------- |
| `org_id` | `str` | obbligatorio | UUID dell'organizzazione |
| `query` | `str` | obbligatorio | Termine di ricerca |
| `entity_types` | `str` | `None` | Filtra per tipo di entita (separato da virgola: `"vendor"`, `"purchase_order"`, `"customer"`, `"material"`) |
| `vendor_number` | `str` | `None` | Filtra per numero fornitore |
| `vendor_name` | `str` | `None` | Filtra per nome fornitore |
| `company_code` | `str` | `None` | Filtra per codice azienda |
| `size` | `int` | `10` | Risultati massimi (limitato a 50) |

**Restituisce:** `list[dict]` — Campi specifici per tipo di entita (i record fornitore hanno `vendor_number`, `vendor_name`, ecc.)

**Esempio — Validare fornitore in ERP:**

```python
vendor = get_field_value(document_data, "supplier_name", "")
if vendor:
    matches = fulltext_search_erp(org_id, vendor,
                                   entity_types="vendor", size=5)
    if not matches:
        set_field_as_invalid(document_data, "supplier_name",
                             "Vendor not found in ERP master data")
```

**Esempio — Cercare ordini di acquisto:**

```python
po_number = get_field_value(document_data, "purchase_order", "")
if po_number:
    results = fulltext_search_erp(org_id, po_number,
                                   entity_types="purchase_order")
    if results:
        # OdA trovato in ERP
        set_field_as_valid(document_data, "purchase_order", "PO verified in ERP")
```

---

## fulltext\_suggestions()

Restituisce suggerimenti di autocompletamento per i termini di ricerca. Raggruppa i risultati per categoria (fornitori, nomi file, numeri fattura).

```python
fulltext_suggestions(org_id, query, **kwargs)
```

**Parametri:**

| Nome | Tipo | Default | Descrizione |
| ---- | ---- | ------- | ----------- |
| `org_id` | `str` | obbligatorio | UUID dell'organizzazione |
| `query` | `str` | obbligatorio | Prefisso / termine di ricerca |
| `limit` | `int` | `10` | Suggerimenti massimi per categoria (limitato a 20) |

**Restituisce:** `dict` con suggerimenti raggruppati:

```python
{
    "vendors": ["ACME Corp", "ACME International"],
    "filenames": ["INV-2026-001.pdf", "INV-2026-002.pdf"],
    "invoice_numbers": ["INV-2026-001", "INV-2026-002"]
}
```

**Esempio — Ottenere suggerimenti fornitori:**

```python
suggestions = fulltext_suggestions(org_id, "ACM", limit=5)
vendor_list = suggestions.get("vendors", [])
```

{% hint style="warning" %}
**Query vuota:** Passare una stringa vuota restituisce `{}` immediatamente.
{% endhint %}

---

## Riferimento Rapido

| Funzione | Scopo | Restituisce |
| -------- | ----- | ----------- |
| `fulltext_search()` | Cerca nel testo OCR di tutti i documenti | `list[dict]` |
| `vector_search()` | Trova documenti semanticamente simili | `list[dict]` |
| `fulltext_search_erp()` | Cerca nei dati master ERP | `list[dict]` |
| `fulltext_suggestions()` | Suggerimenti di autocompletamento | `dict` |

---

## Pattern Comuni

### Controllo Licenza

Tutte e quattro le funzioni controllano automaticamente la preferenza `OPENSEARCH_ENABLED`. Se non abilitata:

```python
# Questo genera RuntimeError("Fulltext search license is missing")
results = fulltext_search(org_id, "test")
```

Per gestire questo in modo elegante negli script:

```python
try:
    results = fulltext_search(org_id, "test")
except RuntimeError:
    # OpenSearch non abilitato per questa organizzazione — salta la ricerca
    results = []
```

### Combinazione con le Funzioni dei Campi

```python
# Cerca -> valida -> imposta campo
results = fulltext_search(org_id, invoice_number,
                          status="exported", size=1)
if results:
    set_field_as_invalid(document_data, "invoice_id",
                         f"Already exists: {results[0]['name']}")
else:
    set_field_as_valid(document_data, "invoice_id", "No duplicate found")
```
