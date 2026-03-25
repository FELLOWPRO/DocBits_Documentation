# Fonctions de Recherche Fulltext et Vectorielle

{% hint style="info" %}
**Disponible à partir de la version 11.48.0**

Ces fonctions nécessitent que la licence/préférence **OPENSEARCH\_ENABLED** soit activée pour votre organisation. Sans activation, toutes les fonctions lèvent une `RuntimeError("Fulltext search license is missing")`.
{% endhint %}

Fonctions pour rechercher dans les archives de documents, trouver des documents similaires et interroger les données de référence ERP. Elles recherchent dans **tous les documents** de l'organisation — contrairement à `get_document_content()` qui ne lit que le texte du document actuel.

{% hint style="success" %}
**Security:** The `org_id` is automatically injected by the script sandbox. You never need to pass it — your scripts always operate within your own organization's data.
{% endhint %}

**Source :** `module/script/helper/document_script_functions.py`

---

## fulltext\_search()

Recherche dans le texte OCR complet de **tous les documents** de l'organisation.

```python
fulltext_search(query, **kwargs)
```

**Paramètres :**

| Nom | Type | Défaut | Description |
| --- | ---- | ------ | ----------- |
| `query` | `str` | obligatoire | Terme de recherche (recherché dans le texte OCR de tous les documents) |
| `search_type` | `str` | `"match_phrase"` | `"match_phrase"` (phrase exacte), `"fuzzy"` (tolérant aux erreurs, jusqu'à 2 caractères de différence), `"prefix"` (commence par) |
| `doc_type` | `str` | `None` | Filtrer par type de document (séparé par des virgules, ex. `"INVOICE,CREDIT_NOTE"`) |
| `status` | `str` | `None` | Filtrer par statut de document (séparé par des virgules, ex. `"ready_for_validation,exported"`) |
| `vendor_name` | `str` | `None` | Filtrer par nom du fournisseur |
| `date_range` | `str` | `None` | `"last_30_days"`, `"last_90_days"`, `"last_180_days"`, `"last_365_days"` |
| `size` | `int` | `10` | Nb. max de résultats (limité à 50) |

**Retourne :** `list[dict]` — Chaque dict contient :

| Champ | Description |
| ----- | ----------- |
| `doc_id` | UUID du document |
| `name` | Nom du fichier (ex. `"INV-2026-001.pdf"`) |
| `doc_type` | Type de document (`"INVOICE"`, `"ORDER_CONFIRMATION"`, etc.) |
| `vendor_name` | Nom du fournisseur |
| `status` | Statut du document |
| `total_amount` | Montant total |
| `ocr_content` | Extrait de texte correspondant du document |
| `highlights` | Dict avec les correspondances surlignées par champ |

**Exemple — Recherche de phrase exacte :**

```python
results = fulltext_search("REVERSE CHARGE",
                          doc_type="INVOICE", size=10)
for doc in results:
    print(doc["name"], doc["ocr_content"])
```

**Exemple — Recherche floue (tolérante aux erreurs OCR) :**

```python
results = fulltext_search("REVERSE CHARGE",
                          search_type="fuzzy",
                          vendor_name="ACME Corp")
```

**Exemple — Recherche par préfixe :**

```python
results = fulltext_search("Rechn", search_type="prefix",
                          date_range="last_90_days")
```

{% hint style="warning" %}
**Requête vide :** Passer une chaîne vide retourne `[]` immédiatement sans effectuer d'appel HTTP.
{% endhint %}

{% hint style="info" %}
**Gestion des erreurs :** Si le service fulltextsearch est inaccessible, la fonction retourne `[]` et enregistre un avertissement. Elle ne lève **pas** d'exception.
{% endhint %}

---

## vector\_search()

Trouve des documents sémantiquement similaires à l'aide d'embeddings vectoriels (recherche k-NN avec des vecteurs à 384 dimensions).

```python
vector_search(doc_id, **kwargs)
```

**Paramètres :**

| Nom | Type | Défaut | Description |
| --- | ---- | ------ | ----------- |
| `doc_id` | `str` | obligatoire | UUID du document source |
| `k` | `int` | `5` | Nombre de documents similaires à retourner (limité à 50) |

**Retourne :** `list[dict]` — Chaque dict contient : `doc_id`, `name`, `doc_type`, `similarity_score` (0-1), `similarity_percent` (0-100).

**Exemple :**

```python
doc_id = document_json["doc_id"]
similar = vector_search(doc_id, k=5)
for doc in similar:
    print(f"{doc['name']}: {doc['similarity_percent']}% similaire")
```

{% hint style="info" %}
**Fonctionnement :** Chaque document est converti en vecteur à 384 dimensions lors de l'indexation. La recherche vectorielle trouve les voisins les plus proches dans cet espace vectoriel.
{% endhint %}

---

## fulltext\_search\_erp()

Recherche dans les données de référence ERP (fournisseurs, commandes d'achat, clients, matériaux) indexées dans OpenSearch.

```python
fulltext_search_erp(query, **kwargs)
```

**Paramètres :**

| Nom | Type | Défaut | Description |
| --- | ---- | ------ | ----------- |
| `query` | `str` | obligatoire | Terme de recherche |
| `entity_types` | `str` | `None` | Filtrer par type d'entité (séparé par des virgules : `"vendor"`, `"purchase_order"`, `"customer"`, `"material"`) |
| `vendor_number` | `str` | `None` | Filtrer par numéro de fournisseur |
| `vendor_name` | `str` | `None` | Filtrer par nom du fournisseur |
| `company_code` | `str` | `None` | Filtrer par code société |
| `size` | `int` | `10` | Nb. max de résultats (limité à 50) |

**Exemple — Valider un fournisseur dans l'ERP :**

```python
vendor = get_field_value(document_data, "supplier_name", "")
if vendor:
    matches = fulltext_search_erp(vendor,
                                   entity_types="vendor", size=5)
    if not matches:
        set_field_as_invalid(document_data, "supplier_name",
                             "Fournisseur introuvable dans les données ERP")
```

---

## fulltext\_suggestions()

Retourne des suggestions d'autocomplétion pour les termes de recherche.

```python
fulltext_suggestions(query, **kwargs)
```

**Paramètres :**

| Nom | Type | Défaut | Description |
| --- | ---- | ------ | ----------- |
| `query` | `str` | obligatoire | Préfixe / terme de recherche |
| `limit` | `int` | `10` | Nb. max de suggestions par catégorie (limité à 20) |

**Exemple :**

```python
suggestions = fulltext_suggestions("ACM", limit=5)
vendor_list = suggestions.get("vendors", [])
```

---

## Référence Rapide

| Fonction | Objectif | Retourne |
| -------- | -------- | -------- |
| `fulltext_search(query, ...)` | Rechercher le texte OCR dans tous les documents | `list[dict]` |
| `vector_search(doc_id, ...)` | Trouver des documents sémantiquement similaires | `list[dict]` |
| `fulltext_search_erp(query, ...)` | Rechercher dans les données ERP | `list[dict]` |
| `fulltext_suggestions(query, ...)` | Suggestions d'autocomplétion | `dict` |

---

## Schémas Courants

### Vérification de Licence

```python
try:
    results = fulltext_search("test")
except RuntimeError:
    results = []
```

### Combinaison avec les Fonctions de Champ

```python
invoice_number = get_field_value(document_data, "invoice_id", "")
results = fulltext_search(invoice_number,
                          status="exported", size=1)
if results:
    set_field_as_invalid(document_data, "invoice_id",
                         f"Existe déjà : {results[0]['name']}")
else:
    set_field_as_valid(document_data, "invoice_id", "Aucun doublon trouvé")
```
