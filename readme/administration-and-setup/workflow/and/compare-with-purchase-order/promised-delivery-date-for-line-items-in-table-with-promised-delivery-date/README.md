# Date de livraison promise pour les lignes d'un tableau avec date de livraison promise

<figure><img src="../../../../../.gitbook/assets/image (3).png" alt="" width="375"><figcaption></figcaption></figure>

## Objectif :

Cette carte de workflow est conçue pour valider la **date de livraison promise des lignes** par rapport à la **date de livraison promise sur le bon de commande**, à l'aide d'opérateurs de comparaison et de règles de tolérance configurables. Elle permet aux workflows de détecter automatiquement les dates de livraison conformes, anticipées ou tardives, et de réagir en conséquence.

## Composants de la carte :

1. **Operator**
   * **Description :**\
     Définit comment la date de livraison promise de la ligne est comparée à la date de livraison promise du bon de commande.
   * **Options :**
     * **Equals (=) :** la date de la ligne doit se situer à l'intérieur de la fenêtre de tolérance.
     * **Not Equals (≠) :** la date de la ligne doit se situer en dehors de la fenêtre de tolérance.
     * **Greater Than (>) :** la date de la ligne doit être postérieure à la fenêtre de tolérance.
     * **Greater or Equals (≥) :** la date de la ligne doit être égale ou postérieure au début de la fenêtre de tolérance.
     * **Lesser Than (<) :** la date de la ligne doit être antérieure à la fenêtre de tolérance.
     * **Lesser or Equals (≤) :** la date de la ligne doit être égale ou antérieure à la fin de la fenêtre de tolérance.<br>
2. **Tolerance Days**
   * **Description :**\
     Spécifie le nombre de jours utilisé pour calculer la fenêtre de tolérance acceptable autour de la date de livraison promise du bon de commande.
   * **Détail :**\
     Cette valeur est un entier et définit combien de jours avant et après la date du bon de commande sont pris en compte lors de la validation.<br>
3. **Allowed Tolerance Days**
   * **Description :**\
     Définit quels jours de la semaine sont comptabilisés lors du calcul des jours de tolérance.
   * **Détail :**\
     Les utilisateurs peuvent sélectionner des jours de semaine précis (par exemple, du lundi au vendredi). Seuls les jours sélectionnés sont inclus dans le calcul de la fenêtre de tolérance.

### Fonctionnalité :

* **Évaluation de la condition :** le système calcule une fenêtre de tolérance autour de la date de livraison promise du bon de commande en fonction des **Tolerance Days** et des **Allowed Tolerance Days** configurés.\
  La date de livraison promise de chaque ligne est ensuite comparée à cette fenêtre à l'aide de l'opérateur sélectionné.
* Exécution de l'action :
  * **Condition vraie :** si l'écart de date de livraison se situe dans la plage de tolérance et correspond à la condition définie par l'opérateur, le workflow se poursuit.
  * **Condition fausse :** si la condition n'est pas remplie, le workflow ne se poursuit pas.

### Mise en place et configuration :

* Sélectionnez l'opérateur de comparaison approprié.
* Saisissez le nombre de jours de tolérance.
* Choisissez quels jours de la semaine doivent être comptabilisés comme jours de tolérance.

### Conclusion :

La carte de workflow **Compare with Purchase Order – Promised Delivery Date for Line Items** offre un moyen flexible d'appliquer des règles de date de livraison. En combinant des opérateurs avec une gestion de la tolérance tenant compte des jours de la semaine, elle permet une validation précise des engagements de livraison tout en réduisant les contrôles manuels et les exceptions.
