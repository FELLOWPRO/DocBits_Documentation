# Fonctions Utilitaires

Fonctions intégrées pour le traitement de chaînes, les mathématiques, les opérations de dates, les regex et les types de données.

**Source :** `module/script/helper/script_processor.py:get_allowed_functions_list()`

---

## Fonctions de chaînes

### Conversion de type

```python
str(value)       # Convertir en chaîne
int(value)       # Convertir en entier
float(value)     # Convertir en flottant
str_to_bool(s)   # "true"/"1"/"yes" → True, tout le reste → False
```

### Méthodes de chaînes

```python
lower(s)              # str.lower — "ABC" → "abc"
upper(s)              # str.upper — "abc" → "ABC"
split(s, sep)         # str.split — "a,b,c".split(",") → ["a","b","c"]
strip(s)              # str.strip — " abc " → "abc"
startswith(s, prefix) # str.startswith
endswith(s, suffix)   # str.endswith
```

{% hint style="info" %}
Celles-ci sont disponibles en tant que fonctions autonomes mais peuvent aussi être appelées comme méthodes sur les chaînes :

```python
# Les deux fonctionnent :
result = upper("hello")      # → "HELLO"
result = "hello".upper()     # → "HELLO"
```
{% endhint %}

---

## Correspondance floue de chaînes

### levenshtein\_distance()

Calcule la distance d'édition entre deux chaînes (nombre de modifications nécessaires).

```python
levenshtein_distance(s1, s2)
```

**Exemple :**

```python
dist = levenshtein_distance("ACME Corp", "ACME Corporation")
# dist = 7
if dist < 5:
    # Les chaînes sont suffisamment similaires
    pass
```

### jaro\_winkler\_similarity()

Calcule un score de similarité entre 0.0 et 1.0.

```python
jaro_winkler_similarity(s1, s2)
```

**Exemple :**

```python
score = jaro_winkler_similarity("Invoice", "Invocie")
# score ≈ 0.96 (très similaire, faute de frappe)

score = jaro_winkler_similarity("Invoice", "Receipt")
# score ≈ 0.45 (dissimilaire)
```

{% hint style="success" %}
**Quand utiliser laquelle ?**
- **Levenshtein** : Bon pour les chaînes courtes, nombre exact d'erreurs
- **Jaro-Winkler** : Meilleur pour les noms/adresses, pondère davantage les correspondances au début
{% endhint %}

---

## Fonctions Regex

Basées sur le module `re` de Python, mais disponibles en tant que fonctions autonomes.

### re\_search()

Recherche la première occurrence d'un motif.

```python
re_search(pattern, string)
```

**Retourne :** Objet Match ou `None`

**Exemple — Extraire un numéro de commande du texte intégral :**

```python
content = get_document_content(document_data)
match = re_search(r"Order number:\s*(\d+)", content)
if match:
    po_number = match.group(1)
    set_field_value(document_data, "purchase_order", po_number)
```

### re\_sub()

Remplace les correspondances de motif par une chaîne de remplacement.

```python
re_sub(pattern, replacement, string)
```

**Exemple — Supprimer les caractères spéciaux de l'ID de facture :**

```python
inv_id = get_field_value(document_data, "invoice_id", "")
cleaned = re_sub(r"[^A-Za-z0-9\-]", "", inv_id)
set_field_value(document_data, "invoice_id", cleaned)
```

### re\_findall()

Trouve toutes les occurrences d'un motif.

```python
re_findall(pattern, string)
```

**Exemple — Trouver tous les numéros de BC dans le document :**

```python
content = get_document_content(document_data)
po_numbers = re_findall(r"PO[- ]?\d{6,}", content)
if po_numbers:
    set_field_value(document_data, "purchase_order", po_numbers[0])
```

---

## Fonctions Date/Heure

### datetime\_today()

Retourne la date d'aujourd'hui en tant qu'objet `datetime`.

```python
today = datetime_today()
```

### datetime\_date

La classe `date` pour la création de dates.

```python
d = datetime_date(2026, 3, 25)  # date(2026, 3, 25)
```

### strptime()

