# Funções Utilitárias

Funções integradas para processamento de strings, matemática, operações com datas, regex e tipos de dados.

**Fonte:** `module/script/helper/script_processor.py:get_allowed_functions_list()`

---

## Funções de String

### Conversão de Tipo

```python
str(value)       # Converter para string
int(value)       # Converter para inteiro
float(value)     # Converter para float
str_to_bool(s)   # "true"/"1"/"yes" → True, tudo o resto → False
```

### Métodos de String

```python
lower(s)              # str.lower — "ABC" → "abc"
upper(s)              # str.upper — "abc" → "ABC"
split(s, sep)         # str.split — "a,b,c".split(",") → ["a","b","c"]
strip(s)              # str.strip — " abc " → "abc"
startswith(s, prefix) # str.startswith
endswith(s, suffix)   # str.endswith
```

{% hint style="info" %}
Estas estão disponíveis como funções autónomas, mas também podem ser chamadas como métodos em strings:

```python
# Ambos funcionam:
result = upper("hello")      # → "HELLO"
result = "hello".upper()     # → "HELLO"
```
{% endhint %}

---

## Correspondência Difusa de Strings

### levenshtein\_distance()

Calcula a distância de edição entre duas strings (número de alterações necessárias).

```python
levenshtein_distance(s1, s2)
```

**Exemplo:**

```python
dist = levenshtein_distance("ACME Corp", "ACME Corporation")
# dist = 7
if dist < 5:
    # As strings são suficientemente semelhantes
    pass
```

### jaro\_winkler\_similarity()

Calcula uma pontuação de semelhança entre 0.0 e 1.0.

```python
jaro_winkler_similarity(s1, s2)
```

**Exemplo:**

```python
score = jaro_winkler_similarity("Invoice", "Invocie")
# score ≈ 0.96 (muito semelhante, erro de digitação)

score = jaro_winkler_similarity("Invoice", "Receipt")
# score ≈ 0.45 (dissemelhante)
```

{% hint style="success" %}
**Quando usar qual?**
- **Levenshtein**: Bom para strings curtas, contagem exata de erros
- **Jaro-Winkler**: Melhor para nomes/endereços, dá mais peso a correspondências no início
{% endhint %}

---

## Funções de Regex

Baseadas no módulo `re` do Python, mas disponíveis como funções autónomas.

### re\_search()

Pesquisa a primeira ocorrência de um padrão.

```python
re_search(pattern, string)
```

**Retorna:** Objeto Match ou `None`

**Exemplo — Extrair número de encomenda do texto completo:**

```python
content = get_document_content(document_data)
match = re_search(r"Order number:\s*(\d+)", content)
if match:
    po_number = match.group(1)
    set_field_value(document_data, "purchase_order", po_number)
```

### re\_sub()

Substitui correspondências de padrão por uma string de substituição.

```python
re_sub(pattern, replacement, string)
```

**Exemplo — Remover caracteres especiais do ID da fatura:**

```python
inv_id = get_field_value(document_data, "invoice_id", "")
cleaned = re_sub(r"[^A-Za-z0-9\-]", "", inv_id)
set_field_value(document_data, "invoice_id", cleaned)
```

### re\_findall()

Encontra todas as ocorrências de um padrão.

```python
re_findall(pattern, string)
```

**Exemplo — Encontrar todos os números de OC no documento:**

```python
content = get_document_content(document_data)
po_numbers = re_findall(r"PO[- ]?\d{6,}", content)
if po_numbers:
    set_field_value(document_data, "purchase_order", po_numbers[0])
```

---

## Funções de Data/Hora

### datetime\_today()

Retorna a data de hoje como objeto `datetime`.

```python
today = datetime_today()
```

### datetime\_date

A classe `date` para criação de datas.

```python
d = datetime_date(2026, 3, 25)  # date(2026, 3, 25)
```

### strptime()

Analisa uma string de data num objeto datetime.

