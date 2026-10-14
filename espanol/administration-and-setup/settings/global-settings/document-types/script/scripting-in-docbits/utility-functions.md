# Funciones de Utilidad

Funciones integradas para procesamiento de cadenas, matematicas, operaciones de fecha, regex y tipos de datos.

**Fuente:** `module/script/helper/script_processor.py:get_allowed_functions_list()`

---

## Funciones de Cadena

### Conversion de Tipos

```python
str(value)       # Convertir a cadena
int(value)       # Convertir a entero
float(value)     # Convertir a decimal
str_to_bool(s)   # "true"/"1"/"yes" -> True, todo lo demas -> False
```

### Metodos de Cadena

```python
lower(s)              # str.lower — "ABC" -> "abc"
upper(s)              # str.upper — "abc" -> "ABC"
split(s, sep)         # str.split — "a,b,c".split(",") -> ["a","b","c"]
strip(s)              # str.strip — " abc " -> "abc"
startswith(s, prefix) # str.startswith
endswith(s, suffix)   # str.endswith
```

{% hint style="info" %}
Estas estan disponibles como funciones independientes pero tambien pueden llamarse como metodos en cadenas:

```python
# Ambos funcionan:
result = upper("hello")      # -> "HELLO"
result = "hello".upper()     # -> "HELLO"
```
{% endhint %}

---

## Coincidencia Difusa de Cadenas

### levenshtein\_distance()

Calcula la distancia de edicion entre dos cadenas (numero de cambios necesarios).

```python
levenshtein_distance(s1, s2)
```

**Ejemplo:**

```python
dist = levenshtein_distance("ACME Corp", "ACME Corporation")
# dist = 7
if dist < 5:
    # Las cadenas son suficientemente similares
    pass
```

### jaro\_winkler\_similarity()

Calcula una puntuacion de similitud entre 0.0 y 1.0.

```python
jaro_winkler_similarity(s1, s2)
```

**Ejemplo:**

```python
score = jaro_winkler_similarity("Invoice", "Invocie")
# score ~ 0.96 (muy similar, error tipografico)

score = jaro_winkler_similarity("Invoice", "Receipt")
# score ~ 0.45 (disimilar)
```

{% hint style="success" %}
**Cuando usar cual?**
- **Levenshtein**: Bueno para cadenas cortas, conteo exacto de errores
- **Jaro-Winkler**: Mejor para nombres/direcciones, pondera mas las coincidencias al inicio
{% endhint %}

---

## Funciones Regex

Basadas en el modulo `re` de Python, pero disponibles como funciones independientes.

### re\_search()

Busca la primera ocurrencia de un patron.

```python
re_search(pattern, string)
```

**Retorna:** Objeto Match o `None`

**Ejemplo — Extraer numero de orden del texto completo:**

```python
content = get_document_content(document_data)
match = re_search(r"Order number:\s*(\d+)", content)
if match:
    po_number = match.group(1)
    set_field_value(document_data, "purchase_order", po_number)
```

### re\_sub()

Reemplaza coincidencias de patron con una cadena de reemplazo.

```python
re_sub(pattern, replacement, string)
```

**Ejemplo — Eliminar caracteres especiales del ID de factura:**

```python
inv_id = get_field_value(document_data, "invoice_id", "")
cleaned = re_sub(r"[^A-Za-z0-9\-]", "", inv_id)
set_field_value(document_data, "invoice_id", cleaned)
```

### re\_findall()

Encuentra todas las ocurrencias de un patron.

```python
re_findall(pattern, string)
```

**Ejemplo — Encontrar todos los numeros de OC en el documento:**

```python
content = get_document_content(document_data)
po_numbers = re_findall(r"PO[- ]?\d{6,}", content)
if po_numbers:
    set_field_value(document_data, "purchase_order", po_numbers[0])
```

---

## Funciones de Fecha/Hora

### datetime\_today()

Retorna la fecha de hoy como un objeto `datetime`.

```python
today = datetime_today()
```

### datetime\_date

La clase `date` para creacion de fechas.

```python
d = datetime_date(2026, 3, 25)  # date(2026, 3, 25)
```

