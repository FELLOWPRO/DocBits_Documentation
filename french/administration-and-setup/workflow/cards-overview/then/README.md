# Then

Une carte **Then** indique au workflow ce qu'il doit faire après son déclencheur **When** et toutes les conditions **And**. Dans le **Workflow Builder**, sélectionnez **Add Card** sous **Then...**. Choisissez une catégorie à gauche ou saisissez un nom dans **Search Card**. Sélectionnez l'aperçu d'une carte pour l'ajouter, renseignez les champs affichés sur la carte, puis enregistrez le workflow. Faites défiler le sélecteur pour voir d'autres cartes. Sélectionnez **×** pour le fermer sans ajouter de carte. Consultez [Workflow](../../) pour la séquence complète.

Les aperçus ci-dessous montrent les actions disponibles, et non des paramètres terminés. Choisissez l'action qui correspond au résultat souhaité.

## Document Field

Définissez ou inversez une case à cocher, saisissez du texte dans un champ, ou copiez un champ dans un autre. Choisissez les noms de champs et la valeur demandés par la carte. Consultez [Document Field](document-field/).

<figure><img src="../../../../.gitbook/assets/then-category-document-field-en.png" alt="Sélecteur de cartes Then en anglais avec Document Field sélectionné ; les aperçus montrent des actions de case à cocher, de texte et de copie de champ."><figcaption><p>Modifiez un champ ou copiez son contenu.</p></figcaption></figure>

## Document

Choisissez **Approve the Document** ou **Reject the Document** lorsque le workflow doit prendre cette décision. Utilisez d'abord une condition **And** si l'approbation doit dépendre d'un contrôle. Consultez [Document](document/).

<figure><img src="../../../../.gitbook/assets/then-category-document-en.png" alt="Sélecteur de cartes Then en anglais avec Document sélectionné ; les aperçus Approve the Document et Reject the Document sont visibles."><figcaption><p>Approuvez ou rejetez le document en cours.</p></figcaption></figure>

## Logic

Utilisez ces cartes pour convertir des valeurs entre les formats nombre, texte et booléen, ou pour lire une valeur dans du JSON. Choisissez les champs d'entrée et de sortie sur la carte sélectionnée.

<figure><img src="../../../../.gitbook/assets/then-category-logic-en.png" alt="Sélecteur de cartes Then en anglais avec Logic sélectionné ; les aperçus visibles convertissent des types de données et lisent des valeurs dans du JSON."><figcaption><p>Transformez des valeurs pour une étape ultérieure du workflow.</p></figcaption></figure>

## Status

Choisissez **Change Status** pour faire passer le document à un statut sélectionné. La carte peut également déclencher un autre workflow. Consultez [Status](status/).

<figure><img src="../../../../.gitbook/assets/then-category-status-en.png" alt="Sélecteur de cartes Then en anglais avec Status sélectionné ; l&#x27;aperçu Change Status comprend un champ de statut et un déclenchement de workflow facultatif."><figcaption><p>Faites passer le document à un autre statut.</p></figcaption></figure>

## Prompts and Scripts

Choisissez cette catégorie pour exécuter un script de prompt DocOperator. Sélectionnez le script et les variables demandées par la carte. La carte propose également des paramètres d'exécution, tels que les nouvelles tentatives.

<figure><img src="../../../../.gitbook/assets/then-category-prompts-scripts-en.png" alt="Sélecteur de cartes Then en anglais avec Prompts and Scripts sélectionné ; l&#x27;aperçu d&#x27;un script de prompt DocOperator est visible."><figcaption><p>Exécutez un script de prompt DocOperator configuré.</p></figcaption></figure>

## Export

Lancez un export, exportez avec une configuration choisie, ou placez un export final en file d'attente. Choisissez la configuration d'export et l'option de tâche en attente affichées sur votre carte. Consultez [Export](export/).

<figure><img src="../../../../.gitbook/assets/then-category-export-en.png" alt="Sélecteur de cartes Then en anglais avec Export sélectionné ; les aperçus montrent des exports de démarrage, configuré, en file d&#x27;attente et alternatif."><figcaption><p>Sélectionnez quand et comment le document est exporté.</p></figcaption></figure>

## Task

Créez une tâche ou une notification et assignez-la à un utilisateur ou à un groupe. Saisissez le titre, la description, la priorité et les paramètres de notification demandés par la carte. Certaines cartes assignent de manière séquentielle. Consultez [Task](task/).

<figure><img src="../../../../.gitbook/assets/then-category-task-en.png" alt="Sélecteur de cartes Then en anglais avec Task sélectionné ; les aperçus visibles créent ou assignent des tâches et des notifications."><figcaption><p>Créez un travail de suivi pour une personne ou un groupe.</p></figcaption></figure>

## Email

Envoyez un e-mail à partir d'un modèle sélectionné, soit à des destinataires, soit à des groupes. Choisissez le modèle et la destination sur la carte.

<figure><img src="../../../../.gitbook/assets/then-category-email-en.png" alt="Sélecteur de cartes Then en anglais avec Email sélectionné ; les aperçus envoient un e-mail basé sur un modèle à des destinataires ou à des groupes."><figcaption><p>Envoyez un e-mail basé sur un modèle.</p></figcaption></figure>

## Table

Modifiez des entrées ou calculez des valeurs dans un tableau du document. Sélectionnez le tableau, les colonnes, l'opérateur et la colonne de résultat demandés par la carte. Consultez [Table](table/).

<figure><img src="../../../../.gitbook/assets/then-category-table-en.png" alt="Sélecteur de cartes Then en anglais avec Table sélectionné ; les aperçus modifient des entrées et calculent des colonnes de résultat."><figcaption><p>Mettez à jour ou calculez des données de tableau.</p></figcaption></figure>

## Assignee

Assignez le document à un utilisateur, un groupe, un destinataire ou une sous-organisation. Certaines cartes utilisent un champ ou une table de décision et proposent une solution de repli. Choisissez la bonne destination et la bonne solution de repli sur la carte sélectionnée. Consultez [Assignee](assignee/).

<figure><img src="../../../../.gitbook/assets/then-category-assignee-en.png" alt="Sélecteur de cartes Then en anglais avec Assignee sélectionné ; les aperçus visibles assignent un utilisateur, un destinataire, un groupe ou un contact fournisseur."><figcaption><p>Acheminez le document vers la prochaine personne ou le prochain groupe responsable.</p></figcaption></figure>

## Action

Exécutez un autre workflow, envoyez une requête HTTPS, appelez une API ou utilisez la carte de calcul d'augmentation des coûts. Ces actions peuvent affecter d'autres systèmes ; demandez à votre administrateur quel point de terminaison et quels paramètres utiliser. Consultez [Action](action/).

<figure><img src="../../../../.gitbook/assets/then-category-action-en.png" alt="Sélecteur de cartes Then en anglais avec Action sélectionné ; les aperçus montrent Run workflow, une requête HTTPS, un appel d&#x27;API et le calcul d&#x27;augmentation des coûts."><figcaption><p>Démarrez un autre workflow ou une action d'intégration.</p></figcaption></figure>
