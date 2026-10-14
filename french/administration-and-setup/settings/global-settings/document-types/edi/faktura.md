# Faktura

## Afficher l'attribut sur chaque poste

Si vous souhaitez afficher un attribut spécifique (comme le numéro de bon de commande) sur chaque poste, suivez les étapes ci-dessous. L'approche différera selon que vous avez besoin de l'attribut dans l'extraction JSON ou dans la sortie XSL.

<figure><img src="../../../../../.gitbook/assets/Screenshot 2025-01-28 at 14.33.16.png" alt=""><figcaption></figcaption></figure>

### Méthode 1 : Afficher l'attribut dans l'extraction JSON (configuration DocBits)

1. Allez dans **Paramètres**
2. Allez dans **Types de documents**
3. Sélectionnez **Invoice/E-Doc**

<figure><img src="../../../../../.gitbook/assets/Screenshot 2025-01-28 at 15.07.58.png" alt=""><figcaption></figcaption></figure>

4. Ouvrez l'onglet **"FATTURAPA"**
5. Cliquez sur **JSON**

<figure><img src="../../../../../.gitbook/assets/Screenshot 2025-01-28 at 15.01.13.png" alt=""><figcaption></figcaption></figure>

6. Pour créer un brouillon, cliquez sur l'icône du **crayon**

<figure><img src="../../../../../.gitbook/assets/Screenshot 2025-01-28 at 14.58.56.png" alt=""><figcaption></figcaption></figure>

7. À l'intérieur du tableau `"tables"`, ajoutez la colonne spécifique que vous souhaitez afficher en fournissant un nom et un chemin :

```
{ 
"name": "PURCHASE_ORDER",    
"path":"path_to_source" 
}
```

**REMARQUE :** Les documents électroniques auront toujours l'origine définie sur **Grande-Bretagne**, donc les montants seront enregistrés au format international, en utilisant un **point (.)** comme séparateur décimal.

8. Enregistrez le brouillon

<figure><img src="../../../../../.gitbook/assets/Screenshot 2025-01-28 at 15.11.04.png" alt=""><figcaption></figcaption></figure>

9. Assurez-vous que votre brouillon est celui qui est **actif**.

<figure><img src="../../../../../.gitbook/assets/Screenshot 2025-01-28 at 16.03.50.png" alt=""><figcaption></figcaption></figure>

### Méthode 2 : Afficher l'attribut dans la sortie XSL (aperçu HTML/PDF)

1. Allez dans **Paramètres**
2. Allez dans **Types de documents**
3. Sélectionnez **Invoice/E-Doc**

<figure><img src="../../../../../.gitbook/assets/Screenshot 2025-01-28 at 15.07.58.png" alt=""><figcaption></figcaption></figure>

4. Ouvrez l'onglet **"FATTURAPA"**
5. **Cliquez sur XLST**

<figure><img src="../../../../../.gitbook/assets/Screenshot 2025-01-28 at 15.23.06.png" alt=""><figcaption></figcaption></figure>

6. Pour créer un brouillon, cliquez sur l'icône du **crayon**

<figure><img src="../../../../../.gitbook/assets/Screenshot 2025-01-28 at 14.58.56.png" alt=""><figcaption></figcaption></figure>

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

<figure><img src="../../../../../.gitbook/assets/Screenshot 2025-01-28 at 15.11.04.png" alt=""><figcaption></figcaption></figure>

9. Assurez-vous que votre brouillon est celui qui est **actif**.

<figure><img src="../../../../../.gitbook/assets/Screenshot 2025-01-28 at 16.03.50.png" alt=""><figcaption></figcaption></figure>
