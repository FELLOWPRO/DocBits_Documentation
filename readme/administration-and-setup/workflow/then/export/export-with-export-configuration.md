# Exporter avec la configuration d'exportation

<figure><img src="../../../../.gitbook/assets/workflow-card-qa-20261021-card-10e6b7590bc6-fr.png" alt="Champs de la carte dans la version affichée. Les champs ne sont pas encore renseignés." width="563"><figcaption><p>Champs de la carte dans la version affichée. Les champs ne sont pas encore renseignés.</p></figcaption></figure>

## **Objectif :**

La carte de workflow **"Exporter un document avec configuration d'exportation"** est conçue pour exporter un document à l'aide d'une configuration d'exportation spécifiée. Il offre la flexibilité d'ignorer toutes les tâches en attente associées au document, garantissant ainsi un processus d'exportation fluide quel que soit son état actuel.

## **Composants de la carte :**

1. **Exporter la configuration**
   * **Descriptif** : Spécifie la configuration d'exportation à utiliser pour le traitement du document.
   * **Détail** : Cette configuration détermine le format, la structure et la destination du document exporté.
2. **Ignorer les tâches en attente**
   * **Descriptif** : Détermine si les tâches en attente liées au document doivent être ignorées lors du processus d'exportation.
   * **Possibilités** :
     * **True** : exporte le document quelles que soient les tâches en attente.
     * **False** : garantit que les tâches en attente sont terminées avant l'exportation.

## **Fonctionnalité :**

* **Évaluation des conditions** : Le système évalue les conditions définies dans les champs **"Quand"** et **"Et sections"** du flux de travail. Si les deux conditions sont remplies, le processus d'exportation est lancé.
* **Exportation de document** : à l'aide de la **Configuration d'exportation** spécifiée, le document est traité et exporté dans le format et la destination définis.
* **Gestion des tâches en attente** : Si **Ignorer les tâches en attente** est défini sur **True**, le processus d'exportation ignore toutes les tâches en attente liées au document. Si la valeur est **False**, les tâches en attente peuvent empêcher l'exportation. Résolvez-les et organisez le déclencheur de flux de travail prévu ou réessayez.

## **Installation et configuration :**

Pour configurer cette carte, les utilisateurs doivent :

1. Sélectionnez la **Exporter la configuration** souhaitée pour définir la manière dont le document sera exporté.
2. Choisissez si vous souhaitez **Ignorer les tâches en attente** en définissant la valeur sur **True** ou **False.**
3. Assurez-vous que les conditions dans **"Quand"** et **"Et sections"** sont correctement définies, car la carte n'exécute son action que lorsque ces conditions sont vraies.

## **Conclusion :**

La carte de workflow **"Exporter un document avec configuration d'exportation"** garantit que les documents sont exportés efficacement et selon des configurations prédéfinies. Avec la possibilité d'ignorer les tâches en attente, cette carte offre une flexibilité dans le traitement des documents à différentes étapes, réduisant ainsi les retards et rationalisant le processus d'exportation.

## Versions actuelles et tâches en attente

Sur la v3, choisissez également **Status après export** : `finished` ferme le document après un export réussi ; `exported` le laisse ouvert pour un traitement ultérieur. Les versions antérieures conservent `finished`. Une sélection manquante est par défaut `finished` ; une sélection invalide est rejetée.

Si des tâches ouvertes empêchent l'export, la fiche signale le refus. Résoudre les tâches et organiser le déclencheur ou réessayer ; l'attente et la reprise automatiques ne sont pas garanties par cette carte. La carte d'exportation en file d'attente distincte collecte une configuration pour l'exportation finale à la fin de l'exécution. Voir [Exporter les cartes et l'état des résultats](../../cards-overview/export-cards-guide.md).

<!-- workflow-card-practical-example-20261021 -->

## Exemple pratique

**Quand utiliser :** Choisissez une configuration d'export spécifique pour un document validé.

**Configuration :** Sélectionnez l'exportateur de démonstration configuré et définissez Ignorer les tâches en attente sur `false`. Utilisez un document avec une tâche ouverte, puis un test séparé sans tâches ouvertes.

**Résultat attendu et contre-exemple :** Il ne faut pas supposer que le cas de tâche ouverte reprend automatiquement. Après avoir résolu la tâche, déclenchez à nouveau l'exportation prévue et vérifiez le résultat de l'exportateur et le statut pris en charge.

Il s’agit d’une configuration illustrative et du résultat attendu. Utilisez les champs, utilisateurs et groupes configurés dans votre organisation de test ; cela ne veut pas dire que cet exemple a été exécuté.
