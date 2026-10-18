# Barre d'outils & Canevas

## Vidéo: Constructeur et canevas

{% embed url="https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/advanced_workflows_canvas/v2/fr.mp4" %}

[Sous-titres (WebVTT)](https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/advanced_workflows_canvas/v2/fr.vtt) · 1:52

<details>
<summary>Transcription</summary>

**Une facture, deux chemins**

Voici un véritable workflow avancé dans DocBits. Un contrôle du montant de la facture mène à deux actions. Les connexions déterminent l’action exécutée. Cet exemple utilise un brouillon non enregistré et des champs de démonstration.

**Configurer le contrôle du montant**

Ouvrez Ajouter, choisissez And et sélectionnez une condition de champ du document. Indiquez le champ du montant, choisissez Supérieur à et saisissez mille. Utilisez la clé exacte du champ définie dans votre configuration documentaire.

**Configurer les actions**

Ajoutez deux cartes Then. Chacune renseigne le champ de démonstration approval route. L’une écrit Approval, l’autre Standard. Ces valeurs identifient le chemin. Configurez vos actions métier pour un workflow de production.

**Relier les sorties**

Reliez Start à l’entrée de la condition. Reliez la sortie bleue de succès à Approval et la sortie orange de condition fausse à Standard. La sortie rouge traite séparément les erreurs d’évaluation. La position des cartes ne crée pas de chemin.

**Préparer les cas de test**

Ouvrez Tester dans la barre d’outils. Choisissez un document de test ou saisissez ses données complètes au format JSON. Vérifiez les montants supérieurs, inférieurs et égaux à mille, ainsi que les valeurs absentes. Examinez les résultats des nœuds après exécution.

**Valider, enregistrer et activer**

Validez les connexions et les paramètres des cartes. Enregistrez explicitement sur le serveur, puis vérifiez l’activation séparément. Les brouillons automatiques du navigateur ne remplacent pas l’enregistrement. L’exécution et les journaux nécessitent le module et l’abonnement appropriés.

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
