# Mappage des champs ZUGFeRD + Swiss QR Code

## Aperçu

Lors du traitement des factures PDF contenant à la fois des données XML ZUGFeRD et un code QR suisse (Swiss QR Code), DocBits extrait les données des deux sources et les fusionne intelligemment.

## Comment ça marche

1. **Extraction XML ZUGFeRD** - DocBits extrait d'abord les champs du XML ZUGFeRD intégré
2. **Détection du Swiss QR Code** - Le barcode détecte et analyse les codes QR suisses
3. **Fusion Intelligente (Smart Merge)** - Les champs vides sont remplis à partir des données Swiss QR (les champs avec des valeurs sont préservés)
4. **Piste d'audit (Audit Trail)** - Les données complètes du code QR sont stockées dans `qr_code_data` pour vérification

## Tableau de Mappage des Champs

### Mappage des Champs Swiss QR Code → DocBits

| Champ Swiss QR | Champ DocBits | Description |
| :--- | :--- | :--- |
| IBAN | `supplier_iban` | IBAN du créancier (ex. CH9300762011...) |
| Amount | `total_amount` | Montant du paiement (ex. 1234.56) |
| Currency | `currency` | Code devise (CHF ou EUR) |
| Reference | `payment_reference` / `esr_reference` | Référence QR ou numéro BVR (ESR) |
| Creditor.Name | `supplier_name` | Nom de la société fournisseur |
| Creditor.AddressLine1 | `supplier_address` | Adresse (rue) |
| Creditor.PostalCode | `supplier_plz` | Code postal |
| Creditor.City | `supplier_city` | Ville |
| Creditor.Country | `supplier_country` | Code pays (CH) |
| Debtor.Name | `company_name` | Nom de la société destinataire |
| Debtor.AddressLine1 | `company_street` | Adresse du destinataire |
| Debtor.PostalCode | `company_plz` | Code postal du destinataire |
| Debtor.City | `company_city` | Ville du destinataire |

## Exemple : Traitement d'une facture type

### Document d'entrée

*   **PDF** : Facture avec XML ZUGFeRD 1.0 intégré + code-barres Swiss QR Code

### Données extraites du Swiss QR Code

```json
{
  "supplier_iban": "CH9300762011623852957",
  "amount_to_pay": 1234.56,
  "currency": "CHF",
  "esr_reference": "210000000003139471430009017",
  "supplier_name": "Sample Company GmbH",
  "supplier": {
    "name": "Sample Company GmbH",
    "address_line_1": "Musterstrasse",
    "address_line_2": "123",
    "postal_code": "8000",
    "city": "Zürich",
    "country": "CH"
  },
  "recipient": {
    "name": "Demo Customer AG",
    "address_line_1": "Beispielweg 45",
    "postal_code": "3000",
    "city": "Bern",
    "country": "CH"
  }
}
```

### Résultats de l'extraction des champs

| Champ | Valeur | Source | Méthode |
| :--- | :--- | :--- | :--- |
| `supplier_iban` | CH9300762011623852957 | ZUGFeRD XML | ED |
| `total_amount` | 1234.56 | ZUGFeRD XML | ED |
| `currency` | CHF | ZUGFeRD XML | ED |
| `supplier_name` | Sample Company GmbH | ZUGFeRD XML | ED |
| `supplier_address` | Musterstrasse 123 | ZUGFeRD XML | ED |
| `payment_reference` | 210000000003139471430009017 | Swiss QR | SWISS_QR |
| `supplier_plz` | 8000 | Swiss QR | SWISS_QR |
| `supplier_city` | Zürich | Swiss QR | SWISS_QR |

## Méthodes d'extraction

| Code Méthode | Description |
| :--- | :--- |
| **ED** | Document Électronique (ZUGFeRD/XRechnung/PEPPOL XML) |
| **SWISS_QR** | Extraction de code-barres Swiss QR Code |
| **OCR** | Reconnaissance Optique de Caractères |
| **ML** | Extraction par Machine Learning |

## Priorité de fusion

1.  **ZUGFeRD XML** a la priorité la plus élevée (données structurées et fiables)
2.  **Swiss QR Code** remplit les champs vides (garanti précis pour les données de paiement)
3.  **OCR/ML** utilisé pour les champs absents des sources électroniques

## Versions de Swiss QR Code prises en charge

*   Format Swiss QR Bill (ISO 20022)
*   Format QR-IBAN (commence par 30, 31)
*   Format IBAN standard
*   Avec/sans référence structurée (QRR, SCOR)

## Exigence de version

Cette fonctionnalité nécessite **api version 10.95.6** et **barcode version 1.0.5** ou supérieure.

### Versions des composants (Environnement Dev)

| Composant | Version | Description |
| :--- | :--- | :--- |
| `api` | 10.95.6 | API principale avec prise en charge de l'extraction ZUGFeRD 1.0 |
| `barcode` | 1.0.5 | Détection et analyse du Swiss QR Code |
| `Auth` | 1.48.8 | Service d'authentification |

