# ZATCA Fatoora (Arabie saoudite)

## Vue d'ensemble

**ZATCA Fatoora** est le QR code de facturation électronique imposé par l'autorité de la Zakat, des impôts et des douanes d'Arabie saoudite. Depuis **décembre 2021 (Phase 1)**, toute facture B2C émise dans le Royaume doit porter un QR Fatoora contenant les cinq champs de base de la facture ; depuis **janvier 2023 (Phase 2)**, le QR porte en outre une enveloppe de signature cryptographique. DocBits décode les deux phases et renvoie chaque champ de paiement de la Phase 1 comme propriété nommée dans la réponse API du document.

### Présentation de la fonctionnalité

ZATCA Fatoora utilise un format **TLV binaire** (1 octet d'ID de tag, 1 octet de longueur, valeur) encapsulé en **Base64**. Tout le texte est en UTF-8, de sorte que les noms de vendeurs en arabe se décodent proprement. L'extracteur expose les tags 1–5 de la Phase 1 sous forme de champs structurés et — lorsqu'ils sont présents — les tags 6–9 de la Phase 2 sous forme de chaînes Base64 pour les outils de compliance aval. **La vérification de la signature et du hash est volontairement hors périmètre** ; elle relève des stacks dédiés à la conformité.

#### Principaux avantages

* **Couverture de conformité obligatoire** : toute facture B2C saoudienne est analysée.
* **Support de l'arabe** : les noms de vendeurs UTF-8 circulent sans réencodage.
* **Phase 1 et Phase 2** : les deux phases sont détectées ; la phase est exposée dans la sortie.
* **Enveloppe Phase 2 préservée** : hash, signature, clé publique et signature de certificat sont conservés sous forme de chaînes Base64 pour les outils de compliance.

***

### Détection

- TLV binaire encapsulé en Base64 (tags 1–9, 1 octet d'ID de tag + 1 octet de longueur + valeur)
- Détection de phase : `zatca_phase = 1` lorsque seuls les tags 1–5 sont présents ; `zatca_phase = 2` lorsque les tags 6–9 le sont aussi

### Disposition des tags TLV

| Tag | Phase | Contenu |
|-----|-------|---------|
| 1 | 1 | Nom du vendeur (UTF-8, supporte l'arabe) |
| 2 | 1 | Numéro d'enregistrement TVA |
| 3 | 1 | Horodatage de la facture (ISO 8601) |
| 4 | 1 | Total de la facture |
| 5 | 1 | Total TVA |
| 6 | 2 | Hash de la facture XML (Base64) |
| 7 | 2 | Signature numérique (Base64) |
| 8 | 2 | Clé publique (Base64) |
| 9 | 2 | Signature du certificat (Base64) |

### Champs extraits

Tous les champs utilisent le préfixe `zatca_` :

| Champ | Description |
|-------|-------------|
| `zatca_seller_name` | Nom du vendeur (UTF-8) |
| `zatca_vat_number` | Numéro d'enregistrement TVA |
| `zatca_invoice_timestamp` | Date/heure de la facture |
| `zatca_invoice_total` | Total de la facture (décimal) |
| `zatca_vat_total` | Total TVA (décimal) |
| `zatca_phase` | `1` (Phase 1) ou `2` (Phase 2) |
| `zatca_invoice_hash` | Hash de la facture XML — Phase 2 uniquement, Base64 |
| `zatca_signature` | Signature numérique — Phase 2 uniquement, Base64 |
| `zatca_public_key` | Clé publique — Phase 2 uniquement, Base64 |
| `zatca_certificate_signature` | Signature du certificat — Phase 2 uniquement, Base64 |

{% hint style="info" %}
**Hors périmètre** : DocBits ne vérifie ni la signature cryptographique, ni le hash, ni la chaîne de certificats. Cette vérification est un sujet de conformité à part entière et doit être gérée par un stack de facturation électronique certifié ZATCA.
{% endhint %}

### Exemple de réponse API (Phase 1)

```json
{
  "zatca_seller_name": "شركة أكمي التجارية",
  "zatca_vat_number": "300123456700003",
  "zatca_invoice_timestamp": "2026-04-24T10:00:00",
  "zatca_invoice_total": 115.00,
  "zatca_vat_total": 15.00,
  "zatca_phase": 1
}
```

***

### Comment activer la fonctionnalité

L'analyse ZATCA Fatoora est couverte par le réglage général **Extraction de codes-barres / QR** — aucune configuration spécifique au standard n'est nécessaire.

1. **Ouvrez les Paramètres** :
   * Depuis le tableau de bord, allez dans **Paramètres**.
   * Choisissez **Traitement des documents**, puis **Module**.
2. **Activez la fonctionnalité** :
   * Faites défiler jusqu'à l'option **Extraction de codes-barres / QR**.
   * Basculez le curseur pour l'activer.

Pour la liste complète des standards de QR codes de paiement, consultez la [page Vue d'ensemble](./README.md).
