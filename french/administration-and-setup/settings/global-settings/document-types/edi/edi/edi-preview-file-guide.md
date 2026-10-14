# Guide de fichier d'aperçu EDI

## 1. Aperçu

Le **Fichier d'aperçu** définit comment les données XML structurées sont rendues dans un format lisible par l'homme, de style PDF. Il combine **HTML et CSS** pour la présentation visuelle et utilise des déclarations **XSLT** `**select**` pour insérer dynamiquement des données du XML personnalisé. Cet aperçu est affiché lors de la **validation des champs** et est également inclus lorsque les documents sont exportés vers **IDM**.

## 2. Objectif et Fonction

* Convertit le XML personnalisé lisible par la machine en un aperçu formaté visuellement (PDF).
* Permet la révision conviviale et la validation des données extraites.
* Assure un rendu cohérent des champs clés du document tels que les en-têtes, les tableaux, les totaux, etc.
* Construit en utilisant **HTML + CSS** pour la mise en page et le design, et **XSLT** pour lier les données à la mise en page.

## 3. Accès et Édition de base

#### **Accéder au fichier :**

1.  Allez dans **Paramètres** → **Type de document** → _\[Votre document (par exemple, Bon de commande)]_ → **E-Doc**.

    ![](https://docs.docbits.com/~gitbook/image?url=https%3A%2F%2F578966019-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FT2n2w4uDCJvv7CJ5zrdk%252Fuploads%252Ff6zyL0AvmqSvrogZdnox%252Fimage.png%3Falt%3Dmedia%26token%3D6bc9ab55-6ee9-43d1-b576-4c5833c208cf\&width=768\&dpr=4\&quality=100\&sign=a23de442\&sv=2)
2. Sous l'onglet **E-Doc**, sélectionnez votre format (par exemple, **EDI**).
3.  Cliquez sur **Aperçu** pour afficher ou modifier le fichier.

    ![](https://docs.docbits.com/~gitbook/image?url=https%3A%2F%2F578966019-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FT2n2w4uDCJvv7CJ5zrdk%252Fuploads%252Fdo1R389GeSqFuZKLD0OP%252Fimage.png%3Falt%3Dmedia%26token%3D930903d4-44af-4188-b015-c60c2dd9d9ab\&width=768\&dpr=4\&quality=100\&sign=77bbb2ce\&sv=2)

#### **Gestion des brouillons :**

* **Créer un brouillon :** Cliquez sur l'icône ✏️ crayon.
* **Supprimer les brouillons :** Utilisez l'icône 🗑️ poubelle pour supprimer les brouillons inutilisés.
* **Activer les modifications :** Cliquez sur la coche ✅ pour publier une version.
  * **Remarque** : Activer une nouvelle version désactivera **automatiquement** la précédente.

## 4. Éditeur HTML/XSLT/CSS

Le **Fichier d'aperçu** est édité dans un éditeur dédié qui prend en charge HTML, XSLT et CSS.

* **HTML** définit la structure du document de sortie (par exemple, tables, divs, mise en page).
* **CSS** contrôle le style (par exemple, polices, espacement, couleurs, alignement).
*   Les déclarations **XSLT** `**select**` sont utilisées pour peupler dynamiquement les champs du XML personnalisé, tels que :

    Copy

    ```
    <xsl:value-of select="/PURCHASE_ORDER/PURCHASE_ORDER_NUMBER/text()" />
    ```
* Vous pouvez également utiliser la **logique XSLT** (`<xsl:if>`, `<xsl:for-each>`, etc.) pour gérer l'affichage conditionnel ou itérer sur les éléments de ligne.

## 5. Fonction d'aperçu (Rendu de sortie)

La fonction d'aperçu vous permet de tester et de vérifier comment un document EDI est rendu avec le Fichier d'aperçu actuel.

#### **Utilisation :**

* Téléchargez un fichier EDI via le processus de téléchargement standard.
* Copiez l'**ID du document** du fichier téléchargé.
* Accédez à l'interface **Aperçu**.
* Ouvrez la **Fonction d'aperçu**.\
  \
  &#x20;![](https://docs.docbits.com/~gitbook/image?url=https%3A%2F%2F578966019-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FT2n2w4uDCJvv7CJ5zrdk%252Fuploads%252F9lddYJl2G4tzpdr9RD5F%252Fimage.png%3Falt%3Dmedia%26token%3Df7663f70-ef10-4e64-bbdc-41048ed8352a\&width=300\&dpr=4\&quality=100\&sign=36ce2b93\&sv=2)
* Entrez l'ID du document et cliquez sur **Tester**.
* L'aperçu de style PDF rendu sera affiché en utilisant la configuration HTML/CSS/XSLT.

Cette fonction est cruciale pour le débogage des liaisons de données, l'affinement de la mise en page et pour garantir que le document est à la fois précis et visuellement clair pour les utilisateurs et les systèmes en aval comme **IDM**.

![](https://docs.docbits.com/~gitbook/image?url=https%3A%2F%2F578966019-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FT2n2w4uDCJvv7CJ5zrdk%252Fuploads%252FJH103tnbqZjuimpOniVg%252Fimage.png%3Falt%3Dmedia%26token%3D4e63cc09-b0de-488f-bdd0-ee5a9246a371\&width=768\&dpr=4\&quality=100\&sign=bfff5bba\&sv=2)

## 6. Guide vidéo

Un guide vidéo pour ce type de fichier est disponible sur la [page Vidéos.](https://docs.docbits.com/administration-and-setup/settings/global-settings/document-types/edi/edi/edi-videos) Utilisez-le pour suivre la configuration, l'édition et l'aperçu.
