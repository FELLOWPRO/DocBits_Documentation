# EMVCo MPM (QR présenté par le marchand)

## Vue d'ensemble

**EMVCo MPM** (Merchant-Presented Mode) est la spécification mondiale de QR codes maintenue par EMVCo — le même organisme derrière les standards de cartes à puce et de paiements sans contact. Une seule enveloppe TLV (Tag-Length-Value) est partagée par plus d'une douzaine de systèmes nationaux de paiements instantanés, de sorte qu'un parseur unique couvre **Pix** (Brésil), **UPI** (Inde), **PayNow** (Singapour), **PromptPay** (Thaïlande), **QRIS** (Indonésie), **QR Ph** (Philippines), **VietQR** (Vietnam), **FPS** (Hong Kong), **DuitNow** (Malaisie), **NETS** (Singapour) et bien d'autres.

### Présentation de la fonctionnalité

Chaque payload EMVCo MPM partage la même enveloppe : il commence par `000201` (Payload Format Indicator = 01) et se termine par `6304<CRC>`, où `<CRC>` est une somme CRC16-CCITT-FALSE sur 4 hex. À l'intérieur, les tags 26–51 encodés en TLV portent des modèles **Merchant Account Info** identifiés par un **sous-tag GUI** — ce tag GUI permet à DocBits de détecter à quel schéma national appartient le QR. Le CRC est validé et le résultat exposé en tant que booléen afin que les marchands puissent détecter les QR falsifiés.

#### Principaux avantages

* **Un extracteur, plusieurs schémas** : un seul parseur TLV générique couvre toute la famille EMVCo MPM.
* **Schémas nationaux identifiés** : la sortie inclut un schéma nommé (p. ex. `pix`, `upi`, `paynow`), ce qui permet à la logique aval de s'embrancher proprement.
* **Validité CRC exposée** : `emvmpm_crc16_valid` révèle les QR falsifiés ou corrompus.
* **Normalisation des devises** : les codes numériques ISO 4217 sont automatiquement mappés vers alpha-3 (20+ devises ; les codes non mappés passent tels quels).

***

### Détection

- Forme magique : commence par `000201` et se termine par `6304<4-hex CRC16-CCITT-FALSE>`
- Un décodeur TLV générique parcourt chaque tag
- Les schémas nationaux sont identifiés par le **sous-tag GUI** dans les modèles Merchant Account Info (tags 26–51)

### Schémas nationaux reconnus

| Sous-tag GUI | Schéma | Pays |
|--------------|--------|------|
| `br.gov.bcb.pix` | **Pix** | Brésil |
| `UPI` | **UPI** | Inde |
| `SG.PAYNOW` | **PayNow / SGQR** | Singapour |
| `SG.COM.NETS` | **NETS** | Singapour |
| `HK.COM.HKICL.FPS` | **FPS** | Hong Kong |
| `ID.CO.QRIS.WWW` | **QRIS** | Indonésie |
| `COM.BDO.QRPH` / `COM.BPI.QRPH` / `PH.PPMI.P2MEMV` | **QR Ph** | Philippines |
| `COM.QRCODE.TELLUSBANGKOK` + AID `A000000677010111` | **PromptPay** | Thaïlande |
| `A000000727` | **VietQR** | Vietnam |

Les valeurs GUI/AID non reconnues restent analysées — l'extracteur se rabat sur l'ensemble de champs génériques EMVCo MPM.

### Champs extraits

Tous les champs utilisent le préfixe `emvmpm_` :

| Champ | Description |
|-------|-------------|
| `emvmpm_scheme` | Schéma national détecté (p. ex. `pix`, `upi`, `paynow`, `qris`, `promptpay`, `vietqr`, `fps`, `qrph`, `nets`) ou `generic` |
| `emvmpm_merchant_name` | Nom du marchand (tag 59) |
| `emvmpm_merchant_city` | Ville du marchand (tag 60) |
| `emvmpm_country_code` | Code pays ISO 3166 alpha-2 (tag 58) |
| `emvmpm_amount` | Montant de la transaction (décimal, tag 54) |
| `emvmpm_currency` | Devise alpha-3 (convertie depuis le code numérique du tag 53) |
| `emvmpm_additional_data` | Objet imbriqué : numéro de facture, libellé de référence, libellé du terminal, motif de la transaction (sous-tags du tag 62) |
| `emvmpm_crc16_valid` | Booléen — `true` si la somme CRC16 correspond |

### Exemple de réponse API (Pix)

```json
{
  "emvmpm_scheme": "pix",
  "emvmpm_merchant_name": "ACME COMERCIO LTDA",
  "emvmpm_merchant_city": "SAO PAULO",
  "emvmpm_country_code": "BR",
  "emvmpm_amount": 125.00,
  "emvmpm_currency": "BRL",
  "emvmpm_additional_data": {
    "reference_label": "PEDIDO-2026-0427"
  },
  "emvmpm_crc16_valid": true
}
```

***

### Comment activer la fonctionnalité

L'analyse EMVCo MPM est couverte par le réglage général **Extraction de codes-barres / QR** — aucune configuration spécifique au standard n'est nécessaire.

1. **Ouvrez les Paramètres** :
   * Depuis le tableau de bord, allez dans **Paramètres**.
   * Choisissez **Traitement des documents**, puis **Module**.
2. **Activez la fonctionnalité** :
   * Faites défiler jusqu'à l'option **Extraction de codes-barres / QR**.
   * Basculez le curseur pour l'activer.

Pour la liste complète des standards de QR codes de paiement, consultez la [page Vue d'ensemble](./README.md).
