# Définir le signe négatif pour les avoirs

### Aperçu

Le paramètre **Définir le signe négatif pour les avoirs** (Set Negative Sign for Credit Notes) garantit que les **avoirs** (notes de crédit) sont enregistrés avec des **montants négatifs**. Un avoir annule ou rembourse une partie d'une facture ; en comptabilité, ses valeurs doivent donc réduire les totaux, c'est-à-dire être négatives. Lorsque ce paramètre est activé, DocBits applique automatiquement ce signe négatif.

Ce paramètre est **activé par défaut**.

### Que fait ce paramètre ?

Lorsqu'un document est reconnu comme un **avoir**, DocBits convertit automatiquement ses montants en valeurs négatives lors du traitement. Cela concerne les champs monétaires, notamment les montants nets, les montants de taxe et les totaux (par exemple montant net, montant de taxe, montant total de taxe, montant net total et montant total).

* **Activé (par défaut)** — Les montants des avoirs sont enregistrés en valeurs négatives (par exemple, `150,00` devient `-150,00`). Les factures normales ne sont pas affectées.
* **Désactivé** — Les montants restent exactement tels qu'ils ont été lus dans le document, sans changement de signe.

{% hint style="info" %}
Cela ne s'applique qu'aux documents identifiés comme des **avoirs**. Les factures normales restent toujours inchangées.
{% endhint %}

### Avantages

* **Comptabilité correcte** : Les avoirs réduisent les soldes, donc les valeurs négatives correspondent à ce qu'attendent vos systèmes comptables et ERP.
* **Aucune modification manuelle** : Votre équipe n'a pas à inverser le signe à la main sur chaque avoir.
* **Cohérence** : Chaque avoir est traité de la même manière dans toute votre organisation.

### Utilisation

1. Allez dans **Paramètres**.
2. Sélectionnez **Traitement des documents**.
3. Sélectionnez **Module**.
4. Ouvrez la section **Type de document**.
5. Repérez **Définir le signe négatif pour les avoirs** et activez ou désactivez le commutateur.

### Quand utiliser cette fonction

* **Laissez-le activé** si votre système comptable ou ERP attend que les avoirs arrivent avec des montants négatifs (c'est la configuration la plus courante).
* **Désactivez-le** uniquement si votre système en aval gère déjà le signe lui-même ou attend que les montants des avoirs restent positifs.
