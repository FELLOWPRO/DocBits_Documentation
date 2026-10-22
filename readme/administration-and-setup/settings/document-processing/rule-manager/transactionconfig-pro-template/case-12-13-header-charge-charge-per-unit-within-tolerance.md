# Frais par unité dans les tolérances

Le scénario suivant illustre un mappage configuré ; il ne constitue pas un modèle par défaut dont le déploiement aurait été vérifié. La sortie réelle, les montants, les signes et les types de documents dépendent des règles et expressions `conflict_resolution` actives, du mappage d’export et des décisions d’approbation. Toute note de débit ou de crédit décrite ci-dessous est soumise à cette configuration ; cet exemple ne garantit ni son émission automatique ni la conformité juridique.

## Scénario :

Les frais d'en-tête par unité se situent dans la plage de tolérance acceptable par rapport au bon de commande.

## Action :

Le système traite les frais d'en-tête tels que facturés et les applique sans ajustements.

## Exemple :

* **Purchase Order (PO):**
  * Frais d'en-tête par unité : $3.50
  * Quantity: 1,200 units
  * Total Header Charge Amount: $4,200.00
* **Invoice Received:**
  * Frais d'en-tête par unité : $3.55 (dans les limites d'une tolérance de 1.43 %)
  * Quantity: 1,200 units
  * Total Header Charge Amount: $4,260.00
* **Tolerance Levels:**
  * Tolérance de charge par unité d'en-tête : ± 2 %

Étant donné que les frais d'en-tête par unité ($3.55) se situent dans la plage de tolérance acceptable de 2 % par rapport au bon de commande, le système :

1. **Accepter les frais d'en-tête par unité :** Le système accepte les frais d'en-tête facturés par unité de $3.55 car ils se situent dans la limite de tolérance définie.
2. **Traitement des frais d'en-tête :** Le système traite la facture avec le montant total des frais d'en-tête en fonction des frais facturés par unité et par quantité :
   * **Montant total des frais d'en-tête = Quantité × Frais d'en-tête par unité**
   * **Montant total des frais d’en-tête = 1,200 unités × $3.55 = $4,260.00**
3. **Finaliser la facture :** Le système traite la transaction sans aucun ajustement, acceptant la facture telle quelle.

Cette approche garantit un traitement fluide et efficace des transactions lorsque les frais d'en-tête se situent dans la plage de tolérance acceptable, évitant ainsi les rejets ou les retards inutiles.
