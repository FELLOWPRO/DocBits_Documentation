# Réglages des données de base

## Aperçu

Dans la section **Réglages des données de base** des paramètres **Champs** pour un **Type de document** spécifique, vous pouvez afficher et configurer les mappages de données de base vers les champs utilisés lors de la validation des champs, en utilisant les données issues de [**Validation des données fournisseur**](../../../document-processing/master-data-lookup.md).

Ces mappages définissent comment les données de base sont appliquées aux champs individuels pendant la validation. Cette page fournit un guide détaillé sur la façon de configurer et de gérer ces mappages.

## **Accéder** aux Réglages des données de base **Paramètres**

Pour accéder aux **Paramètres** des **Réglages des données de base** :

1.  Allez à **Paramètres → Paramètres globaux → Types de documents**

    ![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/settings_document_types.png)
2.  Sélectionnez le **Type de document** souhaité et cliquez sur **Champs**.

    ![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/settings_document_types_fields.png)
3.  Cliquez sur **Réglages des données de base**

    ![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/fields_master_data_settings_1.png)

## Consultation des données de base

Dans la section **Consultation des données de base**, vous pouvez créer des configurations de consultation à partir de vos données de base pour les utiliser comme mappages de champs lors de la validation des champs.

### Entrées par défaut

Dans la section **Consultation des données de base**, certaines entrées par défaut sont fournies par **DocBits**. Ces entrées :

* Ne peuvent pas être modifiées ou supprimées
* Peuvent être désactivées si elles ne sont pas nécessaires

Les entrées par défaut sont clairement marquées avec un **Default** tag pour une identification facile.

![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/fields_master_data_settings_2.png)

### **Créer une configuration de consultation**

Pour créer une nouvelle configuration de consultation pour les données de base :

1. Accédez à la section **Consultation des données de base**.
2.  Cliquez sur **Créer une configuration de consultation** dans le coin supérieur droit.

    ![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/fields_master_data_settings_3.png)
3. Configurez les options suivantes :
   * **Recherche de nom**\
     Le nom de la configuration de consultation.
   * **Recherche du nom du jeu de données**\
     Sélectionnez le jeu de données qui doit être utilisé pour cette configuration de consultation.
   * **Gestionnaire de conflit**\
     Un conflit signifie que la recherche a trouvé plus d'un enregistrement. Ce réglage décide de ce qui se passe alors :
     * **Best Score** – Utilise l'entrée qui correspond au plus grand nombre de champs. Ne laisse jamais le champ vide et peut donc choisir le mauvais enregistrement.
     * **Return None** – Laisse le champ vide, pour qu'un utilisateur choisisse le bon enregistrement.
     * **Return First** – Utilise la première valeur correspondante.
   *   **Type de contexte**

       Spécifie où dans le document la configuration de consultation sera appliquée. Choisissez entre :

       **HEADER**

       La consultation est utilisée lors de la validation des champs. Configurez ce qui suit :

       * **Tout faire correspondre**\
         Lorsqu'elle est activée, un enregistrement doit correspondre à **tous** les champs utilisés. Lorsqu'elle est désactivée (par défaut), la correspondance d'**un seul** champ suffit, ce qui donne une liste plus longue.

       ![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/fields_master_data_settings_4.png)

       \
       **LINE**

       La consultation est utilisée dans un tableau du document. Configurez ce qui suit :

       * **Détail du contexte**\
         Sélectionnez le tableau spécifique auquel la consultation doit être appliquée.
       * **Tout faire correspondre**\
         Lorsqu'elle est activée, un enregistrement doit correspondre à **tous** les champs utilisés. Lorsqu'elle est désactivée (par défaut), la correspondance d'**un seul** champ suffit, ce qui donne une liste plus longue.

       ![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/fields_master_data_settings_5.png)
{% hint style="info" %}
**Tout faire correspondre** et le **Gestionnaire de conflit** agissent ensemble et déterminent si un fournisseur est reconnu automatiquement. La page de configuration les explique avec des exemples :

{% content-ref url="../../../../setup/document-types/fuzzy-data-configuration-with-master-data.md" %}
[fuzzy-data-configuration-with-master-data](../../../../setup/document-types/fuzzy-data-configuration-with-master-data.md)
{% endcontent-ref %}
{% endhint %}

4.  Cliquez sur **Sauvegarder** pour créer la configuration de consultation.

    ![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/fields_master_data_settings_6.png)

### Actions sur une configuration de consultation existante

Pour gérer une configuration de consultation existante, cliquez sur les trois points dans le coin supérieur droit de la configuration que vous souhaitez modifier.

![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/fields_master_data_settings_7.png)

Les actions suivantes sont disponibles :

* **Activer / Désactiver**\
  Bascule l’état de la configuration de consultation.
  * Les configurations actives sont marquées avec un tag **Actif**.
  * Les configurations inactives sont marquées avec un tag **Inactif**.
