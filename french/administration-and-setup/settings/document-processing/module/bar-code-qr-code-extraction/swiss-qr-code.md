# Swiss QR Bill

## Vue d'ensemble

La **Swiss QR Bill** est le standard national de bulletin de paiement qui, depuis le 30 juin 2020, a remplacé les anciens bulletins orange et rouge suisses. Toute facture nationale suisse — qu'elle émane d'un fournisseur d'énergie, d'un assureur ou d'un partenaire commercial — comporte aujourd'hui un QR Swiss QR Bill. DocBits décode ces codes automatiquement et met chaque champ de paiement à disposition via la réponse API.

### Présentation de la fonctionnalité

Les Swiss QR Bills suivent le standard de paiement **ISO 20022** et sont émises en deux versions : **v1.0** (déploiement initial) et **v2.0** (actuelle). L'extracteur DocBits prend en charge les deux. Les payloads reconnus sont décodés en un ensemble complet de champs — créancier, débiteur, IBAN / QR-IBAN, montant, devise, type de référence (QRR, SCOR ou NON), messages structurés et libres, schémas de paiement alternatifs.

<figure><img src="../../../../../.gitbook/assets/image (6) (1) (1) (1) (1) (1) (1) (1).png" alt=""><figcaption></figcaption></figure>

#### Principaux avantages

* **Zéro saisie manuelle** pour les factures suisses : IBAN, montant, référence et créancier alimentent directement le document.
* **Les deux versions couvertes** : v1.0 et v2.0 sont détectées automatiquement.
* **Types de référence préservés** : QRR, SCOR et NON sont conservés exactement tels qu'imprimés, ce qui maintient le rapprochement aval opérationnel.

***

### Détection

- Préfixe magique : `SPC\n0100` (v1.0) ou `SPC\n0200` (v2.0)
- Conforme à ISO 20022
- Le parseur expose également `alt-schemes` (schémas de paiement alternatifs) lorsqu'ils sont présents

### Champs extraits

Tous les champs utilisent le préfixe `swissqr_` :

| Champ | Description |
|-------|-------------|
| `swissqr_account` | IBAN ou QR-IBAN du créancier |
| `swissqr_creditor_name` | Nom du créancier |
| `swissqr_creditor_street` | Rue / ligne d'adresse du créancier |
| `swissqr_creditor_city` | Ville du créancier |
| `swissqr_creditor_postal_code` | Code postal du créancier |
| `swissqr_creditor_country` | Pays du créancier (ISO 3166 alpha-2) |
| `swissqr_debtor_name` | Nom du débiteur (si imprimé) |
| `swissqr_debtor_street`, `swissqr_debtor_city`, `swissqr_debtor_postal_code`, `swissqr_debtor_country` | Adresse du débiteur |
| `swissqr_amount` | Montant (décimal) |
| `swissqr_currency` | Devise (ISO 4217) — généralement `CHF` ou `EUR` |
| `swissqr_reference` | Référence structurée (QRR ou SCOR) |
| `swissqr_reference_type` | `QRR`, `SCOR` ou `NON` |
| `swissqr_unstructured_message` | Texte libre de communication |
| `swissqr_bill_information` | Informations de facturation structurées (S1 / Swico) |
| `swissqr_alt_schemes` | Procédures alternatives (si présentes) |

### Exemple de réponse API

```json
{
  "swissqr_account": "CH4431999123000889012",
  "swissqr_creditor_name": "Robert Schneider AG",
  "swissqr_creditor_street": "Rue du Lac 1268",
  "swissqr_creditor_city": "Biel",
  "swissqr_creditor_postal_code": "2501",
  "swissqr_creditor_country": "CH",
  "swissqr_amount": 1949.75,
  "swissqr_currency": "CHF",
  "swissqr_reference": "210000000003139471430009017",
  "swissqr_reference_type": "QRR",
  "swissqr_unstructured_message": "Bill No. 3139 for services 2026"
}
```

***

### Comment activer la fonctionnalité

L'analyse Swiss QR Bill est couverte par le réglage général **Extraction de codes-barres / QR** — aucune configuration spécifique au standard n'est nécessaire.

1. **Ouvrez les Paramètres** :
   * Depuis le tableau de bord, allez dans **Paramètres**.
   * Choisissez **Traitement des documents**, puis **Module**.
2. **Activez la fonctionnalité** :
   * Faites défiler jusqu'à l'option **Extraction de codes-barres / QR**.
   * Basculez le curseur pour l'activer.

<figure><img src="../../../../../.gitbook/assets/image (444).png" alt=""><figcaption></figcaption></figure>

Pour la liste complète des standards de QR codes de paiement, consultez la [page Vue d'ensemble](./README.md).
