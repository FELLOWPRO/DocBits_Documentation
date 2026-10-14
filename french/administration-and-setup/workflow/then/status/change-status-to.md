# Change Status to

<figure><img src="../../../../.gitbook/assets/image (283).png" alt="" width="563"><figcaption></figcaption></figure>

## **Objectif :**

La carte de workflow **« Change Status »** sert à changer le statut d'un document en l'un des états prédéfinis — **Error, Rejected, Ready for Validation, Pending Approval, Pending Second Approval** — et, en option, à déclencher des workflows associés en fonction du changement de statut. Cette carte automatise le processus de mise à jour des statuts et de déclenchement de workflows, garantissant une gestion efficace des documents et une bonne gestion des erreurs.

## **Composants de la carte :**

1. **Status**
   * **Description** : spécifie le nouveau statut à appliquer au document.
   * **Options** :
     * **Error** : marque le document comme ayant rencontré une erreur.
     * **Rejected** : indique que le document a été rejeté et ne poursuivra pas.
     * **Ready for Validation** : place le document en attente d'examen et de validation par l'utilisateur ou le processus système suivant.
     * **Pending Approval** : place le document dans un état d'attente d'approbation.
     * **Pending Second Approval** : met le document en attente d'un second niveau d'approbation, le cas échéant.
2. **Trigger Workflows**
   * **Description** : détermine si des workflows ultérieurs doivent être déclenchés après le changement de statut.
   * **Options** :
     * **True** : lance tous les workflows pertinents en fonction du changement de statut.
     * **False** : empêche l'exécution de workflows après le changement de statut.

## **Fonctionnalité :**

* **Évaluation de la condition** : le système évalue les conditions définies dans les sections **« Where »** et **« And »**. Si ces conditions sont vraies, la carte procède au changement du statut du document vers la valeur sélectionnée.
* **Mise à jour du statut** : une fois les conditions satisfaites, le statut du document est mis à jour vers l'une des options prédéfinies (Error, Rejected, Ready for Validation, Pending Approval, Pending Second Approval), selon la sélection de l'utilisateur.
* **Action de déclenchement de workflow** : si **Trigger Workflows** est défini sur **True**, le système lance automatiquement tous les workflows associés à la suite de la mise à jour du statut. S'il est défini sur **False**, aucun workflow supplémentaire n'est déclenché et le processus se termine avec le changement de statut.

## **Mise en place et configuration :**

Pour configurer cette carte, les utilisateurs doivent :

1. Spécifier le **Status** souhaité sur lequel le document sera défini lors de l'évaluation de la condition (Error, Rejected, Ready for Validation, Pending Approval ou Pending Second Approval).
2. Choisir de **Trigger Workflows** après le changement de statut en sélectionnant **True** ou **False**.
3. La carte n'exécute son action que si les deux conditions des sections **« Where »** et **« And »** sont évaluées comme vraies.

## **Conclusion :**

La carte de workflow **« Change Status »** offre une approche rationalisée pour gérer les statuts des documents et déclencher les workflows associés. Elle garantit que les documents sont automatiquement acheminés vers le bon statut et que les actions nécessaires sont effectuées, selon le changement de statut. En définissant des conditions d'exécution claires, elle réduit l'effort manuel et améliore l'efficacité du workflow.
