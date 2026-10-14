# Create a New Task and assign it to the group

<figure><img src="../../../../.gitbook/assets/image (289).png" alt="" width="563"><figcaption></figcaption></figure>

## **Objectif :**

La carte de workflow **« Create Group Task or Notification »** facilite la création de tâches ou de notifications pour des groupes spécifiés, garantissant une communication et une gestion des tâches efficaces. Enrichie d'une fonctionnalité d'arbre de décision dans les versions ultérieures, elle détermine dynamiquement le groupe assigné ou la méthode, rationalisant les opérations.

## **Composants de la carte :**

1. **Title**
   * **Description** : spécifie le titre de la tâche ou de la notification.
   * **Détail** : sert d'identifiant à la tâche ou à la notification créée.
2. **Description**
   * **Description** : décrit le contexte ou les détails de la tâche ou de la notification.
   * **Détail** : apporte de la clarté sur son objet.
3. **Priority**
   * **Description** : définit le niveau d'importance de la tâche.
   * **Options** :
     * **High** : nécessite une action immédiate.
     * **Medium** : important mais moins urgent.
     * **Low** : peut être traité plus tard.
4. **Assigned Group**
   * **Description** : spécifie le groupe responsable de la tâche ou de la notification.
   * **Détail** : sélectionné dans une liste déroulante de groupes disponibles.
5. **Email Notification**
   * **Description** : permet d'envoyer un e-mail pour notifier le groupe assigné.
   * **Options** :
     * **True** : envoie une notification par e-mail.
     * **False** : aucune notification par e-mail n'est envoyée.

## **Composants supplémentaires dans la Version 3 et la Version 4**

1. **Decision Tree (Version 3 uniquement)**
   * **Description** : permet d'utiliser un arbre de décision pour la création dynamique de tâches.
   * **Options** :
     * **True** : active le traitement par arbre de décision.
     * **False** : désactive le traitement par arbre de décision.
2. **Task/Notification Option (Version 4 uniquement)**
   * **Description** : permet de créer soit une tâche, soit une notification.
   * **Options** :
     * **Task** : crée une tâche pour le groupe sélectionné.
     * **Notification** : envoie une notification au lieu de créer une tâche.

## **Fonctionnalité :**

* **Évaluation de la condition** :\
  Exécute l'action de la carte uniquement lorsque les sections **« Where »** et **« And »** sont vraies.
* **Création de tâche ou de notification** :
  * Une tâche est créée pour le groupe sélectionné avec le titre, la description et la priorité spécifiés.
  * Dans la Version 4, la carte peut créer une notification au lieu d'une tâche.
* **Attribution dynamique (Version 3 uniquement)** :\
  Si elle est activée, l'arbre de décision détermine dynamiquement le groupe cible.
* **Notification par e-mail** :\
  Envoie une notification par e-mail au groupe si l'option e-mail est définie sur true.

## **Mise en place et configuration :**

1. **Définir les détails de la tâche ou de la notification** : saisissez le titre, la description et la priorité.
2. **Assigner à un groupe** : sélectionnez un groupe dans la liste déroulante pour l'attribution de la tâche ou de la notification.
3. **Activer la notification par e-mail** : indiquez si le groupe doit être notifié par e-mail.
4. **Use Decision Tree (Version 3 uniquement)** : activez l'arbre de décision pour assigner dynamiquement le groupe.
5. **Sélectionner le type de sortie (Version 4 uniquement)** : choisissez si la carte crée une tâche ou une notification.

## **Conclusion :**

La carte de workflow **« Create Group Task or Notification »** simplifie la gestion des tâches et des notifications en ciblant directement les groupes. Sa fonctionnalité d'attribution dynamique, rendue possible par l'arbre de décision, renforce la flexibilité, tandis que les notifications par e-mail garantissent une communication en temps utile. Les Versions 3 et 4 ajoutent des fonctionnalités avancées, en faisant un outil polyvalent pour une exécution efficace du workflow.
