# Any / All Quantity

<figure><img src="../../../../.gitbook/assets/image (269).png" alt="" width="563"><figcaption></figcaption></figure>

<figure><img src="../../../../.gitbook/assets/image (270).png" alt="" width="563"><figcaption></figcaption></figure>

## **Objectif :**

Cette carte de workflow est conçue pour comparer la quantité d'un document à la tolérance définie dans le bon de commande. Elle permet aux utilisateurs d'évaluer si la quantité satisfait certaines conditions, telles que l'égalité ou le dépassement de la tolérance spécifiée. Dans la Version 4, la carte étend ses fonctionnalités en ajoutant la possibilité de comparer plusieurs entités, notamment le bon de commande, les quantités reçues et les quantités du document, offrant une plus grande flexibilité dans la gestion de différents scénarios.

## **Composants de la carte :**

1. **Any / All :**
   * **Description** : spécifie comment la comparaison doit être appliquée à plusieurs éléments ou conditions.
   * **Options** :
     * **Any** : au moins une des conditions doit être vraie pour que l'action soit déclenchée.
     * **All** : toutes les conditions doivent être vraies pour que l'action se poursuive.
2. **Operator :**
   * **Description** : définit la condition qui sera appliquée pour comparer la quantité du document à la tolérance spécifiée.
   * **Options** :
     * **Equals (=)** : vérifie si la quantité correspond à la valeur de tolérance spécifiée.
     * **Not Equals (≠)** : s'assure que la quantité diffère de la valeur de tolérance spécifiée.
     * **Greater Than (>)** : vérifie si la quantité est supérieure à la tolérance spécifiée.
     * **Greater or Equals (≥)** : vérifie si la quantité est supérieure ou égale à la tolérance spécifiée.
     * **Lesser Than (<)** : vérifie si la quantité est inférieure à la tolérance spécifiée.
     * **Lesser or Equals (≤)** : vérifie si la quantité est inférieure ou égale à la tolérance spécifiée.
3. **Tolerance Amount :**
   * **Description** : spécifie la valeur de tolérance à laquelle la quantité du document sera comparée.
   * **Détail** : cette valeur est numérique et représente le seuil d'écart autorisé sur la quantité.
4. **Tolerance Type :**
   * **Description** : définit le type de tolérance qui sera appliqué.
   * **Options** :
     * **Percentage** : la tolérance est calculée en pourcentage de la quantité du bon de commande.
     * **Value** : la tolérance est spécifiée sous forme de valeur numérique fixe.

## **Composants supplémentaires dans la Version 4 :**

* **Comparison Type** : sélectionne les entités à comparer, offrant plus de flexibilité dans la manière dont les quantités sont évaluées en Version 4.
  * **Purchase Order to Document** : compare la quantité du bon de commande à la quantité du document associé.
  * **Received to Document** : compare la quantité reçue à la quantité du document.
  * **Purchase Order to Received** : compare la quantité du bon de commande à la quantité reçue.

## **Fonctionnalité :**

* **Évaluation de la condition :** le système compare la quantité du document à la tolérance du bon de commande en fonction de l'opérateur sélectionné et du montant/type de tolérance. Dans la Version 4, le **Comparison Type** permet de comparer différentes quantités, comme bon de commande vers reçu, ou bon de commande vers document, offrant une comparaison plus dynamique.
* **Exécution de l'action :**
  * **Condition vraie** : si la comparaison renvoie vrai (par ex. la quantité du document se situe dans la plage de tolérance acceptable), le workflow se poursuit.
  * **Condition fausse** : si la comparaison renvoie faux (par ex. la quantité ne respecte pas la tolérance), le workflow ne se poursuit pas.

## **Mise en place et configuration :**

**Version 3 :**

* Les utilisateurs configurent la carte en sélectionnant la quantité du document, en définissant le montant et le type de tolérance, et en choisissant l'opérateur approprié pour comparer la quantité à la tolérance. La carte évalue si la quantité se situe dans le seuil de tolérance et poursuit avec l'action « True » ou « False » selon le résultat.

**Version 4 :**

* En plus de la configuration de la Version 3, les utilisateurs peuvent sélectionner le **Comparison Type**, permettant des comparaisons entre différentes entités, telles que :
  * **Purchase Order to Document**
  * **Received to Document**
  * **Purchase Order to Received**

## **Scénario d'exemple :**

Une facture indique que 100 unités ont été livrées, mais le bon de commande n'autorisait que 90 unités. Le montant de tolérance est fixé à 10 unités et le type de tolérance est absolu.

* **Version 3** : la carte compare les 100 unités du document à la tolérance du bon de commande de 90 unités. Si la quantité dépasse la tolérance, la carte signale l'écart pour un examen complémentaire.
* **Version 4** : la carte pourrait comparer la **quantité du bon de commande** (90 unités) à la **quantité reçue** (100 unités) ou à la **quantité du document** (100 unités). Selon le **Comparison Type** sélectionné, elle vérifie si l'écart entre les deux entités dépasse la tolérance et déclenche l'action correspondante.

## **Conclusion :**

* **Version 3** : cette carte de workflow compare la quantité du document à la tolérance du bon de commande, contribuant à garantir que les écarts de quantité sont signalés et traités de manière appropriée.
* **Version 4** : étend cette fonctionnalité en permettant aux utilisateurs de comparer différentes entités, telles que bon de commande vers reçu ou bon de commande vers document, offrant une plus grande flexibilité dans la gestion de scénarios plus complexes. La Version 4 assure un contrôle plus strict des workflows d'approvisionnement et de réception, offrant des comparaisons et des actions plus dynamiques selon le type de comparaison choisi.
