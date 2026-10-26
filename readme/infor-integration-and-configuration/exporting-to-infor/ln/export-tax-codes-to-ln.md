# Exporter les codes de taxe vers LN

## **Aperçu :**

\
Ce guide vous accompagnera dans le processus de configuration pour garantir que les codes de taxe sont correctement exportés de DocBits vers LN.

## **Codes de taxe uniques**

### **Étape 1 : Configurer la liste de valeurs**

1.  Allez dans **Paramètres** -> **Traitement des documents** -> **Liste de valeurs**.

    <figure><img src="../../../.gitbook/assets/site-extra-list-of-values-fr.png" alt="Liste de valeurs dans l’interface française actuelle. Les noms des listes propres à l’organisation sont masqués ; aucune liste n’a été créée."><figcaption><p>Liste de valeurs dans l’interface française actuelle. Les noms des listes propres à l’organisation sont masqués ; aucune liste n’a été créée.</p></figcaption></figure>
2.  Cliquez sur **Nouveau**.

    <figure><img src="../../../.gitbook/assets/TaxCodes_2.png" alt="Page Liste de valeurs avec les listes existantes et le bouton Nouveau"><figcaption>Liste de valeurs avec les listes existantes</figcaption></figure>
3.  Créez une liste avec le nom `Tax_Country` et cliquez sur **ENREGISTRER**.

    <figure><img src="../../../.gitbook/assets/TaxCodes_3.png" alt="Boîte de dialogue Nouvelle liste avec le nom Tax_Country" width="563"><figcaption>Créer la liste Tax_Country</figcaption></figure>
4.  Créez les trois listes supplémentaires suivantes :

    * `Tax_Code_Full`
    * `Tax_Code_Reduced`
    * `Tax_Code_Free`

    <div><figure><img src="../../../.gitbook/assets/TaxCodes_28.png" alt="Boîte de dialogue Nouvelle liste avec le nom Tax_Code_Full"><figcaption>Créer la liste Tax_Code_Full</figcaption></figure> <figure><img src="../../../.gitbook/assets/TaxCodes_29.png" alt="Boîte de dialogue Nouvelle liste avec le nom Tax_Code_Reduced"><figcaption>Créer la liste Tax_Code_Reduced</figcaption></figure> <figure><img src="../../../.gitbook/assets/TaxCodes_30.png" alt="Boîte de dialogue Nouvelle liste avec le nom Tax_Code_Free"><figcaption>Créer la liste Tax_Code_Free</figcaption></figure></div>
5.  Cliquez sur l'une des listes nouvellement créées pour l'ouvrir. Ensuite, appuyez sur le bouton **Ajouter une ligne** pour ajouter une nouvelle ligne.

    <figure><img src="../../../.gitbook/assets/TaxCode_4.png" alt="Page Liste de valeurs avec le bouton Ajouter une ligne sous la liste ouverte"><figcaption>Ajouter une ligne à la liste ouverte</figcaption></figure>
6.  Entrez les valeurs respectives souhaitées de **LN** et appuyez sur **ENREGISTRER** pour sauvegarder les modifications.

    * Pour plusieurs codes, ajoutez et enregistrez une ligne par valeur dans la liste concernée.

    <div><figure><img src="../../../.gitbook/assets/TaxCodes_5.png" alt="Boîte de dialogue Créer des valeurs avec un code de taxe LN saisi dans le champ Nom"><figcaption>Saisir le code de taxe LN dans le champ Nom</figcaption></figure> <figure><img src="../../../.gitbook/assets/site-extra-list-value-new-fr.png" alt="Formulaire français de création d’une valeur : valeur, sous-organisation, synonymes et traductions. Aucun code de taxe n’a été saisi ou enregistré ; le choix Anglais concerne la langue d’une traduction, pas celle de l’interface."><figcaption><p>Formulaire français de création d’une valeur : valeur, sous-organisation, synonymes et traductions. Aucun code de taxe n’a été saisi ou enregistré ; le choix Anglais concerne la langue d’une traduction, pas celle de l’interface.</p></figcaption></figure></div>

    * **REMARQUE :** Vous pouvez trouver les codes de taxe dans LN sous : **Common** → **Taxation** → **Master Data** → **Tax Codes** → **Tax Codes by Country**

    <figure><img src="../../../.gitbook/assets/TaxCodes_LN.png" alt="Infor LN, session Codes de taxe par pays pour l'Autriche avec les colonnes Code de taxe et Type de taxe"><figcaption>LN : Common > Taxation > Master Data > Tax Codes > Tax Codes by Country</figcaption></figure>

