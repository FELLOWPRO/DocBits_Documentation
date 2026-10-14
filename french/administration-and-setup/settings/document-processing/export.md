# Exportation

## Aperçu

La page Exportation affiche toutes les configurations d'exportation configurées, y compris si elles sont actives ou inactives. À partir de là, les utilisateurs peuvent :

* Consulter et gérer les configurations d'exportation existantes
* Créer de nouvelles connexions d'exportation (par exemple, vers **Infor**, **Infor & IDM**, **Webhook** ou **SFTP**)
* Modifier ou supprimer les configurations d'exportation existantes

## Où le trouver

Vous pouvez le trouver sous : **Paramètres** → **Traitement des documents** → **Exportation**

![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/export_settings_menu_access.png)

## **Utilisation de la page Exportation**

Lorsque vous ouvrez la page Exportation, vous verrez une liste de toutes les configurations d'exportation existantes.

Chaque ligne de la liste affiche :

* **Indicateur de statut**
  * **Vert** signifie que l'exportation est active
  * **Rouge** signifie que l'exportation est désactivée
* **Nom** – le nom de la configuration d'exportation
* **Type de document** – le type de document pour lequel l'exportation est configurée
* **Sous-organisation** – si l'exportation est limitée à une sous-organisation spécifique
* **Méthode d'exportation** – où le document sera envoyé (par exemple, Infor, IDM, SFTP)
* **Actions** – boutons pour **modifier, supprimer** ou **activer/désactiver** la configuration

![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/export_list_view.png)

#### **Règles importantes pour la configuration d'exportation**

Pour chaque **type de document** **au sein d'une organisation ou sous-organisation donnée**, les règles suivantes s'appliquent :

* Vous ne pouvez avoir qu'**une seule exportation Infor active**
* Vous ne pouvez avoir qu'**une seule exportation non-Infor active** (par exemple, Webhook, SFTP)

Cependant, il est possible d'avoir :

* **Une exportation Infor active** _et_ **une exportation non-Infor active** en même temps pour le même type de document
* **Différentes configurations d'exportation pour différentes sous-organisations** — par exemple, une exportation Infor pour Sous-Org A et une autre exportation Infor pour Sous-Org B

## **Créer une nouvelle exportation**

Pour créer une nouvelle exportation :

1. Cliquez sur le bouton **« Nouveau »**. ![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/export_create_new_button.png)
2. Sélectionnez le **Type d'exportation** que vous souhaitez configurer (par exemple, Infor, IDM, SFTP).
3. Remplissez les champs requis en fonction du type d'exportation.
4. Enregistrez la configuration.

## Options d'exportation

#### Webhook

<details>

<summary>Webhook</summary>

![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/export_webhook_configuration.png)

**Descriptions des champs**

* **Title** Le nom de la configuration d'exportation. Il apparaîtra dans la liste des exportations.
* **Sub-Organization** _(optionnel)_ Un menu déroulant avec toutes les sous-organisations disponibles.
  * Si laissé vide : s'applique à l'organisation principale.
  * Si sélectionné : l'exportation ne s'appliquera qu'à la sous-organisation choisie.
* **Document Type** Menu déroulant listant tous les types de documents disponibles. Cela détermine à quel type de document cette configuration d'exportation s'applique.
* **Export URL** L'URL de destination où le document doit être exporté.

</details>

#### SFTP

<details>

<summary>SFTP</summary>

![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/export_sftp_configuration.png)

**Descriptions des champs**

* **Title** Le nom de la configuration d'exportation. Il apparaîtra dans la liste des exportations.
* **Sub-Organization** _(optionnel)_ Un menu déroulant avec toutes les sous-organisations disponibles.
  * Si laissé vide : s'applique à l'organisation principale.
  * Si sélectionné : l'exportation ne s'appliquera qu'à la sous-organisation choisie.
