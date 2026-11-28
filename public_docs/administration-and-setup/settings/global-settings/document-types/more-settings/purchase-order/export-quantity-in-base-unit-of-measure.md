# Quantité exportée dans l'unité de mesure de base

Le commutateur **Export quantity in base unit of measure** se trouve dans la section **Purchase Order** des **More Settings** d'un type de document. Il modifie la quantité et le prix unitaire que l'export vers Infor LN écrit pour les lignes de commande appariées.

Ouvrez-le sous **Settings → Document Types**, sélectionnez l'icône d'engrenage (**More Settings**) sur la carte du type de document et déployez **Purchase Order**.

## Ce que fait le commutateur

* **Off:** DocBits exporte la quantité et le prix unitaire dans l'unité de la facture.
* **On:** DocBits convertit la quantité et le prix unitaire de chaque ligne de commande appariée dans l'unité de mesure de base de cette ligne, à l'aide de son facteur de conversion, et écrit le code de l'unité de base au lieu du code de l'unité facturée.

Une ligne sans facteur de conversion est exportée sans modification ; un facteur manquant ne bloque donc pas l'export.

{% hint style="info" %}
La conversion ne s'applique qu'à l'export vers Infor LN. Les autres destinations d'export conservent l'unité facturée.
{% endhint %}

## Quand l'utiliser

Activez le commutateur lorsque l'instance Infor LN attend des quantités de commande dans l'unité de mesure de base. La conversion utilise le facteur enregistré sur la ligne de commande, et non un facteur que DocBits calcule à partir de la fiche article.

Les paramètres peuvent affecter des documents en cours d'utilisation. Vérifiez le résultat avec un document de test avant d'enregistrer la modification en production. Le commutateur modifie les valeurs exportées ; il ne change pas la façon dont les lignes de facture et de commande sont appariées.

## Pages associées

* [Commande d'achat](README.md)
* [Export des lignes de commande non appariées](export-not-matched-po-lines.md)
* [Exportation alternative](alternate-export.md)

<!-- Documentation review 2026-11-27: switch label, help text and behaviour checked against DocBits_Web src/pages/Settings/Components/DocTypes/PO.vue on origin/sandbox-nova (DOP-53, commit feb262ab89, contained in the deployed NOVA build 11.24.8). -->
