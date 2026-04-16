---
description: Prise en charge des documents électroniques CHILE DTE dans DocBits
---

# 🇨🇱 CHILE DTE

| Propriété | Valeur |
|-----------|--------|
| **Pays / Région** | Chili |
| **Types de documents** | Facture (Factura), Note de crédit, Note de débit, Bon de livraison |
| **Format** | XML |
| **Norme** | DTE (Documento Tributario Electrónico), SII |
| **Paramètres régionaux** | `es_CL` |

DTE (Documento Tributario Electrónico) est la norme chilienne de documents fiscaux électroniques réglementée par le Servicio de Impuestos Internos (SII). Tous les documents DTE partagent le namespace `http://www.sii.cl/SiiDte`. DocBits détecte automatiquement le code de type DTE (`TipoDTE`) et l'achemine vers les règles d'extraction appropriées :

| Code de type | Type de document |
|-------------|-----------------|
| 33 | Factura Electrónica (Facture) |
| 34 | Factura No Afecta o Exenta (Facture exonérée de taxes) |
| 52 | Guía de Despacho (Bon de livraison) |
| 56 | Nota de Débito (Note de débit) |
| 61 | Nota de Crédito (Note de crédit) |

## Statut de prise en charge

| Composant | Statut |
|-----------|--------|
| Aperçu | ✅ Pris en charge |
| Extraction de champs | ✅ Pris en charge |
| Transformation | ✅ Pris en charge |

## Aperçu par défaut

<figure><img src="chile-dte-preview.png" alt="Aperçu Chile DTE Factura dans DocBits"><figcaption><p>Aperçu DocBits par défaut pour une CHILE DTE FACTURA (type 33)</p></figcaption></figure>

## Correspondance des champs

### Champs d'en-tête

| Champ DocBits | Élément XML source | Remarques |
|---|---|---|
| `invoice_id` | `Folio` | Numéro de folio du document |
| `invoice_date` | `FchEmis` | Date d'émission ISO 8601 |
| `due_date` | `FchVenc` | Date d'échéance du paiement |
| `currency` | Fixe : `CLP` | Toujours le peso chilien |
| `total_amount` | `MntTotal` | Montant total TVA comprise |
| `net_amount` | `MntNeto` | Montant net imposable |
| `tax_amount` | `IVA` | Montant de la TVA (taux standard 19 %) |
| `supplier_name` | `RznSoc` (Emisor) | Nom de l'entreprise émettrice |
| `supplier_id` | `RUTEmisor` | RUT de l'émetteur (ex. `76123456-7`) |
| `supplier_address` | `DirOrigen` | Adresse postale de l'émetteur |
| `supplier_city` | `CiudadOrigen` | Ville de l'émetteur |
| `supplier_country` | Fixe : `CL` | Toujours le Chili |
| `buyer_name` | `RznSocRecep` | Nom de l'entreprise destinataire |
| `buyer_id` | `RUTRecep` | RUT du destinataire |
| `buyer_address` | `DirRecep` | Adresse postale du destinataire |
| `buyer_city` | `CiudadRecep` | Ville du destinataire |
| `buyer_country` | Fixe : `CL` | Toujours le Chili |

### Tableau des lignes (`INVOICE_TABLE`)

Chemin de ligne : `Detalle`

| Colonne | Élément XML source | Remarques |
|---|---|---|
| `POSITION` | `NroLinDet` | Numéro de séquence de la ligne |
| `DESCRIPTION` | `NmbItem` | Nom de l'article |
| `QUANTITY` | `QtyItem` | Quantité |
| `UNIT` | `UnmdItem` | Unité de mesure |
| `UNIT_PRICE` | `PrcItem` | Prix unitaire hors TVA |
| `VAT_RATE` | `TasaIVA` (depuis l'en-tête) | Taux IVA en % (généralement 19 %) |
| `VAT` | Calculé | TVA par ligne |
| `NET_AMOUNT` | `MontoItem` | Total de la ligne |

## Règles de classification

DocBits détecte les documents Chile DTE en faisant correspondre le namespace XML et le `TipoDTE` :

| Type de document électronique | Modèle |
|-------------------------------|--------|
| CHILE DTE FACTURA | `http://www.sii.cl/SiiDte` + `<TipoDTE>33</TipoDTE>` |
| CHILE DTE FACTURA ELECTRONICA | `http://www.sii.cl/SiiDte` + `<TipoDTE>34</TipoDTE>` |
| CHILE DTE GUIA DESPACHO | `http://www.sii.cl/SiiDte` + `<TipoDTE>52</TipoDTE>` |
| CHILE DTE NOTA CREDITO | `http://www.sii.cl/SiiDte` + `<TipoDTE>61</TipoDTE>` |

L'élément enveloppe est `<EnvioDTE>` et chaque DTE est encapsulé dans `<DTE><Documento>`.

## Voir aussi

- [Normes de facturation électronique actuellement prises en charge](../../currently-supported-e-invoice-standards/)
- [Documents électroniques pris en charge](./)
