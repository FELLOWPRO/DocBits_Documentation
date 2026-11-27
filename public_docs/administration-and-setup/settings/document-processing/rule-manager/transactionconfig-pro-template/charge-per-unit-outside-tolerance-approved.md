# Cas 14: Frais d’en-tête - Frais par unité hors tolérances (Approuvé)

Le scénario suivant illustre un mappage configuré ; il ne constitue pas un modèle par défaut dont le déploiement aurait été vérifié. La sortie réelle, les montants, les signes et les types de documents dépendent des règles et expressions `conflict_resolution` actives, du mappage d’export et des décisions d’approbation. Toute note de débit ou de crédit décrite ci-dessous est soumise à cette configuration ; cet exemple ne garantit ni son émission automatique ni la conformité juridique.

## Scénario :

Les frais d’en-tête par unité sont en dehors de la tolérance mais ont été approuvés.

## Action :

Le système traite les frais unitaires approuvés et les applique à la transaction.

## Exemple :

* **Purchase Order (PO):**
  * Header Charge Per Unit: $2.50
  * Quantity: 2,000 units
  * Total Header Charge Amount: $5,000.00
* **Invoice Received:**
  * Header Charge Per Unit: $3.00 — 20% above the PO value, outside the configured ±5% tolerance; approved.
  * Quantity: 2,000 units
  * Total Header Charge Amount: $6,000.00
* **Tolerance Levels:**
  * Header Charge Per Unit Tolerance: ±5%

Étant donné que le Header Charge Per Unit ($3.00) dépasse la plage de tolérance acceptable de 5 % mais a été approuvé, le système :

1. **Accepter les frais d'en-tête approuvés par unité :** Le système accepte les frais d'en-tête facturés par unité de $3.00 car ils ont été approuvés malgré le dépassement de la limite de tolérance.
2. **Traitement des frais d'en-tête :** Le système traite la facture en utilisant les frais par unité approuvés et la quantité :
   * **Total Header Charge Amount = Quantity × Approved Header Charge Per Unit**
   * **Total Header Charge Amount = 2,000 units × $3.00 = $6,000.00**
3. **Finaliser la facture :** Le système traite la transaction avec les frais approuvés, pour un montant total de $6,000.00.

Cette approche permet au système de prendre en compte les écarts approuvés dans les frais d'en-tête, garantissant ainsi que la transaction est traitée conformément à l'approbation tout en conservant des registres financiers précis.
