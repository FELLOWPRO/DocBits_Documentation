# Modifications des adresses web

Les adresses web (URL) que vous utilisez pour accéder aux pages de DocBits ont été nettoyées et harmonisées. Cette page explique ce qui a changé, pourquoi vos anciens liens fonctionnent toujours et comment retrouver n'importe quelle page grâce à sa nouvelle adresse.

## Ce qui a changé

Les adresses web de DocBits suivent désormais un schéma clair : l'élément sur lequel vous travaillez vient en premier, suivi de la vue correspondante. Par exemple, l'écran de validation d'un document est désormais :

```
/documents/<document-id>/validation
```

au lieu de l'ancienne adresse :

```
/field_validation_v1/<document-id>
```

Au fil du temps, certains écrans se sont retrouvés avec plusieurs versions et adresses différentes. Par exemple, l'approbation disposait d'adresses distinctes pour la première approbation, la deuxième approbation et les anciennes versions de chacune. Ces écrans partagent désormais une seule adresse, et DocBits affiche automatiquement la bonne version pour votre organisation. Vous n'avez plus besoin de savoir, ni de deviner, quelle version s'applique à vous.

Les adresses utilisent également des mots en minuscules séparés uniquement par des traits d'union, au lieu d'un mélange de tirets bas, de majuscules et d'abréviations.

## Vos anciens liens fonctionnent toujours

Vous n'avez rien à modifier immédiatement. Les favoris, les liens enregistrés dans des e-mails et ceux conservés ailleurs continuent de fonctionner exactement comme avant. Lorsque vous ouvrez une ancienne adresse, DocBits vous redirige automatiquement vers la nouvelle, y compris avec les filtres ou options qui faisaient partie du lien d'origine.

Après la redirection, la barre d'adresse du navigateur affiche la nouvelle adresse. C'est normal : cela signifie que la redirection a fonctionné. Avec le temps, nous vous recommandons de mettre à jour vos favoris afin qu'ils pointent directement vers les nouvelles adresses, pour y accéder sans l'étape de redirection supplémentaire. Il n'y a cependant aucune échéance : les anciennes adresses continueront de fonctionner.

## Trouver une page

Si vous ne savez pas quelle est la nouvelle adresse d'une page, ou si vous souhaitez simplement accéder directement à un élément, vous disposez de trois moyens pour vous repérer :

* **Plan du site.** La page [Sitemap](sitemap.md) répertorie toutes les pages de DocBits, regroupées par domaine, avec un champ de recherche et des filtres. Ouvrez-la depuis la barre latérale, ou depuis la recherche rapide globale en choisissant **View all results**.
* **Recherche rapide globale.** Appuyez sur <kbd>Cmd</kbd> + <kbd>K</kbd> sur Mac ou sur <kbd>Ctrl</kbd> + <kbd>K</kbd> sous Windows, depuis n'importe où dans DocBits, puis saisissez le nom de ce que vous cherchez. Consultez [Global Quick Search](global-quick-search.md) pour plus de détails.
* **L'écran « page introuvable ».** Si vous saisissez ou collez uniquement le début d'une adresse, par exemple `/documents` ou `/analytics`, sans le reste, DocBits affiche un écran « page introuvable » qui répertorie toutes les pages situées sous cette adresse. Il fonctionne comme un index pour ce groupe de pages et propose le même champ de recherche que la recherche rapide globale : vous pouvez donc aussi y effectuer vos recherches.

## Anciennes et nouvelles adresses

Le tableau ci-dessous répertorie toutes les adresses qui ont changé, regroupées par domaine. Lorsque plusieurs anciennes adresses mènent désormais à la même nouvelle adresse, chaque ancienne adresse figure sur sa propre ligne. Les adresses utilisées uniquement par les développeurs (par exemple les pages de débogage ou de démonstration) ne sont pas répertoriées, car elles n'ont aucune incidence sur l'utilisation quotidienne.

Les espaces réservés du tableau représentent des valeurs réelles :

* `<document-id>` : l'ID d'un document
* `<task-id>` : l'ID d'une tâche
* `<workflow-id>` : l'ID d'un workflow
* `<document-type>` : un type de document, tel qu'une facture ou un bon de commande
* `<file-name>` : un nom de fichier
* `<order-number>` / `<sales-order-id>` : une référence de commande d'achat ou de vente
* `<organisation-id>` : un ID d'organisation
* `<layout-type>` : un type de mise en page
* `<supplier-id>` : l'ID d'un fournisseur
* `<page>` : un numéro de page

### Documents

