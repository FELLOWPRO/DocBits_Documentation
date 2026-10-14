# Reject the Document

<figure><img src="../../../../.gitbook/assets/image (282).png" alt="" width="563"><figcaption></figcaption></figure>

## **Objectif :**

La carte de workflow **« Reject the Document »** sert à marquer un document comme rejeté au sein d'un workflow. Cette action interrompt la progression du document et l'empêche de passer à l'étape suivante du workflow. Elle garantit que les documents qui ne satisfont pas les conditions ou critères nécessaires sont signalés et empêchés de poursuivre leur traitement.

## **Composants de la carte :**

1. **Rejection Status**
   * **Description** : ce composant marque le document comme rejeté, signalant qu'il n'a pas satisfait les conditions requises pour l'approbation.
   * **Détail** : lorsqu'elle est déclenchée, cette carte met à jour le statut du document en « rejected ». Cette décision est prise en fonction des conditions définies dans les sections **« Where »** et **« And »**.

## **Fonctionnalité :**

* **Évaluation de la condition** : le système évalue les conditions définies dans les sections **« Where »** et **« And »**.
  * Si **les deux conditions sont vraies**, le document sera rejeté.
  * Si **l'une des conditions est fausse**, la carte ne s'exécute pas et le statut du document reste inchangé.
* **Exécution de l'action** : lorsque les conditions sont satisfaites, le document est marqué comme rejeté. Cette action garantit que seuls les documents satisfaisant des critères spécifiques poursuivent, tandis que les autres sont signalés et interrompus pour examen ou correction.

## **Conclusion :**

La carte de workflow **« Reject the Document »** est un outil essentiel pour contrôler le flux des documents dans les processus automatisés. En permettant le rejet des documents non conformes, elle garantit que seuls les documents valides et exacts poursuivent dans le workflow, améliorant l'efficacité et la précision de la gestion des documents.
