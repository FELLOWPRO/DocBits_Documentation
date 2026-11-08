# Cartes de correspondance de bon de commande - Guide complet

## Cartes de correspondance de bon de commande (PO) - Guide complet

**Statut :** Couvre 15 cartes de comparaison de PO avec des calculs détaillés

***

Les cartes de comparaison de PO de cette page vont dans le groupe **And** du Workflow Builder — elles comparent les données de facture au bon de commande correspondant avant l'exécution des actions Then :

<figure><img src="../../../.gitbook/assets/workflow_designer_cards.png" alt="Canevas du Workflow Builder avec les groupes de cartes When, And et Then"><figcaption><p>Les cartes de comparaison de PO sont ajoutées au groupe <strong>And</strong> via <strong>Add Card</strong>.</p></figcaption></figure>

***

### 📌 Informations sur la version

**Carte la plus évoluée :** CONDITION\_DOC\_TO\_PO\_UNIT\_PRICE (5 versions, v5 la plus récente) **Autres cartes complexes :** CONDITION\_OC\_TO\_PO\_ITEMS (v4), CONDITION\_LESS\_THAN\_TOLERANCE\_AS\_VALUE\_OF\_ORDERED\_QUANTITY (v4)

**Schémas clés :**

* **v2 → v3+:** Ajout de paramètres de tolérance pour une correspondance souple
* **v3 → v4:** Ajout des paramètres de mode de comparaison
* **v4 → v5:** Tolérance améliorée avec plusieurs unités (%, EUR, $, etc.)

📖 [Historique complet des versions](../release.md) | [Versions et comportement des cartes](card-versions-guide.md)

***

### Comprendre la correspondance de PO

Lorsque vous recevez une facture, elle doit correspondre au bon de commande (PO) passé auparavant. Les cartes de correspondance de PO vérifient automatiquement si les données de la facture correspondent à celles du bon de commande.

**Vue d'ensemble :**

```
BC passé      Facture reçue      Rapprochement BC    Décision
(€100)    ➜   (€103)          ➜   (Vérifier si      ➜ Approuver/Rejeter
Qté : 100     Qté : 100           dans la tolérance)
```

<figure><img src="../../../.gitbook/assets/anatomy-po-matching.svg" alt="Balance isométrique à fléau : le plateau de gauche porte le prix unitaire du bon de commande de 100, celui de droite le prix unitaire de la facture de 103 (100 plus un petit poids supplémentaire). Le fléau penche et son aiguille se trouve dans la zone verte qui marque la tolérance de 5 %." width="768"><figcaption><p>Le prix du bon de commande (100 €) se trouve sur le plateau de gauche et le prix de la facture (103 €) sur celui de droite. L'écart de 3 € représente 3 % du prix du bon de commande : l'aiguille reste donc dans la zone verte de tolérance de ±5 % et le contrôle est réussi. Au-delà de ±5 % (en rouge), la facture doit être vérifiée.</p></figcaption></figure>

***

## 1. Correspondance complète du bon de commande

### Objectif

Vérifie si la facture entière correspond parfaitement au bon de commande ou dans les limites de tolérance

### Quand l'utiliser

* Avant d'approuver une facture
* Comme contrôle de qualité préliminaire
* Pour identifier les problèmes suffisamment tôt

### Comment ça fonctionne

Le système compare :

* Quantités facturées vs quantités du bon de commande
* Prix facturés vs prix du bon de commande
* Articles facturés vs articles du bon de commande
* Total de la facture vs total du bon de commande

### Résultat

* **TRUE** (correspondance complète) : tout correspond, continuez
* **FALSE** (écart) : quelque chose ne correspond pas, une vérification est nécessaire

### Exemple

```
BC :
- Article ABC : Qté 100, Prix unitaire €50 = €5000
- Article XYZ : Qté 50, Prix unitaire €20 = €1000
- Total : €6000

Facture :
- Article ABC : Qté 100, Prix unitaire €50 = €5000
- Article XYZ : Qté 50, Prix unitaire €20 = €1000
- Total : €6000

Résultat : ✅ CORRESPONDANCE COMPLÈTE
```

