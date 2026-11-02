# Cas 4, 5: Quantité dans les tolérances, Prix unitaire hors tolérances (Approuvé)

Le scénario suivant illustre un mappage configuré ; il ne constitue pas un modèle par défaut dont le déploiement aurait été vérifié. La sortie réelle, les montants, les signes et les types de documents dépendent des règles et expressions `conflict_resolution` actives, du mappage d’export et des décisions d’approbation. Toute note de débit ou de crédit décrite ci-dessous est soumise à cette configuration ; cet exemple ne garantit ni son émission automatique ni la conformité juridique.

## Scénario :

La quantité sur la facture se situe dans la tolérance, mais le prix unitaire est en dehors de la plage de tolérance acceptable. Cependant, cet écart dans le prix unitaire a été examiné et approuvé par les autorités compétentes.

## Action :

Le système ajuste le prix unitaire en fonction du bon de commande et applique tous les frais de ligne nécessaires pour tenir compte de la différence.

## Exemple :

**Purchase Order (PO):**

Quantity: <mark style="color:green;">100</mark> units

Prix unitaire : $10.00 par unité

Total Amount: <mark style="color:purple;">$1,000.00</mark>

**Invoice Received:**

Quantité : <mark style="color:green;">100</mark> unités (dans la limite des tolérances)

Prix unitaire : <mark style="color:red;">$11.00</mark> par unité (hors tolérance de ±5 %)

Total Amount: <mark style="color:red;">$1,100.00</mark>

**Tolerance Levels:**

Quantity Tolerance: ±2%

Tolérance de prix unitaire : ±5 % (plage prévue : $9.50 à $10.50)

**Approval:**

• Le prix unitaire de $11.00 se situe en dehors de la plage de tolérance, mais a été approuvé manuellement par le service concerné.

Puisque la quantité est dans la tolérance mais que le prix unitaire est hors tolérance (pourtant approuvé), le système :

1\. **Ajuster le prix unitaire** : Le système ajuste le prix unitaire au prix unitaire du PO car l'écart a été approuvé :

• **Prix unitaire ajusté = $10.00 par unité**

• **Montant total ajusté = 100 unités × $10.00 par unité = $1,000.00**

2\. **Appliquer des frais de ligne pour la différence** : Étant donné que le prix unitaire approuvé de $11.00 est supérieur au prix unitaire PO de $10.00, le système applique des frais de ligne pour tenir compte de cette différence :

• **Montant des frais de ligne = (Prix unitaire de la facture approuvé - PO Prix unitaire) × Quantité**

• **Montant des frais de ligne = ($11.00 - $10.00) × 100 unités = $100.00**

3\. **Traitement de la facture** : Le système traite la facture avec :

• **Base Amount:** $1,000.00

• **Line Charge:** $100.00

• **Montant total traité:** $1,100.00

Cela garantit que même si les valeurs de base PO sont maintenues par souci de cohérence, l'écart approuvé dans le prix unitaire est pris en compte par le biais de frais de ligne supplémentaires, ce qui entraîne un traitement financier et une tenue de registres précis.