* **Document Type** Menu déroulant listant tous les types de documents disponibles. Cela détermine à quel type de document cette configuration d'exportation s'applique.
* **Username** Le nom d'utilisateur utilisé pour s'authentifier auprès du serveur SFTP.
* **Password** Le mot de passe correspondant pour le compte SFTP. Assurez-vous que le compte dispose d'un accès en écriture au dossier spécifié.
* **Server URL** Le nom d'hôte ou l'adresse IP du serveur SFTP cible.
* **Port** Le port utilisé pour se connecter au serveur SFTP.
* **Folder** Le chemin sur le serveur SFTP où les documents doivent être téléchargés (par exemple, `/incoming/invoices/`). Doit exister et être accessible en écriture.
*   **XSLT File (Optionnel)**

    Le **fichier XSLT** permet la transformation du format d'exportation par défaut de DocBits.

    * **Quand l'utiliser :** Uniquement si le système récepteur nécessite une structure différente ou un formatage spécifique différent du format par défaut de DocBits.
    * **Laissez-le vide** si le format d'exportation par défaut répond aux exigences.



**Paramètres avancés :**

* **Filename Export Mode** Spécifie si le fichier exporté conserve son nom de fichier original ou est renommé en utilisant l'ID de document DocBits.
* **Include Document History** Lorsqu'il est activé, le fichier exporté inclura l'historique du document basé sur les journaux disponibles dans le tableau de bord.

![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/export_sftp_2.png)

![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/export_sftp_3.png)

</details>

#### Exportation Infor vers SFTP

<details>

<summary>Exportation Infor vers SFTP</summary>

![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/export_infor_sftp_configuration.png)

**Descriptions des champs**

* **Title** Le nom de la configuration d'exportation. Il apparaîtra dans la liste des exportations.
* **Sub-Organization** _(optionnel)_ Un menu déroulant avec toutes les sous-organisations disponibles.
  * Si laissé vide : s'applique à l'organisation principale.
  * Si sélectionné : l'exportation ne s'appliquera qu'à la sous-organisation choisie.
