# Set Checkbox to

<figure><img src="../../../../.gitbook/assets/image (279).png" alt="" width="563"><figcaption></figcaption></figure>

## **Objectif :**

Cette carte de workflow est conçue pour définir un champ de type case à cocher sur une valeur spécifiée (true ou false) en fonction des conditions définies dans les sections **« Where »** et **« And »**. Elle offre un moyen simple mais efficace d'automatiser la mise à jour des cases à cocher lorsque certains critères sont satisfaits, garantissant un traitement rationalisé des documents.

## **Composants de la carte :**

1. **Field Name :**
   * **Description** : spécifie le champ où la case à cocher sera définie.
   * **Détail** : le champ de case à cocher à mettre à jour est identifié par le nom du champ.
2. **Boolean**
   * **Description** : définit la valeur sur laquelle le champ de case à cocher sera défini lorsque les conditions des sections **Where** et **And** sont toutes deux vraies.
   * **Options** :
     * **True** : la case sera définie sur **true** si les conditions sont satisfaites.
     * **False** : la case sera définie sur **false** si les conditions sont satisfaites.

## **Fonctionnalité :**

* **Évaluation de la condition** : le système évalue les conditions des sections **« Where »** et **« And »**.&#x20;
* **Exécution de l'action** : si les sections **« Where »** et **« And »** sont toutes deux évaluées comme vraies, le champ de case à cocher sera mis à jour avec la valeur spécifiée (true ou false). Si l'une des conditions est fausse, aucune action n'est effectuée et la case reste dans son état initial.

## **Mise en place et configuration :**

Pour configurer cette carte, les utilisateurs doivent :

1. **Spécifier le champ de case à cocher cible** qui sera défini sur true ou false lorsque les conditions sont satisfaites.
2. **Choisir la valeur (true ou false)** sur laquelle la case sera définie lors de l'évaluation de la condition.
3. La carte n'exécute son action que si les deux conditions des sections **« Where »** et **« And »** sont évaluées comme vraies.

## **Conclusion :**

La carte de workflow **« Set Checkbox »** est un outil d'automatisation simple et efficace pour mettre à jour les champs de case à cocher en fonction de conditions spécifiques. En garantissant que les sections **« Where »** et **« And »** sont toutes deux satisfaites, elle permet aux utilisateurs d'automatiser les processus et de réduire l'intervention manuelle, garantissant un traitement des documents plus fluide et plus efficace.