```python
strptime(date_string, format)
```

**Exemplo — Analisar e usar data da fatura:**

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

Formata um objeto datetime como string.

```python
strftime(datetime_obj, format)
```

**Exemplo — Definir data de processamento:**

```python
today = datetime_today()
formatted = strftime(today, "%d.%m.%Y")  # "25.03.2026"
set_field_value(document_data, "processing_date", formatted)
```

### fromisocalendar()

Cria uma data a partir da semana do calendário ISO.

```python
fromisocalendar(year, week, day)
```

**Exemplo — Converter semana do calendário em data:**

```python
# SC 12/2026, Segunda-feira
d = fromisocalendar(2026, 12, 1)  # date(2026, 3, 16)
set_date_value(document_data, "delivery_date", str(d))
```

{% hint style="success" %}
**Comum com clientes alemães:** Datas de entrega são frequentemente especificadas como "KW 12". Padrão:

```python
content = get_document_content(document_data)
match = re_search(r"KW\s*(\d{1,2})[/\s]*(\d{4})", content)
if match:
    week = int(match.group(1))
    year = int(match.group(2))
    d = fromisocalendar(year, week, 1)  # Segunda-feira da SC
    set_date_value(document_data, "delivery_date", str(d))
```
{% endhint %}

### calendar\_monthrange()

Retorna o dia da semana do 1.º dia e o número de dias num mês.

```python
weekday_of_first, num_days = calendar_monthrange(year, month)
```

**Exemplo:**

```python
_, days_in_month = calendar_monthrange(2026, 2)
# days_in_month = 28
```

---

## Funções Decimal/Localidade

### parse\_decimal()

Analisa uma string para um número decimal com deteção de localidade.

```python
parse_decimal(value, locale="en_US")
```

**Exemplo:**

```python
amount = parse_decimal("1.234,56", "de_DE")  # → Decimal('1234.56')
amount = parse_decimal("1,234.56", "en_US")  # → Decimal('1234.56')
```

### format\_decimal\_to\_locale()

Formata um número decimal de acordo com a localidade.

```python
format_decimal_to_locale(value, locale)
```

**Exemplo:**

```python
formatted = format_decimal_to_locale(1234.56, "de_DE")  # → "1.234,56"
formatted = format_decimal_to_locale(1234.56, "en_US")  # → "1,234.56"
```

---

## Funções Matemáticas

O módulo `math` completo está disponível:

| Função | Descrição |
| -------- | ----------- |
| `abs(x)` | Valor absoluto |
| `round(x, n)` | Arredondar para n casas decimais |
| `floor(x)` | Arredondar para baixo |
| `ceil(x)` | Arredondar para cima |
| `sqrt(x)` | Raiz quadrada |
| `pow(x, y)` | Potência |
| `log(x)` / `log10(x)` | Logaritmo |
| `pi` | π (3.14159...) |
| `e` | Número de Euler (2.71828...) |
| `sin`, `cos`, `tan` | Trigonometria |
| `acos`, `asin`, `atan` | Trigonometria inversa |
| `degrees`, `radians` | Graus ↔ Radianos |
| `exp`, `fabs`, `fmod` | Funções matemáticas adicionais |
| `hypot`, `ldexp`, `frexp` | Cálculos especiais |
| `modf` | Separar partes inteira/decimal |

---

## Funções de Estruturas de Dados

```python
dict()            # Novo dicionário
list()            # Nova lista
set()             # Novo conjunto
tuple()           # Novo tuplo
defaultdict(type) # collections.defaultdict

len(x)            # Comprimento
isinstance(x, t)  # Verificação de tipo
type(x)           # Obter tipo
deepcopy(x)       # Cópia profunda (copy.deepcopy)

print(x)          # Saída de depuração (apenas para testes)
```

{% hint style="warning" %}
`print()` está disponível apenas para fins de depuração. A saída vai para o log do servidor, não para o utilizador.
{% endhint %}
