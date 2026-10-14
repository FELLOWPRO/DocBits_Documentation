# Change Entries with

<figure><img src="../../../../.gitbook/assets/image (293).png" alt="" width="563"><figcaption></figcaption></figure>

## **Objectif :**

La carte de workflow **« Change Entries in Table »** sert à mettre à jour les entrées d'une table de base de données spécifiée. Elle vous permet de sélectionner une **table** et une **colonne**, puis d'effectuer des opérations mathématiques (addition, soustraction, multiplication ou division) sur les valeurs de cette colonne, à l'aide d'une valeur spécifiée.

## **Composants de la carte :**

1. **Table Name**
   * **Description :** spécifie la **table** dans laquelle les entrées seront mises à jour.
   * **Détail :** une liste déroulante des **tables** disponibles est proposée, vous permettant de sélectionner la table cible pour la mise à jour des entrées.
2. **Column Name**
   * **Description :** spécifie la **colonne** de la table sélectionnée à mettre à jour.
   * **Détail :** une liste de toutes les **colonnes** disponibles sera proposée pour la sélection.
3. **Operation**
   * **Description :** définit l'opération mathématique à effectuer sur les valeurs de la **colonne**.
   * **Options :**
     * **Add (+) :** ajoute une **valeur** spécifiée à la valeur actuelle de la colonne sélectionnée.
     * **Subtract (-) :** soustrait une **valeur** spécifiée de la valeur actuelle de la colonne sélectionnée.
     * **Multiply (\*) :** multiplie la valeur actuelle de la colonne sélectionnée par une **valeur** spécifiée.
     * **Divide (/) :** divise la valeur actuelle de la colonne sélectionnée par une **valeur** spécifiée.
4. **Value**
   * **Description :** spécifie la **valeur** à utiliser dans l'opération sélectionnée.
   * **Détail :** il s'agit du nombre qui sera ajouté, soustrait, multiplié ou divisé avec les entrées de la colonne sélectionnée.

## **Fonctionnalité :**

* **Évaluation de la condition :**\
  La carte n'exécute son action que si les sections **« Where »** et **« And »** sont toutes deux évaluées comme vraies.
* **Mise à jour des entrées de la table :**\
  La carte effectue l'opération sélectionnée (**+**, **-**, **\*** ou **/**) sur les valeurs de la **colonne** choisie de la **table** sélectionnée, à l'aide de la **valeur** spécifiée.

## **Mise en place et configuration :**

* **Sélectionner la table :**\
  Choisissez la **table** où les modifications seront appliquées.
* **Choisir la colonne :**\
  Sélectionnez la **colonne** de la table que vous souhaitez mettre à jour.
* **Sélectionner l'opération :**\
  Choisissez l'opération mathématique (**+**, **-**, **\***, **/**) à appliquer aux valeurs de la colonne sélectionnée.
* **Saisir la valeur :**\
  Fournissez la **valeur** à utiliser dans l'opération sélectionnée.

## **Conclusion :**

La carte de workflow **« Change Entries in Table »** permet des mises à jour automatisées des entrées de base de données en sélectionnant une **table**, une **colonne** et une **opération mathématique** souhaitée. Cette carte est essentielle pour effectuer des modifications de données en masse ou des calculs au sein de votre base de données.
