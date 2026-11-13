# Guide du fichier de description de la structure EDI

## 1. Aperçu général

Le **Structure Descriptor File** (fichier de description de la structure) est un fichier **JSON** qui définit comment les segments EDI répétitifs (par exemple `N1`–`N4`) sont regroupés en une sortie structurée. Il constitue la première étape du traitement EDI :

* **Analyse précise** des segments liés, traités comme une seule unité.
* **Sortie cohérente** pour la [Transformation](../edi-transformation-file-guide.md) et les systèmes en aval.

_Pour un exemple complet avec le détail des segments, consultez le_ [_Descripteur de structure EDI_](edi-structure-descriptor.md)_._

## 2. Accès et modification de base

#### **Accéder au fichier**

1. Dans **Paramètres**, ouvrez [Types De Documents](../../../README.md), puis **E-Doc** pour le type de document à configurer (par exemple _Purchase Order_). Pour modifier ces fichiers, vous avez besoin d'un accès administrateur dans votre organisation.

    <figure><img src="../../../../../../../.gitbook/assets/edi-structure-descriptor-file-guide-list-fr-20261114.png" alt="Page E-Doc de la sandbox en français avec le format EDI déplié et les lignes STRUCTURE DESCRIPTOR, TRANSFORMATION, PREVIEW et EXTRACTION PATHS, chacune avec son statut Par défaut, son type JSON ou XSLT et sa date de modification"><figcaption><p>Ouvrez E-Doc pour votre type de document : le format EDI liste ses fichiers de configuration.</p></figcaption></figure>

2. Dépliez le format **EDI**. Ses fichiers de configuration sont listés ensemble : **STRUCTURE DESCRIPTOR**, **TRANSFORMATION**, **PREVIEW** et **EXTRACTION PATHS**.
3. Cliquez sur la ligne **STRUCTURE DESCRIPTOR**, marquée **JSON**, pour l'ouvrir.

#### **Gestion des brouillons**

La colonne de gauche affiche la liste des **Version** du fichier. La version marquée **Actif** est celle que DocBits utilise.

* **Créer un brouillon** : cliquez sur l'icône crayon ✏️ à côté de la version active pour commencer la modification. Le fichier actif lui-même ne peut pas être modifié directement.
* **Activer les modifications** : cliquez sur l'icône de validation ✅ d'un brouillon pour approuver et publier vos modifications.
* **Supprimer des brouillons** : utilisez l'icône corbeille 🗑️ pour supprimer les brouillons inutilisés. Cette icône n'apparaît que si le fichier compte plusieurs versions.
  * <mark style="color:red;">**Note**</mark> : l'activation d'une nouvelle version **désactive automatiquement** la précédente.

<figure><img src="../../../../../../../.gitbook/assets/edi-structure-descriptor-file-guide-detail-fr-20261114.png" alt="Éditeur du fichier STRUCTURE DESCRIPTOR (JSON) de la sandbox en français, avec à gauche la liste des versions où la version 1 porte la mention Actif et l'icône crayon, et à droite le contenu JSON découpé en groupes"><figcaption><p>Le fichier de description de la structure et sa liste des versions ; l'icône crayon crée un brouillon que vous pouvez modifier.</p></figcaption></figure>

## 3. Fonction d'aperçu (aperçu de la sortie analysée)

La **fonction d'aperçu** vous permet de tester comment un fichier EDI importé est analysé avec la description de structure affichée, avant d'activer une modification.

#### Utilisation

* Importez un fichier EDI via le flux d'import standard.
* Copiez le **Document ID** du fichier importé.
* Ouvrez le fichier **STRUCTURE DESCRIPTOR** comme décrit ci-dessus.
* Cliquez sur **Aperçu** en haut à droite pour ouvrir le panneau de test.

    <div align="left"><figure><img src="../../../../../../../.gitbook/assets/edi-structure-descriptor-file-guide-preview-fr-20261114.png" alt="Panneau de test Aperçu de la sandbox en français, ouvert à droite du fichier STRUCTURE DESCRIPTOR (JSON) : champ Document Id..., bouton Test et sortie XML structurée affichée à côté de l'éditeur" width="560"><figcaption><p>Le panneau de test : saisissez un Document ID et cliquez sur Test ; l'identifiant affiché ici est une donnée d'exemple inventée.</p></figcaption></figure></div>

* Saisissez le **Document ID** dans le champ et cliquez sur **Test**. Le libellé du champ reste en anglais dans l'interface française : **Document Id...**.
* La **sortie structurée** obtenue s'affiche à côté de l'éditeur.

Cette fonction est particulièrement utile pour déboguer les mappages et valider les regroupements structurels en temps réel. Un document EDI représentatif de votre propre format est nécessaire ; le résultat affiché dépend du fichier importé. La manière dont les données analysées sont ensuite présentées dans les autres aperçus de DocBits est décrite dans le [guide du fichier d'aperçu EDI](../edi-preview-file-guide.md).

## 4. Démonstration vidéo

Une démonstration vidéo pour ce type de fichier est disponible sur la [page Vidéos EDI](../edi-videos.md).\
Utilisez-la pour suivre pas à pas la configuration, la modification et l'utilisation de l'aperçu.

Les séquences montrent une configuration et une version existantes. Les paramètres varient selon le type de document et le format. Validez les modifications dans un brouillon avant de les activer.
