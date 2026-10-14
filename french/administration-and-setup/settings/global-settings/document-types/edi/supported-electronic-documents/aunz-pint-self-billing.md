---
description: Prise en charge des documents électroniques AUNZ PINT SELF-BILLING dans DocBits
---

# 🇦🇺 AUNZ PINT SELF-BILLING

| Propriété | Valeur |
|----------|-------|
| **Pays / Région** | Australie / Nouvelle-Zélande |
| **Types de document** | Facture d'autofacturation |
| **Format** | UBL 2.1 XML |
| **Norme** | PINT A-NZ Self-Billing |
| **Paramètre régional** | `en_AU` |

AUNZ PINT Self-Billing est la variante d'autofacturation du modèle de facturation Peppol International de l'A-NZ. Dans les scénarios d'autofacturation, l'acheteur crée la facture au nom du fournisseur. Ce type de document suit la même structure PINT A-NZ mais avec les rôles des parties inversés — l'`AccountingCustomerParty` devient la partie émettrice de la facture et l'`AccountingSupplierParty` est la partie facturée.

## État de la prise en charge

| Composant | État |
|-----------|--------|
| Aperçu | ✅ Pris en charge |
| Extraction des champs | ✅ Pris en charge |
| Transformation | ✅ Pris en charge |

## Aperçu par défaut

<figure><img src="aunz-pint-preview.png" alt="Aperçu de facture AUNZ PINT Self-Billing dans DocBits"><figcaption><p>Aperçu par défaut de DocBits pour une facture AUNZ PINT Self-Billing</p></figcaption></figure>

## Mappage des champs

Le mappage des champs est identique à [AUNZ PINT](aunz-pint.md) avec la différence clé suivante :

- **Les rôles des parties sont inversés** : En autofacturation, l'acheteur est la partie émettrice et le fournisseur est la partie facturée
- La `CustomizationID` contient `urn:peppol.org:pint:selfbilling-1@aunz` au lieu de `billing-1@aunz`

Pour le tableau complet de mappage des champs, voir [AUNZ PINT](aunz-pint.md#mappage-des-champs).

## Règle de classification

DocBits détecte les documents d'autofacturation en faisant correspondre la `CustomizationID` :

```
urn:peppol.org:pint:selfbilling-1@aunz
```

Les motifs d'autofacturation et de facturation régulière sont tous deux classés sous le type de document électronique `PINT A-NZ`.

## Voir aussi

- [AUNZ PINT](aunz-pint.md)
- [Documents électroniques pris en charge](./)