### **Étape 2 : Ajouter des champs dans DocBits**

1.  Naviguez vers **Paramètres** -> **Paramètres globaux** -> **Types de documents**.

    <figure><img src="../../../.gitbook/assets/site-extra-document-types-fr.png" alt="Types de documents dans l’interface française actuelle. Choisissez Champs dans la carte du type concerné ; aucun interrupteur n’a été modifié."><figcaption><p>Types de documents dans l’interface française actuelle. Choisissez Champs dans la carte du type concerné ; aucun interrupteur n’a été modifié.</p></figcaption></figure>
2.  Choisissez le menu **Champs** correspondant au type de document où vous souhaitez ajouter les champs.

    <figure><img src="../../../.gitbook/assets/TaxCodes_7.png" alt="Page Types de documents avec le menu Champs sous chaque type de document"><figcaption>Ouvrir le menu Champs du type de document</figcaption></figure>
3.  Sous **TVA et montants**, créez six nouveaux champs comme suit:

    <figure><img src="../../../.gitbook/assets/TaxCodes_8.png" alt="Onglet Champs avec le groupe TVA et montants et le bouton Créer nouveau"><figcaption>Onglet Champs : groupe TVA et montants</figcaption></figure>

<table data-header-hidden><thead><tr><th width="306"></th><th width="139"></th><th width="119"></th><th></th></tr></thead><tbody><tr><td><strong>Nom</strong></td><td><strong>Titre</strong></td><td><strong>Type de champ</strong></td><td><strong>Liste de valeurs</strong></td></tr><tr><td><code>tax_country</code></td><td>Pays de taxation</td><td>Dropdown</td><td>Tax_Country</td></tr><tr><td><code>tax_country_2</code></td><td>Pays de taxe réduit</td><td>Dropdown</td><td>Tax_Country</td></tr><tr><td><code>tax_country_3</code></td><td>Pays sans taxe</td><td>Dropdown</td><td>Tax_Country</td></tr><tr><td><code>tax_code_without_country</code></td><td>Code de taxe</td><td>Dropdown</td><td>Tax_Code_Full</td></tr><tr><td><code>tax_code_without_country_2</code></td><td>Code de taxe — taux réduit</td><td>Dropdown</td><td>Tax_Code_Reduced</td></tr><tr><td><code>tax_code_without_country_3</code></td><td>Code de taxe — sans taxe</td><td>Dropdown</td><td>Tax_Code_Free</td></tr></tbody></table>

<div><figure><img src="../../../.gitbook/assets/TaxCodes_10.png" alt="Boîte de dialogue Détails du champ du document pour tax_country avec le type Dropdown et la liste Tax_Country"><figcaption>Champ tax_country : Dropdown, liste Tax_Country</figcaption></figure> <figure><img src="../../../.gitbook/assets/TaxCodes_11.png" alt="Boîte de dialogue Détails du champ du document pour tax_country_2 avec le titre Tax Country Reduced"><figcaption>Champ tax_country_2 : Dropdown, liste Tax_Country</figcaption></figure> <figure><img src="../../../.gitbook/assets/TaxCodes_12.png" alt="Boîte de dialogue Détails du champ du document pour tax_country_3 avec le titre Tax Country Free"><figcaption>Champ tax_country_3 : Dropdown, liste Tax_Country</figcaption></figure></div>

