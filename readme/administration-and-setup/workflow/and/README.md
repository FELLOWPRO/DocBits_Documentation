# And

## Comprendre les cartes « And »

### **Objectif des cartes « And » :**

* Les cartes **And** servent de cartes de condition qui définissent les critères devant être remplis pour que le workflow se poursuive. Elles agissent en pratique comme des opérateurs logiques « ET » : toutes les conditions spécifiées dans ces cartes doivent être satisfaites pour que l'action suivante soit déclenchée.

#### Catégories de cartes « And »

D'après les captures d'écran, ces cartes couvrent un large éventail de conditions, parmi lesquelles :

* **Compare with Purchase Order** :
  * Des conditions liées à la validation et à la comparaison par rapport aux bons de commande, comme la comparaison des dates de livraison, des prix unitaires ou des écarts de quantité. Elles sont essentielles pour garantir que les transactions respectent les conditions convenues.

<figure><img src="../../../.gitbook/assets/image (14) (1) (1) (1).png" alt=""><figcaption></figcaption></figure>

* **Document Field** :
  * Elles impliquent des conditions basées sur des champs spécifiques au sein des documents, comme des cases cochées, la comparaison de valeurs de champs ou la vérification qu'un champ de document respecte une tolérance définie. C'est particulièrement important pour l'intégrité des données et les contrôles automatisés au sein des formulaires ou des systèmes de gestion documentaire.

<figure><img src="../../../.gitbook/assets/image (15) (1) (1) (1).png" alt=""><figcaption></figcaption></figure>

* **Date & Time :**
  * Des conditions basées sur les dates et les heures

<figure><img src="../../../.gitbook/assets/image (17) (1) (1).png" alt=""><figcaption></figcaption></figure>

* **Document** :
  * Des conditions basées sur les caractéristiques du document, comme son type ou son association à une sous-organisation particulière. Ces conditions peuvent orienter les workflows en fonction de la catégorisation des documents ou de l'implication d'un service.

<figure><img src="../../../.gitbook/assets/image (18) (1) (1).png" alt=""><figcaption></figcaption></figure>

* **Logic** :
  * Des conditions logiques pouvant impliquer des évaluations telles que « Continuer avec une probabilité de X % » ou l'exécution de requêtes HTTPS, essentielles pour les intégrations et la prise de décision probabiliste au sein des workflows.

<figure><img src="../../../.gitbook/assets/image (19) (1) (1).png" alt=""><figcaption></figcaption></figure>

* **Status** :
  * Centrées sur le statut des documents ou des tâches, ces conditions garantissent que seuls les éléments dans certains états déclenchent des workflows spécifiques, ce qui est essentiel pour une gestion de processus pilotée par le statut.

<figure><img src="../../../.gitbook/assets/image (20) (1) (1).png" alt=""><figcaption></figcaption></figure>

* **Table** :
  * Elles impliquent des conditions basées sur les données d'un tableau, comme la correspondance avec des motifs regex ou la comparaison de valeurs au sein d'un tableau. De telles conditions sont essentielles pour valider et manipuler de grands ensembles de données.

<figure><img src="../../../.gitbook/assets/image (22) (1) (1).png" alt=""><figcaption></figcaption></figure>

* **Assignee** :
  * Des conditions basées sur les assignés d'une tâche ou d'un document. Cela garantit que les actions ne sont effectuées que lorsque certains utilisateurs sont impliqués, renforçant la responsabilité et la précision des tâches.

<figure><img src="../../../.gitbook/assets/image (24) (1) (1).png" alt=""><figcaption></figcaption></figure>

### Application pratique

Ces cartes « And » sont configurées au sein du workflow pour effectuer des contrôles et des validations qui garantissent que le processus respecte strictement les règles métier et les normes d'intégrité des données. Par exemple :

* **Un workflow peut utiliser une carte « And » pour vérifier que le montant total d'une facture correspond au bon de commande avant de déclencher le paiement.**
* **Un autre workflow pourrait utiliser une carte « And » pour s'assurer qu'un document est examiné par des membres d'équipe précis avant de passer à l'étape suivante.**

### Conclusion

Les cartes « And » constituent un composant fondamental des systèmes de workflow qui exigent un contrôle précis de l'exécution des processus en fonction de plusieurs conditions. Elles garantissent que chaque étape d'un workflow ne se poursuit que lorsque tous les critères nécessaires sont pleinement remplis, automatisant ainsi des arbres de décision complexes au sein des processus métier.

Comprendre et configurer correctement ces cartes est essentiel pour exploiter pleinement les capacités de votre système de gestion des workflows afin d'améliorer l'efficacité, la précision et la conformité au sein des processus organisationnels.
