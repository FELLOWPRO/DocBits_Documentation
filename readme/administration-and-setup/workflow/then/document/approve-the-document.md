# Approve the Document



<figure><img src="../../../../.gitbook/assets/image (281).png" alt="" width="563"><figcaption></figcaption></figure>

## **Objectif :**

La carte de workflow **« Approve the Document »** sert à marquer un document comme approuvé. Elle permet au document de progresser vers l'étape suivante du workflow, autorisant l'exécution de traitements automatisés ou de workflows d'approbation. Cette carte aide à rationaliser les processus de gestion des documents, garantissant que seuls les documents approuvés avancent vers des actions complémentaires.

## **Composants de la carte :**

1. **Approval Status**
   * **Description** : ce composant marque le document comme approuvé.
   * **Détail** : lorsque cette carte est déclenchée, le statut d'approbation du document est mis à jour pour indiquer l'approbation. Cette action peut être définie en fonction des conditions des sections **« Where »** et **« And »**.

## **Fonctionnalité :**

* **Évaluation de la condition** : le système évalue les conditions définies dans les sections **« Where »** et **« And »**.
  * Si **les deux conditions sont vraies**, le document sera marqué comme approuvé.
  * Si **l'une des conditions est fausse**, la carte ne s'exécute pas et le statut d'approbation du document reste inchangé.
* **Exécution de l'action** : lorsque les conditions sont satisfaites, le document est approuvé. Cette modification se reflète dans le statut du document, lui permettant de poursuivre dans le workflow.

## **Conclusion :**

La carte de workflow **« Approve the Document »** est un composant clé pour automatiser l'approbation des documents dans les workflows métier. En garantissant que seuls les documents satisfaisant des critères spécifiques sont approuvés, elle aide à maintenir la cohérence, réduit la supervision manuelle et permet un traitement plus fluide des documents.
