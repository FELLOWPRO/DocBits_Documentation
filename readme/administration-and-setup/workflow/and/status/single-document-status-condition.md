# Single Document Status Condition

<figure><img src="../../../../.gitbook/assets/userlmn_928e514bc0e2aa775894e4ec5f992bd9 (1).png" alt="" width="528"><figcaption></figcaption></figure>

**Objectif**

Cette carte de workflow est conçue pour gérer les opérations sur les documents en fonction d'un seul statut de document spécifié. En simplifiant la condition à un seul statut, la carte se concentre sur des déclencheurs de workflow très précis, ce qui la rend idéale pour des activités ciblées de traitement de documents au sein d'un système ERP.

**Composants de la carte**

1. **Operator**
   * **Description** : spécifie la méthode d'évaluation du statut du document par rapport à la condition sélectionnée.
   * **Options** :
     * **is** : déclenche l'opération si le statut actuel du document correspond au statut sélectionné.
     * **is not** : déclenche l'opération si le statut actuel du document ne correspond pas au statut sélectionné.
2. **Status**
   * **Description** : permet de sélectionner un seul statut de document pour définir la condition.
   * **Exemples de statuts** : « Error », « Export Error », « Ready in Validation », « Ready in Review », « Pending Approval », « Pending Second Approval ».
   * **Détail** : les utilisateurs choisissent un statut dans une liste déroulante ou un ensemble de boutons radio. Ce statut sert ensuite de critère pour le fonctionnement de la carte.

**Fonctionnalité**

* **Identification du statut du document** : identifie le statut actuel d'un document à mesure qu'il est traité dans le système ERP.
* **Évaluation de la condition** :
  * En fonction de l'opérateur sélectionné (`is` ou `is not`), la carte vérifie si le statut actuel du document correspond au critère de statut choisi.
* **Exécution de l'action** :
  * **Condition vraie** : si le statut correspond (ou ne correspond pas, selon l'opérateur), l'action correspondante est lancée. Il peut s'agir d'un acheminement pour un traitement complémentaire, de la génération de notifications ou d'autres workflows prédéfinis.
  * **Condition fausse** : si la condition n'est pas satisfaite, aucune action n'est effectuée, ou un chemin alternatif est déclenché.
* **Intégration avec d'autres workflows** : bien qu'elle soit conçue pour l'évaluation d'un seul statut, cette carte peut être intégrée efficacement dans des séquences de workflow plus larges pour garantir un traitement précis des documents.

**Interactions utilisateur**

* **Mise en place et configuration** : les utilisateurs configurent la carte en sélectionnant un opérateur, puis en choisissant un statut parmi les options disponibles. Ce processus de sélection est simple et conçu pour éviter toute confusion.
* **Surveillance et reporting** : permet la surveillance via des rapports ou des tableaux de bord générés par le système qui suivent le traitement des documents en fonction de leur statut, aidant à superviser l'efficacité des workflows mis en œuvre.
* **Gestion des erreurs et notifications** : configurable pour alerter les utilisateurs en cas d'anomalies de traitement ou pour signaler les documents qui ne satisfont pas les conditions définies, garantissant une attention et une résolution rapides.

#### Conclusion

La carte de workflow « Single Document Status Condition » simplifie la gestion des documents en se concentrant sur des conditions de statut individuelles. Cette spécification est utile lorsqu'un contrôle précis des flux de documents est nécessaire, en particulier dans des environnements aux critères de traitement stricts. Documenter clairement cette version de la carte garantira que les utilisateurs comprennent pleinement son application et peuvent l'intégrer efficacement dans leurs opérations quotidiennes, améliorant à la fois la conformité et l'efficacité du traitement des documents.
