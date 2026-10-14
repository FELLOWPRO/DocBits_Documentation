# Validation & Testing

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
