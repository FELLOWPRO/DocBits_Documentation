# Fonctions de recherche Fulltext et vectorielle

{% hint style="info" %}
**Disponible à partir de la version 11.48.0**

Ces fonctions nécessitent que la licence/préférence **OPENSEARCH\_ENABLED** soit activée pour votre organisation. Sans activation, toutes les fonctions lèvent une `RuntimeError("Fulltext search license is missing")`.
{% endhint %}

Fonctions pour rechercher dans les archives de documents, trouver des documents similaires et interroger les données de référence ERP. Elles recherchent dans **tous les documents** de l'organisation, contrairement à `get_document_content()` qui ne lit que le texte du document actuel.

{% hint style="success" %}
**Sécurité :** L'`org_id` est injecté automatiquement par le bac à sable des scripts. Vous n'avez jamais besoin de le transmettre : vos scripts opèrent toujours dans les données de votre propre organisation.
{% endhint %}

**Source :** `module/script/helper/document_script_functions.py`

---

## fulltext\_search()

Recherche dans le texte OCR complet de **tous les documents** de l'organisation. Trouve du texte dans les champs `pages.pageText`, `tfidfCustomPageText` et `ai_text` via le microservice fulltextsearch.

```python
fulltext_search(query, **kwargs)
```

**Paramètres :**

