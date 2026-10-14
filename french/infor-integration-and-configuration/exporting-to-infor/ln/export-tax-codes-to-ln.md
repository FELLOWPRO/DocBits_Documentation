# Exporter les codes de taxe vers LN

## **Aperçu :**

\
Ce guide vous accompagnera dans le processus de configuration pour garantir que les codes de taxe sont correctement exportés de DocBits vers LN.

## **Codes de taxe uniques**

### **Étape 1 : Configurer la liste de valeurs**

1.  Allez dans **Paramètres** -> **Traitement des documents** -> **Liste de valeurs**.

    <figure><img src="../../../.gitbook/assets/TaxCodes_1.png" alt=""><figcaption></figcaption></figure>
2.  Cliquez sur **Nouveau**.

    <figure><img src="../../../.gitbook/assets/TaxCodes_2.png" alt=""><figcaption></figcaption></figure>
3.  Créez une liste avec le nom `Tax_Country` et cliquez sur **ENREGISTRER**.

    <figure><img src="../../../.gitbook/assets/TaxCodes_3.png" alt="" width="563"><figcaption></figcaption></figure>
4.  Créez les trois listes supplémentaires suivantes :

    * `Tax_Code_Full`
    * `Tax_Code_Reduced`
    * `Tax_Code_Free`

    <div><figure><img src="../../../.gitbook/assets/TaxCodes_28.png" alt=""><figcaption></figcaption></figure> <figure><img src="../../../.gitbook/assets/TaxCodes_29.png" alt=""><figcaption></figcaption></figure> <figure><img src="../../../.gitbook/assets/TaxCodes_30.png" alt=""><figcaption></figcaption></figure></div>
5.  Cliquez sur l'une des listes nouvellement créées pour l'ouvrir. Ensuite, appuyez sur le bouton **Ajouter une ligne** pour ajouter une nouvelle ligne.

    <figure><img src="../../../.gitbook/assets/TaxCode_4.png" alt=""><figcaption></figcaption></figure>
6.  Entrez les valeurs respectives souhaitées de **LN** et appuyez sur **ENREGISTRER** pour sauvegarder les modifications.

    * Si vous avez plusieurs valeurs, vous pouvez cliquer sur **Ajouter d'autres valeurs** pour les ajouter.

    <div><figure><img src="../../../.gitbook/assets/TaxCodes_5.png" alt=""><figcaption></figcaption></figure> <figure><img src="../../../.gitbook/assets/TaxCodes_27.png" alt=""><figcaption></figcaption></figure></div>

    * **REMARQUE :** Vous pouvez trouver les codes de taxe dans LN sous : **Common** → **Taxation** → **Master Data** → **Tax Codes** → **Tax Codes by Country**

    <figure><img src="../../../.gitbook/assets/TaxCodes_LN.png" alt=""><figcaption></figcaption></figure>

### **Étape 2 : Ajouter des champs dans DocBits**

1.  Naviguez vers **Paramètres** -> **Paramètres globaux** -> **Types de documents**.

    <figure><img src="../../../.gitbook/assets/TaxCodes_6.png" alt=""><figcaption></figcaption></figure>
2.  Choisissez le menu **Champs** correspondant au type de document où vous souhaitez ajouter les champs.

    <figure><img src="../../../.gitbook/assets/TaxCodes_7.png" alt=""><figcaption></figcaption></figure>
3.  Sous **TVA et montants**, créez six nouveaux champs comme suit:

    <figure><img src="../../../.gitbook/assets/TaxCodes_8.png" alt=""><figcaption></figcaption></figure>

<table data-header-hidden><thead><tr><th width="306"></th><th width="139"></th><th width="119"></th><th></th></tr></thead><tbody><tr><td><strong>Nom</strong></td><td><strong>Titre</strong></td><td><strong>Type de champ</strong></td><td><strong>Liste de valeurs</strong></td></tr><tr><td><code>tax_country</code></td><td>Tax Country</td><td>Dropdown</td><td>Tax_Country</td></tr><tr><td><code>tax_country_2</code></td><td>Tax Country Reduced</td><td>Dropdown</td><td>Tax_Country</td></tr><tr><td><code>tax_country_3</code></td><td>Tax Country Free</td><td>Dropdown</td><td>Tax_Country</td></tr><tr><td><code>tax_code_without_country</code></td><td>Tax Code</td><td>Dropdown</td><td>Tax_Code_Full</td></tr><tr><td><code>tax_code_without_country_2</code></td><td>Tax Code Reduced</td><td>Dropdown</td><td>Tax_Code_Reduced</td></tr><tr><td><code>tax_code_without_country_3</code></td><td>Tax Code Free</td><td>Dropdown</td><td>Tax_Code_Free</td></tr></tbody></table>

