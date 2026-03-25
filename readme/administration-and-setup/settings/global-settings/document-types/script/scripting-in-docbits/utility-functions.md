# Funkcje Pomocnicze

Wbudowane funkcje do przetwarzania ciagow znakow, matematyki, operacji na datach, wyrazen regularnych i typow danych.

**Zrodlo:** `module/script/helper/script_processor.py:get_allowed_functions_list()`

---

## Funkcje ciagow znakow

### Konwersja typow

```python
str(value)       # Konwersja na ciag znakow
int(value)       # Konwersja na liczbe calkowita
float(value)     # Konwersja na liczbe zmiennoprzecinkowa
str_to_bool(s)   # "true"/"1"/"yes" -> True, wszystko inne -> False
```

### Metody ciagow znakow

```python
lower(s)              # str.lower — "ABC" -> "abc"
upper(s)              # str.upper — "abc" -> "ABC"
split(s, sep)         # str.split — "a,b,c".split(",") -> ["a","b","c"]
strip(s)              # str.strip — " abc " -> "abc"
startswith(s, prefix) # str.startswith
endswith(s, suffix)   # str.endswith
```

{% hint style="info" %}
Te funkcje sa dostepne jako samodzielne, ale moga byc tez wywoływane jako metody na ciagach znakow:

```python
# Oba dzialaja:
result = upper("hello")      # -> "HELLO"
result = "hello".upper()     # -> "HELLO"
```
{% endhint %}

---

## Rozmyte dopasowywanie ciagow znakow

### levenshtein\_distance()

Oblicza odleglosc edycyjna miedzy dwoma ciagami znakow (liczba potrzebnych zmian).

```python
levenshtein_distance(s1, s2)
```

**Przyklad:**

```python
dist = levenshtein_distance("ACME Corp", "ACME Corporation")
# dist = 7
if dist < 5:
    # Ciagi sa wystarczajaco podobne
    pass
```

### jaro\_winkler\_similarity()

Oblicza wynik podobienstwa miedzy 0.0 a 1.0.

```python
jaro_winkler_similarity(s1, s2)
```

**Przyklad:**

```python
score = jaro_winkler_similarity("Invoice", "Invocie")
# score ~ 0.96 (bardzo podobne, literowka)

score = jaro_winkler_similarity("Invoice", "Receipt")
# score ~ 0.45 (niepodobne)
```

{% hint style="success" %}
**Kiedy uzywac ktorej?**
- **Levenshtein**: Dobre dla krotkich ciagow znakow, dokladna liczba bledow
- **Jaro-Winkler**: Lepsze dla nazw/adresow, wiecej wagi przykladanej do dopasowania na poczatku
{% endhint %}

---

## Funkcje wyrazen regularnych

Oparte na module Pythona `re`, ale dostepne jako samodzielne funkcje.

### re\_search()

Wyszukuje pierwsze wystapienie wzorca.

```python
re_search(pattern, string)
```

**Zwraca:** Obiekt Match lub `None`

**Przyklad — Wyodrebnianie numeru zamowienia z pelnego tekstu:**

```python
content = get_document_content(document_data)
match = re_search(r"Order number:\s*(\d+)", content)
if match:
    po_number = match.group(1)
    set_field_value(document_data, "purchase_order", po_number)
```

### re\_sub()

Zastepuje dopasowania wzorca ciagiem zastepczym.

```python
re_sub(pattern, replacement, string)
```

**Przyklad — Usuwanie znakow specjalnych z ID faktury:**

```python
inv_id = get_field_value(document_data, "invoice_id", "")
cleaned = re_sub(r"[^A-Za-z0-9\-]", "", inv_id)
set_field_value(document_data, "invoice_id", cleaned)
```

### re\_findall()

Znajduje wszystkie wystapienia wzorca.

```python
re_findall(pattern, string)
```

**Przyklad — Znajdz wszystkie numery ZZ w dokumencie:**

```python
content = get_document_content(document_data)
po_numbers = re_findall(r"PO[- ]?\d{6,}", content)
if po_numbers:
    set_field_value(document_data, "purchase_order", po_numbers[0])
```

---

## Funkcje daty/czasu

### datetime\_today()

Zwraca dzisiejsza date jako obiekt `datetime`.

```python
today = datetime_today()
```

### datetime\_date

Klasa `date` do tworzenia dat.

```python
d = datetime_date(2026, 3, 25)  # date(2026, 3, 25)
```

