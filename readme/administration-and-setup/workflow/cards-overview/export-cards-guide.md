# Cartes d'exportation de flux de travail et statut du document

<figure><img src="../../../.gitbook/assets/workflow-card-qa-20261021-category-11f244132c25-fr.png" alt="Cartes disponibles dans la catégorie sélectionnée. Renseignez les champs avant utilisation."><figcaption><p>Cartes disponibles dans la catégorie sélectionnée. Renseignez les champs avant utilisation.</p></figcaption></figure>

Choisissez si vous souhaitez exporter immédiatement ou mettre une configuration en file d'attente pour l'exportation finale à la fin de l'exécution. Ces choix sont distincts du statut que le document devrait avoir après une exportation réussie.

| Carte | Quand l'exportation s'exécute | Paramètres importants |
| --- | --- | --- |
| Démarrer l'exportation avec validation (`EXPORT`) | Démarre l'exportation en utilisant les paramètres d'exportation configurés du document. | Validation et, à partir de la v4, Statut après export. |
| Exporter avec la configuration d'exportation (`ACTION_EXPORT_WITH`) | Exporte en utilisant la configuration sélectionnée lors de l'exécution de la carte. | Exporter la configuration, Ignorer les tâches en attente et, à partir de la v3, Statut après exportation. |
| Exportation de file d'attente avec configuration (`ACTION_EXPORT_WITH_CONFIG_DEFERRED`) | Collecte la configuration pour l'exportation finale à la fin de l'exécution. L'ajout d'une demande d'export à la file d'attente ne prouve pas que l'export final a réussi. | Exporter la configuration, Ignorer les tâches en attente et, à partir de la v3, Statut après exportation. |
| Exportation alternative (`ACTION_ALTERNATE_EXPORT`) | Utilise l’itinéraire d’exportation alternatif documenté sur sa carte. | Ne présumez pas qu’elle a les mêmes options de version ou de statut que les trois cartes ci-dessus. |

## Statut après exportation

| Valeur | Signification après une exportation réussie | Utilisation typique |
| --- | --- | --- |
| `finished` | Exporté et fermé. | Le traitement est terminé. |
| `exported` | Exporté mais reste ouvert pour un traitement ultérieur. | L'approbation ou un autre flux de travail doit encore suivre. |

Démarrer Exporter v4, Exporter avec la configuration d'exportation v3 et Exporter en file d'attente v3 proposent cette sélection. Les versions antérieures conservent `finished`. Une sélection manquante revient à `finished` et est enregistrée ; une valeur invalide est rejetée avant l'exportation. Une ancienne carte enregistrée n'acquiert pas le nouveau comportement simplement parce qu'une nouvelle version de modèle existe. Inspectez la version de la carte et testez à nouveau toute mise à niveau explicite.

Les conditions de statut du document et Change Status proposent également `exported` dans les versions contenant la mise à jour de statut correspondante. Le changement de statut à lui seul ne permet pas d'effectuer une exportation. Utilisez le résultat de l'exportation et les journaux pour établir que les données ont réellement atteint leur destination.

## Exportation immédiate avec configuration

1. Ajoutez la carte sous Ensuite et sélectionnez une configuration d'exportation valide.
2. Choisissez si vous souhaitez ignorer les tâches en attente. Désactivez cette option si les tâches doivent bloquer l'exportation.
3. Sur la v3, sélectionnez délibérément `finished` ou `exported`.
4. Testez avec un document dans un statut de traitement autorisé, puis inspectez le résultat et la destination de la carte.

Si des tâches en attente empêchent l'export, la carte enregistre un export refusé. Résolvez les tâches et organisez le déclencheur de flux de travail prévu ou réessayez. Cette carte ne promet pas d'attendre et de reprendre automatiquement. Un délai d'attente ne prouve pas non plus que le système distant n'a rien fait ; inspectez l’historique des exportations avant de répéter une opération susceptible de créer des doublons.

## Exportation de file d'attente avec configuration

Ajoutez cette carte lorsque l'exportation doit être collectée pour la dernière étape de l'exécution. Sélectionnez la configuration, la stratégie des tâches en attente et l'état des résultats. La carte enregistre la configuration demandée ; inspectez le résultat final de l’exportation séparément. Le message confirmant la demande en file d'attente n'est pas une confirmation d'écriture comptable.

Par exemple, sélectionnez `exported` lorsqu'une exportation réussie doit laisser le document disponible pour une approbation ultérieure. Sélectionnez `finished` lorsqu'aucun autre traitement n'est requis. Revérifiez l'état final ainsi que la destination de l'exportation.

## Chèques obligatoires

Testez une configuration valide, une configuration manquante, des tâches en attente avec les deux paramètres et les deux statuts de résultat. Testez la version déjà utilisée dans un workflow existant avant de la modifier. Pour une exportation en file d'attente, vérifiez l'exécution finale ; pour une exportation immédiate, vérifiez son propre résultat. Consultez les [Workflow Logs](../workflow-logs.md) et ne confondez pas une carte ignorée avec un succès.
