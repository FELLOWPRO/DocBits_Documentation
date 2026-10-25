# Tableau de bord

Le **Tableau de bord du flux de travail** est la page d'accueil de la zone des workflows. Il montre les performances de vos workflows — totaux d'exécutions, taux de réussite et d'échec, graphique des exécutions dans le temps et activité récente — et vous donne accès à la liste des workflows, au Test Manager et au Card SDK.

## Indicateurs de volume

Les trois premières cartes présentent les workflows exécutés aujourd’hui, les workflows créés pendant la période et le nombre total d’exécutions. Le sous-titre de la carte **Exécutions totales** indique la durée de la période sélectionnée.

<figure><img src="../../.gitbook/assets/workflow-kpi-volume-current-fr.png" alt="Indicateurs de volume : workflows exécutés aujourd’hui, workflows créés et exécutions totales sur la période sélectionnée."><figcaption><p>Indicateurs de volume : workflows exécutés aujourd’hui, workflows créés et exécutions totales sur la période sélectionnée.</p></figcaption></figure>

## Résultats d’exécution

Les trois cartes suivantes présentent les **Exécutions réussies**, le **Taux de réussite** et le **Taux d’échec**. Les sous-titres indiquent le nombre total d’exécutions servant de contexte aux indicateurs.

<figure><img src="../../.gitbook/assets/workflow-kpi-outcomes-current-fr.png" alt="Résultats d’exécution : exécutions réussies, taux de réussite et taux d’échec."><figcaption><p>Résultats d’exécution : exécutions réussies, taux de réussite et taux d’échec.</p></figcaption></figure>

## Graphique des exécutions

Le graphique présente les séries de réussite et d’échec avec les mois affichés en français.

<figure><img src="../../.gitbook/assets/workflow-chart-current-fr.png" alt="Graphique des exécutions : séries de réussite et d’échec sur les sept mois affichés en français."><figcaption><p>Graphique des exécutions : séries de réussite et d’échec sur les sept mois affichés en français.</p></figcaption></figure>


## Onglets

- **Tableau de bord** — indicateurs d'exécution et activité récente.
- **Liste des flux de travail** — chaque workflow avec son type, son ordre d'exécution et son déclencheur. Créez-en un nouveau avec **Nouveau flux de travail**.
- **Liste des gestionnaires de tests** — scénarios de test qui valident vos workflows ; exécutez-les avec **Exécuter tous les tests**.
- **Licence** — informations sur la licence des workflows.
- **Kit de développement logiciel pour cartes** — créez et téléversez des cartes de workflow personnalisées (voir [Card SDK](card-sdk.md)).

La barre d'outils propose également **Modèles**, qui ouvre la bibliothèque de modèles réutilisables, et **Processus d'importation**, qui importe un workflow à partir d'un fichier JSON. Pour enregistrer un workflow comme modèle, consultez le [constructeur Flux standard](standard-workflow-builder.md#ajouter-des-cartes).

La **gestion des tests** vous permet d'enregistrer des scénarios de test par workflow et de les exécuter ensemble, afin de confirmer que vos workflows se comportent toujours correctement après des modifications :

<figure><img src="../../.gitbook/assets/prior-u032-fr.png" alt="Liste des scénarios de test de workflows."><figcaption><p>Liste des scénarios de test de workflows.</p></figcaption></figure>

## Étapes suivantes

- Créez une automatisation linéaire avec le builder **Flux standard**.
- Créez un flux avec branches grâce au builder **Flux de travail avancé**.
