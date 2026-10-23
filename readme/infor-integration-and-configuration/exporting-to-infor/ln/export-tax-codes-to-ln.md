# Exporter les codes de taxe vers LN

## **Aperçu :**

\
Ce guide vous accompagnera dans le processus de configuration pour garantir que les codes de taxe sont correctement exportés de DocBits vers LN.

## **Codes de taxe uniques**

### **Étape 1 : Configurer la liste de valeurs**

1.  Allez dans **Paramètres** -> **Traitement des documents** -> **Liste de valeurs**.

    <figure><img src="../../../.gitbook/assets/site-extra-list-of-values-fr.png" alt="Liste de valeurs dans l’interface française actuelle. Les noms des listes propres à l’organisation sont masqués ; aucune liste n’a été créée."><figcaption><p>Liste de valeurs dans l’interface française actuelle. Les noms des listes propres à l’organisation sont masqués ; aucune liste n’a été créée.</p></figcaption></figure>
2.  Cliquez sur **Nouveau**.

    <figure><img src="../../../.gitbook/assets/TaxCodes_2.png" alt="Page List of Values avec le bouton New en surbrillance dans la barre d'outils"><figcaption></figcaption></figure>
3.  Créez une liste avec le nom `Tax_Country` et cliquez sur **ENREGISTRER**.

    <figure><img src="../../../.gitbook/assets/TaxCodes_3.png" alt="Boîte de dialogue New List of Values avec le nom Tax_Country saisi et le bouton Save visible" width="563"><figcaption></figcaption></figure>
4.  Créez les trois listes supplémentaires suivantes :

    * `Tax_Code_Full`
    * `Tax_Code_Reduced`
    * `Tax_Code_Free`

    <div><figure><img src="../../../.gitbook/assets/TaxCodes_28.png" alt="Page List of Values avec l'entrée Tax_Code_Full créée dans la liste"><figcaption></figcaption></figure> <figure><img src="../../../.gitbook/assets/TaxCodes_29.png" alt="Page List of Values avec l'entrée Tax_Code_Reduced créée dans la liste"><figcaption></figcaption></figure> <figure><img src="../../../.gitbook/assets/TaxCodes_30.png" alt="Page List of Values avec l'entrée Tax_Code_Free créée dans la liste"><figcaption></figcaption></figure></div>
5.  Cliquez sur l'une des listes nouvellement créées pour l'ouvrir. Ensuite, appuyez sur le bouton **Ajouter une ligne** pour ajouter une nouvelle ligne.

    <figure><img src="../../../.gitbook/assets/TaxCode_4.png" alt="Page List of Values pour Tax_Country avec le bouton Add Row visible dans la barre d'outils"><figcaption></figcaption></figure>
6.  Entrez les valeurs respectives souhaitées de **LN** et appuyez sur **ENREGISTRER** pour sauvegarder les modifications.

    * Pour plusieurs codes, ajoutez et enregistrez une ligne par valeur dans la liste concernée.

    <div><figure><img src="../../../.gitbook/assets/TaxCodes_5.png" alt="Liste de valeurs de Tax_Country avec une nouvelle entrée de ligne et le bouton Save"><figcaption></figcaption></figure> <figure><img src="../../../.gitbook/assets/site-extra-list-value-new-fr.png" alt="Formulaire français de création d’une valeur : valeur, sous-organisation, synonymes et traductions. Aucun code de taxe n’a été saisi ou enregistré ; le choix Anglais concerne la langue d’une traduction, pas celle de l’interface."><figcaption><p>Formulaire français de création d’une valeur : valeur, sous-organisation, synonymes et traductions. Aucun code de taxe n’a été saisi ou enregistré ; le choix Anglais concerne la langue d’une traduction, pas celle de l’interface.</p></figcaption></figure></div>

    * **REMARQUE :** Vous pouvez trouver les codes de taxe dans LN sous : **Common** → **Taxation** → **Master Data** → **Tax Codes** → **Tax Codes by Country**

    <figure><img src="../../../.gitbook/assets/TaxCodes_LN.png" alt="Écran LN Tax Codes by Country sous Common, Taxation, Master Data affichant la vue d'ensemble des codes de taxe"><figcaption></figcaption></figure>

### **Étape 2 : Ajouter des champs dans DocBits**

