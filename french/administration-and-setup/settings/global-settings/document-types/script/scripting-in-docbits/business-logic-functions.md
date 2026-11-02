# Fonctions de Logique Métier

Fonctions pour les recherches, la correspondance BC, les tâches, la gestion des utilisateurs/groupes et les changements de statut.

**Source :** `module/script/helper/document_script_functions.py`

---

## get\_lookup\_records()

Interroge les données de référence à partir des tables de recherche (fournisseurs, articles, comptes GL, etc.).

```python
get_lookup_records(org_id, sub_org_id, lookup_name, filters, **kwargs)
```

**Paramètres :**

| Nom | Type | Description |
| ---- | ---- | ----------- |
| `org_id` | `str` | UUID de l'organisation |
| `sub_org_id` | `str/None` | UUID de la sous-organisation (ou `None`) |
| `lookup_name` | `str` | Nom de la recherche (ex. `"supplier"`, `"item"`, `"gl_account"`) |
| `filters` | `list` | Conditions de filtrage (voir les formats ci-dessous) |
| `skip` | `int` | Décalage pour la pagination (par défaut : 0) |
| `limit` | `int` | Résultats maximum (par défaut : 100) |
| `match_all` | `bool` | `True` = ET, `False` = OU (par défaut : `True`) |
| `sort_order` | `list` | Tri (optionnel) |

### Formats de filtres

Trois formats sont supportés :

```python
# Format 1 : Dict avec champ/opérateur/valeur
filters = [
    {"field": "VENDOR_ID", "operator": "exact", "value": "V001"},
    {"field": "NAME", "operator": "contains", "value": "ACME"},
]

# Format 2 : Tuple/Liste avec 2 éléments (champ, valeur) → opérateur = "exact"
filters = [
    ["VENDOR_ID", "V001"],
    ["CITY", "Munich"],
]

# Format 3 : Tuple/Liste avec 3 éléments (champ, opérateur, valeur)
filters = [
    ["VENDOR_ID", "exact", "V001"],
    ["NAME", "contains", "ACME"],
]
```

### Tri

```python
# Format 1 : Dict
sort_order = [{"field": "NAME", "direction": "asc"}]

# Format 2 : Tuple/Liste
sort_order = [["NAME", "asc"], ["VENDOR_ID", "desc"]]
```

**Exemple — Rechercher un fournisseur par ID fournisseur :**

```python
# Trouver le fournisseur par ID fournisseur
supplier_id = get_field_value(document_data, "supplier_id", "")
records = get_lookup_records(
    org_id, None, "supplier",
    [["VENDOR_ID", supplier_id]],
)
if records:
    supplier = records[0]
    set_field_value(document_data, "supplier_name", supplier.get("NAME", ""))
```

**Exemple — Rechercher des comptes GL avec plusieurs filtres :**

```python
records = get_lookup_records(
    org_id, document_json.get("sub_org_id"), "gl_account",
    [
        {"field": "ACCOUNT_TYPE", "operator": "exact", "value": "EXPENSE"},
        {"field": "IS_ACTIVE", "operator": "exact", "value": "true"},
    ],
    limit=50,
    sort_order=[["ACCOUNT_NUMBER", "asc"]],
)
```

{% hint style="info" %}
Utilise en interne `search_operator="SMART"` qui supporte la correspondance floue.
{% endhint %}

---

## is\_supplier\_valid()

Vérifie si un fournisseur existe dans les données de recherche.

```python
is_supplier_valid(user, filter_data_json, sub_org_id=None)
```

**Paramètres :**

| Nom | Type | Description |
| ---- | ---- | ----------- |
| `user` | `UserAuthentication` | L'objet de contexte `user` |
| `filter_data_json` | `dict` | Filtre au format `{"match_all": True, "filters": [...]}` |
| `sub_org_id` | `str/None` | Sous-organisation |

**Retourne :** `True` s'il y a au moins 1 correspondance, sinon `False`

**Exemple — Valider un fournisseur :**

```python
supplier_id = get_field_value(document_data, "supplier_id", "")
is_valid = is_supplier_valid(user, {
    "match_all": True,
    "filters": [{"field": "VENDOR_ID", "operator": "exact", "value": supplier_id}]
})
if not is_valid:
    set_field_as_invalid(document_data, "supplier_id", "Supplier not found in master data")
```

---

## auto\_po\_match\_for\_purchase\_orders()

