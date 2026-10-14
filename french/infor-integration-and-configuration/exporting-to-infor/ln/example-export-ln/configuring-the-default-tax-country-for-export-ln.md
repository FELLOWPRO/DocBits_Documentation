# Configuration du pays fiscal par défaut pour l'exportation LN

### Aperçu

Le pays fiscal (Tax Country) par défaut pour l'exportation est défini sur **DE (Allemagne)** afin d'éviter les erreurs d'exportation. Vous pouvez le modifier dans le fichier de mappage de l'une des deux façons suivantes :

* Définir une autre valeur statique.
* Le mapper dynamiquement vers un champ de DocBits.

<mark style="color:red;">**Remarque :**</mark> si le champ indiqué n'existe pas ou est vide, l'exportation revient par défaut à **DE**.

### Étapes pour modifier le pays fiscal

#### 1. Obtenir le fichier de mappage

* Accédez à **DocBits → Settings → Document Processing → Export**.
* Ouvrez la configuration d'exportation que vous souhaitez modifier.
*   Cliquez sur **Download** pour obtenir le fichier de mappage.\\

    <figure><img src="../../../../.gitbook/assets/iScreen Shoter - Google Chrome - 250220120028.jpg" alt=""><figcaption></figcaption></figure>
* Ouvrez le fichier dans un éditeur de texte.

#### 2. Modifier le fichier de mappage

Choisissez l'une des deux options ci-dessous et appliquez les modifications nécessaires.

**Option 1 : valeur statique**

Pour définir une valeur statique de pays fiscal, procédez comme suit :

1.  Définissez un nouveau champ statique en ajoutant `,TaxCountry` à la ligne `StaticFields`.

    ```properties
    StaticFields=FinancialCompany...,TaxCountry
    ```
2.  Définissez le code pays en ajoutant la ligne suivante :

    ```properties
    SF_TaxCountry=CountryCode
    ```

    Remplacez `CountryCode` par le code pays réel, par ex. `ES` pour l'Espagne ou `DE` pour l'Allemagne :

    ```properties
    SF_TaxCountry=ES
    ```

**Exemple :**

```properties
StaticFields=FinancialCompany,TaxCountry
SF_TaxCountry=FR
```

<figure><img src="../../../../.gitbook/assets/image (415).png" alt=""><figcaption></figcaption></figure>

**Option 2 : mappage dynamique depuis un champ DocBits**

Pour mapper dynamiquement le pays fiscal depuis un champ de DocBits :

1.  Ajoutez `,TaxCountry` à la ligne `HeaderFields` :

    ```properties
    HeaderFields=SupplierCode,...,TaxCountry
    ```
2.  Définissez le mappage de champ correspondant :

    ```properties
    HF_TaxCountry=DocBits_Field_name
    ```

    Remplacez `DocBits_Field_Name` par le nom réel du champ dans DocBits :

    ```properties
    HF_TaxCountry=tax_country_1
    ```

**Exemple :**

```properties
HeaderFields=SupplierCode,TaxCountry
HF_TaxCountry=tax_country_1
```

<figure><img src="../../../../.gitbook/assets/image (411).png" alt=""><figcaption></figcaption></figure>

### Résumé

* Si le pays fiscal **n'est pas défini ou si le champ est vide**, il prend la valeur **DE** par défaut.
* **Utilisez une valeur statique** si le pays fiscal reste identique pour toutes les exportations.
* **Utilisez un mappage dynamique de champ** si le pays fiscal varie selon le document.

En suivant ces étapes, vous pouvez modifier avec succès le mappage du pays fiscal pour l'adapter à vos besoins.
