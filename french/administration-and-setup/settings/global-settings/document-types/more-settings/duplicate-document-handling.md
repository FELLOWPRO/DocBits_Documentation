# Détection des doublons

## Aperçu

Dans **DocBits**, vous pouvez filtrer les documents en double en spécifiant quels champs doivent correspondre et en définissant un intervalle de temps pendant lequel les doublons doivent être détectés.

Cette page fournit un guide détaillé sur la façon d'activer et d'utiliser efficacement la fonctionnalité **Détection des doublons**.

## Activation de la Détection des doublons

Pour activer la détection des documents en double dans **DocBits**, suivez ces étapes :

1.  Accédez à **Paramètres** → **Paramètres globaux** → **Types de documents**.

    ![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/Calculate_PO_unit_price_1.png)
2.  Sélectionnez le **Type de document** souhaité et cliquez sur **Plus de paramètres**.

    ![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/Calculate_PO_unit_price_2.png)
3.  Allez à la section **Détection des doublons**.

    ![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/DuplicateDocument_3.png)

DocBits fournit deux options pour identifier les documents en double :

1. **Détection des documents en double** :\
   Cette fonctionnalité vérifie les documents en double téléchargés sur **DocBits** en fonction des critères sélectionnés. Si un document correspond aux critères sélectionnés parmi d'autres documents, il sera signalé comme un doublon.
2.  **Détection des factures en double** (Disponible uniquement pour le type de document **Facture**) :\
    Cette fonctionnalité nécessite la synchronisation des factures fournisseurs d'Infor vers DocBits. Elle compare les numéros de facture dans le tableau de bord DocBits avec ceux d'Infor. Si le même numéro de facture apparaît plus d'une fois, il sera signalé comme un doublon.

    <mark style="color:red;">**Remarque**</mark> : L'utilisation de la fonctionnalité **Détection des factures en double** entraînera un coût de crédit supplémentaire.

## Filtrer les documents qui doivent être détectés comme doublons

Une fois la **Détection des doublons** activée, deux menus déroulants seront disponibles pour la configuration :

*   **Champs de détection des doublons**\
    Sélectionnez les champs qui doivent être utilisés pour identifier les doublons (par exemple, Identification du fournisseur, Date, Numéro de facture, etc.). Les documents correspondant à ces champs seront signalés comme des doublons.

    ![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/DuplicateDocument_4.png)
*   **Intervalle de détection des doublons**

    Utilisez ce paramètre pour définir la plage de temps dans laquelle les doublons sont détectés. Les documents téléchargés dans l'intervalle sélectionné seront comparés les uns aux autres en fonction des champs sélectionnés.

    **Options disponibles :**

    * 1 mois
    * 3 mois (Recommandé)
    * 6 mois
    * 1 an

    <mark style="color:red;">**Remarque**</mark> : Un intervalle de 3 mois est recommandé pour garantir des performances optimales. La sélection d'un intervalle plus long peut entraîner des temps de chargement plus lents du tableau de bord.

    ![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/DuplicateDocument_6.png)

## Affichage des documents en double sur le Tableau de bord

Une fois la **Détection des doublons** activée, tous les documents identifiés comme doublons afficheront une icône d'indicateur de doublon sur le tableau de bord.

*   Cliquez sur cette icône pour ouvrir les enregistrements correspondants dans une vue en écran partagé pour une comparaison facile.\
    <mark style="color:red;">**Remarque**</mark> : L'icône n'apparaîtra que si au moins un doublon a été détecté pour le document.

    ![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/DuplicateDocument_7.png)
*   Lors de la visualisation d'un document signalé, une barre d'avertissement apparaîtra en haut, indiquant que le document est un doublon.

    ![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/DuplicateDocument_5.png)
