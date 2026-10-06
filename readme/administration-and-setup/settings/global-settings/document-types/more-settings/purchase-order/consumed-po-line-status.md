# Statut de la ligne de commande PO consommée

**Le statut de la ligne de commande PO consommée** colore les lignes de bon de commande dans l'écran de correspondance selon la proportion de chaque ligne déjà appariée. Activez-le pour le type de document utilisé par vos factures si votre équipe doit repérer rapidement les lignes de PO non utilisées, partiellement utilisées et entièrement utilisées. La couleur est une aide visuelle ; vérifiez la **quantité appariée** et la colonne de quantité de PO sélectionnée avant de décider si une ligne peut être appariée à nouveau.

## Activer le paramètre

1. Ouvrez **Paramètres → Types de documents**. Trouvez le type de document utilisé pour vos factures et sélectionnez la roue dentée sur sa carte pour ouvrir **Plus de paramètres**. La capture montre la carte **Facture**. Laissez les interrupteurs **Activer** et **Extraction** tels quels.

   <figure><img src="../../../../../../.gitbook/assets/1-consumed-po-line-document-types-fr.png" alt="Page Types de documents avec la carte Facture et sa roue dentée Plus de paramètres"><figcaption><p>Ouvrez Plus de paramètres depuis la carte Facture.</p></figcaption></figure>

2. Dépliez **Bon de commande** s'il est replié. Trouvez **Statut de la ligne de commande consommée** et activez son interrupteur. C'est un paramètre distinct de **Mettre à jour le statut du bon de commande du document** plus bas dans la même section.

   <figure><img src="../../../../../../.gitbook/assets/2-consumed-po-line-settings-fr.png" alt="Section Bon de commande de la page Plus de paramètres, avec l'interrupteur Statut de la ligne de commande consommée visible"><figcaption><p>Choisissez l'interrupteur Statut de la ligne de commande consommée.</p></figcaption></figure>

   <figure><img src="../../../../../../.gitbook/assets/3-consumed-po-line-toggle-fr.png" alt="Vue rapprochée du libellé Statut de la ligne de commande consommée et de son interrupteur"><figcaption><p>L'interrupteur est éteint dans cet exemple ; allumez-le pour afficher les couleurs de correspondance.</p></figcaption></figure>

3. Ouvrez une facture avec la correspondance de bon de commande et inspectez ses lignes de PO. Les exemples ci-dessous montrent comment les couleurs des lignes se rapportent à l'état de correspondance. Pour les étapes de correspondance, voir [Écran de Correspondance des Bons de Commande](../../../../../../end-user-and-partner-section/end-user-section/purchase-order-matching/README.md).

## Lire les couleurs des lignes de PO

| Apparence | Signification | À vérifier |
| --- | --- | --- |
| Neutre ou blanche | Aucune quantité de cette ligne de PO n'a encore été appariée. | Vérifiez la quantité de PO et la ligne de facture avant l'appariement. |
| Teinte bleue | Vous avez sélectionné la ligne dans l'écran de correspondance actuel. | La sélection est temporaire ; elle ne signifie pas que la ligne est entièrement appariée. |
| Orange pâle | Une partie de la quantité est appariée, mais la quantité appariée est inférieure à la quantité de PO sélectionnée. | Vérifiez la quantité restante. |
| Violet pâle | La quantité appariée atteint au moins la quantité de PO sélectionnée. | Ne partez pas du principe qu'une quantité supplémentaire est disponible. |

<figure><img src="../../../../../../.gitbook/assets/image (470).png" alt="Ligne de PO avec quantité appariée nulle et sans couleur de statut"><figcaption><p>Aucune quantité n'a encore été appariée.</p></figcaption></figure>

<figure><img src="../../../../../../.gitbook/assets/image (472).png" alt="Ligne de PO avec une teinte bleue de sélection dans l'écran de correspondance"><figcaption><p>La ligne est sélectionnée pour la correspondance en cours.</p></figcaption></figure>

<figure><img src="../../../../../../.gitbook/assets/consumed_po_line_status.png" alt="Ligne de PO avec un fond orange pâle et une quantité appariée inférieure à la quantité de PO"><figcaption><p>La ligne est partiellement utilisée.</p></figcaption></figure>

<figure><img src="../../../../../../.gitbook/assets/image (473).png" alt="Ligne de PO avec un fond violet pâle et une quantité appariée égale à la quantité de PO"><figcaption><p>La ligne est entièrement utilisée.</p></figcaption></figure>

Une ligne barrée a une signification différente : son statut de PO est peut-être exclu par [Statuts de désactivation des bons de commande](purchase-order-disable-statuses.md). Vérifiez ce paramètre si une ligne ne peut pas être sélectionnée.