1.  Naviguez vers **Paramètres** -> **Paramètres globaux** -> **Types de documents**.

    <figure><img src="../../../.gitbook/assets/site-extra-document-types-fr.png" alt="Types de documents dans l’interface française actuelle. Choisissez Champs dans la carte du type concerné ; aucun interrupteur n’a été modifié."><figcaption><p>Types de documents dans l’interface française actuelle. Choisissez Champs dans la carte du type concerné ; aucun interrupteur n’a été modifié.</p></figcaption></figure>
2.  Choisissez le menu **Champs** correspondant au type de document où vous souhaitez ajouter les champs.

    <figure><img src="../../../.gitbook/assets/TaxCodes_7.png" alt="Page Document Types avec l'option Fields ouverte pour un type de document dans le menu"><figcaption></figcaption></figure>
3.  Sous **TVA et montants**, créez six nouveaux champs comme suit:

    <figure><img src="../../../.gitbook/assets/TaxCodes_8.png" alt="Page des paramètres des champs pour un type de document avec la section VAT and Amounts dépliée"><figcaption></figcaption></figure>

<table data-header-hidden><thead><tr><th width="306"></th><th width="139"></th><th width="119"></th><th></th></tr></thead><tbody><tr><td><strong>Nom</strong></td><td><strong>Titre</strong></td><td><strong>Type de champ</strong></td><td><strong>Liste de valeurs</strong></td></tr><tr><td><code>tax_country</code></td><td>Pays de taxation</td><td>Dropdown</td><td>Tax_Country</td></tr><tr><td><code>tax_country_2</code></td><td>Pays de taxe réduit</td><td>Dropdown</td><td>Tax_Country</td></tr><tr><td><code>tax_country_3</code></td><td>Pays sans taxe</td><td>Dropdown</td><td>Tax_Country</td></tr><tr><td><code>tax_code_without_country</code></td><td>Code de taxe</td><td>Dropdown</td><td>Tax_Code_Full</td></tr><tr><td><code>tax_code_without_country_2</code></td><td>Code de taxe — taux réduit</td><td>Dropdown</td><td>Tax_Code_Reduced</td></tr><tr><td><code>tax_code_without_country_3</code></td><td>Code de taxe — sans taxe</td><td>Dropdown</td><td>Tax_Code_Free</td></tr></tbody></table>

<div><figure><img src="../../../.gitbook/assets/TaxCodes_10.png" alt="Page de configuration des champs avec le nouveau champ déroulant Tax Country et la liste de valeurs Tax_Country"><figcaption></figcaption></figure> <figure><img src="../../../.gitbook/assets/TaxCodes_11.png" alt="Page Fields settings avec le nouveau champ déroulant Tax Country Reduced et la List of Values Tax_Country"><figcaption></figcaption></figure> <figure><img src="../../../.gitbook/assets/TaxCodes_12.png" alt="Page des paramètres des champs avec le nouveau champ déroulant Tax Country Free et la List of Values Tax_Country"><figcaption></figcaption></figure></div>

<div><figure><img src="../../../.gitbook/assets/TaxCodes_13.png" alt="Page Fields settings avec le nouveau champ déroulant Tax Code et la List of Values Tax_Code_Full"><figcaption></figcaption></figure> <figure><img src="../../../.gitbook/assets/TaxCodes_14.png" alt="Page de paramètres Fields avec un nouveau champ déroulant Tax Code Reduced et la List of Values Tax_Code_Reduced"><figcaption></figcaption></figure> <figure><img src="../../../.gitbook/assets/TaxCodes_15.png" alt="Page Fields settings avec un nouveau champ déroulant Tax Code Free et la List of Values Tax_Code_Free"><figcaption></figcaption></figure></div>

4.  Après avoir enregistré chaque champ, cliquez sur **Enregistrer les paramètres** pour appliquer les modifications.

    <figure><img src="../../../.gitbook/assets/TaxCodes_20.png" alt="Page Fields settings avec les champs de taxe nouvellement créés et le bouton Save Settings mis en évidence"><figcaption></figcaption></figure>

### **Étape 3 : Modifier la mise en page**

1.  Allez dans **Paramètres** -> **Paramètres globaux** -> **Types de documents**.

    <figure><img src="../../../.gitbook/assets/site-extra-document-types-fr.png" alt="Types de documents dans l’interface française actuelle. Choisissez Champs dans la carte du type concerné ; aucun interrupteur n’a été modifié."><figcaption><p>Types de documents dans l’interface française actuelle. Choisissez Champs dans la carte du type concerné ; aucun interrupteur n’a été modifié.</p></figcaption></figure>
