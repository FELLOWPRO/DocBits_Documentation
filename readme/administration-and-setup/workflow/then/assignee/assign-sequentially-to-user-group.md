# Assign Sequentially to User/Group

<figure><img src="../../../../.gitbook/assets/image (11) (1) (2).png" alt="" width="563"><figcaption></figcaption></figure>

## **Objectif**

La carte de workflow « **Assign the Document Sequentially to User/Group Based on Decision Table** » assigne dynamiquement des documents soit à un utilisateur, soit à un groupe, selon l'évaluation de la table de décision. Cela garantit que les documents sont acheminés de manière appropriée en fonction de règles prédéfinies.

## **Composants de la carte**

1. **Priority (Value)**
   * **Description** : spécifie le niveau de priorité des attributions, où les nombres les plus faibles représentent la priorité la plus élevée.
   * **Détail** : un champ de saisie numérique où la valeur de priorité peut être définie pour contrôler la séquence d'attribution.

## **Fonctionnalité**

* **Évaluation de la table de décision** :\
  La table de décision évalue des conditions prédéfinies pour décider si le document est assigné à un utilisateur ou à un groupe.
* **Attribution du document** :
  * Si la table de décision renvoie un utilisateur, le document est assigné directement à cet utilisateur.
  * Si la table de décision renvoie un groupe, le document est assigné au groupe de manière séquentielle, en respectant la valeur de priorité spécifiée.

## **Mise en place et configuration**

1. Ajoutez la carte **Assign the Document Sequentially** à votre workflow.
2. Configurez le champ **Priority (Value)** :
   * Saisissez une valeur numérique pour définir la priorité d'attribution.
3. Enregistrez et activez le workflow pour appliquer la configuration.

## **Conclusion**

La carte de workflow « **Assign the Document Sequentially to User/Group Based on Decision Table** » garantit un acheminement efficace et dynamique des documents. En s'appuyant sur la logique de la table de décision et les valeurs de priorité, la carte facilite une attribution précise soit à un utilisateur, soit à un groupe, rationalisant les workflows documentaires.
