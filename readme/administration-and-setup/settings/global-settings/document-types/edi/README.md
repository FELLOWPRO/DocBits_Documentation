# Documents électroniques et configuration EDI

{% embed url="https://youtu.be/AxrHNEmmXtg" %}
DocBits Tutoriel sur la facture électronique : traiter XRechnung / ZUGFeRD (Factur-X), valider les données et automatiser les flux de travail
{% endembed %}

Sélectionnez le type de document et le format électronique dans les paramètres des documents électroniques. Cette configuration traite les messages EDI entrants ; elle ne configure pas leur transmission sortante.

<figure><img src="../../../../../.gitbook/assets/site-all-edi-list-fr.png" alt="Format EDI existant avec ses quatre attributs configurés."><figcaption><p>Format EDI existant avec ses quatre attributs configurés.</p></figcaption></figure>

* STRUCTUREDESCRIPTOR : un descripteur de structure JSON analyse le message EDI brut et produit du JSON. DocBits crée ensuite un XML intermédiaire.

* TRANSFORMATION : une feuille XSLT transforme le XML intermédiaire en XML standard pour les traitements suivants.

* PREVIEW : une feuille XSLT produit une présentation lisible à partir du XML transformé. La capture de l’éditeur montre le code source, pas le document rendu.

* EXTRACTIONPATHS : la configuration JSON associe les champs et les colonnes à des expressions XPath évaluées sur le XML transformé.

<figure><img src="../../../../../.gitbook/assets/site-all-edi-detail-fr.png" alt="Attribut STRUCTUREDESCRIPTOR actif : descripteur de structure JSON dans l’éditeur en lecture seule."><figcaption><p>Attribut STRUCTUREDESCRIPTOR actif : descripteur de structure JSON dans l’éditeur en lecture seule.</p></figcaption></figure>

## Règles effectivement utilisées et activation

Si un avoir électronique apparaît comme Invoice, suivez le [guide de diagnostic de la classification](credit-note-recognized-as-invoice.md). Il couvre la source personnalisée ou par défaut effectivement utilisée, les codes de type, Extraction Paths et l’activation en toute sécurité.

## Guides par pays

Consultez les guides par pays pour connaître les libellés exacts des formats, la syntaxe, les limites de version et l’état de configuration examiné. [Formats eDocs, versions et guides par pays](supported-electronic-documents/README.md).


Les vues montrent une configuration et une version existantes. Les paramètres varient selon le type de document et le format. Validez les modifications dans un brouillon avant leur activation.

Certaines mentions, telles que Custom et Default, correspondent à l’interface actuelle du produit. Les identifiants techniques des attributs et le code de configuration restent inchangés.
