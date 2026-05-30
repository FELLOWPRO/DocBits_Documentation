# Affectation par code-barres

### Aperçu

Le paramètre **Affectation par code-barres** (Barcode Assignment) ajoute un outil de code-barres à l'**écran de validation des documents**. Il lit les codes-barres et QR codes présents dans un document et vous permet d'**affecter leurs valeurs aux champs du document** — par exemple, renseigner un numéro de commande, de référence ou de bon de livraison à partir d'un code-barres au lieu de le saisir.

Ce paramètre est **désactivé par défaut**.

### Ce que vous obtenez en l'activant

Une fois le paramètre activé, un nouveau **bouton code-barres** (une icône QR code) apparaît dans la barre d'outils sur le côté droit de l'**écran de validation** (`/field_validation_v1/…`). Ce bouton est le point d'entrée de toute la fonction — sans le paramètre, l'icône reste masquée.

<figure><img src="../../../../.gitbook/assets/barcode_assignment_validation_icon.png" alt="L'icône code-barres (QR code) dans la barre d'outils de validation"><figcaption><p>Lorsque le paramètre est activé, l'icône code-barres apparaît dans la barre d'outils de validation.</p></figcaption></figure>

Voici l'icône en contexte sur l'écran de validation, à côté du document en cours d'examen :

<figure><img src="../../../../.gitbook/assets/barcode_assignment_validation_screen.png" alt="Écran de validation avec l'icône code-barres disponible"><figcaption><p>L'écran de validation — l'icône code-barres (en surbrillance, barre d'outils de droite) n'est affichée que lorsque l'Affectation par code-barres est activée.</p></figcaption></figure>

### Comment les codes-barres sont lus

DocBits détecte les codes-barres pendant le traitement du document et propose leurs valeurs décodées pour l'affectation. Un même document peut comporter plusieurs types de codes-barres — par exemple un **QR code**, un **Code 128** et un **EAN-13** — chacun encodant une valeur différente, telle qu'un numéro de commande, un numéro de facture ou un GLN de fournisseur.

<figure><img src="../../../../.gitbook/assets/barcode_assignment_demo_invoice.png" alt="Facture de démonstration comportant plusieurs types de codes-barres"><figcaption><p>Exemple de facture de démonstration DocBits comportant trois types de codes-barres (QR code → numéro de commande, Code 128 → numéro de facture, EAN-13 → GLN de fournisseur), chacun encodant une valeur que vous pouvez affecter à un champ.</p></figcaption></figure>

{% hint style="info" %}
Les types de codes-barres détectés sont déterminés par le paramètre **Bar-Code / QR Code Extraction** (`Barcode Extraction Types`). Si la boîte de dialogue affiche *« no barcodes extracted found »*, vérifiez que l'extraction des codes-barres est activée et que les types attendus (p. ex. `QRCODE`, `CODE128`, `EAN13`) sont sélectionnés. Voir [Bar-Code / QR Code Extraction](bar-code-qr-code-extraction/README.md).
{% endhint %}

### Utiliser la boîte de dialogue d'Affectation par code-barres

1. Ouvrez un document sur l'**écran de validation**.
2. Cliquez sur l'**icône code-barres** dans la barre d'outils de droite.
3. La boîte de dialogue **Affectation par code-barres** liste chaque code-barres détecté par DocBits dans le document, sous la forme `Barcode <n> : <valeur>`.

<figure><img src="../../../../.gitbook/assets/barcode_assignment_dialog.png" alt="Boîte de dialogue d'Affectation par code-barres listant les codes détectés"><figcaption><p>La boîte de dialogue d'Affectation par code-barres liste chaque code détecté avec une liste déroulante pour choisir le champ cible.</p></figcaption></figure>

4. Pour chaque code-barres, ouvrez sa liste déroulante et choisissez le champ dans lequel la valeur doit aller.

<figure><img src="../../../../.gitbook/assets/barcode_assignment_field_options.png" alt="Choix du champ cible pour un code-barres"><figcaption><p>Chaque code-barres peut être affecté à n'importe quel champ du document — p. ex. Numéro de commande, Numéro de facture, ID fournisseur.</p></figcaption></figure>

5. Dès que vous sélectionnez un champ, celui-ci est renseigné avec la valeur du code-barres.

<figure><img src="../../../../.gitbook/assets/barcode_assignment_field_mapped.png" alt="Code-barres affecté au champ Numéro de commande"><figcaption><p>Après la sélection d'un champ (ici Numéro de commande), le champ est renseigné avec la valeur du code-barres.</p></figcaption></figure>

### Comment l'activer

1. Allez dans **Paramètres**.
2. Sélectionnez **Traitement des documents**.
3. Sélectionnez **Module**.
4. Ouvrez la section **Type de document**.
5. Repérez **Affectation par code-barres** et activez le commutateur.

<figure><img src="../../../../.gitbook/assets/barcode_assignment_toggle.png" alt="Commutateur Affectation par code-barres"><figcaption><p>Le commutateur Affectation par code-barres dans Paramètres → Traitement des documents → Module.</p></figcaption></figure>

### Avantages

* **Saisie plus rapide et sans erreur** : Reprenez les valeurs directement depuis un code-barres au lieu de les lire et de les saisir à la main.
* **Moins de fautes de frappe** : Une valeur scannée correspond exactement à ce qui est encodé dans le code-barres.
* **Vous gardez le contrôle** : Vous décidez quel code-barres va dans quel champ pendant la validation.

### Quand utiliser cette fonction

* **Documents avec codes-barres** : Lorsque vos documents comportent des codes-barres/QR dont les valeurs doivent aller dans des champs précis (p. ex. numéros de commande ou de référence).
* **Flux de validation manuelle** : Lorsqu'une personne examine les documents et souhaite renseigner les champs rapidement à partir des codes-barres.
* **Laissez-le désactivé** si vos documents n'ont pas de codes-barres exploitables, ou si vous n'avez besoin que de l'**extraction** automatique des codes-barres/QR — voir [Bar-Code / QR Code Extraction](bar-code-qr-code-extraction/README.md).

{% hint style="info" %}
**Ceci sert à lire une valeur de code-barres/QR et à l'affecter à un champ pendant la validation.** L'extraction automatique de données structurées à partir de codes de paiement (comme Swiss QR Bill ou GiroCode) — ainsi que la division d'un fichier de plusieurs pages aux pages séparatrices à code-barres — sont gérées par un paramètre **différent** : [Bar-Code / QR Code Extraction](bar-code-qr-code-extraction/README.md).
{% endhint %}
