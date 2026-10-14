# Fulltext & Vector Search Funktionen

{% hint style="info" %}
**Verfügbar ab Version 11.48.0**

Diese Funktionen erfordern, dass die Lizenz bzw. Einstellung **OPENSEARCH\_ENABLED** für Ihre Organisation aktiviert ist. Ohne Aktivierung lösen alle Funktionen einen `RuntimeError("Fulltext search license is missing")` aus.
{% endhint %}

Funktionen zum Durchsuchen von Dokumentarchiven, zum Finden ähnlicher Dokumente und zum Abfragen von ERP-Stammdaten. Diese durchsuchen **alle Dokumente** der Organisation — im Gegensatz zu `get_document_content()`, das nur den Text des aktuellen Dokuments liest.

{% hint style="success" %}
**Sicherheit:** Die `org_id` wird von der Skript-Sandbox automatisch eingefügt. Sie müssen sie nie übergeben — Ihre Skripte arbeiten immer ausschließlich mit den Daten Ihrer eigenen Organisation.
{% endhint %}

**Quelle:** `module/script/helper/document_script_functions.py`

---

## fulltext\_search()

Durchsucht den vollständigen OCR-Text **aller Dokumente** der Organisation. Findet Text in den Feldern `pages.pageText`, `tfidfCustomPageText` und `ai_text` über den Microservice fulltextsearch.

```python
fulltext_search(query, **kwargs)
```

**Parameter:**

| Name | Typ | Standard | Beschreibung |
| ---- | --- | -------- | ------------ |
| `query` | `str` | erforderlich | Suchbegriff (wird im OCR-Text aller Dokumente gesucht) |
| `search_type` | `str` | `"match_phrase"` | `"match_phrase"` (exakte Phrase), `"fuzzy"` (fehlertolerant, bis zu 2 Zeichen Abweichung), `"prefix"` (beginnt mit) |
| `doc_type` | `str` | `None` | Filter nach Dokumenttyp (kommagetrennt, z. B. `"INVOICE,CREDIT_NOTE"`) |
| `status` | `str` | `None` | Filter nach Dokumentstatus (kommagetrennt, z. B. `"ready_for_validation,exported"`) |
| `vendor_name` | `str` | `None` | Filter nach Lieferantenname |
| `date_range` | `str` | `None` | `"last_30_days"`, `"last_90_days"`, `"last_180_days"`, `"last_365_days"` |
| `size` | `int` | `10` | Maximale Anzahl Ergebnisse (auf 50 begrenzt) |

**Rückgabe:** `list[dict]` — Jedes Dict enthält:

| Feld | Beschreibung |
| ---- | ------------ |
| `doc_id` | Dokument-UUID |
| `name` | Dateiname (z. B. `"INV-2026-001.pdf"`) |
| `doc_type` | Dokumenttyp (`"INVOICE"`, `"ORDER_CONFIRMATION"` usw.) |
| `vendor_name` | Lieferantenname |
| `status` | Dokumentstatus |
| `total_amount` | Gesamtbetrag |
| `ocr_content` | Passender Textauszug aus dem Dokument |
| `highlights` | Dict mit hervorgehobenen Treffern pro Feld |

**Beispiel — Suche nach exakter Phrase:**

```python
results = fulltext_search("REVERSE CHARGE",
                          doc_type="INVOICE", size=10)
for doc in results:
    print(doc["name"], doc["ocr_content"])
```

**Beispiel — Fuzzy-Suche (tolerant gegenüber OCR-Tippfehlern):**

```python
# Finds "REVERSE CHARGE" even with OCR errors like "REVERS CHARG"
results = fulltext_search("REVERSE CHARGE",
                          search_type="fuzzy",
                          vendor_name="ACME Corp")
```

**Beispiel — Präfix-Suche:**

```python
# Finds all documents containing words starting with "Rechn"
results = fulltext_search("Rechn", search_type="prefix",
                          date_range="last_90_days")
```

{% hint style="warning" %}
**Leere Abfrage:** Die Übergabe eines leeren Strings gibt sofort `[]` zurück, ohne einen HTTP-Aufruf auszuführen.
{% endhint %}

{% hint style="info" %}
**Fehlerbehandlung:** Wenn der Service fulltextsearch nicht erreichbar ist, gibt die Funktion `[]` zurück und protokolliert eine Warnung. Sie löst **keine** Exception aus.
{% endhint %}

---

## vector\_search()

Findet semantisch ähnliche Dokumente mithilfe von Vektor-Embeddings (k-NN-Suche mit 384-dimensionalen Vektoren). Nützlich, um Dokumente mit ähnlichem Inhalt unabhängig vom genauen Wortlaut zu finden.

```python
vector_search(doc_id, **kwargs)
```

**Parameter:**

| Name | Typ | Standard | Beschreibung |
| ---- | --- | -------- | ------------ |
| `doc_id` | `str` | erforderlich | UUID des Quelldokuments (das Dokument, zu dem ähnliche Treffer gesucht werden) |
| `k` | `int` | `5` | Anzahl der zurückgegebenen ähnlichen Dokumente (auf 50 begrenzt) |

**Rückgabe:** `list[dict]` — Jedes Dict enthält:

