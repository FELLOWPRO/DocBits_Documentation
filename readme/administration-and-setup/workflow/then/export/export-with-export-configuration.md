# Export with Export Configuration

<figure><img src="../../../../.gitbook/assets/image (284).png" alt="" width="563"><figcaption></figcaption></figure>

## **Objectif :**

La carte de workflow **« Export Document with Export Configuration »** est conçue pour exporter un document à l'aide d'une configuration d'export spécifiée. Elle offre la flexibilité d'ignorer les tâches en attente associées au document, garantissant un processus d'export fluide quel que soit son état actuel.

## **Composants de la carte :**

1. **Export Configuration**
   * **Description** : spécifie la configuration d'export à utiliser pour traiter le document.
   * **Détail** : cette configuration détermine le format, la structure et la destination du document exporté.
2. **Ignore Pending Tasks**
   * **Description** : détermine si les tâches en attente liées au document doivent être ignorées pendant le processus d'export.
   * **Options** :
     * **True** : exporte le document indépendamment des tâches en attente.
     * **False** : garantit que les tâches en attente sont terminées avant l'export.

## **Fonctionnalité :**

* **Évaluation de la condition** : le système évalue les conditions définies dans les sections **« Where »** et **« And »** du workflow. Si les deux conditions sont vraies, le processus d'export est lancé.
* **Export du document** : à l'aide de l'**Export Configuration** spécifiée, le document est traité et exporté dans le format et vers la destination définis.
* **Gestion des tâches en attente** : si **Ignore Pending Tasks** est défini sur **True**, le processus d'export contourne toutes les tâches en suspens liées au document. S'il est défini sur **False**, l'export est différé jusqu'à ce que toutes les tâches soient résolues.

## **Mise en place et configuration :**

Pour configurer cette carte, les utilisateurs doivent :

1. Sélectionner l'**Export Configuration** souhaitée pour définir comment le document sera exporté.
2. Choisir d'**Ignore Pending Tasks** en définissant la valeur sur **True** ou **False**.
3. S'assurer que les conditions des sections **« Where »** et **« And »** sont correctement définies, car la carte n'exécute son action que lorsque ces conditions sont vraies.

## **Conclusion :**

La carte de workflow **« Export Document with Export Configuration »** garantit que les documents sont exportés de manière efficace et conformément à des configurations prédéfinies. Avec la possibilité d'ignorer les tâches en attente, cette carte offre de la flexibilité dans la gestion des documents à différentes étapes, réduisant les retards et rationalisant le processus d'export.
