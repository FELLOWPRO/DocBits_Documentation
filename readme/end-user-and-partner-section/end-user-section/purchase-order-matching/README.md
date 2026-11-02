# Écran de Correspondance des Bons de Commande

Utilisez la **Correspondance des Bons de Commande** pour comparer les lignes du bon de commande chargées pour un document avec les lignes de facture extraites. Les données du bon de commande peuvent provenir d'une intégration ERP ou d'un autre import configuré. L'écran affiche le document à côté des deux tableaux afin que vous puissiez vérifier les montants, les quantités, les prix et les écarts avant d'enregistrer ou d'exporter.

## Rapprocher les lignes d’une facture et d’une commande

Le parcours commence par un numéro de commande reconnu et trois lignes de facture rapprochées. Il présente ensuite la recherche manuelle comme exception, une liaison volontairement incorrecte, un rapprochement partiel, le rapprochement automatique et l’enregistrement. Vérifiez le résultat après rechargement : enregistrer ne suffit ni à approuver ni à exporter la facture.

{% embed url="https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/po-matching-customer/v4/fr.mp4" %}

[Regarder la vidéo avec les sous-titres](https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/po-matching-customer/v4/fr.html)

{% hint style="info" %}
La capture utilise des données de test synthétiques : trois lignes de facture extraites et leur commande. Le papier, les boîtes d’archives et la livraison totalisent 118 EUR hors taxes. Le rapprochement complet affiche 118 EUR rapprochés et aucun montant restant.
{% endhint %}

<figure><img src="../../../.gitbook/assets/po-tutorial-v4-full-fr.png" alt="Rapprochement complet : les trois lignes sont liées, avec 118 EUR rapprochés et 0 EUR restants."><figcaption><p>Rapprochement complet : les trois lignes sont liées, avec 118 EUR rapprochés et 0 EUR restants.</p></figcaption></figure>

## Rechercher et inspecter un bon de commande

1. Ouvrez la facture dans la **Correspondance des Bons de Commande**. Lorsque son numéro de commande est reconnu, DocBits charge la commande correspondante. Utilisez la recherche manuelle si le numéro manque ou pour examiner une autre commande.
2. Sélectionnez l'icône de filtre à côté de la zone de recherche pour définir **Mot-clé**, **Fournisseur**, **Statut**, **Statut de la commande**, les dates, la plage de montants, le tri et le nombre d'enregistrements affichés. Sélectionnez **Plus** pour des critères supplémentaires. Sélectionnez **Appliquer** pour lancer la recherche ou **Supprimer** pour réinitialiser les filtres.
3. Sélectionnez un numéro de bon de commande au-dessus du tableau pour inspecter ses lignes. L'icône de rafraîchissement à côté du numéro recharge les données de ce bon de commande. Ce rechargement peut dépendre de l'intégration configurée.
4. Comparez chaque ligne de commande avec la facture et son tableau extrait. Le **+** ouvre les détails de rapprochement existants ; il ne lie pas lui-même la ligne à la facture.

<figure><img src="../../../.gitbook/assets/po-tutorial-v4-search-fr.png" alt="La recherche manuelle affiche les trois lignes de la commande de test. Utilisez les filtres si nécessaire ; un numéro de commande reconnu ne demande pas une seconde recherche."><figcaption><p>La recherche manuelle affiche les trois lignes de la commande de test. Utilisez les filtres si nécessaire ; un numéro de commande reconnu ne demande pas une seconde recherche.</p></figcaption></figure>

<figure><img src="../../../.gitbook/assets/po-tutorial-v4-partial-fr.png" alt="Rapprochement partiel : le papier représente 50 EUR rapprochés et 68 EUR restent ouverts. Il ne s’agit pas d’un seuil fixe de cinquante pour cent."><figcaption><p>Rapprochement partiel : le papier représente 50 EUR rapprochés et 68 EUR restent ouverts. Il ne s’agit pas d’un seuil fixe de cinquante pour cent.</p></figcaption></figure>

## Apparier les lignes et vérifier le résultat

Lorsque les deux tableaux contiennent des lignes, connectez une ligne de facture à la ligne de bon de commande correspondante en la faisant glisser, ou utilisez les actions de correspondance du menu contextuel de la ligne. **Appariement automatique** tente de connecter les lignes éligibles selon les règles de votre organisation. Vérifiez le résultat avant d'enregistrer : un numéro d'article identique à lui seul ne prouve pas que la quantité, le prix ou les conditions de livraison concordent. Consultez [Outils de Correspondance des Bons de Commande](purchase-order-matching-tools.md) pour la barre d'outils, les contrôles de colonnes et les actions manuelles, et [Raccourcis clavier](keyboard-shortcuts.md) pour les actions au clavier.

