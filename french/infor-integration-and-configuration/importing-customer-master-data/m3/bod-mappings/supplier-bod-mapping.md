# Supplier BOD Mapping

Cette page documente la façon dont DocBits ingère les données de base fournisseurs d'Infor M3 via les BODs `SyncSupplierPartyMaster` et `SyncRemitToPartyMaster`. Les deux BODs alimentent la même table de données de base `SUPPLIER` dans DocBits.

{% file src="../../../../.gitbook/assets/Sync.SupplierPartyMaster.pdf" %}
SupplierPartyMaster — Référence d'origine du mappage BOD (PDF)
{% endfile %}

{% file src="../../../../.gitbook/assets/Sync.RemitToPartyMaster.pdf" %}
RemitToPartyMaster — Référence d'origine du mappage BOD (PDF)
{% endfile %}

## Principes clés

- **CONO + SUNO est la clé d'appariement.** Une ligne `supplier_header` dans DocBits est identifiée de manière unique par `(customer_number = sharedCONO, supplier_number = sharedSUNO)`. Cela permet à une seule organisation DocBits de consolider plusieurs sociétés M3.
- **`variationID` protège contre les BODs hors-séquence.** M3 peut émettre le même enregistrement maître plusieurs fois en succession rapide ; la `variationID` entrante doit être supérieure à celle stockée pour qu'une mise à jour soit acceptée. Les deux BODs suivent leur `variationID` indépendamment (`variation_id_supplier_bod`, `variation_id_remit_to_party`).
- **Aucun écrasement silencieux.** SupplierPartyMaster et RemitToPartyMaster partagent plusieurs champs (nom, téléphone, TVA, banque, statut). Chaque BOD ne met à jour que les champs qu'il possède, et uniquement si sa `variationID` avance. Au sein de l'ensemble partagé, le BOD reçu le plus récemment (par type de BOD) l'emporte.
- **La synchronisation multi-banque est pilotée par préférence.** Comportement par défaut : la dernière `FinancialParty` est écrite dans `bank_id` sur l'en-tête. Avec la préférence `ALLOW_MULTIPLE_SUPPLIER_ACCOUNTS_SYNC` activée, chaque entrée `FinancialParty` est persistée dans `supplier_account` (IBAN, ID de compte, code devise, indicateur de préférence).
- **Découpe optionnelle du suffixe CONO.** Certaines installations M3 ajoutent un suffixe de division au numéro de société (par ex. `100_01`). La préférence `EXCLUDE_DIVISION_FOR_CUSTOMER_NUMBER` retire les suffixes `_*` pour que les clés DocBits restent cohérentes. Avec la découpe activée, plusieurs BODs RemitToPartyMaster par division s'effondrent sur une seule clé d'appariement — et le BOD avec la `variationID` la plus élevée l'emporte. Voir la FAQ « *Que se passe-t-il quand un BOD RemitToPartyMaster est émis par division ?* » ci-dessous.

## Sync.SupplierPartyMaster

→ Table de données de base DocBits : **SUPPLIER**

```python
header_mappings = {
            "sharedCONO": "//DataArea/Sync/AccountingEntityID",
            "sharedSUNO": "//SupplierPartyMaster/PartyIDs/ID",
            "variationID": "//SupplierPartyMaster/PartyIDs/ID/@variationID",
            "supplierName": "//SupplierPartyMaster/Name",
            "phone": '//Communication[ChannelCode="Phone"]/DialNumber',
            "vatNo": "//SupplierPartyMaster/PartyIDs/TaxID",
            "paymentTermId": "//SupplierPartyMaster/PaymentTermID",
            "paymentMethodCode": "//SupplierPartyMaster/PaymentMethodCode",
            "buyerPersonReferenceId": "//SupplierPartyMaster/BuyerPersonReference/IDs/ID",
            "buyerPersonReference": "//SupplierPartyMaster/BuyerPersonReference/Name",
            "supplier_category": "//SupplierPartyMaster/Classification/Codes/Code[@listID='Supplier Categories']",
            "supplier_group": "//SupplierPartyMaster/Classification/Codes/Code[@listID='Supplier Group']",
            "discount_terms_description": "//SupplierPartyMaster/UserArea/Property/NameValue[@name='eam.UDFCHAR06']",
            "status": "//SupplierPartyMaster/Status/Code",
            "bank_id": "//SupplierPartyMaster/FinancialParty[last()]/FinancialAccount/ID",
        }
```

### Référence des champs

