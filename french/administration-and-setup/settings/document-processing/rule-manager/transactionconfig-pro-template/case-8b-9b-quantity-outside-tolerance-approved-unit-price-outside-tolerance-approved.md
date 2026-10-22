# Cas 8b, 9b: Quantité hors tolérances (Approuvé), Prix unitaire hors tolérances (Approuvé)

Le scénario suivant illustre un mappage configuré ; il ne constitue pas un modèle par défaut dont le déploiement aurait été vérifié. La sortie réelle, les montants, les signes et les types de documents dépendent des règles et expressions `conflict_resolution` actives, du mappage d’export et des décisions d’approbation. Toute note de débit ou de crédit décrite ci-dessous est soumise à cette configuration ; cet exemple ne garantit ni son émission automatique ni la conformité juridique.

## Scénario :

La quantité et le prix unitaire se situent en dehors de la plage de tolérance mais ont été approuvés.

## Action :

Le système traite la transaction en utilisant les valeurs facturées pour la quantité et le prix unitaire, en appliquant tous les ajustements ou frais de ligne nécessaires.

## Exemple :

* **Purchase Order (PO):**
  * Quantity: 200 units
  * Prix unitaire : $25.00 par unité
  * Total Amount: $5,000.00
* **Invoice Received:**
  * Quantité : 220 unités (hors tolérance de 10%, homologué)
  * Prix unitaire : $27.00 par unité (hors tolérance de 8 %, approuvé)
  * Total Amount: $5,940.00
* **Tolerance Levels:**
  * Quantity Tolerance: ±5%
  * Unit Price Tolerance: ±2%

Étant donné que la quantité (220 unités) et le prix unitaire ($27.00) sont en dehors des limites de tolérance acceptables mais ont été approuvés, le système :

1. **Accepter la quantité approuvée :** Le système accepte la quantité facturée de 220 unités car elle a été approuvée bien qu'elle soit en dehors de la plage de tolérance.
2. **Accepter le prix unitaire approuvé :** Le système accepte le prix unitaire facturé de $27.00 par unité car il a été approuvé bien qu'il soit en dehors de la plage de tolérance.
3. **Calculer le montant total :** Le système calcule le montant total en fonction des valeurs de facture approuvées :
   * **Montant total = Quantité × Prix unitaire**
   * **Montant total = 220 unités × $27.00 par unité = $5,940.00**
4. **Appliquer les ajustements ou frais de ligne nécessaires :** Le cas échéant, le système peut appliquer des frais de ligne ou des ajustements supplémentaires en fonction des politiques de l'organisation en matière de gestion des écarts approuvés.
5. **Traiter la facture :** Le système utilise les valeurs approuvées de quantité et de prix unitaire et finalise la transaction pour un montant total de $5,940.00.

Cette approche garantit que la transaction est traitée conformément aux écarts approuvés, ce qui permet une flexibilité tout en conservant des dossiers financiers précis.