Déclenche la correspondance automatique des BC via le microservice po-match-service.

```python
auto_po_match_for_purchase_orders(user, document_data, po_numbers)
```

**Paramètres :**

| Nom | Type | Description |
| ---- | ---- | ----------- |
| `user` | `UserAuthentication` | Doit être un vrai objet utilisateur |
| `document_data` | `dict` | Contexte du document |
| `po_numbers` | `str/list` | Numéros de BC (séparés par des virgules ou liste) |

**Retourne :** `document_data` mis à jour avec `po_items`, `po_match_status`, `po_multi_matched`

**Exemple — Correspondance automatique de BC :**

```python
po_nr = get_field_value(document_data, "purchase_order", "")
if po_nr:
    auto_po_match_for_purchase_orders(user, document_data, po_nr)
```

{% hint style="warning" %}
**Protection contre les doublons :** Les numéros de BC déjà vérifiés sont stockés dans `already_verified_po_numbers` et ne seront pas mis en correspondance à nouveau.
{% endhint %}

---

## get\_next\_sequence\_number()

Obtient et incrémente atomiquement un numéro de séquence dans la base de données.

```python
get_next_sequence_number(org_id, sequence_name, default_value=1)
```

**Paramètres :**

| Nom | Type | Description |
| ---- | ---- | ----------- |
| `org_id` | `str` | UUID de l'organisation |
| `sequence_name` | `str` | Doit contenir `"sequence"` (ex. `"invoice_sequence"`) |
| `default_value` | `int` | Valeur de départ quand la séquence est nouvellement créée |

**Retourne :** `int` — le prochain numéro, ou `None` si le nom est invalide

**Exemple — Générer un numéro de document interne :**

```python
seq_nr = get_next_sequence_number(org_id, "invoice_sequence", 1000)
set_field_value(document_data, "internal_number", str(seq_nr))
```

{% hint style="danger" %}
**Règle de nommage :** Le `sequence_name` doit commencer ou finir par "sequence", ou contenir "SEQUENCE\_". Sinon la fonction retourne `None`.
{% endhint %}

---

## create\_document\_task()

Crée une tâche pour le document en cours.

```python
create_document_task(user, document_data, title, description, priority,
                     assigned_to_user_id, assigned_to_group_id, send_email)
```

**Paramètres :**

| Nom | Type | Description |
| ---- | ---- | ----------- |
| `user` | `UserAuthentication` | Contexte utilisateur |
| `title` | `str` | Titre de la tâche |
| `description` | `str` | Description |
| `priority` | `str/int` | Priorité |
| `assigned_to_user_id` | `str/None` | Utilisateur assigné |
| `assigned_to_group_id` | `str/None` | Groupe assigné |
| `send_email` | `bool` | Envoyer une notification par e-mail |

**Exemple — Créer une tâche pour les factures à montant élevé :**

```python
amount = float(get_field_value(document_data, "total_amount", "0"))
if amount > 50000:
    create_document_task(
        user, document_data,
        title="High invoice amount - review required",
        description=f"Invoice amount: {amount} exceeds 50,000 threshold",
        priority="HIGH",
        assigned_to_user_id=None,
        assigned_to_group_id="uuid-of-finance-group",
        send_email=True
    )
```

---

## set\_document\_sub\_org\_id()

Attribue une sous-organisation à un document.

```python
set_document_sub_org_id(document_data, sub_org_id)
```

**Effets de bord :**
- Définit `sub_org_id` dans `document_json`
- Sauvegarde directement en base de données (si `doc_id` est présent)

**Exemple — Routage basé sur le fournisseur :**

```python
supplier = get_field_value(document_data, "supplier_name", "", is_clean=True)
sub_org_map = {
    "ACMECORP": "uuid-acme-sub-org",
    "WIDGETSINC": "uuid-widgets-sub-org",
}
for key, sub_org in sub_org_map.items():
    if key in supplier:
        set_document_sub_org_id(document_data, sub_org)
        break
```

---

## update\_document\_status\_with\_doc\_id()

Change le statut d'un document.

```python
update_document_status_with_doc_id(doc_id, user, org_id, status, message=None,
                                    doc_classification_class=None)
```

**Paramètres :**