<div><figure><img src="../../../.gitbook/assets/TaxCodes_13.png" alt="Boîte de dialogue Détails du champ du document pour tax_code_without_country avec la liste Tax_Code_Full"><figcaption>Champ tax_code_without_country : Dropdown, liste Tax_Code_Full</figcaption></figure> <figure><img src="../../../.gitbook/assets/TaxCodes_14.png" alt="Boîte de dialogue Détails du champ du document pour tax_code_without_country_2 avec la liste Tax_Code_Reduced"><figcaption>Champ tax_code_without_country_2 : Dropdown, liste Tax_Code_Reduced</figcaption></figure> <figure><img src="../../../.gitbook/assets/TaxCodes_15.png" alt="Boîte de dialogue Détails du champ du document pour tax_code_without_country_3 avec la liste Tax_Code_Free"><figcaption>Champ tax_code_without_country_3 : Dropdown, liste Tax_Code_Free</figcaption></figure></div>

4.  Après avoir enregistré chaque champ, cliquez sur **Enregistrer les paramètres** pour appliquer les modifications.

    <figure><img src="../../../.gitbook/assets/TaxCodes_20.png" alt="Onglet Champs avec le bouton Enregistrer les paramètres au-dessus de la liste des champs"><figcaption>Enregistrer les paramètres pour appliquer les nouveaux champs</figcaption></figure>

### **Étape 3 : Modifier la mise en page**

1.  Allez dans **Paramètres** -> **Paramètres globaux** -> **Types de documents**.

    <figure><img src="../../../.gitbook/assets/site-extra-document-types-fr.png" alt="Types de documents dans l’interface française actuelle. Choisissez Champs dans la carte du type concerné ; aucun interrupteur n’a été modifié."><figcaption><p>Types de documents dans l’interface française actuelle. Choisissez Champs dans la carte du type concerné ; aucun interrupteur n’a été modifié.</p></figcaption></figure>
2.  Ouvrez le menu **Modifier la mise en page** pour le type de document que vous souhaitez modifier.

    <figure><img src="../../../.gitbook/assets/TaxCodes_19.png" alt="Page Types de documents avec le lien Modifier la mise en page sous chaque type de document"><figcaption>Ouvrir Modifier la mise en page du type de document</figcaption></figure>
3.  Sélectionnez l'**Origine du document** appropriée pour laquelle vous souhaitez appliquer les codes de taxe

    <figure><img src="../../../.gitbook/assets/TaxCodes_26.png" alt="Layout Builder avec le sélecteur d'origine du document et la barre d'outils du modèle"><figcaption>Layout Builder : sélectionner l'origine du document</figcaption></figure>
4.  Faites défiler jusqu'à la section **Tax Details**.

    <figure><img src="../../../.gitbook/assets/TaxCodes_21.png" alt="Layout Builder avec le groupe Détails de taxe et ses champs dans l'arborescence des éléments"><figcaption>Faire défiler jusqu'au groupe Détails de taxe</figcaption></figure>
5. Développez le menu déroulant **Éléments du formulaire**.
6.  Dans la section **Tax Details**, utilisez l'outil **Horizontal Separator**. Faites-le glisser et déposez-le entre les sous-sections dans la section fiscale pour les séparer clairement et réduire la confusion.

    <figure><img src="../../../.gitbook/assets/TaxCodes_22.png" alt="Layout Builder avec la liste Éléments de formulaire déroulée"><figcaption>Dérouler Éléments de formulaire</figcaption></figure>
7. Développez le menu déroulant **Champs**.
8.  Recherchez **Tax Country** et faites glisser le champ dans son domaine respectif.

    <figure><img src="../../../.gitbook/assets/TaxCodes_23.png" alt="Layout Builder avec le champ Tax Country déposé dans la zone Détails de taxe"><figcaption>Glisser Tax Country dans la zone Détails de taxe</figcaption></figure>
9.  Recherchez **Tax Code** et faites glisser le champ dans son domaine correspondant.

    <figure><img src="../../../.gitbook/assets/TaxCodes_24.png" alt="Layout Builder avec le champ Tax Code placé sous Tax Country"><figcaption>Glisser Tax Code dans la zone Détails de taxe</figcaption></figure>
10. Enregistrez le modèle.

    <figure><img src="../../../.gitbook/assets/TaxCodes_25.png" alt="Layout Builder avec le modèle enregistré et les deux champs de taxe dans le groupe Détails de taxe"><figcaption>Modèle enregistré avec les deux champs de taxe</figcaption></figure>

