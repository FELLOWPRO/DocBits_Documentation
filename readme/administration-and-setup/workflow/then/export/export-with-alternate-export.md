# Exporter avec une exportation alternative

<figure><img src="../../../../.gitbook/assets/workflow-card-qa-20261021-card-379e4b3a5355-fr.png" alt="Champs de la carte dans la version affichée. Les champs ne sont pas encore renseignés." width="563"><figcaption><p>Champs de la carte dans la version affichée. Les champs ne sont pas encore renseignés.</p></figcaption></figure>

## Quand utiliser cette carte

Utilisez cette action Ensuite pour l'exportation alternative configurée sur le type de document actuel. Configurez et validez cet itinéraire avant d'ajouter l'action.

## La configuration provient du type de document

La carte n'a pas de sélecteur de configuration d'exportation. Il indique si l'exportation alternative est activée, la configuration d'exportation alternative et l'état après l'exportation à partir des paramètres de type de document. En interne, ce sont `DOC_ALTERNATE_EXPORT_SETTING`, `DOC_ALTERNATE_EXPORT_EXPORT_CONFIG` et `DOC_ALTERNATE_EXPORT_STATUS`.

Une exportation alternative explicitement désactivée génère une condition d’échec. Les données d'activation, la configuration ou l'état des résultats manquants sont signalés plutôt que de remplacer silencieusement la route par défaut. La demande d'exportation vérifie les tâches en attente.

## Vérifier le résultat

Inspectez le journal de la carte, l’historique des exportations, l’état du document et la destination de test autorisée. Une demande, un délai d'attente ou un changement de statut ne suffit pas à établir que les données ont atteint la destination. Vérifiez l'historique des exportations avant de réessayer une opération susceptible de créer des doublons.

<!-- workflow-card-complete-example-20261021 action_alternate_export -->

### Autre exemple d'exportation

**Configuration :** Préparez le type de document synthétique `DEMO_INVOICE` avec l'exportation alternative activée, une configuration d'exportation de test autorisée et l'état du résultat souhaité dans ses paramètres de type de document. Ajoutez cette action Then après les vérifications requises. Cette carte lit ces paramètres ; il n'offre pas de sélecteur de configuration d'exportation.

**Résultat attendu et contre-exemple :** L'action demande l'exportation via cette configuration alternative et vérifie les tâches en attente. Vérifiez le résultat de l'exportation et la destination du test séparément. La désactivation de l'exportation alternative entraîne une condition d'échec ; un paramètre ou une configuration d’activation absent ne constitue pas une exportation réussie. N'exécutez pas cet exemple sur une destination comptable.

Il s'agit d'une configuration de test illustrative et du résultat attendu ; il n'a pas été exécuté. Utilisez les données et les destinataires configurés dans votre organisation de test.