2.  Ouvrez le menu **Modifier la mise en page** pour le type de document que vous souhaitez modifier.

    <figure><img src="../../../.gitbook/assets/TaxCodes_19.png" alt="Page Document Types avec l'option Edit Layout ouverte pour un type de document dans le menu"><figcaption></figcaption></figure>
3.  Sélectionnez l'**Origine du document** appropriée pour laquelle vous souhaitez appliquer les codes de taxe

    <figure><img src="../../../.gitbook/assets/TaxCodes_26.png" alt="Éditeur de mise en page avec le menu déroulant Document Origin ouvert pour sélectionner l'origine appropriée"><figcaption></figcaption></figure>
4.  Faites défiler jusqu'à la section **Tax Details**.

    <figure><img src="../../../.gitbook/assets/TaxCodes_21.png" alt="Éditeur de mise en page défilé jusqu'à la section Tax Details du modèle de document"><figcaption></figcaption></figure>
5. Développez le menu déroulant **Éléments du formulaire**.
6.  Dans la section **Tax Details**, utilisez l'outil **Horizontal Separator**. Faites-le glisser et déposez-le entre les sous-sections dans la section fiscale pour les séparer clairement et réduire la confusion.

    <figure><img src="../../../.gitbook/assets/TaxCodes_22.png" alt="Éditeur de mise en page avec le menu déroulant Form Elements développé et l'outil Horizontal Separator en surbrillance"><figcaption></figcaption></figure>
7. Développez le menu déroulant **Champs**.
8.  Recherchez **Tax Country** et faites glisser le champ dans son domaine respectif.

    <figure><img src="../../../.gitbook/assets/TaxCodes_23.png" alt="Éditeur de mise en page avec le menu déroulant Form Fields déplié et le champ Tax Country en cours de recherche"><figcaption></figcaption></figure>
9.  Recherchez **Tax Code** et faites glisser le champ dans son domaine correspondant.

    <figure><img src="../../../.gitbook/assets/TaxCodes_24.png" alt="Éditeur de mise en page avec le menu déroulant Form Fields déployé et la recherche du champ Tax Code en cours"><figcaption></figcaption></figure>
10. Enregistrez le modèle.

    <figure><img src="../../../.gitbook/assets/TaxCodes_25.png" alt="Éditeur de mise en page avec le bouton Save mis en évidence après le placement des champs de taxe"><figcaption></figcaption></figure>

### Étape 4 : Vérifiez que tout a fonctionné

Après avoir téléchargé un nouveau document dans DocBits avec les paramètres de document corrects sélectionnés, vous devriez maintenant être en mesure de sélectionner les codes de taxe que vous avez ajoutés aux listes à l'étape 1.

<figure><img src="../../../.gitbook/assets/TaxCodes_31.png" alt="Écran de validation d'un document téléversé avec les valeurs de la liste déroulante du code de taxe ouvertes"><figcaption></figcaption></figure>

## Code de taxe multiple

### **Étape 1 : Configurer la liste de valeurs**

1.  Allez dans **Paramètres** -> **Traitement des documents** -> **Liste de valeurs**.

    <figure><img src="../../../.gitbook/assets/site-extra-list-of-values-fr.png" alt="Liste de valeurs dans l’interface française actuelle. Les noms des listes propres à l’organisation sont masqués ; aucune liste n’a été créée."><figcaption><p>Liste de valeurs dans l’interface française actuelle. Les noms des listes propres à l’organisation sont masqués ; aucune liste n’a été créée.</p></figcaption></figure>
2.  Cliquez sur **Nouveau**.

    <figure><img src="../../../.gitbook/assets/TaxCodes_2.png" alt="Page List of Values avec le bouton New en surbrillance dans la barre d'outils"><figcaption></figcaption></figure>
3.  Créez une liste avec le nom `Tax_Country` et cliquez sur **ENREGISTRER**.

    <figure><img src="../../../.gitbook/assets/TaxCodes_3.png" alt="Boîte de dialogue New List of Values avec le nom Tax_Country saisi et le bouton Save visible" width="563"><figcaption></figcaption></figure>