***

## 2. Comparaison des prix unitaires (document vs bon de commande)

### Objectif

Compare le prix unitaire de la facture avec le prix unitaire du bon de commande

### Paramètres

* **Tolérance de prix unitaire** : autoriser un écart jusqu'à ce montant
* **Type de tolérance** : pourcentage (%) ou absolu (€/$)
* **Opérateur** : est égal à, est supérieur à, est inférieur à, etc.

### Comment ça fonctionne (tolérance en pourcentage)

**Formule :**

```
Écart % = |(Prix facture - Prix BC)| / Prix BC × 100

Contrôle : l'écart % est-il ≤ à la tolérance % ?
```

**Exemple pas à pas :**

```
Étape 1 : Récupérer les prix
  Prix unitaire du BC : €100.00
  Prix unitaire de la facture : €103.00

Étape 2 : Calculer la différence
  Différence = |€103.00 - €100.00| = €3.00

Étape 3 : Calculer le pourcentage
  Pourcentage = (€3.00 / €100.00) × 100 = 3%

Étape 4 : Vérifier la tolérance (5 % autorisés)
  3 % ≤ 5 % ? OUI ✅

Résultat : RÉUSSI - dans la tolérance
```

### Exemples concrets

#### Exemple 1 : petite hausse (acceptée)

```
Prix du BC : €50.00
Prix de la facture : €51.50
Tolérance : ±3%

Calcul :
  Écart = |(€51.50 - €50.00)| / €50.00 × 100
  Écart = €1.50 / €50.00 × 100 = 3%

3 % ≤ 3 % ? OUI ✅ ACCEPTER
```

#### Exemple 2 : forte hausse (rejetée)

```
Prix du BC : €50.00
Prix de la facture : €55.00
Tolérance : ±3%

Calcul :
  Écart = |(€55.00 - €50.00)| / €50.00 × 100
  Écart = €5.00 / €50.00 × 100 = 10%

10 % ≤ 3 % ? NON ❌ REJETER - VÉRIFICATION NÉCESSAIRE
```

#### Exemple 3 : remise (également contrôlée)

```
Prix du BC : €100.00
Prix de la facture : €97.00
Tolérance : ±5%

Calcul :
  Écart = |(€97.00 - €100.00)| / €100.00 × 100
  Écart = €3.00 / €100.00 × 100 = 3%

3 % ≤ 5 % ? OUI ✅ ACCEPTER (la remise est dans la tolérance)
```

#### Exemple 4 : tolérance en valeur absolue

```
Prix du BC : €10.00
Prix de la facture : €10.50
Tolérance : ±€1.00 (absolue, pas en %)

Calcul :
  Écart = |€10.50 - €10.00| = €0.50

€0.50 ≤ €1.00 ? OUI ✅ ACCEPTER
```

### Que faire des résultats

**Si RÉUSSI ✅ :**

* Passer au contrôle suivant
* Ou approuver la facture
* Ou poursuivre avec l'export

**Si ÉCHEC ❌ :**

* Signaler pour vérification manuelle
* Demander une explication au fournisseur
* Contacter l'équipe achats
* Approuver avec une note si c'est acceptable

***

## 3. Comparaison des quantités

### Objectif

Vérifie si la quantité commandée correspond à la quantité facturée

### Paramètres

* **Tolérance** : montant ou % d'écart autorisé
* **Opérateur** : égal à, supérieur à, inférieur à
* **Type de quantité** : commandée, reçue, ouverte

### Exemple de calcul

**Tolérance en pourcentage :**

```
Formule :
  Écart de quantité % = |(Qté facture - Qté BC)| / Qté BC × 100

Exemple :
  Quantité du BC : 100 unités
  Quantité facturée : 103 unités
  Tolérance : ±5%

  Écart = |(103 - 100)| / 100 × 100
  Écart = 3 / 100 × 100 = 3%

  3 % ≤ 5 % ? OUI ✅ ACCEPTER
```

