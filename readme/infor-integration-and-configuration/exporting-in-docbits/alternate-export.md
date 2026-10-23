# Exportation alternative

## **Étape 1 : créer une nouvelle exportation**

1. Accédez à **Settings** > **Document Processing** > **Export**.
2. Cliquez sur **Create New Export** pour définir une nouvelle configuration d'exportation.
3. Enregistrez la configuration et veillez à ce que l'exportation soit **désactivée**.

<figure><img src="../../.gitbook/assets/image (368).png" alt="Liste des paramètres d'exportation avec les lignes Alternate-Export-Invoice-LN-IDM-BOD et Export-Invoice-LN pour le type de document Invoice, la méthode d'exportation Infor-IoN-Cloud et les icônes d'action"><figcaption></figcaption></figure>

### **Étape 2 : activer l'exportation alternative**

1. Accédez à **Settings** > **Global Settings** > **Document Type** > **More Settings**.
2. Repérez le paramètre **Alternate Export** et activez-le.
3. Configurez les éléments suivants :
   * **Document Status** : indiquez le statut des documents après l'exportation alternative.
   * **Export Configuration** : sélectionnez la configuration d'exportation que vous venez de créer, à utiliser pour l'exportation alternative.

<figure><img src="../../.gitbook/assets/image (369).png" alt="Page More Settings du type de document Invoice montrant l'option Alternate Export avec le statut Pending approval et l'Export Configuration Alternate-Export-Invoice-LN-IDM-BOD-8203"><figcaption></figcaption></figure>

## Utiliser l'exportation alternative

**Dans l'écran PO-Matching**

* Une fois l'exportation alternative activée, vous pouvez la sélectionner directement dans l'écran **PO-Matching**.

<figure><img src="../../.gitbook/assets/image (370).png" alt="Écran PO Matching avec la recherche du numéro de commande 100000300, les boutons CONFIRM &amp;amp; EXPORT et Reject et le panneau Document Alternate Export"><figcaption></figcaption></figure>

**Avec la carte de workflow**

* La carte de workflow **Alternate Export** peut également être utilisée pour automatiser ce processus. Configurez la carte selon vos besoins afin d'appliquer la logique d'exportation alternative à votre workflow.
