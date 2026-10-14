# Calculer le prix unitaire du bon de commande

## **Présentation**

Vous pouvez choisir de calculer automatiquement le **prix unitaire** de chaque ligne de bon de commande à partir du **montant** et de la **quantité** de la ligne, au lieu d’utiliser le prix unitaire fourni avec le bon de commande. Cela est particulièrement utile lorsque le prix unitaire dans le bon de commande (dans Infor ERP / SAP) diffère du prix sur le document. De telles divergences peuvent survenir si une remise est appliquée au prix unitaire dans le bon de commande, tandis que le document applique uniquement la remise au montant net.

## **Étapes d’activation**

1.  Naviguez vers **Paramètres** -> **Paramètres globaux** -> **Types de documents**.

    <figure><img src="../../../../../../.gitbook/assets/Calculate_PO_unit_price_1.png" alt=""><figcaption></figcaption></figure>
2.  Sélectionnez le type de document souhaité et cliquez sur **Paramètres avancés**.

    <figure><img src="../../../../../../.gitbook/assets/Calculate_PO_unit_price_2.png" alt=""><figcaption></figcaption></figure>
3.  Dans la section **Bon de commande**, activez l’option **Calculer le prix unitaire du BC**.

    <figure><img src="../../../../../../.gitbook/assets/Calculate_PO_unit_price_3.png" alt=""><figcaption></figcaption></figure>

## Comment le prix est calculé

Une fois le paramètre activé, le prix unitaire d’une ligne de bon de commande est calculé comme suit :

**`Prix unitaire = Montant de la ligne ÷ Quantité × Prix unitaire par`**

où le **montant de la ligne** est choisi ainsi :

| La ligne de bon de commande contient                                                          | Montant de la ligne utilisé             |
| -------------------------------------------------------------------------------------------- | -------------------------------------- |
| un **montant net** (`extended_amount`) supérieur à 0 et ne dépassant pas le total de la ligne | le montant net                         |
| pas de montant net, ou un montant net supérieur au total de la ligne                          | le **total** de la ligne (`total_amount`) |
| aucun montant positif, ou aucune quantité positive                                           | rien n’est calculé, le prix du BC reste |

Pourquoi le montant net est prioritaire : les flux ERP (Infor BODs) envoient le montant net de la ligne sous `extended_amount` et incluent **les taxes et charges en supplément** dans `total_amount`. Diviser un total taxé par la quantité donne un prix unitaire brut, et toute facture dont le prix est net apparaît alors comme un _prix unitaire sous-évalué_ bien que correct. Exemple d’une vraie ligne de bon de commande : quantité 9, montant net 879,84, total 954,63 (8,5 % de taxe) — le prix basé sur le net est 97,76 et correspond à la facture ; le prix basé sur le total serait 106,07.

Un montant net qui est **plus élevé** que le total de la ligne ne peut pas être un montant net, donc le total est utilisé dans ce cas. Un `Prix unitaire par` de 0 ou vide est considéré comme 1.

{% hint style="info" %}
Le prix calculé est écrit dans la capture d’écran du bon de commande stockée sur le document, et il est **recalculé à chaque fois que le document est apparié** (appariement automatique du BC, appariement manuel, appariement à l’enregistrement). Un document apparié avant la modification du paramètre adopte donc le nouveau prix lors de son prochain appariement — aucun rechargement du bon de commande n’est nécessaire.
{% endhint %}

## Exemple :

<figure><img src="../../../../../../.gitbook/assets/Calculate_PO_unit_price_4.png" alt="" width="563"><figcaption></figcaption></figure>

Dans ce cas, le prix unitaire (sans la remise) est extrait du document, tandis que le bon de commande dans l’ERP stocke le prix unitaire avec la remise appliquée. Cela entraîne une discordance dans le prix unitaire. Avec le paramètre activé, le prix unitaire est pris à partir du montant de la ligne et de la quantité, de sorte que les deux parties concordent.

## Paramètres associés

* [Règles d’appariement des bons de commande](purchase-order-matching-rules.md) — les règles comparent le prix unitaire **effectif**, qui est ce prix calculé lorsque le paramètre est activé.
* [Paramètres de tolérance des bons de commande](purchase-order-tolerance-settings-additional-purchase-order-tolerance.md) — la marge de déviation possible entre le prix de la facture et le prix calculé.