**Tolérance absolue :**

```
Formule :
  Écart de quantité = |Qté facture - Qté BC|

Exemple :
  Quantité du BC : 100 unités
  Quantité facturée : 102 unités
  Tolérance : ±5 unités

  Écart = |102 - 100| = 2 unités

  2 unités ≤ 5 unités ? OUI ✅ ACCEPTER
```

### Scénarios concrets

#### Sur-livraison (plus que commandé)

```
Commandé : 100 unités
Facturé : 110 unités
Tolérance : ±5%

Écart = |(110-100)|/100 × 100 = 10%

10 % ≤ 5 % ? NON ❌

Décision : contacter le fournisseur - plus livré que commandé
Raison possible : erreur du fournisseur, livraison partielle déjà reçue
```

#### Sous-livraison (moins que commandé)

```
Commandé : 100 unités
Facturé : 95 unités
Tolérance : ±5%

Écart = |(95-100)|/100 × 100 = 5%

5 % ≤ 5 % ? OUI ✅

Décision : accepter - dans la tolérance
Raison possible : livraison partielle, le reste suit
```

***

## 4. Prix combiné de l'écart de quantité

### Objectif

Lorsque la quantité diffère, calcule si l'écart de prix total est acceptable

### Pourquoi c'est important

```
Scénario : vous avez commandé 100 unités mais vous en avez reçu 110
- La quantité dépasse de 10 % (défavorable)
- MAIS : seuls 10 % supplémentaires vous sont facturés
- L'effet combiné peut être acceptable
```

### Calcul

**Formule :**

```
Écart combiné = Écart de quantité × Écart de prix

Si les deux sont dans la tolérance, l'écart combiné est généralement acceptable
```

**Exemple :**

```
BC :
- Prix unitaire : €100
- Quantité : 100
- Total : €10,000

Facture :
- Prix unitaire : €102 (2 % de plus)
- Quantité : 105 (5 % de plus)
- Total : €10,710

Analyse :
- Écart de prix : 2 % ✅
- Écart de quantité : 5 % ✅
- Effet combiné : 1.02 × 1.05 = 1.071 = 7.1 % de hausse totale

L'écart combiné est-il acceptable ? Généralement OUI ✅
```

***

## 5. Comparaison de l'ID article / du numéro d'article fournisseur

### Objectif

Vérifie si les articles de la facture correspondent aux articles du bon de commande

### Comment ça fonctionne

**Correspondance exacte (la plus simple) :**

```
ID article du BC : ABC-123
ID article de la facture : ABC-123
Résultat : ✅ CORRESPONDANCE
```

**Numéro d'article fournisseur (plus courant) :**

```
Article du BC : ABC-123 (notre code interne)
Article fournisseur : SUPP-456 (leur code pour le même article)
Le système les associe au même article
Résultat : ✅ CORRESPONDANCE
```

### Scénario : et si cela ne correspond pas ?

```
Article du BC : ABC-123 (fil de cuivre, 2 mm)
Article de la facture : ABC-124 (fil d'acier, 2 mm)

Résultat : ❌ AUCUNE CORRESPONDANCE

Actions :
1. S'agit-il d'une substitution ? Vérifiez avec les achats
2. S'agit-il d'une erreur ? Contactez le fournisseur
3. La description est-elle similaire ? Vérifiez manuellement
```

***

## 6. Vérification du type de commande

### Objectif

Vérifie que le type de bon de commande est correct

### Types de commande

* **Standard Order** : achat courant
* **Rush Order** : urgent, peut comporter une majoration
* **Frame Agreement** : contrat à long terme
* **Blanket Order** : contrat sans échéance
* **Consignment** : paiement seulement à l'utilisation

### Exemple de contrôle

