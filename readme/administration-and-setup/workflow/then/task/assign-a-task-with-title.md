# Assign a Task with Title

<figure><img src="../../../../.gitbook/assets/image (291).png" alt="" width="563"><figcaption></figcaption></figure>

## **Objectif :**

La carte de workflow « Assign Task / Notification from Decision Table » est conçue pour assigner dynamiquement des tâches ou des notifications en fonction des résultats d'une table de décision. Cette carte garantit que les tâches ou notifications sont assignées au bon utilisateur ou groupe selon la logique définie dans la table de décision, avec une notification par e-mail facultative envoyée au destinataire.

## **Composants de la carte :**

1. **Title**
   * **Description** : spécifie le titre de la tâche ou de la notification créée.
   * **Détail** : le titre doit fournir un contexte et décrire l'objet de la tâche ou de la notification.
2. **Description**
   * **Description** : définit le contenu ou l'objet de la tâche ou de la notification.
   * **Détail** : fournit des informations supplémentaires sur la tâche ou la notification, expliquant le contexte ou l'action requise.
3. **Priority**
   * **Description** : définit le niveau d'urgence de la tâche ou de la notification.
   * **Options** :
     * **High** : tâches ou notifications nécessitant une attention immédiate.
     * **Medium** : tâches importantes à traiter rapidement.
     * **Low** : tâches pouvant être traitées plus tard.
4. **Assignee Type**
   * **Description** : spécifie l'utilisateur ou le groupe assigné à la tâche ou à la notification en fonction de la sortie de la table de décision.
   * **Détail** : la table de décision évalue dynamiquement les conditions et renvoie l'utilisateur ou le groupe approprié pour l'attribution.
5. **Email Notification**
   * **Description** : configure si une notification par e-mail sera envoyée à l'utilisateur ou au groupe assigné.
   * **Options** :
     * **True** : envoie une notification par e-mail au destinataire.
     * **False** : aucune notification par e-mail n'est envoyée.

#### **Composants supplémentaires dans la Version 3**

1. **Notification Type**
   * **Description** : spécifie si la carte crée une tâche ou une notification.
   * **Options** :
     * **Task** : crée une tâche assignée à l'utilisateur ou au groupe issu de la table de décision.
     * **Notification** : envoie une notification à l'utilisateur ou au groupe issu de la table de décision.

## **Fonctionnalité :**

* **Évaluation de la condition :**\
  La carte n'exécute son action que si les sections **« Where »** et **« And »** sont toutes deux évaluées comme vraies.
* **Attribution de la tâche / notification**\
  La carte assigne la tâche ou la notification à l'utilisateur ou au groupe identifié par la table de décision. La table de décision évalue dynamiquement des conditions prédéfinies et renvoie le destinataire correspondant.
* **Notification par e-mail**\
  Si elle est configurée pour cela, une notification par e-mail est envoyée à l'utilisateur ou au groupe assigné.
* **Fonctionnalité de la Version 3**\
  Dans la Version 3, la carte permet de créer soit une Task, soit une Notification, offrant plus de flexibilité pour la gestion des tâches et la communication.

## **Mise en place et configuration :**

1. **Définir les détails de la tâche ou de la notification** :\
   Saisissez le titre, la description et la priorité de la tâche ou de la notification.
2. **Configurer la table de décision** :\
   Configurez la table de décision pour déterminer dynamiquement quel utilisateur ou groupe doit se voir assigner la tâche ou la notification.
3. **Activer la notification par e-mail** :\
   Indiquez si une notification par e-mail doit être envoyée à l'utilisateur ou au groupe assigné.
4. **Spécifier le type de notification (Version 3)** :\
   Choisissez si la carte créera une tâche ou enverra une notification.

## **Conclusion :**

La carte de workflow **« Assign Task / Notification from Decision Table »** automatise l'attribution de tâches ou de notifications en fonction de conditions dynamiques définies dans une table de décision. La Version 3 enrichit sa fonctionnalité en permettant aux utilisateurs de choisir entre créer une tâche ou une notification, et garantit que le bon destinataire est toujours assigné. La fonctionnalité de notification par e-mail tient les utilisateurs informés, rationalisant la communication et la gestion des tâches.
