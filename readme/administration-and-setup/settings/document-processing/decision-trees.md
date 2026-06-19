# Arbres de décision

{% embed url="https://youtu.be/omFWSkSjlL0" %}
Comment créer un arbre de décision dans DocBits (conditions, politiques, test et export)
{% endembed %}

## Vue d'ensemble

Les arbres de décision sont une fonctionnalité puissante qui permet d'automatiser le processus de routage et de prise de décision en s'appuyant sur des règles prédéfinies. Cette fonctionnalité est particulièrement utile dans les environnements complexes où diverses conditions doivent être évaluées pour déterminer la marche à suivre appropriée, comme attribuer des prix, déterminer des quantités ou router des documents.

#### Composants clés

* **Liste des arbres de décision** : il s'agit de l'interface principale dans laquelle tous les arbres de décision existants sont répertoriés. Chaque arbre de décision peut être associé à un type de document spécifique tel qu'une `INVOICE` ou un `QUOTE`.
* **Concepteur d'arbre de décision** : cette interface permet de créer et de modifier des arbres de décision, où vous pouvez définir des règles, des opérateurs et des actions à exécuter lorsque certaines conditions sont remplies.

## Interface des arbres de décision

#### Liste des arbres de décision

La liste des arbres de décision affiche tous les arbres de décision configurés. Ouvrez-la depuis **Settings → Document Processing → Decision Trees**.

<figure><img src="../../../.gitbook/assets/decision_trees.png" alt="Liste des arbres de décision"><figcaption><p>La liste des arbres de décision</p></figcaption></figure>

Chaque entrée affiche :

| Colonne | Description |
|--------|-------------|
| **Name** | Le nom de l'arbre de décision. Cliquez dessus pour ouvrir le concepteur. |
| **Document Type** | Le type de document auquel s'applique l'arbre (par ex. `INVOICE`, `QUOTE`). |
| **Last Modified By** | L'utilisateur ayant modifié l'arbre en dernier. |
| **Last Modified At** | Horodatage de la dernière modification. |
| **Actions** | Menu à trois points pour modifier, copier, exporter ou supprimer l'arbre. |

#### Créer un arbre de décision

1. Cliquez sur **+ Add Decision Tree** dans le coin supérieur droit.
2. Saisissez un **Name** et sélectionnez le **Document Type**.
3. Utilisez le concepteur d'arbre de décision (ci-dessous) pour définir des conditions, des politiques et des résultats.

#### Importer un arbre de décision

Cliquez sur **Import Decision Tree** pour téléverser un fichier d'arbre de décision précédemment exporté (au format JSON). Cela est utile pour copier un arbre d'une organisation ou d'un environnement à un autre.

## Concepteur d'arbre de décision

Le concepteur d'arbre de décision vous permet de configurer les règles qui régissent la manière dont les décisions sont prises.

### **Composants du concepteur d'arbre de décision**

* **Rules** : chaque règle se compose de conditions et d'actions.
* **Select Source** : ce menu déroulant vous permet de spécifier le champ source à évaluer.
* **Select Operator** : définit l'opérateur logique (par ex. `<=`, `>=`, `=`, `!=`) à appliquer au champ source.
* **Result** : définit le résultat ou l'action à exécuter lorsque les conditions sont remplies.
* **Add New Row** : vous permet d'ajouter des règles supplémentaires à l'arbre de décision.

### Exemple de configuration d'un arbre de décision

Cet arbre de décision évalue le champ **Total Amount** et l'attribue à différents groupes selon des conditions prédéfinies. Chaque règle compare le montant total à une valeur spécifique et, selon la condition qui est vraie, le **Group** correspondant est renvoyé.

<figure><img src="../../../.gitbook/assets/decision_tree_example_total_amount.png" alt="Exemple d'arbre de décision Total Amount"><figcaption></figcaption></figure>

Cet arbre de décision évalue deux conditions clés pour déterminer quel groupe doit être attribué : **Total Amount** et **Warehouse Status**. L'arbre utilise des seuils basés sur le montant total pour définir quel groupe est renvoyé, avec la distinction supplémentaire de savoir si l'entrepôt est désigné comme « Warehouse Main », « Warehouse Sub » ou « Not Warehouse Main ».

<figure><img src="../../../.gitbook/assets/decision_tree_example_warehouse_status.png" alt="Exemple d'arbre de décision Warehouse Status"><figcaption></figcaption></figure>

Chaque règle est évaluée de manière séquentielle.

## Politique de l'arbre de décision

La politique de l'arbre de décision définit la manière dont les multiples règles d'un arbre de décision sont traitées. Vous pouvez choisir parmi plusieurs politiques :

### **1. Politique d'unicité (Unique)**

