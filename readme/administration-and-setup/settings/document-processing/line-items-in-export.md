# Éléments de ligne dans l'exportation

Ce qu'il advient du tableau des éléments de ligne lorsqu'un document est approuvé et exporté dépend de la méthode d'exportation. Cette page explique quelles colonnes quittent DocBits, lesquelles sont obligatoires, et pourquoi une exportation peut contenir moins de lignes que l'écran de validation.

## Deux types d'exportation

| Méthode d'exportation | Ce qui est envoyé pour le tableau |
|---|---|
| **webhook**, **watcher**, **sftp**, **infor_sftp** (JSON / XML) | Le tableau tel qu'il apparaît sur l'écran de validation : chaque [colonne de tableau](../global-settings/document-types/table-columns.md) non masquée de chaque ligne, avec la valeur, la valeur formatée et le niveau de confiance. |
| **infor-m3-cloud**, **infor-m3-toml-cloud**, **infor-idm-***, **infor-gls840-onpremise**, **infor-m3-oc-charges-onpremise** (BOD Infor ERP / SAP) | Pas le tableau brut. DocBits en construit des **lignes de réception** et des **lignes de coût** (voir ci-dessous) et les mappe sur les champs du BOD avec le mappage configuré sous [Exportation vers INFOR](../../../infor-integration-and-configuration/exporting-to-infor/README.md). |

## Lignes de réception et lignes de coût (exportations Infor)

Une ligne de facture ERP est soit une **ligne de réception**, qui solde une réception de bon de commande, soit une **ligne de coût**, qui impute un montant à un compte du grand livre avec des dimensions. DocBits décide pour chaque ligne de facture :

* Les **lignes de réception** proviennent de la **correspondance de bon de commande**. Chaque ligne de facture qui a été rapprochée d'une ligne de bon de commande (Tableau de bord → Correspondance de bon de commande, ou automatiquement avec la *correspondance automatique de bon de commande*) devient une ligne de réception portant le numéro de bon de commande, la ligne de bon de commande, la ligne de réception ainsi que la quantité et le montant rapprochés. Une facture sans correspondance de bon de commande n'a **aucune ligne de réception** ; l'aperçu d'exportation affiche alors `receipt_lines: []`, ce qui est correct et non un bug.
* Les **lignes de coût** proviennent de l'**enregistrement comptable** que crée l'étape de comptabilité analytique (ou la comptabilité automatique) : compte du grand livre, dimensions, montant, quantité par ligne. Une facture sans enregistrement comptable n'a pas de lignes de coût.
* Les **lignes de taxe** sont construites à partir des montants de taxe de l'en-tête, pas à partir du tableau.

Pour les exportations Infor, le tableau des éléments de ligne est donc l'*entrée* de la correspondance de bon de commande et de la comptabilité ; ce que l'ERP reçoit est le résultat de ces deux étapes. Une ligne qui n'est ni rapprochée d'un bon de commande ni comptabilisée n'atteint pas l'ERP.

{% hint style="warning" %}
Pour que la correspondance de bon de commande fonctionne, le tableau doit comporter les colonnes par défaut **numéro d'article, prix unitaire, quantité et montant total**. Si l'une d'elles est masquée, l'écran de validation affiche *Line Item Table is missing Mandatory column for PO* et aucune ligne de réception ne peut être construite.
{% endhint %}

## Colonnes obligatoires et boîte de dialogue d'approbation

Avant qu'un document puisse être approuvé, DocBits contrôle le tableau :

1. Chaque colonne marquée **Obligatoire** (Paramètres → Types de documents → Colonnes de tableau) doit avoir une valeur dans chaque ligne.
2. Chaque ligne doit passer le **contrôle du total de ligne** : `total = quantité × prix unitaire + frais − remise`, à 0,02 près. Les lignes en échec sont marquées ; le message indique la valeur attendue et la valeur réelle.
3. La **somme des totaux de ligne** est comparée au montant net de l'en-tête. Un écart est un avertissement et ne bloque pas l'approbation.

La boîte de dialogue d'approbation liste ce qui manque encore. Un administrateur peut désactiver tous les contrôles de tableau par type de document avec **Ignorer la validation du tableau** (Types de documents → Plus de paramètres) ; les totaux de ligne et les colonnes obligatoires ne sont alors plus contrôlés, les contrôles d'en-tête restent actifs.

Détail des messages : [Dépannage de l'extraction de table](../../../overview-and-basics/faq/document-processing/table-extraction-troubleshoot.md), section « Messages sur le tableau ».

## Tableau vide

* Les **exportations JSON / XML** envoient le document avec `tables: []` (ou le tableau avec zéro ligne). Le système destinataire doit savoir traiter un tableau vide.
* Les **exportations Infor** sans lignes de réception ni lignes de coût n'envoient que l'en-tête et les lignes de taxe. La plupart des ERP rejettent une facture sans lignes : configurez la comptabilité automatique ou une ligne de coût par défaut pour ces types de document, ou dirigez-les vers une autre exportation.
* Un type de document **sans tableau** (aucun tableau configuré) n'envoie jamais de données de lignes ; c'est le comportement attendu pour des types de document tels que les confirmations de commande, rapprochées au niveau de l'en-tête.

## Vérifier avant d'approuver

Les partenaires et le support disposant d'un accès API ou MCP peuvent demander la charge utile d'exportation d'un document avant son envoi : l'outil MCP `get_export_preview(doc_id)` renvoie exactement ce que l'exportation enverra, `receipt_lines`, `cost_lines` et `tax_lines` pour les exportations Infor, `tables` pour les exportations JSON. Utilisez-le lorsque l'ERP signale des lignes manquantes : si `receipt_lines` est vide, la facture n'a pas été rapprochée d'un bon de commande ; si `cost_lines` est vide, aucun enregistrement comptable n'existe.

## Pages associées

* [Exportation](export.md) : configurations et méthodes d'exportation
* [Colonnes de Tableau](../global-settings/document-types/table-columns.md)
* [Exportation vers INFOR](../../../infor-integration-and-configuration/exporting-to-infor/README.md) : mappages des champs BOD pour les lignes de réception, de coût et de taxe
