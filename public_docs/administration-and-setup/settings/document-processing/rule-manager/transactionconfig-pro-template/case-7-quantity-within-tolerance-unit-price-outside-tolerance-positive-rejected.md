# Cas 7 : Quantité dans la tolérance, Prix unitaire hors tolérance (Dépassement positif rejeté)

Le scénario suivant est un mappage configuré à titre d'exemple, et non un modèle par défaut dont le déploiement aurait été vérifié. La sortie réelle, les montants, les signes et les types de documents dépendent des règles et expressions `conflict_resolution` actives, du mappage d'export et des décisions d'approbation. Toute note de débit ou de crédit décrite ci-dessous est conditionnée par cette configuration ; cet exemple ne garantit ni une émission automatique ni la conformité juridique.

## Scénario :

La quantité se situe dans la tolérance, mais le prix unitaire dépasse la plage acceptable (tolérance positive) et n'est pas approuvé.

## Action :

Le système rejette le prix unitaire facturé, l'ajuste pour correspondre au bon de commande et peut générer une note de débit pour tenir compte du montant surfacturé.

## Exemple :

* **Purchase Order (PO):**
  * Quantity: 200 unités
  * Unit Price: $15.00 par unité
  * Total Amount: $3,000.00
* **Invoice Received:**
  * Quantity: 198 unités — 1 % inférieur à la valeur du PO, dans la tolérance configurée de ±2 %.
  * Unit Price: $17.00 par unité — 13.33 % supérieur à la valeur du PO, hors de la tolérance configurée de ±1 % ; rejeté.
  * Total Amount: $3,366.00
* **Tolerance Levels:**
  * Quantity Tolerance: ±2%
  * Unit Price Tolerance: ±1%

La quantité (198 unités) se situe dans la plage de tolérance acceptable, mais le prix unitaire ($17.00) dépasse la tolérance acceptable et n'est pas approuvé ; le système va donc :

1. **Rejeter le prix unitaire facturé:** Le système n'accepte pas le prix unitaire facturé de $17.00.
2. **Ajuster le prix unitaire:** Le système ajuste le prix unitaire pour correspondre au prix unitaire du bon de commande d'origine.
   * Prix unitaire ajusté = $15.00 (issu du PO)
3. **Calculer le montant total corrigé:** À l'aide du prix unitaire ajusté, le système recalcule le montant total.
   * **Corrected Total Amount = Quantity × Adjusted Unit Price**
   * **Corrected Total Amount = 198 units × $15.00 per unit = $2,970.00**
4. **Générer une note de débit:** Le système génère une note de débit pour tenir compte de l'écart dû à la surfacturation.
   * **Debit Note Amount = Original Invoice Total - Corrected Total Amount**
   * **Debit Note Amount = $3,366.00 - $2,970.00 = $396.00**
   * Cette note de débit représente le montant surfacturé par le fournisseur.
5. **Traiter la facture:** Le système traite la facture avec le montant total corrigé de $2,970.00 et émet une note de débit de $396.00 pour compenser la surfacturation.

Cette approche garantit que toute surfacturation est corrigée, en alignant la transaction sur les conditions du bon de commande et en protégeant les intérêts financiers de l'entreprise.
