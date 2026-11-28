# Commande d'achat

La carte **Purchase Order** des **More Settings** d'un type de document contrôle la manière dont les documents de ce type sont appariés aux commandes d'achat. Les paramètres s'appliquent à un seul type de document à la fois : ouvrez donc d'abord le type de document que vous voulez modifier sous **Settings → Document Types**.

Pour trouver les paramètres d'une facture :

1. Ouvrez **Settings → Document Types**.
2. Trouvez la carte **Invoice** et sélectionnez son icône d'engrenage (**More Settings**).
3. Ouvrez la section **Purchase Order** pour examiner ses options d'appariement et de validation.

<figure><img src="../../../../../../.gitbook/assets/dbdc226228-invoice-card-en-20261030.png" alt="English Invoice document type card with the More Settings gear at the upper right"><figcaption><p>La carte Invoice dans l'environnement de test Dev anglais actuel. L'icône d'engrenage ouvre More Settings ; les autres contrôles s'appliquent au type de document.</p></figcaption></figure>

<figure><img src="../../../../../../.gitbook/assets/dbdc226-po-section-en-20261030.png" alt="Closed Purchase Order section labelled PO Matching and Validation"><figcaption><p>La section Purchase Order dans More Settings, affichée fermée. Déployez son en-tête pour voir les options ; aucun paramètre n'a été modifié pour cette capture.</p></figcaption></figure>

Commencez par les règles d'appariement et les tolérances, puis ajustez le comportement autour de l'appariement et de l'export :

* [Règles de Correspondance des Bons de Commande](purchase-order-matching-rules.md) et [Paramètres de tolérance de commande d'achat / Tolérance de commande d'achat supplémentaire](purchase-order-tolerance-settings-additional-purchase-order-tolerance.md) définissent la manière dont les lignes de facture et de commande sont comparées.
* [Options de correspondance automatique et d'exportation](auto-match-and-export-options.md), [Export des lignes de commande non appariées](export-not-matched-po-lines.md) et [Exportation alternative](alternate-export.md) couvrent ce qui se passe après un appariement.
* [Quantité exportée dans l'unité de mesure de base](export-quantity-in-base-unit-of-measure.md) convertit la quantité et le prix unitaire exportés dans l'unité de mesure de base, pour l'export vers Infor LN.
* [Tableau PO dans le Constructeur de Mise en Page](po-table-in-layout-builder.md), [Statut de la ligne de commande PO consommée](consumed-po-line-status.md) et [Calculer le prix unitaire de la commande](calculate-po-unit-price.md) modifient ce que les utilisateurs voient dans la vue d'appariement.
* [Vérification automatique des mises à jour de CA](auto-check-for-po-updates.md), [Statuts de commande exclus du rapprochement](purchase-order-disable-statuses.md) et [Mettre à jour le statut de la commande d'achat du document](update-document-purchase-order-status.md) contrôlent la manière dont les données et les statuts de commande restent à jour.
* [Carte des Numéros d'Article Fournisseur - Documentation Administrateur](supplier-item-number-map-admin-documentation.md) et la page générale [Bon de commande](purchase-order.md) apportent un complément de contexte.

Les paramètres peuvent affecter des documents en production. Vérifiez les modifications avec un document de test avant de les enregistrer en production.

Cette vue d'ensemble indique où trouver les paramètres. Elle ne vérifie ni un appariement de commande ni un export terminé.