4.  Créez les trois listes supplémentaires suivantes :

    * `Tax_Code_Full`
    * `Tax_Code_Reduced`
    * `Tax_Code_Free`

    <div><figure><img src="../../../.gitbook/assets/TaxCodes_28.png" alt="Page List of Values avec l'entrée Tax_Code_Full créée dans la liste"><figcaption></figcaption></figure> <figure><img src="../../../.gitbook/assets/TaxCodes_29.png" alt="Page List of Values avec l'entrée Tax_Code_Reduced créée dans la liste"><figcaption></figcaption></figure> <figure><img src="../../../.gitbook/assets/TaxCodes_30.png" alt="Page List of Values avec l'entrée Tax_Code_Free créée dans la liste"><figcaption></figcaption></figure></div>
5.  Cliquez sur l'une des listes nouvellement créées pour l'ouvrir. Ensuite, appuyez sur le bouton **Ajouter une ligne** pour ajouter une nouvelle ligne.

    <figure><img src="../../../.gitbook/assets/TaxCode_4.png" alt="Page List of Values pour Tax_Country avec le bouton Add Row visible dans la barre d'outils"><figcaption></figcaption></figure>
6.  Entrez les valeurs respectives souhaitées de **LN** et appuyez sur **ENREGISTRER** pour sauvegarder les modifications.

    * Pour plusieurs codes, ajoutez et enregistrez une ligne par valeur dans la liste concernée.

    <div><figure><img src="../../../.gitbook/assets/TaxCodes_5.png" alt="Liste de valeurs de Tax_Country avec une nouvelle entrée de ligne et le bouton Save"><figcaption></figcaption></figure> <figure><img src="../../../.gitbook/assets/site-extra-list-value-new-fr.png" alt="Formulaire français de création d’une valeur : valeur, sous-organisation, synonymes et traductions. Aucun code de taxe n’a été saisi ou enregistré ; le choix Anglais concerne la langue d’une traduction, pas celle de l’interface."><figcaption><p>Formulaire français de création d’une valeur : valeur, sous-organisation, synonymes et traductions. Aucun code de taxe n’a été saisi ou enregistré ; le choix Anglais concerne la langue d’une traduction, pas celle de l’interface.</p></figcaption></figure></div>

    * **REMARQUE :** Vous pouvez trouver les codes de taxe dans LN sous : **Common** → **Taxation** → **Master Data** → **Tax Codes** → **Tax Codes by Country**

    <figure><img src="../../../.gitbook/assets/TaxCodes_LN.png" alt="Écran LN Tax Codes by Country sous Common, Taxation, Master Data affichant la vue d'ensemble des codes de taxe"><figcaption></figcaption></figure>

### **Étape 2 : Ajouter des champs dans DocBits**

1.  Naviguez vers **Paramètres** -> **Paramètres globaux** -> **Types de documents**.

    <figure><img src="../../../.gitbook/assets/site-extra-document-types-fr.png" alt="Types de documents dans l’interface française actuelle. Choisissez Champs dans la carte du type concerné ; aucun interrupteur n’a été modifié."><figcaption><p>Types de documents dans l’interface française actuelle. Choisissez Champs dans la carte du type concerné ; aucun interrupteur n’a été modifié.</p></figcaption></figure>
2.  Choisissez le menu **Champs** correspondant au type de document où vous souhaitez ajouter les champs.

    <figure><img src="../../../.gitbook/assets/TaxCodes_7.png" alt="Page Document Types avec l'option Fields ouverte pour un type de document dans le menu"><figcaption></figcaption></figure>
3.  Sous **TVA et montants**, créez six nouveaux champs comme suit:

    <figure><img src="../../../.gitbook/assets/TaxCodes_8.png" alt="Page des paramètres des champs pour un type de document avec la section VAT and Amounts dépliée"><figcaption></figcaption></figure>

<table data-header-hidden><thead><tr><th width="306"></th><th width="139"></th><th width="119"></th><th></th></tr></thead><tbody><tr><td><strong>Nom</strong></td><td><strong>Titre</strong></td><td><strong>Type de champ</strong></td><td><strong>Liste de valeurs</strong></td></tr><tr><td><code>tax_country</code></td><td>Pays de taxation</td><td>Dropdown</td><td>Tax_Country</td></tr><tr><td><code>tax_country_2</code></td><td>Pays de taxe réduit</td><td>Dropdown</td><td>Tax_Country</td></tr><tr><td><code>tax_country_3</code></td><td>Pays sans taxe</td><td>Dropdown</td><td>Tax_Country</td></tr><tr><td><code>tax_code_without_country</code></td><td>Code de taxe</td><td>Dropdown</td><td>Tax_Code_Full</td></tr><tr><td><code>tax_code_without_country_2</code></td><td>Code de taxe — taux réduit</td><td>Dropdown</td><td>Tax_Code_Reduced</td></tr><tr><td><code>tax_code_without_country_3</code></td><td>Code de taxe — sans taxe</td><td>Dropdown</td><td>Tax_Code_Free</td></tr></tbody></table>

