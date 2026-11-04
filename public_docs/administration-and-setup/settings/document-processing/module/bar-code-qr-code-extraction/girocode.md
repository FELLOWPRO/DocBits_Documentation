# GiroCode (EPC069-12)

## Vue d'ensemble

Le **GiroCode** est le QR code de paiement SEPA défini par le European Payments Council dans la spécification **EPC069-12**. Il est le standard de facto sur les factures des banques allemandes et autrichiennes (Sparkasse, VR-Banken, Deutsche Bank, Commerzbank, PSA Austria) et il est également émis aux Pays-Bas, en Belgique et en Finlande. DocBits décode les deux révisions (**v001** et **v002**) et retourne la charge utile SEPA complète dans la réponse API du document.

### Présentation de la fonctionnalité

Un GiroCode contient tout ce qu'il faut pour initier un virement SEPA : BIC et IBAN du bénéficiaire, nom du bénéficiaire, montant, motif et soit une référence créancière structurée, soit un texte libre de communication. DocBits normalise la charge utile afin d'accepter sans erreur **les montants avec `.` ou `,` comme séparateur décimal** — une déviation fréquente des générateurs allemands par rapport à la spécification.

#### Principaux avantages

* **Large couverture DE / AT** : toutes les grandes banques de détail impriment des GiroCodes sur les factures clients.
* **Deux révisions supportées** : v001 (BIC obligatoire) et v002 (BIC optionnel dans l'EEE).
* **Tolérant aux séparateurs décimaux** : `227.01` et `227,01` sont acceptés indifféremment.

***

### Détection

- Préfixe magique : `BCD\n001` (v001) ou `BCD\n002` (v002)
- Charge utile structurée par lignes conforme à la spécification EPC069-12
- **v002** rend le BIC optionnel lorsque l'IBAN appartient à l'Espace unique de paiements en euros

### Champs extraits

Tous les champs utilisent le préfixe `girocode_` :

| Champ | Description |
|-------|-------------|
| `girocode_bic` | BIC du bénéficiaire (obligatoire en v001, optionnel en v002 pour l'EEE) |
| `girocode_creditor_name` | Nom du bénéficiaire |
| `girocode_iban` | IBAN du bénéficiaire |
| `girocode_amount` | Montant (décimal) — `.` et `,` acceptés |
| `girocode_currency` | Devise (généralement `EUR`) |
| `girocode_purpose` | Code de motif SEPA |
| `girocode_structured_reference` | Référence créancière structurée (ISO 11649 RF) |
| `girocode_unstructured_remittance` | Communication libre |
| `girocode_version` | `001` ou `002` |

### Exemple de réponse API

Exemple réel (facture Dr. Meindl u. Partner) :

```json
{
  "girocode_bic": "DAAEDEDDXXX",
  "girocode_creditor_name": "Dr. Meindl u. Partner",
  "girocode_iban": "DE69300606010006343686",
  "girocode_amount": 227.01,
  "girocode_currency": "EUR",
  "girocode_unstructured_remittance": "38710498001705 - QR",
  "girocode_version": "002"
}
```

***

### Comment activer la fonctionnalité

L'analyse GiroCode est couverte par le réglage général **Extraction de codes-barres / QR** — aucune configuration spécifique au standard n'est nécessaire.

1. **Ouvrez les Paramètres** :
   * Depuis le tableau de bord, allez dans **Paramètres**.
   * Choisissez **Traitement des documents**, puis **Module**.
2. **Activez la fonctionnalité** :
   * Faites défiler jusqu'à l'option **Extraction de codes-barres / QR**.
   * Basculez le curseur pour l'activer.

Pour la liste complète des standards de QR codes de paiement, consultez la [page Vue d'ensemble](./README.md).