### Étape 4 : Vérifiez que tout a fonctionné

Après avoir téléchargé un nouveau document dans DocBits avec les paramètres de document corrects sélectionnés, vous devriez maintenant être en mesure de sélectionner les codes de taxe que vous avez ajoutés aux listes à l'étape 1.

<figure><img src="../../../.gitbook/assets/TaxCodes_31.png" alt="Vue de validation des champs d'une facture avec les listes Tax Country et Tax Code remplies"><figcaption>Les nouvelles listes dans la vue de validation</figcaption></figure>

## Code de taxe multiple

### **Étape 1 : Configurer la liste de valeurs**

1.  Allez dans **Paramètres** -> **Traitement des documents** -> **Liste de valeurs**.

    <figure><img src="../../../.gitbook/assets/site-extra-list-of-values-fr.png" alt="Liste de valeurs dans l’interface française actuelle. Les noms des listes propres à l’organisation sont masqués ; aucune liste n’a été créée."><figcaption><p>Liste de valeurs dans l’interface française actuelle. Les noms des listes propres à l’organisation sont masqués ; aucune liste n’a été créée.</p></figcaption></figure>
2.  Cliquez sur **Nouveau**.

    <figure><img src="../../../.gitbook/assets/TaxCodes_2.png" alt="Page Liste de valeurs avec les listes existantes et le bouton Nouveau"><figcaption>Liste de valeurs avec les listes existantes</figcaption></figure>
3.  Créez une liste avec le nom `Tax_Country` et cliquez sur **ENREGISTRER**.

    <figure><img src="../../../.gitbook/assets/TaxCodes_3.png" alt="Boîte de dialogue Nouvelle liste avec le nom Tax_Country" width="563"><figcaption>Créer la liste Tax_Country</figcaption></figure>
4.  Créez les trois listes supplémentaires suivantes :

    * `Tax_Code_Full`
    * `Tax_Code_Reduced`
    * `Tax_Code_Free`

    <div><figure><img src="../../../.gitbook/assets/TaxCodes_28.png" alt="Boîte de dialogue Nouvelle liste avec le nom Tax_Code_Full"><figcaption>Créer la liste Tax_Code_Full</figcaption></figure> <figure><img src="../../../.gitbook/assets/TaxCodes_29.png" alt="Boîte de dialogue Nouvelle liste avec le nom Tax_Code_Reduced"><figcaption>Créer la liste Tax_Code_Reduced</figcaption></figure> <figure><img src="../../../.gitbook/assets/TaxCodes_30.png" alt="Boîte de dialogue Nouvelle liste avec le nom Tax_Code_Free"><figcaption>Créer la liste Tax_Code_Free</figcaption></figure></div>
5.  Cliquez sur l'une des listes nouvellement créées pour l'ouvrir. Ensuite, appuyez sur le bouton **Ajouter une ligne** pour ajouter une nouvelle ligne.

    <figure><img src="../../../.gitbook/assets/TaxCode_4.png" alt="Page Liste de valeurs avec le bouton Ajouter une ligne sous la liste ouverte"><figcaption>Ajouter une ligne à la liste ouverte</figcaption></figure>
6.  Entrez les valeurs respectives souhaitées de **LN** et appuyez sur **ENREGISTRER** pour sauvegarder les modifications.

    * Pour plusieurs codes, ajoutez et enregistrez une ligne par valeur dans la liste concernée.

    <div><figure><img src="../../../.gitbook/assets/TaxCodes_5.png" alt="Boîte de dialogue Créer des valeurs avec un code de taxe LN saisi dans le champ Nom"><figcaption>Saisir le code de taxe LN dans le champ Nom</figcaption></figure> <figure><img src="../../../.gitbook/assets/site-extra-list-value-new-fr.png" alt="Formulaire français de création d’une valeur : valeur, sous-organisation, synonymes et traductions. Aucun code de taxe n’a été saisi ou enregistré ; le choix Anglais concerne la langue d’une traduction, pas celle de l’interface."><figcaption><p>Formulaire français de création d’une valeur : valeur, sous-organisation, synonymes et traductions. Aucun code de taxe n’a été saisi ou enregistré ; le choix Anglais concerne la langue d’une traduction, pas celle de l’interface.</p></figcaption></figure></div>

    * **REMARQUE :** Vous pouvez trouver les codes de taxe dans LN sous : **Common** → **Taxation** → **Master Data** → **Tax Codes** → **Tax Codes by Country**

    <figure><img src="../../../.gitbook/assets/TaxCodes_LN.png" alt="Infor LN, session Codes de taxe par pays pour l'Autriche avec les colonnes Code de taxe et Type de taxe"><figcaption>LN : Common > Taxation > Master Data > Tax Codes > Tax Codes by Country</figcaption></figure>

