# Modèles d'e-mails

## **Aperçu**

Les modèles d'e-mails vous permettent de personnaliser les notifications par e-mail automatisées envoyées depuis DocBits. Les modèles peuvent inclure des champs dynamiques (par exemple, `{{FieldID}}`), des images et une mise en forme HTML.

## **Accès aux modèles d'e-mails**

1.  Accédez à : **Paramètres → Paramètres globaux → Modèles d'e-mails**

    ![](https://docs.docbits.com/~gitbook/image?url=https%3A%2F%2F578966019-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FT2n2w4uDCJvv7CJ5zrdk%252Fuploads%252FWzjaI1Jinpw0PQHCuwM0%252Fimage.png%3Falt%3Dmedia%26token%3D21f7af41-6ebe-4e25-952f-9ae0b11cade2\&width=768\&dpr=4\&quality=100\&sign=ae789081\&sv=2)
2. Le tableau de bord affiche tous les modèles avec :
   * **Nom**
   * **Sujet**
   * Date de **Dernière modification**
   * **Actions** (Modifier ou Supprimer).

![](https://docs.docbits.com/~gitbook/image?url=https%3A%2F%2F578966019-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FT2n2w4uDCJvv7CJ5zrdk%252Fuploads%252FENN4zipGg75mpi2OooPP%252Fimage.png%3Falt%3Dmedia%26token%3Ddff6d8a8-e5b3-4e52-bee1-e311daba7b64\&width=768\&dpr=4\&quality=100\&sign=4202a84f\&sv=2)

## **Création d'un nouveau modèle**

### **1 Configuration de base**

* Cliquez sur **Nouveau**.
* Remplissez les champs sur la droite :
  * **Nom** : Identifiant du modèle (par exemple, "Erreur de document").
  * **Sujet** : Ligne d'objet de l'e-mail (par exemple, "Action requise : Erreur de document").
  *   **Type de document** : Sélectionnez dans la liste déroulante (par exemple, "Facture").

      ![](https://docs.docbits.com/~gitbook/image?url=https%3A%2F%2F578966019-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FT2n2w4uDCJvv7CJ5zrdk%252Fuploads%252FXzmfZBIoyoDS7tTz1qo4%252Fimage.png%3Falt%3Dmedia%26token%3D24547984-2406-41b5-95d6-0f7f45e06258\&width=768\&dpr=4\&quality=100\&sign=f7aa9b89\&sv=2)

### **2 Éditeur de modèle**

* **Menu** : Formatez le texte, ajoutez des liens ou insérez des tableaux.
* **Éditeur HTML** : Cliquez sur l'icône `<>` pour modifier le HTML brut.
* **Ajouter des images** : Utilisez la fonction **Télécharger**.
*   **Champs dynamiques** : Insérez les valeurs des champs de document en

    * **Option de champ variable** : Sélectionnez dans une liste déroulante.
    * **Saisie manuelle** : Tapez `{{FieldID}}` (par exemple, `{{InvoiceNumber}}`).

    ![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/email_templates_4.png)

### **3 Enregistrement**

* Cliquez sur **Enregistrer** pour stocker le modèle.

## **Envoi d'un e-mail de test**

1.  Ouvrez le modèle et cliquez sur **Envoyer un test**.

    ![](https://docs.docbits.com/~gitbook/image?url=https%3A%2F%2F578966019-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FT2n2w4uDCJvv7CJ5zrdk%252Fuploads%252FZTskZNsVfWj6IwBmwoR5%252Fimage.png%3Falt%3Dmedia%26token%3D62229942-2ee7-4d58-833c-eb863b18f2d3\&width=768\&dpr=4\&quality=100\&sign=b804f787\&sv=2)
2. Entrez :
   * **E-mail du destinataire** (obligatoire).
   * **Valeurs des champs** (facultatif ; données fictives pour les espaces réservés). ![](https://docs.docbits.com/~gitbook/image?url=https%3A%2F%2F578966019-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FT2n2w4uDCJvv7CJ5zrdk%252Fuploads%252FO2yw8EgefTPSCIhxUFH6%252Fimage.png%3Falt%3Dmedia%26token%3D2acc0067-3698-4565-92d8-6c4ddabe497c\&width=300\&dpr=4\&quality=100\&sign=461ae8e7\&sv=2)
3. Vérifiez l'e-mail de test et ajustez le modèle si nécessaire.

## **Utilisation des modèles dans les notifications**

Les modèles enregistrés peuvent être liés aux flux de travail de [**Notification par e-mail**](email-notification/) (par exemple, rappels d'approbation, mises à jour de statut).