Analyse une chaîne de date en un objet datetime.

```python
strptime(date_string, format)
```

**Exemple — Analyser et utiliser la date de facture :**

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

Formate un objet datetime en chaîne.

```python
strftime(datetime_obj, format)
```

**Exemple — Définir la date de traitement :**

```python
today = datetime_today()
formatted = strftime(today, "%d.%m.%Y")  # "25.03.2026"
set_field_value(document_data, "processing_date", formatted)
```

### fromisocalendar()

Crée une date à partir d'une semaine calendaire ISO.

```python
fromisocalendar(year, week, day)
```

**Exemple — Convertir une semaine calendaire en date :**

```python
# SC 12/2026, Lundi
d = fromisocalendar(2026, 12, 1)  # date(2026, 3, 16)
set_date_value(document_data, "delivery_date", str(d))
```

{% hint style="success" %}
**Courant avec les clients allemands :** Les dates de livraison sont souvent spécifiées comme "KW 12". Modèle :

```python
content = get_document_content(document_data)
match = re_search(r"KW\s*(\d{1,2})[/\s]*(\d{4})", content)
if match:
    week = int(match.group(1))
    year = int(match.group(2))
    d = fromisocalendar(year, week, 1)  # Lundi de la SC
    set_date_value(document_data, "delivery_date", str(d))
```
{% endhint %}

### calendar\_monthrange()

Retourne le jour de la semaine du 1er et le nombre de jours dans un mois.

```python
weekday_of_first, num_days = calendar_monthrange(year, month)
```

**Exemple :**

```python
_, days_in_month = calendar_monthrange(2026, 2)
# days_in_month = 28
```

---

## Fonctions Décimales/Locale

### parse\_decimal()

Analyse une chaîne en nombre décimal avec détection de la locale.

```python
parse_decimal(value, locale="en_US")
```

**Exemple :**

```python
amount = parse_decimal("1.234,56", "de_DE")  # → Decimal('1234.56')
amount = parse_decimal("1,234.56", "en_US")  # → Decimal('1234.56')
```

### format\_decimal\_to\_locale()

Formate un nombre décimal selon la locale.

```python
format_decimal_to_locale(value, locale)
```

**Exemple :**

```python
formatted = format_decimal_to_locale(1234.56, "de_DE")  # → "1.234,56"
formatted = format_decimal_to_locale(1234.56, "en_US")  # → "1,234.56"
```

---

## Fonctions mathématiques

Le module `math` complet est disponible :

| Fonction | Description |
| -------- | ----------- |
| `abs(x)` | Valeur absolue |
| `round(x, n)` | Arrondir à n décimales |
| `floor(x)` | Plancher (arrondi vers le bas) |
| `ceil(x)` | Plafond (arrondi vers le haut) |
| `sqrt(x)` | Racine carrée |
| `pow(x, y)` | Puissance |
| `log(x)` / `log10(x)` | Logarithme |
| `pi` | π (3.14159...) |
| `e` | Nombre d'Euler (2.71828...) |
| `sin`, `cos`, `tan` | Trigonométrie |
| `acos`, `asin`, `atan` | Trigonométrie inverse |
| `degrees`, `radians` | Degrés ↔ Radians |
| `exp`, `fabs`, `fmod` | Fonctions mathématiques supplémentaires |
| `hypot`, `ldexp`, `frexp` | Calculs spéciaux |
| `modf` | Séparer les parties entière/décimale |

---

## Fonctions de structures de données

```python
dict()            # Nouveau dictionnaire
list()            # Nouvelle liste
set()             # Nouvel ensemble
tuple()           # Nouveau tuple
defaultdict(type) # collections.defaultdict

len(x)            # Longueur
isinstance(x, t)  # Vérification de type
type(x)           # Obtenir le type
deepcopy(x)       # Copie profonde (copy.deepcopy)

print(x)          # Sortie de débogage (pour les tests uniquement)
```

{% hint style="warning" %}
`print()` n'est disponible qu'à des fins de débogage. La sortie va dans le journal du serveur, pas vers l'utilisateur.
{% endhint %}
