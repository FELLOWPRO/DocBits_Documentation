# Assign Document and Create Task/Notification

<figure><img src="../../../../.gitbook/assets/image (14) (1) (2).png" alt="" width="563"><figcaption></figcaption></figure>

## **Objectif**

La carte de workflow « **Assign Document and Create Task/Notification Based on Decision Table** » assigne un document et crée une tâche ou une notification avec des détails configurables. Le destinataire est déterminé par le retour d'une table de décision, et la carte permet de définir des priorités et d'envoyer des notifications par e-mail.

## **Composants de la carte**

1. **Assignee Type**
   * **Description :** spécifie si le retour de la table de décision assigne le document et la tâche/notification à un utilisateur ou à un groupe.
   * **Détail :** un champ pour configurer le type de destinataire comme « User » ou « Group » en fonction de la sortie de la table de décision.
2. **Task/Notification**
   * **Description :** spécifie le type d'action à créer pour le destinataire.
   * **Détail :** une liste déroulante pour sélectionner « Task » ou « Notification » selon les besoins du workflow.
3. **Title**
   * **Description :** le titre de la tâche ou de la notification.
   * **Détail :** un champ pour fournir un titre concis qui identifie la tâche ou la notification.
4. **Description**
   * **Description :** des détails supplémentaires sur la tâche ou la notification.
   * **Détail :** un champ pour décrire l'objet et le contexte de la tâche ou de la notification.
5. **Priority**
   * **Description :** définit le niveau d'urgence de la tâche ou de la notification.
   * **Options :**
     * **High :** nécessite une attention immédiate.
     * **Medium :** important mais non urgent.
     * **Low :** peut être traité plus tard.
6. **Assignee Type**
   * **Description :** ce champ détermine le type de destinataire (User ou Group) auquel le document et la tâche/notification sont assignés.
   * **Détail :** un menu déroulant pour sélectionner si la tâche/notification est assignée à un utilisateur ou à un groupe en fonction de la sortie de la table de décision.
7. **Send Mail**
   * **Description :** configure si une notification par e-mail est envoyée au destinataire.
   * **Options :**
     * **True :** envoie une notification par e-mail.
     * **False :** aucune notification par e-mail n'est envoyée.
8. **Value**
   * **Description :** définit la priorité numérique de l'attribution du document.
   * **Détail :** un champ pour saisir une valeur numérique, où les nombres les plus faibles indiquent une priorité plus élevée.

## **Fonctionnalité**

* **Évaluation de la condition :**\
  La carte n'exécute ses actions que si les conditions du workflow sont satisfaites.
* **Évaluation de la table de décision :**\
  La table de décision détermine si le document et la tâche/notification sont assignés à un utilisateur ou à un groupe.
* **Attribution du document et création de tâche/notification :**\
  Le document est assigné au résultat de la table de décision. Une tâche ou une notification est créée avec le titre, la description et le niveau de priorité spécifiés.
* **Notification par e-mail :**\
  Si « Send Mail » est défini sur True, une notification par e-mail est envoyée au destinataire.

## **Mise en place et configuration**

1. **Définir le type de destinataire :**
   * Configurez le champ Assignee Type sur « User » ou « Group » en fonction de la sortie de la table de décision.
2. **Sélectionner Task/Notification :**
   * Choisissez « Task » ou « Notification » dans la liste déroulante Task/Notification.
3. **Définir les détails de la tâche/notification :**
   * Saisissez le Title et la Description de la tâche ou de la notification.
   * Sélectionnez la Priority (High, Medium ou Low) dans la liste déroulante.
4. **Activer la notification par e-mail :**
   * Définissez l'option Send Mail sur True ou False, selon qu'une notification par e-mail doit être envoyée.
5. **Définir la priorité numérique :**
   * Saisissez une valeur numérique dans le champ Value pour déterminer la priorité de l'attribution, où les nombres les plus faibles sont traités en premier.
6. Enregistrez la configuration de la carte et activez le workflow.

## **Conclusion**

La carte de workflow « Assign Document and Create Task/Notification Based on Decision Table » garantit que les tâches ou notifications sont assignées dynamiquement à l'utilisateur ou au groupe approprié en fonction des résultats de la table de décision. Cette carte facilite une délégation efficace des tâches, des priorités personnalisables et des notifications par e-mail facultatives pour améliorer la réactivité du workflow.
