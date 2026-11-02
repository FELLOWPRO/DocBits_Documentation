# SPAYD / Short Payment Descriptor (Tchèque)

## Vue d'ensemble

**SPAYD** (Short Payment Descriptor), également appelé **SPD**, est le QR code de paiement standard défini par l'Association bancaire tchèque. Il est imprimé sur quasiment toutes les factures commerciales tchèques et partiellement utilisé en Slovaquie. DocBits décode les payloads SPAYD et retourne l'instruction de paiement complète — y compris les symboles tchèques spécifiques (variable, specific, constant) — dans la réponse API du document.

### Présentation de la fonctionnalité

Un payload SPAYD est une liste de paires clé:valeur séparées par des astérisques. Les valeurs sont encodées en pourcentage, de sorte que les noms de destinataires et messages en UTF-8 sont préservés. DocBits supporte la variante `ACC` courante (IBAN plus BIC optionnel, séparés par `+`), `ALT-ACC` (IBAN alternatifs, séparés par virgules), et préserve toutes les clés inconnues spécifiques à un fournisseur dans un champ dédié (`spayd_raw_pairs`), afin qu'aucune donnée ne soit perdue en aval.

#### Principaux avantages

* **Couverture complète des paiements tchèques** : IBAN/BIC ainsi que les symboles VS/SS/KS sont extraits vers des champs nommés.
* **Sûr en Unicode** : les noms de destinataires et messages UTF-8 encodés en pourcentage restent intacts.
* **Compatible vers l'avenir** : les clés inconnues sont préservées dans `spayd_raw_pairs`.

***

### Détection

- Préfixe magique : `SPD*1.0*`
- Payload est une liste séparée par `*` de paires `KEY:value`, p. ex. `SPD*1.0*ACC:CZ5508000000001234567899*AM:480.55*CC:CZK`
- Les valeurs sont **encodées en pourcentage** (RFC 3986)
- `ACC` peut porter `IBAN+BIC` (séparés par `+`) ; `ALT-ACC` porte des IBAN alternatifs séparés par virgules

### Champs extraits

Tous les champs utilisent le préfixe `spayd_` :

| Champ | Description |
|-------|-------------|
| `spayd_iban` | IBAN principal (depuis `ACC`) |
| `spayd_bic` | BIC (depuis `ACC`, si présent) |
| `spayd_alt_ibans` | Liste des IBAN alternatifs (depuis `ALT-ACC`) |
| `spayd_amount` | Montant (décimal, depuis `AM`) |
| `spayd_currency` | Devise (depuis `CC`, généralement `CZK`) |
| `spayd_variable_symbol` | Symbole variable (`VS`) — numéro de facture/référence |
| `spayd_specific_symbol` | Symbole spécifique (`SS`) |
| `spayd_constant_symbol` | Symbole constant (`KS`) |
| `spayd_recipient_name` | Nom du destinataire (depuis `RN`) |
| `spayd_due_date` | Date d'échéance (depuis `DT`, `YYYYMMDD`) |
| `spayd_message` | Message libre (depuis `MSG`) |
| `spayd_raw_pairs` | Paires `KEY:value` inconnues ou spécifiques au fournisseur, préservées telles quelles |

### Exemple de réponse API

```json
{
  "spayd_iban": "CZ5508000000001234567899",
  "spayd_amount": 480.55,
  "spayd_currency": "CZK",
  "spayd_variable_symbol": "2026041720",
  "spayd_constant_symbol": "0308",
  "spayd_recipient_name": "Moje firma, s.r.o.",
  "spayd_due_date": "20260507",
  "spayd_message": "Platba za fakturu 2026041720"
}
```

***

### Comment activer la fonctionnalité

L'analyse SPAYD est couverte par le réglage général **Extraction de codes-barres / QR** — aucune configuration spécifique au standard n'est nécessaire.

1. **Ouvrez les Paramètres** :
   * Depuis le tableau de bord, allez dans **Paramètres**.
   * Choisissez **Traitement des documents**, puis **Module**.
2. **Activez la fonctionnalité** :
   * Faites défiler jusqu'à l'option **Extraction de codes-barres / QR**.
   * Basculez le curseur pour l'activer.

Pour la liste complète des standards de QR codes de paiement, consultez la [page Vue d'ensemble](./README.md).