```
Type de commande du BC : Standard Order
Type de commande de la facture : Standard Order
Résultat : ✅ CORRESPONDANCE

En cas d'écart : les conditions, le paiement et les prix peuvent changer
```

***

## 7. Vérification de la date de livraison

### Objectif

Vérifie si la date de livraison correspond à la date promise sur le bon de commande

### Calcul

**Livraison en retard :**

```
Formule :
  Jours de retard = Date de livraison facture - Date promise du BC

Exemple :
  Date promise du BC : 2025-10-15
  Livraison réelle : 2025-10-22
  Jours de retard = 7 jours

Si la tolérance est de ±3 jours :
  7 ≤ 3 ? NON ❌ EN RETARD
```

**Livraison en avance :**

```
Formule :
  Jours d'avance = Date promise du BC - Date de livraison facture

Exemple :
  Date promise du BC : 2025-10-15
  Livraison réelle : 2025-10-10
  Jours d'avance = 5 jours

Une livraison en avance est généralement acceptable ✅
Sauf si vous en avez besoin à un moment précis
```

### Paramètres de tolérance

```
±3 jours : autoriser 3 jours de retard ou d'avance
±5 jours : autoriser jusqu'à 5 jours d'écart
0 jour : correspondance exacte obligatoire
```

***

## 8. Vérification des frais (taxes, transport, etc.)

### Objectif

Vérifie si les frais supplémentaires (taxes, transport, manutention) correspondent au bon de commande

### Frais courants

```
- Transport : €50
- Manutention : €10
- Emballage : €5
- Assurance : €15
- Taxes : €300
```

### Calcul

**Exemple : contrôle des frais de transport**

```
Transport du BC : €50.00
Transport de la facture : €51.00
Tolérance : ±3%

Écart = |€51.00 - €50.00| / €50.00 × 100 = 2%

2 % ≤ 3 % ? OUI ✅ ACCEPTER
```

**Exemple : plusieurs frais**

```
Total des frais du BC :
  - Transport : €50
  - Taxes : €300
  - Manutention : €10
  Total : €360

Total des frais de la facture :
  - Transport : €50
  - Taxes : €312 (taxe de 11 %)
  - Manutention : €10
  Total : €372

Différence : €12
Vérifiez si c'est dans la tolérance ✅ ou ❌
```

***

## 9. Vérification des taxes

### Objectif

Vérifie que les montants de taxe sont correctement calculés

### Calcul

**Formule :**

```
Montant de taxe = Sous-total × Taux de taxe

Exemple :
  Sous-total : €1000
  Taux de taxe : 19 %
  Taxe attendue : €1000 × 0.19 = €190

Taxe de la facture : €190
Correspondance ? OUI ✅
```

**Problèmes courants :**

```
1. Taux de taxe modifié (selon la région)
2. Taxe appliquée au mauvais montant (avant/après remises)
3. Plusieurs taux de taxe (certains articles à 7 %, d'autres à 19 %)
4. Articles exonérés (taxe de 0 %)
```

**Exemple : taxation à plusieurs taux**

```
Article A : €100 @ 19 % de taxe = €119
Article B : €100 @ 7 % de taxe = €107
Article C : €100 @ 0 % de taxe = €100
Total : €326

La facture indique €325 (erreur de €1)

Contrôle : dans la tolérance ou à examiner ?
```

***

## 10. Correspondance site/centre de coûts

### Objectif

Garantit que la facture concerne le bon site ou le bon centre de coûts

### Exemple

```
Le BC concerne :
- Site : Berlin Plant
- Centre de coûts : CC-2025

La facture doit indiquer :
- Site : Berlin Plant ✅
- Centre de coûts : CC-2025 ✅

Si le site diffère : une autre approbation peut être nécessaire
```

***

## 11. Validation du statut fournisseur

### Objectif

Vérifie si le fournisseur est toujours approuvé ou actif

### Types de statut