<div><figure><img src="../../../.gitbook/assets/TaxCodes_10.png" alt=""><figcaption></figcaption></figure> <figure><img src="../../../.gitbook/assets/TaxCodes_11.png" alt=""><figcaption></figcaption></figure> <figure><img src="../../../.gitbook/assets/TaxCodes_12.png" alt=""><figcaption></figcaption></figure></div>

<div><figure><img src="../../../.gitbook/assets/TaxCodes_13.png" alt=""><figcaption></figcaption></figure> <figure><img src="../../../.gitbook/assets/TaxCodes_14.png" alt=""><figcaption></figcaption></figure> <figure><img src="../../../.gitbook/assets/TaxCodes_15.png" alt=""><figcaption></figcaption></figure></div>

4.  Après avoir enregistré chaque champ, cliquez sur **Enregistrer les paramètres** pour appliquer les modifications.

    <figure><img src="../../../.gitbook/assets/TaxCodes_20.png" alt=""><figcaption></figcaption></figure>

### **Étape 3 : Modifier la mise en page**

1.  Allez dans **Paramètres** -> **Paramètres globaux** -> **Types de documents**.

    <figure><img src="../../../.gitbook/assets/TaxCodes_6.png" alt=""><figcaption></figcaption></figure>
2.  Ouvrez le menu **Modifier la mise en page** pour le type de document que vous souhaitez modifier.

    <figure><img src="../../../.gitbook/assets/TaxCodes_19.png" alt=""><figcaption></figcaption></figure>
3.  Sélectionnez l'**Origine du document** appropriée pour laquelle vous souhaitez appliquer les codes de taxe

    <figure><img src="../../../.gitbook/assets/TaxCodes_26.png" alt=""><figcaption></figcaption></figure>
4.  Faites défiler jusqu'à la section **Tax Details**.

    <figure><img src="../../../.gitbook/assets/TaxCodes_21.png" alt=""><figcaption></figcaption></figure>
5. Développez le menu déroulant **Éléments du formulaire**.
6.  Dans la section **Tax Details**, utilisez l'outil **Horizontal Separator**. Faites-le glisser et déposez-le entre les sous-sections dans la section fiscale pour les séparer clairement et réduire la confusion.

    <figure><img src="../../../.gitbook/assets/TaxCodes_22.png" alt=""><figcaption></figcaption></figure>
7. Développez le menu déroulant **Champs**.
8.  Recherchez **Tax Country** et faites glisser le champ dans son domaine respectif.

    <figure><img src="../../../.gitbook/assets/TaxCodes_23.png" alt=""><figcaption></figcaption></figure>
9.  Recherchez **Tax Code** et faites glisser le champ dans son domaine correspondant.

    <figure><img src="../../../.gitbook/assets/TaxCodes_24.png" alt=""><figcaption></figcaption></figure>
10. Enregistrez le modèle.

    <figure><img src="../../../.gitbook/assets/TaxCodes_25.png" alt=""><figcaption></figcaption></figure>

### Étape 4 : Vérifiez que tout a fonctionné

Après avoir téléchargé un nouveau document dans DocBits avec les paramètres de document corrects sélectionnés, vous devriez maintenant être en mesure de sélectionner les codes de taxe que vous avez ajoutés aux listes à l'étape 1.

<figure><img src="../../../.gitbook/assets/TaxCodes_31.png" alt=""><figcaption></figcaption></figure>

## Code de taxe multiple

### **Étape 1 : Configurer la liste de valeurs**

1.  Allez dans **Paramètres** -> **Traitement des documents** -> **Liste de valeurs**.

    <figure><img src="../../../.gitbook/assets/TaxCodes_1.png" alt=""><figcaption></figcaption></figure>
2.  Cliquez sur **Nouveau**.

    <figure><img src="../../../.gitbook/assets/TaxCodes_2.png" alt=""><figcaption></figcaption></figure>
3.  Créez une liste avec le nom `Tax_Country` et cliquez sur **ENREGISTRER**.

    <figure><img src="../../../.gitbook/assets/TaxCodes_3.png" alt="" width="563"><figcaption></figcaption></figure>
4.  Créez les trois listes supplémentaires suivantes :

    * `Tax_Code_Full`
    * `Tax_Code_Reduced`
    * `Tax_Code_Free`

    <div><figure><img src="../../../.gitbook/assets/TaxCodes_28.png" alt=""><figcaption></figcaption></figure> <figure><img src="../../../.gitbook/assets/TaxCodes_29.png" alt=""><figcaption></figcaption></figure> <figure><img src="../../../.gitbook/assets/TaxCodes_30.png" alt=""><figcaption></figcaption></figure></div>
