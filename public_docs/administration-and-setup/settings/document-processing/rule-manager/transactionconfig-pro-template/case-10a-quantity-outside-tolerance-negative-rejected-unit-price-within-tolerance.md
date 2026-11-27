# Cas 10a: Quantité hors tolérances (Dépassement négatif rejeté), Prix unitaire dans les tolérances

Le scénario suivant illustre un mappage configuré ; il ne constitue pas un modèle par défaut dont le déploiement aurait été vérifié. La sortie réelle, les montants, les signes et les types de documents dépendent des règles et expressions `conflict_resolution` actives, du mappage d’export et des décisions d’approbation. Toute note de débit ou de crédit décrite ci-dessous est soumise à cette configuration ; cet exemple ne garantit ni son émission automatique ni la conformité juridique.

## Scénario :

La quantité est inférieure à la fourchette acceptable (tolérance négative) et n'est pas approuvée, bien que le prix unitaire soit dans la tolérance.

## Action :

Le système ajuste la quantité pour qu'elle corresponde au niveau approuvé, gardant ainsi le prix unitaire cohérent. La transaction est traitée en conséquence.

## Exemple :

* **Purchase Order (PO):**
  * Quantity: 150 units
  * Unit Price: $20.00 per unit
  * Total Amount: $3,000.00
* **Invoice Received:**
  * Quantity: 140 units — 6.67% below the PO value, outside the configured ±5% tolerance; rejected.
  * Unit Price: $20.00 per unit (within tolerance)
  * Total Amount: $2,800.00
* **Tolerance Levels:**
  * Quantity Tolerance: ±5%
  * Unit Price Tolerance: ±2%

Étant donné que la quantité (140 unités) est inférieure à la limite de tolérance acceptable (écart négatif de -6.67 %) et n'est pas approuvée, mais que le prix unitaire ($20.00) est dans la tolérance, le système :

1. **Rejeter la quantité inférieure :** Le système n'accepte pas la quantité inférieure car elle se situe en dehors de la plage de tolérance approuvée.
2. **Ajuster la quantité :** Le système ajuste la quantité pour qu'elle corresponde au niveau approuvé spécifié dans le bon de commande.
   * Approved Quantity = 150 units (from PO)
3. **Maintenir le prix unitaire :** Le prix unitaire de $20.00 par unité est dans les limites de tolérance et reste inchangé.
4. **Recalculer le montant total :** Le système calcule le montant total en utilisant la quantité approuvée et le prix unitaire accepté :
   * **Total Amount = Approved Quantity × Unit Price**
   * **Total Amount = 150 units × $20.00 per unit = $3,000.00**
5. **Traiter la facture :** Le système traite la facture pour un montant total ajusté de $3,000.00, correspondant à la quantité et au prix unitaire approuvés. Le fournisseur est censé facturer la totalité de la quantité approuvée.

Cette approche garantit que la transaction financière est conforme aux conditions du bon de commande et évite la sous-facturation tout en conservant des registres financiers précis.