```
✅ ACTIVE : approuvé, peut être utilisé
⚠️ ON HOLD : bloqué temporairement
❌ INACTIVE : plus d'activité commerciale
⚠️ CONDITIONAL : uniquement pour certains articles
```

### Exemple de contrôle

```
Fournisseur : ABC Corp
Statut dans la base : ACTIVE
Statut à la création du BC : ACTIVE
Statut à l'arrivée de la facture : INACTIVE

Alerte : le statut du fournisseur a changé ! Analysez pourquoi.
```

***

## Quelle tolérance utiliser ?

### Tolérances strictes (risque plus faible, travail manuel plus important)

```
À utiliser pour :
- Articles de forte valeur
- Articles dont l'exactitude est critique
- Secteurs réglementés

Paramètres :
- Prix unitaire : ±1 %
- Quantité : ±1 %
- Date de livraison : ±1 jour
- Frais : ±1 %
```

### Tolérances modérées (équilibrées)

```
À utiliser pour :
- La plupart des transactions commerciales
- Articles standard
- Achats courants

Paramètres :
- Prix unitaire : ±3-5 %
- Quantité : ±3-5 %
- Date de livraison : ±3 jours
- Frais : ±5 %
```

### Tolérances larges (risque plus élevé, moins de travail manuel)

```
À utiliser pour :
- Articles de faible valeur
- Achats en gros
- Accords fournisseurs offrant de la souplesse

Paramètres :
- Prix unitaire : ±10 %
- Quantité : ±10 %
- Date de livraison : ±7 jours
- Frais : ±10 %
```

***

## Exemple de workflow de correspondance de PO

```
La facture arrive
    ↓
Condition : « Le montant est-il > €5000 ? » ➜ OUI
    ↓
Contrôle : correspondance complète ? ➜ NON (écart de prix de 10 %)
    ↓
Contrôle : prix unitaire dans 5 % ? ➜ NON (écart de 12 %)
    ↓
Contrôle : quantité dans 5 % ? ➜ OUI (écart de 2 %)
    ↓
Décision : ÉCHEC - écart de prix trop important
    ↓
Signaler pour : vérification manuelle / approbation de l'acheteur
    ↓
Attendre : le commentaire de l'acheteur
    ↓
Si approuvé : poursuivre avec l'export
Si rejeté : renvoyer au fournisseur
```

***

## Dépannage de la correspondance de PO

### « PO introuvable »

```
Cause : le numéro de PO de la facture n'existe pas dans le système
Correction :
1. Vérifiez l'orthographe du numéro de PO
2. Vérifiez si le PO a été créé
3. Vérifiez que le PO se trouve dans la bonne organisation
4. Demandez la référence du PO au fournisseur
```

### « Les articles ne correspondent pas »

```
Cause : les articles de la facture diffèrent de ceux du BC
Raisons possibles :
1. Substitution approuvée par les achats
2. Numéros d'article différents pour le même article
3. Erreur du fournisseur
Correction : contactez les achats ou le fournisseur
```

### « Prix supérieur à celui du PO »

```
Cause : prix de la facture > prix du BC
Raisons possibles :
1. Hausse de prix approuvée
2. Erreur du fournisseur
3. Différence de devise
4. Prestations supplémentaires incluses
Correction : vérifiez avec les achats
```

### « Date de livraison erronée »

```
Cause : facture datée après la livraison promise
Raisons possibles :
1. L'expédition a été retardée
2. Date de réception différente de la date de facture
3. Livraison partielle
Correction : consultez les documents d'expédition ou contactez le fournisseur
```

***

## Tableau récapitulatif

