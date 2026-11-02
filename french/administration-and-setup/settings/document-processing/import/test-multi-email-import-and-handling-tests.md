# Test : importation et traitement des e-mails

## Quels éléments sont testés ?

Ces tests garantissent le bon fonctionnement de notre système d'importation d'e-mails. Les principaux objectifs sont de :

1. **Envoyer des e-mails** avec pièces jointes.
2. **Recevoir et déplacer des e-mails** vers des dossiers spécifiques.
3. **Vérifiez si les e-mails sont lus ou non lus.**
4. **Importer les e-mails dans notre système.**
5. **Nettoyez** en supprimant ensuite les e-mails et les documents importés.

## Étapes à suivre

1. **Setup:**
   * **Obtenir les paramètres d'environnement :** Chargez les détails et les informations d'identification du serveur de messagerie à partir des variables d'environnement.
   * **Crypter le mot de passe de l'e-mail :** Crypter en toute sécurité le mot de passe de l'e-mail.
2. **Envoyer et gérer les e-mails:**
   * **Envoyer des e-mails :** Utilisez une fonction SMTP pour envoyer des e-mails avec des sujets et des pièces jointes spécifiques.
   * **Déplacer les e-mails :** Utilisez les fonctions IMAP pour déplacer les e-mails vers le dossier cible.
   * **Liste des dossiers :** Vérifiez si le dossier cible existe.
   * **Supprimer les e-mails :** Nettoyez les e-mails en les supprimant des dossiers.
   * **Vérifier l'état des e-mails :** Vérifiez si les e-mails sont marqués comme non lus ou lus.
3.  **Test Sequence**

    **Initial Setup:**

    * **Vérifier la connexion :** Vérifiez la connexion au serveur de messagerie et obtenez l’ID de connexion.
    * **Test de connexion :** Confirmez que la connexion avec les informations d'identification stockées fonctionne.
    * **Vérification du dossier :** Assurez-vous que le dossier cible existe sur le serveur de messagerie.

    **Email Operations:**

    * **Envoyer des e-mails de test :** Envoyez trois e-mails avec des sujets uniques.
    * **Récupérer les identifiants d'e-mail :** Obtenez les identifiants des e-mails envoyés depuis la boîte de réception.
    * **Déplacer les e-mails :** Déplacez ces e-mails de la boîte de réception vers le dossier cible.
    * **Vérifier l'état des e-mails :** Assurez-vous que les e-mails du dossier cible sont marqués comme non lus.

    **Email Importing:**

    * **Récupérer les e-mails :** Importez les e-mails du dossier cible dans notre système.
    * **Vérifiez les e-mails importés :** Assurez-vous que les e-mails importés sont correctement récupérés et enregistrés.

    **Log Verification:**

    * **Vérifier les journaux d'importation :** Vérifiez que les sujets des e-mails envoyés sont enregistrés dans les journaux d'importation.

    **Cleanup:**

    * **Supprimer les documents importés :** Supprimez les documents importés des e-mails.
    * **Supprimer les e-mails :** Nettoyez en supprimant les e-mails envoyés et déplacés des dossiers.

### Explication détaillée de chaque test

* **Configuration et initialisation :**
  * **Initialiser les données partagées :** Préparer les données partagées pour les tests.
* **Tests de connexion e-mail:**
  * **Get Connection ID:** Vérifiez si nous pouvons nous connecter au serveur de messagerie et obtenez un ID pour la connexion.
  * **Vérification de connexion :** Assurez-vous que la connexion au serveur de messagerie fonctionne correctement.
* **Tests de vérification des dossiers :**
  * **Vérifiez le dossier cible :** Assurez-vous que le dossier cible existe sur le serveur de messagerie.
  * **Vérifier la liste des dossiers :** Assurez-vous que la liste des dossiers du serveur correspond à nos attentes.
* **Envoi d'e-mail et ID Récupération :**
  * **Envoyer des e-mails :** Envoyez trois e-mails de test avec des sujets et des pièces jointes spécifiques.
  * **Obtenir les identifiants de courrier électronique :** Récupérez les identifiants uniques de ces e-mails envoyés depuis la boîte de réception.
* **Déplacement d'e-mails et vérification de l'état :**
  * **Déplacer les e-mails vers le dossier :** Déplacez les e-mails de test de la boîte de réception vers le dossier cible.
  * **Vérifiez l'état non lu :** Assurez-vous que les e-mails sont marqués comme non lus après leur déplacement.
* **Récupération d'e-mails et validation des réponses :**
  * **Récupérer les e-mails du dossier :** Importez les e-mails du dossier cible dans notre système.
  * **Valider les e-mails récupérés :** Confirmez que les e-mails récupérés correspondent aux e-mails envoyés.
* **Vérification du journal d’importation:**
  * **Récupérer le journal d'importation :** Récupérer le journal des e-mails importés.
  * **Vérifiez les sujets des e-mails dans le journal :** Assurez-vous que les sujets des e-mails de test sont présents dans le journal d'importation.
* **Cleanup:**
  * **Supprimer les documents importés :** Supprimez les documents importés des e-mails.
  * **Supprimer les e-mails :** Supprimez les e-mails de test de la boîte de réception et du dossier cible pour que tout reste propre.

\


