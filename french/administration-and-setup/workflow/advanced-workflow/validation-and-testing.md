# Validation & Testing

## Vidéo: Variables, tests et activation

{% embed url="https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/advanced_workflows_testing/v2/fr.mp4" %}

[Sous-titres (WebVTT)](https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/advanced_workflows_testing/v2/fr.vtt) · 1:53

<details>
<summary>Transcription</summary>

**Choisissez le type**

Ouvrez Variables avec les accolades. Choisissez texte, nombre, oui ou non, ou document. Recherchez les noms. Document contient une référence définie par une action dédiée ; ce formulaire n’accepte pas de valeur documentaire.

**Portée de l’organisation**

Choisissez un nom unique, un type et une valeur initiale. Création, modification et suppression sont enregistrées immédiatement dans l’organisation. D’autres workflows partagent ces valeurs. Enregistrer ou abandonner le canevas n’annule pas ces changements.

**Validez la structure**

Cliquez sur Valider. Examinez erreurs et avertissements au-dessus du canevas. Un message cible son nœud. Vérifiez actions, entrées, sorties, cycles et jonctions. Une structure valide ne garantit pas des données correctes.

**Choisissez le contexte**

La lecture dans la barre ouvre le choix du document. Choisissez document, données personnalisées ou test sans document pour les cartes indépendantes. Start lance directement. Les tests incluent les modifications non enregistrées et simulent les actions destructrices.

**Examinez les résultats**

Examinez messages et durées : vert, succès ; orange, condition fausse ; rouge, erreur ; gris, ignoré. Corrigez et retestez. Le gestionnaire de tests permet des scénarios reproductibles : succès, alternatives, données absentes et erreurs.

**Enregistrez avant d’activer**

Le brouillon local est enregistré automatiquement environ toutes les trente secondes après modification. Enregistrez explicitement sur le serveur. Activez après le premier enregistrement. Vérifiez l’état dans la liste avant d’attendre une exécution automatique.

</details>

[Voir les cinq chapitres](../advanced-workflow-videos.md)

Pendant que vous construisez un Advanced Workflow, deux contrôles de la barre d'outils vous permettent de le vérifier sans quitter le générateur. Ils servent aux *vérifications rapides pendant la construction* — pour des tests enregistrés et reproductibles, utilisez le [Test Manager](../test-manager.md).

## Validate

Cliquez sur le contrôle **Validate** (l'icône cercle coché, ou appuyez sur <kbd>Cmd/Ctrl</kbd> + <kbd>Shift</kbd> + <kbd>V</kbd>). La validation vérifie le graphe à la recherche de problèmes — nœuds non connectés, configuration manquante et connexions invalides — et les signale pour que vous puissiez les corriger avant que le workflow ne s'exécute sur des documents réels.

## Test

Cliquez sur le contrôle **Test** (l'icône lecture, ou appuyez sur <kbd>Cmd/Ctrl</kbd> + <kbd>Shift</kbd> + <kbd>T</kbd>) pour exécuter le flux actuel sur un exemple et observer son comportement, sans affecter les documents en production. C'est le moyen le plus rapide de vérifier une modification que vous venez d'apporter sur le canevas.

## Quand utiliser lequel

- **Validate / Test dans le générateur** (cette page) — un retour immédiat pendant que vous concevez le flux.
- **[Test Manager](../test-manager.md)** — enregistrez le scénario pour pouvoir le réexécuter plus tard (et conjointement avec tous vos autres scénarios) afin de détecter les régressions après de futures modifications.

## Étapes suivantes

- Passez en revue les types de nœuds et les connexions dans [Nœuds](nodes.md).
- Découvrez tous les contrôles de la barre d'outils et du canevas dans [Barre d'outils et canevas](toolbar-and-canvas.md).
