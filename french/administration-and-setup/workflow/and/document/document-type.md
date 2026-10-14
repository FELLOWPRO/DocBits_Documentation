# Document Type

<figure><img src="../../../../.gitbook/assets/image (16) (1).png" alt="" width="563"><figcaption></figcaption></figure>

## Objectif :

Cette carte de workflow est conçue pour évaluer si un document correspond à un type spécifique. En vérifiant si le document correspond au type donné, les workflows peuvent se poursuivre ou effectuer des actions alternatives en fonction de cette condition. Cela aide à automatiser les processus où le type de document dicte les étapes suivantes du workflow.

## Composants de la carte :

1. **Operator**
   * **Description** : définit si le document doit ou non être du type spécifié.
   * **Options** :
     * **Is** : le document doit correspondre au type spécifié pour que la condition soit vraie.
     * **Is Not** : le document ne doit pas correspondre au type spécifié pour que la condition soit vraie.
2. **Type**
   * **Description** : spécifie le type de document à comparer.
   * **Détail** : il inclut divers types de documents tels que « Invoice », « Purchase Order », etc., en fonction desquels la condition (is/is not) sera évaluée.

## Fonctionnalité :

* **Évaluation de la condition** : le système évalue si le type de document du champ spécifié satisfait la condition définie par l'opérateur. Il compare la valeur du champ au type de document fourni.
* **Exécution de l'action** :
  * **Condition vraie** : si le type de document correspond au type spécifié (ou non, selon l'opérateur), le workflow se poursuit avec la condition vraie. Cela peut déclencher des actions telles que le traitement complémentaire du document, son envoi pour approbation ou l'application de règles spécifiques en fonction du type de document.
  * **Condition fausse** : si le type de document ne correspond pas au type spécifié, le workflow se poursuit avec la condition fausse. Cela peut déclencher des actions alternatives, comme l'acheminement du document vers un processus différent ou l'arrêt des actions ultérieures.

## Mise en place et configuration :

* Les utilisateurs configurent la carte en sélectionnant le champ de document qui contient le type de document dans une liste de champs disponibles. Ensuite, l'opérateur est sélectionné pour définir si le document doit ou non être du type spécifié. Enfin, les utilisateurs définissent la condition de poursuite (vraie ou fausse), qui détermine l'action suivante en fonction du type de document.

## Conclusion :

La carte de workflow « Document Type Comparison » est essentielle pour garantir que les workflows se poursuivent en fonction du type de document traité. En comparant le type de document, elle aide les organisations à automatiser les tâches d'acheminement et de traitement des documents, garantissant que les documents sont traités de manière appropriée selon leur type.
