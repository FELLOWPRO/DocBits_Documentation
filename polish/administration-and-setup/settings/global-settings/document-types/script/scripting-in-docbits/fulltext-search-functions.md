# Funkcje Wyszukiwania Fulltext i Wektorowego

{% hint style="info" %}
**Dostepne od wersji 11.48.0**

Te funkcje wymagaja aktywacji licencji/preferencji **OPENSEARCH\_ENABLED** dla organizacji. Bez niej wszystkie funkcje generuja `RuntimeError("Fulltext search license is missing")`.
{% endhint %}

Funkcje do przeszukiwania archiwow dokumentow, znajdowania podobnych dokumentow i odpytywania danych bazowych ERP. Przeszukuja **wszystkie dokumenty** organizacji — w przeciwienstwie do `get_document_content()`, ktore czyta tylko tekst biezacego dokumentu.

{% hint style="success" %}
**Security:** The `org_id` is automatically injected by the script sandbox. You never need to pass it — your scripts always operate within your own organization's data.
{% endhint %}

**Zrodlo:** `module/script/helper/document_script_functions.py`

---

## fulltext\_search()

Przeszukuje pelny tekst OCR **wszystkich dokumentow** w organizacji. Znajduje tekst w polach `pages.pageText`, `tfidfCustomPageText` i `ai_text` za posrednictwem mikroserwisu fulltextsearch.

```python
fulltext_search(query, **kwargs)
```

**Parametry:**

| Nazwa | Typ | Domyslnie | Opis |
| ----- | --- | --------- | ---- |
| `query` | `str` | wymagane | Szukana fraza (przeszukiwana w tekscie OCR wszystkich dokumentow) |
| `search_type` | `str` | `"match_phrase"` | `"match_phrase"` (dokladna fraza), `"fuzzy"` (tolerancja bledow, do 2 znakow roznicy), `"prefix"` (zaczyna sie od) |
| `doc_type` | `str` | `None` | Filtruj po typie dokumentu (rozdzielone przecinkami, np. `"INVOICE,CREDIT_NOTE"`) |
| `status` | `str` | `None` | Filtruj po statusie dokumentu (rozdzielone przecinkami, np. `"ready_for_validation,exported"`) |
| `vendor_name` | `str` | `None` | Filtruj po nazwie dostawcy |
| `date_range` | `str` | `None` | `"last_30_days"`, `"last_90_days"`, `"last_180_days"`, `"last_365_days"` |
| `size` | `int` | `10` | Maks. wynikow (ograniczone do 50) |

**Zwraca:** `list[dict]` — Kazdy dict zawiera:

| Pole | Opis |
| ---- | ---- |
| `doc_id` | UUID dokumentu |
| `name` | Nazwa pliku (np. `"INV-2026-001.pdf"`) |
| `doc_type` | Typ dokumentu (`"INVOICE"`, `"ORDER_CONFIRMATION"`, itp.) |
| `vendor_name` | Nazwa dostawcy |
| `status` | Status dokumentu |
| `total_amount` | Kwota calkowita |
| `ocr_content` | Dopasowany fragment tekstu z dokumentu |
| `highlights` | Dict z podswietlonymi dopasowaniami na pole |

**Przyklad — Wyszukiwanie dokladnej frazy:**

```python
results = fulltext_search("REVERSE CHARGE",
                          doc_type="INVOICE", size=10)
for doc in results:
    print(doc["name"], doc["ocr_content"])
```

**Przyklad — Wyszukiwanie rozmyte (tolerancja bledow OCR):**

```python
# Znajduje "REVERSE CHARGE" nawet z bledami OCR jak "REVERS CHARG"
results = fulltext_search("REVERSE CHARGE",
                          search_type="fuzzy",
                          vendor_name="ACME Corp")
```

**Przyklad — Wyszukiwanie prefiksowe:**

```python
# Znajduje wszystkie dokumenty zawierajace slowa zaczynajace sie od "Rechn"
results = fulltext_search("Rechn", search_type="prefix",
                          date_range="last_90_days")
```

{% hint style="warning" %}
**Puste zapytanie:** Przekazanie pustego ciagu zwraca natychmiast `[]` bez wykonywania wywolania HTTP.
{% endhint %}

{% hint style="info" %}
**Obsluga bledow:** Jesli usluga fulltextsearch jest nieosiagalna, funkcja zwraca `[]` i loguje ostrzezenie. **Nie** generuje wyjatku.
{% endhint %}

---

## vector\_search()

Znajduje semantycznie podobne dokumenty za pomoca osadzen wektorowych (wyszukiwanie k-NN z wektorami 384-wymiarowymi). Przydatne do znajdowania dokumentow o podobnej tresci niezaleznie od dokladnego slownictwa.

```python
vector_search(doc_id, **kwargs)
```

**Parametry:**

| Nazwa | Typ | Domyslnie | Opis |
| ----- | --- | --------- | ---- |
| `doc_id` | `str` | wymagane | UUID dokumentu zrodlowego (dokument, dla ktorego szukamy podobnych) |
| `k` | `int` | `5` | Liczba podobnych dokumentow do zwrocenia (ograniczone do 50) |

**Zwraca:** `list[dict]` — Kazdy dict zawiera:

