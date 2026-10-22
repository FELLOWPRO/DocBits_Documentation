# Cas 7: Quantité dans les tolérances, Prix unitaire hors tolérances (Dépassement positif rejeté)

Le scénario suivant illustre un mappage configuré ; il ne constitue pas un modèle par défaut dont le déploiement aurait été vérifié. La sortie réelle, les montants, les signes et les types de documents dépendent des règles et expressions `conflict_resolution` actives, du mappage d’export et des décisions d’approbation. Toute note de débit ou de crédit décrite ci-dessous est soumise à cette configuration ; cet exemple ne garantit ni son émission automatique ni la conformité juridique.

## Scénario :

La quantité est dans les limites de tolérance, mais le prix unitaire dépasse la fourchette acceptable (tolérance positive) et n'est pas approuvé.

## Action :

Le système rejette le prix unitaire facturé, l'ajuste pour correspondre au bon de commande et peut générer une note de débit pour tenir compte du montant facturé en trop.

## Exemple :

* **Purchase Order (PO):**
  * Quantity: 200 units
  * Prix unitaire : $15.00 par unité
  * Total Amount: $3,000.00
* **Invoice Received:**
  * Quantité : 198 unités (avec une tolérance de 1%)
  * Prix unitaire : $17.00 par unité (en dehors de la tolérance positive de 13.33 %)
  * Total Amount: $3,366.00
* **Tolerance Levels:**
  * Quantity Tolerance: ±2%
  * Unit Price Tolerance: ±1%

Étant donné que la quantité (198 unités) se situe dans la plage de tolérance acceptable mais que le prix unitaire ($17.00) dépasse la tolérance acceptable et n'est pas approuvé, le système :

1. **Rejeter le prix unitaire facturé :** Le système n'accepte pas le prix unitaire facturé de $17.00.
2. **Ajuster le prix unitaire :** Le système ajuste le prix unitaire pour qu'il corresponde au prix unitaire du bon de commande d'origine.
   * Prix unitaire ajusté = $15.00 (à partir de PO)
3. **Calculer le montant total corrigé :** À l'aide du prix unitaire ajusté, le système recalcule le montant total.
   * **Montant total corrigé = Quantité × Prix unitaire ajusté**
   * **Montant total corrigé = 198 unités × $15.00 par unité = $2,970.00**
4. **Générer une note de débit :** Le système génère une note de débit pour tenir compte de la différence due au surfacturation.
   * **Montant de la note de débit = Total de la facture originale - Montant total corrigé**
   * **Montant de la note de débit = $3,366.00 - $2,970.00 = $396.00**
   * Cette note de débit représente le montant surfacturé par le fournisseur.
5. **Traiter la facture :** Le système traite la facture pour un montant total corrigé de $2,970.00 et émet une note de débit de $396.00 pour compenser la surfacturation.

Cette approche garantit que toute surfacturation est corrigée, alignant la transaction sur les conditions du bon de commande et protégeant les intérêts financiers de l'entreprise.
