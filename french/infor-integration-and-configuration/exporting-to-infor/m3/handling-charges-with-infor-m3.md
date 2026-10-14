# Gestion des frais avec Infor M3

## Aperçu

Ce document fournit des informations détaillées sur la manière dont DocBits s'intègre à Infor M3 pour gérer les frais associés aux factures et aux bons de commande (PO). Il inclut des scénarios de frais externes et les solutions attendues.

## Scénarios de gestion des frais

| ID du scénario | Description                                                                          | Cas métier                                                                                                                             | Solution attendue                                                                                                                                                                                                                         |
| -------------- | ------------------------------------------------------------------------------------ | -------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| 1              | Frais externes absents du PO mais présents sur la facture (acceptés)                 | Des frais externes figurent sur la facture mais ne sont pas indiqués sur le PO. Ces frais sont acceptés.                               | Les frais seront comptabilisés selon la règle comptable PP20-228, sur la base de l'élément de coût envoyé par DocBits.                                                                                                                    |
| 2              | Frais externes absents du PO mais présents sur la facture (non acceptés)             | Des frais externes figurent sur la facture mais ne sont pas indiqués sur le PO. Ces frais ne sont ni acceptés ni approuvés.            | La valeur totale de la facture est enregistrée avec des frais d'en-tête pour les frais non approuvés. Une note de débit est en outre créée pour ces frais.                                                                               |
| 3              | Frais externes de la facture supérieurs ou inférieurs à ceux du PO (dans la tolérance) | Les frais externes de la facture sont supérieurs ou inférieurs à ceux du PO, mais restent dans la tolérance acceptée.                | Les frais supplémentaires sont comptabilisés selon la règle comptable PP20-228, sur la base de l'élément de coût envoyé par DocBits.                                                                                                      |
| 4              | Frais externes de la facture supérieurs à ceux du PO (hors tolérance, non approuvés) | Les frais externes de la facture sont supérieurs à ceux du PO et dépassent la tolérance acceptée, et ils ne sont pas approuvés.        | La facture est enregistrée avec le montant total de la facture. Des frais non approuvés supplémentaires sont ajoutés en tant que frais d'en-tête, et une note de débit est créée pour ces frais supplémentaires.                         |
| 5              | Frais externes de la facture supérieurs à ceux du PO (hors tolérance, approuvés dans DocBits) | Les frais externes de la facture sont supérieurs à ceux du PO et dépassent la tolérance acceptée, et ils sont approuvés dans DocBits. | Les frais supplémentaires sont comptabilisés sur PP20-228. Deux options sont envisagées :\<br>- Si la tolérance APS900 > DocBits, les frais supplémentaires sont comptabilisés automatiquement.\<br>- Si la tolérance APS900 = DocBits, les frais supplémentaires sont comptabilisés avec de nouveaux éléments de frais absents du PO. |
| 6              | Frais externes de la facture inférieurs à ceux du PO (hors tolérance, non approuvés) | Les frais externes de la facture sont inférieurs à ceux du PO et dépassent la tolérance acceptée, et ils ne sont pas approuvés.        | La facture est comptabilisée comme non approuvée dans APS110. L'équipe comptabilité fournisseurs ajuste les frais via l'option Invoice Control dans APS110, qui appelle APS360.                                                          |
| 7              | Frais externes sur le PO et aucun frais sur la facture                               | Des frais externes sont indiqués sur le PO, mais la facture ne comporte aucun frais.                                                   | La facture est comptabilisée comme non approuvée dans APS110. L'équipe comptabilité fournisseurs ajuste les frais via l'option Invoice Control dans APS110, qui appelle APS360.                                                          |

## Exemple pour le scénario 5

| Champ          | Valeur du PO | Valeur de la facture fournisseur |
| -------------- | ------------ | -------------------------------- |
| Ligne 1        | 6000 $       | 6000 $                           |
| Fret (E001)    | 1000 $       | 3000 $                           |
| **Total**      | 7000 $       | 9000 $                           |

**Tolérance du fret :** 100 $ approuvés automatiquement dans M3 (APS900) et dans DocBits. Valeur totale de facture de 9000 $ approuvée manuellement (frais inclus).

**APS451 (ligne de facture) :**

* Line Type 1 (ligne de facture) : 9000 $
* Line Type 5 (frais de ligne) : 1000 $ (élément : E001 pour le fret sur le PO, 1000 $)
* Line Type 5 (frais de ligne) : 2000 $ (élément : E101 pour le fret sur le PO, 0 $)

### Champs et valeurs importants pour la gestion des frais dans DocBits

| Champ                       | Description                                                          |
| --------------------------- | -------------------------------------------------------------------- |
| Sequence Number             | Identifiant unique de chaque scénario de frais                       |
| Costing Element ID          | Identifiant de l'élément de coût                                     |
| Costing Element Description | Description de l'élément de coût                                     |
| Charge Type                 | Généralement « External »                                            |
| Charge Invoicing            | Pertinence à déterminer                                              |
| Distribution Method         | Méthode utilisée pour répartir les frais                             |
| Gross Weight                | Applicable si le poids brut figure sur la facture                    |
| Volume                      | Cas d'application à définir                                          |
| Net Amount                  | Cas d'application à définir                                          |
| 3rd Party Charge            | Présence sur la facture et exigences de traitement                   |
| Invoice Charge Quantity     | Clarification nécessaire                                             |
| Markup                      | Supposé correspondre à la différence entre les frais et la remise    |
| Charge Category             | Pertinence à définir                                                 |
| Costing Operator            | Pertinence à définir                                                 |

\