Si un document n'est pas apparié, lisez le motif affiché au-dessus de la zone du bon de commande. Il peut indiquer que le numéro de bon de commande est absent, que le bon de commande est introuvable, que ses lignes ne sont pas disponibles, ou que la facture n'a aucune ligne extraite. Corrigez le document ou la configuration indiqués par ce motif. Un administrateur peut inspecter les [règles d'appariement](../../../administration-and-setup/settings/global-settings/document-types/more-settings/purchase-order/purchase-order-matching-rules.md) et l'[extraction de tableaux](../../../administration-and-setup/settings/document-processing/classification-and-extraction/README.md) lorsque aucune ligne de facture n'apparaît.

Messages courants et étapes suivantes :

| Ce que vous voyez | Ce qu'il faut vérifier |
| --- | --- |
| Aucun numéro de bon de commande | Saisissez ou corrigez le numéro de bon de commande sur le document, puis enregistrez. |
| Aucun bon de commande trouvé | Vérifiez le numéro et contrôlez si le bon de commande a été importé dans cette organisation. |
| Le bon de commande est trouvé mais non connecté | Essayez l'**Appariement automatique**, ou connectez les lignes manuellement après avoir vérifié les deux tableaux. |
| Aucune ligne du bon de commande ne correspond | Comparez les valeurs de la facture avec le bon de commande et consultez l'historique d'appariement. |
| Aucun article de commande trouvé | Vérifiez l'[extraction de tableaux](../../../administration-and-setup/settings/document-processing/classification-and-extraction/README.md) avant toute tentative d'appariement. |
| Aucune ligne ouverte du bon de commande | Vérifiez les [statuts des lignes consommées](../../../administration-and-setup/settings/global-settings/document-types/more-settings/purchase-order/consumed-po-line-status.md) et les statuts exclus. |

{% hint style="warning" %}
L'enregistrement peut relancer l'appariement après un numéro de bon de commande modifié ou nouvellement détecté. Vérifiez le résultat affiché après l'enregistrement. Si un appariement ne peut pas être enregistré, lisez l'erreur affichée à l'écran et demandez à un administrateur de vérifier la [règle de transformation](../../../administration-and-setup/settings/global-settings/document-types/transformation-rules.md) et les [règles d'appariement](../../../administration-and-setup/settings/global-settings/document-types/more-settings/purchase-order/purchase-order-matching-rules.md).
{% endhint %}

Utilisez l'**Historique d'appariement** (icône horloge, selon vos permissions) pour inspecter la façon dont un appariement précédent a été décidé. C'est une vue en lecture seule. Vous pouvez consulter quelles règles ont été exécutées et pourquoi un candidat n'a pas été apparié ; ouvrir l'historique n'exporte pas le document.

### Plusieurs lignes pour une correspondance

Une seule ligne de facture peut correspondre à plusieurs lignes de bon de commande, ou l'inverse, lorsque vos règles d'appariement le permettent. Ouvrez les détails **+** d'une ligne pour inspecter une éventuelle correspondance multiple. Vérifiez la quantité et le prix combinés, pas seulement une ligne. Un panneau de détails vide signifie qu'aucune correspondance multiple n'est à inspecter. Consultez [Outils de Correspondance des Bons de Commande](purchase-order-matching-tools.md) pour modifier les connexions.

### Quantités, écarts et remises

Selon la configuration, l'appariement peut comparer la quantité commandée, reçue ou restante, ainsi que le prix unitaire, le numéro d'article et d'autres champs mappés. Un écart peut être accepté si le type de document comporte une tolérance configurée. Vérifiez l'écart affiché avant de l'accepter. Les [paramètres de tolérance](../../../administration-and-setup/settings/global-settings/document-types/more-settings/purchase-order/purchase-order-tolerance-settings-additional-purchase-order-tolerance.md) et le [guide des remises](discounts.md) expliquent ces cas.

La zone des totaux, lorsqu'elle est disponible, aide à rapprocher le montant net de la facture des lignes appariées et des frais. Si un **Montant non réglé** subsiste, inspectez les valeurs individuelles des lignes et tout [élément de coût](../../../administration-and-setup/settings/document-processing/classification-and-extraction/table-extraction-for-costing-element.md) avant l'export.

## Vérifier les totaux et enregistrer

Contrôlez l'aperçu du document à droite et comparez les totaux des lignes et les éventuels frais. Pour une explication complète des actions de la barre d'outils supérieure, consultez [Outils de Correspondance des Bons de Commande](purchase-order-matching-tools.md). Sélectionnez **Enregistrer** après avoir modifié les appariements. Sélectionnez **Exporter** seulement après avoir vérifié le document et le résultat de l'appariement ; la flèche à côté d'Exporter montre d'autres choix d'export configurés. Votre organisation peut proposer des actions d'export différentes.

La barre d'outils de l'aperçu permet de naviguer entre les pages du document, de zoomer, de télécharger l'original et d'ouvrir une vue plus grande. Utilisez-la pour vérifier que le numéro de bon de commande et les valeurs des lignes figurent bien sur la facture. Si vous quittez la page avec des modifications d'appariement non enregistrées, elles peuvent être perdues.

Les comparaisons disponibles et les valeurs de tolérance dépendent des paramètres de votre type de document. Lisez [Règles d'appariement des bons de commande](../../../administration-and-setup/settings/global-settings/document-types/more-settings/purchase-order/purchase-order-matching-rules.md), [Paramètres de tolérance](../../../administration-and-setup/settings/global-settings/document-types/more-settings/purchase-order/purchase-order-tolerance-settings-additional-purchase-order-tolerance.md), [Statuts désactivés](../../../administration-and-setup/settings/global-settings/document-types/more-settings/purchase-order/purchase-order-disable-statuses.md) et [Statut des lignes de bon de commande consommées](../../../administration-and-setup/settings/global-settings/document-types/more-settings/purchase-order/consumed-po-line-status.md) pour les paramètres d'administrateur. Pour les lignes plusieurs-à-un, consultez [Remises](discounts.md) et les [Outils de Correspondance](purchase-order-matching-tools.md).
