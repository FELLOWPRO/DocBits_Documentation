# Affectation par code-barres

### Aperçu

Le paramètre **Affectation par code-barres** (Barcode Assignment) permet à DocBits d'utiliser les **codes-barres présents dans un fichier pour le séparer en documents individuels**. C'est utile lorsque plusieurs documents sont numérisés ensemble dans un seul grand PDF et qu'un code-barres indique où un document se termine et où commence le suivant.

Ce paramètre est **désactivé par défaut**.

### Que fait ce paramètre ?

Lorsque ce paramètre est activé, DocBits recherche les codes-barres dans un fichier entrant de plusieurs pages et le divise en documents distincts aux positions marquées. Chaque document obtenu est ensuite traité séparément.

* **Activé** — DocBits détecte les codes-barres et sépare automatiquement un fichier combiné en documents individuels en fonction de ceux-ci.
* **Désactivé** — Le fichier est traité comme un seul document ; les codes-barres ne servent pas à le diviser.

{% hint style="info" %}
Il s'agit ici de **diviser et d'affecter** des pages en fonction des codes-barres. La lecture des données encodées dans un code-barres (par exemple pour les QR codes de paiement) est gérée séparément dans **Bar-Code / QR Code Extraction**.
{% endhint %}

### Avantages

* **Numérisation par lots plus rapide** : Numérisez une pile entière de documents en une seule passe, séparés par des feuilles à code-barres, au lieu de numériser chaque document individuellement.
* **Moins de tri manuel** : DocBits crée les documents individuels pour vous, personne n'a donc à diviser le PDF à la main.
* **Moins d'erreurs** : Les documents sont séparés exactement aux positions marquées à chaque fois.

### Utilisation

1. Allez dans **Paramètres**.
2. Sélectionnez **Traitement des documents**.
3. Sélectionnez **Module**.
4. Ouvrez la section **Type de document**.
5. Repérez **Affectation par code-barres** et activez le commutateur.

### Quand utiliser cette fonction

* **Numérisation en grand volume** : Lorsque vous numérisez de nombreux documents ensemble et utilisez des feuilles séparatrices à code-barres entre eux.
* **Lots mixtes** : Lorsqu'un seul fichier entrant contient plusieurs documents différents à traiter séparément.
* **Laissez-le désactivé** si vos documents arrivent toujours sous forme de fichiers distincts — la division n'est alors pas nécessaire.