| Nom | Type | Défaut | Description |
| ---- | ---- | ------- | ----------- |
| `query` | `str` | obligatoire | Terme de recherche (recherché dans le texte OCR de tous les documents) |
| `search_type` | `str` | `"match_phrase"` | `"match_phrase"` (phrase exacte), `"fuzzy"` (tolérant aux fautes, jusqu'à 2 caractères de différence), `"prefix"` (commence par) |
| `doc_type` | `str` | `None` | Filtrer par type de document (séparés par des virgules, par ex. `"INVOICE,CREDIT_NOTE"`) |
| `status` | `str` | `None` | Filtrer par statut de document (séparés par des virgules, par ex. `"ready_for_validation,exported"`) |
| `vendor_name` | `str` | `None` | Filtrer par nom de fournisseur |
| `date_range` | `str` | `None` | `"last_30_days"`, `"last_90_days"`, `"last_180_days"`, `"last_365_days"` |
| `size` | `int` | `10` | Nombre maximal de résultats (plafonné à 50) |

**Retourne :** `list[dict]` — Chaque dict contient :

| Champ | Description |
| ----- | ----------- |
| `doc_id` | UUID du document |
| `name` | Nom du fichier (par ex. `"INV-2026-001.pdf"`) |
| `doc_type` | Type de document (`"INVOICE"`, `"ORDER_CONFIRMATION"`, etc.) |
| `vendor_name` | Nom du fournisseur |
| `status` | Statut du document |
| `total_amount` | Montant total |
| `ocr_content` | Extrait de texte correspondant du document |
| `highlights` | Dict avec les correspondances surlignées par champ |

**Exemple — Recherche d'une phrase exacte :**

```python
results = fulltext_search("REVERSE CHARGE",
                          doc_type="INVOICE", size=10)
for doc in results:
    print(doc["name"], doc["ocr_content"])
```

**Exemple — Recherche floue (tolérante aux fautes de l'OCR) :**

```python
# Finds "REVERSE CHARGE" even with OCR errors like "REVERS CHARG"
results = fulltext_search("REVERSE CHARGE",
                          search_type="fuzzy",
                          vendor_name="ACME Corp")
```

**Exemple — Recherche par préfixe :**

```python
# Finds all documents containing words starting with "Rechn"
results = fulltext_search("Rechn", search_type="prefix",
                          date_range="last_90_days")
```

{% hint style="warning" %}
**Requête vide :** Passer une chaîne vide retourne immédiatement `[]` sans effectuer d'appel HTTP.
{% endhint %}

{% hint style="info" %}
**Gestion des erreurs :** Si le service fulltextsearch est injoignable, la fonction retourne `[]` et consigne un avertissement. Elle ne lève **pas** d'exception.
{% endhint %}

---

## vector\_search()

Trouve des documents sémantiquement similaires à l'aide d'embeddings vectoriels (recherche k-NN avec des vecteurs à 384 dimensions). Utile pour trouver des documents au contenu proche, quelle que soit la formulation exacte.

```python
vector_search(doc_id, **kwargs)
```

**Paramètres :**

| Nom | Type | Défaut | Description |
| ---- | ---- | ------- | ----------- |
| `doc_id` | `str` | obligatoire | UUID du document source (le document pour lequel on cherche des correspondances similaires) |
| `k` | `int` | `5` | Nombre de documents similaires à retourner (plafonné à 50) |

**Retourne :** `list[dict]` — Chaque dict contient :

| Champ | Description |
| ----- | ----------- |
| `doc_id` | UUID du document similaire |
| `name` | Nom du fichier |
| `doc_type` | Type de document |
| `similarity_score` | Score de similarité brut (0-1) |
| `similarity_percent` | Similarité en pourcentage (0-100) |

**Exemple — Trouver des documents similaires :**

```python
doc_id = document_json["doc_id"]
similar = vector_search(doc_id, k=5)
for doc in similar:
    print(f"{doc['name']}: {doc['similarity_percent']}% similar")
```

{% hint style="info" %}
**Fonctionnement :** Chaque document est converti en un vecteur à 384 dimensions lors de l'indexation. La recherche vectorielle trouve les plus proches voisins dans cet espace vectoriel, qui correspondent à des documents sémantiquement similaires.
{% endhint %}

---

## fulltext\_search\_erp()

Recherche dans les données de référence ERP (fournisseurs, bons de commande, clients, articles) indexées dans OpenSearch.

```python
fulltext_search_erp(query, **kwargs)
```

**Paramètres :**

| Nom | Type | Défaut | Description |
| ---- | ---- | ------- | ----------- |
| `query` | `str` | obligatoire | Terme de recherche |
| `entity_types` | `str` | `None` | Filtrer par type d'entité (séparés par des virgules : `"vendor"`, `"purchase_order"`, `"customer"`, `"material"`) |
| `vendor_number` | `str` | `None` | Filtrer par numéro de fournisseur |
| `vendor_name` | `str` | `None` | Filtrer par nom de fournisseur |
| `company_code` | `str` | `None` | Filtrer par code société |
| `size` | `int` | `10` | Nombre maximal de résultats (plafonné à 50) |

**Retourne :** `list[dict]` — Champs propres à chaque type d'entité (les enregistrements fournisseur contiennent `vendor_number`, `vendor_name`, etc.)

**Exemple — Valider un fournisseur dans l'ERP :**

```python
vendor = get_field_value(document_data, "supplier_name", "")
if vendor:
    matches = fulltext_search_erp(vendor,
                                   entity_types="vendor", size=5)
    if not matches:
        set_field_as_invalid(document_data, "supplier_name",
                             "Vendor not found in ERP master data")
```

**Exemple — Rechercher des bons de commande :**

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

Retourne des suggestions d'autocomplétion pour les termes de recherche. Regroupe les résultats par catégorie (fournisseurs, noms de fichiers, numéros de facture).

```python
fulltext_suggestions(query, **kwargs)
```

**Paramètres :**

| Nom | Type | Défaut | Description |
| ---- | ---- | ------- | ----------- |
| `query` | `str` | obligatoire | Préfixe / terme de recherche |
| `limit` | `int` | `10` | Nombre maximal de suggestions par catégorie (plafonné à 20) |

**Retourne :** `dict` avec les suggestions regroupées :

```python
{
    "vendors": ["ACME Corp", "ACME International"],
    "filenames": ["INV-2026-001.pdf", "INV-2026-002.pdf"],
    "invoice_numbers": ["INV-2026-001", "INV-2026-002"]
}
```

**Exemple — Obtenir des suggestions de fournisseurs :**

```python
suggestions = fulltext_suggestions("ACM", limit=5)
vendor_list = suggestions.get("vendors", [])
```

{% hint style="warning" %}
**Requête vide :** Passer une chaîne vide retourne immédiatement `{}`.
{% endhint %}

---

## Référence rapide

| Fonction | Objectif | Retourne |
| -------- | ------- | ------- |
| `fulltext_search(query, ...)` | Rechercher dans le texte OCR de tous les documents | `list[dict]` |
| `vector_search(doc_id, ...)` | Trouver des documents sémantiquement similaires | `list[dict]` |
| `fulltext_search_erp(query, ...)` | Rechercher dans les données de référence ERP | `list[dict]` |
| `fulltext_suggestions(query, ...)` | Suggestions d'autocomplétion | `dict` |

---

## Schémas courants

### Vérification de la licence

Les quatre fonctions vérifient automatiquement la préférence `OPENSEARCH_ENABLED`. Si elle n'est pas activée :

```python
# This will raise RuntimeError("Fulltext search license is missing")
results = fulltext_search("test")
```

Pour gérer ce cas proprement dans les scripts :

```python
try:
    results = fulltext_search("test")
except RuntimeError:
    # OpenSearch not enabled for this org — skip search
    results = []
```

### Combinaison avec les fonctions de champ

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
