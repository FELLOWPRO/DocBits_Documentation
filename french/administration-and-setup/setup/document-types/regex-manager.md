# Gestionnaire Regex

Cette fonction de DocBits vous offre une alternative à la classification par modèle : elle permet d’écrire des expressions régulières de recherche pour un type de document, à des fins de classification et d’autres usages.

Type de document : le gestionnaire Regex vous permet d’écrire des expressions régulières, qui sont ensuite recherchées dans le document. Si DocBits trouve une correspondance avec l’expression régulière d’un document défini, il classe le document dans le type de document correspondant. Par exemple, si vous écrivez une expression régulière pour trouver « Gutschrift » et que DocBits trouve ce terme dans un document, il le classera comme avoir.

Origine du document : grâce aux expressions régulières, DocBits reconnaît aussi le pays d’origine d’un document. Par exemple, si une expression régulière pour un document espagnol contient le terme « Factura » et que DocBits trouve ce terme dans le document, il saura que le document est d’origine espagnole et le classera en conséquence.

## **Accéder au gestionnaire Regex**

Dans DocBits, ouvrez Paramètres → Types de documents. Sous « Types de documents personnalisés », cliquez sur « Nouveau ». Saisissez un nom pour le type de document, ajoutez une description facultative et cochez « Tableau disponible » si le document contient un tableau. Choisissez ensuite « Expression régulière » au lieu de « Auto » et cliquez sur « Suivant ».

<figure><img src="../../../.gitbook/assets/regex-manager-create-fr-20261006.png" alt="Page de création d’un nouveau type de document avec le champ de nom, la case Tableau disponible, la description et les boutons Auto et Expression régulière"><figcaption><p>Choisissez « Expression régulière » pour classer le nouveau type de document avec des expressions régulières.</p></figcaption></figure>

## **Ajouter et supprimer des regex**

L’étape « Expression régulière » affiche les modèles regex existants, chacun avec son origine et son motif, ainsi qu’un bouton « Ajouter » pour créer un nouveau modèle. Utilisez le menu d’actions en fin de ligne pour gérer l’entrée concernée. Cliquez sur « Suivant » pour passer à « Champs et groupes ».

<figure><img src="../../../.gitbook/assets/regex-manager-list-fr-20261006.png" alt="Étape Expression régulière avec le bouton Ajouter et un tableau de trois modèles regex avec origine, motif et actions"><figcaption><p>Modèles regex existants avec origine et motif. « Ajouter » en crée un nouveau.</p></figcaption></figure>