<div><figure><img src="../../../.gitbook/assets/TaxCodes_10.png" alt="Page de configuration des champs avec le nouveau champ déroulant Tax Country et la liste de valeurs Tax_Country"><figcaption></figcaption></figure> <figure><img src="../../../.gitbook/assets/TaxCodes_11.png" alt="Page Fields settings avec le nouveau champ déroulant Tax Country Reduced et la List of Values Tax_Country"><figcaption></figcaption></figure> <figure><img src="../../../.gitbook/assets/TaxCodes_12.png" alt="Page des paramètres des champs avec le nouveau champ déroulant Tax Country Free et la List of Values Tax_Country"><figcaption></figcaption></figure></div>

<div><figure><img src="../../../.gitbook/assets/TaxCodes_13.png" alt="Page Fields settings avec le nouveau champ déroulant Tax Code et la List of Values Tax_Code_Full"><figcaption></figcaption></figure> <figure><img src="../../../.gitbook/assets/TaxCodes_14.png" alt="Page de paramètres Fields avec un nouveau champ déroulant Tax Code Reduced et la List of Values Tax_Code_Reduced"><figcaption></figcaption></figure> <figure><img src="../../../.gitbook/assets/TaxCodes_15.png" alt="Page Fields settings avec un nouveau champ déroulant Tax Code Free et la List of Values Tax_Code_Free"><figcaption></figcaption></figure></div>

4.  Après avoir enregistré chaque champ, cliquez sur **Enregistrer les paramètres** pour appliquer les modifications.

    <figure><img src="../../../.gitbook/assets/TaxCodes_20.png" alt="Page Fields settings avec les champs de taxe nouvellement créés et le bouton Save Settings mis en évidence"><figcaption></figcaption></figure>

### **Étape 3 : Modifier la mise en page**

1.  Allez dans **Paramètres** -> **Paramètres globaux** -> **Types de documents**.

    <figure><img src="../../../.gitbook/assets/site-extra-document-types-fr.png" alt="Types de documents dans l’interface française actuelle. Choisissez Champs dans la carte du type concerné ; aucun interrupteur n’a été modifié."><figcaption><p>Types de documents dans l’interface française actuelle. Choisissez Champs dans la carte du type concerné ; aucun interrupteur n’a été modifié.</p></figcaption></figure>
2.  Ouvrez le menu **Modifier la mise en page** pour le type de document que vous souhaitez modifier.

    <figure><img src="../../../.gitbook/assets/TaxCodes_19.png" alt="Page Document Types avec l'option Edit Layout ouverte pour un type de document dans le menu"><figcaption></figcaption></figure>
3.  Sélectionnez l'**Origine du document** appropriée pour laquelle vous souhaitez appliquer les codes de taxe

    <figure><img src="../../../.gitbook/assets/TaxCodes_26.png" alt="Éditeur de mise en page avec le menu déroulant Document Origin ouvert pour sélectionner l'origine appropriée"><figcaption></figcaption></figure>
4.  Faites défiler jusqu'à la section **Tax Details**.

    <figure><img src="../../../.gitbook/assets/TaxCodes_21.png" alt="Éditeur de mise en page défilé jusqu'à la section Tax Details du modèle de document"><figcaption></figcaption></figure>
5. Développez le menu déroulant **Éléments du formulaire**.
6.  Dans la section Tax Details, utilisez l'outil **Sub Group**. Faites-le glisser et déposez-le à côté d'un champ existant.

    <figure><img src="../../../.gitbook/assets/TaxCodesMulti_1.png" alt="Éditeur de mise en page avec le menu déroulant Form Elements développé et l'outil Sub Group mis en évidence"><figcaption></figcaption></figure>
