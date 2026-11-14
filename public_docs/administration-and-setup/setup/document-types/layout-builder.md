# Éditeur de mise en page

Utilisez l’éditeur de mise en page pour organiser les champs et les contrôles que les utilisateurs voient lorsqu’ils valident ou approuvent un document. Une mise en page appartient à un seul type de document, une seule origine et un seul type de mise en page : vérifiez ces trois éléments en haut de la page avant d’enregistrer.

{% embed url="https://youtu.be/-m45XGiIeig" %}
DocBits Layout Builder Tutorial: Create Custom Document Layouts for Faster, Cleaner Validation
{% endembed %}

## Ouvrir la mise en page

1. Ouvrez **Settings → Document Types**.
2. Sélectionnez le type de document à modifier et ouvrez **Layout Builder**. Pour un sous-type de document, ouvrez l’action Layout Builder de ce sous-type.
3. Vérifiez l’en-tête. Le sélecteur de gauche correspond à l’**origine** (par exemple **Default**), suivi de **Document Type** (par exemple **Invoice**) et de **Layout type** (par exemple **Field Validation**). Chaque sélecteur ouvre une liste ; choisir une autre entrée charge la mise en page correspondante. Si l’éditeur de mise en page n’est pas disponible, un administrateur doit peut-être activer le module pour votre organisation.

<figure><img src="https://raw.githubusercontent.com/FELLOWPRO/DocBits_Documentation/refs/heads/main/public_docs/.gitbook/assets/layout-builder-overview.png" alt="L’éditeur de mise en page d’une facture dans DocBits, avec les sélecteurs d’origine, de type de document et de type de mise en page, les onglets Structure, Fields et Elements, la zone de mise en page et le panneau Properties à droite"><figcaption><p>L’éditeur de mise en page : les sélecteurs de l’en-tête, les listes d’éléments à gauche, la zone de mise en page au centre et le panneau Properties à droite.</p></figcaption></figure>

## Utiliser l’en-tête

* **Document Type** et **Layout type** permettent de changer de mise en page. La page recharge la mise en page choisie.
* À côté de **Save**, DocBits indique si la mise en page présente des **unsaved changes**. Après un enregistrement, il indique la date du dernier enregistrement de la mise en page.
* **Save** enregistre la mise en page pour le type de document, l’origine et le type de mise en page sélectionnés.
* Le menu **More** (trois points) contient **Auto Generate template**, **Apply Default layout to Origins**, **Use default template**, **Edit JSON**, **Copy JSON** et **Layout settings**. **Auto Generate template** et **Use default template** remplacent une mise en page personnalisée : vérifiez d’abord le type de document et la mise en page sélectionnés. **Edit JSON** est destiné à la configuration avancée et ne doit être utilisé que si vous maîtrisez le format du modèle.
* Si vous quittez la page avec des modifications non enregistrées, DocBits vous demande si vous souhaitez les enregistrer ou les abandonner.

## Trouver des éléments : Structure, Fields, Elements

La partie gauche comporte trois onglets :

| Onglet | Utilisation |
| --- | --- |
| **Structure** | Affiche la mise en page sous forme d’arborescence. Les groupes et leurs champs sont listés dans l’ordre où ils apparaissent dans la zone de mise en page, avec le nombre de champs placés et disponibles. |
| **Fields** | Tous les champs configurés pour le type de document, regroupés par groupe de champs et repliés par défaut. Le filtre permet de passer entre les champs **All**, **Unused** et **Hidden**, et le nom technique du champ est affiché sous l’étiquette du champ. |
| **Elements** | Contrôles de présentation et d’interaction tels que Text, Label, Check Box, les séparateurs, les tableaux, les boutons et les sous-groupes. |

<figure><img src="https://raw.githubusercontent.com/FELLOWPRO/DocBits_Documentation/refs/heads/main/public_docs/.gitbook/assets/layout-builder-structure.png" alt="L’onglet Structure de l’éditeur de mise en page, avec les groupes Invoice details, Payment details, Purchase Order et Delivery Details dépliés sur leurs champs"><figcaption><p>L’onglet Structure montre la mise en page construite sous forme d’arborescence de groupes et de champs.</p></figcaption></figure>

