# Decision Table has Returns

<figure><img src="../../../../.gitbook/assets/image (2) (1) (1) (1) (1) (1) (1) (1).png" alt="" width="563"><figcaption></figcaption></figure>

## **Objectif :**

Cette carte DocBits vérifie si une table de décision spécifiée renvoie des valeurs pour un document donné et détermine si les données renvoyées doivent être utilisées dans les étapes ultérieures du workflow. Elle garantit que les workflows peuvent s'adapter dynamiquement en fonction des résultats de la table de décision.

## **Fonctionnalité :**

* **Validation de la table de décision :** cette carte vérifie si la table de décision sélectionnée fournit des valeurs de retour pour le document en cours de traitement.
* **Sélection de la table de décision :** les utilisateurs spécifient le nom de la table de décision à vérifier.
* **Utiliser les données de retour :** les utilisateurs peuvent indiquer s'il faut utiliser les données de retour dans les cartes ultérieures à l'aide d'un paramètre **Boolean** :
  * **True :** les données de retour sont disponibles et seront utilisées dans les étapes ultérieures du workflow.
  * **False :** les données de retour ne seront pas utilisées et le workflow se poursuit sans elles.

## **Utilisation :**

Cette carte est idéale pour les workflows impliquant une logique conditionnelle ou une prise de décision fondée sur des règles prédéfinies dans une table de décision. Elle garantit une intégration fluide des sorties de la table de décision dans les processus de workflow.

## **Scénario d'exemple :**

* Un utilisateur configure la carte pour vérifier les valeurs de retour de la table de décision **« Invoice Processing Rules »**. Le **Boolean** est défini sur **True**, indiquant que les données de retour (par ex. les exigences d'approbation) seront utilisées dans les cartes ultérieures pour guider les décisions du workflow.

En utilisant la carte « Decision Table Check », les organisations peuvent renforcer la flexibilité du workflow, rationaliser le traitement fondé sur des règles et garantir la cohérence de la prise de décision au sein des workflows automatisés.