5.  Cliquez sur l'une des listes nouvellement créées pour l'ouvrir. Ensuite, appuyez sur le bouton **Ajouter une ligne** pour ajouter une nouvelle ligne.

    <figure><img src="../../../.gitbook/assets/TaxCode_4.png" alt=""><figcaption></figcaption></figure>
6.  Entrez les valeurs respectives souhaitées de **LN** et appuyez sur **ENREGISTRER** pour sauvegarder les modifications.

    * Si vous avez plusieurs valeurs, vous pouvez cliquer sur **Ajouter d'autres valeurs** pour les ajouter.

    <div><figure><img src="../../../.gitbook/assets/TaxCodes_5.png" alt=""><figcaption></figcaption></figure> <figure><img src="../../../.gitbook/assets/TaxCodes_27.png" alt=""><figcaption></figcaption></figure></div>

    * **REMARQUE :** Vous pouvez trouver les codes de taxe dans LN sous : **Common** → **Taxation** → **Master Data** → **Tax Codes** → **Tax Codes by Country**

    <figure><img src="../../../.gitbook/assets/TaxCodes_LN.png" alt=""><figcaption></figcaption></figure>

### **Étape 2 : Ajouter des champs dans DocBits**

1.  Naviguez vers **Paramètres** -> **Paramètres globaux** -> **Types de documents**.

    <figure><img src="../../../.gitbook/assets/TaxCodes_6.png" alt=""><figcaption></figcaption></figure>
2.  Choisissez le menu **Champs** correspondant au type de document où vous souhaitez ajouter les champs.

    <figure><img src="../../../.gitbook/assets/TaxCodes_7.png" alt=""><figcaption></figcaption></figure>
3.  Sous **TVA et montants**, créez six nouveaux champs comme suit:

    <figure><img src="../../../.gitbook/assets/TaxCodes_8.png" alt=""><figcaption></figcaption></figure>

<table data-header-hidden><thead><tr><th width="306"></th><th width="139"></th><th width="119"></th><th></th></tr></thead><tbody><tr><td><strong>Nom</strong></td><td><strong>Titre</strong></td><td><strong>Type de champ</strong></td><td><strong>Liste de valeurs</strong></td></tr><tr><td><code>tax_country</code></td><td>Tax Country</td><td>Dropdown</td><td>Tax_Country</td></tr><tr><td><code>tax_country_2</code></td><td>Tax Country Reduced</td><td>Dropdown</td><td>Tax_Country</td></tr><tr><td><code>tax_country_3</code></td><td>Tax Country Free</td><td>Dropdown</td><td>Tax_Country</td></tr><tr><td><code>tax_code_without_country</code></td><td>Tax Code</td><td>Dropdown</td><td>Tax_Code_Full</td></tr><tr><td><code>tax_code_without_country_2</code></td><td>Tax Code Reduced</td><td>Dropdown</td><td>Tax_Code_Reduced</td></tr><tr><td><code>tax_code_without_country_3</code></td><td>Tax Code Free</td><td>Dropdown</td><td>Tax_Code_Free</td></tr></tbody></table>

<div><figure><img src="../../../.gitbook/assets/TaxCodes_10.png" alt=""><figcaption></figcaption></figure> <figure><img src="../../../.gitbook/assets/TaxCodes_11.png" alt=""><figcaption></figcaption></figure> <figure><img src="../../../.gitbook/assets/TaxCodes_12.png" alt=""><figcaption></figcaption></figure></div>

<div><figure><img src="../../../.gitbook/assets/TaxCodes_13.png" alt=""><figcaption></figcaption></figure> <figure><img src="../../../.gitbook/assets/TaxCodes_14.png" alt=""><figcaption></figcaption></figure> <figure><img src="../../../.gitbook/assets/TaxCodes_15.png" alt=""><figcaption></figcaption></figure></div>

4.  Après avoir enregistré chaque champ, cliquez sur **Enregistrer les paramètres** pour appliquer les modifications.

    <figure><img src="../../../.gitbook/assets/TaxCodes_20.png" alt=""><figcaption></figcaption></figure>

### **Étape 3 : Modifier la mise en page**

1.  Allez dans **Paramètres** -> **Paramètres globaux** -> **Types de documents**.

    <figure><img src="../../../.gitbook/assets/TaxCodes_6.png" alt=""><figcaption></figcaption></figure>
