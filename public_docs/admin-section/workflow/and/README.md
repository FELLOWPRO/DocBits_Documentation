# Et

## Compréhension des cartes "Et"

### **But des cartes "Et" :**

* Les cartes **Et** servent de cartes de condition qui spécifient les critères qui doivent être remplis pour que le flux de travail puisse se poursuivre. Elles agissent efficacement comme des opérateurs logiques "ET", ce qui signifie que toutes les conditions spécifiées dans ces cartes doivent être satisfaites pour que l'action suivante soit déclenchée.

#### Catégories de cartes "Et"

À partir des captures d'écran, il est clair que ces cartes couvrent un large éventail de conditions, qui incluent :

*   **Comparer avec le bon de commande** :

* Conditions liées à la validation et à la comparaison par rapport aux bons de commande, telles que la comparaison des dates de livraison, des prix unitaires ou des différences de quantité. Celles-ci sont cruciales pour garantir que les transactions sont conformes aux termes convenus.



<figure><img src="../../../.gitbook/assets/And1.png" alt=""><figcaption></figcaption></figure>

*   **Champ de document** :

* Il s'agit de conditions basées sur des champs spécifiques dans les documents, comme le marquage des cases à cocher, la comparaison des valeurs des champs, ou s'assurer qu'un champ de document respecte une tolérance spécifiée. Cela est particulièrement important pour l'intégrité des données et les vérifications automatisées dans les formulaires ou les systèmes de gestion de documents.



<figure><img src="../../../.gitbook/assets/And2.png" alt=""><figcaption></figcaption></figure>

* **Document** :
* Conditions basées sur les caractéristiques du document, telles que le type ou l'association avec une sous-organisation particulière. Ces conditions peuvent orienter les flux de travail en fonction de la catégorisation des documents ou de l'implication départementale.

<figure><img src="../../../.gitbook/assets/And3.png" alt=""><figcaption></figcaption></figure>

* **Logique** :
* Conditions logiques qui pourraient impliquer des évaluations comme "Continuer avec une chance de X%" ou exécuter des requêtes HTTPS, qui sont essentielles pour les intégrations et la prise de décisions probabilistes au sein des flux de travail.

<figure><img src="../../../.gitbook/assets/And4.png" alt=""><figcaption></figcaption></figure>

*   **Statut** :

* En se concentrant sur l'état des documents ou des tâches, ces conditions garantissent que seuls les éléments dans certains états déclenchent des flux de travail spécifiques, ce qui est crucial pour la gestion des processus basée sur l'état.



<figure><img src="../../../.gitbook/assets/And5.png" alt=""><figcaption></figcaption></figure>

* **Tableau** :
* Il s'agit de conditions basées sur des données de tableau, telles que la correspondance de motifs regex ou la comparaison de valeurs dans un tableau. De telles conditions sont essentielles pour valider et manipuler de grands ensembles de données.

<figure><img src="../../../.gitbook/assets/And6.png" alt=""><figcaption></figcaption></figure>

*   **Bénéficiaire** :

* Conditions basées sur les bénéficiaires de tâches ou de documents. Cela garantit que des actions ne sont entreprises que lorsque certains utilisateurs sont impliqués, renforçant ainsi la responsabilité et la spécificité des tâches.



<figure><img src="../../../.gitbook/assets/And7.png" alt=""><figcaption></figcaption></figure>

### Application pratique

Ces cartes "Et" sont configurées dans le flux de travail pour effectuer des vérifications et des validations qui garantissent que le processus respecte strictement les règles métier et les normes d'intégrité des données. Par exemple :

* **Un flux de travail pourrait utiliser une carte "Et" pour vérifier que le montant total d'une facture correspond au bon de commande avant de déclencher le paiement.**
* **Un autre flux de travail pourrait utiliser une carte "Et" pour s'assurer qu'un document est examiné par des membres spécifiques de l'équipe avant de passer à l'étape suivante.**

### Conclusion

Les cartes "Et" sont un composant fondamental des systèmes de flux de travail qui nécessitent un contrôle précis de l'exécution du processus en fonction de plusieurs conditions. Elles garantissent que chaque étape d'un flux de travail ne se poursuit que lorsque tous les critères nécessaires sont pleinement satisfaits, automatisant ainsi des arbres de décision complexes au sein des processus métier.

Comprendre et configurer correctement ces cartes est crucial pour tirer pleinement parti des capacités de votre système de gestion des flux de travail afin d'améliorer l'efficacité, la précision et la conformité au sein des processus organisationnels.
