# Testez votre connexion BOD avec Postman

## Aperçu

Cette page explique comment vérifier le traitement réussi de votre BOD (Business Object Document) en utilisant Postman. Vous allez tester le point de terminaison API pertinent en envoyant une requête avec votre fichier de mappage BOD. Suivez les étapes ci-dessous pour compléter le processus.

## Accéder à votre Clé API et Fichier de mappage BOD

### Récupérer votre Clé API

1.  Allez dans **Paramètres → Paramètres globaux → Intégration et SSO**.

    ![Page de paramètres dans DocBits avec la navigation Global Settings ouverte et Integrations & SSO en surbrillance entre Document Types et Email Templates](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/settings_integration.png)
2.  Vous pouvez soit copier manuellement votre **clé API**, soit cliquer sur le bouton de copie pour la copier dans votre presse-papiers.

    ![Page Integration & SSO dans DocBits affichant le champ API Key avec son bouton de copie au-dessus de la section SSO Service Provider Settings](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/test_bod_connection_postman_1.png)

### **Télécharger le Fichier de mappage BOD**

1.  Allez dans **Paramètres → Traitement des documents → Exporter**.

    ![Page de paramètres dans DocBits avec la navigation Document Processing ouverte listant Import, OCR Settings, Classification and Extraction et Module](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/settings_export.png)
2.  Dans la colonne **Actions** de l'entrée d'exportation pertinente, cliquez sur le menu à trois points et sélectionnez **Éditer**.

    ![Page Export settings dans DocBits avec les lignes google Invoice webhook et Infor LN Test Invoice et le menu Actions ouvert](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/test_bod_connection_postman_2.png)
3.  Localisez le **Fichier de mappage BOD** et cliquez sur le bouton **Télécharger** pour l'enregistrer.

    ![Boîte de dialogue Infor ION avec le champ Title Test et les boutons de téléchargement ION-Mapping File, IDM Mapping File et BOD-Mapping File](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/test_bod_connection_postman_3.png)

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

    ![Espace de travail Postman avec l'écran d'accueil, l'onglet History et l'option Create a new request](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/test_bod_connection_postman_4.png)

    ![Boîte de dialogue Import de Postman avec le champ de collage cURL ouvert pour importer la requête BOD](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/test_bod_connection_postman_5.png)
2.  **Définissez la Clé API**\
    Allez dans l'onglet **Headers**, localisez l'en-tête `X-API-KEY` et collez votre clé API dans la colonne **Value**.

    ![Requête Postman pour https://api.docbits.com/prod-api/import/purchase_order_bod avec l'onglet Headers et la ligne X-API-KEY](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/test_bod_connection_postman_6.png)
3.  **Téléchargez le Fichier BOD**\
    Allez dans l'onglet **Body**, localisez la clé `file`, puis cliquez sur **Select Files** dans la colonne **Value** et téléchargez votre fichier BOD XML.

    ![Onglet Body de la requête Postman avec les clés form-data org_id, sub_org_id, file avec Select Files et custom_fields_mapping](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/test_bod_connection_postman_7.png)
4.  **Envoyez la Requête**\
    Cliquez sur **Send** pour effectuer l'appel API.

    ![Requête Postman avec l'onglet Authorization ouvert et No Auth sélectionné](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/test_bod_connection_postman_8.png)
5.  **Vérifiez la Réponse**\
    Vérifiez la réponse pour confirmer que votre BOD a été traité avec succès.

    ![Volet de réponse Postman avec le statut 200 OK et le message du corps BOD processed successfully](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/test_bod_connection_postman_9.png)
