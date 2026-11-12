# Bon de commande

## Aperçu

Ce paramètre active la section [**Purchase Order Matching**](../../../../../../end-user-and-partner-section/end-user-section/purchase-order-matching/), qui devient accessible après la validation du document.

<mark style="color:red;">**Remarque**</mark>: Pour le type de document **Invoice**, les exigences supplémentaires suivantes doivent être respectées :

* Le paramètre **Purchase Order** doit être activé (comme décrit sur cette page)
* La facture doit être de type **Purchase Invoice**
* Un **Extracted Table** doit être présent

## Étapes d'activation <a href="#activation-steps" id="activation-steps"></a>

1. Allez dans **Settings → Document Types**.
2. Repérez la carte du type de document et cliquez sur l'engrenage (**More Settings**).
3. Dépliez la section **Purchase Order** et activez **Purchase Order**.

<figure><img src="../../../../../../.gitbook/assets/po-settings-purchase-order-fr-20261031.png" alt="More Settings du type de document Invoice avec la section Purchase Order ouverte"><figcaption><p>La section <strong>Purchase Order</strong> dans <strong>More Settings</strong>. Le premier interrupteur active l'appariement des bons de commande pour le type de document, les interrupteurs suivants l'affinent.</p></figcaption></figure>

## **Fonctionnalité**

Une fois le paramètre activé, la section [**Purchase Order Matching**](../../../../../../end-user-and-partner-section/end-user-section/purchase-order-matching/) est disponible après la validation du document.

### Quelle quantité est comparée

La quantité de la commande que l'appariement compare dépend de **PO match server side** :

* **PO match server side off** – une liste **Match quantity** s'affiche à côté de l'interrupteur **Purchase Order**. Choisissez **Quantity**, **Received Quantity** ou **Received Delivery Open Quantity**. DocBits compare la quantité choisie avec son propre moteur d'appariement.
* **PO match server side on** – l'appariement suit le jeu de règles du type de document et **Match quantity** fait partie de ces règles. La ligne d'en-tête de la section affiche alors le lien **Configure PO matching rules**, qui ouvre les règles. Voir [Purchase Order Matching Rules](purchase-order-matching-rules.md).

{% hint style="info" %}
La capture ci-dessus a été prise avec **PO match server side** activé : la liste **Match quantity** n'y figure donc pas, elle se règle dans les règles d'appariement.
{% endhint %}

### Paiement anticipé avant réception des marchandises

Certaines factures arrivent avant les marchandises. Pour apparier une telle facture sur la quantité commandée plutôt que sur la quantité reçue, activez **Allow pre-payment before goods receipt** dans la même section.

L'interrupteur n'apparaît que si les trois conditions suivantes sont réunies :

* le type de document est **Invoice**,
* **Purchase Order** est activé,
* et la quantité appariée est **Received Quantity**.

Si vous remplacez la quantité appariée par une autre valeur, l'interrupteur disparaît des paramètres. Sur l'[PO matching screen](../../../../../../end-user-and-partner-section/end-user-section/purchase-order-matching/), **Match as pre-payment** apparaît alors sous **Use Lines Net Amount for Matched Total**, avec l'indication *Match on ordered quantity instead of received quantity*. L'interrupteur est grisé et accompagné d'une note lorsque le fournisseur ne peut pas être facturé avant la réception des marchandises dans l'ERP.

Tant que l'interrupteur est activé, l'écran lit la quantité commandée, et non la quantité reçue, pour les liaisons manuelles et pour le total apparié. Le choix est enregistré sur le document et **Auto Match** s'exécute à nouveau ; si cet appariement échoue, le choix revient à sa valeur précédente.
