# Module actif

<figure><img src="../../../../.gitbook/assets/workflow-card-qa-20261021-card-405c9bb87c62-fr.png" alt="Champs de la carte dans la version affichée. Les champs ne sont pas encore renseignés." width="563"><figcaption><p>Champs de la carte dans la version affichée. Les champs ne sont pas encore renseignés.</p></figcaption></figure>

## **Objectif :**

Cette carte DocBits vérifie si un module spécifique du système est actif ou inactif. Elle permet aux workflows de se poursuivre en fonction de l'état d'activation d'un module, garantissant que les actions ne sont effectuées que si le module nécessaire est disponible.

## **Fonctionnalité :**

* **Validation de l'état du module :** cette carte vérifie l'état d'activation d'un module spécifié et l'évalue par rapport à une condition définie par l'utilisateur.
* **Sélection du module :** les utilisateurs spécifient le nom du module à vérifier, garantissant une validation précise.
* **Opérateurs :** les conditions suivantes peuvent être appliquées :
  * **Is :** le workflow se poursuit si le module sélectionné est actif.
  * **N'est-ce pas :** le workflow se poursuit si le module sélectionné est inactif.

## **Utilisation :**

Cette carte est particulièrement utile aux administrateurs ou aux gestionnaires de système qui doivent créer des workflows dépendant de la disponibilité ou de la fonctionnalité de modules spécifiques. Elle aide à garantir que les workflows ne sont exécutés que lorsque tous les modules requis sont correctement configurés.

## **Scénario d'exemple**

* Un utilisateur configure la carte pour vérifier si le module **« Traitement des documents »** **est actif.** Si le module est actif, le workflow se poursuit en déclenchant des tâches automatisées de traitement des documents. Si le module est inactif, le workflow s'arrête, évitant des actions inutiles.

En utilisant la carte « Module Active Check », les organisations peuvent améliorer la fiabilité du workflow, éviter les erreurs dues à des modules inactifs et garantir que les processus sont alignés sur la configuration du système.
