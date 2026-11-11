---
description: >-
  Utilisez la carte Modifier le statut en pour qu'un changement de statut ne
  relance pas le même Workflow.
---

# Changer le statut sans relancer votre Workflow

Lorsqu'un document reçoit un nouveau statut, DocBits lance les Workflows prévus pour ce statut. Cela peut inclure le Workflow qui vient de changer le statut. Si ses conditions sont toujours remplies, il s'exécute à nouveau et crée une deuxième tâche ou un deuxième export.

Cette page explique comment configurer votre Workflow pour que chaque document ne le traverse qu'une seule fois.

## Le réglage décisif

La carte [Modifier le statut en](../then/status/change-status-to.md) définit le nouveau statut. Son réglage **Déclencher des flux de travail** décide si ce changement de statut peut lancer des Workflows :

* **Faux :** aucun Workflow n'est lancé. Utilisez cette valeur, sauf si un autre Workflow doit poursuivre le traitement du document.
* **Vrai :** DocBits lance les Workflows dont les conditions correspondent au document avec son nouveau statut. Cela peut inclure le Workflow qui a effectué le changement.

La page de la carte décrit tous les statuts et les versions de la carte.

## Quels Workflows démarrent après un changement de statut

Lorsque **Déclencher des flux de travail** est sur **Vrai**, DocBits examine chaque Workflow actif et vérifie ses conditions sur le type et le statut du document, par exemple une carte **Le statut du document**. Un Workflow démarre si le document, avec son nouveau statut, y correspond.

Un Workflow qui ne vérifie pas le statut correspond à **tous** les statuts. S'il change lui-même le statut, le nouveau statut le relance donc.

Donner à un document le statut qu'il a déjà n'a aucun effet : le statut reste le même et aucun Workflow ne démarre.

## Exemple : une exécution ou deux

La règle : une fois que votre Workflow a fait son travail, ses propres conditions ne doivent plus être remplies.

<figure><img src="../../../.gitbook/assets/status-change-runs-once-vs-twice-fr.png" alt="Deux workflows, tous deux avec Déclencher des flux de travail sur Vrai. À gauche : la condition vérifie que le type est Facture et que le statut est Prêt pour la validation. Après le passage à Validé en attente d'approbation, la condition n'est plus remplie, le workflow n'est pas relancé, résultat 1 tâche. À droite : la condition vérifie seulement que le type est Facture. Le nouveau statut lance le workflow une deuxième fois ; il crée une deuxième tâche et définit à nouveau Validé en attente d'approbation, ce qui ne change rien. Résultat 2 tâches." width="800"><figcaption><p>Le même workflow avec et sans condition sur le statut</p></figcaption></figure>

À droite, le Workflow s'exécute une deuxième fois et crée une tâche en double. Il s'arrête là uniquement parce que le deuxième changement de statut définit un statut que le document a déjà.

**Deux Workflows peuvent se lancer mutuellement.** Si un Workflow définit **Validé en attente d'approbation** et qu'un autre remet le document sur **Prêt pour la validation**, tous deux avec **Vrai**, ils se relancent sans cesse. Donnez à chaque Workflow une condition sur le statut de départ et n'utilisez **Vrai** que là où c'est nécessaire.

## Configuration pas à pas

1. **Utilisez la version 3 de Modifier le statut en.** Les versions antérieures n'ont pas de réglage **Déclencher des flux de travail** (voir [Versions de la carte](../then/status/change-status-to.md#versions-de-la-carte)).
2. **Vérifiez le statut de départ.** Ajoutez la carte **Et** **Le statut du document** (sous **Et → Statut**) et réglez-la sur **Est** **Prêt pour la validation**. Voir [Condition de statut de document unique](../and/status/single-document-status-condition.md). Si le statut seul ne permet pas de savoir si l'étape est terminée, vérifiez aussi un champ que votre Workflow remplit une fois son travail fait.
3. **Ajoutez l'action**, par exemple créer une tâche ou exporter le document.
4. **Ajoutez Modifier le statut en** et choisissez le statut suivant, par exemple **Validé en attente d'approbation**.
5. **Choisissez la valeur de Déclencher des flux de travail.** Commencez par **Faux**. Choisissez **Vrai** uniquement si un autre Workflow doit poursuivre avec le nouveau statut.
6. **Essayez avec un vrai document.** Vérifiez qu'une seule tâche ou un seul export a été créé et que le document a bien le nouveau statut.

{% hint style="info" %}
Les tests dans le concepteur de Workflows ne font que simuler le changement de statut. Le statut n'est pas enregistré et aucun autre Workflow ne démarre. Pour voir le comportement réel, utilisez un vrai document.
{% endhint %}

## Protection intégrée

DocBits limite les dégâts lorsque des Workflows se relancent mutuellement encore et encore :

* **Une seule exécution de Workflow à la fois par document.** Les exécutions pour un même document s'attendent les unes les autres, et chaque exécution voit le document tel que la précédente l'a laissé.
* **Limite d'exécutions.** Par défaut, un même Workflow s'exécute au maximum 50 fois sur un document. Au-delà, DocBits ne le lance plus pour ce document.

Ces limites finissent par arrêter la répétition, mais de nombreuses tâches ou de nombreux exports peuvent déjà exister à ce moment-là. C'est une condition sur le statut qui l'empêche. Si un doublon pose un vrai problème, vérifiez aussi son existence avant d'agir, par exemple si une tâche ouverte existe déjà pour le document.

## Voir aussi

* [Modifier le statut en](../then/status/change-status-to.md) : la carte, ses statuts et ses versions
* [Condition de statut de document unique](../and/status/single-document-status-condition.md) : vérifier le statut du document dans une condition
* [Quand mon workflow s’exécute-t-il ?](../workflow-execution-model.md)
* [Vue d'ensemble du parcours d'apprentissage](../workflow-learning-path.md)
