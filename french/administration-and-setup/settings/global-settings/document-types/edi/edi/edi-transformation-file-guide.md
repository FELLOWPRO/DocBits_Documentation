# Guide de fichier de transformation EDI

## 1. Aperçu

Le **Fichier de Transformation** définit comment le XML structuré—créé à l'aide du **Fichier de Descripteur de Structure**—est converti en un format XML personnalisé qui correspond aux exigences spécifiques de formulaire ou de type de document de votre organisation.

Cette transformation est effectuée à l'aide de **XSLT (Transformations de Feuilles de Style Extensibles)**, qui peut être créé et maintenu à travers l'**Éditeur XSLT** dans l'interface DocBits.

## 2. Objectif et Fonction

* Transforme le **XML intermédiaire** (sortie du Descripteur de Structure) en un **XML final** aligné avec votre schéma de document.
* Permet la flexibilité pour s'adapter aux formats de partenaires EDI variés et aux exigences internes du système.
* Construit en utilisant des **règles XSLT**, qui vous permettent de définir des correspondances, des formats de valeur, de la logique conditionnelle et de la structure.

## 3. Accès et Édition de Base

#### Accéder au Fichier

1.  Allez dans **Paramètres → Type de Document** → \[Votre Document (par ex., _Bon de Commande_)] → **E-Doc.**

    ![](https://docs.docbits.com/~gitbook/image?url=https%3A%2F%2F578966019-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FT2n2w4uDCJvv7CJ5zrdk%252Fuploads%252F1yCRagLzRFmy2hPRDDc1%252Fimage.png%3Falt%3Dmedia%26token%3D020874a9-1eae-4965-9dd2-c23461fc5884\&width=768\&dpr=4\&quality=100\&sign=5e53a730\&sv=2)
2. Sous l'onglet **E-Doc**, sélectionnez votre format (par ex., **EDI**).
3.  Cliquez sur **Transformation** pour afficher ou éditer.

    ![](https://docs.docbits.com/~gitbook/image?url=https%3A%2F%2F578966019-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FT2n2w4uDCJvv7CJ5zrdk%252Fuploads%252FZtaE4dZT9E1exWMZ5FCI%252Fimage.png%3Falt%3Dmedia%26token%3D787868b4-47b4-455e-9a26-112f692b91f3\&width=768\&dpr=4\&quality=100\&sign=460124f1\&sv=2)

#### Gestion des Brouillons

* **Créer un Brouillon** : Cliquez sur l'icône ✏️.
* **Supprimer les Brouillons** : Utilisez l'icône 🗑️ pour supprimer les brouillons inutilisés.
* **Activer les Changements** : Cliquez sur la coche ✅ pour publier une version.
  * **Remarque** : Activer une nouvelle version désactivera **automatiquement** la précédente.

## 4. Éditeur XSLT

Le Fichier de Transformation est édité à l'aide d'un **Éditeur XSLT** intégré qui prend en charge la coloration syntaxique et la validation.

* Ajoutez des modèles pour mapper des chemins spécifiques du XML d'entrée à la structure souhaitée.
* Utilisez la logique conditionnelle (par ex., `<xsl:if>`, `<xsl:choose>`) pour gérer les formats de données optionnels ou variés.
* Appliquez des fonctions de formatage au besoin (par ex., manipulation de chaînes, formatage de dates).

## 5. Fonction d'Aperçu (Aperçu du XML Transformé)

La **Fonction d'Aperçu** vous permet de tester et de prévisualiser comment un fichier EDI téléchargé est traité en utilisant le **Fichier de Transformation** actuel.

#### Utilisation

* Téléchargez un fichier EDI via le flux de téléchargement standard.
* Copiez l'**ID du Document** du fichier téléchargé.
* Accédez à l'interface du **Fichier de Transformation**.
*   Ouvrez la **Fonction d'Aperçu**.\


    <div align="left"><img src="https://docs.docbits.com/~gitbook/image?url=https%3A%2F%2F578966019-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FT2n2w4uDCJvv7CJ5zrdk%252Fuploads%252F9lddYJl2G4tzpdr9RD5F%252Fimage.png%3Falt%3Dmedia%26token%3Df7663f70-ef10-4e64-bbdc-41048ed8352a&#x26;width=768&#x26;dpr=4&#x26;quality=100&#x26;sign=36ce2b93&#x26;sv=2" alt="" width="375"></div>
* Entrez l'**ID du Document** dans le champ et appuyez sur **Tester**.
* Le **XML transformé en sortie** sera affiché.

Ceci est particulièrement utile pour déboguer les correspondances XSLT et s'assurer que la structure XML finale répond à vos exigences de format.

![](https://docs.docbits.com/~gitbook/image?url=https%3A%2F%2F578966019-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FT2n2w4uDCJvv7CJ5zrdk%252Fuploads%252FWbwwmXgp6nRPIb1zBpgj%252Fimage.png%3Falt%3Dmedia%26token%3Dab5766f1-45bf-484e-9aa4-ab3059705591\&width=768\&dpr=4\&quality=100\&sign=46905864\&sv=2)

## 6. Guide Vidéo

Un guide vidéo pour ce type de fichier est disponible sur la [page Vidéos.](https://docs.docbits.com/administration-and-setup/settings/global-settings/document-types/edi/edi/edi-videos) Utilisez-le pour suivre la configuration, l'édition et la prévisualisation.
