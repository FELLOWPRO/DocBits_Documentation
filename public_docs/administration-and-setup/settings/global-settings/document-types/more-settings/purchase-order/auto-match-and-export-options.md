# Options de correspondance automatique et d'exportation

Trois paramètres à la fin de la carte **Bon de commande** déterminent qui voit les raccourcis de correspondance des BC et quels documents peuvent être exportés automatiquement après une correspondance. Ils s'appliquent à un type de document à la fois.

<figure><img src="../../../../../../.gitbook/assets/doc-type-settings-po-options-fr.png" alt="La carte Bon de commande des paramètres du type de document avec toutes les options de BC"><figcaption><p>La carte Bon de commande. Les trois options ci-dessous sont les trois dernières lignes.</p></figcaption></figure>

## Autoriser l'exportation automatique pour les lignes de commande non comparables

L'exportation automatique après la correspondance des BC exige normalement un document **entièrement apparié**. Lorsque cet interrupteur est activé, les documents dont le statut est **Pas de lignes de po compatibles** peuvent aussi être exportés automatiquement. Ce statut signifie que le bon de commande ne contient aucune ligne à laquelle la facture peut être appariée.

* **Désactivé (par défaut) :** seuls les documents entièrement appariés sont exportés automatiquement.
* **Activé :** les documents entièrement appariés et les documents sans lignes de BC pouvant être appariées sont exportés automatiquement.

L'interrupteur n'a d'effet que lorsque des documents sont exportés automatiquement, par exemple avec [**Correspondance et exportation automatiques des bons de commande 100%**](../../../../document-processing/module/auto-export-if-po-matched-100.md) ou une carte d'exportation DocFlow. Il ne modifie pas la façon dont les lignes sont appariées.

## Correspondance automatique et exportation visibles pour

L'écran de correspondance des BC propose une action **Correspondance automatique et exportation**. Elle apparie le document et l'exporte juste après la correspondance. Ce paramètre détermine qui obtient cette action :

| Valeur | Qui voit l'action |
| ------ | ----------------- |
| **Seul l'administrateur** (par défaut) | Les administrateurs |
| **Tous les utilisateurs** | Chaque utilisateur qui peut ouvrir l'écran de correspondance des BC |

Les administrateurs voient toujours l'action. Le paramètre n'active pas la fonctionnalité. Le module [**Correspondance et exportation automatiques des bons de commande 100%**](../../../../document-processing/module/auto-export-if-po-matched-100.md) doit être actif pour l'organisation.

## Utilisez le montant net des lignes pour le total correspondant visible à

L'écran de correspondance des BC peut calculer le **Total correspondant** à partir du **Montant net** des lignes de facture appariées au lieu de le calculer autrement. Ce paramètre détermine qui peut activer ce calcul :

| Valeur | Qui voit l'interrupteur |
| ------ | ----------------------- |
| **Seul l'administrateur** (par défaut) | Les administrateurs |
| **Tous les utilisateurs** | Chaque utilisateur qui peut ouvrir l'écran de correspondance des BC |

Lorsque l'interrupteur est activé, le Total correspondant utilise directement les valeurs du Montant net des lignes de facture appariées.
