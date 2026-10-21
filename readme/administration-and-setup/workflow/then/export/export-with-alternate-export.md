# Exporter avec une exportation alternative

<figure><img src="../../../../.gitbook/assets/workflow-card-qa-20261021-card-379e4b3a5355-fr.png" alt="Champs de la carte dans la version affichée. Les champs ne sont pas encore renseignés." width="563"><figcaption><p>Champs de la carte dans la version affichée. Les champs ne sont pas encore renseignés.</p></figcaption></figure>

## **Objectif**

La carte de workflow **« Exporter un document avec une exportation alternative »** permet d'exporter un document à l'aide d'une configuration d'export alternative. Elle offre de la flexibilité en permettant aux utilisateurs de contourner la configuration d'export par défaut et d'en utiliser une alternative, garantissant la compatibilité avec des exigences ou des scénarios spécifiques.

## **Composants de la carte**

**Configuration d'exportation alternative**

* **Descriptif** : spécifie la configuration d'export à utiliser pour le document.
* **Détail** : cette configuration remplace les paramètres par défaut et applique la configuration d'export alternative spécifiée dans le workflow.

## **Fonctionnalité**

* **Évaluation de la condition** :\
  Le système évalue les conditions définies dans les sections **« Quand »** et **« Et »** du workflow. La carte ne s'exécute que si toutes les conditions sont vraies.
* **Export du document** :\
  Une fois exécutée, la carte utilise la configuration d'export alternative pour traiter et exporter le document. Cela permet une gestion d'export sur mesure pour des workflows spécifiques.

## **Mise en place et configuration**

Pour configurer cette carte :

1. Assurez-vous que les sections **« Quand »** et **« Et »** sont correctement configurées, car la carte ne s'exécute que si ces conditions sont évaluées comme vraies.
2. Vérifiez que la configuration d'export alternative est valide et active dans le système.

## **Conclusion**

La carte de workflow **« Exporter un document avec une exportation alternative »** améliore la flexibilité et le contrôle des processus d'export de documents. En permettant la sélection d'une configuration d'export alternative, elle répond à des exigences d'export variées tout en maintenant une automatisation efficace du workflow.
