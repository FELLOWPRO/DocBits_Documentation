# Cas 10b: Quantité insuffisante rejetée et prix unitaire hors tolérance rejeté

Le scénario suivant illustre un mappage configuré ; il ne constitue pas un modèle par défaut dont le déploiement aurait été vérifié. La sortie réelle, les montants, les signes et les types de documents dépendent des règles et expressions `conflict_resolution` actives, du mappage d’export et des décisions d’approbation. Toute note de débit ou de crédit décrite ci-dessous est soumise à cette configuration ; cet exemple ne garantit ni son émission automatique ni la conformité juridique.

## Scénario :

La quantité et le prix unitaire sont hors tolérance et aucun n’a été approuvé.

## Action :

Le système rejette les données de la facture, ajuste les valeurs pour qu'elles correspondent au bon de commande et génère les notes de débit ou de crédit nécessaires.

## Exemple :

* **Purchase Order (PO):**
  * Quantity: 150 units
  * Prix unitaire : $30.00 par unité
  * Total Amount: $4,500.00
* **Invoice Received:**
  * Quantité : 140 unités (hors tolérance de -6.67%, rejeté)
  * Prix unitaire : $33.00 par unité (hors tolérance de 10 %, rejeté)
  * Total Amount: $4,620.00
* **Tolerance Levels:**
  * Quantity Tolerance: ±5%
  * Unit Price Tolerance: ±2%

Étant donné que la quantité (140 unités) et le prix unitaire ($33.00) se situent en dehors des limites de tolérance acceptables et qu'aucun des deux n'a été approuvé, le système :

1. **Rejeter les données de la facture :** Le système n'accepte pas la quantité facturée ou le prix unitaire en raison de leur écart par rapport aux limites de tolérance.
2. **Ajuster la quantité :** Le système ajuste la quantité pour qu'elle corresponde à la quantité du bon de commande d'origine.
   * Quantité ajustée = 150 unités (à partir de PO)
3. **Ajuster le prix unitaire :** Le système ajuste le prix unitaire pour qu'il corresponde au prix unitaire du bon de commande d'origine.
   * Prix unitaire ajusté = $30.00 par unité (à partir de PO)
4. **Recalculer le montant total :** Le système recalcule le montant total en utilisant la quantité ajustée et le prix unitaire :
   * **Montant total corrigé = Quantité ajustée × Prix unitaire ajusté**
   * **Montant total corrigé = 150 unités × $30.00 par unité = $4,500.00**
5. **Générer une note de débit :** Le total de la facture originale étant supérieur au total corrigé, le système génère une note de débit pour le montant surfacturé.
   * **Montant de la note de débit = Total de la facture originale - Montant total corrigé**
   * **Montant de la note de débit = $4,620.00 - $4,500.00 = $120.00**
6. **Traiter la facture :** Le système traite la facture pour un montant total corrigé de $4,500.00 et émet une note de débit de $120.00 pour compenser la surfacturation.

Cette approche garantit que la transaction financière est corrigée pour correspondre aux conditions du bon de commande, tout en maintenant des pratiques de facturation précises et équitables.