* **Document Type** Menu déroulant listant tous les types de documents disponibles. Cela détermine à quel type de document cette configuration d'exportation s'applique.
* **IDM Mapping File** Sélectionnez un fichier de mappage dans le gestionnaire de fichiers. [Besoin d'aide pour en créer un ? Consultez le Guide de Mappage IDM](../../../infor-integration-and-configuration/exporting-to-infor/creating-an-idm-mapping-file.md)
* **BOD Mapping File** Sélectionnez un fichier de mappage dans le gestionnaire de fichiers. [Besoin d'aide pour en créer un ? Consultez le Guide de Mappage BOD](../../../infor-integration-and-configuration/exporting-to-infor/creating-a-bod-mapping-file.md)
* **Folder** Le chemin sur le serveur SFTP où les documents doivent être téléchargés (par exemple, `/incoming/invoices/`). Doit exister et être accessible en écriture.

</details>

#### **SMB**

<details>

<summary>SMB</summary>

![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/export_smb_configuration.png)

**Descriptions des champs**

* **Title** Le nom de la configuration d'exportation. Il apparaîtra dans la liste des exportations.
* **Sub-Organization** _(optionnel)_ Un menu déroulant avec toutes les sous-organisations disponibles.
  * Si laissé vide : s'applique à l'organisation principale.
  * Si sélectionné : l'exportation ne s'appliquera qu'à la sous-organisation choisie.
* **Document Type** Menu déroulant listant tous les types de documents disponibles. Cela détermine à quel type de document cette configuration d'exportation s'applique.
* **Username** Le nom d'utilisateur utilisé pour se connecter au partage SMB.
* **Password** Le mot de passe correspondant pour l'authentification SMB.
* **Server URL** L'adresse du serveur SMB.
* **Port** Numéro de port utilisé pour accéder au partage SMB.
* **Folder** Le chemin du dossier dans le partage SMB où les documents doivent être enregistrés (par exemple, `/incoming/invoices/`). Doit exister et être accessible en écriture.
*   **JPL Mapping File (Optionnel)**

    Le **fichier JPL** est utilisé pour définir une transformation des données exportées avant qu'elles ne soient écrites dans le partage SMB.

    * **Quand l'utiliser :** Uniquement lorsque les données du document exporté doivent être ajustées pour correspondre au formatage externe ou aux attentes du système.
    * **Laissez-le vide** si aucune transformation n'est nécessaire.

</details>

#### **Infor IDM**

<details>

<summary>Infor IDM</summary>

![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/export_infor_idm_configuration.png)

**Descriptions des champs**

* **Title** Le nom de la configuration d'exportation. Il apparaîtra dans la liste des exportations.
* **Sub-Organization** _(optionnel)_ Un menu déroulant avec toutes les sous-organisations disponibles.
  * Si laissé vide : s'applique à l'organisation principale.
  * Si sélectionné : l'exportation ne s'appliquera qu'à la sous-organisation choisie.
* **Document Type** Menu déroulant listant tous les types de documents disponibles. Cela détermine à quel type de document cette configuration d'exportation s'applique.
* **ION Mapping File** Sélectionnez un fichier de mappage dans le gestionnaire de fichiers.
* **IDM Mapping File** Sélectionnez un fichier de mappage dans le gestionnaire de fichiers. [Besoin d'aide pour en créer un ? Consultez le Guide de Mappage IDM](../../../infor-integration-and-configuration/exporting-to-infor/creating-an-idm-mapping-file.md)
* **Cloud / On-Prem Toggle** Un commutateur pour indiquer le type de déploiement Infor :
  * **Cloud** : Sélectionnez ceci si vous êtes client Infor CloudSuite.
  * **On-Prem** : Sélectionnez ceci si Infor est auto-hébergé.

</details>

#### **Infor ION**

<details>

<summary>Infor ION</summary>

![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/export_infor_ion_configuration.png)

**Descriptions des champs**

* **Title** Le nom de la configuration d'exportation. Il apparaîtra dans la liste des exportations.
* **Sub-Organization** _(optionnel)_ Un menu déroulant avec toutes les sous-organisations disponibles.
  * Si laissé vide : s'applique à l'organisation principale.
  * Si sélectionné : l'exportation ne s'appliquera qu'à la sous-organisation choisie.
* **Document Type** Menu déroulant listant tous les types de documents disponibles. Cela détermine à quel type de document cette configuration d'exportation s'applique.
* **ION Mapping File** Sélectionnez un fichier de mappage dans le gestionnaire de fichiers.
* **BOD Mapping File** Sélectionnez un fichier de mappage dans le gestionnaire de fichiers. [Besoin d'aide pour en créer un ? Consultez le Guide de Mappage BOD](../../../infor-integration-and-configuration/exporting-to-infor/creating-a-bod-mapping-file.md)
* **Cloud / On-Prem Toggle** Un commutateur pour indiquer le type de déploiement Infor :
  * **Cloud** : Sélectionnez ceci si vous êtes client Infor CloudSuite.
  * **On-Prem** : Sélectionnez ceci si Infor est auto-hébergé.

</details>

#### Infor IDM + ION BOD

<details>

<summary>Infor IDM + ION BOD</summary>

![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/export_infor_idm_ion_bod_configuration.png)

**Descriptions des champs**

* **Title** Le nom de la configuration d'exportation. Il apparaîtra dans la liste des exportations.
* **Sub-Organization** _(optionnel)_ Un menu déroulant avec toutes les sous-organisations disponibles.
  * Si laissé vide : s'applique à l'organisation principale.
  * Si sélectionné : l'exportation ne s'appliquera qu'à la sous-organisation choisie.
* **Document Type** Menu déroulant listant tous les types de documents disponibles. Cela détermine à quel type de document cette configuration d'exportation s'applique.
* **ION Mapping File** Sélectionnez un fichier de mappage dans le gestionnaire de fichiers.
* **IDM Mapping File** Sélectionnez un fichier de mappage dans le gestionnaire de fichiers. [Besoin d'aide pour en créer un ? Consultez le Guide de Mappage IDM](../../../infor-integration-and-configuration/exporting-to-infor/creating-an-idm-mapping-file.md)
* **BOD Mapping File** Sélectionnez un fichier de mappage dans le gestionnaire de fichiers. [Besoin d'aide pour en créer un ? Consultez le Guide de Mappage BOD](../../../infor-integration-and-configuration/exporting-to-infor/creating-a-bod-mapping-file.md)
* **Cloud / On-Prem Toggle** Un commutateur pour indiquer le type de déploiement Infor :
  * **Cloud** : Sélectionnez ceci si vous êtes client Infor CloudSuite.
  * **On-Prem** : Sélectionnez ceci si Infor est auto-hébergé.

</details>

### Pour les clients Infor CloudSuite

#### Infor IDM + LN

<details>

<summary>Infor IDM + LN</summary>

![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/export_infor_idm_ln_configuration.png)

**Descriptions des champs**

* **Title** Le nom de la configuration d'exportation. Il apparaîtra dans la liste des exportations.
* **Sub-Organization** _(optionnel)_ Un menu déroulant avec toutes les sous-organisations disponibles.
  * Si laissé vide : s'applique à l'organisation principale.
  * Si sélectionné : l'exportation ne s'appliquera qu'à la sous-organisation choisie.
* **Document Type** Menu déroulant listant tous les types de documents disponibles. Cela détermine à quel type de document cette configuration d'exportation s'applique.
* **ION Mapping File** Sélectionnez un fichier de mappage dans le gestionnaire de fichiers.
* **IDM Mapping File** Sélectionnez un fichier de mappage dans le gestionnaire de fichiers. [Besoin d'aide pour en créer un ? Consultez le Guide de Mappage IDM](../../../infor-integration-and-configuration/exporting-to-infor/creating-an-idm-mapping-file.md)
* **LN Mapping File** Sélectionnez un fichier de mappage dans le gestionnaire de fichiers. [Besoin d'aide pour en créer un ? Consultez l'Exemple de Mappage LN](../../../infor-integration-and-configuration/exporting-to-infor/ln/example-export-ln/)

</details>

#### Infor IDM + M3

<details>

<summary>Infor IDM + M3</summary>

![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/export_infor_idm_m3_configuration.png)

**Descriptions des champs**

* **Title** Le nom de la configuration d'exportation. Il apparaîtra dans la liste des exportations.
* **Sub-Organization** _(optionnel)_ Un menu déroulant avec toutes les sous-organisations disponibles.
  * Si laissé vide : s'applique à l'organisation principale.
  * Si sélectionné : l'exportation ne s'appliquera qu'à la sous-organisation choisie.
* **Document Type** Menu déroulant listant tous les types de documents disponibles. Cela détermine à quel type de document cette configuration d'exportation s'applique.
* **ION Mapping File** Sélectionnez un fichier de mappage dans le gestionnaire de fichiers.
* **IDM Mapping File** Sélectionnez un fichier de mappage dans le gestionnaire de fichiers. [Besoin d'aide pour en créer un ? Consultez le Guide de Mappage IDM](../../../infor-integration-and-configuration/exporting-to-infor/creating-an-idm-mapping-file.md)
* **M3 Mapping File** Sélectionnez un fichier de mappage dans le gestionnaire de fichiers. [Besoin d'aide pour en créer un ? Consultez l'Exemple de Mappage M3](../../../infor-integration-and-configuration/exporting-to-infor/m3/example-export-m3.md)

</details>

#### Infor IDM + M3 (toml)

<details>

<summary>Infor IDM + M3 (toml)</summary>

![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/export_infor_idm_m3_toml_configuration.png)

**Descriptions des champs**

* **Title** Le nom de la configuration d'exportation. Il apparaîtra dans la liste des exportations.
* **Sub-Organization** _(optionnel)_ Un menu déroulant avec toutes les sous-organisations disponibles.
  * Si laissé vide : s'applique à l'organisation principale.
  * Si sélectionné : l'exportation ne s'appliquera qu'à la sous-organisation choisie.
* **Document Type** Menu déroulant listant tous les types de documents disponibles. Cela détermine à quel type de document cette configuration d'exportation s'applique.
* **ION Mapping File** Sélectionnez un fichier de mappage dans le gestionnaire de fichiers.
* **IDM Mapping File** Sélectionnez un fichier de mappage dans le gestionnaire de fichiers. [Besoin d'aide pour en créer un ? Consultez le Guide de Mappage IDM](../../../infor-integration-and-configuration/exporting-to-infor/creating-an-idm-mapping-file.md)
* **M3 toml Mapping File** Sélectionnez un fichier de mappage dans le gestionnaire de fichiers ou utilisez l'option sélectionner Toml pour utiliser un toml créé avec le gestionnaire de règles. [Besoin d'aide pour en créer un ? Consultez le Guide du Gestionnaire de Règles](rule-manager/)

</details>
