# Comparaison des champs de document

<figure><img src="../../../.gitbook/assets/userlmn_7d5c06ce63181faee30b7bc6903e4d7b.png" alt=""><figcaption></figcaption></figure>

**Objectif**

Cette carte de flux de travail est conçue pour comparer automatiquement les valeurs de deux champs spécifiés dans un document en fonction d'un opérateur défini. Elle est utilisée pour garantir l'intégrité des données et s'assurer que les données du document respectent les règles commerciales ou les conditions.

**Composants de la carte**

1. **Noms des champs**
* **Description** : Spécifie les noms des deux champs dans le document qui seront comparés.
* **Détail** : Les utilisateurs doivent saisir les noms exacts des champs tels qu'ils apparaissent dans le système. Ces champs peuvent être de n'importe quel type de données prenant en charge la comparaison, comme des champs numériques, de date ou de texte.
2. **Opérateur**
* **Description** : L'opérateur de comparaison utilisé pour évaluer la relation entre les valeurs des deux champs.
* **Options** :
* **Égal (==)** : Vérifie si la valeur du premier champ est égale à la valeur du deuxième champ.
* **Non égal (!=)** : Vérifie si la valeur du premier champ n'est pas égale à la valeur du deuxième champ.
* **Supérieur à (>)** : Vérifie si la valeur du premier champ est supérieure à la valeur du deuxième champ.
* **Supérieur ou égal (>=)** : Vérifie si la valeur du premier champ est supérieure ou égale à la valeur du deuxième champ.
* **Inférieur à (<)** : Vérifie si la valeur du premier champ est inférieure à la valeur du deuxième champ.
* **Inférieur ou égal (<=)** : Vérifie si la valeur du premier champ est inférieure ou égale à la valeur du deuxième champ.

**Fonctionnalité**

* **Sélection des champs** : Les utilisateurs saisissent ou sélectionnent les noms des deux champs à comparer. Cela se fait généralement via un formulaire ou un menu déroulant dans la configuration de la carte.
* **Sélection de l'opérateur** : Les utilisateurs choisissent un opérateur dans une liste d'options disponibles qui définit comment les champs doivent être comparés.
* **Exécution de la comparaison** :
* Le système lit les valeurs des champs spécifiés et applique l'opérateur sélectionné pour évaluer la relation entre eux.
* En fonction du résultat de la comparaison (vrai ou faux), des actions ultérieures peuvent être déclenchées. Par exemple, si une comparaison échoue, le système peut signaler le document pour examen, bloquer le traitement ultérieur ou notifier les parties responsables.

**Interactions utilisateur**

* **Configuration et paramétrage** : Les utilisateurs configurent la comparaison en saisissant les noms des champs et en sélectionnant un opérateur. Cette configuration doit être simple et guidée, éventuellement avec du texte d'aide ou des exemples.
* **Surveillance et rapports** : Le système peut fournir des retours sur les résultats des comparaisons, tels que l'enregistrement de toutes les comparaisons effectuées, leurs résultats et les actions prises en réponse aux résultats de la comparaison.
* **Gestion des erreurs et notifications** : Les utilisateurs reçoivent des alertes si la comparaison ne peut pas être exécutée (par exemple, si l'un des champs n'est pas trouvé dans le document ou n'est pas dans un format comparable).

#### Conclusion

La carte de flux de travail "Comparaison des champs de document" est essentielle pour maintenir l'exactitude et la cohérence des données à travers les documents dans un système ERP. Elle aide à automatiser des vérifications qui seraient autrement manuelles, sujettes aux erreurs et chronophages, améliorant ainsi l'efficacité et la fiabilité du traitement des documents. Documenter clairement cette carte dans le manuel de votre système ERP aidera les utilisateurs à utiliser efficacement cette fonctionnalité, garantissant que les données à travers les documents restent cohérentes et conformes aux règles commerciales.
