# Changer le statut en

<figure><img src="../../../../.gitbook/assets/workflow-card-qa-20261021-card-2da4ec250da9-fr.png" alt="Champs de la carte dans la version affichée. Les champs ne sont pas encore renseignés." width="563"><figcaption><p>Champs de la carte dans la version affichée. Les champs ne sont pas encore renseignés.</p></figcaption></figure>

## **Objectif :**

La carte de workflow **« Change Status »** sert à changer le statut d'un document en l'un des états prédéfinis — **Erreur, Rejeté, Prêt pour validation, En attente d'approbation, En attente de deuxième approbation** — et, en option, à déclencher des workflows associés en fonction du changement de statut. Cette carte automatise le processus de mise à jour des statuts et de déclenchement de workflows, garantissant une gestion efficace des documents et une bonne gestion des erreurs.

## **Composants de la carte :**

1. **Statut**
   * **Descriptif** : spécifie le nouveau statut à appliquer au document.
   * **Possibilités** :
     * **Error** : marque le document comme ayant rencontré une erreur.
     * **Rejeté** : indique que le document a été rejeté et ne poursuivra pas.
     * **Prêt pour la validation** : place le document en attente d'examen et de validation par l'utilisateur ou le processus système suivant.
     * **En attente d'approbation** : place le document dans un état d'attente d'approbation.
     * **En attente de deuxième approbation** : met le document en attente d'un second niveau d'approbation, le cas échéant.
2. **Déclencher des workflows**
   * **Descriptif** : détermine si des workflows ultérieurs doivent être déclenchés après le changement de statut.
   * **Possibilités** :
     * **True** : lance tous les workflows pertinents en fonction du changement de statut.
     * **False** : empêche l'exécution de workflows après le changement de statut.

## **Fonctionnalité :**

* **Évaluation de la condition** : le système évalue les conditions définies dans les sections **« Quand »** et **« Et »**. Si ces conditions sont vraies, la carte procède au changement du statut du document vers la valeur sélectionnée.
* **Mise à jour du statut** : une fois les conditions satisfaites, le statut du document est mis à jour vers l'une des options prédéfinies (Error, Rejected, Ready for Validation, Pending Approval, Pending Second Approval), selon la sélection de l'utilisateur.
* **Action de déclenchement de workflow** : si **Déclencher des flux de travail** est défini sur **True**, le système lance automatiquement tous les workflows associés à la suite de la mise à jour du statut. S'il est défini sur **False**, aucun workflow supplémentaire n'est déclenché et le processus se termine avec le changement de statut.

## **Mise en place et configuration :**

Pour configurer cette carte, les utilisateurs doivent :

1. Spécifier le **Statut** souhaité sur lequel le document sera défini lors de l'évaluation de la condition (Error, Rejected, Ready for Validation, Pending Approval ou Pending Second Approval).
2. Choisir de **Déclencher des flux de travail** après le changement de statut en sélectionnant **True** ou **False**.
3. La carte n'exécute son action que si les deux conditions des sections **« Quand »** et **« Et »** sont évaluées comme vraies.

## **Conclusion :**

La carte de workflow **« Change Status »** offre une approche rationalisée pour gérer les statuts des documents et déclencher les workflows associés. Elle garantit que les documents sont automatiquement acheminés vers le bon statut et que les actions nécessaires sont effectuées, selon le changement de statut. En définissant des conditions d'exécution claires, elle réduit l'effort manuel et améliore l'efficacité du workflow.

<!-- workflow-card-practical-example-20261021 -->

## Exemple pratique

**Quand utiliser :** Déplacer un document révisé vers un état de traitement défini.

**Configuration :** Sélectionnez votre statut `Demo Review` configuré et désactivez le déclenchement de workflows supplémentaires pour cet exemple.

**Résultat attendu et contre-exemple :** Le document reçoit le statut sélectionné. Cette action à elle seule n’exécute pas l’exportation configurée séparément.

Il s’agit d’une configuration illustrative et du résultat attendu. Utilisez les champs, utilisateurs et groupes configurés dans votre organisation de test ; cela ne veut pas dire que cet exemple a été exécuté.