7.  Pour nommer votre sous-groupe, cliquez sur le sous-groupe et entrez le nom souhaité dans le champ **Étiquette**.

    <div><figure><img src="../../../.gitbook/assets/TaxCodesMulti_2.png" alt="Éditeur de mise en page avec un élément Sub Group nouvellement ajouté et sélectionné dans la section Tax Details"><figcaption></figcaption></figure> <figure><img src="../../../.gitbook/assets/TaxCodesMulti_3.png" alt="Éditeur de mise en page avec le champ Label du Sub Group sélectionné ouvert pour la désignation"><figcaption></figcaption></figure></div>
8.  Faites glisser et déposez les champs qui correspondent à ce groupe dans le champ **Sub Group**.

    <figure><img src="../../../.gitbook/assets/TaxCodeMulti_4.png" alt="Éditeur de mise en page avec un champ en train d'être déplacé vers le nouveau Sub Group dans la section Tax Details"><figcaption></figcaption></figure>
9. Développez le menu déroulant **Champs**.
10. Recherchez **Tax** et faites glisser et déposer les champs respectifs, tels que **Tax Country** et **Tax Code**, dans le sous-groupe correspondant.

    <figure><img src="../../../.gitbook/assets/TaxCodeMulti_5.png" alt="Éditeur de mise en page avec la liste déroulante Fields déroulée et le champ Tax Country en cours de recherche"><figcaption></figcaption></figure>
11. Répétez les étapes 5 à 10 2 fois pour atteindre l'état suivant:

    <figure><img src="../../../.gitbook/assets/TaxCodeMulti_6.png" alt="Éditeur de mise en page avec le sous-groupe fiscal placé dans la section Tax Details après avoir répété les étapes"><figcaption></figcaption></figure>
12. Enregistrez le modèle.

    <figure><img src="../../../.gitbook/assets/TaxCodeMulti_7.png" alt="Éditeur de mise en page avec le bouton Save mis en évidence après l'agencement des sous-groupes de taxe"><figcaption></figcaption></figure>

### Étape 4 : Vérifiez que tout a fonctionné et les changements résultants

Après avoir téléchargé un nouveau document dans DocBits avec les paramètres de document corrects sélectionnés, vous pourrez sélectionner les codes de taxe que vous avez ajoutés à l'étape 1 et ajouter plusieurs codes de taxe configurés à l'étape 3.

* Le document commencera par trois sections distinctes : une pour les montants au taux normal, une pour les montants au taux réduit et une pour les montants sans taxe.
* Cliquer sur le bouton plus dans une section créera un duplicata, permettant plusieurs soumissions au taux de taxe sélectionné.

<figure><img src="../../../.gitbook/assets/TaxCodeMulti_8.png" alt="Écran de validation d'un document téléversé affichant les sections de taxe avec le bouton plus"><figcaption></figcaption></figure>

* Les sections peuvent être supprimées en cliquant sur le bouton de suppression.

<figure><img src="../../../.gitbook/assets/TaxCodeMulti_9.png" alt="Écran de validation d'un document téléversé avec une section de taxes et le bouton de suppression en surbrillance"><figcaption></figcaption></figure>

* Les montants totaux seront calculés comme une somme de toutes les sections.
* La validation du montant total sera modifiée en fonction de toutes les sections fiscales.
* Les scripts pour les nouvelles sections ne peuvent être appliqués qu'une fois que des champs ont été ajoutés à la vue.

### Remarque pour LN :

Dans **LN**, la position USt sera remplie en fonction du numéro de position du menu déroulant Tax Code/Tax Country. Seul le numéro de position sera envoyé à l'exportation.

<figure><img src="../../../.gitbook/assets/TaxCodesLN_2.png" alt="Écran LN montrant le champ USt Position rempli en fonction du numéro de position du code de taxe"><figcaption></figcaption></figure>

<figure><img src="../../../.gitbook/assets/TaxCodesLN_3.png" alt="Écran LN affichant la facture exportée avec la valeur USt Position renseignée"><figcaption></figcaption></figure>

#### **Mapping d'exportation**

Pour lier la ligne de taxe à la ligne de coût :

1. Ajoutez `TaxLine` à la liste **InvoiceCostFields**.
2. Ajoutez l'entrée suivante, suivant l'exemple ci-dessous :\
   `ICF_TaxLine = TF_position`

<figure><img src="../../../.gitbook/assets/TaxCodeMulti_10.png" alt="List of Values de InvoiceCostFields avec l'entrée TaxLine et le mappage ICF_TaxLine"><figcaption></figcaption></figure>
