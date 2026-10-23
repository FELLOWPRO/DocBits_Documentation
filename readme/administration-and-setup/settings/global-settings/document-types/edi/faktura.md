# Faktura

## Afficher l'attribut sur chaque poste

Si vous souhaitez afficher un attribut spécifique (comme le numéro de bon de commande) sur chaque poste, suivez les étapes ci-dessous. L'approche différera selon que vous avez besoin de l'attribut dans l'extraction JSON ou dans la sortie XSL.

<figure><img src="../../../../../.gitbook/assets/Screenshot 2025-01-28 at 14.33.16.png" alt="Table de facture avec les colonnes Position, Description, Quantity et Unit Price listant les lignes du bon de commande avec totaux"><figcaption></figcaption></figure>

### Méthode 1 : Afficher l'attribut dans l'extraction JSON (configuration DocBits)

1. Allez dans **Paramètres**
2. Allez dans **Types de documents**
3. Sélectionnez **Invoice/E-Doc**

<figure><img src="../../../../../.gitbook/assets/Screenshot 2025-01-28 at 15.07.58.png" alt="Page de paramètres du type de document Invoice avec les onglets Extraction type, Edit layout, Document Sub Types, Table columns, Fields et Model Training"><figcaption></figcaption></figure>

4. Ouvrez l'onglet **"FATTURAPA"**
5. Cliquez sur **JSON**

<figure><img src="../../../../../.gitbook/assets/Screenshot 2025-01-28 at 15.01.13.png" alt="Liste des formats FATTURAPA avec les entrées Preview, Extraction Paths, variantes FacturX ZUGFERD, Peppol et XRECHNUNG avec XSLT"><figcaption></figcaption></figure>

6. Pour créer un brouillon, cliquez sur l'icône du **crayon**

<figure><img src="../../../../../.gitbook/assets/Screenshot 2025-01-28 at 14.58.56.png" alt="Paramètres du type de document Invoice avec l'entrée du type de document électronique FATTURAPA et un horodatage"><figcaption></figcaption></figure>

7. À l'intérieur du tableau `"tables"`, ajoutez la colonne spécifique que vous souhaitez afficher en fournissant un nom et un chemin :

```
{ 
"name": "PURCHASE_ORDER",    
"path":"path_to_source" 
}
```

**REMARQUE :** Les documents électroniques auront toujours l'origine définie sur **Grande-Bretagne**, donc les montants seront enregistrés au format international, en utilisant un **point (.)** comme séparateur décimal.

8. Enregistrez le brouillon

<figure><img src="../../../../../.gitbook/assets/Screenshot 2025-01-28 at 15.11.04.png" alt="Entrée de version Draft avec l'horodatage 28.01.2025 15:10:12 dans la vue de test de DocBits"><figcaption></figcaption></figure>

9. Assurez-vous que votre brouillon est celui qui est **actif**.

<figure><img src="../../../../../.gitbook/assets/Screenshot 2025-01-28 at 16.03.50.png" alt="Entrée de la liste des versions Draft montrant la version 91.20 avec un horodatage confirmant le brouillon actif"><figcaption></figcaption></figure>

### Méthode 2 : Afficher l'attribut dans la sortie XSL (aperçu HTML/PDF)

1. Allez dans **Paramètres**
2. Allez dans **Types de documents**
3. Sélectionnez **Invoice/E-Doc**

<figure><img src="../../../../../.gitbook/assets/Screenshot 2025-01-28 at 15.07.58.png" alt="Page de paramètres du type de document Invoice avec les onglets Extraction type, Edit layout, Document Sub Types, Table columns, Fields et Model Training"><figcaption></figcaption></figure>

4. Ouvrez l'onglet **"FATTURAPA"**
5. **Cliquez sur XLST**

<figure><img src="../../../../../.gitbook/assets/Screenshot 2025-01-28 at 15.23.06.png" alt="Onglet FATTURAPA listant les formats de documents électroniques, notamment EDI, variantes FacturX ZUGFERD, Peppol et versions XRECHNUNG"><figcaption></figcaption></figure>

6. Pour créer un brouillon, cliquez sur l'icône du **crayon**

<figure><img src="../../../../../.gitbook/assets/Screenshot 2025-01-28 at 14.58.56.png" alt="Paramètres du type de document Invoice avec l'entrée du type de document électronique FATTURAPA et un horodatage"><figcaption></figcaption></figure>

7. Dans le bloc `<xsl:for-each select="path">` qui génère les lignes du tableau, ajoutez un extrait comme celui-ci là où vous souhaitez que l'attribut apparaisse (par exemple, dans sa propre colonne) :

```
<tr>
    <!-- Other columns ... -->

    <td>
        <!-- PO number -->
        <xsl:variable name="variable_name" select="value" />
        <xsl:value-of 
            select="path_to_attribute" 
        />
    </td>
</tr>
```

**REMARQUE :** Les documents électroniques auront toujours l'origine définie sur **Grande-Bretagne**, donc les montants seront enregistrés au format international, en utilisant un **point (.)** comme séparateur décimal.

8. Enregistrez le brouillon

<figure><img src="../../../../../.gitbook/assets/Screenshot 2025-01-28 at 15.11.04.png" alt="Entrée de version Draft avec l'horodatage 28.01.2025 15:10:12 dans la vue de test de DocBits"><figcaption></figcaption></figure>

9. Assurez-vous que votre brouillon est celui qui est **actif**.

<figure><img src="../../../../../.gitbook/assets/Screenshot 2025-01-28 at 16.03.50.png" alt="Entrée de la liste des versions Draft montrant la version 91.20 avec un horodatage confirmant le brouillon actif"><figcaption></figcaption></figure>
