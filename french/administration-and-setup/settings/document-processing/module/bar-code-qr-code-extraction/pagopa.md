# PagoPA

## Vue d'ensemble

**PagoPA** est le standard de QR code de paiement de l'administration publique italienne. Toute facture émise par un organisme de la PA italienne (communes, universités, santé, administrations fiscales) comporte un QR code PagoPA. DocBits décode la charge utile et renvoie les quatre champs de paiement obligatoires dans la réponse API du document.

### Présentation de la fonctionnalité

Les charges utiles PagoPA sont compactes et strictement structurées : exactement **cinq champs séparés par un pipe** sur une seule ligne. Les montants sont encodés en **centimes** (entier) et automatiquement convertis en euros décimaux par l'extracteur. Les zéros de tête du `codice_avviso` (avis de paiement à 18 chiffres) sont préservés — il ne doit jamais être interprété comme entier, car il s'agit d'un identifiant de longueur fixe.

#### Principaux avantages

* **Couverture obligatoire** pour les factures PA italiennes : `codice_avviso` et code fiscal du créancier sont extraits vers des champs nommés.
* **Traitement numérique sûr** : le `codice_avviso` à 18 chiffres conserve ses zéros de tête ; le montant en centimes est également exposé comme euro décimal.

***

### Détection

- Préfixe magique : `PAGOPA|002|`
- Exactement **5 champs séparés par un pipe** après le préfixe : `PAGOPA|002|<codice_avviso>|<fiscal_code_creditor>|<amount_cents>|<auth>`
- **EUR uniquement** — aucune autre devise n'est valide selon la spécification

### Champs extraits

Tous les champs utilisent le préfixe `pagopa_` :

| Champ | Description |
|-------|-------------|
| `pagopa_codice_avviso` | Avis de paiement à 18 chiffres — zéros de tête préservés (chaîne) |
| `pagopa_fiscal_code_creditor` | Code fiscal du créancier à 11 chiffres (chaîne) |
| `pagopa_amount_cents` | Montant en centimes (entier) |
| `pagopa_amount` | Montant en euros (décimal, dérivé de `pagopa_amount_cents`) |
| `pagopa_auth` | Indicateur d'auth/version optionnel depuis la charge utile |

### Exemple de réponse API

```json
{
  "pagopa_codice_avviso": "301234567890123456",
  "pagopa_fiscal_code_creditor": "80012345678",
  "pagopa_amount_cents": 12050,
  "pagopa_amount": 120.50
}
```

***

### Comment activer la fonctionnalité

L'analyse PagoPA est couverte par le réglage général **Extraction de codes-barres / QR** — aucune configuration spécifique au standard n'est nécessaire.

1. **Ouvrez les Paramètres** :
   * Depuis le tableau de bord, allez dans **Paramètres**.
   * Choisissez **Traitement des documents**, puis **Module**.
2. **Activez la fonctionnalité** :
   * Faites défiler jusqu'à l'option **Extraction de codes-barres / QR**.
   * Basculez le curseur pour l'activer.

Pour la liste complète des standards de QR codes de paiement, consultez la [page Vue d'ensemble](./README.md).
