# Exécuter le flux de travail

<figure><img src="../../../../.gitbook/assets/workflow_card_run_workflow_v1-fr-fr.png" alt="Exécuter le flux de travail, Version 1" width="634"><figcaption><p>Version 1</p></figcaption></figure>

<figure><img src="../../../../.gitbook/assets/workflow_card_run_workflow_v2-fr-fr.png" alt="Exécuter le flux de travail, Version 2" width="634"><figcaption><p>Version 2</p></figcaption></figure>

## Objectif :

La carte **« Exécuter le workflow »** permet aux utilisateurs d'exécuter dynamiquement un workflow sélectionné parmi une liste de workflows disponibles. Cette carte est utile pour automatiser des processus où plusieurs workflows sont interconnectés, permettant des opérations rationalisées.

## Composants de la carte :

1. **Flux de travail**
   * **Descriptif :** spécifie le workflow à exécuter lorsque les conditions sont évaluées comme vraies.
   * **Détail :** une liste déroulante de tous les workflows disponibles est proposée pour la sélection.

## Fonctionnalité :

* **Évaluation de la condition :** la carte n'exécute le workflow sélectionné que si les sections **« Quand »** et **« Et »** sont toutes deux évaluées comme vraies.
  * Si l'une des conditions est fausse, aucune action n'est effectuée et le workflow reste non déclenché.
* **Exécution du workflow :**
  * Lorsque les conditions sont satisfaites, le workflow spécifié est déclenché automatiquement.
  * Si les conditions ne sont pas satisfaites, aucun workflow n'est exécuté.

## Mise en place et configuration :

1. **Sélectionnez le workflow :** choisissez le workflow à déclencher dans la **liste déroulante** des workflows disponibles.
2. **Définir les conditions :** configurez les sections **« Quand »** et **« Et »** pour spécifier les critères à satisfaire pour que le workflow s'exécute.

## Conclusion :

La carte **« Exécuter le workflow »** offre un moyen pratique et efficace de relier des workflows, automatisant facilement des processus à plusieurs étapes. En garantissant que les conditions des sections **« Quand »** et **« Et »** sont satisfaites, les utilisateurs peuvent exécuter des workflows de manière dynamique et réduire l'intervention manuelle.

<!-- workflow-card-practical-example-20261021 -->

## Exemple pratique

**Quand utiliser :** Réutiliser un workflow de validation existant.

**Configuration :** Sélectionnez un flux de travail enfant de démonstration configuré qui définit `routing_result` sur `checked`.

**Résultat attendu et contre-exemple :** Le workflow sélectionné est invoqué dans son contexte d'exécution pris en charge. Vérifier son propre journal et son résultat de champ ; ne le reliez pas au parent dans une boucle.

Il s’agit d’une configuration illustrative et du résultat attendu. Utilisez les champs, utilisateurs et groupes configurés dans votre organisation de test ; cela ne veut pas dire que cet exemple a été exécuté.