*   **Duplicata**\
    Après avoir saisi un nom et cliqué sur **Terminé**, une copie de la configuration de consultation sélectionnée est créée.

    ![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/fields_master_data_settings_8.png)
* **Éditer/Vue**\
  Permet de modifier la configuration de consultation sélectionnée.\
  Après avoir apporté vos modifications, cliquez sur **Sauvegarder** pour les appliquer.\
  <mark style="color:red;">**Remarque**</mark> : Les configurations de consultation par défaut ne peuvent être qu’affichées, pas éditées. L’option **Éditer** sera remplacée par **Vue**.
*   **Supprimer**\
    Supprime définitivement la configuration de consultation sélectionnée après confirmation.\
    <mark style="color:red;">**Remarque**</mark> : Seules les configurations sans le tag **Default** peuvent être supprimées.

    ![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/fields_master_data_settings_9.png)

### Créer un nouveau champ

Pour ajouter un nouveau champ à votre configuration de consultation :

1. Ouvrez la configuration de consultation souhaitée.
2.  Cliquez sur **Créer** dans le coin supérieur droit.

    ![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/fields_master_data_settings_10.png)
3. Configurez les options nécessaires.
   * **Champ de recherche**\
     Le champ qui sera recherché dans le jeu de données sélectionné.
   * **Champ de validation**\
     Le champ qui sera affiché lors de la validation des champs.
   * **Champ parental** (facultatif)\
     Ce champ est utilisé pour valider l’exactitude de la valeur dans le **Champ de validation** en s’assurant qu’elle correspond à l’entrée parente correspondante dans le jeu de données de consultation.
   * **Opérateur de recherche** (facultatif)\
     Choisissez comment **DocBits** recherche les correspondances dans le jeu de données :
     * **Smart** – _(par défaut)_ Ignore les espaces et la ponctuation et recherche le terme **n'importe où** dans le champ. « Meier » trouve donc aussi « Meier Bau GmbH ».
     * **Contient** – Recherche les entrées qui contiennent le terme exact n’importe où dans le champ.
     * **se termine par** – Recherche les entrées qui se terminent par le terme spécifié.
     * **exact** – Recherche une correspondance exacte de la valeur entière.
     * **commence par** – Recherche les entrées qui commencent par le terme spécifié.
   * **Déclenchement automatique** (facultatif)\
     Lorsqu’il est activé, DocBits remplira automatiquement tous les champs de la configuration de consultation dès que ce champ est renseigné.
   *   **Consultable** (facultatif)\
       Lorsqu’il est activé, les utilisateurs peuvent rechercher manuellement des données de base lors de la validation des champs **et** le champ participe à la recherche automatique. Laissez-le décoché si le champ ne doit pas influencer le résultat automatique.

       ![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/fields_master_data_settings_12.png)

       ![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/fields_master_data_settings_13.png)
4.  Cliquez sur **Sauvegarder** pour créer le nouveau champ.

    ![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/fields_master_data_settings_11.png)

### Actions sur un champ existant

Pour gérer un champ existant, cliquez sur les trois points dans la colonne **Actions** à côté du champ que vous souhaitez modifier.

![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/fields_master_data_settings_14.png)

Les actions suivantes sont disponibles :

* **Éditer/Vue**\
  Permet de modifier le champ sélectionné.\
  Après avoir apporté vos modifications, cliquez sur **Sauvegarder** pour les appliquer.\
  <mark style="color:red;">**Remarque**</mark> : Les champs par défaut peuvent uniquement être affichés, pas édités. Dans ces cas, l’option **Éditer** apparaîtra comme **Vue**.
*   **Supprimer**\
    Supprime définitivement le champ sélectionné après confirmation.\
    <mark style="color:red;">**Remarque**</mark> : Seuls les champs sans le tag **Default** peuvent être supprimés.

    ![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/fields_master_data_settings_9.png)

## Données de base LOV

La section **Données de base LOV** vous permet de créer des configurations de menus déroulants en utilisant des valeurs provenant de vos données de base. Ces menus déroulants peuvent être indépendants ou dépendants d’autres menus déroulants, permettant un filtrage dynamique et des sélections en cascade lors de la validation des champs.

### Créer une configuration de recherche Lov

Une configuration de recherche lov définit comment les options du menu déroulant sont obtenues à partir d’une table de données de base et comment ces valeurs sont affichées et renseignées dans les champs du document.

**Pour créer une nouvelle configuration de recherche Lov :**

1. Accédez à la section **Données de base LOV**.
2.  Cliquez sur **Créer une configuration de recherche Lov** dans le coin supérieur droit.

    ![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/fields_master_data_settings_15.png)
