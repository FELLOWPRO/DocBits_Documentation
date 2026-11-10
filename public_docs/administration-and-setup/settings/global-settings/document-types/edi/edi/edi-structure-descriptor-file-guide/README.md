# EDI Structure Descriptor File Guide

## 1. Overview

Le **Structure Descriptor File** est un fichier **JSON** qui définit comment les segments EDI répétitifs (par exemple `N1`–`N4`) sont regroupés en une sortie structurée. Il constitue la première étape du traitement EDI :

* **Analyse précise** des segments liés en tant qu'unités uniques.
* **Sortie cohérente** pour la [Transformation](../edi-transformation-file-guide.md) et les systèmes en aval.

_Pour un exemple complet avec le détail des segments, consultez_ [_Structure Descriptor Example_](edi-structure-descriptor.md)_._

## 2. Access & Basic Editing

#### **Accéder au fichier**

1. Accédez à **Settings** → **Document Types** et ouvrez **E-Doc** pour le type de document que vous souhaitez configurer (par exemple _Purchase Order_). Vous devez disposer d'un accès administrateur au sein de votre organisation pour modifier ces fichiers.

    <!-- dbdc-139-edi-sd-list-en.png --><figure><img src="https://raw.githubusercontent.com/FELLOWPRO/DocBits_Documentation/refs/heads/main/public_docs/.gitbook/assets/dbdc-139-edi-sd-list-en.png" alt="Page E-Doc de la sandbox en anglais avec le format EDI déplié et la ligne JSON STRUCTURE DESCRIPTOR listée au-dessus de TRANSFORMATION, PREVIEW et EXTRACTION PATHS"><figcaption>Ouvrez E-Doc pour votre type de document ; le format EDI liste ses fichiers de configuration.</figcaption></figure>

2. Dépliez le format **EDI**. Ses fichiers de configuration sont listés ensemble : **STRUCTURE DESCRIPTOR**, **TRANSFORMATION**, **PREVIEW** et **EXTRACTION PATHS**.
3. Cliquez sur la ligne **STRUCTURE DESCRIPTOR**, marquée **JSON**, pour l'ouvrir.

#### **Gestion des brouillons**

La colonne de gauche affiche la liste des **Version** du fichier. La version marquée **Active** est celle utilisée par DocBits.

* **Créer un brouillon** : cliquez sur l'icône crayon ✏️ à côté de la version active pour commencer la modification. Le fichier actif lui-même ne peut pas être modifié directement.
* **Supprimer des brouillons** : utilisez l'icône corbeille 🗑️ pour supprimer les brouillons inutilisés.
* **Activer les modifications** : cliquez sur l'icône de validation ✅ d'un brouillon pour approuver et publier vos modifications.
  * <mark style="color:red;">**Note**</mark> : l'activation d'une nouvelle version **désactive automatiquement** la précédente.

<!-- dbdc-139-edi-sd-detail-en.png --><figure><img src="https://raw.githubusercontent.com/FELLOWPRO/DocBits_Documentation/refs/heads/main/public_docs/.gitbook/assets/dbdc-139-edi-sd-detail-en.png" alt="Éditeur JSON Structure Descriptor de la sandbox en anglais avec la liste des versions à gauche, la version 1 marquée Active et une icône crayon permettant de créer un brouillon"><figcaption>Le fichier Structure Descriptor et sa liste des versions ; le crayon crée un brouillon que vous pouvez modifier.</figcaption></figure>

## 3. Preview Function (Preview Parsed Output)

La **Preview Function** vous permet de tester comment un fichier EDI importé est analysé avec le Structure Descriptor actuellement affiché, avant d'activer une quelconque modification.

#### Utilisation

* Importez un fichier EDI via le flux d'import standard.
* Copiez le **Document ID** du fichier importé.
* Ouvrez le fichier **Structure Descriptor** comme décrit ci-dessus.
* Cliquez sur **Preview** en haut à droite pour ouvrir le panneau de test.

    <div align="left"><!-- dbdc-139-edi-sd-preview-en.png --><figure><img src="https://raw.githubusercontent.com/FELLOWPRO/DocBits_Documentation/refs/heads/main/public_docs/.gitbook/assets/dbdc-139-edi-sd-preview-en.png" alt="Page Structure Descriptor de la sandbox en anglais avec le panneau de test Preview ouvert, montrant le champ de saisie Document Id et le bouton Test" width="560"><figcaption>Le panneau de test : saisissez un Document ID et cliquez sur Test.</figcaption></figure></div>

* Saisissez le **Document ID** dans le champ et cliquez sur **Test**.
* La **sortie structurée** obtenue s'affiche à côté de l'éditeur.

Cette fonction est particulièrement utile pour déboguer les mappages et valider les regroupements structurels en temps réel. Un document EDI représentatif de votre propre format est nécessaire ; le résultat affiché dépend du fichier importé.

## 4. Video Walkthrough

Un guide vidéo pour ce type de fichier est disponible sur la [page Videos.](../edi-videos.md)\
Utilisez-le pour suivre pas à pas la configuration, la modification et l'usage de Preview.

Les vues présentent une configuration et une version existantes. Les paramètres varient selon le type de document et le format. Validez les modifications dans un brouillon avant l'activation.
