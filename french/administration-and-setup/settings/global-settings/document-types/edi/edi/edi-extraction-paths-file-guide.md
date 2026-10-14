# Guide du fichier des chemins d'extraction EDI

## 1. Aperçu

Le **Fichier des chemins d'extraction** définit comment les données sont extraites du **XML structuré** dans des champs de document spécifiques et des tables dans l'interface. Il associe les **identifiants de champ** aux **expressions XPath**, qui sont évaluées pour extraire des valeurs du XML dans les champs de document correspondants. Ce fichier joue un rôle crucial pour garantir que les données extraites apparaissent correctement lors de la validation des champs et du traitement en aval.

## 2. Objectif et Fonction

* Associe chaque champ de document et colonne de table à un emplacement spécifique dans le XML structuré en utilisant des expressions XPath.
* Garantit que les valeurs correctes sont renseignées dans des champs tels que `order_number`, `supplier_name` et `total_amount`.
* Prend en charge à la fois les **champs simples** (via un objet `fields`) et les **tables** (via un tableau `tables` avec des chemins de ligne et des correspondances de colonnes).
* Permet un contrôle précis sur la manière dont les données sont extraites du XML, y compris l'utilisation de fonctions XPath comme `sum()`.

Exemple de mappage de champ :

Copier

```
"order_number": "//PURCHASE_ORDER/PURCHASE_ORDER/text()"
```

## 3. Accès et Édition de base

#### **Accès au fichier :**

1.  Accédez à **Paramètres** → **Type de document** → _\[Votre document (par exemple, Bon de commande)]_ → **E-Doc**.

    ![](https://docs.docbits.com/~gitbook/image?url=https%3A%2F%2F578966019-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FT2n2w4uDCJvv7CJ5zrdk%252Fuploads%252Ff6zyL0AvmqSvrogZdnox%252Fimage.png%3Falt%3Dmedia%26token%3D6bc9ab55-6ee9-43d1-b576-4c5833c208cf\&width=768\&dpr=4\&quality=100\&sign=a23de442\&sv=2)
2. Sous l'onglet **E-Doc**, sélectionnez votre format (par exemple, **EDI**).
3.  Cliquez sur **Chemins d'extraction** pour afficher ou modifier le fichier.

    ![](https://docs.docbits.com/~gitbook/image?url=https%3A%2F%2F578966019-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FT2n2w4uDCJvv7CJ5zrdk%252Fuploads%252FawwG5QnErp1yy1eYHrlX%252Fimage.png%3Falt%3Dmedia%26token%3D46a6d8b3-52d2-4c13-bc72-1a74955efd9f\&width=768\&dpr=4\&quality=100\&sign=e612882b\&sv=2)

#### **Gestion des brouillons :**

* **Créer un brouillon :** Cliquez sur l'icône ✏️.
* **Supprimer les brouillons :** Utilisez l'icône 🗑️ pour supprimer les brouillons inutilisés.
* **Activer les modifications :** Cliquez sur la coche ✅ pour publier une version.
  * **Remarque** : Activer une nouvelle version désactivera **automatiquement** la précédente.

## 4. Éditeur et Syntaxe

Le Fichier des chemins d'extraction est écrit en **JSON** et contient deux composants principaux :

* **fields** : Un dictionnaire où chaque clé est un identifiant de champ et chaque valeur est une expression XPath qui définit comment extraire les données.
* **tables** : Une liste de définitions de table qui incluent :
  * `name` : L'identifiant de la table.
  * `row_path` : Un XPath qui identifie chaque ligne de la table.
  * `columns` : Une liste de correspondances de colonnes (`name`, `path`).

Vous pouvez également utiliser des fonctions XPath (par exemple, `sum()`) et des expressions pour calculer des valeurs dynamiquement à partir d'éléments répétés.

Copier

```
jsonCopyEdit"total_net_amount": "sum(//PURCHASE_ORDER/ORDER_LINES/ORDER_LINE/SUB_TOTAL)"
```

## 5. Fonction d'aperçu (Évaluer l'extraction)

La **Fonction d'aperçu** vous permet de simuler le comportement des chemins d'extraction avec un document réellement téléchargé.

**Utilisation :**

* Téléchargez un fichier EDI via le processus de téléchargement standard.
* Copiez l'**ID du document**.
* Accédez à l'interface des **Chemins d'extraction**.
* Ouvrez la **Fonction d'aperçu**.\
  \
  ![](https://docs.docbits.com/~gitbook/image?url=https%3A%2F%2F578966019-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FT2n2w4uDCJvv7CJ5zrdk%252Fuploads%252F9lddYJl2G4tzpdr9RD5F%252Fimage.png%3Falt%3Dmedia%26token%3Df7663f70-ef10-4e64-bbdc-41048ed8352a\&width=300\&dpr=4\&quality=100\&sign=36ce2b93\&sv=2)
* Entrez l'ID du document et cliquez sur **Tester**.
* Le résultat montrera comment chaque champ et table est renseigné en fonction des chemins configurés.

Cette fonction est essentielle pour vérifier que vos expressions XPath sont correctement définies et extraient les valeurs attendues avant d'activer le brouillon.

![](https://docs.docbits.com/~gitbook/image?url=https%3A%2F%2F578966019-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FT2n2w4uDCJvv7CJ5zrdk%252Fuploads%252F81uvH6FFVBJsSZucanWY%252Fimage.png%3Falt%3Dmedia%26token%3Dde3ba545-1ee3-44b2-a629-9660d80174f2\&width=768\&dpr=4\&quality=100\&sign=43c8b507\&sv=2)

## 6. Guide vidéo

Un guide vidéo pour ce type de fichier est disponible sur la [page des vidéos.](https://docs.docbits.com/administration-and-setup/settings/global-settings/document-types/edi/edi/edi-videos) Utilisez-le pour suivre la configuration, l'édition et l'aperçu.
