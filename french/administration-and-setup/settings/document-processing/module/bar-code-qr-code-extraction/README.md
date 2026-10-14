# Extraction de codes-barres / QR

{% hint style="info" %}
**Associé :** Pour lire manuellement la valeur d'un code-barres/QR lors de la validation d'un document et l'affecter à un champ, voir [Affectation par code-barres](../barcode-assignment.md).
{% endhint %}

## **Vue d'ensemble**

Cette fonctionnalité permet l'extraction automatique d'informations contenues dans **les codes-barres et les QR codes** présents dans les documents. Il s'agit d'un réglage « tout ou rien » — l'activer déclenche l'extraction pour les deux types de codes.

## Comment activer l'extraction de codes-barres / QR

Pour activer la fonctionnalité, procédez ainsi :

1. **Ouvrez les Paramètres** :
   * Depuis le tableau de bord, allez dans **Paramètres**.
   * Choisissez **Traitement des documents**, puis **Module**.
2. **Activez la fonctionnalité** :
   * Faites défiler jusqu'à l'option **Extraction de codes-barres / QR**.
   *   Basculez le curseur pour activer l'extraction.\
       \


       <figure><img src="../../../../../.gitbook/assets/image (445).png" alt=""><figcaption></figcaption></figure>

## **Types de codes pris en charge**

DocBits prend en charge l'extraction des types de codes suivants :

* **QR-CODE**
* **EAN-2**, **EAN-5**, **EAN-8**, **EAN-13**
* **UPC-A**, **UPC-E**
* **ISBN-10**, **ISBN-13**
* **COMPOSITE**
* **I25**&#x20;
* **DATABAR**, **DATABAR-EXP**
* **CODABAR**
* **CODE-39**, **CODE-93**, **CODE-128**
* **PDF-417**
* **SQ-CODE**

## Standards de QR codes de paiement

Au-delà du décodage générique, DocBits reconnaît **sept standards distincts de QR codes de paiement** et extrait automatiquement leurs champs de paiement dans la réponse API du document. Les clients n'ont plus besoin de décoder manuellement ces chaînes — chaque standard dispose de son propre préfixe de champ (p. ex. `swissqr_*`, `girocode_*`) afin que les valeurs alimentent directement le matching, la validation et l'export.

| # | Standard | Région | Préfixe de champ | Usage typique |
|---|----------|--------|------------------|---------------|
| 1 | [Swiss QR Bill](swiss-qr-code.md) | Suisse | `swissqr_*` | Toute facture suisse depuis 2020 |
| 2 | [GiroCode (EPC069-12)](girocode.md) | DE, AT, NL, BE, FI | `girocode_*` | Paiements SEPA |
| 3 | [SPAYD / SPD](spayd.md) | CZ, partiellement SK | `spayd_*` | Standard de l'Association bancaire tchèque |
| 4 | [PagoPA](pagopa.md) | IT (administration publique) | `pagopa_*` | Obligatoire sur les factures de la PA italienne |
| 5 | [URIs de paiement crypto](crypto-uris.md) | Mondial (crypto) | `crypto_*` | Bitcoin, Lightning, Ethereum, Zcash, Litecoin |
| 6 | [EMVCo MPM](emvco-mpm.md) | BR, IN, SG, TH, MY, ID, PH, VN, HK et plus | `emvmpm_*` | Pix, UPI, PayNow, PromptPay, QRIS, QR Ph, VietQR, FPS |
| 7 | [ZATCA Fatoora](zatca-fatoora.md) | Arabie saoudite | `zatca_*` | Obligatoire sur toute facture KSA |

**La détection est automatique.** Chaque chaîne QR décodée est inspectée pour son préfixe magique (p. ex. `SPC\n0200` pour Swiss QR Bill v2.0 ou `PAGOPA|002|` pour PagoPA) ; seuls les standards reconnus sont convertis en champs structurés.

### **Pages associées**

[Détails sur l'extraction de codes-barres](bar-code-extractions.md)
