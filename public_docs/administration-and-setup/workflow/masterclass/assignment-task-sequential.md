---
description: "P1 : distinguer affectation, tâche et approbation séquentielle"
---

# P1 : distinguer affectation, tâche et approbation séquentielle

Une **affectation documentaire** définit la responsabilité actuelle. Une **tâche** est un travail distinct. Une **notification** informe. Aucune ne constitue déjà une approbation personnelle. Affecter un groupe ne prouve pas non plus l’accord de chacun de ses membres.

Les cartes séquentielles collectent destinataires et ordre d’approbation. L’exemple utilise A à l’ordre 10 et B à 20. La finalisation examinée commence par la plus petite valeur. Le passage à B suit la décision utilisateur traitée par le circuit d’approbation ; un nœud Wait ne réalise pas ce transfert à lui seul.

Évitez une affectation directe dans la même exécution si vous attendez le premier destinataire séquentiel : la finalisation peut ignorer cette première affectation après une affectation directe du document. Pour les tâches, configurez séparément `task_type`, priorité, destinataire et `send_email`. Désactivez les e-mails pour les exercices.

La recette métier nécessite A→approuver→B→approuver, refus de A, destinataire absent et nouveau déclenchement. Le refus doit empêcher l’export final ; un destinataire non résolu ne doit pas apparaître comme une approbation terminée. Vérifiez séparément responsabilité et tâches. La simulation ne prouve pas un transfert réel entre utilisateurs.

{% embed url="https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/workflow-two-step/v1/fr.mp4" %}

**Vidéo:** Approbation en deux étapes avec des tables de décision · 3:01 · [Sous-titres (WebVTT)](https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/workflow-two-step/v1/fr.vtt)

<details>

<summary>Transcription</summary>

**Deux étapes, deux tables de décision** · [0:00](https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/workflow-two-step/v1/fr.mp4#t=0.25)

Une approbation en deux étapes : d'abord les approbateurs renvoyés par une table de décision, puis un groupe final qui vient toujours en dernier. Deux tables de décision : l'une renvoie des utilisateurs, l'autre un groupe.

**Une chaîne : table, attribution, table, attribution** · [0:14](https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/workflow-two-step/v1/fr.mp4#t=14.283)

Placez chaque carte d'attribution juste après sa propre table de décision, en une seule chaîne : table, attribution, table, attribution. Les deux tables enregistrent leurs retours.

**Chaque attribution juste après sa table** · [0:28](https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/workflow-two-step/v1/fr.mp4#t=28.316)

Un Workflow ne garde que le dernier résultat d'une table de décision. Chaque carte d'attribution le lit quand elle s'exécute : elle doit donc passer avant que la table suivante le remplace.

**Les priorités fixent l'ordre** · [0:40](https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/workflow-two-step/v1/fr.mp4#t=40.216)

L'ordre des approbations vient des priorités, pas de l'ordre des cartes : le plus petit nombre reçoit le document en premier. Donnez au groupe final le nombre le plus élevé.

**Test : approbateurs, puis le groupe** · [0:51](https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/workflow-two-step/v1/fr.mp4#t=51.883)

Le test montre chaque carte en succès. La première carte d'attribution met en file les deux approbateurs, la seconde le groupe final. À la fin de l'exécution, une dernière attribution donne le document au premier d'entre eux.

**Côte à côte : ne fonctionne pas** · [1:19](https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/workflow-two-step/v1/fr.mp4#t=79.916)

Cette disposition ne fonctionne pas. Deux chemins côte à côte semblent identiques, mais le Workflow les exécute étape par étape : d'abord les deux tables, puis les deux cartes d'attribution.

**Approbateurs perdus - sans erreur** · [1:32](https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/workflow-two-step/v1/fr.mp4#t=92.85)

Le test exécute d'abord les deux tables, puis les deux cartes d'attribution. Toutes deux lisent le résultat de la seconde table : le groupe est mis en file deux fois et les approbateurs sont perdus. Chaque carte affiche un succès, rien ne vous avertit. Utilisez la chaîne.

**Un dernier approbateur fixe : priorité 99** · [2:02](https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/workflow-two-step/v1/fr.mp4#t=122.983)

Dans un Workflow Standard, un approbateur fixe peut toujours venir en dernier : attribuez les utilisateurs de la table, puis ajoutez une carte qui attribue un utilisateur avec une priorité élevée, par exemple 99.

**Garder les priorités de la table plus basses** · [2:18](https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/workflow-two-step/v1/fr.mp4#t=138.783)

Les priorités de la table doivent rester inférieures à ce nombre. Si la table ne trouve personne, le Workflow s'arrête à la carte de la table et personne n'est attribué. Un utilisateur renvoyé par les deux est sollicité deux fois.

**Vérifier dans un test** · [2:32](https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/workflow-two-step/v1/fr.mp4#t=152.983)

Un Workflow Standard teste une carte à la fois : testez donc les mêmes cartes dans un Advanced Workflow. La première carte met en file les approbateurs de la table, la seconde ajoute l'utilisateur fixe. Leurs priorités le placent en dernier.

</details>

## Cartes et paramètres d’exemple

Ces valeurs décrivent des paramètres de cartes, pas un workflow complet importable. Remplacez YOUR_* par vos choix de test. Le concepteur gère l’ID caché de l’appelant. Catalogue : Dev, DocFlow 2.10.38, 21 octobre 2026 ; contrôlez versions et droits de votre organisation.

### `action_assign_doc_to_user_sequential` · v2

Identité: `859b2ea5-27a9-41e4-b7f1-3cf8812b9343`

| Paramètre | Type / choix | Exemple |
| --- | --- | --- |
| `user` | `user:int` | `"YOUR_TEST_USER_ID"` |
| `value` | `value:int` | `10` |

### `action_create_task_for_user_sequential` · v2

Identité: `548b3583-6a96-483f-8c66-7871d5b067fa`

| Paramètre | Type / choix | Exemple |
| --- | --- | --- |
| `description` | `description:str` | `"WF-TRAINING-001"` |
| `task_type` | `task / notification` | `"task"` |
| `priority` | `high / medium / low` | `"medium"` |
| `send_email` | `send_email:bool` | `false` |
| `value` | `value:int` | `20` |
| `user` | `user:int` | `"YOUR_TEST_USER_ID"` |
| `title` | `title:str` | `"WF-TRAINING-001"` |

## Cas de test métier

| Cas | Entrée / configuration | Résultat attendu |
| --- | --- | --- |
| ASSIGN-01 | A:10; B:20 | A → Approuver → B → Approuver |
| ASSIGN-02 | A → Refuser | EXPORT=NO |
| ASSIGN-03 | recipient=∅ | Chemin de repli |
| ASSIGN-04 | RUN-1 → RUN-2 | vérifier les doublons |
| ASSIGN-05 | direct + sequential | vérifier le premier destinataire |

## Preuves et limites

Paramètres et comportement ont été confrontés au catalogue Dev et au code examiné. Les cas métier constituent une procédure de recette. Aucune approbation personnelle, modification réelle ou livraison n’a été réalisée pour ce chapitre.

[Poursuivre l’apprentissage](../workflow-learning-path.md) · [Kit de formation](../workflow-training-kit.md)
