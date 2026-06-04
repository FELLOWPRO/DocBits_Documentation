---
hidden: true
---

# In Order Confirmation Purchase Order

### Compare with Purchase Order :

**In Order Confirmation Purchase Order**

<figure><img src="https://lh7-us.googleusercontent.com/glQHETatKah-1YugeLqBb7Jim6lNJxuarRv-KEMv4NPzFfcjSm6mVhTMdI30nxdJ0SHXZ55Oup6KH7K-J6IxjUOiG0wxUX8toAaCopgBJwPyr94CPjoKuauNTmoHGGhg6f3gwHD39W7gpvijg4LQVJ4" alt="" width="563"><figcaption></figcaption></figure>

#### Carte Logic : Correspondance de quantité, prix unitaire ou remise

Cette carte logique est conçue pour vérifier automatiquement que la quantité, le prix unitaire ou la remise détaillés dans une confirmation de commande correspondent aux chiffres correspondants du bon de commande. Cette vérification garantit la cohérence et l'exactitude entre ce qui a été commandé et ce que le fournisseur confirme livrer.

#### Condition de déclenchement

La logique est activée lorsque l'une des conditions suivantes est remplie dans une confirmation de commande par rapport au bon de commande initial :

* **Quantity** : la quantité d'articles commandés correspond à la quantité confirmée par le fournisseur.
* **Unit Price** : le prix par article convenu correspond à la confirmation du fournisseur.
* **Discount** : toute remise appliquée est cohérente entre le bon de commande et la confirmation de commande.

#### Résultats

* **Equals** : si la quantité, le prix unitaire ou la remise de la confirmation de commande correspond exactement au bon de commande, le système considère la confirmation comme valide et poursuit les étapes suivantes du processus d'approvisionnement.
* **Not Equal** : en cas d'écart sur la quantité, le prix unitaire ou la remise, le système signale la confirmation de commande pour un examen manuel. Cela garantit que toute incohérence est résolue avant de poursuivre.

#### Avantages

* **Exactitude et cohérence** : préserve l'exactitude du processus d'approvisionnement, en garantissant que les paiements et les livraisons sont effectués sur la base de chiffres corrects.
* **Efficacité** : automatise le processus de vérification, réduisant le besoin de contrôles manuels et accélérant le traitement des commandes.
* **Maîtrise des coûts** : aide à prévenir les surpaiements ou les livraisons incorrectes en détectant les écarts en amont du processus.

<figure><img src="https://lh7-us.googleusercontent.com/DRTMJxJ9XLeC5zWSU8QuZwPLkqHzmCUm9RwiUZIkcc8pVxMZsxLv56dX9spzqr7KeDkTigbeBX2DvAZRe-6MdqOgAnrO-QPnCbi4e6hP4--P_O0A0DSoQJxjGeefOS1p6GuXHs1YXv-A73DXYaE8qlI" alt="" width="563"><figcaption></figcaption></figure>

1. **Définir les paramètres de comparaison** : configurez les champs spécifiques (quantité, prix unitaire, remise) que la carte logique vérifiera pour établir une correspondance.
2. **Automatiser la vérification** : configurez le système pour comparer automatiquement ces détails à la réception d'une confirmation de commande.
3. **Personnaliser les alertes** : décidez du workflow de gestion des écarts, y compris la personnalisation des alertes pour l'examen manuel.

Cette carte logique est essentielle pour garantir que les détails d'une confirmation de commande correspondent au bon de commande initial, préservant l'intégrité du cycle d'approvisionnement. \`\`