| Feld | Beschreibung |
| ---- | ------------ |
| `doc_id` | UUID des ähnlichen Dokuments |
| `name` | Dateiname |
| `doc_type` | Dokumenttyp |
| `similarity_score` | Roher Ähnlichkeitswert (0-1) |
| `similarity_percent` | Ähnlichkeit in Prozent (0-100) |

**Beispiel — Ähnliche Dokumente finden:**

```python
doc_id = document_json["doc_id"]
similar = vector_search(doc_id, k=5)
for doc in similar:
    print(f"{doc['name']}: {doc['similarity_percent']}% similar")
```

{% hint style="info" %}
**Funktionsweise:** Jedes Dokument wird bei der Indizierung in einen 384-dimensionalen Vektor umgewandelt. Die Vektorsuche findet die nächsten Nachbarn in diesem Vektorraum, die semantisch ähnlichen Dokumenten entsprechen.
{% endhint %}

---

## fulltext\_search\_erp()

Durchsucht ERP-Stammdaten (Lieferanten, Bestellungen, Kunden, Materialien), die in OpenSearch indiziert sind.

```python
fulltext_search_erp(query, **kwargs)
```

**Parameter:**

| Name | Typ | Standard | Beschreibung |
| ---- | --- | -------- | ------------ |
| `query` | `str` | erforderlich | Suchbegriff |
| `entity_types` | `str` | `None` | Filter nach Entitätstyp (kommagetrennt: `"vendor"`, `"purchase_order"`, `"customer"`, `"material"`) |
| `vendor_number` | `str` | `None` | Filter nach Lieferantennummer |
| `vendor_name` | `str` | `None` | Filter nach Lieferantenname |
| `company_code` | `str` | `None` | Filter nach Buchungskreis |
| `size` | `int` | `10` | Maximale Anzahl Ergebnisse (auf 50 begrenzt) |

**Rückgabe:** `list[dict]` — Felder je nach Entitätstyp (Lieferantendatensätze enthalten `vendor_number`, `vendor_name` usw.)

**Beispiel — Lieferant im ERP validieren:**

```python
vendor = get_field_value(document_data, "supplier_name", "")
if vendor:
    matches = fulltext_search_erp(vendor,
                                   entity_types="vendor", size=5)
    if not matches:
        set_field_as_invalid(document_data, "supplier_name",
                             "Vendor not found in ERP master data")
```

**Beispiel — Bestellungen suchen:**

```python
po_number = get_field_value(document_data, "purchase_order", "")
if po_number:
    results = fulltext_search_erp(po_number,
                                   entity_types="purchase_order")
    if results:
        # PO found in ERP
        set_field_as_valid(document_data, "purchase_order", "PO verified in ERP")
```

---

## fulltext\_suggestions()

Gibt Autovervollständigungs-Vorschläge für Suchbegriffe zurück. Gruppiert die Ergebnisse nach Kategorie (Lieferanten, Dateinamen, Rechnungsnummern).

```python
fulltext_suggestions(query, **kwargs)
```

**Parameter:**

| Name | Typ | Standard | Beschreibung |
| ---- | --- | -------- | ------------ |
| `query` | `str` | erforderlich | Präfix / Suchbegriff |
| `limit` | `int` | `10` | Maximale Anzahl Vorschläge pro Kategorie (auf 20 begrenzt) |

**Rückgabe:** `dict` mit gruppierten Vorschlägen:

```python
{
    "vendors": ["ACME Corp", "ACME International"],
    "filenames": ["INV-2026-001.pdf", "INV-2026-002.pdf"],
    "invoice_numbers": ["INV-2026-001", "INV-2026-002"]
}
```

**Beispiel — Lieferantenvorschläge abrufen:**

```python
suggestions = fulltext_suggestions("ACM", limit=5)
vendor_list = suggestions.get("vendors", [])
```

{% hint style="warning" %}
**Leere Abfrage:** Die Übergabe eines leeren Strings gibt sofort `{}` zurück.
{% endhint %}

---

## Schnellübersicht

| Funktion | Zweck | Rückgabe |
| -------- | ----- | -------- |
| `fulltext_search(query, ...)` | OCR-Text aller Dokumente durchsuchen | `list[dict]` |
| `vector_search(doc_id, ...)` | Semantisch ähnliche Dokumente finden | `list[dict]` |
| `fulltext_search_erp(query, ...)` | ERP-Stammdaten durchsuchen | `list[dict]` |
| `fulltext_suggestions(query, ...)` | Autovervollständigungs-Vorschläge | `dict` |

---

## Häufige Muster

### Lizenzprüfung

Alle vier Funktionen prüfen automatisch die Einstellung `OPENSEARCH_ENABLED`. Wenn sie nicht aktiviert ist:

```python
# This will raise RuntimeError("Fulltext search license is missing")
results = fulltext_search("test")
```

So behandeln Sie das in Skripten sauber:

```python
try:
    results = fulltext_search("test")
except RuntimeError:
    # OpenSearch not enabled for this org — skip search
    results = []
```

### Kombination mit Feld-Funktionen

```python
# Search → validate → set field
invoice_number = get_field_value(document_data, "invoice_id", "")
results = fulltext_search(invoice_number,
                          status="exported", size=1)
if results:
    set_field_as_invalid(document_data, "invoice_id",
                         f"Already exists: {results[0]['name']}")
else:
    set_field_as_valid(document_data, "invoice_id", "No duplicate found")
```
