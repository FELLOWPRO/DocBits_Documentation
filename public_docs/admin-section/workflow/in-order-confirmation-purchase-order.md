---
hidden: true
---

# Dans la confirmation de commande Bon de commande

### Comparer avec le bon de commande :

**Dans la confirmation de commande Bon de commande**

<figure><img src="https://lh7-us.googleusercontent.com/glQHETatKah-1YugeLqBb7Jim6lNJxuarRv-KEMv4NPzFfcjSm6mVhTMdI30nxdJ0SHXZ55Oup6KH7K-J6IxjUOiG0wxUX8toAaCopgBJwPyr94CPjoKuauNTmoHGGhg6f3gwHD39W7gpvijg4LQVJ4" alt="" width="563"><figcaption></figcaption></figure>

#### Carte logique : Correspondance de la quantité ou du prix unitaire ou de la remise

Cette carte logique est conçue pour vérifier automatiquement que la quantité, le prix unitaire ou la remise détaillés dans une confirmation de commande correspondent aux chiffres correspondants dans le bon de commande. Cette vérification assure la cohérence et l'exactitude entre ce qui a été commandé et ce que le fournisseur confirme livrer.

#### Condition de déclenchement

La logique est activée lorsqu'une des conditions suivantes est remplie dans une confirmation de commande par rapport au bon de commande original :

* **Quantité** : La quantité d'articles commandés correspond à la quantité confirmée par le fournisseur.
* **Prix unitaire** : Le prix par article convenu correspond à la confirmation du fournisseur.
* **Remise** : Toutes les remises appliquées sont cohérentes entre le bon de commande et la confirmation de commande.

#### Résultats

* **Égal** : Si la quantité, le prix unitaire ou la remise de la confirmation de commande correspondent exactement au bon de commande, le système considère la confirmation comme valide et passe aux étapes suivantes du processus d'achat.
* **Non égal** : S'il y a une divergence dans la quantité, le prix unitaire ou la remise, le système signale la confirmation de commande pour un examen manuel. Cela garantit que toutes les discordances sont résolues avant de continuer.

#### Avantages

* **Exactitude et cohérence** : Maintient l'exactitude dans le processus d'achat, garantissant que les paiements et les livraisons sont effectués sur la base de chiffres corrects.
* **Efficacité** : Automatise le processus de vérification, réduisant le besoin de vérifications manuelles et accélérant le traitement des commandes.
* **Contrôle des coûts** : Aide à prévenir les trop-payés ou les livraisons incorrectes en détectant les divergences tôt dans le processus.

<figure><img src="https://lh7-us.googleusercontent.com/DRTMJxJ9XLeC5zWSU8QuZwPLkqHzmCUm9RwiUZIkcc8pVxMZsxLv56dX9spzqr7KeDkTigbeBX2DvAZRe-6MdqOgAnrO-QPnCbi4e6hP4--P_O0A0DSoQJxjGeefOS1p6GuXHs1YXv-A73DXYaE8qlI" alt="" width="563"><figcaption></figcaption></figure>

1. **Définir les paramètres de comparaison** : Configurez les champs spécifiques (quantité, prix unitaire, remise) que la carte logique vérifiera pour une correspondance.
2. **Automatiser la vérification** : Configurez le système pour comparer automatiquement ces détails dès réception d'une confirmation de commande.
3. **Personnaliser les alertes** : Décidez du flux de travail pour la gestion des divergences, y compris la personnalisation des alertes pour examen manuel.

Cette carte logique est essentielle pour s'assurer que les détails d'une confirmation de commande s'alignent avec le bon de commande original, sauvegardant l'intégrité du cycle d'achat.
