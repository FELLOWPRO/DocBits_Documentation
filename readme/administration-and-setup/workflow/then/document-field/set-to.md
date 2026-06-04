# Set to

<figure><img src="../../../../.gitbook/assets/image (278).png" alt="" width="563"><figcaption></figcaption></figure>

## **Objectif :**

Cette carte de workflow est conçue pour définir automatiquement un champ spécifié du document sur une valeur texte prédéfinie en fonction des conditions définies dans les sections **« Where »** et **« And »**. Elle permet aux utilisateurs de rationaliser la saisie de données en garantissant que les champs sont renseignés avec des valeurs cohérentes lorsque certains critères sont satisfaits.

## **Composants de la carte :**

1. **Field Name**
   * **Description** : spécifie le champ qui sera mis à jour avec la valeur texte.&#x20;
   * **Détail** : le champ sélectionné sera mis à jour avec la valeur texte spécifiée si les conditions des sections **« Where »** et **« And »** sont satisfaites.
2. **Text**
   * **Description** : définit la valeur texte qui sera définie dans le champ cible lorsque les conditions sont évaluées comme vraies.
   * **Détail** : il peut s'agir d'un message personnalisé, d'un statut ou d'une valeur prédéfinie que l'utilisateur souhaite écrire dans le champ. Le texte doit être conforme au format de saisie attendu du champ (par ex. alphanumérique, date ou autres types d'informations textuelles).

## **Fonctionnalité :**

* **Évaluation de la condition** : le système évalue les conditions des sections **« Where »** et **« And »** :
  * Si **les deux conditions sont vraies**, les actions définies dans la **« Then Section »** seront exécutées. Plus précisément, le champ cible (Field Name) sera renseigné avec le texte spécifié.
  * Si **la section « Where » ou la section « And » est fausse**, aucune action n'est effectuée et le champ reste inchangé. Les actions de la **Then Section** sont entièrement ignorées si l'une des conditions est fausse.
* **Exécution de l'action** : si les deux conditions des sections **« Where »** et **« And »** sont satisfaites, le système renseigne automatiquement le champ spécifié avec la valeur texte choisie. Si les conditions ne sont pas satisfaites, aucune modification n'est apportée au champ.

## **Mise en place et configuration :**

Pour configurer cette carte :

1. **Sélectionnez le champ** (Field Name) qui sera mis à jour avec la valeur texte. Les champs disponibles dans le document sont répertoriés pour la sélection.
2. **Spécifiez la valeur texte** qui sera écrite dans le champ cible lorsque les conditions sont vraies.
3. L'action ne s'exécute que si les conditions des sections **« Where »** et **« And »** sont toutes deux évaluées comme vraies.

## **Conclusion :**

La carte de workflow **« Set Field to Text »** offre un moyen simple d'automatiser le renseignement de valeurs texte dans des champs de document spécifiques en fonction de conditions prédéfinies. Cela réduit la saisie manuelle de données et garantit la cohérence du traitement des documents, en faisant un outil utile pour automatiser les workflows et améliorer l'efficacité.
