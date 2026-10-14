# Journaux de flux de travail

## **Aperçu**

Les **Journaux de flux de travail** permettent aux utilisateurs d'analyser quels flux de travail ont été exécutés pour un document, de comprendre les résultats de l'exécution et d'approfondir les détails au niveau des conditions pour le débogage ou la validation.

## **Accès aux journaux de flux de travail**

Pour accéder aux journaux de flux de travail :

1. Naviguez jusqu'au **Tableau de bord**.
2. Cliquez sur le **menu Actions** (icône à trois points) à côté du document souhaité.
3. Sélectionnez **Journaux de flux de travail** dans le menu.
   * <mark style="color:red;">**Remarque**</mark>**&#x20;:** La fonctionnalité de workflow doit être activée pour accéder à cette option.
4.  Un **panneau latéral** s'ouvre montrant un résumé des flux de travail exécutés.

    ![](https://docs.docbits.com/~gitbook/image?url=https%3A%2F%2F578966019-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FT2n2w4uDCJvv7CJ5zrdk%252Fuploads%252FAlgg3jnSVRVyuYxy4tAp%252Fimage.png%3Falt%3Dmedia%26token%3D4e8fcd63-6113-47eb-95a4-95a7821dc9b9\&width=768\&dpr=4\&quality=100\&sign=9e6ba9f5\&sv=2)

## **Composants du panneau des journaux de flux de travail**

#### **1. Compteurs de résumé de flux de travail**

Situation en haut du panneau des journaux :

* **Bleu** : Nombre total de flux de travail exécutés.
* **Rouge** : Flux de travail ayant abouti à des **erreurs**.
* **Jaune** : Flux de travail qui n'ont pas été **terminés** en raison de divergences de conditions.
* **Vert** : Flux de travail exécutés avec succès.

#### **2. Tableau d'exécution de flux de travail**

Chaque ligne dans le tableau représente une exécution de flux de travail et inclut :

* **Nom du flux de travail**
* **Horodatage** (Créé le)
* **Durée d'exécution** (en secondes)
* **Icône de résultat**:
  * Coche verte : Le flux de travail a été exécuté avec succès.
  * Croix rouge : Le flux de travail a été exécuté avec une erreur.
  * Tiret orange : L'exécution a été arrêtée en raison d'une condition non satisfaite.

En cliquant sur la **flèche** à gauche de chaque ligne, vous pouvez développer la **vue détaillée du flux de travail**.

<div align="left"><figure><img src="../../.gitbook/assets/workflow_test9_match_check_overview.png" alt="" width="563"><figcaption></figcaption></figure></div>

### **Vue détaillée du flux de travail**

En cliquant sur une ligne de flux de travail spécifique, vous ouvrez son **journal d'exécution détaillé**, montrant :

#### **Évaluation des conditions**

* Bloc **Quand...** : Condition initiale.
* Bloc(s) **Et...** : Conditions supplémentaires.
* Bloc(s) **Alors...** : Actions effectuées lorsque toutes les conditions sont remplies.

Chaque ligne de condition montre :

* Coche **verte** : Condition remplie.
* Tiret **orange** : Condition non remplie.
* Croix **rouge** : La condition a échoué **en raison d'une erreur**

### **Note de comportement importante**

Si une condition dans un flux de travail n'est **pas remplie**, le système **arrête d'évaluer d'autres cartes de flux de travail** dans ce flux de travail. Ce comportement évite un traitement inutile. En tant qu'indicateur visuel, la carte qui **n'a pas rempli sa condition** est affichée en **gris**, et toutes les **cartes suivantes** dans le même flux de travail apparaîtront également en **gris**, indiquant qu'elles n'ont pas été **exécutées**.
