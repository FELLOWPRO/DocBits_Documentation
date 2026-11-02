# Cas 14: Frais d’en-tête - Frais par unité hors tolérances (Approuvé)

Le scénario suivant illustre un mappage configuré ; il ne constitue pas un modèle par défaut dont le déploiement aurait été vérifié. La sortie réelle, les montants, les signes et les types de documents dépendent des règles et expressions `conflict_resolution` actives, du mappage d’export et des décisions d’approbation. Toute note de débit ou de crédit décrite ci-dessous est soumise à cette configuration ; cet exemple ne garantit ni son émission automatique ni la conformité juridique.

## Scénario :

Les frais d’en-tête par unité sont en dehors de la tolérance mais ont été approuvés.

## Action :

Le système traite les frais unitaires approuvés et les applique à la transaction.

## Exemple :

* **Purchase Order (PO):**
  * Frais d'en-tête par unité : $2.50
  * Quantity: 2,000 units
  * Total Header Charge Amount: $5,000.00
* **Invoice Received:**
  * Frais d'en-tête par unité : $3.00 (tolérance extérieure de 20 %, approuvée)
  * Quantity: 2,000 units
  * Total Header Charge Amount: $6,000.00
* **Tolerance Levels:**
  * Tolérance de charge par unité d'en-tête : ± 5 %

Étant donné que les frais d’en-tête par unité ($3.00) dépassent la plage de tolérance acceptable de 5 % mais ont été approuvés, le système :

1. **Accepter les frais d'en-tête approuvés par unité :** Le système accepte les frais d'en-tête facturés par unité de $3.00 car ils ont été approuvés malgré le dépassement de la limite de tolérance.
2. **Traitement des frais d'en-tête :** Le système traite la facture en utilisant les frais par unité approuvés et la quantité :
   * **Montant total des frais d'en-tête = Quantité × Frais d'en-tête approuvés par unité**
   * **Montant total des frais d’en-tête = 2,000 unités × $3.00 = $6,000.00**
3. **Finaliser la facture :** Le système traite la transaction avec les frais approuvés, pour un montant total de $6,000.00.

Cette approche permet au système de prendre en compte les écarts approuvés dans les frais d'en-tête, garantissant ainsi que la transaction est traitée conformément à l'approbation tout en conservant des registres financiers précis.
