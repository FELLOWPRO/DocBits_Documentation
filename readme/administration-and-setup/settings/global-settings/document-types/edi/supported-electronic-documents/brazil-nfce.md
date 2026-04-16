---
description: Support du document électronique BRAZIL NFC-E dans DocBits
---

# 🇧🇷 BRAZIL NFC-E

| Propriété | Valeur |
|-----------|--------|
| **Pays / Région** | Brésil |
| **Types de documents** | Facture consommateur (Nota Fiscal de Consumidor Eletrônica) |
| **Format** | XML |
| **Standard** | NFC-e 4.0 (facture consommateur au détail / point de vente) |
| **Langue** | `pt_BR` |

La NFC-e (Nota Fiscal de Consumidor Eletrônica, `<mod>65</mod>`) est la facture électronique brésilienne pour les ventes au détail aux consommateurs finaux. Elle partage le schéma XML de la NF-e (espace de noms `nfeProc`) mais utilise le code modèle 65. Les documents NFC-e utilisent généralement un CPF (numéro fiscal individuel) pour l'acheteur à la place d'un CNPJ, et n'incluent pas de PIS/COFINS par ligne pour les transactions de vente au détail simples.

## Statut de prise en charge

| Composant | Statut |
|-----------|--------|
| Aperçu | ✅ Pris en charge |
| Extraction des champs | ✅ Pris en charge |
| Transformation | ✅ Pris en charge |

## Aperçu par défaut

<figure><img src="brazil-nfce-preview.png" alt="Aperçu Brazil NFC-e dans DocBits"><figcaption><p>Aperçu DocBits par défaut pour un document BRAZIL NFC-E</p></figcaption></figure>

## Correspondance des champs

### Champs d'en-tête

| Champ DocBits | XPath source | Remarques |
|---|---|---|
| `invoice_id` | `//*[local-name()='ide']/*[local-name()='nNF']` | Numéro de la Nota Fiscal |
| `invoice_date` | `//*[local-name()='ide']/*[local-name()='dhEmi']` | ISO 8601 avec décalage BRT |
| `currency` | Fixe : `BRL` | Toujours Real brésilien |
| `total_amount` | `//*[local-name()='ICMSTot']/*[local-name()='vNF']` | Valeur totale de la NFC-e |
| `net_amount` | `//*[local-name()='ICMSTot']/*[local-name()='vProd']` | Sous-total des produits |
| `tax_amount` | `//*[local-name()='ICMSTot']/*[local-name()='vICMS']` | Total de la taxe ICMS |
| `supplier_name` | `//*[local-name()='emit']/*[local-name()='xNome']` | Nom du détaillant |
| `supplier_id` | `//*[local-name()='emit']/*[local-name()='CNPJ']` ou `CPF` | CNPJ ou CPF |
| `buyer_name` | `//*[local-name()='dest']/*[local-name()='xNome']` | Nom du consommateur |
| `buyer_id` | `//*[local-name()='dest']/*[local-name()='CPF']` ou `CNPJ` | CPF (individuel) ou CNPJ |

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
| `VAT_RATE` | `*[local-name()='imposto']/*[local-name()='ICMS']//*[local-name()='pICMS']` | Taux ICMS (%) |

## Règle de classification

DocBits détecte les documents BRAZIL NFC-E via le motif `<mod>65</mod>` dans le XML de l'espace de noms `http://www.portalfiscal.inf.br/nfe`.

## Liens connexes

- [BRAZIL NF-E](brazil-nfe.md)
- [BRAZIL CT-E](brazil-cte.md)
- [BRAZIL NFS-E](brazil-nfse.md)
- [Documents électroniques pris en charge](./)
