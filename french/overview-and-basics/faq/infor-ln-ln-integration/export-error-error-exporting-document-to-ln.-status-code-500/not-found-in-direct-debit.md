# non trouvé dans le prélèvement automatique

## **Étape 1: Vérifier la configuration LN**

1. Connectez-vous à **LN CE**.
2. Accédez au menu **Options** et sélectionnez **Exécuter le programme**.
3. Dans le champ d'entrée, tapez **Paramètres ACP** et appuyez sur Entrée pour ouvrir le programme.
4. Cliquez sur la flèche à côté du champ **Ensemble réel** pour développer les paramètres.
5. Allez à la section **Correspondance**.
   * **Vérifiez le paramètre de correspondance automatique :**
     * Si la **Correspondance automatique** est définie sur **Correspondre à la réception d'achat**, passez à l'étape suivante.
     * Si elle n'est **pas** définie sur **Correspondre à la réception d'achat**, mais que vous avez toujours cette erreur, veuillez nous contacter.

## **Étape 2: Ouvrir les paramètres de DocBits**

Si la **Correspondance automatique** est définie sur **Correspondre à la réception d'achat**, procédez aux étapes suivantes dans DocBits :

1. Ouvrez **DocBits** et accédez à la section **Paramètres**.
2. Accédez au **Traitement des documents**.
3. Sélectionnez **Exporter**.
4. Dans la section **Exporter**, cliquez sur l'icône des **trois points** à côté de l'export qui ne fonctionne pas et sélectionnez **Modifier**.
5. Dans le menu **Modifier les paramètres d'export**, cliquez sur **Télécharger le fichier de mappage LN**.

## **Étape 3: Modifier le fichier de mappage LN**

1. Ouvrez le fichier de mappage LN téléchargé.
2. Recherchez le champ **IRF\_PackingSlip**.
   * Si le champ **IRF\_PackingSlip** est présent et défini sur **rien** (vide), mettez à jour avec **TF\_packing\_slip**.
   * Si le champ **IRF\_PackingSlip** n'est **pas présent**, ajoutez-le au fichier et définissez sa valeur sur **TF\_packing\_slip**.
3. Pour le champ **InvoiceReceiptFields**, ajoutez **PackingSlip** aux valeurs.

Il devrait ressembler à ceci :

<figure><img src="../../../../.gitbook/assets/PackingSlip.png" alt=""><figcaption></figcaption></figure>

## **Étape 4: Ajouter le fichier mis à jour à DocBits**

1. Retournez à la section **Exporter** dans DocBits où vous avez précédemment téléchargé le fichier de mappage LN.
2. Téléchargez le fichier de mappage LN édité avec les nouvelles mises à jour.

## Si vous rencontrez toujours l'**Erreur d'exportation du document vers LN** avec le code d'état **500**, veuillez nous contacter
