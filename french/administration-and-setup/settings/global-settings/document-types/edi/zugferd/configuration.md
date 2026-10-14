# Configuration de ZUGFeRD

{% embed url="https://youtu.be/AxrHNEmmXtg" %}
Tutoriel DocBits E-Invoice : Traiter XRechnung / ZUGFeRD (Factur-X), valider les données et automatiser les workflows
{% endembed %}

## **Versions supportées de ZUGFeRD**

DocBits supporte toutes les versions majeures de ZUGFeRD, notamment :

* **1.0**
* **2.0**
* **2.1** (conforme à FACTUR-X 1.0.05)
* **2.2**
* **2.3** (conforme à FACTUR-X 1.07.2)
* **2.3.2**

#### Activation et modification standard

Le standard ZUGFeRD est toujours actif par défaut, mais vous pouvez y apporter des modifications si nécessaire.

### **Étapes pour modifier les paramètres ZUGFeRD :**

1. Naviguez vers **Paramètres → Paramètres globaux → Types de documents → Facture**.
2. Cliquez sur **E-Doc**.
3. Une liste de tous les e-docs disponibles apparaîtra.
4. Localisez la version **ZUGFeRD** que vous souhaitez modifier.

## **Configuration de la transformation et du chemin XML :**

Dans les **paramètres de transformation**, vous pouvez définir le chemin pour localiser des informations spécifiques dans le fichier XML et les enregistrer dans une nouvelle structure, ce qui facilite l'accès aux données. <mark style="color:red;">**Remarque**</mark> : Si vous utilisez cette fonctionnalité, vous devez utiliser les nouveaux chemins XML créés, et non les chemins XML originaux, dans la **Prévisualisation** et le **Chemin d'extraction**.

### **Étapes pour modifier le fichier de transformation :**

1. Ouvrez la **Transformation**.
2. Créez un nouveau brouillon en cliquant sur l'**icône crayon**.
3. Sélectionnez le brouillon nouvellement créé.
4. Créez un nouveau champ ou modifiez-en un existant.
5. Définissez le chemin souhaité pour l'extraction des données.
6. Cliquez sur **Enregistrer**.

### Remarques importantes :

* Le **fichier de prévisualisation** est utilisé uniquement pour **FACTUR-X** et non pour **ZUGFeRD**. ZUGFeRD utilisera le **PDF** original.

## Configuration du PDF de prévisualisation

La **Configuration du PDF de prévisualisation** est utilisée pour générer une version du document lisible par l'utilisateur. Vous pouvez la personnaliser avec du HTML pour qu'elle corresponde à vos besoins.

### **Étapes pour modifier le fichier de prévisualisation :**

1. Ouvrez la **Prévisualisation**.
2. Créez un nouveau brouillon en cliquant sur l'**icône crayon**.
3. Sélectionnez le brouillon nouvellement créé.
4. Créez un nouveau champ ou modifiez-en un existant.
5. Définissez le chemin souhaité pour l'extraction des données.
6. Cliquez sur **Enregistrer**.

## Configuration des chemins d'extraction

La **Configuration des chemins d'extraction** est utilisée pour extraire des données et remplir des champs dans l'**écran de validation**, tels que le tableau des factures ou les champs configurés dans la mise en page de la facture.

### **Étapes pour modifier les** **chemins d'extraction** :

1. Ouvrez les **Chemins d'extraction**.
2. Créez un nouveau brouillon en cliquant sur l'**icône crayon**.
3. Sélectionnez le brouillon nouvellement créé.
4. Créez un nouveau champ ou modifiez-en un existant.
5. Le côté gauche représente l'**ID de champ DocBits**, qui se trouve dans **Paramètres → Paramètres globaux → Types de documents → Facture → Champs**.
6. Le côté droit représente le **chemin vers le champ** créé dans la Transformation.
7. Cliquez sur **Enregistrer**.

En suivant ces étapes, vous pouvez garantir une extraction et une validation précises des données pour les factures ZUGFeRD.