| Carte           | Ce qu'elle vérifie    | Calcul principal     | Tolérance courante |
| -------------- | --------------------- | -------------------- | ---------------- |
| Correspondance complète     | Tout            | Tous les contrôles           | Variable           |
| Prix unitaire     | Prix par unité        | Écart en % ou en €    | ±3-5%            |
| Quantité       | Quantité commandée        | Écart en % ou en unités | ±3-5%            |
| Prix combiné | Total avec variation de quantité | Qté × Prix          | ±5-10%           |
| ID article        | Bons articles           | Correspondance de chaîne         | Exacte            |
| Type de commande     | Type d'achat      | Correspondance de chaîne         | Exacte            |
| Date de livraison  | Date d'arrivée          | Écart en jours       | ±3 jours          |
| Frais        | Frais supplémentaires            | Écart en % ou en €    | ±5%              |
| Taxe            | Montant de taxe            | Calcul du % de taxe    | ±1%              |
| Site       | Centre de coûts           | Correspondance de chaîne         | Exacte            |
| Fournisseur       | Approuvé ?             | Contrôle de statut         | Actifs uniquement      |

***

## Documentation associée

* Voir le guide « Validation des factures » pour le workflow complet
* Voir « Paramètres de tolérance » pour les valeurs recommandées par secteur
* Voir « Gestion des exceptions » pour ce qu'il faut faire en cas d'échec
* Contactez votre équipe achats pour les politiques de tolérance spécifiques

<!-- workflow-card-example-condition_promised_delivery_date_to_current-20261021 -->

### Date de livraison promise par rapport à la date de référence

<figure><img src="../../../.gitbook/assets/workflow-card-qa-20261021-card-extra-ca4dcfa998e7-fr.png" alt="Champs de la carte dans la version affichée. Les espaces réservés ne sont pas configurés." width="563"><figcaption><p>Champs de la carte dans la version affichée. Les espaces réservés ne sont pas configurés.</p></figcaption></figure>

`CONDITION_PROMISED_DELIVERY_DATE_TO_CURRENT` · version 2

Supposons une date de référence `2026-10-21` et une date de livraison promise de ligne `2026-10-23`. Sélectionnez la comparaison « postérieur à » et une tolérance de zéro jour. La date future satisfait cette comparaison ; `2026-10-20` non. Configurez délibérément les options Any/All et les jours de tolérance acceptés, et testez séparément une date manquante.

<!-- workflow-card-example-condition_po_extracted_table_column-20261021 -->

### Colonne de bon de commande comparée à une colonne extraite

<figure><img src="../../../.gitbook/assets/workflow-card-qa-20261021-card-extra-e2c12dd67cc0-fr.png" alt="Champs de la carte dans la version affichée. Les espaces réservés ne sont pas configurés." width="563"><figcaption><p>Champs de la carte dans la version affichée. Les espaces réservés ne sont pas configurés.</p></figcaption></figure>

`CONDITION_PO_EXTRACTED_TABLE_COLUMN` · version 2

Comparez la colonne d'article du PO correspondant avec la colonne extraite `article_number`, en utilisant l'égalité et All. Des valeurs correspondantes `DEMO-A` passent ; une valeur extraite `DEMO-B` échoue. Sélectionnez une table de correspondance uniquement lorsqu'un remplacement documenté d'un identifiant par une valeur est nécessaire ; vérifiez ce mappage avant de comparer.

<!-- workflow-card-example-condition_check_facility_in_po-20261021 -->

### Sites de bon de commande autorisés

<figure><img src="../../../.gitbook/assets/workflow-card-qa-20261021-card-extra-813ff783b1f2-fr.png" alt="Champs de la carte dans la version affichée. Les espaces réservés ne sont pas configurés." width="563"><figcaption><p>Champs de la carte dans la version affichée. Les espaces réservés ne sont pas configurés.</p></figcaption></figure>

`CONDITION_CHECK_FACILITY_IN_PO` · version 2

Sélectionnez All, la comparaison « est dans » et le code de site configuré `DEMO-NORTH`. Les lignes de PO correspondantes de ce site passent ; une ligne de `DEMO-SOUTH` échoue. Utilisez les codes de site issus des données du PO plutôt que de supposer qu'un libellé d'affichage est son code.

<!-- workflow-card-example-condition_purchase_order_full_match-20261021 -->