Garantit qu'une seule règle est satisfaite. Si plusieurs règles sont satisfaites, l'arbre de décision renverra « false ».

**Exemple :**

| Règle | Condition            | Groupe renvoyé |
| ---- | -------------------- | ------------ |
| 1    | Total Amount <= 1000 | GROUP_1     |
| 2    | Total Amount <= 2000 | GROUP_2     |
| 3    | Total Amount <= 5000 | GROUP_5     |
| 4    | Total Amount <= 4000 | GROUP_4     |
| 5    | Total Amount <= 3000 | GROUP_3     |

Si le montant total est de **1500**, les règles évaluées seront :

* **Règle 1** : Total Amount <= 1000 (ne correspond pas)
* **Règle 2** : Total Amount <= 2000 (correspond)
* **Règle 3** : Total Amount <= 5000 (correspond)
* **Règle 4** : Total Amount <= 4000 (correspond)
* **Règle 5** : Total Amount <= 3000 (correspond)

Étant donné que plusieurs règles correspondent (**Règle 2**, **Règle 3**, **Règle 4**, **Règle 5**), l'arbre de décision renverra **false**, car la politique **Unique** garantit qu'une seule règle peut correspondre.

### **2. Politique de la première règle (First)**

La première règle correspondante est appliquée et aucune autre règle n'est évaluée.

**Exemple :**

| Règle | Condition            | Groupe renvoyé |
| ---- | -------------------- | ------------ |
| 1    | Total Amount <= 1000 | GROUP_1     |
| 2    | Total Amount <= 2000 | GROUP_2     |
| 3    | Total Amount <= 5000 | GROUP_5     |
| 4    | Total Amount <= 4000 | GROUP_4     |
| 5    | Total Amount <= 3000 | GROUP_3     |

Si le montant total est de **1500**, les règles évaluées seront :

* **Règle 1** : Total Amount <= 1000 (ne correspond pas)
* **Règle 2** : Total Amount <= 2000 (correspond) → L'arbre de décision cesse d'évaluer les règles suivantes et applique **GROUP_2**.

### **3. Politique de priorité (Priority)**

