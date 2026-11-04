# Condition de statut de document unique

<figure><img src="../../../.gitbook/assets/userlmn_928e514bc0e2aa775894e4ec5f992bd9.png" alt=""><figcaption></figcaption></figure>

**Objectif**

Cette carte de workflow est conçue pour gérer les opérations sur les documents en fonction d'un seul statut de document spécifié. En simplifiant la condition à un seul statut, la carte se concentre sur des déclencheurs de workflow très spécifiques, ce qui la rend idéale pour les activités de traitement de document ciblées au sein d'un système ERP.

**Composants de la carte**

1. **Opérateur**
* **Description** : Spécifie la méthode d'évaluation du statut du document par rapport à la condition sélectionnée.
* **Options** :
* **est** : Déclenche l'opération si le statut actuel du document correspond au statut sélectionné.
* **n'est pas** : Déclenche l'opération si le statut actuel du document ne correspond pas au statut sélectionné.
2. **Statut**
* **Description** : Permet la sélection d'un seul statut de document pour définir la condition.
* **Exemples de statuts** : "Erreur", "Erreur d'export", "Prêt à valider", "Prêt à examiner", "Approbation en attente", "Deuxième approbation en attente".
* **Détail** : Les utilisateurs choisissent un statut dans une liste déroulante ou un ensemble de boutons radio. Ce statut sert ensuite de critère pour l'opération de la carte.

**Fonctionnalités**

* **Identification du statut du document** : Identifie le statut actuel d'un document lors de son traitement à travers le système ERP.
* **Évaluation de la condition** :
* En fonction de l'opérateur sélectionné (`est` ou `n'est pas`), la carte vérifie si le statut actuel du document correspond au critère de statut choisi.
* **Exécution de l'action** :
* **Condition vraie** : Si le statut correspond (ou ne correspond pas, en fonction de l'opérateur), l'action correspondante est initiée. Cela pourrait être l'acheminement pour un traitement ultérieur, la génération de notifications ou d'autres workflows prédéfinis.
* **Condition fausse** : Si la condition n'est pas remplie, aucune action n'est entreprise, ou un chemin alternatif est déclenché.
* **Intégration avec d'autres workflows** : Bien qu'il soit conçu pour une évaluation de statut unique, cette carte peut être intégrée efficacement dans des séquences de workflow plus larges pour garantir une manipulation précise des documents.

**Interactions utilisateur**

* **Configuration et paramétrage** : Les utilisateurs configurent la carte en sélectionnant un opérateur, puis en choisissant un statut parmi les options disponibles. Ce processus de sélection est simple et conçu pour éviter toute confusion.
* **Surveillance et reporting** : Permet la surveillance à travers des rapports générés par le système ou des tableaux de bord qui suivent le traitement des documents en fonction de leur statut, aidant à superviser l'efficacité des workflows mis en place.
* **Gestion des erreurs et notifications** : Configurable pour alerter les utilisateurs de toute anomalie de traitement ou pour signaler les documents ne répondant pas aux conditions définies, garantissant une attention et une résolution rapides.

#### Conclusion

La carte de workflow "Condition de statut de document unique" simplifie la gestion des documents en se concentrant sur des conditions de statut individuelles. Cette spécification est utile dans les cas où un contrôle précis sur les flux de documents est nécessaire, notamment dans des environnements avec des critères de traitement stricts. Documenter clairement cette version de la carte garantira que les utilisateurs comprennent pleinement son application et peuvent l'intégrer efficacement dans leurs opérations quotidiennes, améliorant à la fois la conformité et l'efficacité du traitement des documents.