Sélectionnez un élément pour l’ajouter, ou faites-le glisser dans la zone de mise en page. Le titre d’un groupe indique à la personne qui valide le document ce qui appartient à cette section. Créez ou renommez d’abord les champs de document réutilisables dans [Types de documents](README.md).

## Travailler dans la zone de mise en page

* **Main layout** affiche la mise en page du document lui-même. **Table** affiche la mise en page de tableau utilisée pour les lignes de facture.
* **Document** ouvre ou ferme le document d’exemple à côté de la zone de mise en page, pour comparer la mise en page avec un document réel.
* Les groupes sont dessinés sous forme de cartes ; les champs d’un groupe peuvent être disposés en lignes et recevoir des largeurs différentes.

## Modifier les propriétés d’un élément

Sélectionnez un élément ou un groupe dans la zone de mise en page. Le panneau **Properties** à droite est toujours visible et organisé en sections :

* **Display** – étiquette, nom du champ, position de l’étiquette et largeur de l’élément.
* **Behaviour** – lecture seule, masqué et ordre de tabulation.
* **Values & lists** – les valeurs proposées pour l’élément.
* **Automation** – les règles qui renseignent ou modifient l’élément.
* **Borders & spacing** – l’apparence de l’élément.

Pour la largeur, choisissez l’un des préréglages (25, 33, 50, 66, 75 ou 100 pour cent) au lieu de saisir une valeur, puis vérifiez le résultat dans la zone de mise en page. Les sections et les options affichées dépendent de l’élément sélectionné. Pour plus de détails, consultez [Configurer les propriétés des champs](../../settings/global-settings/document-types/layout-manager/configuring-field-properties.md).

## Traduire les étiquettes des boutons

Les boutons tels que **Save Rules**, **Auto Accounting**, **PO Match**, **Export**, **Export Without Validation** et **Reject** tirent leur étiquette d’une clé de traduction. La vue affiche l’étiquette dans la langue de la personne qui ouvre la mise en page. Si la clé ne contient aucun texte pour cette langue, DocBits affiche l’étiquette enregistrée dans la mise en page.

* Un bouton autonome dispose d’un champ **Translation Key** dans **Properties**.
* **Invoice Buttons** regroupe plusieurs boutons. Définissez la clé pour un bouton enfant unique, ou une clé par enfant dans la liste du panneau du groupe.

Les mises en page créées avant ce changement conservent leurs étiquettes : DocBits y renseigne la clé par défaut de chaque type de bouton. Les mises en page enregistrées avec une clé conservent cette clé, y compris après un rechargement.

## Save and go back to Dashboard

Un bouton du type **Save and go back to Dashboard** enregistre les valeurs du document comme **Save**, puis ouvre le Dashboard. Ce type convient aux mises en page dans lesquelles un vérificateur traite une file de documents les uns après les autres.

* Ajoutez un élément de type bouton dans la zone de mise en page et choisissez le type dans son panneau **Properties**.
* Si l’enregistrement échoue, le bouton reste sur l’écran de validation et n’ouvre pas le Dashboard, ce qui permet de corriger le problème au préalable.
* L’étiquette est résolue comme celle de tout autre bouton ; voir *Traduire les étiquettes des boutons* ci-dessus.

## Vérifier et enregistrer

Organisez les groupes et les champs, vérifiez la mise en page dans la zone de mise en page et utilisez **Save** dans l’en-tête lorsque le résultat vous convient. Pour les mises en page propres à une origine, consultez [Mises en page par origine](origin-layouts.md).

{% hint style="info" %}
Les captures d’écran montrent des paramètres synthétiques dans l’organisation de test DocBits, avec l’anglais sélectionné dans l’application. Aucune mise en page n’a été enregistrée ni remplacée lors de leur réalisation.
{% endhint %}
