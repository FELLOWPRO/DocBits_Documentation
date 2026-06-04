# Assign Sequentially to User

<figure><img src="../../../../.gitbook/assets/image (9) (1) (2).png" alt="" width="563"><figcaption></figcaption></figure>

## **Objectif**

La carte de workflow « **Assign Sequentially to User** » automatise l'attribution de documents à un utilisateur sélectionné de manière séquentielle. La valeur de priorité détermine l'ordre d'attribution, les nombres les plus faibles représentant la priorité la plus élevée.

## **Composants de la carte**

1. **User**
   * **Description** : l'utilisateur sélectionné se verra attribuer le document en fonction de la séquence du workflow.
   * **Détail** : un menu déroulant qui répertorie tous les utilisateurs disponibles pour l'attribution.
2. **Priority (Value)**
   * **Description** : un champ de saisie numérique où le niveau de priorité de l'utilisateur peut être défini.
   * **Détail** : les nombres les plus faibles indiquent une priorité plus élevée. Les documents sont attribués aux utilisateurs par ordre croissant de priorité.

## **Fonctionnalité**

* **Attribution du document** :\
  La carte attribue les documents à l'utilisateur sélectionné de manière séquentielle, en tenant compte du niveau de priorité.\
  Si plusieurs utilisateurs ont la même priorité, les documents sont attribués dans l'ordre d'apparition des utilisateurs dans le menu déroulant.

## **Mise en place et configuration**

1. Ajoutez la carte **Assign the Document Sequentially** à votre workflow.
2. Configurez le champ **User** :
   * Sélectionnez un utilisateur dans le menu déroulant.
3. Configurez le champ **Priority (Value)** :
   * Saisissez une valeur numérique pour définir la priorité d'attribution.
4. Enregistrez et activez le workflow pour appliquer la configuration.

## **Conclusion**

La carte de workflow « Assign the Document Sequentially to User » garantit une distribution organisée des documents en les attribuant selon une séquence hiérarchisée. Cela améliore la gestion des tâches et réduit les retards de traitement.
