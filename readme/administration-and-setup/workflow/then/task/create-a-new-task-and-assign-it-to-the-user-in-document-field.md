# Create a New Task and assign it to the User in Document Field

<figure><img src="../../../../.gitbook/assets/image (290).png" alt="" width="563"><figcaption></figcaption></figure>

## **Objectif :**

La carte de workflow **« Create Field-Based Task or Notification »** sert à créer des tâches ou des notifications assignées dynamiquement à des utilisateurs identifiés dans des champs de document spécifiques. Cette carte offre un mécanisme de repli facultatif pour garantir une exécution fluide du workflow même lorsque le champ de document ne spécifie pas d'utilisateur valide.

## **Composants de la carte :**&#x20;

1. **Title**
   * **Description** : spécifie le titre de la tâche ou de la notification.
   * **Détail** : sert à nommer et à identifier la tâche ou la notification créée.
2. **Description**
   * **Description** : fournit des détails supplémentaires sur la tâche ou la notification.
   * **Détail** : garantit que le destinataire comprend l'objet et le contexte de la tâche ou de la notification.
3. **Priority**
   * **Description** : définit l'urgence de la tâche ou de la notification.
   * **Options** :
     * **High** : nécessite une attention immédiate.
     * **Medium** : important mais moins urgent.
     * **Low** : peut être traité plus tard.
4. **Field Name**
   * **Description** : spécifie le champ de document qui sera utilisé pour assigner la tâche ou la notification.
   * **Détail** : le champ sélectionné déterminera dynamiquement l'utilisateur auquel la tâche ou la notification sera assignée. Si le champ est vide ou invalide, la tâche ou la notification sera assignée à l'utilisateur de repli sélectionné dans la liste déroulante.
5. **Email Notification**
   * **Description** : configure si l'utilisateur assigné est notifié par e-mail.
   * **Options** :
     * **True** : envoie une notification par e-mail à l'utilisateur assigné.
     * **False** : aucune notification par e-mail n'est envoyée.
6. **Fallback User**
   * **Description** : permet de sélectionner un utilisateur dans une liste déroulante pour assigner la tâche ou la notification lorsqu'aucun utilisateur valide n'est trouvé dans le champ de document.
   * **Détail** : garantit que la tâche ou la notification est assignée même si le champ de document est vide ou invalide.

## **Composants supplémentaires dans la Version 3 :**

1. **Notification Type**&#x20;
   * **Description** : spécifie si la carte crée une tâche ou une notification.
   * **Options** :
     * **Task** : crée une tâche assignée à l'utilisateur spécifié.
     * **Notification** : envoie une notification au lieu de créer une tâche.

## **Fonctionnalité :**

* **Évaluation de la condition** :\
  La carte n'exécute son action que si les sections **« Where »** et **« And »** sont toutes deux évaluées comme vraies.
* **Création de tâche ou de notification** :
  * Assigne la tâche ou la notification à l'utilisateur identifié dans le champ de document.
  * Dans la Version 3, permet de créer soit une tâche, soit une notification.
* **Mécanisme de repli** :\
  Si le champ de document n'identifie pas d'utilisateur valide, la carte assigne la tâche ou la notification à l'utilisateur de repli sélectionné dans la liste déroulante.
* **Notification par e-mail** :\
  Envoie une notification par e-mail à l'utilisateur assigné si elle est configurée pour cela.

## **Mise en place et configuration :**

1. **Définir les détails de la tâche ou de la notification** : saisissez le titre, la description et la priorité.
2. **Sélectionner le champ de document** : choisissez le champ qui spécifie l'utilisateur de l'attribution de la tâche ou de la notification.
3. **Activer la notification par e-mail** : indiquez si une notification par e-mail doit être envoyée à l'utilisateur assigné.
4. **Sélectionner l'utilisateur de repli** : choisissez un utilisateur de repli dans la liste déroulante pour l'attribution si le champ de document n'identifie pas d'utilisateur valide.
5. **Spécifier le type de notification (Version 3)** : indiquez si la carte crée une tâche ou une notification.

## **Conclusion :**

La carte de workflow **« Create Field-Based Task or Notification »** rationalise la gestion des tâches et des notifications en assignant dynamiquement les responsabilités en fonction des champs de document. Son mécanisme d'utilisateur de repli et ses options enrichies dans la Version 3 offrent de la flexibilité, garantissant que les tâches ou notifications sont toujours assignées, même lorsque les données du document sont incomplètes.
