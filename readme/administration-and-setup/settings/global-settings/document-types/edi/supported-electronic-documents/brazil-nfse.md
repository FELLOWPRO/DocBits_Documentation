---
description: Support du document électronique BRAZIL NFS-E dans DocBits
---

# 🇧🇷 BRAZIL NFS-E

| Propriété | Valeur |
|-----------|--------|
| **Pays / Région** | Brésil |
| **Types de documents** | Facture de services (Nota Fiscal de Serviços Eletrônica) |
| **Format** | XML |
| **Standard** | NFS-e 2.04 (standard national ABRASF pour les factures de services municipaux) |
| **Langue** | `pt_BR` |

La NFS-e (Nota Fiscal de Serviços Eletrônica) est la facture électronique brésilienne pour les services, émise au niveau municipal. DocBits prend en charge le schéma standard ABRASF (Associação Brasileira das Secretarias de Finanças das Capitais). Les documents NFS-e utilisent une structure XML différente de la NF-e : la taxe principale est l'ISS (Imposto Sobre Serviços) plutôt que l'ICMS, et le fournisseur/acheteur sont appelés `PrestadorServico` / `TomadorServico`. L'élément `Discriminacao` contient la description du service en texte libre.

## Statut de prise en charge

| Composant | Statut |
|-----------|--------|
| Aperçu | ✅ Pris en charge |
| Extraction des champs | ✅ Pris en charge |
| Transformation | ✅ Pris en charge |

## Aperçu par défaut

<figure><img src="brazil-nfse-preview.png" alt="Aperçu Brazil NFS-e dans DocBits"><figcaption><p>Aperçu DocBits par défaut pour un document BRAZIL NFS-E</p></figcaption></figure>

## Correspondance des champs

### Champs d'en-tête

| Champ DocBits | XPath source | Remarques |
|---|---|---|
| `invoice_id` | `//*[local-name()='Numero']` | Numéro de la NFS-e |
| `invoice_date` | `//*[local-name()='DataEmissao']` | Date d'émission ISO 8601 |
| `currency` | Fixe : `BRL` | Toujours Real brésilien |
| `total_amount` | `//*[local-name()='ValorServicos']` | Valeur brute du service |
| `net_amount` | `//*[local-name()='ValorLiquidoNfse']` | Valeur nette après déductions |
| `tax_amount` | `//*[local-name()='ValorIss']` | ISS (taxe municipale sur les services) |
| `supplier_name` | `//*[local-name()='PrestadorServico']//*[local-name()='RazaoSocial']` | Nom du prestataire de services |
| `supplier_id` | `//*[local-name()='PrestadorServico']//*[local-name()='Cnpj']` | CNPJ du prestataire |
| `buyer_name` | `//*[local-name()='TomadorServico']//*[local-name()='RazaoSocial']` | Nom du bénéficiaire du service |
| `buyer_id` | `//*[local-name()='TomadorServico']//*[local-name()='Cnpj']` | CNPJ du bénéficiaire |

> La NFS-e décrit un service unique dans l'élément `Discriminacao` plutôt que des lignes de détail. Aucun `INVOICE_TABLE` n'est extrait.

## Règle de classification

DocBits détecte les documents BRAZIL NFS-E via l'espace de noms :

```
http://www.abrasf.org.br/nfse.xsd
```

## Liens connexes

- [BRAZIL NF-E](brazil-nfe.md)
- [BRAZIL NFC-E](brazil-nfce.md)
- [BRAZIL CT-E](brazil-cte.md)
- [Documents électroniques pris en charge](./)
