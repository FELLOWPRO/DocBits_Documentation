# Frais par unité hors tolérances (Rejeté)

Le scénario suivant illustre un mappage configuré ; il ne constitue pas un modèle par défaut dont le déploiement aurait été vérifié. La sortie réelle, les montants, les signes et les types de documents dépendent des règles et expressions `conflict_resolution` actives, du mappage d’export et des décisions d’approbation. Toute note de débit ou de crédit décrite ci-dessous est soumise à cette configuration ; cet exemple ne garantit ni son émission automatique ni la conformité juridique.

## Scénario :

Le Charge Per Unit est hors tolérance et n’a pas été approuvé.

## Action :

Le système ajuste le Charge Per Unit pour qu’il corresponde au bon de commande ou aux niveaux approuvés, générant ainsi toutes les notes de débit ou de crédit nécessaires.

## Exemple :

* **Purchase Order (PO):**
  * Charge Per Unit: $6.00
  * Quantity: 800 units
  * Total Charge Amount: $4,800.00
* **Invoice Received:**
  * Charge Per Unit: $7.00 (variance 16.67%, outside the ±5% tolerance, rejected)
  * Quantity: 800 units
  * Total Charge Amount: $5,600.00
* **Tolerance Levels:**
  * Charge Per Unit Tolerance: ±5%

Étant donné que le Charge Per Unit ($7.00) dépasse la plage de tolérance acceptable de 5 % et n'a pas été approuvé, le système :

1. **Reject the Invoiced Charge Per Unit:** Le système n'accepte pas le Charge Per Unit facturé de $7.00 en raison de l'écart dépassant la limite de tolérance.
2. **Adjust the Charge Per Unit:** Le système ajuste le Charge Per Unit pour qu'il corresponde au bon de commande ou au Charge Per Unit approuvé :
   * Adjusted Charge Per Unit = $6.00 (from PO)
3. **Recalculate the Total Charge Amount:** Le système recalcule le Total Charge Amount en fonction du Charge Per Unit ajusté :
   * **Corrected Total Charge Amount = Quantity × Adjusted Charge Per Unit**
   * **Corrected Total Charge Amount = 800 units × $6.00 = $4,800.00**
4. **Generate a Debit Note:** Le total de la facture originale étant supérieur au total corrigé, le système génère une note de débit pour le montant surfacturé :
   * **Debit Note Amount = Original Invoice Total - Corrected Total Charge Amount**
   * **Debit Note Amount = $5,600.00 - $4,800.00 = $800.00**
5. **Process the Invoice:** Le système traite la facture avec le Total Charge Amount corrigé de $4,800.00 et émet une note de débit de $800.00 pour tenir compte du montant surfacturé.

Cette approche garantit que les transactions financières sont conformes aux conditions du bon de commande, en rejetant les écarts non approuvés et en maintenant des pratiques de facturation précises.
