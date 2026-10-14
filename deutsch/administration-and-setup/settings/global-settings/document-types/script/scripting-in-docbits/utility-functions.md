# Hilfsfunktionen

Eingebaute Funktionen für Stringverarbeitung, Mathematik, Datumsoperationen, Regex und Datentypen.

**Quelle:** `module/script/helper/script_processor.py:get_allowed_functions_list()`

---

## String-Funktionen

### Typkonvertierung

```python
str(value)       # In String konvertieren
int(value)       # In Integer konvertieren
float(value)     # In Float konvertieren
str_to_bool(s)   # "true"/"1"/"yes" → True, alles andere → False
```

### String-Methoden

```python
lower(s)              # str.lower — "ABC" → "abc"
upper(s)              # str.upper — "abc" → "ABC"
split(s, sep)         # str.split — "a,b,c".split(",") → ["a","b","c"]
strip(s)              # str.strip — " abc " → "abc"
startswith(s, prefix) # str.startswith
endswith(s, suffix)   # str.endswith
```

{% hint style="info" %}
Diese stehen als eigenständige Funktionen zur Verfügung, können aber auch als Methoden auf Strings aufgerufen werden:

```python
# Beides funktioniert:
result = upper("hello")      # → "HELLO"
result = "hello".upper()     # → "HELLO"
```
{% endhint %}

---

## Fuzzy-String-Matching

### levenshtein\_distance()

Berechnet die Editierdistanz zwischen zwei Strings (Anzahl der benötigten Änderungen).

```python
levenshtein_distance(s1, s2)
```

**Beispiel:**

```python
dist = levenshtein_distance("ACME Corp", "ACME Corporation")
# dist = 7
if dist < 5:
    # Strings sind ähnlich genug
    pass
```

### jaro\_winkler\_similarity()

Berechnet einen Ähnlichkeitswert zwischen 0.0 und 1.0.

```python
jaro_winkler_similarity(s1, s2)
```

**Beispiel:**

```python
score = jaro_winkler_similarity("Invoice", "Invocie")
# score ≈ 0.96 (sehr ähnlich, Tippfehler)

score = jaro_winkler_similarity("Invoice", "Receipt")
# score ≈ 0.45 (unähnlich)
```

{% hint style="success" %}
**Wann welche verwenden?**
- **Levenshtein**: Gut für kurze Strings, exakte Fehleranzahl
- **Jaro-Winkler**: Besser für Namen/Adressen, gewichtet Übereinstimmungen am Anfang stärker
{% endhint %}

---

## Regex-Funktionen

Basierend auf Pythons `re`-Modul, aber als eigenständige Funktionen verfügbar.

### re\_search()

Sucht nach dem ersten Vorkommen eines Musters.

```python
re_search(pattern, string)
```

**Rückgabe:** Match-Objekt oder `None`

**Beispiel — Bestellnummer aus Volltext extrahieren:**

```python
content = get_document_content(document_data)
match = re_search(r"Order number:\s*(\d+)", content)
if match:
    po_number = match.group(1)
    set_field_value(document_data, "purchase_order", po_number)
```

### re\_sub()

Ersetzt Muster-Treffer durch einen Ersetzungsstring.

```python
re_sub(pattern, replacement, string)
```

**Beispiel — Sonderzeichen aus Rechnungs-ID entfernen:**

```python
inv_id = get_field_value(document_data, "invoice_id", "")
cleaned = re_sub(r"[^A-Za-z0-9\-]", "", inv_id)
set_field_value(document_data, "invoice_id", cleaned)
```

### re\_findall()

Findet alle Vorkommen eines Musters.

```python
re_findall(pattern, string)
```

**Beispiel — Alle PO-Nummern im Dokument finden:**

```python
content = get_document_content(document_data)
po_numbers = re_findall(r"PO[- ]?\d{6,}", content)
if po_numbers:
    set_field_value(document_data, "purchase_order", po_numbers[0])
```

---

## Datum/Uhrzeit-Funktionen

### datetime\_today()

Gibt das heutige Datum als `datetime`-Objekt zurück.

```python
today = datetime_today()
```

### datetime\_date

Die `date`-Klasse zur Datumserstellung.

```python
d = datetime_date(2026, 3, 25)  # date(2026, 3, 25)
```

### strptime()

Parst einen Datumsstring in ein datetime-Objekt.

```python
strptime(date_string, format)
```

