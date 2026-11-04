# Date de livraison promise pour les articles de la table avec date de livraison promise

<figure><img src="../../../../../.gitbook/assets/image.png" alt="" width="375"><figcaption></figcaption></figure>

## Objet :

Cette carte de flux de travail est conçue pour valider la **date de livraison promise des articles** par rapport à la **date de livraison promise sur le bon de commande**, à l'aide d'opérateurs de comparaison et de règles de tolérance configurables. Elle permet aux flux de travail de détecter automatiquement les dates de livraison conformes, précoces ou tardives et de réagir en conséquence.

## Composants de la carte :

1. **Opérateur**
   * **Description :**
     Définit comment la date de livraison promise de l'article est comparée à la date de livraison promise du bon de commande.
   * **Options :**
     * **Égal (=) :** La date de l'article doit se situer dans la fenêtre de tolérance.
     * **Non égal (≠) :** La date de l'article doit se situer en dehors de la fenêtre de tolérance.
     * **Supérieur à (>) :** La date de l'article doit être après la fenêtre de tolérance.
     * **Supérieur ou égal (≥) :** La date de l'article doit être le jour ou après le début de la fenêtre de tolérance.
     * **Inférieur à (<) :** La date de l'article doit être avant la fenêtre de tolérance.
     * **Inférieur ou égal (≤) :** La date de l'article doit être le jour ou avant la fin de la fenêtre de tolérance.<br>
2. **Jours de tolérance**
   * **Description :**
     Spécifie le nombre de jours utilisés pour calculer la fenêtre de tolérance acceptable autour de la date de livraison promise du bon de commande.
   * **Détail :**
     Cette valeur est un entier et définit le nombre de jours avant et après la date du bon de commande qui sont pris en compte lors de la validation.<br>
3. **Jours de tolérance autorisés**
   * **Description :**
     Définit quels jours de la semaine sont comptabilisés lors du calcul des jours de tolérance.
   * **Détail :**
     Les utilisateurs peuvent sélectionner des jours de semaine spécifiques (par exemple, du lundi au vendredi). Seuls les jours sélectionnés sont inclus lors du calcul de la fenêtre de tolérance.

### Fonctionnalité :

* **Évaluation de la condition :** Le système calcule une fenêtre de tolérance autour de la date de livraison promise du bon de commande en fonction des **jours de tolérance** et des **jours de tolérance autorisés** configurés.
  La date de livraison promise de chaque article est ensuite comparée à cette fenêtre à l'aide de l'opérateur sélectionné.
* Exécution de l'action :
  * **Condition vraie :** Si la différence de date de livraison se situe dans la plage de tolérance et correspond à la condition définie par l'opérateur, le flux de travail se poursuit.
  * **Condition fausse :** Si la condition n'est pas remplie, le flux de travail ne continuera pas.

### Configuration et paramétrage :

* Sélectionnez l'opérateur de comparaison approprié.
* Entrez le nombre de jours de tolérance.
* Choisissez les jours de la semaine qui doivent être comptabilisés comme jours de tolérance.

### Conclusion :

La carte de flux de travail **Comparer avec le bon de commande – Date de livraison promise pour les articles** offre un moyen flexible de faire respecter les règles de date de livraison. En combinant les opérateurs avec une gestion de la tolérance tenant compte des jours de la semaine, elle permet une validation précise des engagements de livraison tout en réduisant les vérifications manuelles et les exceptions.
