# Create a New Task and assign it to the Recipient

<figure><img src="../../../../.gitbook/assets/image (288).png" alt="" width="563"><figcaption></figcaption></figure>

## **Objectif :**

La carte de workflow **« Create Task with Fallback »** assure une délégation efficace des tâches en les assignant à des rôles spécifiques — Disponent ou Purchaser — tout en intégrant un mécanisme de repli pour éviter les échecs d'attribution de tâches. Cette carte améliore la fiabilité et l'adaptabilité du workflow dans des scénarios dynamiques.

## **Composants de la carte :**

1. **Title**
   * **Description** : spécifie le titre de la tâche créée.
   * **Détail** : fournit un identifiant concis à la tâche.
2. **Description**
   * **Description** : décrit l'objet ou le contexte de la tâche.
   * **Détail** : clarifie les détails de la tâche.
3. **Priority**
   * **Description** : définit le niveau d'urgence de la tâche.
   * **Options** :
     * **High** : nécessite une attention immédiate.
     * **Medium** : important mais non urgent.
     * **Low** : peut être traité plus tard.
4. **Assigned Role**
   * **Description** : spécifie le rôle principal auquel la tâche est assignée.
   * **Options** :
     * **Disponent** : assigne la tâche au Disponent.
     * **Purchaser** : assigne la tâche au Purchaser.
5. **Email Notification**
   * **Description** : permet de notifier l'utilisateur assigné par e-mail.
   * **Options** :
     * **True** : envoie une notification par e-mail à l'utilisateur.
     * **False** : aucune notification par e-mail n'est envoyée.
6. **Fallback User**
   * **Description** : fournit une option de repli pour l'attribution de la tâche si le rôle destinataire n'est pas trouvé.
   * **Détail** : permet de sélectionner un utilisateur dans une liste déroulante pour garantir la délégation de la tâche.

## **Fonctionnalité :**

* **Évaluation de la condition** :\
  La carte ne s'exécute que si les conditions des sections **« Where »** et **« And »** sont satisfaites.
* **Attribution de la tâche** :
  * La tâche est assignée au rôle sélectionné (Disponent ou Purchaser).
  * Si le rôle spécifié n'est pas trouvé, la tâche est assignée à un utilisateur de la liste déroulante de repli.
* **Notification par e-mail** :\
  Envoie un e-mail à l'utilisateur assigné si la notification par e-mail est activée.

## **Mise en place et configuration :**

1. **Spécifier les détails de la tâche** : saisissez le titre, la description et la priorité de la tâche.
2. **Sélectionner le rôle principal** : choisissez le rôle auquel la tâche sera assignée (Disponent ou Purchaser).
3. **Configurer l'utilisateur de repli** : sélectionnez un utilisateur de repli dans la liste déroulante pour garantir l'attribution de la tâche si le rôle principal n'est pas trouvé.
4. **Activer la notification par e-mail** : indiquez si l'utilisateur assigné doit recevoir une notification par e-mail.

## **Conclusion :**

La carte de workflow **« Create Task with Fallback »** assure une délégation des tâches fluide en intégrant un mécanisme de repli. En assignant les tâches en fonction des rôles et en proposant une option d'utilisateur alternatif, elle renforce la fiabilité et la flexibilité des processus de gestion des tâches.
