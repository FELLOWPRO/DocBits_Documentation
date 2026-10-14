# Bar Code Extractions

## Aperçu

Cette fonctionnalité permet la détection automatique des codes-barres sur les documents. Lorsqu'elle est activée, tous les types de codes-barres pris en charge sont analysés et extraits pendant le traitement.

## Comment activer l'extraction de codes-barres

Pour activer la fonctionnalité Bar-Code Extraction, procédez comme suit :

1. **Accédez aux paramètres** :
   * Depuis le tableau de bord, allez dans **Settings**.
   * Sélectionnez **Document Processing**, puis choisissez **Module**.
2. **Activez la fonctionnalité** :
   * Faites défiler la page jusqu'à l'option **Bar-Code Extraction**.
   * Faites glisser le curseur pour activer Bar-Code Extraction.\\

## **Paramètres supplémentaires**

### **Barcode Assignment**

#### **Objectif :** permet aux validateurs d'affecter manuellement une valeur de code-barres extraite à un champ de document précis pendant la validation des champs.

#### Comment activer **Barcode Assignment**

Pour activer la fonctionnalité **Barcode Assignment**, procédez comme suit :

1. **Accédez aux paramètres** :
   * Depuis le tableau de bord, allez dans **Settings**.
   * Sélectionnez **Document Processing**, puis choisissez **Module**.
2. **Activez la fonctionnalité** :
   * Faites défiler la page jusqu'à l'option **Barcode Assignment**.
   * Faites glisser le curseur pour activer **Barcode Assignment**.\\

#### **Fonctionnement :**

* Ajoute une option « Assign Barcode » dans l'écran de validation des champs.\\
* Les utilisateurs peuvent sélectionner une valeur de code-barres détectée et l'associer à un champ du document, comme PO Number ou Invoice Number.\\

### Séparation d'un document par code-barres / code QR

**Objectif :** sépare automatiquement les documents de plusieurs pages en documents distincts en fonction de la présence de codes-barres ou de codes QR spécifiques.

#### Comment activer la séparation d'un document par code-barres / code QR

Pour activer la fonctionnalité de **séparation d'un document par code-barres / code QR**, procédez comme suit :

1. **Accédez aux paramètres** :
   * Depuis le tableau de bord, allez dans **Settings**.
   * Sélectionnez **Document Processing**, puis choisissez **Classification and Extraction**.
2. **Activez la fonctionnalité** :
   * Repérez l'option **Document Splitting**.
   * Pour **Split**, sélectionnez **Split by Barcode / QR Code**.
   * Pour **Barcode Type**, choisissez un ou plusieurs types de codes-barres pris en charge dans la liste.
   * Pour **Barcode Pattern**, définissez le motif qui doit déclencher une séparation. Vous pouvez utiliser une **expression régulière** (regex) pour faire correspondre des valeurs de code-barres dynamiques.

**Fonctionnement :**

* Vous sélectionnez les types de codes-barres qui doivent déclencher une séparation.
* Vous définissez un motif auquel le code-barres doit correspondre. Il peut s'agir d'une chaîne fixe ou d'une regex (p. ex. `^INV\d{6}$` pour faire correspondre des codes-barres comme `INV123456`).
* Pendant le traitement du document, chaque fois qu'une page contient un code-barres correspondant, un **nouveau document est créé** à partir de cette page.

### Types de codes pris en charge

Consultez la [page d'aperçu](./) pour la liste complète des formats de codes-barres et de codes QR pris en charge.
