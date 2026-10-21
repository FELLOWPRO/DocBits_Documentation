# Attribuer un document au groupe d'approvisionnement

<figure><img src="../../../../.gitbook/assets/workflow-card-qa-20261021-card-9b2624ff9d34-fr.png" alt="Champs de la carte dans la version affichée. Les champs ne sont pas encore renseignés." width="563"><figcaption><p>Champs de la carte dans la version affichée. Les champs ne sont pas encore renseignés.</p></figcaption></figure>

## **Objectif :**

La carte de workflow **« Assign to Procurement Group »** sert à assigner un document à un groupe d'approvisionnement spécifié au sein du système. Cela aide à rationaliser la gestion des documents en garantissant que l'équipe appropriée traite le document en fonction de son groupe d'approvisionnement assigné.

## **Composants de la carte :**

1. **Groupe d'approvisionnement**
   * **Descriptif :** spécifie le groupe d'approvisionnement auquel le document sera assigné.
   * **Détail :** le groupe d'approvisionnement sélectionné sera responsable du traitement et de la gestion du document.

## **Fonctionnalité :**

* **Évaluation de la condition :**\
  La carte n'exécute son action que si les sections **« Quand »** et **« Et »** sont toutes deux évaluées comme vraies.
* **Exécution de l'action :**\
  Si les deux conditions sont vraies, le document est assigné au groupe d'approvisionnement spécifié. Si l'une des conditions est fausse, aucune action n'est effectuée et le document reste non assigné.

## **Mise en place et configuration :**

* **Sélectionner le Procurement Group :** choisissez le groupe d'approvisionnement auquel assigner le document dans la liste déroulante.

## **Conclusion :**

La carte de workflow **« Assign to Procurement Group »** offre un moyen simple mais efficace de garantir que les documents sont automatiquement assignés à la bonne équipe d'approvisionnement pour un traitement complémentaire.

<!-- workflow-card-practical-example-20261021 -->

## Exemple pratique

**Quand utiliser :** Envoyer une exception d'achat à son groupe d'approvisionnement.

**Configuration :** Sélectionnez le groupe configuré `Demo Procurement`.

**Résultat attendu et contre-exemple :** Le document est affecté à ce groupe d'approvisionnement. Un groupe ordinaire portant un nom similaire ne doit pas être considéré comme étant la même cible configurée.

Il s’agit d’une configuration illustrative et du résultat attendu. Utilisez les champs, utilisateurs et groupes configurés dans votre organisation de test ; cela ne veut pas dire que cet exemple a été exécuté.
