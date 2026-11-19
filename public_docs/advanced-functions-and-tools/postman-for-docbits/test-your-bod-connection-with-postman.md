# Testez votre connexion BOD avec Postman

## Aperçu

Cette page explique comment vérifier le traitement réussi de votre BOD (Business Object Document) avec Postman. Vous testez le point de terminaison API correspondant en envoyant une requête accompagnée de votre fichier de mappage BOD. Suivez les étapes ci-dessous pour mener le test jusqu'au bout.

## Accéder à votre clé API et au fichier de mappage BOD

### Récupérer votre clé API

1.  Allez dans **Paramètres → SYSTÈME ET ADMINISTRATION → Intégration et SSO**.

    <figure><img src="../../.gitbook/assets/test-bod-connection-integration-sso-fr-20261112.png" alt="La table Clés API de la page Intégration et SSO : pour chaque clé, le préfixe masqué, le nom, la date d'expiration, la dernière utilisation, le statut, l'icône de copie et le menu Actions à trois points."><figcaption><p>La table <strong>Clés API</strong> de la page <strong>Intégration et SSO</strong>. Chaque ligne affiche le préfixe masqué de la clé, son nom, la date d'expiration (colonne <strong>Expire</strong>), la dernière utilisation (colonne <strong>Dernière Utilisation</strong>) et le statut.</p></figcaption></figure>
2.  Vous pouvez copier votre **clé API** manuellement ou cliquer sur l'icône de copie pour la placer dans le presse-papiers.

    <figure><img src="../../.gitbook/assets/test-bod-connection-api-key-copy-fr-20261112.png" alt="Gros plan sur une ligne de la table Clés API : le préfixe masqué de la clé, son icône de copie, le nom de la clé et le menu Actions à trois points."><figcaption><p>Cliquez sur l'icône de copie à côté d'une clé pour copier sa valeur. Pour des raisons de sécurité, la table n'affiche que le préfixe de la clé suivi de <code>****</code> ; la clé complète n'est affichée qu'une seule fois, lors de sa création. Si vous ne disposez plus de la clé complète, créez-en une nouvelle comme décrit dans <a href="../../administration-and-setup/settings/global-settings/integration/api-key-management.md">Gestion des clés API</a>.</p></figcaption></figure>

    La liste des clés, l'icône de copie et le menu **Actions** à trois points sont décrits en détail sur la page [Gestion des clés API](../../administration-and-setup/settings/global-settings/integration/api-key-management.md).

### **Télécharger le fichier de mappage BOD**

1.  Allez dans **Paramètres → TRAITEMENT DES DOCUMENTS → Exporter**.

    <figure><img src="../../.gitbook/assets/test-bod-connection-export-list-fr-20261112.png" alt="La liste Exporter avec deux configurations d'exportation ; sur une ligne, le menu Actions à trois points est ouvert et propose Désactiver, Éditer et Supprimer."><figcaption><p>La liste <strong>Exporter</strong>. Chaque ligne correspond à une configuration d'exportation ; la colonne <strong>Méthode D'exportation</strong> indique comment les documents sont envoyés.</p></figcaption></figure>
2.  Dans la colonne **Actions** de la configuration concernée, cliquez sur le menu à trois points et sélectionnez **Éditer**.

    <figure><img src="../../.gitbook/assets/test-bod-connection-export-list-fr-20261112.png" alt="La liste Exporter avec le menu Actions à trois points ouvert sur une ligne : Désactiver, Éditer et Supprimer."><figcaption><p>Le menu <strong>Actions</strong> de la ligne est ouvert et <strong>Éditer</strong> est disponible. <strong>Éditer</strong> ouvre la configuration d'exportation ; la page <a href="../../administration-and-setup/settings/document-processing/export.md">Exportation</a> décrit chaque colonne et chaque action.</p></figcaption></figure>
3.  Repérez le champ **Fichier de cartographie de la BOD** et cliquez sur le bouton **Télécharger** pour enregistrer le fichier.

    <figure><img src="../../.gitbook/assets/test-bod-connection-bod-mapping-fr-20261112.png" alt="Le formulaire de configuration d'exportation Infor IDM + ION BOD en mode édition : les champs Fichier API ION, Fichier de mappage IDM et Fichier de cartographie de la BOD, chacun avec un bouton Télécharger."><figcaption><p>La configuration d'exportation en mode édition. Sous <strong>Configuration d'exportation</strong>, le champ <strong>Fichier de cartographie de la BOD</strong> propose un bouton <strong>Télécharger</strong> qui enregistre le fichier de mappage (BOD-Mapping.properties) sur votre ordinateur. Pour modifier ce fichier, voir <a href="../../infor-integration-and-configuration/exporting-to-infor/creating-a-bod-mapping-file.md">Créer un fichier de mappage BOD</a>.</p></figcaption></figure>

