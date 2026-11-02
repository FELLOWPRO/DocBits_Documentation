# Cas 15 : Frais de ligne par unité hors tolérance (rejetés)

Le scénario suivant illustre un mappage configuré ; il ne constitue pas un modèle par défaut dont le déploiement aurait été vérifié. La sortie réelle, les montants, les signes et les types de documents dépendent des règles et expressions `conflict_resolution` actives, du mappage d’export et des décisions d’approbation. Toute note de débit ou de crédit décrite ci-dessous est soumise à cette configuration ; cet exemple ne garantit ni son émission automatique ni la conformité juridique.

## Scénario

Les frais par unité d’une ligne dépassent la tolérance et l’écart n’a pas été approuvé. Ce cas concerne des frais de ligne, pas des frais d’en-tête.

## Action illustrative

Un mappage configuré pour retenir les frais du PO après rejet remplacerait les frais unitaires facturés par ceux du PO. Tout ajustement distinct ou toute note de débit ou de crédit dépend du mappage d’export et des décisions d’approbation.

## Exemple

* **Commande d’achat (PO) :**
  * Frais de ligne par unité : $4.00
  * Quantité : 1,500 unités
  * Total des frais de ligne : $6,000.00
* **Facture reçue :**
  * Frais de ligne par unité : $5.00 — soit 25% au-dessus du PO, hors de la tolérance configurée de ±5% ; rejetés.
  * Quantité : 1,500 unités
  * Total des frais de ligne : $7,500.00
* **Tolérance configurée :** Frais par unité ±5%.

Dans ce mappage illustratif :

1. Rejeter les frais facturés de $5.00 par unité, car l’écart de 25% dépasse ±5% et n’a pas été approuvé.
2. Retenir les frais du PO de $4.00 par unité.
3. Recalculer le total des frais de ligne : **1,500 unités × $4.00 = $6,000.00**.
4. Calculer l’excédent facturé : **$7,500.00 - $6,000.00 = $1,500.00**.
5. Appliquer le traitement configuré de cet écart. Une note de crédit de $1,500.00 constitue un résultat possible du mappage, pas une action garantie du système. Son montant, son signe, son type de document et son émission dépendent des règles actives, du mappage d’export et des approbations.

Validez le mappage des frais de ligne et les documents comptables produits avant d’utiliser ce scénario en production.