Choisir cette option vous permet de définir des priorités pour chaque règle. Plus le numéro sélectionné est bas, plus la priorité est élevée (c'est-à-dire que la priorité 1 a la priorité la plus élevée). Les règles sont évaluées selon leur ordre de priorité. La règle correspondante ayant la priorité la plus élevée sera appliquée.

**Exemple :**

<table><thead><tr><th width="137">Règle</th><th width="110">Priorité</th><th width="268">Condition</th><th>Groupe renvoyé</th></tr></thead><tbody><tr><td>1</td><td>5</td><td>Total Amount &#x3C;= 1000</td><td>GROUP_1</td></tr><tr><td>2</td><td>4</td><td>Total Amount &#x3C;= 2000</td><td>GROUP_2</td></tr><tr><td>3</td><td>3</td><td>Total Amount &#x3C;= 3000</td><td>GROUP_3</td></tr><tr><td>4</td><td>2</td><td>Total Amount &#x3C;= 4000</td><td>GROUP_4</td></tr><tr><td>5</td><td>1</td><td>Total Amount &#x3C;= 5000</td><td>GROUP_5</td></tr></tbody></table>

Si le montant total est de **1500**, les règles évaluées seront :

* **Règle 1** : Total Amount <= 1000 (ne correspond pas)
* **Règle 2** : Total Amount <= 2000 (correspond)
* **Règle 3** : Total Amount <= 3000 (correspond)
* **Règle 4** : Total Amount <= 4000 (correspond)
* **Règle 5** : Total Amount <= 5000 (correspond)

Étant donné que la priorité est appliquée dans l'ordre **5, 4, 3, 2, 1**, la règle correspondante ayant la priorité la plus élevée sera la **Règle 5** (**GROUP_5**). L'arbre de décision renverra **GROUP_5**, car la **Règle 5** a la priorité la plus élevée (priorité 1).

### **4. Politique de collecte (somme) (Collect (sum))**

Cette politique collecte toutes les règles correspondantes et additionne les résultats. Elle ne fonctionne qu'avec un **Return Type Value**.

**Exemple :**

| Règle | Condition            | Valeur renvoyée |
| ---- | -------------------- | ------------ |
| 1    | Total Amount <= 1000 | 1            |
| 2    | Total Amount <= 2000 | 2            |
| 3    | Total Amount <= 3000 | 3            |
| 4    | Total Amount <= 4000 | 4            |
| 5    | Total Amount <= 5000 | 5            |

Pour la valeur d'entrée **Total Amount = 3500**, l'évaluation des règles serait :

* **Règle 1** : Total Amount <= 1000 (ne correspond pas)
* **Règle 2** : Total Amount <= 2000 (ne correspond pas)
* **Règle 3** : Total Amount <= 3000 (correspond, Return Value = 3)
* **Règle 4** : Total Amount <= 4000 (correspond, Return Value = 4)
* **Règle 5** : Total Amount <= 5000 (correspond, Return Value = 5)

Étant donné que la politique **Collect (sum)** est appliquée, on additionne les **Return Values** des règles correspondantes, à savoir **3, 4, 5**.

**L'addition de ces valeurs** donne :

* 5 + 4 + 3 = **12**

Ainsi, le résultat renvoyé par l'arbre de décision serait **12**, qui est la somme de toutes les valeurs de retour correspondantes.

### **5. Politique de collecte (min/max/count) (Collect (min/max/count))**

Cette politique collecte toutes les règles correspondantes et sélectionne soit le **minimum**, soit le **maximum**, soit **compte** les occurrences. Elle ne fonctionne qu'avec un **Return Type Value**.

**Exemple :**

| Règle | Condition            | Valeur renvoyée |
| ---- | -------------------- | ------------ |
| 1    | Total Amount <= 1000 | 1            |
| 2    | Total Amount <= 2000 | 2            |
| 3    | Total Amount <= 3000 | 3            |
| 4    | Total Amount <= 4000 | 4            |
| 5    | Total Amount <= 5000 | 5            |

1. Si l'option **Collect (min)** est sélectionnée, le résultat renverra le **minimum** des **Return Values** des règles correspondantes.
   * Pour la valeur d'entrée **Total Amount = 3500**, l'évaluation des règles serait :
     * **Règle 1** : Total Amount <= 1000 (ne correspond pas)
     * **Règle 2** : Total Amount <= 2000 (ne correspond pas)
     * **Règle 3** : Total Amount <= 3000 (correspond, Return Value = 3)
     * **Règle 4** : Total Amount <= 4000 (correspond, Return Value = 4)
     * **Règle 5** : Total Amount <= 5000 (correspond, Return Value = 5)
   * Les **règles correspondantes** sont la Règle 3, la Règle 4 et la Règle 5, avec des **Return Values** de **3, 4 et 5**.
   * Étant donné que la politique **Collect (min)** est appliquée, le résultat sera la **valeur minimale**, soit **3**.
   * **Résultat** : **3**
2. Si l'option **Collect (max)** est sélectionnée, le résultat renverra le **maximum** des **Return Values** des règles correspondantes.
   * Pour la même évaluation que ci-dessus, le résultat sera :
   * **Résultat** : **5**
3. Si l'option **Collect (count)** est sélectionnée, le résultat comptera le **nombre de règles correspondantes**.
   * Pour la même évaluation que ci-dessus, le résultat sera :
   * **Résultat** : **3** (puisque 3 règles correspondent).

### **6. Politique d'ordre des règles (Rule Order)**

Cette politique applique les règles dans l'ordre où elles apparaissent dans l'arbre de décision et renvoie le résultat de la règle qui correspond en premier.

**Exemple :**

| Règle | Condition            | Groupe renvoyé |
| ---- | -------------------- | ------------ |
| 1    | Total Amount <= 1000 | GROUP_1     |
| 2    | Total Amount <= 2000 | GROUP_2     |
| 3    | Total Amount <= 3000 | GROUP_3     |
| 4    | Total Amount <= 4000 | GROUP_4     |
| 5    | Total Amount <= 5000 | GROUP_5     |

Étant donné que la valeur d'entrée est **Total Amount = 3500**, l'évaluation des règles serait :

* **Règle 1** : Total Amount <= 1000 (ne correspond pas)
* **Règle 2** : Total Amount <= 2000 (ne correspond pas)
* **Règle 3** : Total Amount <= 3000 (correspond)
* **Règle 4** : Total Amount <= 4000 (correspond)
* **Règle 5** : Total Amount <= 5000 (correspond)

Sous **Rule Order**, l'arbre traitera les règles dans l'ordre où elles sont répertoriées. Ainsi, les règles correspondantes seront :

* **Règle 3** : GROUP_3
* **Règle 4** : GROUP_4
* **Règle 5** : GROUP_5

**Résultat** : **GROUP_3**, **GROUP_4**, **GROUP_5**

### **7. Politique « n'importe laquelle » (Any)**

Plusieurs règles peuvent être vraies, mais le résultat de ces règles doit être identique.

**Exemple :**

| Règle | Condition            | Groupe renvoyé |
| ---- | -------------------- | ------------ |
| 1    | Total Amount <= 1000 | GROUP_1     |
| 2    | Total Amount <= 2000 | GROUP_2     |
| 3    | Total Amount <= 3000 | GROUP_3     |
| 4    | Total Amount <= 4000 | GROUP_4     |
| 5    | Total Amount <= 5000 | GROUP_5     |

Si le montant total est de **2500**, les règles évaluées seront :

* **Règle 1** : Total Amount <= 1000 (ne correspond pas)
* **Règle 2** : Total Amount <= 2000 (ne correspond pas)
* **Règle 3** : Total Amount <= 3000 (correspond)
* **Règle 4** : Total Amount <= 4000 (correspond)
* **Règle 5** : Total Amount <= 5000 (correspond)

Pour que la politique **Any** s'applique, toutes les règles correspondantes doivent renvoyer le même **Return Group**. Étant donné que les groupes ne correspondent pas entre les différentes règles, le résultat serait **false**.

### **8. Politique de la première règle et de la suivante (First & Adjacent)**

Choisit le résultat de la règle adjacente à la première règle qui est vraie.

**Exemple :**

| Règle | Condition            | Groupe renvoyé |
| ---- | -------------------- | ------------ |
| 1    | Total Amount <= 1000 | GROUP_1     |
| 2    | Total Amount <= 2000 | GROUP_2     |
| 3    | Total Amount <= 3000 | GROUP_3     |
| 4    | Total Amount <= 4000 | GROUP_4     |
| 5    | Total Amount <= 5000 | GROUP_5     |

Si le montant total est de **1500**, les règles évaluées seront :

* **Règle 1** : Total Amount <= 1000 (ne correspond pas)
* **Règle 2** : Total Amount <= 2000 (correspond)

Étant donné que la **Règle 2** est la première règle qui correspond, **First & Adjacent** appliquerait le résultat de la **Règle 3** : **GROUP_3**.

## **Tester l'arbre de décision**

**Vue d'ensemble :**
Le concepteur d'arbre de décision inclut une fonctionnalité de test pour valider la logique des règles configurées. Cette fonctionnalité permet aux utilisateurs de tester l'arbre de décision en fournissant des valeurs d'entrée spécifiques pour les champs sélectionnés.

**Étapes pour utiliser la fonctionnalité de test :**

1.  **Localiser le bouton de test :**

    * Dans le concepteur d'arbre de décision, repérez le bouton **Test**.

    <figure><img src="../../../.gitbook/assets/decision_tree_test_button.png" alt="Bouton Test de l'arbre de décision" width="563"><figcaption></figcaption></figure>
2.  **Ouvrir la fenêtre contextuelle de test :**

    * Cliquez sur le bouton **Test**.
    * Une fenêtre contextuelle apparaît, fournissant des champs de saisie correspondant aux critères utilisés dans l'arbre de décision.

    <figure><img src="../../../.gitbook/assets/decision_tree_test_popup.png" alt="Fenêtre contextuelle de test de l'arbre de décision" width="421"><figcaption></figcaption></figure>
3. **Fournir des valeurs d'entrée :**
   *   Saisissez des valeurs dans les champs de saisie pour simuler un scénario réel.

       <figure><img src="../../../.gitbook/assets/decision_tree_test_input.png" alt="Saisie de test de l'arbre de décision" width="428"><figcaption></figcaption></figure>
4.  **Évaluer les résultats :**

    * Après avoir saisi les entrées, l'arbre les traite selon la politique choisie.
    * Le système met en surbrillance la ou les règles qui correspondent aux entrées fournies.

    <figure><img src="../../../.gitbook/assets/decision_tree_test_result.png" alt="Résultat de test de l'arbre de décision" width="563"><figcaption></figcaption></figure>
5. **Examiner le retour en l'absence de correspondance :**
   * Si aucune règle n'est mise en surbrillance, le système affichera un retour expliquant pourquoi aucune règle ne correspond.
   * Utilisez ce retour pour ajuster les entrées ou examiner la configuration de l'arbre afin d'identifier d'éventuels problèmes.

## Export et enregistrement

* **Save** : enregistre la configuration actuelle de l'arbre de décision.
* **Export** : vous permet d'exporter la configuration de l'arbre de décision, qui peut ensuite être importée dans un autre environnement ou utilisée à des fins de sauvegarde.

## Cas d'usage

* **Workflows d'approbation** — routez les factures vers différents approbateurs en fonction de seuils de montant (par exemple, les montants supérieurs à 10 000 nécessitent l'approbation d'un responsable).
* **Règles de validation** — validez automatiquement les valeurs des champs et signalez les documents qui ne répondent pas aux critères configurés.
* **Attribution séquentielle** — attribuez des documents aux utilisateurs dans un ordre spécifique en fonction de conditions.