3. Configurez les options suivantes :
   * **Consulter le nom de Lov**\
     Le nom de la configuration de recherche lov.
   * **Recherche du nom du jeu de données Lov**\
     Sélectionnez la table de données de base qui doit être utilisée pour cette configuration de recherche lov.
   *   **Type de contexte**\
       Spécifie où dans le document la configuration de recherche lov sera appliquée :

       **HEADER**

       La configuration de recherche lov est utilisée lors de la validation des champs. Configurez ce qui suit :

       * **Champ d'étiquette de consultation**\
         Sélectionnez la colonne dont la valeur sera affichée dans le menu déroulant.
       * **Champ de valeur de recherche**\
         Sélectionnez la colonne dont la valeur sera stockée en interne et utilisée pour le filtrage lorsqu’une sélection est faite. Cette valeur n’est pas affichée à l’utilisateur.
       * **Hors champ**\
         Définit le champ dans la validation des champs qui recevra l’étiquette sélectionnée du menu déroulant.

       ![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/fields_master_data_settings_16.png)

       \
       **LINE**

       La configuration de recherche lov est utilisée dans un tableau du document. Configurez ce qui suit :

       * **Détail du contexte**\
         Sélectionnez le tableau spécifique où cette configuration de recherche lov doit être active.
       * **Champ d'étiquette de consultation**\
         La colonne dont la valeur sera affichée dans le menu déroulant.
       * **Champ de valeur de recherche**\
         Sélectionnez la colonne dont la valeur sera stockée en interne et utilisée pour le filtrage lorsqu’une sélection est faite. Cette valeur n’est pas affichée à l’utilisateur.
       * **Hors champ**\
         Spécifie le champ cible dans le tableau où l’étiquette sélectionnée sera renseignée.

       ![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/fields_master_data_settings_17.png)
4.  Cliquez sur **Sauvegarder** pour créer la configuration de recherche lov.

    ![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/fields_master_data_settings_18.png)

### Actions sur une configuration de recherche lov existante

Pour gérer une configuration de recherche lov existante, cliquez sur les trois points dans le coin supérieur droit de la configuration.

![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/fields_master_data_settings_19.png)

**Actions disponibles :**

* **Activer / Désactiver**\
  Bascule l’état de la configuration de recherche lov.
  * Les configurations **Actif** sont marquées avec un tag **Actif**.
  * Les configurations **Inactif** sont marquées avec un tag **Inactif**.
*   **Duplicata**\
    Après avoir saisi un nom et cliqué sur **Terminé**, une copie de la configuration de recherche lov sélectionnée est créée.

    ![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/fields_master_data_settings_21.png)
* **Éditer / Vue**\
  Modifiez la configuration sélectionnée. Après avoir apporté des modifications, cliquez sur **Sauvegarder**.
*   **Supprimer**\
    Supprime définitivement la configuration après confirmation.

    ![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/fields_master_data_settings_20.png)

### Créer un nouveau champ

Dans chaque configuration de recherche lov, vous pouvez définir des champs supplémentaires comme menus déroulants qui agissent comme pré-filtres pour la logique lov principale.

Ces champs sont évalués avant le chargement du menu déroulant lov principal. En fonction des valeurs sélectionnées dans ces champs, les résultats du champ lov principal sont filtrés dynamiquement — permettant des menus déroulants dépendants.\
Par exemple, la sélection d’un pays dans un champ de pré-filtre peut réduire les options de ville dans le menu déroulant lov principal.

En plus de créer de nouveaux champs, vous pouvez également utiliser des champs existants comme pré-filtres. Lorsqu’ils sont configurés de cette manière, la valeur sélectionnée dans le champ existant filtrera automatiquement le menu déroulant lov principal.

**Pour ajouter un nouveau champ :**

1. Ouvrez la configuration de recherche lov souhaitée.
2.  Cliquez sur **Créer** dans le coin supérieur droit.

    ![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/fields_master_data_settings_22.png)
3.  Configurez les options nécessaires.

    **Options de configuration du champ (s’applique aux contextes HEADER et LINE) :**

    * **Champ de recherche**\
      La colonne à rechercher dans le jeu de données sélectionné pour les valeurs du menu déroulant.
      * **Champ du filtre**\
        Spécifie le champ dont la valeur est utilisée pour pré-filtrer les résultats de la configuration de recherche lov avant que le menu déroulant principal ne soit rempli.
      * **Valeur du filtre** (facultatif)\
        Ajoutez des filtres statiques pour affiner davantage les résultats de la recherche.
      * **Requis**\
        Lorsqu’il est activé, ce champ doit être renseigné avant que tout menu déroulant dépendant puisse être rempli.
4.  Cliquez sur **Sauvegarder** pour créer le nouveau champ.

    ![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/fields_master_data_settings_23.png)

### Actions sur un champ existant

Pour gérer un champ existant dans une configuration de recherche lov, cliquez sur les trois points dans la colonne **Actions** à côté du champ.

![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/fields_master_data_settings_24.png)

**Actions disponibles :**

* **Éditer**\
  Modifiez le champ sélectionné. Après les modifications, cliquez sur **Sauvegarder** pour appliquer.
*   **Supprimer**\
    Supprime définitivement le champ après confirmation.

    ![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/fields_master_data_settings_20.png)
