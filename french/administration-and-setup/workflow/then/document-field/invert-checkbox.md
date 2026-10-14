# Invert Checkbox

<figure><img src="../../../../.gitbook/assets/image (280).png" alt=""><figcaption></figcaption></figure>

## **Objectif :**

Cette carte de workflow est conçue pour inverser l'état actuel d'un champ de type case à cocher. Si la case est cochée (true), elle sera décochée (false), et vice versa. L'inversion se produit en fonction des conditions définies dans les sections **« Where »** et **« And »**. Cette carte aide à automatiser les workflows où une condition nécessite de basculer l'état d'une case à cocher selon des critères spécifiques.

## **Composants de la carte :**

1. **Field Name**
   * **Description** : spécifie le champ de case à cocher à inverser.&#x20;
   * **Détail** : l'état du champ de case à cocher sélectionné sera basculé de true à false ou de false à true en fonction de son état actuel.

## **Fonctionnalité :**

* **Évaluation de la condition** : le système évalue les conditions définies dans les sections **« Where »** et **« And »** :
  * Si **les deux conditions sont vraies**, l'action de la **« Then Section »** s'exécute, ce qui signifie ici que l'état du champ de case à cocher sera basculé.
  * Si **l'une des conditions est fausse**, la carte ne s'exécute pas et aucune modification n'est apportée au champ de case à cocher.
* **Exécution de l'action** : si les conditions des sections **« Where »** et **« And »** sont évaluées comme vraies, l'état du champ de case à cocher sera inversé :
  * Si la case est cochée (true), elle sera décochée (false).
  * Si la case est décochée (false), elle sera cochée (true).

## **Mise en place et configuration :**

Pour configurer cette carte, les utilisateurs doivent :

1. **Sélectionner le champ de case à cocher** (Field Name) qui sera inversé. Les champs de case à cocher disponibles dans le document sont répertoriés pour la sélection.
2. Le champ de case à cocher ne sera inversé que si les conditions des sections **« Where »** et **« And »** sont vraies.

## **Conclusion :**

La carte de workflow **« Invert checkbox \[Field Name] »** offre un outil d'automatisation simple mais puissant pour basculer les valeurs de cases à cocher en fonction de conditions spécifiques. En réduisant le besoin d'ajustements manuels des cases à cocher, cette carte améliore l'efficacité du traitement des documents et garantit la cohérence entre les workflows.
