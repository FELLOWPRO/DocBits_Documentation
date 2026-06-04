# Assign document to matching sub organization

<figure><img src="../../../../.gitbook/assets/image (303).png" alt="" width="563"><figcaption></figcaption></figure>

## **Objectif :**

La carte de workflow **« Assign Document to Matching Sub-Organization Based on Field »** assigne dynamiquement un document à une sous-organisation, en fonction d'un champ spécifié dans le document. Si aucune sous-organisation correspondante n'est trouvée, la carte utilise une sous-organisation de repli prédéfinie.

## **Composants de la carte :**

1. **Field Name**
   * **Description :** spécifie le champ de document à utiliser pour déterminer la sous-organisation correspondante.
   * **Détail :** la carte recherche une valeur dans le champ spécifié pour la faire correspondre à une sous-organisation disponible.
2. **Sub-Organization (Fallback)**
   * **Description :** définit la sous-organisation de repli à utiliser si aucune correspondance n'est trouvée dans le champ spécifié.
   * **Détail :** si la valeur du champ ne correspond à aucune sous-organisation, le document sera assigné à la sous-organisation de repli sélectionnée.

## **Fonctionnalité :**

* **Évaluation de la condition :**\
  La carte n'exécute son action que si les sections **« Where »** et **« And »** sont toutes deux évaluées comme vraies.
* **Attribution dynamique :**\
  La carte vérifie la valeur du champ spécifié et assigne le document à la sous-organisation qui correspond à cette valeur.
* **Mécanisme de repli :**\
  Si aucune sous-organisation correspondante n'est trouvée, le document est assigné à la sous-organisation de repli.

## **Mise en place et configuration :**

* **Sélectionner le Field Name :**\
  Choisissez le champ du document qui contient la valeur à faire correspondre à une sous-organisation.
* **Sélectionner la sous-organisation de repli :**\
  Choisissez la sous-organisation qui sera utilisée si aucune correspondance n'est trouvée dans le champ du document.

## **Conclusion :**

La carte de workflow **« Assign Document to Matching Sub-Organization Based on Field »** offre de la flexibilité en acheminant dynamiquement les documents vers la sous-organisation appropriée, avec une option de repli supplémentaire pour garantir qu'aucun document ne reste non assigné.