### Correspondance complète du bon de commande

<figure><img src="../../../.gitbook/assets/workflow-card-qa-20261021-card-extra-91a5b2a70e88-fr.png" alt="Champs de la carte dans la version affichée. Les espaces réservés ne sont pas configurés." width="563"><figcaption><p>Champs de la carte dans la version affichée. Les espaces réservés ne sont pas configurés.</p></figcaption></figure>

`CONDITION_PURCHASE_ORDER_FULL_MATCH` · version 2

Utilisez une facture et un PO de démonstration entièrement correspondants, avec une quantité `2` et un prix unitaire `100` des deux côtés, et des tolérances de quantité et de prix configurées. Sélectionnez la condition de correspondance complète : elle passe. Testez ensuite un prix hors de la tolérance configurée. Des données de comparaison manquantes ou un PO absent ne constituent pas une correspondance complète réussie. Un bon de livraison a une comparaison de quantité uniquement ; ne supposez pas que les règles de prix de facture s'y appliquent.

<!-- workflow-card-example-condition_po_update_empty_column_check-20261021 -->

### Colonne de base de données de PO vide

<figure><img src="../../../.gitbook/assets/workflow-card-qa-20261021-card-extra-f20345d72edd-fr.png" alt="Champs de la carte dans la version affichée. Les espaces réservés ne sont pas configurés." width="563"><figcaption><p>Champs de la carte dans la version affichée. Les espaces réservés ne sont pas configurés.</p></figcaption></figure>

`CONDITION_PO_UPDATE_EMPTY_COLUMN_CHECK` · version 2

Sélectionnez une table et une colonne de PO valides proposées par la carte, ainsi que l'opérateur « est vide ». Pour un enregistrement de PO correspondant existant avec une valeur vide, la condition passe ; une valeur renseignée échoue. Vérifiez d'abord la référence de PO et le mappage table/colonne. Le booléen `false` reste une valeur booléenne présente ; un enregistrement de PO manquant est une erreur de données distincte.

<!-- workflow-card-example-condition_compare_unit_price_percent_per-20261021 -->

### Tolérance en pourcentage par base de prix

<figure><img src="../../../.gitbook/assets/workflow-card-qa-20261021-card-extra-14ec95131dfc-fr.png" alt="Champs de la carte dans la version affichée. Les espaces réservés ne sont pas configurés." width="563"><figcaption><p>Champs de la carte dans la version affichée. Les espaces réservés ne sont pas configurés.</p></figcaption></figure>

`CONDITION_COMPARE_UNIT_PRICE_PERCENT_PER` · version 2

Exemple : un prix unitaire de PO de `200`, un prix de base de `100` et une tolérance configurée de `1` produisent un taux effectif de `(200 / 100) * (1 / 100) = 0.02`, soit `2%`. La bande de comparaison est `196–204`. L'égalité dans la tolérance accepte un prix de document de `203` et rejette `210`. Ne supposez pas que cette carte équivaut à une tolérance fixe de 1 %.

<!-- workflow-card-example-condition_compare_po_line_value-20261021 -->

### Valeur de ligne de bon de commande par rapport à une référence

<figure><img src="../../../.gitbook/assets/workflow-card-qa-20261021-card-extra-43a5d2686fb7-fr.png" alt="Champs de la carte dans la version affichée. Les espaces réservés ne sont pas configurés." width="563"><figcaption><p>Champs de la carte dans la version affichée. Les espaces réservés ne sont pas configurés.</p></figcaption></figure>

`CONDITION_COMPARE_PO_LINE_VALUE` · version 2

Sélectionnez la colonne de PO correspondante `item_number`, l'égalité et la valeur `DEMO-A`. Une ligne avec `DEMO-A` passe ; `DEMO-B` échoue. Utilisez uniquement les opérateurs pris en charge pour le type de données sélectionné, et testez séparément l'absence de données de ligne correspondantes.
