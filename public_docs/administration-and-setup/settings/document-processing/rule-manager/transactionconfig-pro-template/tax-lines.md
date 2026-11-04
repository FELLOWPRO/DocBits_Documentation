# Lignes de taxe

Le scénario suivant illustre un mappage configuré ; il ne constitue pas un modèle par défaut dont le déploiement aurait été vérifié. La sortie réelle, les montants, les signes et les types de documents dépendent des règles et expressions `conflict_resolution` actives, du mappage d’export et des décisions d’approbation. Toute note de débit ou de crédit décrite ci-dessous est soumise à cette configuration ; cet exemple ne garantit ni son émission automatique ni la conformité juridique.

## Scénario :

Gère les écarts de montants de taxes entre la facture et le bon de commande.

## Action :

Le système ajuste les lignes de taxe en fonction des taux et montants de taxe approuvés, garantissant ainsi le respect des réglementations fiscales applicables.

## Exemple :

* **Purchase Order (PO):**
  * Subtotal Amount: $10,000.00
  * Tax Rate: 8%
  * Montant de taxe prévu : $800.00
  * Total Amount with Tax: $10,800.00
* **Invoice Received:**
  * Subtotal Amount: $10,000.00
  * Taux d'imposition : 10 % (écart)
  * Invoiced Tax Amount: $1,000.00
  * Total Amount with Tax: $11,000.00

Étant donné que le taux de taxe sur la facture (10 %) diffère du taux de taxe prévu (8 %) et n'est pas approuvé, le système :

1. **Rejeter le taux de taxe facturé :** Le système n'accepte pas le taux de taxe de 10 % car il ne correspond pas au taux approuvé dans le bon de commande.
2. **Ajuster le taux de taxe :** Le système ajuste le taux de taxe pour qu'il corresponde au taux approuvé du bon de commande.
   * Taux d'imposition ajusté = 8 % (à partir de PO)
3. **Recalculer le montant de la taxe :** Le système recalcule le montant de la taxe en fonction du taux de taxe ajusté :
   * **Montant de taxe corrigé = Montant du sous-total × Taux de taxe ajusté**
   * **Montant corrigé de la taxe = $10,000.00 × 8% = $800.00**
4. **Recalculer le Montant Total :** Le système recalcule le montant total TTC :
   * **Montant total corrigé avec taxe = Montant sous-total + Montant de taxe corrigé**
   * **Montant total corrigé avec taxe = $10,000.00 + $800.00 = $10,800.00**
5. **Générer un avoir :** Le système génère un avoir pour corriger la taxe surfacturée :
   * **Montant de la note de crédit = Montant de taxe sur la facture originale - Montant de taxe corrigé**
   * **Montant de la note de crédit = $1,000.00 - $800.00 = $200.00**
6. **Traiter la facture :** Le système traite la facture avec une taxe corrigée de $800.00 et un montant total de $10,800.00, et émet une note de crédit correspondant à l’écart de taxe de $200.00.

Cette approche garantit que la taxe sur la facture est cohérente avec le bon de commande et est conforme aux réglementations fiscales applicables, évitant ainsi les trop-payés et garantissant l'exactitude des dossiers financiers.
