# Cas 15: Frais d’en-tête - Frais par unité hors tolérances (Rejeté)

Le scénario suivant illustre un mappage configuré ; il ne constitue pas un modèle par défaut dont le déploiement aurait été vérifié. La sortie réelle, les montants, les signes et les types de documents dépendent des règles et expressions `conflict_resolution` actives, du mappage d’export et des décisions d’approbation. Toute note de débit ou de crédit décrite ci-dessous est soumise à cette configuration ; cet exemple ne garantit ni son émission automatique ni la conformité juridique.

## Scénario :

Les frais d'en-tête par unité sont en dehors de la tolérance et n'ont pas été approuvés.

## Action :

Le système ajuste les frais d'en-tête pour qu'ils correspondent au bon de commande, traite la transaction en conséquence et génère toutes les notes nécessaires.

## Exemple :

* **Purchase Order (PO):**
  * Frais d'en-tête par unité : $4.00
  * Quantity: 1,500 units
  * Total Header Charge Amount: $6,000.00
* **Invoice Received:**
  * Frais d'en-tête par unité : $5.00 (hors tolérance de 25 %, rejeté)
  * Quantity: 1,500 units
  * Total Header Charge Amount: $7,500.00
* **Tolerance Levels:**
  * Tolérance de charge par unité d'en-tête : ± 5 %

Étant donné que les frais d’en-tête par unité ($5.00) dépassent la plage de tolérance acceptable de 5 % et n'ont pas été approuvés, le système :

1. **Rejeter les frais d'en-tête facturés par unité :** Le système n'accepte pas les frais d'en-tête facturés par unité de $5.00 en raison de l'écart dépassant la limite de tolérance.
2. **Ajustez les frais par unité d'en-tête :** Le système ajuste les frais par unité pour qu'ils correspondent au bon de commande d'origine ou aux frais par unité approuvés :
   * Frais d'en-tête ajustés par unité = $4.00 (à partir de PO)
3. **Recalculer le montant total des frais d'en-tête :** Le système recalcule le montant total des frais en fonction des frais ajustés par unité :
   * **Montant total des frais d'en-tête corrigé = Quantité × Frais d'en-tête ajustés par unité**
   * **Montant total corrigé des frais d’en-tête = 1,500 unités × $4.00 = $6,000.00**
4. **Générer une note de crédit :** Le total de la facture originale étant supérieur au total corrigé, le système génère une note de crédit pour le montant surfacturé :
   * **Montant de la note de crédit = Total de la facture originale - Montant total des frais d'en-tête corrigé**
   * **Montant de la note de crédit = $7,500.00 - $6,000.00 = $1,500.00**
5. **Traiter la facture :** Le système traite la facture avec des frais totaux corrigés de $6,000.00 et émet une note de crédit de $1,500.00 pour tenir compte du montant surfacturé.

Cette approche garantit que la transaction est alignée sur les conditions initiales du bon de commande, en maintenant un traitement financier précis tout en corrigeant les éventuelles surfacturations.
