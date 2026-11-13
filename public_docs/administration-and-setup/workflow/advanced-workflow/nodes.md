# Nœuds

## Vidéo: Nœuds et chemins

{% embed url="https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/advanced_workflows_logic/v2/fr.mp4" %}

[Sous-titres (WebVTT)](https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/advanced_workflows_logic/v2/fr.vtt) · 1:49

<details>
<summary>Transcription</summary>

**Le rôle de chaque nœud**

Start lance manuellement. When définit un événement. Aucun des deux ne reçoit de connexion entrante. And vérifie une condition. Then exécute une action. Les deux constructeurs partagent le catalogue de cartes. Les notes expliquent sans être exécutées.

**Trois résultats distincts**

Reliez une sortie à l’entrée suivante. Dans le concepteur, bleu signifie succès, orange condition fausse, rouge erreur. And possède trois résultats ; Then, succès et erreur. Les vues d’exécution affichent le succès en vert.

**Construisez une alternative**

Vérifiez si une facture dépasse le seuil. Reliez bleu à l’approbation, orange au traitement normal et rouge à la gestion des erreurs. Une condition fausse continue par son chemin connecté ; elle n’arrête pas toutes les branches.

**Joindre avec Wait ALL**

Wait ALL réunit des branches. Chaque nœud source doit avoir suivi un chemin relié à la jonction. Connectez les deux contrôles requis et l’action suivante. Un chemin non sélectionné ne fournit pas le résultat attendu.

**Alternatives avec ANY et OR**

Wait ANY et OR réunissent les branches si au moins une source suit un chemin connecté. OR exige deux nœuds sources distincts. Ces jonctions ne rendent pas les choix exclusifs et n’annulent pas d’autres actions. Testez le graphe entier.

**Gardez un graphe exécutable**

Rendez les nœuds accessibles depuis une entrée. Évitez les cycles et les connexions entrantes vers Start ou When. Incluez une action Then et validez les chemins. Les nœuds Delay importés exigent une durée positive ; Ajouter ne propose pas Delay.

</details>

[Voir les cinq chapitres](../advanced-workflow-videos.md)

Un Workflow Avancé est un graphe de **nœuds** reliés par des arêtes. Vous ajoutez des nœuds depuis le menu **+ Add** (ou par un clic droit sur le canevas) et vous les reliez pour définir le flux d'exécution.

<figure><img src="../../../.gitbook/assets/workflow_advanced_add_menu.png" alt="Menu d'ajout de nœud avec les types de nœuds disponibles"><figcaption><p>Le menu de nœud <strong>+ Add</strong> — les types de nœuds disponibles.</p></figcaption></figure>

## Types de nœuds

- **Start** — le point d'entrée du workflow. Ajouté automatiquement ; tout flux commence ici.
- **When** — une carte de déclenchement, identique à celle du générateur Standard.
- **And** — une carte de condition. Elle est évaluée à vrai ou faux et peut ramifier le flux.
- **Then** — une carte d'action qui effectue un traitement (définir des champs, créer des tâches, appeler des API, …).
- **Wait ALL** — attend que *toutes* les branches entrantes soient terminées avant de continuer.
- **Wait ANY** — continue dès que *l'une* des branches entrantes est terminée.
- **OR** — ramifie le flux vers des chemins alternatifs.
- **Note** — une annotation en texte libre sur le canevas ; elle n'affecte pas l'exécution.

Les nœuds **When / And / Then** utilisent exactement les mêmes cartes que celles décrites dans la section [Cartes](../cards-overview.md).

## Relier les nœuds

{% embed url="https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/workflow-results/v1/fr.mp4" %}

**Vidéo:** Succès, condition échouée et erreur dans une exécution · 1:24 · [Sous-titres (WebVTT)](https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/workflow-results/v1/fr.vtt)

<details>

<summary>Transcription</summary>

**Quand, Et, Dans ce cas à l'exécution** · [0:00](https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/workflow-results/v1/fr.mp4#t=0.25)

Quand un Workflow s'exécute, la carte Quand le démarre. Les cartes Et vérifient des conditions et les cartes Dans ce cas agissent. La suite dépend du résultat de chaque carte.

**Succès, condition échouée ou erreur** · [0:12](https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/workflow-results/v1/fr.mp4#t=12.85)

Chaque carte Et se termine par l'un de trois résultats. Un succès suit le chemin bleu, une condition échouée le chemin orange et une erreur le chemin rouge.

**Données manquantes : une erreur** · [0:24](https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/workflow-results/v1/fr.mp4#t=24.783)

Des données manquantes ne sont pas une condition échouée. S'il manque un champ dont la carte a besoin, une variable ou le document, la carte signale une erreur et prend le chemin rouge.

**Pas de chemin orange : arrêt** · [0:36](https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/workflow-results/v1/fr.mp4#t=36.816)

Si une condition échoue et que son chemin orange n'est pas relié, le Workflow s'arrête sur cette carte. L'exécution se termine en condition échouée.

**Relié : juste une autre branche** · [0:47](https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/workflow-results/v1/fr.mp4#t=47.416)

Si le chemin orange est relié, une condition échouée est simplement une autre branche. Le Workflow continue par là et peut quand même finir en succès.

**Chemin rouge : rattraper les erreurs** · [0:57](https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/workflow-results/v1/fr.mp4#t=57.716)

Reliez le chemin rouge à une solution de repli, par exemple une tâche pour une personne, pour que les erreurs ne passent pas inaperçues. Le repli s'exécute, mais l'exécution reste marquée en erreur.

**Comment une exécution se termine** · [1:11](https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/workflow-results/v1/fr.mp4#t=71.283)

En bref : toute erreur fait de l'exécution une erreur. Une condition échouée sans chemin orange relié en fait une condition échouée. Tout le reste se termine en succès.

</details>

Les nœuds sont reliés par des **arêtes colorées**. Faites glisser depuis une poignée située sur le côté **droit** d'un nœud vers la poignée d'entrée située sur le côté **gauche** d'un autre nœud pour créer une connexion. Chaque couleur indique un résultat d'exécution différent :

- **Success** (bleu) — le chemin par défaut emprunté lorsqu'un nœud se termine avec succès. Disponible sur tous les types de nœuds.
- **Failed Condition** (orange) — emprunté lorsqu'une condition est évaluée à faux. Disponible sur les nœuds **And** (condition).
- **Error** (rouge) — emprunté lorsqu'un nœud rencontre une erreur pendant l'exécution. Disponible sur les nœuds **And** et **Then** (action).

## Mise en évidence du chemin d'exécution

Cliquez sur un nœud pour voir son chemin d'exécution. Tous les nœuds qui y mènent et tous ceux qui en découlent sont mis en évidence — tout le reste est atténué. Pour les nœuds **Wait ALL**, chaque branche entrante est affichée afin que vous puissiez voir exactement ce que la barrière attend avant de continuer.

## Étapes suivantes

- Transmettez des données entre les nœuds avec les [Variables](variables.md).
- Vérifiez et exécutez votre flux avec la [Validation & Test](validation-and-testing.md).