### strptime()

Analiza una cadena de fecha en un objeto datetime.

```python
strptime(date_string, format)
```

**Ejemplo — Analizar y usar fecha de factura:**

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

Formatea un objeto datetime como cadena.

```python
strftime(datetime_obj, format)
```

**Ejemplo — Establecer fecha de procesamiento:**

```python
today = datetime_today()
formatted = strftime(today, "%d.%m.%Y")  # "25.03.2026"
set_field_value(document_data, "processing_date", formatted)
```

### fromisocalendar()

Crea una fecha a partir de la semana del calendario ISO.

```python
fromisocalendar(year, week, day)
```

**Ejemplo — Convertir semana del calendario a fecha:**

```python
# SC 12/2026, Lunes
d = fromisocalendar(2026, 12, 1)  # date(2026, 3, 16)
set_date_value(document_data, "delivery_date", str(d))
```

{% hint style="success" %}
**Comun con clientes alemanes:** Las fechas de entrega a menudo se especifican como "KW 12". Patron:

```python
content = get_document_content(document_data)
match = re_search(r"KW\s*(\d{1,2})[/\s]*(\d{4})", content)
if match:
    week = int(match.group(1))
    year = int(match.group(2))
    d = fromisocalendar(year, week, 1)  # Lunes de la SC
    set_date_value(document_data, "delivery_date", str(d))
```
{% endhint %}

### calendar\_monthrange()

Retorna el dia de la semana del 1ro y el numero de dias en un mes.

```python
weekday_of_first, num_days = calendar_monthrange(year, month)
```

**Ejemplo:**

```python
_, days_in_month = calendar_monthrange(2026, 2)
# days_in_month = 28
```

---

## Funciones Decimal/Regional

### parse\_decimal()

Analiza una cadena a un numero decimal con deteccion de configuracion regional.

```python
parse_decimal(value, locale="en_US")
```

**Ejemplo:**

```python
amount = parse_decimal("1.234,56", "de_DE")  # -> Decimal('1234.56')
amount = parse_decimal("1,234.56", "en_US")  # -> Decimal('1234.56')
```

### format\_decimal\_to\_locale()

Formatea un numero decimal segun la configuracion regional.

```python
format_decimal_to_locale(value, locale)
```

**Ejemplo:**

```python
formatted = format_decimal_to_locale(1234.56, "de_DE")  # -> "1.234,56"
formatted = format_decimal_to_locale(1234.56, "en_US")  # -> "1,234.56"
```

---

## Funciones Matematicas

El modulo completo `math` esta disponible:

| Funcion | Descripcion |
| -------- | ----------- |
| `abs(x)` | Valor absoluto |
| `round(x, n)` | Redondear a n decimales |
| `floor(x)` | Piso (redondear hacia abajo) |
| `ceil(x)` | Techo (redondear hacia arriba) |
| `sqrt(x)` | Raiz cuadrada |
| `pow(x, y)` | Potencia |
| `log(x)` / `log10(x)` | Logaritmo |
| `pi` | Pi (3.14159...) |
| `e` | Numero de Euler (2.71828...) |
| `sin`, `cos`, `tan` | Trigonometria |
| `acos`, `asin`, `atan` | Trigonometria inversa |
| `degrees`, `radians` | Grados <-> Radianes |
| `exp`, `fabs`, `fmod` | Funciones matematicas adicionales |
| `hypot`, `ldexp`, `frexp` | Calculos especiales |
| `modf` | Separar partes entera/decimal |

---

## Funciones de Estructura de Datos

```python
dict()            # Nuevo diccionario
list()            # Nueva lista
set()             # Nuevo conjunto
tuple()           # Nueva tupla
defaultdict(type) # collections.defaultdict

len(x)            # Longitud
isinstance(x, t)  # Verificacion de tipo
type(x)           # Obtener tipo
deepcopy(x)       # Copia profunda (copy.deepcopy)

print(x)          # Salida de depuracion (solo para pruebas)
```

{% hint style="warning" %}
`print()` solo esta disponible para fines de depuracion. La salida va al log del servidor, no al usuario.
{% endhint %}
