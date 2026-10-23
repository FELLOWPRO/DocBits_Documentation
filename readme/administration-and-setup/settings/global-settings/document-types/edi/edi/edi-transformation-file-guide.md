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

    ![Éditeur du type de document Purchase Order avec les onglets Edit layout, Document Sub Types, Table columns, Fields, Model Training, Regex, Scripts et E-Doc](https://docs.docbits.com/~gitbook/image?url=https%3A%2F%2F578966019-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FT2n2w4uDCJvv7CJ5zrdk%252Fuploads%252F1yCRagLzRFmy2hPRDDc1%252Fimage.png%3Falt%3Dmedia%26token%3D020874a9-1eae-4965-9dd2-c23461fc5884\&width=768\&dpr=4\&quality=100\&sign=5e53a730\&sv=2)
2. Sous l'onglet **E-Doc**, sélectionnez votre format (par ex., **EDI**).
3.  Cliquez sur **Transformation** pour afficher ou éditer.

    ![Onglet EDI E-Doc affichant les fichiers Transformation et Preview XSLT ainsi que les entrées Extraction Paths et Purchase Order BOD](https://docs.docbits.com/~gitbook/image?url=https%3A%2F%2F578966019-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FT2n2w4uDCJvv7CJ5zrdk%252Fuploads%252FZtaE4dZT9E1exWMZ5FCI%252Fimage.png%3Falt%3Dmedia%26token%3D787868b4-47b4-455e-9a26-112f692b91f3\&width=768\&dpr=4\&quality=100\&sign=460124f1\&sv=2)

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


    <div align="left"><img src="https://docs.docbits.com/~gitbook/image?url=https%3A%2F%2F578966019-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FT2n2w4uDCJvv7CJ5zrdk%252Fuploads%252F9lddYJl2G4tzpdr9RD5F%252Fimage.png%3Falt%3Dmedia%26token%3Df7663f70-ef10-4e64-bbdc-41048ed8352a&#x26;width=768&#x26;dpr=4&#x26;quality=100&#x26;sign=36ce2b93&#x26;sv=2" alt="Panneau d'aperçu d'Extraction paths avec un sélecteur de documents affichant 29 documents et un bouton Preview" width="375"></div>
* Entrez l'**ID du Document** dans le champ et appuyez sur **Tester**.
* Le **XML transformé en sortie** sera affiché.

Ceci est particulièrement utile pour déboguer les correspondances XSLT et s'assurer que la structure XML finale répond à vos exigences de format.

![Vue de test Transformation XSLT affichant la feuille de style avec sélecteurs de valeurs EDI et le XML du bon de commande transformé avec lignes de commande et totaux](https://docs.docbits.com/~gitbook/image?url=https%3A%2F%2F578966019-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FT2n2w4uDCJvv7CJ5zrdk%252Fuploads%252FWbwwmXgp6nRPIb1zBpgj%252Fimage.png%3Falt%3Dmedia%26token%3Dab5766f1-45bf-484e-9aa4-ab3059705591\&width=768\&dpr=4\&quality=100\&sign=46905864\&sv=2)

## 6. Guide Vidéo

Un guide vidéo pour ce type de fichier est disponible sur la [page Vidéos.](https://docs.docbits.com/administration-and-setup/settings/global-settings/document-types/edi/edi/edi-videos) Utilisez-le pour suivre la configuration, l'édition et la prévisualisation.

## Règles effectivement utilisées et activation

Les règles propres à l’organisation ont priorité sur celles par défaut pour le format eDoc détecté. Vérifiez la TRANSFORMATION active et vérifiez quel nœud fournit invoice_type dans le XML transformé ; le chemin dépend du format. Save enregistre un brouillon ; utilisez la coche pour l’activer après les tests. Le rendu Preview ne prouve pas le type de document enregistré. Consultez le [guide de diagnostic de la classification](../credit-note-recognized-as-invoice.md) pour les codes 381/261, les scripts suivants et les précautions à prendre avant un retraitement.


<figure><img src="../../../../../../.gitbook/assets/site-all-edi-list-fr.png" alt="Format EDI existant avec ses quatre attributs configurés."><figcaption><p>Format EDI existant avec ses quatre attributs configurés.</p></figcaption></figure>

<figure><img src="../../../../../../.gitbook/assets/site-all-edi-transformation-fr.png" alt="Attribut TRANSFORMATION actif : code source XSLT pour transformer le XML intermédiaire."><figcaption><p>Attribut TRANSFORMATION actif : code source XSLT pour transformer le XML intermédiaire.</p></figcaption></figure>


Les vues montrent une configuration et une version existantes. Les paramètres varient selon le type de document et le format. Validez les modifications dans un brouillon avant leur activation.

Dans la version de l’interface illustrée, certaines mentions, telles que Custom et Default, restent en anglais. Les identifiants techniques des attributs et le code de configuration restent inchangés.
