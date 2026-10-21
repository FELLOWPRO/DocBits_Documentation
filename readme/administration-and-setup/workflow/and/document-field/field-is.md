# Vérifier la présence et le contenu d’un champ

<figure><img src="../../../../.gitbook/assets/workflow-card-qa-20261021-card-db30554e1eb1-fr.png" alt="Champs de la carte dans la version affichée. Les champs ne sont pas encore renseignés. Certains libellés de cette version de la carte ont encore une traduction incomplète ou incorrecte dans l’interface. Les explications de cette page emploient les termes corrects." width="563"><figcaption><p>Champs de la carte dans la version affichée. Les champs ne sont pas encore renseignés. Certains libellés de cette version de la carte ont encore une traduction incomplète ou incorrecte dans l’interface. Les explications de cette page emploient les termes corrects.</p></figcaption></figure>

## **Objectif :**

Cette carte de workflow est conçue pour automatiser des actions en fonction de la présence ou de l'état d'un champ spécifié dans un document. En évaluant si le champ est vide, manquant ou renseigné, elle permet aux workflows de traiter les documents avec précision et exactitude.

## **Composants de la carte :**

1. **Nom du champ**
   * **Descriptif :** spécifie le nom du champ à évaluer.
   * **Détail :** il doit correspondre à l'identifiant exact utilisé dans le document pour garantir une détection précise du champ.
2. **Opérateurs**
   * **Descriptif** : définit la condition qui déclenche le workflow, en fonction de la présence ou de l'état du champ.
   * **Possibilités** :
     * **Vide/Pas dans le document :** le workflow se déclenche si le champ est soit absent du document, soit présent mais vide.
     * **Dans Document/Non Vide :** le workflow se déclenche si le champ existe dans le document et contient une valeur.

## **Fonctionnalité :**

* **Détection de l'état :** la carte surveille le champ spécifié pour évaluer sa présence et son état.
* **Évaluation de la condition :**
  * Le système évalue si le champ spécifié est dans l'état (Empty/Not in Document ou In Document/Not Empty) défini par l'opérateur sélectionné.
*

**Exécution de l'action :**
* **Condition Vide/Pas dans le document :** si l'état du champ correspond à cette condition (c.-à-d. que le champ est soit absent du document, soit présent mais vide), le système déclenche les actions associées. Celles-ci peuvent inclure la génération d'alertes, le signalement du document pour examen ou l'arrêt du workflow.
* **État dans le document/non vide :** si l'état du champ correspond à cette condition (c.-à-d. que le champ existe dans le document et contient une valeur), le système déclenche les actions associées. Celles-ci peuvent inclure l'activation des étapes suivantes du workflow, la mise à jour d'enregistrements ou le déclenchement de notifications.
## **Mise en place et configuration :**

* Les utilisateurs sélectionnent le champ dans une liste de champs de document disponibles. L'opérateur est choisi via un menu déroulant, offrant des options claires entre « Empty/Not in Document » ou « In Document/Not Empty ».

## **Conclusion :**

La carte de workflow « Field Presence and State Validation » est un outil essentiel pour les workflows de traitement de documents, garantissant un traitement précis des champs manquants ou renseignés. En automatisant des actions en fonction de l'état des champs, cette carte améliore l'intégrité des données, réduit les erreurs et garantit que les workflows fonctionnent de manière fluide et efficace.

<!-- workflow-card-practical-example-20261021 -->

## Exemple pratique

**Quand utiliser :** Détectez les factures dont le numéro de facture doit encore être révisé.

**Configuration :** Sélectionnez le champ `invoice_number` et Vide/Pas dans le document.

**Résultat attendu et contre-exemple :** Un champ vide ou manquant est réussi. Une valeur renseignée telle que `DEMO-001` ne remplit pas cette condition.

Il s’agit d’une configuration illustrative et du résultat attendu. Utilisez les champs, utilisateurs et groupes configurés dans votre organisation de test ; cela ne veut pas dire que cet exemple a été exécuté.
