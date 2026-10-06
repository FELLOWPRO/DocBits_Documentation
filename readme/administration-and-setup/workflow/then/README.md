# Then : choisir une carte d'action

Une carte **Then** indique à un workflow quoi faire après son déclencheur **When** et ses éventuelles conditions **And**. Dans le **Workflow Builder**, sélectionnez **Ajouter une carte** sous **Dans ce cas...**. Choisissez une catégorie à gauche ou tapez un nom dans **Carte de recherche**. Sélectionnez un aperçu de carte pour l'ajouter, remplissez les champs affichés sur la carte, puis enregistrez le workflow. Faites défiler la fenêtre de sélection pour voir d'autres cartes. Sélectionnez **×** pour la fermer sans ajouter de carte. Voir [Workflow](../README.md) pour la séquence complète.

Les aperçus ci-dessous montrent des actions disponibles, pas des paramètres déjà configurés. Choisissez l'action qui correspond au résultat souhaité.

## Champ du document

Définir ou inverser une case à cocher, saisir du texte dans un champ, ou copier un champ dans un autre. Choisissez les noms de champs et les valeurs demandés par la carte. Voir [Champ du document](document-field/README.md).

<figure><img src="../../../.gitbook/assets/then-category-document-field-fr.png" alt="Sélecteur de cartes Then en français avec la catégorie Champ du document sélectionnée ; les aperçus montrent les actions case à cocher, texte et copie de champ."><figcaption>Modifier un champ ou copier son contenu.</figcaption></figure>

## Document

Choisissez **Approuver le document** ou **Rejeter le document** lorsque le workflow doit prendre cette décision. Ajoutez d'abord une condition **And** si l'approbation doit dépendre d'un contrôle. Voir [Document](document/README.md).

<figure><img src="../../../.gitbook/assets/then-category-document-fr.png" alt="Sélecteur de cartes Then en français avec la catégorie Document sélectionnée ; les aperçus Approuver le document et Rejeter le document sont visibles."><figcaption>Approuver ou rejeter le document actuel.</figcaption></figure>

## Logique

Utilisez ces cartes pour convertir des valeurs entre formats numérique, texte et booléen, ou pour lire une valeur dans un JSON. Choisissez les champs d'entrée et de sortie sur la carte sélectionnée.

<figure><img src="../../../.gitbook/assets/then-category-logic-fr.png" alt="Sélecteur de cartes Then en français avec la catégorie Logique sélectionnée ; les aperçus visibles convertissent des types de données et lisent des valeurs dans un JSON."><figcaption>Transformer des valeurs pour une étape ultérieure du workflow.</figcaption></figure>

## Statut

Choisissez **Modifier le statut** pour faire passer le document au statut sélectionné. La carte peut aussi déclencher un autre workflow. Voir [Statut](status/README.md).

<figure><img src="../../../.gitbook/assets/then-category-status-fr.png" alt="Sélecteur de cartes Then en français avec la catégorie Statut sélectionnée ; l'aperçu Modifier le statut contient un champ de statut et un déclenchement de workflow facultatif."><figcaption>Faire passer le document à un autre statut.</figcaption></figure>

## Invites et scripts

Choisissez cette catégorie pour exécuter un script d'invite DocOperator. Sélectionnez le script et les variables demandés par la carte. La carte propose aussi des paramètres d'exécution tels que les tentatives.

<figure><img src="../../../.gitbook/assets/then-category-prompts-scripts-fr.png" alt="Sélecteur de cartes Then en français avec la catégorie Invites et scripts sélectionnée ; un aperçu de script d'invite DocOperator est visible."><figcaption>Exécuter un script d'invite DocOperator configuré.</figcaption></figure>

## Exportation

Lancer une exportation, exporter avec une configuration choisie, ou mettre en file d'attente une exportation finale. Choisissez la configuration d'exportation et l'option de tâches en attente affichés sur votre carte. Voir [Exportation](export/README.md).

<figure><img src="../../../.gitbook/assets/then-category-export-fr.png" alt="Sélecteur de cartes Then en français avec la catégorie Exportation sélectionnée ; les aperçus montrent le lancement, l'exportation configurée, la file d'attente et l'exportation finale."><figcaption>Choisir quand et comment le document est exporté.</figcaption></figure>

## Tâche

Créer une tâche ou une notification et l'assigner à un utilisateur ou à un groupe. Saisissez le titre, la description, la priorité et les paramètres de notification demandés par la carte. Certaines cartes assignent de façon séquentielle. Voir [Tâche](task/README.md).

<figure><img src="../../../.gitbook/assets/then-category-task-fr.png" alt="Sélecteur de cartes Then en français avec la catégorie Tâche sélectionnée ; les aperçus visibles créent ou assignent des tâches et des notifications."><figcaption>Créer un travail de suivi pour une personne ou un groupe.</figcaption></figure>

## E-mail

Envoyer un e-mail à l'aide d'un modèle sélectionné, soit à des destinataires, soit à des groupes. Choisissez le modèle et la destination sur la carte.

<figure><img src="../../../.gitbook/assets/then-category-email-fr.png" alt="Sélecteur de cartes Then en français avec la catégorie E-mail sélectionnée ; les aperçus envoient un e-mail avec modèle à des destinataires ou à des groupes."><figcaption>Envoyer un e-mail avec un modèle.</figcaption></figure>

## Tableau

Modifier des entrées ou calculer des valeurs dans un tableau de document. Sélectionnez le tableau, les colonnes, l'opérateur et la colonne de résultat demandés par la carte. Voir [Tableau](table/README.md).

<figure><img src="../../../.gitbook/assets/then-category-table-fr.png" alt="Sélecteur de cartes Then en français avec la catégorie Tableau sélectionnée ; les aperçus modifient des entrées et calculent des colonnes de résultat."><figcaption>Mettre à jour ou calculer les données d'un tableau.</figcaption></figure>

## Attribué à

Assigner le document à un utilisateur, un groupe, un bénéficiaire ou une sous-organisation. Certaines cartes utilisent un champ ou une table de décision et proposent une solution de repli. Choisissez la bonne destination et la solution de repli sur la carte sélectionnée. Voir [Attribué à](assignee/README.md).

<figure><img src="../../../.gitbook/assets/then-category-assignee-fr.png" alt="Sélecteur de cartes Then en français avec la catégorie Attribué à sélectionnée ; les aperçus visibles assignent un utilisateur, un bénéficiaire, un groupe ou un contact fournisseur."><figcaption>Acheminer le document vers la prochaine personne ou le prochain groupe responsable.</figcaption></figure>

## Action

Exécuter un autre workflow, envoyer une requête HTTPS, appeler une API, ou utiliser la carte de calcul d'IA pour les majorations de coûts. Ces actions peuvent affecter d'autres systèmes ; demandez à votre administrateur quel point d'accès et quels paramètres utiliser. Voir [Action](action/README.md).

<figure><img src="../../../.gitbook/assets/then-category-action-fr.png" alt="Sélecteur de cartes Then en français avec la catégorie Action sélectionnée ; les aperçus montrent Exécuter le flux de travail, requête HTTPS, appel d'API et calcul de l'IA pour les majorations de coûts."><figcaption>Démarrer un autre workflow ou une action d'intégration.</figcaption></figure>
