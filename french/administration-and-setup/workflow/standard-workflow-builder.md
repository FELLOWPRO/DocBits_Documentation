# Standard Workflow

Le constructeur **Standard Workflow** est l'éditeur linéaire, basé sur des cartes, qui permet d'automatiser le traitement des documents. Un workflow est composé de trois groupes de cartes — **When** (le déclencheur), **And** (des conditions supplémentaires) et **Then** (les actions à exécuter). Lorsqu'un document satisfait les conditions When/And, les actions Then s'exécutent automatiquement.

## Comment y accéder

Ouvrez **Workflow Dashboard → Workflow List**, puis cliquez sur **Add Workflow** pour créer un nouveau workflow Standard, ou cliquez sur un workflow existant pour le modifier.

<figure><img src="../../.gitbook/assets/workflow_list.png" alt="Workflow List avec le type, l'ordre d'exécution et le déclencheur"><figcaption><p>La Workflow List — chaque ligne est un workflow que vous pouvez ouvrir, activer/désactiver ou modifier.</p></figcaption></figure>

## Le modèle When / And / Then

<figure><img src="../../.gitbook/assets/workflow_designer_cards.png" alt="Canevas du Standard Workflow avec des cartes When, And et Then"><figcaption><p>Le canevas du Standard Workflow. Cet exemple se déclenche sur les factures d'une sous-organisation et les assigne à un utilisateur.</p></figcaption></figure>

- **When** — le déclencheur qui démarre le workflow (par ex. *Document type is Invoice*).
- **And** — des conditions supplémentaires qui doivent également être vraies (par ex. *Document is part of sub-organization*). Laissez vide pour exécuter le workflow à chaque correspondance de la carte When.
- **Then** — les actions à effectuer (par ex. *Assign the document to the user*, créer une tâche, appeler une API, envoyer un e-mail).

## Ajouter des cartes

Cliquez sur **Add Card** dans n'importe quel groupe pour ouvrir la bibliothèque de cartes. Les cartes sont organisées par catégorie afin que vous puissiez trouver le bloc de construction dont vous avez besoin :

<figure><img src="../../.gitbook/assets/workflow_add_card_picker.png" alt="Bibliothèque Add Card regroupée par catégorie"><figcaption><p>La bibliothèque <strong>Add Card</strong> — cartes de condition, cartes de comparaison, cartes d'action et plus encore, regroupées par catégorie.</p></figcaption></figure>

Enregistrez avec **Save Workflow**, ou enregistrez la disposition comme modèle réutilisable avec **Save Template**.

## Étapes suivantes

- Découvrez ce que fait chaque carte dans la section **Cards**.
- Combinez des cartes en solutions éprouvées avec les **Workflow Pattern Guides**.
- Pour des flux avec branches et chemins parallèles (Wait ALL / Wait ANY / OR), utilisez le constructeur **Advanced Workflow**.
