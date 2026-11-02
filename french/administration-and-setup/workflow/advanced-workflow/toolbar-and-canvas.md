# Barre d'outils & Canevas

## Vidéo: Constructeur et canevas

Rencontrez Alain et suivez ses explications dans la véritable interface française de DocBits. Il vérifie le tableau de bord, la liste des workflows et la licence, puis ouvre un brouillon non enregistré dans le concepteur. Il nomme le workflow, configure le contrôle du montant et deux actions, dispose les cartes et relie les deux chemins, étape par étape. Il présente ensuite la préparation des tests avec un document ou des données personnalisées. Le compte de démonstration ne dispose pas d’abonnement Advanced Workflow et bloque la validation ; le brouillon reste non enregistré et inactif.

{% embed url="https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/advanced_workflows_canvas-admin/v7/fr.mp4" %}

[Ouvrir la vidéo](https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/advanced_workflows_canvas-admin/v7/fr.mp4) · [Sous-titres (WebVTT)](https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/advanced_workflows_canvas-admin/v7/fr.vtt) · [Transcription (texte)](https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/advanced_workflows_canvas-admin/v7/fr.txt) · 3:37

| Dans cette vidéo | Début |
| --- | --- |
| Présentation de l’administrateur | [0:00](https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/advanced_workflows_canvas-admin/v7/fr.mp4#t=0) |
| Vérifier l’accès | [0:07](https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/advanced_workflows_canvas-admin/v7/fr.mp4#t=7) |
| Nommer le workflow | [0:34](https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/advanced_workflows_canvas-admin/v7/fr.mp4#t=34) |
| Configurer le contrôle du montant | [0:49](https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/advanced_workflows_canvas-admin/v7/fr.mp4#t=49) |
| Ajouter l’action Approval | [1:14](https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/advanced_workflows_canvas-admin/v7/fr.mp4#t=74) |
| Ajouter l’action Standard | [1:36](https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/advanced_workflows_canvas-admin/v7/fr.mp4#t=96) |
| Organiser les cartes | [1:58](https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/advanced_workflows_canvas-admin/v7/fr.mp4#t=118) |
| Relier les chemins | [2:13](https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/advanced_workflows_canvas-admin/v7/fr.mp4#t=133) |
| Préparer les tests | [2:39](https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/advanced_workflows_canvas-admin/v7/fr.mp4#t=159) |
| Valider, enregistrer et activer | [3:05](https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/advanced_workflows_canvas-admin/v7/fr.mp4#t=185) |

<details>
<summary>Transcription</summary>

**Présentation de l’administrateur**

Je m’occupe de DocBits ici. Je vous montre comment créer un contrôle de facture avec deux chemins.

**Vérifier l’accès**

Je commence dans le tableau de bord des workflows et j’ouvre la liste. Ensuite, je vérifie la licence. Workflow et Advanced Workflow doivent tous les deux disposer d’un accès actif. Lorsque ces accès sont actifs, Nouveau workflow propose Advanced Workflow. Ce compte de documentation n’a pas de licence workflow active. Je continue donc avec un aperçu non enregistré dans le concepteur.

**Nommer le workflow**

Je travaille dans le véritable concepteur DocBits. Je donne d’abord un nom clair au brouillon. Nous vérifierons un montant de facture et utiliserons deux actions simples pour montrer les chemins possibles. Cette démonstration reste non enregistrée.

**Configurer le contrôle du montant**

J’ouvre le menu d’ajout et je choisis une carte de condition. Dans la catégorie Champ de document, je sélectionne la condition Docfield. Je renseigne le champ total_amount. Puis je choisis le comparateur supérieur à. Et je saisis mille. Utilisez votre propre identifiant de champ. Un montant égal à mille ne satisfait pas cette comparaison.

**Ajouter l’action Approval**

J’ajoute maintenant une carte d’action de la catégorie Champ de document. Cette action définit la valeur d’un champ du document. J’utilise la clé de démonstration approval_route. Et je saisis la valeur Approval. Cela identifie le chemin. Un véritable processus d’approbation nécessite ses propres actions métier.

**Ajouter l’action Standard**

J’ajoute une deuxième carte avec la même action. Cette action définit la valeur d’un champ du document. J’utilise la clé de démonstration approval_route. Cette fois, le champ de démonstration reçoit la valeur Standard. Les deux cartes sont configurées. Leurs connexions doivent encore déterminer quelle action sera exécutée.

**Organiser les cartes**

Je déplace les cartes pour obtenir une disposition lisible. Les deux actions vont à droite. La condition est au centre et Start à gauche. Déplacer une carte change sa position. Cela ne crée aucune connexion.

**Relier les chemins**

Je relie la sortie de Start à l’entrée de la condition. Le chemin de succès rejoint Approval par une connexion bleue. Le chemin orange de condition non satisfaite rejoint Standard. La sortie rouge d’erreur est distincte et traite les erreurs d’évaluation. Ici, elle reste sans connexion. Dans un workflow de production, définissez comment traiter ces erreurs.

**Préparer les tests**

Le bouton de test dans la barre d’outils ouvre la sélection d’un document de test. Je peux choisir un document de démonstration ou préparer des données personnalisées complètes. Testez des montants supérieurs, inférieurs et égaux à mille. Vérifiez aussi un montant absent. Ce compte n’a pas de licence Advanced Workflow. Je montre la préparation du test, pas un résultat exécuté.

**Valider, enregistrer et activer**

La validation vérifie les connexions et les paramètres des cartes. Ici, l’absence de licence bloque cette validation. Avec un compte autorisé, j’enregistrerais explicitement le workflow sur le serveur. Ensuite, je vérifierais séparément l’activation. L’interrupteur est désactivé avant le premier enregistrement. L’indicateur de brouillon automatique désigne une copie locale du navigateur. Il ne signifie pas que le workflow est enregistré ou activé.

</details>

[Voir les cinq chapitres](../advanced-workflow-videos.md)

La barre d'outils du Workflow Avancé s'étend en bas du canevas et vous donne tout le nécessaire pour construire, naviguer et gérer le flux.

## Commandes de la barre d'outils

- **+ Add** — ouvre le menu de nœud pour ajouter un nœud (voir [Nœuds](nodes.md)).
- **Undo / Redo** — recule ou avance dans vos modifications.
- **Zoom in / Zoom out** — modifie le niveau de zoom du canevas.
- **Workflow name** — nomme le workflow en ligne.
- **Edit description** — ajoute une description au workflow.
- **Variables** — ouvre le panneau [Variables](variables.md).
- **Help** — ouvre la boîte de dialogue des raccourcis clavier et de l'aide.
- **Validate / Test** — vérifie et exécute le flux (voir [Validation & Test](validation-and-testing.md)).
- **Snap to grid** — active ou désactive l'alignement des nœuds sur la grille pour des dispositions soignées.
- **Mini-map** — active ou désactive une petite carte de vue d'ensemble pour naviguer dans les grands graphes.
- **Save** — enregistre le workflow. Un indicateur **auto-save** indique la date du dernier enregistrement automatique du flux.

## Raccourcis clavier

Appuyez sur <kbd>?</kbd> sur le canevas pour ouvrir à tout moment la boîte de dialogue des raccourcis et de l'aide.

<figure><img src="../../../.gitbook/assets/workflow_advanced_shortcuts.png" alt="Boîte de dialogue des raccourcis clavier et de l'aide"><figcaption><p>La boîte de dialogue des raccourcis clavier et de l'aide — raccourcis, mise en évidence du chemin d'exécution et couleurs des connexions.</p></figcaption></figure>

| Raccourci | Action |
|---|---|
| <kbd>Cmd/Ctrl</kbd> + <kbd>S</kbd> | Enregistrer le workflow |
| <kbd>Cmd/Ctrl</kbd> + <kbd>Shift</kbd> + <kbd>V</kbd> | Valider le workflow |
| <kbd>Cmd/Ctrl</kbd> + <kbd>Shift</kbd> + <kbd>T</kbd> | Tester le workflow |
| <kbd>Cmd/Ctrl</kbd> + <kbd>Z</kbd> / <kbd>Shift</kbd> + <kbd>Z</kbd> | Annuler / Rétablir |
| <kbd>Cmd/Ctrl</kbd> + <kbd>C</kbd> / <kbd>V</kbd> / <kbd>D</kbd> | Copier / Coller / Dupliquer les nœuds sélectionnés |
| <kbd>Cmd/Ctrl</kbd> + <kbd>A</kbd> | Sélectionner tous les nœuds |
| <kbd>Shift</kbd> + Glisser | Sélectionner des nœuds (glisser) |
| <kbd>Cmd/Ctrl</kbd> + Clic gauche | Ajouter/retirer un nœud de la sélection |
| Clic droit | Menu d'ajout de nœud |
| <kbd>Del</kbd> | Supprimer le nœud sélectionné |
| <kbd>?</kbd> | Afficher cette aide |

## Étapes suivantes

- Construisez le flux avec les [Nœuds](nodes.md) et les [Variables](variables.md).
