# Funzioni di Utilita

Funzioni integrate per l'elaborazione di stringhe, matematica, operazioni con date, regex e tipi di dati.

**Sorgente:** `module/script/helper/script_processor.py:get_allowed_functions_list()`

---

## Funzioni Stringa

### Conversione di Tipo

```python
str(value)       # Converti in stringa
int(value)       # Converti in intero
float(value)     # Converti in numero a virgola mobile
str_to_bool(s)   # "true"/"1"/"yes" → True, tutto il resto → False
```

### Metodi Stringa

```python
lower(s)              # str.lower — "ABC" → "abc"
upper(s)              # str.upper — "abc" → "ABC"
split(s, sep)         # str.split — "a,b,c".split(",") → ["a","b","c"]
strip(s)              # str.strip — " abc " → "abc"
startswith(s, prefix) # str.startswith
endswith(s, suffix)   # str.endswith
```

{% hint style="info" %}
Queste sono disponibili come funzioni autonome ma possono anche essere chiamate come metodi sulle stringhe:

```python
# Entrambi funzionano:
result = upper("hello")      # → "HELLO"
result = "hello".upper()     # → "HELLO"
```
{% endhint %}

---

## Corrispondenza Approssimativa di Stringhe

### levenshtein\_distance()

Calcola la distanza di modifica tra due stringhe (numero di modifiche necessarie).

```python
levenshtein_distance(s1, s2)
```

**Esempio:**

```python
dist = levenshtein_distance("ACME Corp", "ACME Corporation")
# dist = 7
if dist < 5:
    # Le stringhe sono abbastanza simili
    pass
```

### jaro\_winkler\_similarity()

Calcola un punteggio di similarita tra 0.0 e 1.0.

```python
jaro_winkler_similarity(s1, s2)
```

**Esempio:**

```python
score = jaro_winkler_similarity("Invoice", "Invocie")
# score ≈ 0.96 (molto simile, errore di battitura)

score = jaro_winkler_similarity("Invoice", "Receipt")
# score ≈ 0.45 (dissimile)
```

{% hint style="success" %}
**Quando usare quale?**
- **Levenshtein**: Buono per stringhe brevi, conteggio esatto degli errori
- **Jaro-Winkler**: Migliore per nomi/indirizzi, pesa maggiormente le corrispondenze all'inizio
{% endhint %}

---

## Funzioni Regex

Basate sul modulo `re` di Python, ma disponibili come funzioni autonome.

### re\_search()

Cerca la prima occorrenza di un pattern.

```python
re_search(pattern, string)
```

**Restituisce:** Oggetto Match oppure `None`

**Esempio — Estrarre il numero d'ordine dal testo completo:**

```python
content = get_document_content(document_data)
match = re_search(r"Order number:\s*(\d+)", content)
if match:
    po_number = match.group(1)
    set_field_value(document_data, "purchase_order", po_number)
```

### re\_sub()

Sostituisce le corrispondenze del pattern con una stringa di sostituzione.

```python
re_sub(pattern, replacement, string)
```

**Esempio — Rimuovere caratteri speciali dall'ID fattura:**

```python
inv_id = get_field_value(document_data, "invoice_id", "")
cleaned = re_sub(r"[^A-Za-z0-9\-]", "", inv_id)
set_field_value(document_data, "invoice_id", cleaned)
```

### re\_findall()

Trova tutte le occorrenze di un pattern.

```python
re_findall(pattern, string)
```

**Esempio — Trovare tutti i numeri OA nel documento:**

```python
content = get_document_content(document_data)
po_numbers = re_findall(r"PO[- ]?\d{6,}", content)
if po_numbers:
    set_field_value(document_data, "purchase_order", po_numbers[0])
```

---

## Funzioni Data/Ora

### datetime\_today()

Restituisce la data odierna come oggetto `datetime`.

```python
today = datetime_today()
```

### datetime\_date

La classe `date` per la creazione di date.

```python
d = datetime_date(2026, 3, 25)  # date(2026, 3, 25)
```

### strptime()

