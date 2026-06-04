# Tax in document field

<figure><img src="../../../../.gitbook/assets/image (268).png" alt="" width="563"><figcaption></figcaption></figure>

## **Objectif :**

Cette carte de workflow est conçue pour évaluer si la valeur de taxe d'un champ de document correspond à la valeur de taxe d'un bon de commande, en tenant compte des tolérances basées sur le charge ID. La carte compare ces deux valeurs de taxe (l'une issue du champ de document, l'autre du bon de commande) et vérifie si elles satisfont une condition spécifiée (par ex. égal, supérieur, inférieur, etc.). Cela aide à garantir la cohérence des valeurs de taxe et à signaler les écarts pour examen ou approbation complémentaire dans les workflows d'approvisionnement.

## **Composants de la carte :**

1. **Field Name**
   * **Description** : spécifie le champ de document qui contient la valeur de taxe à comparer à la valeur de taxe du bon de commande.
   * **Détail** : ce champ doit correspondre à l'identifiant exact de la valeur de taxe dans le document.
2. **Operator**
   * **Description** : définit la condition à appliquer à la comparaison entre la valeur de taxe du document et la valeur de taxe du bon de commande.
   * **Options** :
     * **Equals (=)** : vérifie si la taxe du champ de document correspond à la taxe du bon de commande.
     * **Not Equals (≠)** : s'assure que la taxe du champ de document ne correspond pas à la taxe du bon de commande.
     * **Greater Than (>)** : vérifie si la taxe du champ de document est supérieure à la taxe du bon de commande.
     * **Greater or Equals (≥)** : vérifie si la taxe du champ de document est supérieure ou égale à la taxe du bon de commande.
     * **Lesser Than (<)** : vérifie si la taxe du champ de document est inférieure à la taxe du bon de commande.
     * **Lesser or Equals (≤)** : vérifie si la taxe du champ de document est inférieure ou égale à la taxe du bon de commande.
3. **Master Data Table**
   * **Description** : la table qui contient les détails du bon de commande, y compris le charge ID et les valeurs de taxe.
   * **Détail** : cette table doit comporter une référence au charge ID associé à la valeur de taxe du bon de commande.
4. **Tolerance Amount**
   * **Description** : le montant seuil dans lequel les valeurs de taxe peuvent varier. Il sert à tenir compte des écarts mineurs dans les calculs de taxe.
   * **Détail** : le montant de tolérance doit être une valeur numérique, définissant l'écart maximal autorisé entre les valeurs de taxe.
5. **Tolerance Type**
   * **Description** : spécifie le type de tolérance appliqué, absolu ou en pourcentage.
   * **Options** :
     * **Value** : la tolérance est une valeur numérique fixe.
     * **Percentage** : la tolérance est calculée en pourcentage de la valeur de taxe.

## **Fonctionnalité :**

* **Évaluation de la condition :** le système évalue si la valeur de taxe du champ de document satisfait la condition spécifiée lorsqu'elle est comparée à la valeur de taxe du bon de commande (avec la référence au charge ID issue de la Master Data Table). Le montant et le type de tolérance sont pris en compte dans cette évaluation pour autoriser des écarts mineurs dans les calculs de taxe.
* **Exécution de l'action :**
  * **Condition vraie** : si la taxe du champ de document satisfait la condition lorsqu'elle est comparée à la taxe du bon de commande (dans le montant et le type de tolérance), le workflow se poursuit.
  * **Condition fausse** : si la taxe du champ de document ne satisfait pas la condition (soit hors de la plage de tolérance, soit la comparaison échoue), le workflow s'arrête.

## **Mise en place et configuration :**

* Les utilisateurs doivent sélectionner le champ de document qui contient la valeur de taxe à comparer. Ils choisiront ensuite l'opérateur définissant la manière de réaliser la comparaison (par ex. égal, supérieur). Ils doivent ensuite spécifier la référence à la Master Data Table et définir le montant et le type de tolérance pour tenir compte des écarts mineurs de taxe.

## **Scénario d'exemple :**

* Une facture indique un montant de taxe de 100 $. Le bon de commande correspondant, présent dans la Master Data Table, spécifie une valeur de taxe de 95 $. À l'aide de l'opérateur « Greater Than », le système compare la valeur de taxe du document (100 $) à la valeur de taxe du bon de commande (95 $) avec une tolérance de 10 $ (type de tolérance absolu). Puisque l'écart de 5 $ se situe dans la plage de tolérance, le workflow se poursuit sans déclencher d'alertes.

## **Conclusion :**

La carte de workflow « Tax in Document Field Comparison » garantit que les valeurs de taxe des documents sont alignées sur les détails des bons de commande, en autorisant des écarts mineurs selon les tolérances spécifiées. En automatisant cette vérification, les organisations peuvent réduire les erreurs dans les calculs de taxe et rationaliser les processus d'approvisionnement, diminuant le besoin d'interventions ou d'approbations manuelles.
