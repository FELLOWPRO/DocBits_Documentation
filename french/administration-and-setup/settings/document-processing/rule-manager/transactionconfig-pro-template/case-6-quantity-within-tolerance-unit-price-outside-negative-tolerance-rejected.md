# Cas 6 : Quantité dans la tolérance, prix inférieur à la limite (rejeté)

Le scénario suivant illustre un mappage configuré ; il ne constitue pas un modèle par défaut dont le déploiement aurait été vérifié. La sortie réelle, les montants, les signes et les types de documents dépendent des règles et expressions `conflict_resolution` actives, du mappage d’export et des décisions d’approbation. Toute note de débit ou de crédit décrite ci-dessous est soumise à cette configuration ; cet exemple ne garantit ni son émission automatique ni la conformité juridique.

## Scénario

La quantité respecte la tolérance, mais le prix unitaire facturé est inférieur à la plage autorisée et l’écart de prix n’a pas été approuvé.

## Action illustrative

Un mappage configuré pour retenir le prix du PO après rejet conserverait la quantité et remplacerait le prix unitaire facturé par celui du PO. La production d’un ajustement, d’une note de débit, d’une note de crédit ou d’aucun document distinct dépend du mappage actif et des décisions d’approbation. Des frais d’en-tête supplémentaires ne s’appliquent que s’ils sont explicitement configurés.

## Exemple

* **Commande d’achat (PO) :**
  * Quantité : 100 unités
  * Prix unitaire : $10.00 par unité
  * Total : $1,000.00
* **Facture reçue :**
  * Quantité : 100 unités — écart réel de 0%, dans la tolérance configurée de ±2%.
  * Prix unitaire : $9.00 — écart réel de -10%, hors de la tolérance configurée de ±1% ; rejeté.
  * Total : $900.00
* **Tolérances configurées :**
  * Quantité : ±2%
  * Prix unitaire : ±1%

Dans ce mappage illustratif :

1. Rejeter le prix unitaire facturé de $9.00, car l’écart dépasse la tolérance et n’a pas été approuvé.
2. Retenir le prix unitaire du PO de $10.00.
3. Recalculer le total de l’exemple : **100 unités × $10.00 = $1,000.00**.
4. Calculer l’écart signé comme le total facturé moins le total recalculé : **$900.00 - $1,000.00 = -$100.00**.
5. Appliquer le mappage d’export et la décision d’approbation configurés. La valeur -$100.00 est un écart signé, et non une instruction inconditionnelle d’émettre une note de crédit. Le mappage détermine le montant, le signe et le type de document de tout ajustement.

Cet exemple ne signifie pas qu’une note de crédit annule automatiquement une sous-facturation. Vérifiez le traitement comptable attendu dans le mappage d’export actif avant d’utiliser la règle.
