# AI Calculation for Cost Increase Surcharges

<figure><img src="../../../../.gitbook/assets/image (309).png" alt="" width="563"><figcaption></figcaption></figure>

## Objectif :

La carte de workflow **« AI Calculation for Cost Increase Surcharges »** utilise l'IA pour calculer automatiquement les montants de surcharge en fonction des augmentations de coûts. Elle garantit des calculs de surcharge cohérents et précis, rationalisant les workflows et réduisant l'effort manuel.

## Composants de la carte :

* **Cost Increase Factor**
  * **Description :** le multiplicateur ou le pourcentage appliqué au coût de base pour calculer la surcharge.
  * **Détail :** détermine le montant de la surcharge en fonction de l'augmentation de coût (par ex. un facteur de 1,10 pour une augmentation de 10 %).
* **Base Cost Field**
  * **Description :** le champ contenant la valeur de coût d'origine utilisée comme base du calcul de la surcharge.
  * **Détail :** sélectionné automatiquement ou défini au sein du workflow pour référence lors du calcul.
* **Surcharge Field**
  * **Description :** le champ où la valeur de surcharge calculée par l'IA est stockée.
  * **Détail :** ce champ reflète la surcharge calculée, la rendant disponible pour un traitement ou un reporting complémentaire.

## Fonctionnalité :

**Évaluation de la condition :**

* La carte ne s'active que si les conditions des sections **« Where »** et **« And »** sont toutes deux évaluées comme vraies.
* Si l'une des conditions est évaluée comme fausse, aucun calcul de surcharge n'est effectué.

**Calcul piloté par l'IA :**

* Le système applique le **Cost Increase Factor** au **Base Cost Field** pour calculer la surcharge.
* Le résultat est stocké dans le **Surcharge Field**, garantissant son accessibilité pour les étapes ultérieures du workflow.

## Conclusion :

La carte de workflow **« AI Calculation for Cost Increase Surcharges »** automatise l'application des surcharges en fonction des augmentations de coûts. En s'appuyant sur l'IA pour la précision et la cohérence, cette carte élimine les calculs manuels, améliore l'efficacité et facilite une gestion précise des coûts dans les workflows automatisés.
