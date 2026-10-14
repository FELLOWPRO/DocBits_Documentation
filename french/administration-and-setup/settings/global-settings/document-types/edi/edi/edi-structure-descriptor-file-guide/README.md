# Guide du fichier de description de la structure EDI

## **1. Aperçu**

Le **Fichier de Description de la Structure** définit comment les segments EDI répétitifs (par exemple, `N1`–`N4`) sont regroupés en JSON structuré. Il garantit :

* **Analyse précise** des éléments liés en tant qu'unités uniques.
* **Sortie cohérente** pour les systèmes en aval.

_Pour un exemple complet avec des détails de segment, consultez_ [_Exemple de Description de la Structure_](edi-structure-descriptor.md)_._

## **2. Accès et Édition de Base**

#### **Accéder au Fichier**

1.  **Paramètres** → **Type de Document** → \[Votre Document (par exemple, _Bon de Commande_)] → **E-Doc.**

    ![](https://docs.docbits.com/~gitbook/image?url=https%3A%2F%2F578966019-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FT2n2w4uDCJvv7CJ5zrdk%252Fuploads%252Ff6zyL0AvmqSvrogZdnox%252Fimage.png%3Falt%3Dmedia%26token%3D6bc9ab55-6ee9-43d1-b576-4c5833c208cf\&width=768\&dpr=4\&quality=100\&sign=a23de442\&sv=2)
2. Sous **E-Doc**, sélectionnez votre format (par exemple, _EDI_ ).
3.  Cliquez sur **Description de la Structure**.

    ![](https://docs.docbits.com/~gitbook/image?url=https%3A%2F%2F578966019-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FT2n2w4uDCJvv7CJ5zrdk%252Fuploads%252FOuNVhIuYBPJTu4PdMecy%252Fimage.png%3Falt%3Dmedia%26token%3Dd111b34e-0dd9-4436-9df4-f59490ac0d87\&width=768\&dpr=4\&quality=100\&sign=6e8e9f0e\&sv=2)

#### **Gestion des Brouillons**

* **Créer un Brouillon** : Cliquez sur l'icône ✏️ pour commencer l'édition.
* **Supprimer les Brouillons** : Utilisez l'icône 🗑️ pour supprimer les brouillons inutilisés.
* **Activer les Modifications** : Cliquez sur l'icône ✅ pour approuver et publier vos modifications.
  * **Remarque** : Activer une nouvelle version désactivera **automatiquement** la précédente.

## 3. Fonction d'Aperçu (Aperçu XML analysé)

La **Fonction d'Aperçu** vous permet de tester et de prévisualiser comment un fichier EDI téléchargé est analysé en utilisant le Fichier de Description de la Structure actuel.

#### Utilisation

* Téléchargez un fichier EDI via le flux de téléchargement standard.
* Copiez l'**ID du Document** du fichier téléchargé.
* Accédez à l'interface du **Fichier de Description de la Structure**.
*   Ouvrez la **Fonction d'Aperçu**.\


    <div align="left"><img src="https://docs.docbits.com/~gitbook/image?url=https%3A%2F%2F578966019-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FT2n2w4uDCJvv7CJ5zrdk%252Fuploads%252F9lddYJl2G4tzpdr9RD5F%252Fimage.png%3Falt%3Dmedia%26token%3Df7663f70-ef10-4e64-bbdc-41048ed8352a&#x26;width=768&#x26;dpr=4&#x26;quality=100&#x26;sign=36ce2b93&#x26;sv=2" alt="" width="375"></div>
* Entrez l'**ID du Document** dans le champ et appuyez sur **Tester**.
* La **sortie XML structurée résultante** sera affichée.

Ceci est particulièrement utile pour le débogage des mappages et la validation des regroupements structurels en temps réel.

![](https://docs.docbits.com/~gitbook/image?url=https%3A%2F%2F578966019-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FT2n2w4uDCJvv7CJ5zrdk%252Fuploads%252FBXU6zeFapt7ZIVFl37Iz%252Fimage.png%3Falt%3Dmedia%26token%3D9d51e329-b781-4781-a527-3258f6f933c6\&width=768\&dpr=4\&quality=100\&sign=4ca17281\&sv=2)

## 6. Guide Vidéo

Un guide vidéo pour ce type de fichier est disponible sur la [page Vidéos.](https://docs.docbits.com/administration-and-setup/settings/global-settings/document-types/edi/edi/edi-videos) Utilisez-le pour suivre la configuration, l'édition et la prévisualisation.
