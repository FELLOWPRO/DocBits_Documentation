# Fulltext & Vector Search Funktionen

{% hint style="info" %}
**Verfügbar ab Version 11.48.0**

Diese Funktionen erfordern, dass die **OPENSEARCH\_ENABLED** Lizenz/Einstellung für Ihre Organisation aktiviert ist. Ohne Aktivierung werfen alle Funktionen einen `RuntimeError("Fulltext search license is missing")`.
{% endhint %}

Funktionen zum Durchsuchen von Dokumentarchiven, zum Finden ähnlicher Dokumente und zum Abfragen von ERP-Stammdaten. Diese durchsuchen **alle Dokumente** der Organisation — im Gegensatz zu `get_document_content()`, das nur den Text des aktuellen Dokuments liest.

**Quelle:** `module/script/helper/document_script_functions.py`

---

## fulltext\_search()

Durchsucht den vollständigen OCR-Text **aller Dokumente** in der Organisation.

```python
fulltext_search(org_id, query, **kwargs)
```

**Parameter:**

| Name | Typ | Standard | Beschreibung |
| ---- | --- | -------- | ------------ |
| `org_id` | `str` | erforderlich | Organisations-UUID (verwenden Sie die Kontextvariable `org_id`) |
| `query` | `str` | erforderlich | Suchbegriff (wird im OCR-Text aller Dokumente gesucht) |
| `search_type` | `str` | `"match_phrase"` | `"match_phrase"` (exakte Phrase), `"fuzzy"` (fehlertolerant, bis zu 2 Zeichen Abweichung), `"prefix"` (beginnt mit) |
| `doc_type` | `str` | `None` | Filter nach Dokumenttyp (kommagetrennt, z.B. `"INVOICE,CREDIT_NOTE"`) |
| `status` | `str` | `None` | Filter nach Dokumentstatus (kommagetrennt, z.B. `"ready_for_validation,exported"`) |
| `vendor_name` | `str` | `None` | Filter nach Lieferantenname |
| `date_range` | `str` | `None` | `"last_30_days"`, `"last_90_days"`, `"last_180_days"`, `"last_365_days"` |
| `size` | `int` | `10` | Max. Ergebnisse (begrenzt auf 50) |

**Rückgabe:** `list[dict]` — Jedes Dict enthält:

| Feld | Beschreibung |
| ---- | ------------ |
| `doc_id` | Dokument-UUID |
| `name` | Dateiname (z.B. `"INV-2026-001.pdf"`) |
| `doc_type` | Dokumenttyp (`"INVOICE"`, `"ORDER_CONFIRMATION"`, etc.) |
| `vendor_name` | Lieferantenname |
| `status` | Dokumentstatus |
| `total_amount` | Gesamtbetrag |
| `ocr_content` | Textauszug aus dem Dokument |
| `highlights` | Dict mit hervorgehobenen Treffern pro Feld |

**Beispiel — Suche nach exakter Phrase:**

```python
results = fulltext_search(org_id, "REVERSE CHARGE",
                          doc_type="INVOICE", size=10)
for doc in results:
    print(doc["name"], doc["ocr_content"])
```

**Beispiel — Fuzzy-Suche (OCR-fehlertolerant):**

```python
results = fulltext_search(org_id, "REVERSE CHARGE",
                          search_type="fuzzy",
                          vendor_name="ACME Corp")
```

**Beispiel — Präfix-Suche:**

```python
results = fulltext_search(org_id, "Rechn", search_type="prefix",
                          date_range="last_90_days")
```

{% hint style="warning" %}
**Leere Abfrage:** Die Übergabe eines leeren Strings gibt sofort `[]` zurück.
{% endhint %}

{% hint style="info" %}
**Fehlerbehandlung:** Wenn der Fulltextsearch-Service nicht erreichbar ist, gibt die Funktion `[]` zurück und protokolliert eine Warnung. Sie löst **keine** Exception aus.
{% endhint %}

---

## vector\_search()

Findet semantisch ähnliche Dokumente mittels Vektor-Embeddings (k-NN-Suche mit 384-dimensionalen Vektoren).

```python
vector_search(org_id, doc_id, **kwargs)
```