### **Étape 2 : Ajouter des champs dans DocBits**

1.  Naviguez vers **Paramètres** -> **Paramètres globaux** -> **Types de documents**.

    <figure><img src="../../../.gitbook/assets/site-extra-document-types-fr.png" alt="Types de documents dans l’interface française actuelle. Choisissez Champs dans la carte du type concerné ; aucun interrupteur n’a été modifié."><figcaption><p>Types de documents dans l’interface française actuelle. Choisissez Champs dans la carte du type concerné ; aucun interrupteur n’a été modifié.</p></figcaption></figure>
2.  Choisissez le menu **Champs** correspondant au type de document où vous souhaitez ajouter les champs.

    <figure><img src="../../../.gitbook/assets/TaxCodes_7.png" alt="Page Types de documents avec le menu Champs sous chaque type de document"><figcaption>Ouvrir le menu Champs du type de document</figcaption></figure>
3.  Sous **TVA et montants**, créez six nouveaux champs comme suit:

    <figure><img src="../../../.gitbook/assets/TaxCodes_8.png" alt="Onglet Champs avec le groupe TVA et montants et le bouton Créer nouveau"><figcaption>Onglet Champs : groupe TVA et montants</figcaption></figure>

<table data-header-hidden><thead><tr><th width="306"></th><th width="139"></th><th width="119"></th><th></th></tr></thead><tbody><tr><td><strong>Nom</strong></td><td><strong>Titre</strong></td><td><strong>Type de champ</strong></td><td><strong>Liste de valeurs</strong></td></tr><tr><td><code>tax_country</code></td><td>Pays de taxation</td><td>Dropdown</td><td>Tax_Country</td></tr><tr><td><code>tax_country_2</code></td><td>Pays de taxe réduit</td><td>Dropdown</td><td>Tax_Country</td></tr><tr><td><code>tax_country_3</code></td><td>Pays sans taxe</td><td>Dropdown</td><td>Tax_Country</td></tr><tr><td><code>tax_code_without_country</code></td><td>Code de taxe</td><td>Dropdown</td><td>Tax_Code_Full</td></tr><tr><td><code>tax_code_without_country_2</code></td><td>Code de taxe — taux réduit</td><td>Dropdown</td><td>Tax_Code_Reduced</td></tr><tr><td><code>tax_code_without_country_3</code></td><td>Code de taxe — sans taxe</td><td>Dropdown</td><td>Tax_Code_Free</td></tr></tbody></table>

<div><figure><img src="../../../.gitbook/assets/TaxCodes_10.png" alt="Boîte de dialogue Détails du champ du document pour tax_country avec le type Dropdown et la liste Tax_Country"><figcaption>Champ tax_country : Dropdown, liste Tax_Country</figcaption></figure> <figure><img src="../../../.gitbook/assets/TaxCodes_11.png" alt="Boîte de dialogue Détails du champ du document pour tax_country_2 avec le titre Tax Country Reduced"><figcaption>Champ tax_country_2 : Dropdown, liste Tax_Country</figcaption></figure> <figure><img src="../../../.gitbook/assets/TaxCodes_12.png" alt="Boîte de dialogue Détails du champ du document pour tax_country_3 avec le titre Tax Country Free"><figcaption>Champ tax_country_3 : Dropdown, liste Tax_Country</figcaption></figure></div>

