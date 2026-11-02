---
description: "Vérifiez les modifications d’un workflow Standard avec quatre scénarios enregistrés : un cas positif, la limite exacte, un montant inférieur et un autre numéro de facture. Le tutoriel remplace > par ≥, révèle un véritable échec de test et confirme que les quatre cas réussissent à nouveau après correction."
---

# Vérifier les modifications des workflows avec des tests de régression

Vérifiez les modifications d’un workflow Standard avec quatre scénarios enregistrés : un cas positif, la limite exacte, un montant inférieur et un autre numéro de facture. Le tutoriel remplace > par ≥, révèle un véritable échec de test et confirme que les quatre cas réussissent à nouveau après correction.

{% embed url="https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/workflow-regression-admin/v1/fr.mp4" %}

[Regarder avec les sous-titres](https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/workflow-regression-admin/v1/fr.html) · [Ouvrir la vidéo](https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/workflow-regression-admin/v1/fr.mp4) · [Sous-titres (WebVTT)](https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/workflow-regression-admin/v1/fr.vtt) · [Transcription](https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/workflow-regression-admin/v1/fr.txt) · 4:35

## Les quatre cas de test

| Cas | Total (EUR) | Numéro de facture | Statut attendu |
| --- | --- | --- | --- |
| Positif | 1785 | Numéro de formation | En attente d’approbation |
| Limite exacte | 1000 | Numéro de formation | Prêt pour validation |
| Sous la limite | 999 | Numéro de formation | Prêt pour validation |
| Autre facture | 1785 | Numéro différent | Prêt pour validation |

## Procédure dans le gestionnaire de tests

Le workflow de formation reste inactif. Exécutez les quatre scénarios enregistrés individuellement, confirmez le résultat initial, remplacez uniquement > par ≥, conservez les attentes et examinez le cas limite en échec. Rétablissez > puis relancez les quatre cas. Ne modifiez une attente que si le besoin métier a réellement changé.

{% hint style="info" %}
Dans cet exemple, Réussi confirme le statut attendu du document. Vérifiez les autres effets, notamment l’affectation, l’e-mail et l’export, sur le document ou chez le destinataire. Les tests manuels peuvent réellement modifier les données ; utilisez vos propres documents de formation.
{% endhint %}

## Vérifier la règle de départ

Notre règle de formation enregistrée traite les factures portant exactement ce numéro de facture. Le montant total doit être supérieur à mille. Elle passe ensuite le statut à En attente d’approbation. Déclencher les workflows est réglé sur Faux. Pendant cet exercice, la règle reste désactivée dans la liste. Aujourd’hui, je vérifie les effets d’une modification. Il me faut un cas positif et des cas dans lesquels l’action ne doit pas se produire.

## Enregistrer le test positif

Dans le gestionnaire de tests, j’ajoute un scénario et je sélectionne notre règle enregistrée. Son nom décrit le montant et le résultat attendu. Je charge les données d’entrée au format JSON et un second fichier JSON contenant le résultat attendu. La facture de formation a un total de mille sept cent quatre-vingt-cinq euros. Le statut initial est Prêt pour validation. Le statut attendu est En attente d’approbation. Je clique sur Envoyer pour enregistrer ce premier cas.

## Enregistrer le cas à la limite exacte

Je crée ensuite le cas à la limite exacte. Le même numéro de facture, mais exactement mille euros. Supérieur à mille exclut exactement mille. Le résultat attendu conserve donc Prêt pour validation. J’enregistre également ce cas sous un nom distinct.

## Tester une valeur sous la limite

Le troisième cas utilise neuf cent quatre-vingt-dix-neuf euros. Il est sous la limite et attend lui aussi que le statut initial reste inchangé.

## Vérifier la restriction au document de formation

Le quatrième cas dépasse à nouveau mille, mais utilise un autre numéro de facture. Un montant correspondant ne doit pas suffire à déclencher l’action. Les quatre scénarios concernent notre propre document de formation synthétique. Les tests manuels peuvent réellement modifier les documents ; je n’utilise donc pas une facture client en cours.

## Rouvrir les données enregistrées

Avec Modifier, je peux rouvrir les données d’entrée et le résultat attendu d’un scénario enregistré. Je vérifie encore le statut, le numéro de facture et le montant. Le résultat attendu décrit la règle métier. Je ne le modifierai pas simplement pour qu’une règle modifiée repasse au vert.

