# Frais par unité dans les tolérances

Le scénario suivant illustre un mappage configuré ; il ne constitue pas un modèle par défaut dont le déploiement aurait été vérifié. La sortie réelle, les montants, les signes et les types de documents dépendent des règles et expressions `conflict_resolution` actives, du mappage d’export et des décisions d’approbation. Toute note de débit ou de crédit décrite ci-dessous est soumise à cette configuration ; cet exemple ne garantit ni son émission automatique ni la conformité juridique.

## Scénario :

Les frais unitaires indiqués sur la facture se situent dans la plage de tolérance acceptable par rapport au bon de commande.

## Action :

Le système accepte les frais unitaires tels que facturés et traite la transaction sans ajustements.

## Exemple :

* **Purchase Order (PO):**
  * Charge Per Unit: $5.00
  * Quantity: 500 units
  * Total Charge Amount: $2,500.00
* **Invoice Received:**
  * Frais par unité : $5.10 (dans la limite d'une tolérance de 2 %)
  * Quantity: 500 units
  * Total Charge Amount: $2,550.00
* **Tolerance Levels:**
  * Charge Per Unit Tolerance: ±3%

Étant donné que les frais par unité ($5.10) se situent dans la plage de tolérance acceptable de 3 % par rapport au bon de commande, le système :

1. **Accepter les frais par unité :** Le système accepte les frais facturés par unité de $5.10 car ils se situent dans la limite de tolérance définie.
2. **Traitement de la transaction :** Le système traite la facture avec le montant total des frais en fonction des frais facturés par unité et de la quantité :
   * **Montant total des frais = Quantité × Frais par unité**
   * **Montant total des frais = 500 unités × $5.10 = $2,550.00**
3. **Finaliser la facture :** Le système traite la transaction sans aucun ajustement, acceptant la facture telle quelle.

Cette approche permet au système de s'adapter à des écarts mineurs acceptables dans les frais, garantissant ainsi un traitement fluide et efficace des transactions sans rejets ni retards inutiles.
