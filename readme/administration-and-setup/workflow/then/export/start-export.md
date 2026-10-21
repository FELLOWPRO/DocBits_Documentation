# Démarrer l'exportation

<figure><img src="../../../../.gitbook/assets/workflow-card-qa-20261021-card-f55f53ace7e0-fr.png" alt="Champs de la carte dans la version affichée. Les champs ne sont pas encore renseignés." width="563"><figcaption><p>Champs de la carte dans la version affichée. Les champs ne sont pas encore renseignés.</p></figcaption></figure>

## **Objectif :**

La carte de workflow **"Démarrer l'exportation"** est conçue pour lancer le processus d'exportation d'un document. Cette carte fonctionne comme un déclencheur au sein du flux de travail pour démarrer de manière transparente l'opération d'exportation une fois que les conditions des sections précédentes sont remplies.

## **Composants de la carte :**

1. **Action**
   1. **Descriptif** : Lance le processus d'exportation du document.
   2. **Détail** : La carte utilise les paramètres d'exportation configurés dans le système pour traiter et exporter le document.

## **Fonctionnalité :**

* **Évaluation des conditions** : Le système évalue les conditions définies dans les champs **"Quand"** et **"Et sections"** du flux de travail. Si toutes les conditions sont remplies, le processus d'exportation commence.
* **Exportation du document** : Le document est traité et exporté en utilisant la configuration d'exportation par défaut ou préalablement définie.

## **Installation et configuration :**

Les versions antérieures utilisent les paramètres d'exportation déjà définis dans le système. Sur la version 4, configurez la validation et sélectionnez Statut après export. Vérifiez également que :

1. Les conditions **"Quand"** et **"Et Sections"** sont correctement configurées, car la carte ne s'exécute que si ces conditions sont évaluées comme vraies.
2. Une configuration d'exportation valide est associée au document dans le système.

## **Conclusion :**

La carte de flux de travail **"Démarrer l'exportation"** fournit un moyen rationalisé et automatisé de déclencher le processus d'exportation. En s'appuyant sur des paramètres préconfigurés et des évaluations conditionnelles, il garantit un traitement efficace et précis des documents.

## Versions de la carte et statut des résultats

La déclaration ci-dessus concernant l'absence de configuration spécifique à la carte s'applique à la carte Start Export antérieure. Démarrer l'exportation avec validation v4 inclut la validation et le **Statut après l'exportation**. Choisissez `finished` pour fermer un document exporté avec succès, ou `exported` pour le garder ouvert pour un traitement ultérieur. Les versions antérieures conservent `finished`. Voir [Exporter les cartes et l'état des résultats](../../cards-overview/export-cards-guide.md) pour les valeurs par défaut, les erreurs et les tests.

<!-- workflow-card-practical-example-20261021 -->

## Exemple pratique

**Quand utiliser :** Exportez un document une fois les vérifications requises passées.

**Configuration :** Sélectionnez le statut post-export pris en charge, par exemple `exported` lorsque le document doit rester disponible pour un traitement ultérieur. Assurez-vous que l'exportateur configuré et les données requises sont prêts.

**Résultat attendu et contre-exemple :** Après une exportation réussie, l'état du résultat sélectionné est appliqué. Une erreur de l’exportateur n’est pas une exportation terminée ; inspectez son journal et testez la branche d’échec.

Il s’agit d’une configuration illustrative et du résultat attendu. Utilisez les champs, utilisateurs et groupes configurés dans votre organisation de test ; cela ne veut pas dire que cet exemple a été exécuté.