**Beispiel — Rechnungsdatum parsen und verwenden:**

```python
inv_date_str = get_field_value(document_data, "invoice_date", "")
try:
    date_obj = strptime(inv_date_str, "%Y-%m-%d")
    year = date_obj.year
    month = date_obj.month
except ValueError:
    pass
```

### strftime()

Formatiert ein datetime-Objekt als String.

```python
strftime(datetime_obj, format)
```

**Beispiel — Verarbeitungsdatum setzen:**

```python
today = datetime_today()
formatted = strftime(today, "%d.%m.%Y")  # "25.03.2026"
set_field_value(document_data, "processing_date", formatted)
```

### fromisocalendar()

Erstellt ein Datum aus der ISO-Kalenderwoche.

```python
fromisocalendar(year, week, day)
```

**Beispiel — Kalenderwoche in Datum umwandeln:**

```python
# KW 12/2026, Montag
d = fromisocalendar(2026, 12, 1)  # date(2026, 3, 16)
set_date_value(document_data, "delivery_date", str(d))
```

{% hint style="success" %}
**Häufig bei deutschen Kunden:** Liefertermine werden oft als "KW 12" angegeben. Muster:

```python
content = get_document_content(document_data)
match = re_search(r"KW\s*(\d{1,2})[/\s]*(\d{4})", content)
if match:
    week = int(match.group(1))
    year = int(match.group(2))
    d = fromisocalendar(year, week, 1)  # Montag der KW
    set_date_value(document_data, "delivery_date", str(d))
```
{% endhint %}

### calendar\_monthrange()

Gibt den Wochentag des 1. und die Anzahl der Tage eines Monats zurück.

```python
weekday_of_first, num_days = calendar_monthrange(year, month)
```

**Beispiel:**

```python
_, days_in_month = calendar_monthrange(2026, 2)
# days_in_month = 28
```

---

## Dezimal-/Locale-Funktionen

### parse\_decimal()

Parst einen String zu einer Dezimalzahl mit Locale-Erkennung.

```python
parse_decimal(value, locale="en_US")
```

**Beispiel:**

```python
amount = parse_decimal("1.234,56", "de_DE")  # → Decimal('1234.56')
amount = parse_decimal("1,234.56", "en_US")  # → Decimal('1234.56')
```

### format\_decimal\_to\_locale()

Formatiert eine Dezimalzahl gemäß Locale.

```python
format_decimal_to_locale(value, locale)
```

**Beispiel:**

```python
formatted = format_decimal_to_locale(1234.56, "de_DE")  # → "1.234,56"
formatted = format_decimal_to_locale(1234.56, "en_US")  # → "1,234.56"
```

---

## Mathematische Funktionen

Das vollständige `math`-Modul ist verfügbar:

| Funktion | Beschreibung |
| -------- | ------------ |
| `abs(x)` | Absolutwert |
| `round(x, n)` | Auf n Dezimalstellen runden |
| `floor(x)` | Abrunden |
| `ceil(x)` | Aufrunden |
| `sqrt(x)` | Quadratwurzel |
| `pow(x, y)` | Potenz |
| `log(x)` / `log10(x)` | Logarithmus |
| `pi` | π (3,14159...) |
| `e` | Eulersche Zahl (2,71828...) |
| `sin`, `cos`, `tan` | Trigonometrie |
| `acos`, `asin`, `atan` | Inverse Trigonometrie |
| `degrees`, `radians` | Grad ↔ Bogenmaß |
| `exp`, `fabs`, `fmod` | Weitere mathematische Funktionen |
| `hypot`, `ldexp`, `frexp` | Spezialberechnungen |
| `modf` | Ganzzahl-/Dezimalteil trennen |

---

## Datenstruktur-Funktionen

```python
dict()            # Neues Dictionary
list()            # Neue Liste
set()             # Neues Set
tuple()           # Neues Tuple
defaultdict(type) # collections.defaultdict

len(x)            # Länge
isinstance(x, t)  # Typprüfung
type(x)           # Typ ermitteln
deepcopy(x)       # Tiefe Kopie (copy.deepcopy)

print(x)          # Debug-Ausgabe (nur zum Testen)
```

{% hint style="warning" %}
`print()` ist nur zu Debug-Zwecken verfügbar. Die Ausgabe geht in das Server-Log, nicht zum Benutzer.
{% endhint %}
