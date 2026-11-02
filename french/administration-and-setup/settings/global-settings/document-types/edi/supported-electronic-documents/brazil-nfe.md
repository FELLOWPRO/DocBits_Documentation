---
description: Support du document électronique BRAZIL NF-E dans DocBits
---

# 🇧🇷 BRAZIL NF-E

<!-- edocs-country-scope -->

{% hint style="info" %}
Consultez le guide du pays pour connaître les limites de version, la configuration effectivement utilisée et la vidéo explicative du pays. [Brésil](countries/brazil.md). Il s’agit de familles de documents différentes. Une version NFS-e configurée ne certifie pas chaque schéma municipal ni chaque structure nationale de facture de services.
{% endhint %}

| Propriété | Valeur |
|-----------|--------|
| **Pays / Région** | Brésil |
| **Types de documents** | Facture (Nota Fiscal Eletrônica) |
| **Format** | XML |
| **Standard** | NF-e 4.0 (Nota Fiscal Eletrônica — biens & commerce interétatique) |
| **Langue** | `pt_BR` |

La NF-e (Nota Fiscal Eletrônica, `<mod>55</mod>`) est la facture électronique brésilienne pour les biens et le commerce interétatique, réglementée par SEFAZ. Chaque NF-e contient une clé d'accès unique de 44 chiffres (`chNFe`), des lignes de produits détaillées et des données fiscales multi-niveaux (ICMS, IPI, PIS, COFINS). DocBits classe les NF-e en détectant l'espace de noms `http://www.portalfiscal.inf.br/nfe`.

## Statut de prise en charge

| Composant | Statut |
|-----------|--------|
| Aperçu | ✅ Pris en charge |
| Extraction des champs | ✅ Pris en charge |
| Transformation | ✅ Pris en charge |

## Aperçu par défaut

<figure><img src="../../../../../../.gitbook/assets/brazil-nfe-preview.png" alt="Aperçu Brazil NF-e dans DocBits"><figcaption><p>Aperçu DocBits par défaut pour un document BRAZIL NF-E</p></figcaption></figure>

## Correspondance des champs

### Champs d'en-tête

| Champ DocBits | XPath source | Remarques |
|---|---|---|
| `invoice_id` | `//*[local-name()='ide']/*[local-name()='nNF']` | Numéro de la Nota Fiscal |
| `invoice_date` | `//*[local-name()='ide']/*[local-name()='dhEmi']` | ISO 8601 avec décalage BRT |
| `currency` | Fixe : `BRL` | Toujours Real brésilien |
| `total_amount` | `//*[local-name()='ICMSTot']/*[local-name()='vNF']` | Valeur totale de la NF-e |
| `net_amount` | `//*[local-name()='ICMSTot']/*[local-name()='vProd']` | Valeur totale des produits |
| `tax_amount` | `//*[local-name()='ICMSTot']/*[local-name()='vICMS']` | Total de la taxe ICMS |
| `supplier_name` | `//*[local-name()='emit']/*[local-name()='xNome']` | Nom de la société émettrice |
| `supplier_id` | `//*[local-name()='emit']/*[local-name()='CNPJ']` ou `CPF` | CNPJ (14 chiffres) ou CPF (11 chiffres) |
| `buyer_name` | `//*[local-name()='dest']/*[local-name()='xNome']` | Nom de la société destinataire |
| `buyer_id` | `//*[local-name()='dest']/*[local-name()='CNPJ']` ou `CPF` | CNPJ ou CPF |

### Table des lignes (`INVOICE_TABLE`)

Chemin de ligne : `//*[local-name()='det']`

| Colonne | XPath relatif | Remarques |
|---|---|---|
| `POSITION` | `@nItem` | Numéro de séquence de la ligne |
| `ITEM_CODE` | `*[local-name()='prod']/*[local-name()='cProd']` | Code produit |
| `DESCRIPTION` | `*[local-name()='prod']/*[local-name()='xProd']` | Description du produit |
| `NCM_CODE` | `*[local-name()='prod']/*[local-name()='NCM']` | Classification douanière NCM |
| `CFOP_CODE` | `*[local-name()='prod']/*[local-name()='CFOP']` | Code d'opération fiscal |
| `UNIT` | `*[local-name()='prod']/*[local-name()='uCom']` | Unité de mesure |
| `QUANTITY` | `*[local-name()='prod']/*[local-name()='qCom']` | Quantité commerciale |
| `UNIT_PRICE` | `*[local-name()='prod']/*[local-name()='vUnCom']` | Prix unitaire |
| `TOTAL_AMOUNT` | `*[local-name()='prod']/*[local-name()='vProd']` | Total de la ligne |
| `ICMS_AMOUNT` | `*[local-name()='imposto']/*[local-name()='ICMS']//*[local-name()='vICMS']` | Taxe ICMS par ligne |
| `PIS_AMOUNT` | `*[local-name()='imposto']/*[local-name()='PIS']//*[local-name()='vPIS']` | Taxe PIS par ligne |
| `COFINS_AMOUNT` | `*[local-name()='imposto']/*[local-name()='COFINS']//*[local-name()='vCOFINS']` | Taxe COFINS par ligne |
| `VAT_RATE` | `*[local-name()='imposto']/*[local-name()='ICMS']//*[local-name()='pICMS']` | Taux ICMS (%) |

## Règle de classification

DocBits détecte les documents BRAZIL NF-E en recherchant la chaîne :

```
http://www.portalfiscal.inf.br/nfe
```

dans l'espace de noms XML (le code `mod=55` pour NF-e et `mod=65` pour NFC-e sont distingués séparément).

## Liens connexes

- [BRAZIL NFC-E](brazil-nfce.md)
- [BRAZIL CT-E](brazil-cte.md)
- [BRAZIL NFS-E](brazil-nfse.md)
- [Documents électroniques pris en charge](./)