| Champ DocBits | Source M3 | Description |
|---|---|---|
| `sharedCONO` | Numéro de société M3 | Mappe sur `customer_number` dans `supplier_header`. Élément de la clé d'appariement. |
| `sharedSUNO` | `CIDMAS.IDSUNO` | Numéro de fournisseur M3. Élément de la clé d'appariement. |
| `variationID` | Attribut du BOD | Stocké dans `variation_id_supplier_bod`. Les BODs entrants ne sont acceptés que si leur `variationID` dépasse celle stockée. Un attribut absent est traité comme `0` (force-update). |
| `supplierName` | `CIDMAS.IDSUNM` | Nom d'affichage du fournisseur. |
| `phone` | `CIDMAS.PHNO/PHN2/IDTFNO` | Numéro de téléphone du canal `Phone`. |
| `vatNo` | `CIDMAS.IDVRNO` | Identifiant TVA. Lu depuis `PartyIDs/TaxID` (sans filtre `@schemeName` dans le chemin d'ingestion M3). **OUVERT** — quand M3 émet plusieurs éléments `TaxID` avec des valeurs `@schemeName` différentes (par ex. `VatCode`, `TaxIdentificationNumber`), la première occurrence l'emporte. Un filtre `schemeName` configurable est prévu ; partagez un BOD d'exemple afin de définir le default correct. <!-- tracked in DOCB-12313 --> |
| `paymentTermId` | `CIDVEN.IITEPY` | Identifiant des conditions de paiement. |
| `paymentMethodCode` | — | Code de mode de paiement, lorsqu'il est fourni. |
| `buyerPersonReferenceId` / `buyerPersonReference` | `CIDVEN.IIBUYE` / `CSYUSR.CRRENM` | Référence (utilisateur M3) et nom d'affichage de l'acheteur assigné. |
| `supplier_category` | — | Lu depuis `Classification/Codes/Code[@listID='Supplier Categories']`. Extension UserArea optionnelle ; NULL sur installations M3 standard. |
| `supplier_group` | `CIDVEN.IISUCL` | Groupe de classification du fournisseur. |
| `discount_terms_description` | — | Extension UserArea optionnelle (`eam.UDFCHAR06`) utilisée par le calculateur de date d'escompte de DocBits. Quand le fournisseur fournit ici une valeur de jours d'escompte, DocBits la combine avec la date de facture pour produire une date d'échéance d'escompte pour l'équipe comptable. |
| `status` | `CIDMAS.IDSTAT` | Statut actif/inactif du fournisseur, pris depuis `SupplierPartyMaster/Status/Code`. |
| `bank_id` | `CBANAC.BCBKNO` | Compte bancaire par défaut, pris depuis la *dernière* `FinancialParty`. Activez `ALLOW_MULTIPLE_SUPPLIER_ACCOUNTS_SYNC` pour synchroniser chaque `FinancialParty` dans la table `supplier_account`. |

## Sync.RemitToPartyMaster

→ Table de données de base DocBits : **SUPPLIER**

```python
header_mappings = {
            "sharedCONO": "//DataArea/Sync/AccountingEntityID",
            "sharedSUNO": "//RemitToPartyMaster/PartyIDs/ID",
            "variationID": "//RemitToPartyMaster/PartyIDs/ID/@variationID",
            "supplierName": "//RemitToPartyMaster/Name",
            "phone": '//Communication[ChannelCode="Phone"]/DialNumber',
            "vatNo": "//RemitToPartyMaster/PartyIDs/TaxID",
            "bank_id": "//RemitToPartyMaster/FinancialParty[last()]/FinancialAccount/ID",
            "status": "//RemitToPartyMaster/Status/Code",
        }
```

### Référence des champs

| Champ DocBits | Source M3 | Description |
|---|---|---|
| `sharedCONO` / `sharedSUNO` | Société M3 / `CIDMAS.IDSUNO` | Même sémantique que sur `SupplierPartyMaster`. Joint la même ligne `supplier_header`. |
| `variationID` | Attribut du BOD | Stocké dans `variation_id_remit_to_party` — suivi indépendamment de la `variationID` SupplierPartyMaster. |
| `supplierName` | `CIDMAS.IDSUNM` | Nom d'affichage de la partie remit-to. Écrit dans la colonne partagée `supplier_name`. |
| `phone` | `CIDREF.IRPHNO` | Numéro de téléphone du bloc communication remit-to. |
| `vatNo` | `CIDMAS.IDCORG` | Identifiant TVA de la partie remit-to. Même limitation `@schemeName` que sur SupplierPartyMaster — la première occurrence l'emporte. <!-- tracked in DOCB-12313 --> |
| `bank_id` | `CBANAC.BCBKNO` | Compte bancaire remit-to (`FinancialParty[last()]`). Même préférence multi-banque s'applique. |
| `status` | `CIDMAS.IDSTAT` | Statut actif/inactif de la partie remit-to. |

## Comment les deux BODs interagissent sur la table `SUPPLIER` partagée

Les deux BODs alimentent la même ligne `supplier_header`. Pour les champs qu'ils partagent (`supplierName`, `phone`, `vatNo`, `bank_id`, `status`), DocBits applique les règles suivantes :

1. Trouver la ligne via `(customer_number = sharedCONO, supplier_number = sharedSUNO)`.
2. Comparer la `variationID` entrante à la `variationID` stockée *pour le même type de BOD*.
3. Si la `variationID` entrante est supérieure (ou `0`, force-update), mettre à jour les champs détenus par ce BOD. Sinon, écarter le BOD.
4. La `variationID` de l'autre type de BOD n'est pas touchée ; ses valeurs précédemment stockées restent en place.

Les lignes `supplier_address` et `supplier_account` associées au fournisseur sont supprimées puis réinsérées lors d'une mise à jour, afin que les tables secondaires reflètent toujours le BOD le plus récent. Cela a un effet de bord lorsque M3 émet un BOD RemitToPartyMaster *par division* (certains tenants le font lorsque des connexions bancaires sont maintenues à la fois sur une division vide et sur des divisions spécifiques) : après que `EXCLUDE_DIVISION_FOR_CUSTOMER_NUMBER` a retiré le suffixe de division, chaque BOD par division vise la même clé `(customer_number, supplier_number)`. Le BOD avec la `variationID` la plus élevée l'emporte. Si ce BOD « gagnant » provient d'une division sans connexions bancaires, les comptes bancaires du BOD précédent sont effacés lors de la réinsertion.

## Questions fréquentes

### Pourquoi DocBits suit-il CONO si tous mes fournisseurs viennent d'une seule société M3 ?

Le routage CONO est obligatoire car DocBits est multi-tenant par conception : une organisation peut ingérer des BODs de plusieurs sociétés M3. CONO fait partie de la clé d'appariement pour que les fournisseurs de sociétés différentes n'entrent pas en collision. Si vous n'avez qu'une société, vous pouvez ignorer la valeur, mais la colonne-clé reste remplie.

### Les deux BODs écrivent sur la même ligne fournisseur — le dernier BOD écrase-t-il tout ?

Non. Chaque type de BOD ne possède que les champs qu'il envoie, et les mises à jour sont contrôlées par une `variationID` indépendante. Un SupplierPartyMaster qui ne change que le nom du fournisseur n'annule pas le numéro de téléphone qu'un RemitToPartyMaster ultérieur aurait écrit.

### `Supplier Categories` et `eam.UDFCHAR06` ne sont jamais émis par mon M3 — que faire ?

Ce sont des extensions UserArea optionnelles. Sans l'extension, les colonnes restent NULL et aucune fonction DocBits n'en dépend. Activez la logique de date d'escompte uniquement quand votre M3 est configuré pour émettre `eam.UDFCHAR06`.

### `vatNo` doit-il filtrer sur `schemeName='TaxIdentificationNumber'` ?

Le chemin d'ingestion BOD M3 lit actuellement `PartyIDs/TaxID` sans filtre `schemeName`. Le filtre est utilisé dans les chemins XSLT e-facture (Facturae, XRechnung, KSeF), pas dans l'ingestion M3. Quand M3 émet plusieurs éléments `TaxID` avec des valeurs `@schemeName` différentes, la première occurrence l'emporte — ce qui peut produire des identifiants TVA incorrects. Un filtre configurable est prévu ; un BOD d'exemple issu de votre tenant nous aide à définir le `schemeName` default correct. <!-- tracked in DOCB-12313 -->

### Que se passe-t-il quand un BOD RemitToPartyMaster est émis par division ?

Certains tenants M3 maintiennent des connexions bancaires à la fois sur une division vide et sur des divisions spécifiques, ce qui amène M3 à émettre un BOD RemitToPartyMaster séparé par division. La clé d'appariement dans DocBits est `(customer_number = sharedCONO, supplier_number = sharedSUNO)` — la division n'en fait pas partie.

- Avec la préférence `EXCLUDE_DIVISION_FOR_CUSTOMER_NUMBER` activée, les BODs par division s'effondrent sur la même ligne. Le BOD avec la `variationID` la plus élevée l'emporte, et les lignes `supplier_account` sont réinsérées uniquement depuis ce BOD. Si le BOD gagnant provient d'une division sans connexions bancaires, les comptes bancaires précédemment stockés sont effacés.
- Avec la préférence désactivée (la CONO conserve son suffixe de division), les BODs par division visent des clés distinctes et coexistent.

Si votre tenant envoie des BODs RemitToPartyMaster par division et dépend de la liste consolidée des banques, contactez-nous avec un exemple afin que nous puissions planifier une amélioration.

### Je veux synchroniser tous les comptes bancaires du fournisseur, pas seulement le dernier. Comment faire ?

Activez la préférence `ALLOW_MULTIPLE_SUPPLIER_ACCOUNTS_SYNC`. Avec le drapeau activé, chaque `FinancialParty` du BOD est persisté dans la table `supplier_account` (IBAN, ID de compte financier, code devise, indicateur de préférence). La colonne héritée `bank_id` sur l'en-tête continue de porter la dernière entrée pour la rétrocompatibilité.
