# Test : importation et traitement des e-mails

## Objectif

Ces tests garantissent que notre système peut gérer correctement l'importation d'e-mails. Cela inclut l'envoi d'e-mails, leur réception et leur déplacement vers des dossiers spécifiques, la vérification s'ils sont lus ou non, leur importation dans le système et leur nettoyage ultérieur.

## Étapes de test

1. **Setup:**
   * **Obtenir les paramètres d'environnement :** Chargez les détails nécessaires tels que les informations sur le serveur de messagerie et les informations d'identification à partir des variables d'environnement.
   * **Crypter le mot de passe de l'e-mail :** Cryptez en toute sécurité le mot de passe de l'e-mail pour une utilisation en toute sécurité.
2. **Envoi et gestion d'e-mails :**
   * **Envoyer un e-mail :** Utilisez une fonction SMTP pour envoyer un e-mail avec un objet et une pièce jointe spécifiques.
   * **Déplacer l'e-mail :** Utilisez les fonctions IMAP pour déplacer l'e-mail vers un dossier cible.
   * **Liste des dossiers :** Assurez-vous que le dossier cible existe.
   * **Supprimez l'e-mail :** Nettoyez en supprimant l'e-mail du dossier.
   * **Vérifier l'état de l'e-mail :** Vérifiez si l'e-mail est marqué comme lu ou non lu.
3.  **Test Sequence**

    **Initial Setup:**

    * **Vérifier la connexion :** Vérifiez la connexion au serveur de messagerie et obtenez l’ID de connexion.
    * **Test de connexion :** Confirmez que la connexion avec les informations d'identification stockées fonctionne.
    * **Vérification du dossier :** Assurez-vous que le dossier cible existe sur le serveur de messagerie.

    **Email Operations:**

    * **Envoyer un e-mail de test :** Envoyez un e-mail avec un sujet spécifique.
    * **Récupérer l'e-mail ID:** Obtenez l’ID de l'e-mail envoyé depuis la boîte de réception.
    * **Déplacer l'e-mail :** Déplacez l'e-mail de la boîte de réception vers le dossier cible.
    * **Vérifier l'état de l'e-mail :** Assurez-vous que l'e-mail dans le dossier cible est marqué comme non lu.

    **Email Importing:**

    * **Récupérer l'e-mail :** Importez l'e-mail du dossier cible dans notre système.
    * **Vérifiez l'e-mail importé :** Assurez-vous que l'e-mail importé est correctement récupéré et enregistré.

    **Log Verification:**

    * **Vérifier le journal d'importation :** Vérifiez que l'objet de l'e-mail envoyé est enregistré dans le journal d'importation.

    **Cleanup:**

    * **Supprimer le document importé :** Supprimez le document importé de l'e-mail.
    * **Supprimer l'e-mail :** Supprimez l'e-mail envoyé et déplacé des dossiers pour que tout reste propre.

## Explication détaillée de chaque test

* **Configuration et initialisation :**
  * **Initialiser les données partagées :** Préparer les données partagées pour les tests.
* **Tests de connexion e-mail:**
  * **Get Connection ID:** Vérifiez si nous pouvons nous connecter au serveur de messagerie et obtenez un ID pour la connexion.
  * **Vérification de connexion :** Assurez-vous que la connexion au serveur de messagerie fonctionne correctement.
* **Tests de vérification des dossiers :**
  * **Vérifiez le dossier cible :** Assurez-vous que le dossier cible existe sur le serveur de messagerie.
  * **Vérifier la liste des dossiers :** Assurez-vous que la liste des dossiers du serveur correspond à nos attentes.
* **Envoi d'e-mail et ID Récupération :**
  * **Envoyer un e-mail :** Envoyez un e-mail de test avec un objet et une pièce jointe spécifiques.
  * **Get Email ID:** Récupérez l’ID unique de cet email envoyé depuis la boîte de réception.
* **Déplacement d'e-mails et vérification de l'état :**
  * **Déplacer l'e-mail vers le dossier :** Déplacez l'e-mail de test de la boîte de réception vers le dossier cible.
  * **Vérifiez l'état non lu :** Assurez-vous que l'e-mail est marqué comme non lu après son déplacement.
* **Récupération d'e-mails et validation des réponses :**
  * **Récupérer l'e-mail du dossier :** Importez l'e-mail du dossier cible dans notre système.
  * **Valider l'e-mail récupéré :** Confirmez que l'e-mail récupéré est présent dans la réponse.
* **Vérification du journal d’importation:**
  * **Récupérer le journal d'importation :** Récupérer le journal des e-mails importés.
  * **Vérifiez l'objet de l'e-mail dans le journal :** Assurez-vous que l'objet de l'e-mail de test est présent dans le journal d'importation.
* **Cleanup:**
  * **Supprimer le document importé :** Supprimez le document importé de l'e-mail.
  * **Supprimez l'e-mail :** Supprimez l'e-mail de test de la boîte de réception et du dossier cible pour que tout reste propre.

\


