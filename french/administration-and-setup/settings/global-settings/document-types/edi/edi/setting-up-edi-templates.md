---
hidden: true
---

# Configurer les attributs EDI

Sélectionnez le format réel du message et le type de document. Vérifiez les attributs existants et les versions actives avant de modifier la configuration.

<figure><img src="../../../../../../.gitbook/assets/site-all-edi-list-fr.png" alt="Format EDI existant avec ses quatre attributs configurés."><figcaption><p>Format EDI existant avec ses quatre attributs configurés.</p></figcaption></figure>

Définissez les segments, éléments et boucles dans un descripteur de structure JSON. Testez des messages représentatifs et inspectez le XML intermédiaire produit.

<figure><img src="../../../../../../.gitbook/assets/site-all-edi-detail-fr.png" alt="Attribut STRUCTUREDESCRIPTOR actif : descripteur de structure JSON dans l’éditeur en lecture seule."><figcaption><p>Attribut STRUCTUREDESCRIPTOR actif : descripteur de structure JSON dans l’éditeur en lecture seule.</p></figcaption></figure>

Utilisez TRANSFORMATION avec XSLT pour convertir le XML intermédiaire en XML standard attendu. Configurez PREVIEW séparément pour la présentation ; XSLT ne traite pas directement le JSON.

<figure><img src="../../../../../../.gitbook/assets/site-all-edi-transformation-fr.png" alt="Attribut TRANSFORMATION actif : code source XSLT pour transformer le XML intermédiaire."><figcaption><p>Attribut TRANSFORMATION actif : code source XSLT pour transformer le XML intermédiaire.</p></figcaption></figure>

Configurez EXTRACTIONPATHS en JSON avec des expressions XPath pour le XML obtenu. Vérifiez les champs, lignes et montants sur des exemples réels. Validez un brouillon avant son activation ; les captures montrent une configuration active existante.

<figure><img src="../../../../../../.gitbook/assets/site-all-edi-extraction-paths-fr.png" alt="Attribut EXTRACTIONPATHS actif : configuration JSON contenant des expressions XPath d’extraction."><figcaption><p>Attribut EXTRACTIONPATHS actif : configuration JSON contenant des expressions XPath d’extraction.</p></figcaption></figure>

Dans la version de l’interface illustrée, certaines mentions, telles que Custom et Default, restent en anglais. Les identifiants techniques des attributs et le code de configuration restent inchangés.