<div><figure><img src="../../../.gitbook/assets/TaxCodes_13.png" alt="Boîte de dialogue Détails du champ du document pour tax_code_without_country avec la liste Tax_Code_Full"><figcaption>Champ tax_code_without_country : Dropdown, liste Tax_Code_Full</figcaption></figure> <figure><img src="../../../.gitbook/assets/TaxCodes_14.png" alt="Boîte de dialogue Détails du champ du document pour tax_code_without_country_2 avec la liste Tax_Code_Reduced"><figcaption>Champ tax_code_without_country_2 : Dropdown, liste Tax_Code_Reduced</figcaption></figure> <figure><img src="../../../.gitbook/assets/TaxCodes_15.png" alt="Boîte de dialogue Détails du champ du document pour tax_code_without_country_3 avec la liste Tax_Code_Free"><figcaption>Champ tax_code_without_country_3 : Dropdown, liste Tax_Code_Free</figcaption></figure></div>

4.  Après avoir enregistré chaque champ, cliquez sur **Enregistrer les paramètres** pour appliquer les modifications.

    <figure><img src="../../../.gitbook/assets/TaxCodes_20.png" alt="Onglet Champs avec le bouton Enregistrer les paramètres au-dessus de la liste des champs"><figcaption>Enregistrer les paramètres pour appliquer les nouveaux champs</figcaption></figure>

### **Étape 3 : Modifier la mise en page**

1.  Allez dans **Paramètres** -> **Paramètres globaux** -> **Types de documents**.

    <figure><img src="../../../.gitbook/assets/site-extra-document-types-fr.png" alt="Types de documents dans l’interface française actuelle. Choisissez Champs dans la carte du type concerné ; aucun interrupteur n’a été modifié."><figcaption><p>Types de documents dans l’interface française actuelle. Choisissez Champs dans la carte du type concerné ; aucun interrupteur n’a été modifié.</p></figcaption></figure>
2.  Ouvrez le menu **Modifier la mise en page** pour le type de document que vous souhaitez modifier.

    <figure><img src="../../../.gitbook/assets/TaxCodes_19.png" alt="Page Types de documents avec le lien Modifier la mise en page sous chaque type de document"><figcaption>Ouvrir Modifier la mise en page du type de document</figcaption></figure>
3.  Sélectionnez l'**Origine du document** appropriée pour laquelle vous souhaitez appliquer les codes de taxe

    <figure><img src="../../../.gitbook/assets/TaxCodes_26.png" alt="Layout Builder avec le sélecteur d'origine du document et la barre d'outils du modèle"><figcaption>Layout Builder : sélectionner l'origine du document</figcaption></figure>
4.  Faites défiler jusqu'à la section **Tax Details**.

    <figure><img src="../../../.gitbook/assets/TaxCodes_21.png" alt="Layout Builder avec le groupe Détails de taxe et ses champs dans l'arborescence des éléments"><figcaption>Faire défiler jusqu'au groupe Détails de taxe</figcaption></figure>
5. Développez le menu déroulant **Éléments du formulaire**.
6.  Dans la section Tax Details, utilisez l'outil **Sub Group**. Faites-le glisser et déposez-le à côté d'un champ existant.

    <figure><img src="../../../.gitbook/assets/TaxCodesMulti_1.png" alt="Layout Builder avec l'outil Sous-groupe dans la liste Éléments de formulaire"><figcaption>Sélectionner l'outil Sous-groupe</figcaption></figure>
7.  Pour nommer votre sous-groupe, cliquez sur le sous-groupe et entrez le nom souhaité dans le champ **Étiquette**.

    <div><figure><img src="../../../.gitbook/assets/TaxCodesMulti_2.png" alt="Layout Builder avec un nouveau sous-groupe vide à côté d'un champ existant"><figcaption>Déposer le sous-groupe à côté d'un champ</figcaption></figure> <figure><img src="../../../.gitbook/assets/TaxCodesMulti_3.png" alt="Panneau des propriétés avec le champ Libellé du nouveau sous-groupe"><figcaption>Nommer le sous-groupe dans le champ Libellé</figcaption></figure></div>
