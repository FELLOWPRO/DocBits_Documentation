# Calculate Columns with

<figure><img src="../../../../.gitbook/assets/image (294).png" alt="" width="563"><figcaption></figcaption></figure>

## **Objectif :**

La carte de workflow **« Calculate Columns in Table »** sert à effectuer des calculs entre les colonnes d'un tableau sélectionné. Elle permet aux utilisateurs de sélectionner des colonnes, d'appliquer une opération mathématique et de stocker le résultat dans une colonne de résultat spécifiée.

## **Composants de la carte :**

1. **Table Name**
   * **Description :** spécifie la **table** dans laquelle les colonnes seront calculées.
   * **Détail :** une liste déroulante de toutes les **tables** disponibles est proposée pour la sélection.
2. **Column Name (1re colonne)**
   * **Description :** spécifie la **première colonne** à impliquer dans le calcul.
   * **Détail :** une liste de toutes les **colonnes** disponibles est proposée pour la sélection.
3. **Operation**
   * **Description :** définit l'opération mathématique à appliquer entre les colonnes sélectionnées.
   * **Options :**
     * **Add (+) :** ajoute la valeur de la seconde colonne à la valeur de la première colonne.
     * **Subtract (-) :** soustrait la valeur de la seconde colonne de la valeur de la première colonne.
     * **Multiply (\*) :** multiplie la valeur de la première colonne par la valeur de la seconde colonne.
     * **Divide (/) :** divise la valeur de la première colonne par la valeur de la seconde colonne.
4. **Column Name (2e colonne)**
   * **Description :** spécifie la **seconde colonne** à impliquer dans le calcul.
   * **Détail :** une liste des **colonnes** disponibles est proposée pour la sélection.
5. **Result Column**
   * **Description :** spécifie la **colonne** où le résultat du calcul sera stocké.
   * **Détail :** une liste des **colonnes** disponibles est proposée, où la valeur calculée sera enregistrée.

## **Fonctionnalité :**

* **Évaluation de la condition :**\
  La carte n'exécute son action que si les sections **« Where »** et **« And »** sont toutes deux évaluées comme vraies.
* **Calcul de colonnes :**\
  La carte effectue l'opération mathématique sélectionnée entre les deux colonnes choisies.
* **Stockage du résultat :**\
  Le résultat du calcul est stocké dans la **colonne de résultat** sélectionnée.

## **Mise en place et configuration :**

* **Sélectionner la table :**\
  Choisissez la **table** où les colonnes seront calculées.
* **Choisir les colonnes :**\
  Sélectionnez la **première colonne** et la **seconde colonne** qui seront utilisées dans le calcul.
* **Sélectionner l'opération :**\
  Choisissez l'opération mathématique (**Add (+)**, **Subtract (-)**, **Multiply (\*)**, **Divide (/)**) à appliquer entre les colonnes.
* **Sélectionner la colonne de résultat :**\
  Choisissez la **colonne de résultat** où le calcul sera stocké.

## **Conclusion :**

La carte de workflow **« Calculate Columns in Table »** permet aux utilisateurs d'effectuer des calculs dynamiques entre les colonnes d'un tableau et de stocker les résultats dans une colonne désignée. La carte offre la flexibilité d'appliquer différentes opérations mathématiques et garantit que le résultat est stocké dans la colonne spécifiée.
