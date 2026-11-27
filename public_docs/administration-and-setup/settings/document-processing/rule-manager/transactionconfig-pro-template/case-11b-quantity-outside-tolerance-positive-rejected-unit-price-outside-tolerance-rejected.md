# Cas 11b: Quantité excédentaire rejetée et prix unitaire hors tolérance rejeté

Le scénario suivant illustre un mappage configuré ; il ne constitue pas un modèle par défaut dont le déploiement aurait été vérifié. La sortie réelle, les montants, les signes et les types de documents dépendent des règles et expressions `conflict_resolution` actives, du mappage d’export et des décisions d’approbation. Toute note de débit ou de crédit décrite ci-dessous est soumise à cette configuration ; cet exemple ne garantit ni son émission automatique ni la conformité juridique.

## Scénario :

La quantité dépasse la plage acceptable (positive) et est rejetée, et le prix unitaire est également hors tolérance et rejeté.

## Action :

Le système ajuste la quantité et le prix unitaire pour qu'ils correspondent aux niveaux approuvés du bon de commande, rejetant tout excédent, et traite la transaction.

## Exemple :

* **Purchase Order (PO):**
  * Quantity: 200 units
  * Unit Price: $50.00 per unit
  * Total Amount: $10,000.00
* **Invoice Received:**
  * Quantity: 220 units — 10% above the PO value, outside the configured ±5% tolerance; rejected.
  * Unit Price: $55.00 per unit — 10% above the PO value, outside the configured ±2% tolerance; rejected.
  * Total Amount: $12,100.00
* **Tolerance Levels:**
  * Quantity Tolerance: ±5%
  * Unit Price Tolerance: ±2%

Étant donné que la quantité (220 unités) et le prix unitaire ($55.00) dépassent les limites de tolérance acceptables et qu'aucun des deux n'a été approuvé, le système :

1. **Reject the Excess Quantity:** Le système n'accepte pas la quantité facturée de 220 unités et l'ajuste pour qu'elle corresponde au bon de commande d'origine.
   * Adjusted Quantity = 200 units (from PO)
2. **Reject the Invoice Unit Price:** Le système n'accepte pas le prix unitaire facturé de $55.00 et l'ajuste pour qu'il corresponde au bon de commande d'origine.
   * Adjusted Unit Price = $50.00 per unit (from PO)
3. **Recalculate the Total Amount:** Le système calcule le montant total en utilisant la quantité ajustée et le prix unitaire :
   * **Corrected Total Amount = Adjusted Quantity × Adjusted Unit Price**
   * **Corrected Total Amount = 200 units × $50.00 per unit = $10,000.00**
4. **Process the Invoice:** Le système traite la facture pour un montant total corrigé de $10,000.00, en rejetant la quantité excédentaire et le prix unitaire supérieur.

Cette approche garantit que la transaction est conforme aux conditions initiales du bon de commande, en maintenant des contrôles cohérents en matière de prix et de quantité tout en rejetant les écarts non approuvés.