### strptime()

Parsuje ciag znakow daty na obiekt datetime.

```python
strptime(date_string, format)
```

**Przyklad — Parsowanie i uzycie daty faktury:**

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

Formatuje obiekt datetime jako ciag znakow.

```python
strftime(datetime_obj, format)
```

**Przyklad — Ustawienie daty przetwarzania:**

```python
today = datetime_today()
formatted = strftime(today, "%d.%m.%Y")  # "25.03.2026"
set_field_value(document_data, "processing_date", formatted)
```

### fromisocalendar()

Tworzy date z kalendarza ISO (tydzien kalendarzowy).

```python
fromisocalendar(year, week, day)
```

**Przyklad — Konwersja tygodnia kalendarzowego na date:**

```python
# Tydzien 12/2026, Poniedzialek
d = fromisocalendar(2026, 12, 1)  # date(2026, 3, 16)
set_date_value(document_data, "delivery_date", str(d))
```

{% hint style="success" %}
**Czeste u klientow niemieckich:** Daty dostawy sa czesto podawane jako "KW 12". Wzorzec:

```python
content = get_document_content(document_data)
match = re_search(r"KW\s*(\d{1,2})[/\s]*(\d{4})", content)
if match:
    week = int(match.group(1))
    year = int(match.group(2))
    d = fromisocalendar(year, week, 1)  # Poniedzialek tygodnia kalendarzowego
    set_date_value(document_data, "delivery_date", str(d))
```
{% endhint %}

### calendar\_monthrange()

Zwraca dzien tygodnia 1. dnia miesiaca i liczbe dni w miesiacu.

```python
weekday_of_first, num_days = calendar_monthrange(year, month)
```

**Przyklad:**

```python
_, days_in_month = calendar_monthrange(2026, 2)
# days_in_month = 28
```

---

## Funkcje Decimal/Locale

### parse\_decimal()

Parsuje ciag znakow na liczbe dziesietna z wykrywaniem lokalizacji.

```python
parse_decimal(value, locale="en_US")
```

**Przyklad:**

```python
amount = parse_decimal("1.234,56", "de_DE")  # -> Decimal('1234.56')
amount = parse_decimal("1,234.56", "en_US")  # -> Decimal('1234.56')
```

### format\_decimal\_to\_locale()

Formatuje liczbe dziesietna zgodnie z lokalizacja.

```python
format_decimal_to_locale(value, locale)
```

**Przyklad:**

```python
formatted = format_decimal_to_locale(1234.56, "de_DE")  # -> "1.234,56"
formatted = format_decimal_to_locale(1234.56, "en_US")  # -> "1,234.56"
```

---

## Funkcje matematyczne

Dostepny jest pelny modul `math`:

| Funkcja | Opis |
| -------- | ----------- |
| `abs(x)` | Wartosc bezwzgledna |
| `round(x, n)` | Zaokraglenie do n miejsc po przecinku |
| `floor(x)` | Podloga (zaokraglenie w dol) |
| `ceil(x)` | Sufit (zaokraglenie w gore) |
| `sqrt(x)` | Pierwiastek kwadratowy |
| `pow(x, y)` | Potega |
| `log(x)` / `log10(x)` | Logarytm |
| `pi` | Pi (3.14159...) |
| `e` | Liczba Eulera (2.71828...) |
| `sin`, `cos`, `tan` | Trygonometria |
| `acos`, `asin`, `atan` | Odwrotna trygonometria |
| `degrees`, `radians` | Stopnie <-> Radiany |
| `exp`, `fabs`, `fmod` | Dodatkowe funkcje matematyczne |
| `hypot`, `ldexp`, `frexp` | Obliczenia specjalne |
| `modf` | Rozdzielenie czesci calkowitej/dziesietnej |

---

## Funkcje struktur danych

```python
dict()            # Nowy slownik
list()            # Nowa lista
set()             # Nowy zbior
tuple()           # Nowa krotka
defaultdict(type) # collections.defaultdict

len(x)            # Dlugosc
isinstance(x, t)  # Sprawdzenie typu
type(x)           # Pobierz typ
deepcopy(x)       # Glebokie kopiowanie (copy.deepcopy)

print(x)          # Wyjscie debugowania (tylko do testow)
```

{% hint style="warning" %}
`print()` jest dostepne tylko do celow debugowania. Wyjscie trafia do logu serwera, nie do uzytkownika.
{% endhint %}