8.  Faites glisser et déposez les champs qui correspondent à ce groupe dans le champ **Sub Group**.

    <figure><img src="../../../.gitbook/assets/TaxCodeMulti_4.png" alt="Layout Builder avec les champs de taxe déplacés dans le nouveau sous-groupe"><figcaption>Déplacer les champs de taxe dans le sous-groupe</figcaption></figure>
9. Développez le menu déroulant **Champs**.
10. Recherchez **Tax** et faites glisser et déposer les champs respectifs, tels que **Tax Country** et **Tax Code**, dans le sous-groupe correspondant.

    <figure><img src="../../../.gitbook/assets/TaxCodeMulti_5.png" alt="Layout Builder avec Tax Country et Tax Code dans le sous-groupe"><figcaption>Tax Country et Tax Code dans le sous-groupe</figcaption></figure>
11. Répétez les étapes 5 à 10 2 fois pour atteindre l'état suivant:

    <figure><img src="../../../.gitbook/assets/TaxCodeMulti_6.png" alt="Layout Builder avec trois sous-groupes de taxe pour le taux normal, réduit et exonéré"><figcaption>Trois sous-groupes : normal, réduit et exonéré</figcaption></figure>
12. Enregistrez le modèle.

    <figure><img src="../../../.gitbook/assets/TaxCodeMulti_7.png" alt="Layout Builder avec le modèle multi-codes de taxe enregistré"><figcaption>Enregistrer le modèle multi-codes de taxe</figcaption></figure>

### Étape 4 : Vérifiez que tout a fonctionné et les changements résultants

Après avoir téléchargé un nouveau document dans DocBits avec les paramètres de document corrects sélectionnés, vous pourrez sélectionner les codes de taxe que vous avez ajoutés à l'étape 1 et ajouter plusieurs codes de taxe configurés à l'étape 3.

* Le document commencera par trois sections distinctes : une pour les montants au taux normal, une pour les montants au taux réduit et une pour les montants sans taxe.
* Cliquer sur le bouton plus dans une section créera un duplicata, permettant plusieurs soumissions au taux de taxe sélectionné.

<figure><img src="../../../.gitbook/assets/TaxCodeMulti_8.png" alt="Vue de validation avec trois sections de taxe distinctes et les boutons ajouter et supprimer"><figcaption>Trois sections de taxe dans la vue de validation</figcaption></figure>

* Les sections peuvent être supprimées en cliquant sur le bouton de suppression.

<figure><img src="../../../.gitbook/assets/TaxCodeMulti_9.png" alt="Vue de validation avec une section de taxe dupliquée par le bouton plus"><figcaption>Ajouter une section avec le bouton plus</figcaption></figure>

* Les montants totaux seront calculés comme une somme de toutes les sections.
* La validation du montant total sera modifiée en fonction de toutes les sections fiscales.
* Les scripts pour les nouvelles sections ne peuvent être appliqués qu'une fois que des champs ont été ajoutés à la vue.

### Remarque pour LN :

Dans **LN**, la position USt sera remplie en fonction du numéro de position du menu déroulant Tax Code/Tax Country. Seul le numéro de position sera envoyé à l'exportation.

<figure><img src="../../../.gitbook/assets/TaxCodesLN_2.png" alt="Infor LN, session Lignes de taxe par facture externe avec la colonne de position de taxe"><figcaption>LN : Tax Lines by External Invoice</figcaption></figure>

<figure><img src="../../../.gitbook/assets/TaxCodesLN_3.png" alt="Infor LN, session Lignes de taxe par facture externe avec le numéro de position"><figcaption>LN : le numéro de position est exporté comme USt Position</figcaption></figure>

#### **Mapping d'exportation**

Pour lier la ligne de taxe à la ligne de coût :

1. Ajoutez `TaxLine` à la liste **InvoiceCostFields**.
2. Ajoutez l'entrée suivante, suivant l'exemple ci-dessous :\
   `ICF_TaxLine = TF_position`

<figure><img src="../../../.gitbook/assets/TaxCodeMulti_10.png" alt="Fichier de mappage d'export avec l'entrée ICF_TaxLine à côté des champs de coût de facture"><figcaption>Mappage d'export : ICF_TaxLine = TF_position</figcaption></figure>
