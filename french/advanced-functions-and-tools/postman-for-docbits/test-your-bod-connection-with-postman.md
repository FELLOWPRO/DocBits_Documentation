# Testez votre connexion BOD avec Postman

## Aperçu

Cette page explique comment vérifier le traitement réussi de votre BOD (Business Object Document) en utilisant Postman. Vous allez tester le point de terminaison API pertinent en envoyant une requête avec votre fichier de mappage BOD. Suivez les étapes ci-dessous pour compléter le processus.

## Accéder à votre Clé API et Fichier de mappage BOD

### Récupérer votre Clé API

1.  Allez dans **Paramètres → Paramètres globaux → Intégration et SSO**.

    ![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/settings_integration.png)
2.  Vous pouvez soit copier manuellement votre **clé API**, soit cliquer sur le bouton de copie pour la copier dans votre presse-papiers.

    ![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/test_bod_connection_postman_1.png)

### **Télécharger le Fichier de mappage BOD**

1.  Allez dans **Paramètres → Traitement des documents → Exporter**.

    ![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/settings_export.png)
2.  Dans la colonne **Actions** de l'entrée d'exportation pertinente, cliquez sur le menu à trois points et sélectionnez **Éditer**.

    ![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/test_bod_connection_postman_2.png)
3.  Localisez le **Fichier de mappage BOD** et cliquez sur le bouton **Télécharger** pour l'enregistrer.

    ![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/test_bod_connection_postman_3.png)

## Testez le Point de Terminaison dans Postman

1.  **Collez la commande cURL dans Postman**

    Ouvrez Postman et collez la commande cURL suivante dans la section **Import**. Postman configurera automatiquement la requête.

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

    ![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/test_bod_connection_postman_4.png)

    ![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/test_bod_connection_postman_5.png)
2.  **Définissez la Clé API**\
    Allez dans l'onglet **Headers**, localisez l'en-tête `X-API-KEY` et collez votre clé API dans la colonne **Value**.

    ![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/test_bod_connection_postman_6.png)
3.  **Téléchargez le Fichier BOD**\
    Allez dans l'onglet **Body**, localisez la clé `file`, puis cliquez sur **Select Files** dans la colonne **Value** et téléchargez votre fichier BOD XML.

    ![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/test_bod_connection_postman_7.png)
4.  **Envoyez la Requête**\
    Cliquez sur **Send** pour effectuer l'appel API.

    ![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/test_bod_connection_postman_8.png)
5.  **Vérifiez la Réponse**\
    Vérifiez la réponse pour confirmer que votre BOD a été traité avec succès.

    ![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/test_bod_connection_postman_9.png)