**Parameter:**

| Name | Typ | Standard | Beschreibung |
| ---- | --- | -------- | ------------ |
| `org_id` | `str` | erforderlich | Organisations-UUID |
| `doc_id` | `str` | erforderlich | Quell-Dokument-UUID |
| `k` | `int` | `5` | Anzahl ähnlicher Dokumente (begrenzt auf 50) |

**Rückgabe:** `list[dict]` — Jedes Dict enthält: `doc_id`, `name`, `doc_type`, `similarity_score` (0-1), `similarity_percent` (0-100).

**Beispiel:**

```python
doc_id = document_json["doc_id"]
similar = vector_search(org_id, doc_id, k=5)
for doc in similar:
    print(f"{doc['name']}: {doc['similarity_percent']}% ähnlich")
```

{% hint style="info" %}
**Funktionsweise:** Jedes Dokument wird bei der Indizierung in einen 384-dimensionalen Vektor umgewandelt. Die Vektorsuche findet die nächsten Nachbarn in diesem Vektorraum.
{% endhint %}

---

## fulltext\_search\_erp()

Durchsucht ERP-Stammdaten (Lieferanten, Bestellungen, Kunden, Materialien), die in OpenSearch indiziert sind.

```python
fulltext_search_erp(org_id, query, **kwargs)
```

**Parameter:**

| Name | Typ | Standard | Beschreibung |
| ---- | --- | -------- | ------------ |
| `org_id` | `str` | erforderlich | Organisations-UUID |
| `query` | `str` | erforderlich | Suchbegriff |
| `entity_types` | `str` | `None` | Filter nach Entitätstyp (kommagetrennt: `"vendor"`, `"purchase_order"`, `"customer"`, `"material"`) |
| `vendor_number` | `str` | `None` | Filter nach Lieferantennummer |
| `vendor_name` | `str` | `None` | Filter nach Lieferantenname |
| `company_code` | `str` | `None` | Filter nach Buchungskreis |
| `size` | `int` | `10` | Max. Ergebnisse (begrenzt auf 50) |

**Beispiel — Lieferant im ERP validieren:**

```python
vendor = get_field_value(document_data, "supplier_name", "")
if vendor:
    matches = fulltext_search_erp(org_id, vendor,
                                   entity_types="vendor", size=5)
    if not matches:
        set_field_as_invalid(document_data, "supplier_name",
                             "Lieferant nicht in ERP-Stammdaten gefunden")
```

---

## fulltext\_suggestions()

Gibt Autovervollständigungs-Vorschläge für Suchbegriffe zurück.

```python
fulltext_suggestions(org_id, query, **kwargs)
```

**Parameter:**

| Name | Typ | Standard | Beschreibung |
| ---- | --- | -------- | ------------ |
| `org_id` | `str` | erforderlich | Organisations-UUID |
| `query` | `str` | erforderlich | Präfix / Suchbegriff |
| `limit` | `int` | `10` | Max. Vorschläge pro Kategorie (begrenzt auf 20) |

**Beispiel:**

```python
suggestions = fulltext_suggestions(org_id, "ACM", limit=5)
vendor_list = suggestions.get("vendors", [])
```

---

## Schnellübersicht

| Funktion | Zweck | Rückgabe |
| -------- | ----- | -------- |
| `fulltext_search()` | OCR-Text aller Dokumente durchsuchen | `list[dict]` |
| `vector_search()` | Semantisch ähnliche Dokumente finden | `list[dict]` |
| `fulltext_search_erp()` | ERP-Stammdaten durchsuchen | `list[dict]` |
| `fulltext_suggestions()` | Autovervollständigungs-Vorschläge | `dict` |

---

## Häufige Muster

### Lizenzprüfung

```python
try:
    results = fulltext_search(org_id, "test")
except RuntimeError:
    results = []
```

### Kombination mit Feld-Funktionen

```python
results = fulltext_search(org_id, invoice_number,
                          status="exported", size=1)
if results:
    set_field_as_invalid(document_data, "invoice_id",
                         f"Bereits vorhanden: {results[0]['name']}")
else:
    set_field_as_valid(document_data, "invoice_id", "Kein Duplikat gefunden")
```
