# Run Workflow

<figure><img src="../../../../.gitbook/assets/image (307).png" alt="" width="563"><figcaption></figcaption></figure>

## Objectif :

La carte **« Run Workflow »** permet aux utilisateurs d'exécuter dynamiquement un workflow sélectionné parmi une liste de workflows disponibles. Cette carte est utile pour automatiser des processus où plusieurs workflows sont interconnectés, permettant des opérations rationalisées.

## Composants de la carte :

1. **Workflow**
   * **Description :** spécifie le workflow à exécuter lorsque les conditions sont évaluées comme vraies.
   * **Détail :** une liste déroulante de tous les workflows disponibles est proposée pour la sélection.

## Fonctionnalité :

* **Évaluation de la condition :** la carte n'exécute le workflow sélectionné que si les sections **« Where »** et **« And »** sont toutes deux évaluées comme vraies.
  * Si l'une des conditions est fausse, aucune action n'est effectuée et le workflow reste non déclenché.
* **Exécution du workflow :**
  * Lorsque les conditions sont satisfaites, le workflow spécifié est déclenché automatiquement.
  * Si les conditions ne sont pas satisfaites, aucun workflow n'est exécuté.

## Mise en place et configuration :

1. **Sélectionner le workflow :** choisissez le workflow à déclencher dans la **liste déroulante** des workflows disponibles.
2. **Définir les conditions :** configurez les sections **« Where »** et **« And »** pour spécifier les critères à satisfaire pour que le workflow s'exécute.

## Conclusion :

La carte **« Run Workflow »** offre un moyen pratique et efficace de relier des workflows, automatisant facilement des processus à plusieurs étapes. En garantissant que les conditions des sections **« Where »** et **« And »** sont satisfaites, les utilisateurs peuvent exécuter des workflows de manière dynamique et réduire l'intervention manuelle.
