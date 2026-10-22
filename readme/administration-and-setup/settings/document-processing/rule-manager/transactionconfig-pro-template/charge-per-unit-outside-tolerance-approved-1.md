# Cas 14: Ligne de frais - Frais par unité hors tolérances (Approuvé)

Le scénario suivant illustre un mappage configuré ; il ne constitue pas un modèle par défaut dont le déploiement aurait été vérifié. La sortie réelle, les montants, les signes et les types de documents dépendent des règles et expressions `conflict_resolution` actives, du mappage d’export et des décisions d’approbation. Toute note de débit ou de crédit décrite ci-dessous est soumise à cette configuration ; cet exemple ne garantit ni son émission automatique ni la conformité juridique.

## Scénario :

Les frais par unité sont hors tolérance mais ont été approuvés.

## Action :

Le système accepte les frais par unité et applique les frais approuvés, traitant la transaction en conséquence.

## Exemple :

* **Purchase Order (PO):**
  * Charge Per Unit: $4.50
  * Quantity: 1,000 units
  * Total Charge Amount: $4,500.00
* **Invoice Received:**
  * Frais par unité : $5.00 (hors tolérance de 11.11 %, approuvé)
  * Quantity: 1,000 units
  * Total Charge Amount: $5,000.00
* **Tolerance Levels:**
  * Charge Per Unit Tolerance: ±5%

Puisque les frais par unité ($5.00) se situent en dehors de la plage de tolérance acceptable de 5 %, mais ont été approuvés, le système :

1. **Accepter les frais par unité approuvés :** Le système accepte les frais facturés par unité de $5.00 car ils ont été approuvés malgré le dépassement de la limite de tolérance.
2. **Traitement de la transaction :** Le système traite la facture en utilisant les frais unitaires approuvés et la quantité :
   * **Montant total des frais = Quantité × Frais approuvés par unité**
   * **Montant total des frais = 1,000 unités × $5.00 = $5,000.00**
3. **Finaliser la facture :** Le système traite la transaction avec les frais approuvés, pour un montant total de $5,000.00.

Cette approche garantit que le système peut prendre en compte les écarts de frais approuvés, ce qui permet une flexibilité tout en conservant des registres financiers précis.
