# Détection du Code Fiscal

## Que fait ce script ?

Détermine automatiquement le code fiscal correct en se basant sur le texte intégral du document et les montants de taxe/net. Détecte les scénarios d'autoliquidation (reverse charge), les factures exonérées de taxe, et calcule le taux de taxe pour attribuer le code approprié (ex. S1 pour 19 %, S2 pour 7 %).

## Déclencheur

`AFTER_FORMATTING` sur le type de document **INVOICE**

## Script complet

```python
# Obtenir le texte intégral du document et les montants
content = get_document_content(document_data)
tax_amount = get_field_value(document_data, "tax_amount", "0")
net_amount = get_field_value(document_data, "net_amount", "0")

try:
    tax = float(tax_amount) if tax_amount else 0
    net = float(net_amount) if net_amount else 0
except ValueError:
    tax = 0
    net = 0

# Règle 1 : Détection de l'autoliquidation via le texte intégral
if "REVERSE CHARGE" in content.upper() or "UMKEHR DER STEUERSCHULD" in content.upper():
    set_field_value(document_data, "tax_code", "RC")

# Règle 2 : Taxe nulle = exonéré de taxe
elif tax == 0:
    set_field_value(document_data, "tax_code", "Z0")

# Règle 3 : Calculer le taux de taxe à partir des montants
elif net > 0:
    tax_rate = round((tax / net) * 100, 0)
    if tax_rate == 19:
        set_field_value(document_data, "tax_code", "S1")    # Taux standard
    elif tax_rate == 7:
        set_field_value(document_data, "tax_code", "S2")    # Taux réduit
    else:
        set_field_value(document_data, "tax_code", "S3")    # Autre taux
```

## Explication étape par étape

1. **Lire le texte intégral** avec `get_document_content()` pour la détection de mots-clés
2. **Lire les montants de taxe et net** pour le calcul du taux de taxe
3. **Vérifier les mots-clés d'autoliquidation** dans le texte du document (en allemand et en anglais)
4. **Vérifier la taxe nulle** — si le montant de la taxe est 0, attribuer le code exonéré de taxe
5. **Calculer le taux de taxe** à partir du ratio taxe/net et attribuer le code correspondant

## Fonctions utilisées

- [get\_document\_content()](../business-logic-functions.md#get\_document\_content) — Lire le texte intégral OCR
- [get\_field\_value()](../field-functions.md#get\_field\_value) — Lire les valeurs des champs
- [set\_field\_value()](../field-functions.md#set\_field\_value) — Définir le code fiscal
