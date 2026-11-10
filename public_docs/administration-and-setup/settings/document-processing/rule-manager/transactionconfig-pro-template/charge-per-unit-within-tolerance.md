# Frais par unité dans les tolérances

Le scénario suivant illustre un mappage configuré ; il ne constitue pas un modèle par défaut dont le déploiement aurait été vérifié. La sortie réelle, les montants, les signes et les types de documents dépendent des règles et expressions `conflict_resolution` actives, du mappage d’export et des décisions d’approbation. Toute note de débit ou de crédit décrite ci-dessous est soumise à cette configuration ; cet exemple ne garantit ni son émission automatique ni la conformité juridique.

## Scénario :

Le Charge Per Unit indiqué sur la facture se situe dans la plage de tolérance acceptable par rapport au bon de commande.

## Action :

Le système accepte le Charge Per Unit tel que facturé et traite la transaction sans ajustements.

## Exemple :

* **Purchase Order (PO):**
  * Charge Per Unit: $5.00
  * Quantity: 500 units
  * Total Charge Amount: $2,500.00
* **Invoice Received:**
  * Charge Per Unit: $5.10 (variance 2%, within the ±3% tolerance)
  * Quantity: 500 units
  * Total Charge Amount: $2,550.00
* **Tolerance Levels:**
  * Charge Per Unit Tolerance: ±3%

Étant donné que le Charge Per Unit ($5.10) se situe dans la plage de tolérance acceptable de 3 % par rapport au bon de commande, le système :

1. **Accept the Charge Per Unit:** Le système accepte le Charge Per Unit facturé de $5.10 car il se situe dans la limite de tolérance définie.
2. **Process the Transaction:** Le système traite la facture avec le Total Charge Amount en fonction du Charge Per Unit facturé et de la Quantity :
   * **Total Charge Amount = Quantity × Charge Per Unit**
   * **Total Charge Amount = 500 units × $5.10 = $2,550.00**
3. **Finalize the Invoice:** Le système traite la transaction sans aucun ajustement, acceptant la facture telle quelle.

Cette approche permet au système de s'adapter à des écarts mineurs acceptables dans les frais, garantissant ainsi un traitement fluide et efficace des transactions sans rejets ni retards inutiles.
