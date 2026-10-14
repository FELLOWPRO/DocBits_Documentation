---
description: Prise en charge des documents électroniques CHILE DTE dans DocBits
---

# 🇨🇱 CHILE DTE

| Propriété | Valeur |
|----------|-------|
| **Pays / Région** | Chili |
| **Types de documents** | Facture, Note de crédit, Note de débit, Bon de livraison |
| **Format** | XML |
| **Norme** | DTE (Documento Tributario Electrónico), SII |
| **Locale** | `es_CL` |

DTE (Documento Tributario Electrónico) est la norme chilienne de documents fiscaux électroniques réglementée par le Servicio de Impuestos Internos (SII). Tous les documents DTE partagent l'espace de noms `http://www.sii.cl/SiiDte`. DocBits détecte automatiquement le code de type DTE (`TipoDTE`) et achemine vers les règles d'extraction appropriées :

| Code de type | Type de document |
|-----------|--------------|
| 33 | Factura Electrónica (Facture) |
| 34 | Factura No Afecta o Exenta (Facture exonérée) |
| 52 | Guía de Despacho (Bon de livraison) |
| 56 | Nota de Débito (Note de débit) |
| 61 | Nota de Crédito (Note de crédit) |

## Statut de prise en charge

| Composant | Statut |
|-----------|--------|
| Aperçu | ✅ Pris en charge |
| Extraction des champs | ✅ Pris en charge |
| Transformation | ✅ Pris en charge |

## Aperçu par défaut

<figure><img src="chile-dte-preview.png" alt="Aperçu de facture Chile DTE dans DocBits"><figcaption><p>Aperçu par défaut DocBits pour une CHILE DTE FACTURA (type 33)</p></figcaption></figure>

## Mappage des champs

### Champs d'en-tête

| Champ DocBits | Élément XML source | Remarques |
|---|---|---|
| `invoice_id` | `Folio` | Numéro de folio du document |
| `invoice_date` | `FchEmis` | Date d'émission ISO 8601 |
| `due_date` | `FchVenc` | Date d'échéance |
| `currency` | Fixe : `CLP` | Toujours peso chilien |
| `total_amount` | `MntTotal` | Montant total TTC |
| `net_amount` | `MntNeto` | Montant net imposable |
| `tax_amount` | `IVA` | Montant de la TVA (taux standard 19%) |
| `supplier_name` | `RznSoc` (Emisor) | Nom de l'entreprise émettrice |
| `supplier_id` | `RUTEmisor` | RUT de l'émetteur (ex. `76123456-7`) |
| `supplier_address` | `DirOrigen` | Adresse de l'émetteur |
| `supplier_city` | `CiudadOrigen` | Ville de l'émetteur |
| `supplier_country` | Fixe : `CL` | Toujours Chili |
| `buyer_name` | `RznSocRecep` | Nom de l'entreprise destinataire |
| `buyer_id` | `RUTRecep` | RUT du destinataire |
| `buyer_address` | `DirRecep` | Adresse du destinataire |
| `buyer_city` | `CiudadRecep` | Ville du destinataire |
| `buyer_country` | Fixe : `CL` | Toujours Chili |

### Tableau des lignes (`INVOICE_TABLE`)

Chemin de la ligne : `Detalle`

| Colonne | Élément XML source | Remarques |
|---|---|---|
| `POSITION` | `NroLinDet` | Numéro de ligne |
| `DESCRIPTION` | `NmbItem` | Désignation de l'article |
| `QUANTITY` | `QtyItem` | Quantité |
| `UNIT` | `UnmdItem` | Unité de mesure |
| `UNIT_PRICE` | `PrcItem` | Prix unitaire HT |
| `VAT_RATE` | `TasaIVA` (de l'en-tête) | Taux de TVA en % (typiquement 19%) |
| `VAT` | Calculé | TVA par ligne |
| `NET_AMOUNT` | `MontoItem` | Total de la ligne |

## Règles de classification

DocBits détecte les documents Chile DTE en faisant correspondre l'espace de noms XML et `TipoDTE` :

| Type de document électronique | Modèle |
|--------------------------|---------|
| CHILE DTE FACTURA | `http://www.sii.cl/SiiDte` + `<TipoDTE>33</TipoDTE>` |
| CHILE DTE FACTURA ELECTRONICA | `http://www.sii.cl/SiiDte` + `<TipoDTE>34</TipoDTE>` |
| CHILE DTE GUIA DESPACHO | `http://www.sii.cl/SiiDte` + `<TipoDTE>52</TipoDTE>` |
| CHILE DTE NOTA CREDITO | `http://www.sii.cl/SiiDte` + `<TipoDTE>61</TipoDTE>` |

L'élément enveloppe est `<EnvioDTE>` et chaque DTE est enveloppé dans `<DTE><Documento>`.

## Voir aussi

- [Normes de e-facturation actuellement prises en charge](../../currently-supported-e-invoice-standards/)
- [Documents électroniques pris en charge](./)