| Ancienne adresse | Nouvelle adresse |
|---|---|
| `/document/<document-id>` | `/documents/<document-id>` |
| `/field_validation_v1/<document-id>` | `/documents/<document-id>/validation` |
| `/field_validation/<document-id>` | `/documents/<document-id>/validation` |
| `/medi_order_v3/<document-id>` | `/documents/<document-id>/validation` |
| `/ready_for_approval_v3/<document-id>` | `/documents/<document-id>/approval` |
| `/ready-for-approval-v2/<document-id>` | `/documents/<document-id>/approval` |
| `/ready-for-approval/<document-id>` | `/documents/<document-id>/approval` |
| `/ready-for-second-approval-v3/<document-id>` | `/documents/<document-id>/approval` |
| `/ready-for-second-approval-v2/<document-id>` | `/documents/<document-id>/approval` |
| `/ready-for-second-approval/<document-id>` | `/documents/<document-id>/approval` |
| `/in_review/<document-id>` | `/documents/<document-id>/review` |
| `/in-review-v2/<document-id>` | `/documents/<document-id>/review` |
| `/rejected/<document-id>` | `/documents/<document-id>/rejected` |
| `/summary/<document-id>` | `/documents/<document-id>/summary` |
| `/tbl_ext_v3/<document-id>` | `/documents/<document-id>/table-extraction` |
| `/tbl_training/<document-id>` | `/documents/<document-id>/table-training` |
| `/table_train_v3` | `/table-training` |
| `/doc_flow/<document-id>` | `/documents/<document-id>/flow` |
| `/document_pdf/<file-name>/<document-id>` | `/documents/<document-id>/pdf/<file-name>` |
| `/document_error/<document-id>` | `/documents/<document-id>/error` |
| `/document_classifiy/<document-id>` | `/documents/<document-id>/classify` |
| `/accounting/<document-id>` | `/documents/<document-id>/accounting` |
| `/quote-details/<document-id>` | `/documents/<document-id>/quote` |
| `/vertex-details/<document-id>` | `/documents/<document-id>/vertex` |
| `/po-matching/<document-id>` | `/documents/<document-id>/po-matching` |
| `/po-matching-v3/<document-id>` | `/documents/<document-id>/po-matching-v3` |
| `/ocr-document/<document-id>/<page>` | `/documents/<document-id>/ocr/<page>` |
| `/fields_sep_comp_v3/<document-id>` | `/documents/<document-id>/window/medi-fields` |
| `/simple_fields_comp/<document-id>` | `/documents/<document-id>/window/fields` |
| `/show_pdf/<document-id>` | `/documents/<document-id>/window/pdf` |

### Tâches

| Ancienne adresse | Nouvelle adresse |
|---|---|
| `/task/<task-id>` | `/tasks/<task-id>` |

### Workflows

| Ancienne adresse | Nouvelle adresse |
|---|---|
| `/workflowsdashboard` | `/workflows` |
| `/my_workflow/<document-type>/<workflow-id>` | `/workflows/my/<document-type>/<workflow-id>` |
| `/workflow_designer/<workflow-id>` | `/workflows/designer/<workflow-id>` |
| `/advanced_workflow_designer/<workflow-id>` | `/workflows/advanced-designer/<workflow-id>` |
| `/workflow_logs/<workflow-id>` | `/workflows/logs/<workflow-id>` |
| `/template_designer/<workflow-id>` | `/workflows/templates/<workflow-id>` |
| `/flow` | `/workflows/flow` |

### Commandes et factures

| Ancienne adresse | Nouvelle adresse |
|---|---|
| `/purchase-order` | `/supplier/purchase-orders` |
| `/purchase-order-detail/<order-number>` | `/supplier/purchase-orders/<order-number>` |
| `/sales_order_detail/<sales-order-id>` | `/sales-orders/<sales-order-id>` |
| `/asn_shipment` | `/shipments/asn` |
| `/asn_shipment/dashboard` | `/shipments/asn` |
| `/shipment-order` | `/shipments/orders` |
| `/invoice/dashboard` | `/invoices` |
| `/invoice/details/<document-id>` | `/invoices/<document-id>` |
| `/accounting_range` | `/accounting/range` |

### Analyses et recherche

| Ancienne adresse | Nouvelle adresse |
|---|---|
| `/analytics-dashboard` | `/analytics` |
| `/report` | `/analytics/reports` |
| `/performance_report` | `/analytics/performance` |
| `/touchless-intelligence/supplier/<supplier-id>` | `/analytics/touchless/suppliers/<supplier-id>` |
| `/touchless-intelligence/document/<document-id>/trace` | `/analytics/touchless/documents/<document-id>/trace` |
| `/supplier-statistic` | `/analytics/suppliers` |
| `/graph-explorer` | `/analytics/graph-explorer` |
| `/full-search` | `/search` |

### Liens partagés

| Ancienne adresse | Nouvelle adresse |
|---|---|
| `/status/<document-id>` | `/share/documents/<document-id>/status` |
| `/sales_order_detail/<sales-order-id>/share` | `/share/sales-orders/<sales-order-id>` |
| `/supplier_invoice/share/get_details` | `/share/supplier-invoice` |

### Compte et connexion

| Ancienne adresse | Nouvelle adresse |
|---|---|
| `/register` | `/auth/register` |
| `/register-success` | `/auth/register-success` |
| `/verify-email` | `/auth/verify-email` |
| `/forget-password` | `/auth/forgot-password` |
| `/reset-password` | `/auth/reset-password` |
| `/set-password` | `/auth/set-password` |
| `/supplier/register/terms_and_conditions/<organisation-id>` | `/supplier/register/terms-and-conditions/<organisation-id>` |

### Mises en page

| Ancienne adresse | Nouvelle adresse |
|---|---|
| `/layout-builder/<document-type>/<layout-type>` | `/layouts/builder/<document-type>/<layout-type>` |
| `/manage_layout_builder/<document-type>` | `/layouts/builder/<document-type>` |
| `/manage_approval_layout_builder_v2/<document-type>/<layout-type>` | `/layouts/builder/<document-type>/<layout-type>` |
| `/vertex_layout_builder/<document-type>/<layout-type>` | `/layouts/builder/<document-type>/<layout-type>` |
| `/manage_approval_layout_builder/<document-type>/<layout-type>` | `/layouts/builder/<document-type>/<layout-type>` |
