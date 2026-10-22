# Test : connexion d’importation FTP

#### Objectif

Ces tests garantissent le bon fonctionnement de notre système d'importation FTP. Nous vérifions que nous pouvons ajouter une nouvelle connexion d'importation FTP, tester la connexion, l'activer/désactiver et la nettoyer par la suite.



{% embed url="https://grafana.polydocs.io/d-solo/b6ad3a9c-260c-46a3-9ade-47691e743d4d/docbits?from=1715746603760&orgId=1&panelId=84&refresh=1m&to=1715768203760" %}

## Scénarios de test

1. **Setup:**
   * **Variables d'environnement :** Chargez les détails nécessaires tels que les informations sur le serveur FTP et les informations d'identification à partir des variables d'environnement.
2.  **FTP Connection Tests:**

    **Ajouter une nouvelle connexion :**

    * **Test d’ajout d’une connexion d’importation FTP (`test_add_new_ftp_import_connection`):**
      * Ajoutez une nouvelle connexion d'importation FTP avec les informations d'identification et les détails du serveur fournis.
      * **Résultat attendu :** La connexion doit être ajoutée avec succès.

    **Deactivate Connection:**

    * **Test Désactiver FTP Importer la connexion (`test_deactivate_ftp_import_connection`) :**
      * Désactivez la connexion d'importation FTP nouvellement ajoutée.
      * **Résultat attendu :** La connexion doit être désactivée avec succès.

    **Test Connection:**

    * **Test de connexion FTP (`test_test_ftp_connection`):**
      * Testez si la connexion d'importation FTP peut se connecter avec succès au serveur FTP.
      * **Résultat attendu :** La connexion doit être testée avec succès.

    **Vérifier la connexion dans la liste:**

    * **Test de présence de la connexion FTP dans la liste (`test_check_ftp_connection_in_list`):**
      * Vérifiez si la connexion d'importation FTP nouvellement ajoutée est présente dans la liste des connexions.
      * **Résultat attendu :** La connexion doit être trouvée dans la liste.

    **Vérifier la connexion désactivée :**

    * **Test de vérification FTP Connexion désactivée (`test_check_ftp_connection_deactivated`) :**
      * Vérifiez que la connexion d'importation FTP est marquée comme inactive dans la liste.
      * **Résultat attendu :** La connexion doit être inactive.

    **Ajouter un dossier de test :**

    * **Test Ajouter un dossier de test à la connexion (`test_add_test_folder_to_connection`) :**
      * Ajoutez un répertoire par défaut (dossier de test) à la connexion d'importation FTP.
      * **Résultat attendu :** Le répertoire par défaut doit être ajouté avec succès.

    **Reactivate Connection:**

    * **Test Réactiver FTP Importer la connexion (`test_reactivate_ftp_import_connection`) :**
      * Réactivez la connexion d'importation FTP précédemment désactivée.
      * **Résultat attendu :** La connexion doit être réactivée avec succès.

    **Vérifier la connexion réactivée :**

    * **Test de vérification FTP Connexion réactivée (`test_check_ftp_connection_reactivated`) :**
      * Vérifiez que la connexion d'importation FTP est marquée comme active dans la liste.
      * **Résultat attendu :** La connexion doit être active.

    **Cleanup:**

    * **Test de nettoyage FTP Importation (`test_cleanup_ftp_import`) :**
      * Supprimez la connexion d'importation FTP pour nettoyer après les tests.
      * **Résultat attendu :** La connexion doit être supprimée avec succès.

## Explication détaillée de chaque test

* **Configuration et initialisation :**
  * **Initialiser les données partagées :** Préparer les données partagées pour les tests.
* **FTP Connection Tests:**
  * **Ajouter une nouvelle connexion :** Ajoutez une nouvelle connexion d'importation FTP avec les informations d'identification fournies et les détails du serveur.
  * **Désactiver la connexion :** Désactivez la connexion d'importation FTP nouvellement ajoutée.
  * **Test de connexion :** Testez si la connexion d'importation FTP peut se connecter avec succès au serveur FTP.
  * **Vérifier la connexion dans la liste :** Vérifiez que la nouvelle connexion d'importation FTP est présente dans la liste des connexions.
  * **Vérifier la connexion désactivée :** Confirmez que la connexion d'importation FTP est marquée comme inactive dans la liste.
  * **Ajouter un dossier de test :** Ajoutez un répertoire par défaut (dossier de test) à la connexion d'importation FTP.
  * **Réactiver la connexion :** Réactivez la connexion d'importation FTP précédemment désactivée.
  * **Vérifier la connexion réactivée :** Assurez-vous que la connexion d'importation FTP est marquée comme active dans la liste.
  * **Cleanup :** Supprimez la connexion d'importation FTP pour nettoyer après les tests.

\


