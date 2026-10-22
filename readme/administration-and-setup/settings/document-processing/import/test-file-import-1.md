# Test : importation de fichiers 1

## Objectif

Ces tests sont conçus pour garantir le bon fonctionnement de notre système d'importation de fichiers. Nous testons spécifiquement l'importation des fichiers PDF et TIFF dans le système, en nous assurant qu'ils sont traités et stockés avec succès.

#### Préparation et nettoyage des tests

* **Setup:**
  * Avant chaque test, nous enregistrons un message de configuration.
  * **Nettoyage :** Après chaque test, nous nettoyons en supprimant tous les documents créés par l'utilisateur de test de la base de données pour garantir qu'aucune donnée restante n'affecte les tests suivants.

#### Scénarios de test

1. **Import PDF File:**
   * **Test d’importation PDF (`test_import_pdf`):**
     * Importez un fichier PDF (`FellowBananaInvoice.pdf`) dans le système.
     * **Résultat attendu :** Le fichier doit être importé avec succès, renvoyant un document ID.
2. **Import TIFF File:**
   * **Test d’importation TIFF (`test_import_tiff`):**
     * Importez un fichier TIFF (`TIFF_FILE.TIF`) dans le système.
     * **Résultat attendu :** Le fichier doit être importé avec succès, renvoyant un document ID.

## Explication détaillée de chaque test

* **Configuration et nettoyage :**
  * **Logging :** Un message de configuration et de nettoyage est enregistré pour chaque test.
  * **Nettoyage de la base de données (`clean_documents`) :** Supprime tous les documents créés par l'utilisateur test de la base de données pour maintenir un état propre.
*   **Tests d'importation de fichiers :**

    **Import PDF File:**

    * **Load User:** Chargez l'utilisateur test.
    * **Chemin du fichier :** Spécifiez le chemin d'accès au fichier PDF (`tests/files/pdfs/FellowBananaInvoice.pdf`).
    * **Import File:** Utilisez la classe `FileImporter` pour importer le fichier PDF.
    * **Vérifiez la réponse :** Assurez-vous que la réponse est une liste contenant un message de réussite et un document ID.

    **Import TIFF File:**

    * **Load User:** Chargez l'utilisateur test.
    * **Chemin du fichier :** Spécifiez le chemin d'accès au fichier TIFF (`tests/files/pdfs/TIFF_FILE.TIF`).
    * **Import File:** Utilisez la classe `FileImporter` pour importer le fichier TIFF.
    * **Vérifiez la réponse :** Assurez-vous que la réponse est une liste contenant un message de réussite et un document ID.

## Structure du code

* **Logger :** Utilisé pour enregistrer les messages de débogage pendant la configuration, le nettoyage et l'exécution des tests.
* **Database Helper :** Exécute les requêtes sans renvoyer de résultats pour le nettoyage.
* **File Importer:** Gère l'importation de fichiers dans le système.
* **Fixtures :** `set_up` fixtures de test pour gérer la configuration et le nettoyage des tests.
* **Tests:**
  * `test_import_pdf` : Teste l'importation d'un fichier PDF.
  * `test_import_tiff` : Teste l'importation d'un fichier TIFF.

#### Résumé

Ces tests garantissent que notre fonctionnalité d'importation de fichiers fonctionne comme prévu pour les fichiers PDF et TIFF. En suivant cette approche, nous vérifions que les fichiers sont importés correctement et que le système peut gérer différents types de fichiers sans problème.


