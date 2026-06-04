# Nœuds

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

Les nœuds sont reliés par des **arêtes colorées**. Faites glisser depuis une poignée située sur le côté **droit** d'un nœud vers la poignée d'entrée située sur le côté **gauche** d'un autre nœud pour créer une connexion. Chaque couleur indique un résultat d'exécution différent :

- **Success** (bleu) — le chemin par défaut emprunté lorsqu'un nœud se termine avec succès. Disponible sur tous les types de nœuds.
- **Failed Condition** (orange) — emprunté lorsqu'une condition est évaluée à faux. Disponible sur les nœuds **And** (condition).
- **Error** (rouge) — emprunté lorsqu'un nœud rencontre une erreur pendant l'exécution. Disponible sur les nœuds **And** et **Then** (action).

## Mise en évidence du chemin d'exécution

Cliquez sur un nœud pour voir son chemin d'exécution. Tous les nœuds qui y mènent et tous ceux qui en découlent sont mis en évidence — tout le reste est atténué. Pour les nœuds **Wait ALL**, chaque branche entrante est affichée afin que vous puissiez voir exactement ce que la barrière attend avant de continuer.

## Étapes suivantes

- Transmettez des données entre les nœuds avec les [Variables](variables.md).
- Vérifiez et exécutez votre flux avec la [Validation & Test](validation-and-testing.md).
