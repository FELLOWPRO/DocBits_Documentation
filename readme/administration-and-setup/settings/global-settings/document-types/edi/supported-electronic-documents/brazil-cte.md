---
description: Support du document électronique BRAZIL CT-E dans DocBits
---

# 🇧🇷 BRAZIL CT-E

| Propriété | Valeur |
|-----------|--------|
| **Pays / Région** | Brésil |
| **Types de documents** | Document de transport (Conhecimento de Transporte Eletrônico) |
| **Format** | XML |
| **Standard** | CT-e 3.0 (connaissement de fret/transport électronique) |
| **Langue** | `pt_BR` |

Le CT-e (Conhecimento de Transporte Eletrônico, `<mod>57</mod>`) est le document de transport électronique brésilien émis par les entreprises de logistique et de fret. Il documente le service de transport, la valeur du chargement, les municipalités d'origine et de destination (`cMunIni` / `cMunFim`) ainsi que le prix du fret (`vTPrest`). Contrairement à la NF-e, le CT-e utilise `cteProc` comme élément racine et référence les documents NF-e associés.

## Statut de prise en charge

| Composant | Statut |
|-----------|--------|
| Aperçu | ✅ Pris en charge |
| Extraction des champs | ✅ Pris en charge |
| Transformation | ✅ Pris en charge |

## Aperçu par défaut

<figure><img src="brazil-cte-preview.png" alt="Aperçu Brazil CT-e dans DocBits"><figcaption><p>Aperçu DocBits par défaut pour un document BRAZIL CT-E</p></figcaption></figure>

## Correspondance des champs

### Champs d'en-tête

| Champ DocBits | XPath source | Remarques |
|---|---|---|
| `invoice_id` | `//*[local-name()='ide']/*[local-name()='nCT']` | Numéro du CT-e |
| `invoice_date` | `//*[local-name()='ide']/*[local-name()='dhEmi']` | ISO 8601 avec décalage BRT |
| `currency` | Fixe : `BRL` | Toujours Real brésilien |
| `total_amount` | `//*[local-name()='vPrest']/*[local-name()='vTPrest']` | Valeur totale du service de fret |
| `net_amount` | `//*[local-name()='vPrest']/*[local-name()='vRec']` | Montant à recevoir |
| `tax_amount` | `//*[local-name()='ICMS']//*[local-name()='vICMS']` | ICMS sur le service de transport |
| `supplier_name` | `//*[local-name()='emit']/*[local-name()='xNome']` | Nom du transporteur (transportadora) |
| `supplier_id` | `//*[local-name()='emit']/*[local-name()='CNPJ']` | CNPJ du transporteur |
| `buyer_name` | `//*[local-name()='dest']/*[local-name()='xNome']` | Nom du destinataire (consignataire) |
| `buyer_id` | `//*[local-name()='dest']/*[local-name()='CNPJ']` | CNPJ du destinataire |

> Le CT-e ne comprend pas de table de lignes — le service de transport est une charge unique au niveau du document.

## Règle de classification

DocBits détecte les documents BRAZIL CT-E via :

```
http://www.portalfiscal.inf.br/cte
```

dans l'espace de noms XML (élément racine `<cteProc>`).

## Liens connexes

- [BRAZIL NF-E](brazil-nfe.md)
- [BRAZIL NFC-E](brazil-nfce.md)
- [BRAZIL NFS-E](brazil-nfse.md)
- [Documents électroniques pris en charge](./)
