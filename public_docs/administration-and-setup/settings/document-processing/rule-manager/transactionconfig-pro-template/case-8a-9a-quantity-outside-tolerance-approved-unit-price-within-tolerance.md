# Cas 8a, 9a: Quantité hors tolérances (Approuvé), Prix unitaire dans les tolérances

Le scénario suivant illustre un mappage configuré ; il ne constitue pas un modèle par défaut dont le déploiement aurait été vérifié. La sortie réelle, les montants, les signes et les types de documents dépendent des règles et expressions `conflict_resolution` actives, du mappage d’export et des décisions d’approbation. Toute note de débit ou de crédit décrite ci-dessous est soumise à cette configuration ; cet exemple ne garantit ni son émission automatique ni la conformité juridique.

## Scénario :

La quantité sur la facture est en dehors de la tolérance acceptable mais a été approuvée, tandis que le prix unitaire reste dans la tolérance.

## Action :

Le système accepte la quantité approuvée et le prix unitaire selon la facture et traite la transaction en conséquence.

## Exemple :

* **Purchase Order (PO):**
  * Quantity: 150 units
  * Unit Price: $12.00 per unit
  * Total Amount: $1,800.00
* **Invoice Received:**
  * Quantity: 160 units — 6.67% above the PO value, outside the configured ±5% tolerance; approved.
  * Unit Price: $12.00 per unit (within tolerance)
  * Total Amount: $1,920.00
* **Tolerance Levels:**
  * Quantity Tolerance: ±5%
  * Unit Price Tolerance: ±2%

Étant donné que la quantité (160 unités) dépasse la limite de tolérance acceptable mais a été approuvée et que le prix unitaire ($12.00) se situe dans la fourchette acceptable, le système :

1. **Accept the Approved Quantity:** Le système reconnaît que la quantité a été approuvée même si elle est en dehors de la plage de tolérance normale.
2. **Accept the Unit Price:** Le prix unitaire de $12.00 par unité se situe dans la tolérance acceptable, il est donc accepté tel que facturé.
3. **Process the Transaction:** Le système calcule le montant total en utilisant la quantité approuvée et le prix unitaire :
   * **Total Amount = Quantity × Unit Price**
   * **Total Amount = 160 units × $12.00 per unit = $1,920.00**
4. **Finalize the Invoice:** Le système traite la facture pour un montant total de $1,920.00, correspondant à la quantité approuvée et au prix unitaire accepté.

Cette approche permet au système de prendre en compte les écarts de quantité approuvés tout en garantissant que le prix unitaire reste dans la fourchette prévue, facilitant ainsi le traitement fluide des transactions.