2.  Ouvrez le menu **Modifier la mise en page** pour le type de document que vous souhaitez modifier.

    <figure><img src="../../../.gitbook/assets/TaxCodes_19.png" alt=""><figcaption></figcaption></figure>
3.  Sélectionnez l'**Origine du document** appropriée pour laquelle vous souhaitez appliquer les codes de taxe

    <figure><img src="../../../.gitbook/assets/TaxCodes_26.png" alt=""><figcaption></figcaption></figure>
4.  Faites défiler jusqu'à la section **Tax Details**.

    <figure><img src="../../../.gitbook/assets/TaxCodes_21.png" alt=""><figcaption></figcaption></figure>
5. Développez le menu déroulant **Éléments du formulaire**.
6.  Dans la section Tax Details, utilisez l'outil **Sub Group**. Faites-le glisser et déposez-le à côté d'un champ existant.

    <figure><img src="../../../.gitbook/assets/TaxCodesMulti_1.png" alt=""><figcaption></figcaption></figure>
7.  Pour nommer votre sous-groupe, cliquez sur le sous-groupe et entrez le nom souhaité dans le champ **Étiquette**.

    <div><figure><img src="../../../.gitbook/assets/TaxCodesMulti_2.png" alt=""><figcaption></figcaption></figure> <figure><img src="../../../.gitbook/assets/TaxCodesMulti_3.png" alt=""><figcaption></figcaption></figure></div>
8.  Faites glisser et déposez les champs qui correspondent à ce groupe dans le champ **Sub Group**.

    <figure><img src="../../../.gitbook/assets/TaxCodeMulti_4.png" alt=""><figcaption></figcaption></figure>
9. Développez le menu déroulant **Champs**.
10. Recherchez **Tax** et faites glisser et déposer les champs respectifs, tels que **Tax Country** et **Tax Code**, dans le sous-groupe correspondant.

    <figure><img src="../../../.gitbook/assets/TaxCodeMulti_5.png" alt=""><figcaption></figcaption></figure>
11. Répétez les étapes 5 à 10 2 fois pour atteindre l'état suivant:

    <figure><img src="../../../.gitbook/assets/TaxCodeMulti_6.png" alt=""><figcaption></figcaption></figure>
12. Enregistrez le modèle.

    <figure><img src="../../../.gitbook/assets/TaxCodeMulti_7.png" alt=""><figcaption></figcaption></figure>

### Étape 4 : Vérifiez que tout a fonctionné et les changements résultants

Après avoir téléchargé un nouveau document dans DocBits avec les paramètres de document corrects sélectionnés, vous pourrez sélectionner les codes de taxe que vous avez ajoutés à l'étape 1 et ajouter plusieurs codes de taxe configurés à l'étape 3.

* Le document commencera par trois sections distinctes : une pour les montants de taxe pleine, une pour les montants de taxe réduite et une pour les montants de taxe gratuite.
* Cliquer sur le bouton plus dans une section créera un duplicata, permettant plusieurs soumissions au taux de taxe sélectionné.

<figure><img src="../../../.gitbook/assets/TaxCodeMulti_8.png" alt=""><figcaption></figcaption></figure>

* Les sections peuvent être supprimées en cliquant sur le bouton de suppression.

<figure><img src="../../../.gitbook/assets/TaxCodeMulti_9.png" alt=""><figcaption></figcaption></figure>

* Les montants totaux seront calculés comme une somme de toutes les sections.
* La validation du montant total sera modifiée en fonction de toutes les sections fiscales.
* Les scripts pour les nouvelles sections ne peuvent être appliqués qu'une fois que des champs ont été ajoutés à la vue.

### Remarque pour LN :

Dans **LN**, la position USt sera remplie en fonction du numéro de position du menu déroulant Tax Code/Tax Country. Seul le numéro de position sera envoyé à l'exportation.

<figure><img src="../../../.gitbook/assets/TaxCodesLN_2.png" alt=""><figcaption></figcaption></figure>

<figure><img src="../../../.gitbook/assets/TaxCodesLN_3.png" alt=""><figcaption></figcaption></figure>

#### **Mapping d'exportation**

Pour lier la ligne de taxe à la ligne de coût :

1. Ajoutez `TaxLine` à la liste **InvoiceCostFields**.
2. Ajoutez l'entrée suivante, suivant l'exemple ci-dessous :\
   `ICF_TaxLine = TF_position`

<figure><img src="../../../.gitbook/assets/TaxCodeMulti_10.png" alt=""><figcaption></figcaption></figure>
