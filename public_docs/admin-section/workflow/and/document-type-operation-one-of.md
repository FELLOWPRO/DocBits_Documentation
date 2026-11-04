# Opération de type de document un de

<figure><img src="../../../.gitbook/assets/userlmn_14ab8ac5e693d9bbe68d178795d12a9f.png" alt=""><figcaption></figcaption></figure>

**Objectif**

Cette carte est conçue pour gérer les actions sur les documents en fonction de leur type, en utilisant une logique conditionnelle simple (est/n'est pas) pour déclencher ou empêcher des flux de travail spécifiques. Cela permet un contrôle précis sur la façon dont différents types de documents sont traités dans le système ERP.

**Composants de la carte**

1. **Opérateur**
* **Description** : Détermine la logique conditionnelle appliquée aux types de documents.
* **Options** :
* **est** : L'opération sera déclenchée si le type de document correspond à l'un des types spécifiés dans la liste.
* **n'est pas** : L'opération sera déclenchée si le type de document ne correspond à aucun des types répertoriés.
2. **Liste des types de documents**
* **Description** : Spécifie une liste de types de documents auxquels la condition s'appliquera.
* **Détail** : Cela peut inclure une variété de types de documents tels que "Facture", "Bon de commande", "Contrat", "Dossier d'employé", etc., sur la base desquels la condition (est/n'est pas) sera évaluée.

**Fonctionnalité**

* **Identification du document** : Le système identifie d'abord le type de chaque document entrant ou existant en fonction des attributs prédéfinis ou des métadonnées.
* **Évaluation de la condition** :
* Si l'opérateur est **est**, la carte vérifie si le type de document est dans la liste fournie.
* Si l'opérateur est **n'est pas**, la carte vérifie si le type de document n'est pas dans la liste.
* **Déclenchement de l'action** : En fonction du résultat de l'évaluation de la condition :
* **Vrai** : Lance les opérations ou flux de travail associés si la condition est remplie.
* **Faux** : Le processus est contourné ou une opération alternative est déclenchée si la condition n'est pas remplie.
* **Intégration et automatisation** : S'intègre de manière transparente avec d'autres composants du système, garantissant que la gestion des documents est automatisée et respecte les flux de travail et les politiques organisationnels.

**Interactions utilisateur**

* **Configuration** : Les utilisateurs doivent spécifier l'opérateur et énumérer les types de documents lors de la configuration de la carte. Cette configuration peut inclure des éléments d'interface tels que des menus déroulants ou des cases à cocher pour sélectionner les types de documents et les opérateurs.
* **Surveillance et ajustements** : Les utilisateurs peuvent suivre les résultats et l'efficacité de cette carte grâce aux journaux et rapports générés par le système ERP. Des ajustements peuvent être apportés à la liste ou à l'opérateur en fonction des besoins commerciaux évolutifs.
* **Gestion des erreurs et des retours** : Fournit des mécanismes de retour d'informations pour les erreurs rencontrées pendant l'opération. Les utilisateurs peuvent configurer des alertes en cas d'échec des conditions, garantissant une attention rapide aux problèmes.

#### Conclusion

La carte de flux de travail "Condition de type de document" joue un rôle crucial dans la gestion des opérations basées sur les documents avec précision et flexibilité. En utilisant une logique conditionnelle simple, elle contribue à garantir que les documents sont traités de manière appropriée, améliorant ainsi l'efficacité et la conformité. Documenter clairement cette carte aidera les utilisateurs à comprendre comment l'implémenter et l'utiliser efficacement, en en faisant une partie précieuse de la documentation de votre système ERP.
