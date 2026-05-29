# Affectation par code-barres

### Aperçu

Le paramètre **Affectation par code-barres** (Barcode Assignment) ajoute un outil de code-barres à l'**écran de validation des documents**. Il lit les codes-barres et QR codes présents dans un document et vous permet d'**affecter leurs valeurs aux champs du document** — par exemple, renseigner un numéro de référence, de commande ou de bon de livraison à partir d'un code-barres au lieu de le saisir.

Ce paramètre est **désactivé par défaut**.

### Que fait ce paramètre ?

Lorsque ce paramètre est activé, un petit **bouton code-barres** (une icône QR code) apparaît dans la barre d'outils pendant que vous validez un document. En cliquant dessus, vous voyez les codes-barres que DocBits a trouvés dans le document, et vous pouvez affecter chacun à un champ. Le champ est alors renseigné avec la valeur lue dans le code-barres.

* **Activé** — Le bouton code-barres est affiché sur l'écran de validation. Vous pouvez lire les codes-barres du document et affecter leurs valeurs aux champs.
* **Désactivé** — Le bouton est masqué et les valeurs des codes-barres ne sont pas proposées pour l'affectation pendant la validation.

{% hint style="info" %}
**Ceci sert à lire une valeur de code-barres/QR et à l'affecter à un champ pendant la validation.** L'extraction automatique de données structurées à partir de codes de paiement (comme Swiss QR Bill ou GiroCode) — ainsi que la division d'un fichier de plusieurs pages aux pages séparatrices à code-barres — sont gérées par un paramètre **différent** : [Bar-Code / QR Code Extraction](bar-code-qr-code-extraction/README.md).
{% endhint %}

### Avantages

* **Saisie plus rapide et sans erreur** : Reprenez les valeurs directement depuis un code-barres au lieu de les lire et de les saisir à la main.
* **Moins de fautes de frappe** : Une valeur scannée correspond exactement à ce qui est encodé dans le code-barres.
* **Vous gardez le contrôle** : Vous décidez quel code-barres va dans quel champ pendant la validation.

### Utilisation

1. Allez dans **Paramètres**.
2. Sélectionnez **Traitement des documents**.
3. Sélectionnez **Module**.
4. Ouvrez la section **Type de document**.
5. Repérez **Affectation par code-barres** et activez le commutateur.
6. Ensuite, lors de la validation d'un document, cliquez sur le **bouton code-barres** dans la barre d'outils et affectez les valeurs des codes-barres détectés aux champs correspondants.

### Quand utiliser cette fonction

* **Documents avec codes-barres** : Lorsque vos documents comportent des codes-barres/QR dont les valeurs doivent aller dans des champs précis (p. ex. numéros de commande ou de référence).
* **Flux de validation manuelle** : Lorsqu'une personne examine les documents et souhaite renseigner les champs rapidement à partir des codes-barres.
* **Laissez-le désactivé** si vos documents n'ont pas de codes-barres exploitables, ou si vous n'avez besoin que de l'**extraction** automatique des codes-barres/QR — voir [Bar-Code / QR Code Extraction](bar-code-qr-code-extraction/README.md).
