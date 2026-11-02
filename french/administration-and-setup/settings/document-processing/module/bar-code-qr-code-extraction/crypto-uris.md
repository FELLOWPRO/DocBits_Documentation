# URIs de paiement crypto (BIP21 / BIP321)

## Vue d'ensemble

Les URIs de paiement crypto constituent le standard informel mais largement adopté pour encoder des demandes de paiement en cryptomonnaie dans des QR codes. DocBits reconnaît à la fois **BIP21** (l'URI de paiement Bitcoin originale) et **BIP321** (l'extension modernisée de 2024), sur les cinq blockchains les plus courantes : **Bitcoin**, **Lightning Network**, **Zcash**, **Ethereum** et **Litecoin**.

### Présentation de la fonctionnalité

Un payload QR crypto est une URI avec un schéma (`bitcoin:`, `lightning:`, `zcash:`, `ethereum:`, `litecoin:`), une adresse de destinataire et un ensemble de paramètres façon URL. DocBits extrait tous les paramètres BIP21 standards (`amount`, `label`, `message`) et les extensions plus récentes de BIP321 (`lightning=` fallback, `pj=` / `pjos=` payjoin). Selon la spécification BIP21, les paramètres préfixés par `req-` peuvent être rejetés par les clients s'ils ne sont pas supportés — DocBits les conserve donc dans un champ séparé (`crypto_required_params`) pour que les clients décident comment les traiter.

#### Principaux avantages

* **Multi-chaînes** : Bitcoin, Lightning, Zcash, Ethereum et Litecoin dans un seul extracteur.
* **BIP21 + BIP321** : les deux versions sont reconnues ; la version est exposée dans la sortie.
* **Schéma insensible à la casse** : `BITCOIN:` et `bitcoin:` sont traités de la même manière.

***

### Détection

- Détection basée sur le schéma (insensible à la casse) : `bitcoin:`, `lightning:`, `zcash:`, `ethereum:`, `litecoin:`
- Format URI standard : `<scheme>:<address>?<param>=<value>&<param>=<value>`

### Paramètres supportés

**Paramètres principaux BIP21 :**
- `amount` — montant demandé dans l'unité native
- `label` — libellé lisible du destinataire
- `message` — texte libre

**Extensions BIP321 :**
- `lightning=<BOLT11>` — facture Lightning en fallback
- `pj=<endpoint>` / `pjos=<endpoint>` — endpoints payjoin
- `req-*` — paramètres requis (préservés dans `crypto_required_params`)

### Champs extraits

Tous les champs utilisent le préfixe `crypto_` :

| Champ | Description |
|-------|-------------|
| `crypto_scheme` | `bitcoin`, `lightning`, `zcash`, `ethereum` ou `litecoin` |
| `crypto_address` | Adresse du destinataire |
| `crypto_amount` | Montant demandé (décimal) |
| `crypto_currency` | Symbole de la devise native (`BTC`, `ETH`, `LTC`, `ZEC`) |
| `crypto_label` | Libellé du destinataire (si défini) |
| `crypto_message` | Texte libre (si défini) |
| `crypto_lightning_fallback` | Facture Lightning BOLT11 (depuis `lightning=` BIP321) |
| `crypto_payjoin_endpoint` | Endpoint payjoin (depuis `pj=` / `pjos=`) |
| `crypto_required_params` | Tous les paramètres `req-*`, préservés pour décision côté client |
| `crypto_uri_version` | `bip21` ou `bip321` |

### Exemple de réponse API

```json
{
  "crypto_scheme": "bitcoin",
  "crypto_address": "bc1q9h6mksxrsfnd4ymr8mu2w2v3v0sylgkfghxwzm",
  "crypto_amount": 0.00254,
  "crypto_currency": "BTC",
  "crypto_label": "Acme Invoice 2026-042",
  "crypto_message": "Payment for invoice 2026-042",
  "crypto_uri_version": "bip21"
}
```

***

### Comment activer la fonctionnalité

L'analyse des URIs crypto est couverte par le réglage général **Extraction de codes-barres / QR** — aucune configuration spécifique au standard n'est nécessaire.

1. **Ouvrez les Paramètres** :
   * Depuis le tableau de bord, allez dans **Paramètres**.
   * Choisissez **Traitement des documents**, puis **Module**.
2. **Activez la fonctionnalité** :
   * Faites défiler jusqu'à l'option **Extraction de codes-barres / QR**.
   * Basculez le curseur pour l'activer.

Pour la liste complète des standards de QR codes de paiement, consultez la [page Vue d'ensemble](./README.md).
