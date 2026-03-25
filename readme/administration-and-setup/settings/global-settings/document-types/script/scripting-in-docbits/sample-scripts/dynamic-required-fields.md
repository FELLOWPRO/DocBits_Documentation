# Champs Obligatoires Dynamiques

## Que fait ce script ?

Définit dynamiquement les exigences des champs en fonction du contenu du document. Dans cet exemple : lorsque la devise de la facture n'est pas EUR, le champ de taux de change devient obligatoire et visible. Pour les factures en EUR, le champ de taux de change est masqué et optionnel.

## Déclencheur

`ON_FIELD_CHANGE` sur le type de document **INVOICE**

## Script complet

```python
# Lire la devise actuelle
currency = get_field_value(document_data, "currency", "EUR")

# Devise étrangère : le taux de change est obligatoire et visible
if currency and currency != "EUR":
    set_is_required(document_data, "exchange_rate", True)
    set_is_hidden(document_data, "exchange_rate", False)
else:
    # EUR : le taux de change est optionnel et masqué
    set_is_required(document_data, "exchange_rate", False)
    set_is_hidden(document_data, "exchange_rate", True)
```

## Variante : Facture d'achat vs. facture de coûts

```python
po = get_field_value(document_data, "purchase_order", "")

if po and po.strip():
    # Facture d'achat : le numéro de BC est obligatoire
    set_field_value(document_data, "invoice_category", "PURCHASE_INVOICE")
    set_is_required(document_data, "purchase_order", True)
else:
    # Facture de coûts : le numéro de BC n'est pas nécessaire, masquer le tableau
    set_field_value(document_data, "invoice_category", "COST_INVOICE")
    set_is_required(document_data, "purchase_order", False)
    delete_tables(document_data)
```

## Explication étape par étape

1. **Lire le champ de contrôle** (la devise dans ce cas)
2. **Appliquer les règles métier** — différentes exigences de champs selon la valeur
3. **Définir la visibilité** — masquer les champs non pertinents pour garder l'interface propre
4. **Définir les obligations** — rendre les champs pertinents obligatoires

{% hint style="info" %}
**Choix du déclencheur :** `ON_FIELD_CHANGE` s'exécute à chaque fois qu'un utilisateur modifie un champ, donc les exigences se mettent à jour en temps réel. `AFTER_FORMATTING` ne s'exécute qu'une seule fois après l'extraction initiale.
{% endhint %}

## Fonctions utilisées

- [get\_field\_value()](../field-functions.md#get\_field\_value) — Lire le champ de contrôle
- [set\_is\_required()](../field-functions.md#set\_is\_required) — Définir le champ comme obligatoire/optionnel
- [set\_is\_hidden()](../field-functions.md#set\_is\_hidden) — Afficher/masquer les champs
- [set\_field\_value()](../field-functions.md#set\_field\_value) — Définir le champ de catégorie
- [delete\_tables()](../table-functions.md#delete\_tables) — Supprimer les tables pour les factures de coûts
