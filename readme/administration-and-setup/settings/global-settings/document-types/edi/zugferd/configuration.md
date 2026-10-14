# Configuration ZUGFeRD

{% embed url="https://youtu.be/AxrHNEmmXtg" %}
Tutoriel DocBits E-Invoice : traiter XRechnung / ZUGFeRD (Factur-X), valider les données et automatiser les workflows
{% endembed %}

## **Versions prises en charge de ZUGFeRD**

DocBits prend en charge toutes les versions majeures de ZUGFeRD, notamment :

* **1.0**
* **2.0**
* **2.1** (conforme à FACTUR-X 1.0.05)
* **2.2**
* **2.3** (conforme à FACTUR-X 1.07.2)
* **2.3.2**

#### Activation et modification du standard

Le standard ZUGFeRD est toujours actif par défaut, mais vous pouvez le modifier si nécessaire.

### **Étapes pour modifier les paramètres ZUGFeRD :**

1. Accédez à **Settings → Global Settings → Document Types → Invoice**.
2. Cliquez sur **E-Doc**.\\
3. Une liste de tous les e-docs disponibles apparaît.
4. Repérez la version de **ZUGFeRD** que vous souhaitez modifier.\\

## **Configuration de la transformation et du chemin XML :**

Dans les **paramètres de transformation**, vous pouvez définir le chemin permettant de localiser des informations spécifiques dans le fichier XML et de les enregistrer dans une nouvelle structure, ce qui facilite l'accès aux données.\
<mark style="color:red;">**Remarque**</mark> : si vous utilisez cette fonctionnalité, vous devez utiliser les nouveaux chemins XML créés, et non les chemins XML d'origine, dans **Preview** et **Extraction Path**.

### **Étapes pour modifier le fichier de transformation :**

1. Ouvrez **Transformation**.
2. Créez un nouveau brouillon en cliquant sur l'**icône de crayon**.
3. Sélectionnez le brouillon que vous venez de créer.
4. Créez un nouveau champ ou modifiez un champ existant.
5. Définissez le chemin souhaité pour l'extraction des données.
6. Cliquez sur **Save**.

### Remarques importantes :

* Le **fichier d'aperçu** est utilisé uniquement pour **FACTUR-X** et non pour **ZUGFeRD**. ZUGFeRD utilisera le **PDF** d'origine.

## Configuration du PDF d'aperçu

La **configuration du PDF d'aperçu** sert à générer une version lisible du document. Vous pouvez la personnaliser avec du HTML selon vos besoins.

### **Étapes pour modifier le fichier d'aperçu :**

1. Ouvrez **Preview**.
2. Créez un nouveau brouillon en cliquant sur l'**icône de crayon**.
3. Sélectionnez le brouillon que vous venez de créer.
4. Créez un nouveau champ ou modifiez un champ existant.
5. Définissez le chemin souhaité pour l'extraction des données.
6. Cliquez sur **Save**.

## Configuration des chemins d'extraction

La **configuration des chemins d'extraction** sert à extraire des données et à renseigner des champs dans l'**écran de validation**, tels que le tableau de la facture ou les champs configurés dans la mise en page de la facture.

### **Étapes pour modifier les** **chemins d'extraction** :

1. Ouvrez **Extraction Paths**.
2. Créez un nouveau brouillon en cliquant sur l'**icône de crayon**.
3. Sélectionnez le brouillon que vous venez de créer.
4. Créez un nouveau champ ou modifiez un champ existant.
5. Le côté gauche représente l'**ID de champ DocBits**, que vous trouvez sous **Settings → Global Settings → Document Types → Invoice → Fields**.\\
6. Le côté droit représente le **chemin vers le champ** créé dans la transformation.
7. Cliquez sur **Save**.

En suivant ces étapes, vous garantissez une extraction et une validation précises des données pour les factures ZUGFeRD.