| Nom | Type | Description |
| ---- | ---- | ----------- |
| `doc_id` | `str` | UUID du document |
| `status` | `str` | Nouveau statut (ex. `"error"`, `"ready_for_validation"`) |
| `message` | `str/None` | Message de statut |
| `doc_classification_class` | `str/None` | Pour le statut `CLASSIFIED` : nouveau type de document |

**Exemple — Mettre le document en statut d'erreur :**

```python
doc_id = document_json["doc_id"]
update_document_status_with_doc_id(
    doc_id, user, org_id, "error",
    message="Required field missing: supplier number"
)
```

{% hint style="warning" %}
**Attention :** Les changements de statut déclenchent des actions en aval (flux de travail DocFlow, hooks de changement de statut). N'utilisez que lorsque c'est nécessaire.
{% endhint %}

---

## get\_document\_content()

Retourne le texte OCR complet du document.

```python
get_document_content(document_data)
```

**Retourne :** `str` — Texte concaténé de toutes les pages

**Exemple — Recherche plein texte par mots-clés :**

```python
content = get_document_content(document_data)
if "REVERSE CHARGE" in content.upper():
    set_field_value(document_data, "tax_code", "RC")

# Recherche regex dans le texte intégral
match = re_search(r"Order number:\s*(\S+)", content)
if match:
    set_field_value(document_data, "purchase_order", match.group(1))
```

{% hint style="info" %}
Le résultat est mis en cache pendant 60 secondes (cache TTL avec max 128 entrées).
{% endhint %}

---

## get\_user\_by\_id() / get\_user\_by\_email()

Recherche un utilisateur par ID ou e-mail.

```python
get_user_by_id(user_id)
get_user_by_email(email)
```

**Retourne :** Objet `UsersCache` avec les attributs `.email`, `.first_name`, `.last_name`, `.user_id`

**Exemple — Assigner une tâche à un utilisateur spécifique :**

```python
user_obj = get_user_by_email("manager@company.com")
if user_obj:
    create_document_task(user, document_data,
        title="Review required",
        description="...",
        priority="MEDIUM",
        assigned_to_user_id=str(user_obj.user_id),
        assigned_to_group_id=None,
        send_email=True)
```

---

## get\_group\_by\_id() / get\_group\_by\_name()

Recherche un groupe d'utilisateurs par ID ou nom.

```python
get_group_by_id(group_id)
get_group_by_name(org_id, group_name)
```

**Retourne :** Objet `GroupCache`

**Exemple — Trouver un groupe pour l'assignation de tâche :**

```python
finance_group = get_group_by_name(org_id, "Finance")
if finance_group:
    create_document_task(user, document_data,
        title="Approval needed",
        description="...",
        priority="HIGH",
        assigned_to_user_id=None,
        assigned_to_group_id=str(finance_group.id),
        send_email=True)
```

---

## compare\_values()

Comparaison intelligente de valeurs avec conversion de type.

```python
compare_values(value1, value2)
```

**Logique de comparaison :**
1. `None == None` → `True`
2. `None != non-None` → `False`
3. Chaînes qui sont des nombres → comparaison numérique (`"1.0" == "1.00"` → `True`)
4. Chaînes → insensible à la casse, insensible aux espaces (`"ABC " == " abc"` → `True`)
5. Bool vs Chaîne → comparaison de chaînes (`True == "true"` → `True`)
6. Comparaison décimale en dernier recours

**Exemple — Vérifier que les montants correspondent :**

```python
if compare_values(get_field_value(document_data, "net_amount"),
                  get_field_value(document_data, "calculated_net")):
    set_field_as_valid(document_data, "net_amount", "Amounts match")
```

---

## get\_lov\_values()

Récupère les entrées de Liste de Valeurs (LOV).

```python
get_lov_values(org_id, key, return_type="list_of_objects", sub_org_id=None, language_code="")
```

**Paramètres :**

| Nom | Type | Description |
| ---- | ---- | ----------- |
| `org_id` | `str` | UUID de l'organisation |
| `key` | `str` | Clé LOV |
| `return_type` | `str` | `"list_of_objects"` ou `"list_of_values"` |
| `sub_org_id` | `str/None` | Filtre optionnel de sous-organisation |
| `language_code` | `str` | Code de langue (ex. `"en"`, `"de"`) |

**Retourne :** Les valeurs LOV sous forme de liste d'objets ou de liste plate.

**Exemple — Obtenir les codes fiscaux configurés :**

```python
tax_codes = get_lov_values(org_id, "tax_codes", return_type="list_of_values")
```
