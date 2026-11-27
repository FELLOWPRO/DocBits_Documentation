# Cas 11a: Quantité hors tolérances (Dépassement positif rejeté), Prix unitaire dans les tolérances

Le scénario suivant illustre un mappage configuré ; il ne constitue pas un modèle par défaut dont le déploiement aurait été vérifié. La sortie réelle, les montants, les signes et les types de documents dépendent des règles et expressions `conflict_resolution` actives, du mappage d’export et des décisions d’approbation. Toute note de débit ou de crédit décrite ci-dessous est soumise à cette configuration ; cet exemple ne garantit ni son émission automatique ni la conformité juridique.

## Scénario :

La quantité sur la facture dépasse la fourchette acceptable (positive) et est rejetée, mais le prix unitaire est dans la tolérance.

## Action :

Le système ajuste la quantité au niveau approuvé, en conservant le prix unitaire, et traite la transaction. Toute quantité excédentaire est rejetée et non facturée.

## Exemple :

* **Purchase Order (PO):**
  * Quantity: 100 units
  * Unit Price: $8.00 per unit
  * Total Amount: $800.00
* **Invoice Received:**
  * Quantity: 110 units — 10% above the PO value, outside the configured ±5% tolerance; rejected.
  * Unit Price: $8.00 per unit (within tolerance)
  * Total Amount: $880.00
* **Tolerance Levels:**
  * Quantity Tolerance: ±5%
  * Unit Price Tolerance: ±2%

Étant donné que la quantité (110 unités) dépasse la limite de tolérance acceptable (écart positif de 10 %) et n'est pas approuvée, mais que le prix unitaire ($8.00) est dans la tolérance, le système :

1. **Reject the Excess Quantity:** Le système rejette la quantité qui dépasse le niveau de tolérance approuvé.
2. **Adjust the Quantity:** Le système ajuste la quantité pour qu'elle corresponde au niveau approuvé spécifié dans le bon de commande.
   * Approved Quantity = 100 units (from PO)
3. **Maintain the Unit Price:** Le prix unitaire de $8.00 par unité est dans les limites de tolérance et reste inchangé.
4. **Recalculate the Total Amount:** Le système calcule le montant total en utilisant la quantité approuvée et le prix unitaire accepté :
   * **Total Amount = Approved Quantity × Unit Price**
   * **Total Amount = 100 units × $8.00 per unit = $800.00**
5. **Process the Invoice:** Le système traite la facture avec le montant total ajusté de $800.00, reflétant uniquement la quantité et le prix unitaire approuvés. La quantité excédentaire de 10 unités est rejetée et non facturée.

Cette approche garantit que le montant facturé correspond aux conditions convenues dans le bon de commande, même lorsque le fournisseur tente de facturer une quantité excédentaire.