Analizza una stringa data in un oggetto datetime.

```python
strptime(date_string, format)
```

**Esempio — Analizzare e utilizzare la data fattura:**

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

Formatta un oggetto datetime come stringa.

```python
strftime(datetime_obj, format)
```

**Esempio — Impostare la data di elaborazione:**

```python
today = datetime_today()
formatted = strftime(today, "%d.%m.%Y")  # "25.03.2026"
set_field_value(document_data, "processing_date", formatted)
```

### fromisocalendar()

Crea una data dalla settimana del calendario ISO.

```python
fromisocalendar(year, week, day)
```

**Esempio — Convertire la settimana del calendario in data:**

```python
# Settimana 12/2026, Lunedi
d = fromisocalendar(2026, 12, 1)  # date(2026, 3, 16)
set_date_value(document_data, "delivery_date", str(d))
```

{% hint style="success" %}
**Comune con i clienti tedeschi:** Le date di consegna sono spesso specificate come "KW 12". Pattern:

```python
content = get_document_content(document_data)
match = re_search(r"KW\s*(\d{1,2})[/\s]*(\d{4})", content)
if match:
    week = int(match.group(1))
    year = int(match.group(2))
    d = fromisocalendar(year, week, 1)  # Lunedi della settimana
    set_date_value(document_data, "delivery_date", str(d))
```
{% endhint %}

### calendar\_monthrange()

Restituisce il giorno della settimana del 1o e il numero di giorni in un mese.

```python
weekday_of_first, num_days = calendar_monthrange(year, month)
```

**Esempio:**

```python
_, days_in_month = calendar_monthrange(2026, 2)
# days_in_month = 28
```

---

## Funzioni Decimali/Localizzazione

### parse\_decimal()

Analizza una stringa in un numero decimale con rilevamento della localizzazione.

```python
parse_decimal(value, locale="en_US")
```

**Esempio:**

```python
amount = parse_decimal("1.234,56", "de_DE")  # → Decimal('1234.56')
amount = parse_decimal("1,234.56", "en_US")  # → Decimal('1234.56')
```

### format\_decimal\_to\_locale()

Formatta un numero decimale secondo la localizzazione.

```python
format_decimal_to_locale(value, locale)
```

**Esempio:**

```python
formatted = format_decimal_to_locale(1234.56, "de_DE")  # → "1.234,56"
formatted = format_decimal_to_locale(1234.56, "en_US")  # → "1,234.56"
```

---

## Funzioni Matematiche

Il modulo `math` completo e disponibile:

| Funzione | Descrizione |
| -------- | ----------- |
| `abs(x)` | Valore assoluto |
| `round(x, n)` | Arrotonda a n cifre decimali |
| `floor(x)` | Arrotondamento per difetto |
| `ceil(x)` | Arrotondamento per eccesso |
| `sqrt(x)` | Radice quadrata |
| `pow(x, y)` | Potenza |
| `log(x)` / `log10(x)` | Logaritmo |
| `pi` | π (3,14159...) |
| `e` | Numero di Eulero (2,71828...) |
| `sin`, `cos`, `tan` | Trigonometria |
| `acos`, `asin`, `atan` | Trigonometria inversa |
| `degrees`, `radians` | Gradi ↔ Radianti |
| `exp`, `fabs`, `fmod` | Funzioni matematiche aggiuntive |
| `hypot`, `ldexp`, `frexp` | Calcoli speciali |
| `modf` | Separare parti intere/decimali |

---

## Funzioni Strutture Dati

```python
dict()            # Nuovo dizionario
list()            # Nuova lista
set()             # Nuovo insieme
tuple()           # Nuova tupla
defaultdict(type) # collections.defaultdict

len(x)            # Lunghezza
isinstance(x, t)  # Controllo tipo
type(x)           # Ottieni tipo
deepcopy(x)       # Copia profonda (copy.deepcopy)

print(x)          # Output di debug (solo per test)
```

{% hint style="warning" %}
`print()` e disponibile solo per scopi di debug. L'output va nel log del server, non all'utente.
{% endhint %}
