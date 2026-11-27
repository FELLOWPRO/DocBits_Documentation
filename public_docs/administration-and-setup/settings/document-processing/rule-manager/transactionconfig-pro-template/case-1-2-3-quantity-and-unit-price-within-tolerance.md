# Cas 1, 2, 3: Quantité et prix unitaire dans les tolérances

Le scénario suivant illustre un mappage configuré ; il ne constitue pas un modèle par défaut dont le déploiement aurait été vérifié. La sortie réelle, les montants, les signes et les types de documents dépendent des règles et expressions `conflict_resolution` actives, du mappage d’export et des décisions d’approbation. Toute note de débit ou de crédit décrite ci-dessous est soumise à cette configuration ; cet exemple ne garantit ni son émission automatique ni la conformité juridique.

## Scénario :

La quantité et le prix unitaire sur la facture se situent dans une plage de tolérance acceptable par rapport au bon de commande.

## Action :

Le système accepte les valeurs de la facture et calcule le montant total en fonction de la quantité et du prix unitaire fournis.

## Exemple :

**Purchase Order (PO):**

Quantity: 100 units

Unit Price: $10.00 per unit

Total Amount: $1,000.00

**Invoice Received:**

Quantity: 101 units — 1% above the PO value, within the configured ±2% tolerance.

Unit Price: $10.05 per unit — 0.5% above the PO value, within the configured ±1% tolerance.

Total Amount: $1,015.05

**Tolerance Levels:**

Quantity Tolerance: ±2%

Unit Price Tolerance: ±1%


Étant donné que la quantité (101 unités) et le prix unitaire ($10.05) se situent tous deux dans les niveaux de tolérance acceptables par rapport au bon de commande, le système :


1\. **Accepter les valeurs de la facture :** La quantité et le prix unitaire sur la facture sont acceptés comme valides car ils se situent dans les limites de tolérance définies.

2\. **Calculer le Montant Total :** Le montant total est calculé à partir des valeurs acceptées :

• Total Amount = Quantity × Unit Price

• Total Amount = 101 units × $10.05 per unit = $1,015.05

3\. **Traiter la facture :** La facture est traitée pour un montant total de $1,015.05 et les écritures comptables sont mises à jour en conséquence.

Cette approche garantit que les écarts mineurs qui se situent dans des niveaux de tolérance acceptables n'entraînent pas de rejets de factures ou de retards de paiement, rationalisant ainsi le processus financier.