## Confirmer la situation initiale

Je lance maintenant chacun des quatre cas depuis son propre menu. Ainsi, seuls nos nouveaux scénarios sont exécutés. Je recharge ensuite les résultats. Les quatre affichent une icône verte. Nous disposons maintenant d’une situation initiale confirmée. Dans ce gestionnaire de tests, Réussi concerne le statut attendu du document. Les autres effets, par exemple l’affectation à un utilisateur, doivent aussi être contrôlés sur le document lui-même.

## Effectuer une modification contrôlée

Je change maintenant un seul opérateur : Supérieur à devient Supérieur ou égal à. Le montant reste mille ; toutes les autres conditions et actions restent identiques. J’enregistre la modification et je vérifie à nouveau que la règle de formation est désactivée. Je laisse les résultats attendus inchangés.

## Repérer la régression réelle

Je relance les quatre mêmes cas. Seul le test à mille euros est maintenant rouge ; les trois autres restent verts. Le résultat attendu inchangé révèle la différence, même si les actions s’exécutent correctement sur le plan technique. La fenêtre de détails montre le test échoué et ses données enregistrées. La modification a inclus exactement mille dans la plage correspondante, alors que ce cas doit conserver son statut initial. Je corrige donc la règle. Je ne dois adapter un test échoué à un nouveau résultat attendu que si l’exigence métier a réellement changé.

## Corriger la cause

Dans le workflow, je rétablis la comparaison Supérieur à et j’enregistre. La limite reste mille. Ensuite, je désactive à nouveau la règle de formation dans la liste.

## Réussir à nouveau les quatre cas

Après la correction, je relance les quatre cas. Je vérifie tout le groupe, car une correction pourrait aussi affecter un autre cas. Après rechargement, les quatre résultats sont à nouveau verts. La valeur limite est exclue, le montant positif reste inclus et l’autre numéro de facture reste en dehors de la règle.

## Transmettre la règle testée

Pour finir, je vérifie le workflow de formation désactivé et les quatre résultats enregistrés. Les cas sont prêts pour la prochaine modification. Pour mes propres règles, j’ajoute au besoin d’autres limites métier et des données manquantes. Je peux ainsi vérifier les modifications avec les mêmes attentes explicites.

<details>
<summary>Chapitres et transcription</summary>

| Chapitre | Début |
| --- | --- |
| Je vais modifier un workflow et montrer comment les tests enregistrés permettent de détecter les erreurs. | [0:00](https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/workflow-regression-admin/v1/fr.mp4#t=0.000) |
| Vérifier la règle de départ | [0:07](https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/workflow-regression-admin/v1/fr.mp4#t=7.000) |
| Enregistrer le test positif | [0:35](https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/workflow-regression-admin/v1/fr.mp4#t=35.833) |
| Enregistrer le cas à la limite exacte | [1:07](https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/workflow-regression-admin/v1/fr.mp4#t=67.292) |
| Tester une valeur sous la limite | [1:24](https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/workflow-regression-admin/v1/fr.mp4#t=84.500) |
| Vérifier la restriction au document de formation | [1:34](https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/workflow-regression-admin/v1/fr.mp4#t=94.359) |
| Rouvrir les données enregistrées | [1:54](https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/workflow-regression-admin/v1/fr.mp4#t=114.792) |
| Confirmer la situation initiale | [2:13](https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/workflow-regression-admin/v1/fr.mp4#t=133.542) |
| Effectuer une modification contrôlée | [2:43](https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/workflow-regression-admin/v1/fr.mp4#t=163.875) |
| Repérer la régression réelle | [3:07](https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/workflow-regression-admin/v1/fr.mp4#t=187.542) |
| Corriger la cause | [3:42](https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/workflow-regression-admin/v1/fr.mp4#t=222.500) |
| Réussir à nouveau les quatre cas | [3:53](https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/workflow-regression-admin/v1/fr.mp4#t=233.417) |
| Transmettre la règle testée | [4:15](https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/workflow-regression-admin/v1/fr.mp4#t=255.667) |

Je vais modifier un workflow et montrer comment les tests enregistrés permettent de détecter les erreurs.

[Transcription](https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/workflow-regression-admin/v1/fr.txt)

</details>

## Pages associées

- [Créer et tester un Standard Workflow](standard-workflow-builder.md#standard-workflow-tutorial)
- [Tableau de bord des workflows](workflow-dashboard.md)
