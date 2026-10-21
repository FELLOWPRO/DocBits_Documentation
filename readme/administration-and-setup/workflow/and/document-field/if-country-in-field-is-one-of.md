# Si le pays dans le champ est l'un des

<figure><img src="../../../../.gitbook/assets/workflow-card-qa-20261021-card-364a45ddb67d-fr.png" alt="Champs de la carte dans la version affichée. Les champs ne sont pas encore renseignés." width="563"><figcaption><p>Champs de la carte dans la version affichée. Les champs ne sont pas encore renseignés.</p></figcaption></figure>

## **Objectif**

Cette carte de workflow est conçue pour évaluer si un pays spécifié, situé dans un champ désigné, fait partie d'une liste prédéfinie de pays. Selon cette évaluation, le workflow peut se poursuivre avec une condition vraie ou fausse. Elle aide à automatiser les processus où les actions dépendent de l'appartenance ou non du pays à un ensemble de pays autorisés ou restreints.

## **Composants de la carte :**

1. **Nom du champ**
   * **Descriptif :** spécifie le champ de document où le nom ou le code du pays est stocké.
   * **Détail :** il doit correspondre à l'identifiant exact du champ des données de pays dans le document.
2. **Opérateur**
   * **Descriptif :** définit si le pays du champ doit faire partie d'une liste prédéfinie de pays.
   * **Possibilités :**
     * **Is :** le pays doit être inclus dans la liste de pays spécifiée pour que la condition soit vraie.
     * **N'est-ce pas :** le pays ne doit pas être inclus dans la liste de pays spécifiée pour que la condition soit vraie.
3. **Pays**
   * **Descriptif :** spécifie la liste de pays à laquelle le pays sélectionné sera comparé.
   * **Détail :** il s'agit d'une liste de pays séparés par des virgules. La comparaison vérifie si le pays du champ est inclus dans cette liste.
4. **Continuer la condition**
   * **Descriptif :** définit le résultat de la comparaison. Si le pays satisfait la condition, le workflow se poursuit avec la valeur booléenne spécifiée.
   * **Possibilités :**
     * **True :** le workflow se poursuit si la condition correspond.
     * **False :** le workflow se poursuit si la condition ne correspond pas.

## **Fonctionnalité :**

* **Évaluation de la condition :** le système évalue si le pays spécifié dans le champ fait partie de la liste de pays prédéfinie. Cette évaluation vérifie le nom ou le code du pays par rapport à la liste fournie.
* **Exécution de l'action :**
  * **Condition vraie :**\
    Si le pays du champ fait partie de la liste de pays spécifiée, le workflow se poursuit avec la condition vraie. Cela peut déclencher des actions supplémentaires, comme l'acheminement des documents vers le service approprié, l'application de règles de traitement spécifiques ou l'activation de fonctionnalités propres à une région.
  * **Condition fausse :**\
    Si le pays ne correspond pas à la liste, le workflow se poursuit avec la condition fausse. Cela permet d'exécuter des actions alternatives ou d'arrêter le workflow selon la configuration du système.

## **Mise en place et configuration :**

* Les utilisateurs configurent la carte en sélectionnant le champ de document contenant le pays et en spécifiant la liste de pays à vérifier. L'opérateur est ensuite choisi dans une liste déroulante pour définir si le pays doit ou non faire partie de la liste de pays spécifiée. Enfin, les utilisateurs définissent la condition de poursuite (vraie ou fausse), qui dicte l'étape suivante du workflow.

## **Conclusion :**

La carte de workflow « Country in Field Comparison with List » est un outil précieux pour automatiser des actions selon qu'un pays fait partie ou non d'un groupe prédéfini. En comparant les données de pays à une liste de pays autorisés ou restreints, cette carte améliore l'efficacité du workflow et garantit que les processus du système respectent les règles géographiques appropriées.

<!-- workflow-card-practical-example-20261021 -->

## Exemple pratique

**Quand utiliser :** Acheminer les factures de deux pays spécifiés.

**Configuration :** Sélectionnez le champ du pays, l'un des codes de pays `DE` et `FR`, et la suite `true`.

**Résultat attendu et contre-exemple :** `DE` réussit ; `US` ne satisfait pas à la liste des pays sélectionnés.

Il s’agit d’une configuration illustrative et du résultat attendu. Utilisez les champs, utilisateurs et groupes configurés dans votre organisation de test ; cela ne veut pas dire que cet exemple a été exécuté.
