# Attribuer séquentiellement à l'utilisateur

<figure><img src="../../../../.gitbook/assets/workflow-card-qa-20261021-card-5b15eaee7258-fr.png" alt="Champs de la carte dans la version affichée. Les champs ne sont pas encore renseignés." width="563"><figcaption><p>Champs de la carte dans la version affichée. Les champs ne sont pas encore renseignés.</p></figcaption></figure>

## **Objectif**

La carte de workflow « **Attribuer séquentiellement à l'utilisateur** » automatise l'attribution de documents à un utilisateur sélectionné de manière séquentielle. La valeur de priorité détermine l'ordre d'attribution, les nombres les plus faibles représentant la priorité la plus élevée.

## **Composants de la carte**

1. **Utilisateur**
   * **Descriptif** : l'utilisateur sélectionné se verra attribuer le document en fonction de la séquence du workflow.
   * **Détail** : un menu déroulant qui répertorie tous les utilisateurs disponibles pour l'attribution.
2. **Priorité (Valeur)**
   * **Descriptif** : un champ de saisie numérique où le niveau de priorité de l'utilisateur peut être défini.
   * **Détail** : les nombres les plus faibles indiquent une priorité plus élevée. Les documents sont attribués aux utilisateurs par ordre croissant de priorité.

## **Fonctionnalité**

* **Attribution du document** :\
  La carte attribue les documents à l'utilisateur sélectionné de manière séquentielle, en tenant compte du niveau de priorité.\
  Si plusieurs utilisateurs ont la même priorité, les documents sont attribués dans l'ordre d'apparition des utilisateurs dans le menu déroulant.

## **Mise en place et configuration**

1. Ajoutez la carte **Attribuer le document de manière séquentielle** à votre workflow.
2. Configurez le champ **Utilisateur** :
   * Sélectionnez un utilisateur dans le menu déroulant.
3. Configurez le champ **Priorité (Valeur)** :
   * Saisissez une valeur numérique pour définir la priorité d'attribution.
4. Enregistrez et activez le workflow pour appliquer la configuration.

## **Conclusion**

La carte de workflow « Assign the Document Sequentially to User » garantit une distribution organisée des documents en les attribuant selon une séquence hiérarchisée. Cela améliore la gestion des tâches et réduit les retards de traitement.

<!-- workflow-card-practical-example-20261021 -->

## Exemple pratique

**Quand utiliser :** Ajoutez un utilisateur à une séquence d'approbation de document prioritaire.

**Configuration :** Sélectionnez `Demo Reviewer A` et la priorité `10`. Ajoutez une affectation distincte à la priorité `20` lorsqu'un réviseur ultérieur est nécessaire.

**Résultat attendu et contre-exemple :** Les affectations portent les priorités configurées ; la valeur numérique inférieure a une priorité plus élevée. Vérifiez la séquence d'affectation, pas seulement l'ordre des cartes sur la toile.

Il s’agit d’une configuration illustrative et du résultat attendu. Utilisez les champs, utilisateurs et groupes configurés dans votre organisation de test ; cela ne veut pas dire que cet exemple a été exécuté.