| Pole | Opis |
| ---- | ---- |
| `doc_id` | UUID podobnego dokumentu |
| `name` | Nazwa pliku |
| `doc_type` | Typ dokumentu |
| `similarity_score` | Surowy wynik podobienstwa (0-1) |
| `similarity_percent` | Podobienstwo w procentach (0-100) |

**Przyklad — Znajdowanie podobnych dokumentow:**

```python
doc_id = document_json["doc_id"]
similar = vector_search(doc_id, k=5)
for doc in similar:
    print(f"{doc['name']}: {doc['similarity_percent']}% similar")
```

{% hint style="info" %}
**Jak to dziala:** Kazdy dokument jest konwertowany na wektor 384-wymiarowy podczas indeksowania. Wyszukiwanie wektorowe znajduje najblizszych sasiadow w tej przestrzeni wektorowej, co odpowiada semantycznie podobnym dokumentom.
{% endhint %}

---

## fulltext\_search\_erp()

Przeszukuje dane bazowe ERP (dostawcy, zamowienia zakupu, klienci, materialy) zaindeksowane w OpenSearch.

```python
fulltext_search_erp(query, **kwargs)
```

**Parametry:**

| Nazwa | Typ | Domyslnie | Opis |
| ----- | --- | --------- | ---- |
| `query` | `str` | wymagane | Szukana fraza |
| `entity_types` | `str` | `None` | Filtruj po typie encji (rozdzielone przecinkami: `"vendor"`, `"purchase_order"`, `"customer"`, `"material"`) |
| `vendor_number` | `str` | `None` | Filtruj po numerze dostawcy |
| `vendor_name` | `str` | `None` | Filtruj po nazwie dostawcy |
| `company_code` | `str` | `None` | Filtruj po kodzie firmy |
| `size` | `int` | `10` | Maks. wynikow (ograniczone do 50) |

**Zwraca:** `list[dict]` — Pola specyficzne dla typu encji (rekordy dostawcow maja `vendor_number`, `vendor_name`, itp.)

**Przyklad — Walidacja dostawcy w ERP:**

```python
vendor = get_field_value(document_data, "supplier_name", "")
if vendor:
    matches = fulltext_search_erp(vendor,
                                   entity_types="vendor", size=5)
    if not matches:
        set_field_as_invalid(document_data, "supplier_name",
                             "Vendor not found in ERP master data")
```

**Przyklad — Wyszukiwanie zamowien zakupu:**

```python
po_number = get_field_value(document_data, "purchase_order", "")
if po_number:
    results = fulltext_search_erp(po_number,
                                   entity_types="purchase_order")
    if results:
        # ZZ znalezione w ERP
        set_field_as_valid(document_data, "purchase_order", "PO verified in ERP")
```

---

## fulltext\_suggestions()

Zwraca podpowiedzi autouzupelniania dla szukanych fraz. Grupuje wyniki wedlug kategorii (dostawcy, nazwy plikow, numery faktur).

```python
fulltext_suggestions(query, **kwargs)
```

**Parametry:**

| Nazwa | Typ | Domyslnie | Opis |
| ----- | --- | --------- | ---- |
| `query` | `str` | wymagane | Prefiks / szukana fraza |
| `limit` | `int` | `10` | Maks. podpowiedzi na kategorie (ograniczone do 20) |

**Zwraca:** `dict` z pogrupowanymi podpowiedziami:

```python
{
    "vendors": ["ACME Corp", "ACME International"],
    "filenames": ["INV-2026-001.pdf", "INV-2026-002.pdf"],
    "invoice_numbers": ["INV-2026-001", "INV-2026-002"]
}
```

**Przyklad — Pobieranie podpowiedzi dostawcow:**

```python
suggestions = fulltext_suggestions("ACM", limit=5)
vendor_list = suggestions.get("vendors", [])
```

{% hint style="warning" %}
**Puste zapytanie:** Przekazanie pustego ciagu zwraca natychmiast `{}`.
{% endhint %}

---

## Szybka Referencja

| Funkcja | Cel | Zwraca |
| ------- | --- | ------ |
| `fulltext_search(query, ...)` | Przeszukiwanie tekstu OCR wszystkich dokumentow | `list[dict]` |
| `vector_search(doc_id, ...)` | Znajdowanie semantycznie podobnych dokumentow | `list[dict]` |
| `fulltext_search_erp(query, ...)` | Przeszukiwanie danych bazowych ERP | `list[dict]` |
| `fulltext_suggestions(query, ...)` | Podpowiedzi autouzupelniania | `dict` |

---

## Typowe Wzorce

### Sprawdzanie Licencji

Wszystkie cztery funkcje automatycznie sprawdzaja preferencje `OPENSEARCH_ENABLED`. Jesli nie jest aktywna:

```python
# To wygeneruje RuntimeError("Fulltext search license is missing")
results = fulltext_search("test")
```

Aby obsluzyc to elegancko w skryptach:

```python
try:
    results = fulltext_search("test")
except RuntimeError:
    # OpenSearch nie aktywowany dla tej organizacji — pomin wyszukiwanie
    results = []
```

### Laczenie z Funkcjami Pol

```python
# Szukaj -> waliduj -> ustaw pole
results = fulltext_search(invoice_number,
                          status="exported", size=1)
if results:
    set_field_as_invalid(document_data, "invoice_id",
                         f"Already exists: {results[0]['name']}")
else:
    set_field_as_valid(document_data, "invoice_id", "No duplicate found")
```
