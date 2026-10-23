# Éditeur de mise en page

Utilisez le éditeur de mise en page pour organiser les champs et les contrôles que les utilisateurs voient lorsqu'ils valident ou approuvent un document. Une mise en page appartient à un seul type de document, une seule origine et un seul type de mise en page : vérifiez donc ces trois éléments en haut de la page avant d'enregistrer.

## Ouvrir la mise en page

1. Ouvrez **Paramètres → Types de documents**.
2. Sélectionnez le type de document à modifier, puis ouvrez le **éditeur de mise en page**. Pour un sous-type de document, ouvrez l'action éditeur de mise en page de ce sous-type.
3. Vérifiez l'en-tête. Le sélecteur de gauche correspond à l'**Origine** (par exemple **Par défaut**), suivi du **Type de document** (par exemple **Facture**) et du **Type de mise en page** (par exemple **Validation des champs**). Chaque sélecteur ouvre une liste ; le choix d'une autre entrée charge la mise en page correspondante. Si le éditeur de mise en page n'est pas disponible, un administrateur doit peut-être activer le module pour votre organisation.

<figure><img src="../../../.gitbook/assets/layout-builder-overview-fr.png" alt="Le éditeur de mise en page d'une facture dans DocBits, avec les sélecteurs d'origine, de type de document et de type de mise en page, les onglets Structure, Champs et Éléments, le canevas de mise en page et le panneau Propriétés à droite"><figcaption><p>Le éditeur de mise en page : les sélecteurs de l'en-tête, les listes d'éléments à gauche, le canevas au centre et le panneau Propriétés à droite.</p></figcaption></figure>

## Utiliser l'en-tête

* **Type de document** et **Type de mise en page** permettent de passer d'une mise en page à l'autre. La page recharge la mise en page choisie.
* À côté de **Enregistrer**, DocBits indique si la mise en page comporte des **Modifications non enregistrées**. Après un enregistrement, la date du dernier enregistrement s'affiche.
* **Enregistrer** sauvegarde la mise en page pour le type de document, l'origine et le type de mise en page sélectionnés.
* Le menu **Plus** (trois points) contient **Générer automatiquement un modèle**, **Appliquer la disposition par défaut aux origines**, **Utiliser le modèle par défaut**, **Modifier JSON**, **Copier JSON** et **Paramètres de mise en page**. **Générer automatiquement un modèle** et **Utiliser le modèle par défaut** remplacent une mise en page personnalisée : vérifiez donc d'abord le type de document et la mise en page sélectionnés. **Modifier JSON** relève de la configuration avancée et ne doit être utilisé que si vous maîtrisez le format du modèle.
* Si vous quittez la page avec des modifications non enregistrées, DocBits vous demande si vous souhaitez les enregistrer ou les abandonner.

## Trouver des éléments : Structure, Champs, Éléments

La partie gauche comporte trois onglets :

| Onglet | À quoi il sert |
| --- | --- |
| **Structure** | Afficher la mise en page sous forme d'arborescence. Les groupes et leurs champs sont listés dans l'ordre où ils apparaissent sur le canevas, avec le nombre de champs placés et disponibles. |
| **Champs** | Tous les champs configurés pour le type de document, regroupés par groupe de champs et réduits par défaut. Le filtre alterne entre les champs **Tous**, **Inutilisé** et **Masqué**, et le nom technique du champ apparaît sous son étiquette. |
| **Éléments** | Contrôles de présentation et d'interaction tels que Texte, Étiquette, Case à cocher, séparateurs, tableaux, boutons et sous-groupes. |

<figure><img src="../../../.gitbook/assets/layout-builder-structure-fr.png" alt="L'onglet Structure du éditeur de mise en page affichant les groupes Détails de la facture, Détails du paiement, Bon de commande et Détails de livraison développés en leurs champs"><figcaption><p>L'onglet Structure présente la mise en page créée sous forme d'arborescence de groupes et de champs.</p></figcaption></figure>

Sélectionnez un élément pour l'ajouter, ou faites-le glisser sur le canevas. Le titre d'un groupe indique à la personne qui valide le document ce qui relève de cette section. Créez ou renommez d'abord les champs de document réutilisables dans [Types de documents](README.md).

## Travailler sur le canevas

* **Mise en page principale** affiche la mise en page du document lui-même. **Tableau** affiche la mise en page du tableau utilisée pour les lignes d'articles.
* **Document** ouvre ou ferme le document d'exemple à côté du canevas, ce qui vous permet de comparer la mise en page à un document réel.
* Les groupes sont représentés sous forme de cartes ; les champs d'un groupe peuvent être disposés en lignes et avoir des largeurs différentes.

## Modifier les propriétés d'un élément

Sélectionnez un élément ou un groupe sur le canevas. Le panneau **Propriétés**, à droite, est toujours visible et organisé en sections :

* **Affichage** – étiquette, nom du champ, position de l'étiquette et largeur de l'élément.
* **Comportement** – lecture seule, masqué et index des onglets.
* **Valeurs et listes** – les valeurs proposées pour l'élément.
* **Automatisation** – règles qui remplissent ou modifient l'élément.
* **Bordures et espacement** – l'apparence de l'élément.

Pour la largeur, choisissez l'une des valeurs prédéfinies (25, 33, 50, 66, 75 ou 100 pour cent) au lieu de saisir une valeur, puis vérifiez le résultat sur le canevas. Les sections et options affichées dépendent de l'élément sélectionné. Pour plus de détails, consultez [Configurer les propriétés des champs](../../settings/global-settings/document-types/layout-manager/configuring-field-properties.md).

## Vérifier et enregistrer

Organisez les groupes et les champs, vérifiez la mise en page sur le canevas et utilisez **Enregistrer** dans l'en-tête lorsque le résultat vous convient. Pour les mises en page propres à une origine, consultez [Mises en page par origine](origin-layouts.md).

{% hint style="info" %}
Les captures d'écran présentent des paramètres synthétiques dans l'organisation de test DocBits, avec le français sélectionné dans l'application. Aucune mise en page n'a été enregistrée ni remplacée lors de leur réalisation.
{% endhint %}