## Tester le point de terminaison dans Postman

1.  **Coller la commande cURL dans Postman**

    Ouvrez Postman et collez la commande cURL suivante dans la section **Import**. Postman configure la requête automatiquement.

    ```bash
    curl -X 'POST' \
      'https://api.docbits.com/prod-api/import/purchase_order_bod' \
      -H 'accept: application/json' \
      -H 'X-API-KEY:' \
      -H 'Content-Type: multipart/form-data' \
      -F 'org_id=' \
      -F 'sub_org_id=' \
      -F 'file=@file.xml;type=text/xml' \
      -F 'custom_fields_mapping='
    ```

    <figure><img src="https://raw.githubusercontent.com/FELLOWPRO/DocBits_Documentation/refs/heads/main/public_docs/.gitbook/assets/test_bod_connection_postman_4.png" alt="L'écran de démarrage de Postman avec les boutons Import et New dans la barre supérieure."><figcaption><p>Dans Postman, le bouton <strong>Import</strong> se trouve dans la barre supérieure de la fenêtre.</p></figcaption></figure>

    <figure><img src="https://raw.githubusercontent.com/FELLOWPRO/DocBits_Documentation/refs/heads/main/public_docs/.gitbook/assets/test_bod_connection_postman_5.png" alt="La fenêtre Import de Postman avec le champ Paste cURL to import."><figcaption><p>Dans la fenêtre <strong>Import</strong>, collez la commande cURL ci-dessus dans le champ <strong>Paste cURL to import</strong>. Postman en fait une requête prête à l'emploi.</p></figcaption></figure>
2.  **Définir la clé API**\
    Allez dans l'onglet **Headers**, repérez l'en-tête `X-API-KEY` et collez votre clé API dans la colonne **Value**.

    <figure><img src="https://raw.githubusercontent.com/FELLOWPRO/DocBits_Documentation/refs/heads/main/public_docs/.gitbook/assets/test_bod_connection_postman_6.png" alt="La requête importée dans Postman avec l'onglet Headers ouvert et la ligne d'en-tête X-API-KEY."><figcaption><p>L'onglet <strong>Headers</strong> de la requête importée. Collez la clé API copiée dans DocBits dans la colonne <strong>Value</strong> de la ligne <code>X-API-KEY</code>.</p></figcaption></figure>
3.  **Téléverser le fichier BOD**\
    Allez dans l'onglet **Body**, repérez la clé `file`, puis cliquez sur **Select Files** dans la colonne **Value** et sélectionnez votre fichier BOD XML.

    <figure><img src="https://raw.githubusercontent.com/FELLOWPRO/DocBits_Documentation/refs/heads/main/public_docs/.gitbook/assets/test_bod_connection_postman_7.png" alt="La requête Postman avec l'onglet Body ouvert en mode form-data et le bouton Select Files sur la ligne file."><figcaption><p>L'onglet <strong>Body</strong> en mode <strong>form-data</strong>. Sur la ligne <code>file</code>, cliquez sur <strong>Select Files</strong> et choisissez le fichier BOD XML à tester.</p></figcaption></figure>
4.  **Envoyer la requête**\
    Cliquez sur **Send** pour effectuer l'appel API.

    <figure><img src="https://raw.githubusercontent.com/FELLOWPRO/DocBits_Documentation/refs/heads/main/public_docs/.gitbook/assets/test_bod_connection_postman_8.png" alt="La requête Postman complétée avec le bouton Send dans la barre de requête."><figcaption><p>Une fois la clé et le fichier renseignés, cliquez sur <strong>Send</strong> pour exécuter la requête sur l'API DocBits.</p></figcaption></figure>
5.  **Vérifier la réponse**\
    Vérifiez la réponse pour confirmer que votre BOD a été traité avec succès.

    <figure><img src="https://raw.githubusercontent.com/FELLOWPRO/DocBits_Documentation/refs/heads/main/public_docs/.gitbook/assets/test_bod_connection_postman_9.png" alt="Le volet de réponse de Postman avec le statut 200 OK et un corps JSON contenant success true."><figcaption><p>Un appel réussi renvoie <strong>200 OK</strong> et un corps JSON contenant <code>"success": true</code> — le BOD a été traité.</p></figcaption></figure>
