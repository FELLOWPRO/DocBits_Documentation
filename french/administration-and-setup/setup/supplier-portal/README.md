# Tableau de bord du fournisseur

## Aperçu

Cette page explique comment activer et utiliser le **Tableau de bord du fournisseur**, ainsi que où trouver tous les paramètres pertinents. Le Tableau de bord du fournisseur vous permet d'inviter des fournisseurs à **DocBits**. Une fois l'accès accordé, les fournisseurs peuvent se connecter pour voir le statut de leurs **Commandes d'achat** et **Factures** directement dans **DocBits**.

## Comment activer le Tableau de bord du fournisseur

1.  Allez dans **Paramètres → Traitement des documents → Module**.

    ![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/settings_module.png)
2.  Dans la section **Expédition et fournisseur**, activez l'option **Tableau de bord du fournisseur**.

    ![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/supplier_portal_1.png)

## Paramètres du fournisseur

Une fois la fonctionnalité **Tableau de bord du fournisseur** activée, une nouvelle section **Paramètres du fournisseur** apparaîtra en bas du menu **Paramètres**.

![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/settings_suppplier_settings.png)

[**Paramètres généraux du fournisseur**](../../settings/supplier-setting/supplier-general-settings.md): Ici, vous pouvez personnaliser le **Tableau de bord du fournisseur** en téléchargeant le logo de votre entreprise—affiché dans l'en-tête de tous les modèles d'e-mails—et en gérant des documents légaux tels que les Conditions d'utilisation et la Politique de confidentialité.

[**Modèles d'e-mails**](../../settings/supplier-setting/editing-email-templates.md)**:** Ici, vous pouvez créer et tester les modèles d'e-mails d'invitation qui seront envoyés aux fournisseurs invités.

**Disposition du fournisseur:** Ici, vous pouvez créer et gérer les dispositions qui définissent quelles informations les nouveaux fournisseurs doivent fournir lors du processus d'enregistrement.

[**Configuration d'exportation**](../../settings/supplier-setting/export-configuration-for-supplier-portal.md): Ici, vous pouvez définir comment les données sont mappées et synchronisées entre le **Tableau de bord du fournisseur** et le système **Infor M3** à l'aide de fichiers de mappage ION et IDM.

**Autorisations du fournisseur**: Ici, vous pouvez configurer les autorisations que les fournisseurs auront dans le **Tableau de bord du fournisseur**. Vous pouvez également regrouper les fournisseurs, ce qui facilite la gestion des accès et des paramètres entre plusieurs fournisseurs.

Un guide détaillé sur tous les paramètres du fournisseur peut être trouvé [ici](../../settings/supplier-setting/).

## Tableau de bord des fournisseurs <a href="#supplier-permissions" id="supplier-permissions"></a>

Vous pouvez accéder au **Tableau de bord des fournisseurs** depuis le menu de gauche, comme indiqué ci-dessous.

![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/supplier_portal_2.png)

Tous vos fournisseurs créés sont affichés ici.

## Filtrer les fournisseurs

Vous pouvez rechercher des fournisseurs par N**om** ou N**uméro**, ou utiliser les filtres avancés pour affiner les résultats par :

* **Groupes de fournisseurs**
* **Statut**
* **Créé le**

Vous pouvez également spécifier combien de fournisseurs doivent être affichés par page.

![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/supplier_portal_9.png)

De plus, vous pouvez rapidement filtrer par les statuts **En attente de validation** ou **Enregistrement en cours** en cliquant sur la catégorie correspondante à gauche de la barre de filtre.

![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/10.png)

## Statut du fournisseur

Si vous utilisez le **Tableau de bord du fournisseur**, il est important de comprendre les différents statuts que les fournisseurs peuvent avoir. Voici une liste de tous les statuts possibles des fournisseurs et leur signification :

* **Open**: Fournisseur existant qui n'a pas encore été invité au tableau de bord.
* **Enregistrement en cours**: Le fournisseur a été invité mais n'a pas encore complété le processus d'enregistrement.
* **En attente de l'avis du fournisseur**: L'enregistrement est complet, mais des informations ou des modifications supplémentaires sont requises de la part du fournisseur.
* **En attente de validation**: Le fournisseur a complété l'enregistrement et attend la première validation.
* **En attente d'approbation AP**: Le fournisseur a reçu la première approbation et attend une seconde approbation (Comptabilité).
* **Approuvé**: Le fournisseur a complété le processus et a été entièrement approuvé.
* **Rejeté**: L'enregistrement ou l'approbation du fournisseur a été rejeté.

## Outils dans le Tableau de bord des fournisseurs

À droite de la barre de recherche, vous trouverez plusieurs outils qui vous aident à interagir avec et à gérer le tableau de bord plus efficacement.

### Rafraîchir la table <a href="#refresh-table" id="refresh-table"></a>

![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/supplier_portal_3.png)

Cliquez sur ce bouton pour rafraîchir le tableau de bord et charger les données et statuts les plus récents.

### Définir les colonnes du tableau pour l'organisation <a href="#set-table-columns-for-organization" id="set-table-columns-for-organization"></a>

![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/supplier_portal_4.png)

Cliquez sur ce bouton pour ouvrir un menu où vous pouvez gérer la visibilité des colonnes dans le tableau des commandes d'achat. Utilisez les cases à cocher et les boutons fléchés pour déplacer les colonnes entre les sections visibles et cachées. Vous pouvez également réorganiser les colonnes en faisant glisser et déposer les noms des colonnes. Cliquez sur **Terminé** pour sauvegarder vos modifications.

![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/supplier_portal_7.png)

### Analytique <a href="#analytics" id="analytics"></a>

![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/supplier_portal_5.png)

En cliquant sur ce bouton, une nouvelle section s'ouvrira montrant combien de fournisseurs sont sur le point d'expirer et quand.\
Cliquez sur n'importe quelle catégorie pour appliquer un filtre et voir uniquement ces fournisseurs.

![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/supplier_portal_8.png)

## Créer un fournisseur et envoyer un e-mail d'enregistrement

### **Pour créer un nouveau fournisseur :**

1.  Cliquez sur l'icône plus (+) dans le coin supérieur droit.

    ![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/supplier_portal_6.png)
2.  Remplissez les champs requis, puis cliquez sur **Sauvegarder**.

    ![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/supplier_portal_11.png)
3. Le fournisseur recevra automatiquement un e-mail avec un lien pour créer son compte.

### **Pour envoyer un e-mail d'enregistrement à un fournisseur existant :**

1. Localisez le fournisseur dans le **Tableau de bord des fournisseurs**.
2. Cliquez sur le menu à trois points dans la colonne **Actions**.
3.  Sélectionnez **Magic Link**.

    ![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/supplier_portal_12.png)
4. Vérifiez les détails du fournisseur.
5.  Cliquez sur **Envoyer** pour envoyer le lien d'enregistrement par e-mail.

    ![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/supplier_portal_13.png)

## Comment fonctionne le processus d'enregistrement pour le fournisseur ?

Après l'envoi d'un e-mail d'invitation, le fournisseur doit compléter le processus d'enregistrement pour accéder au **Tableau de bord du fournisseur**.

Un guide détaillé étape par étape sur le processus d'enregistrement peut être trouvé [ici](supplier-registration.md).
