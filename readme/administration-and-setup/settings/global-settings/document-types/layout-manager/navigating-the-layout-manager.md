# Naviguer dans le Layout Builder

Utilisez le **Layout Builder** pour organiser les champs et les groupes que les utilisateurs voient sur un document. Ce guide utilise la mise en page anglaise de **Invoice** dans une organisation sandbox.

## Ouvrir la mise en page Invoice

1. Allez dans **Settings → Document Types**.
2. Trouvez **Invoice** et sélectionnez **Layouts** sur sa carte. Le Layout Builder s'ouvre pour ce type de document.
3. Vérifiez le sélecteur de mise en page en haut à gauche. L'exemple ci-dessous affiche **DEFAULT**.

<figure><img src="../../../../../.gitbook/assets/dbdc177-document-types-en.png" alt="Page Document Types en anglais avec la carte Invoice et son lien Layouts"><figcaption>Ouvrez **Layouts** depuis la carte Invoice.</figcaption></figure>

## Trouver les groupes et les champs

Le panneau **Elements** à gauche comporte trois sections. **Groups** répertorie les sections du document ; le canevas central montre leur disposition actuelle. Sélectionnez un champ dans le canevas et ouvrez **Properties** pour modifier ses paramètres d'affichage. Voir [Configuring Field Properties](configuring-field-properties.md) pour les options disponibles.

<figure><img src="../../../../../.gitbook/assets/dbdc177-layout-elements-en.png" alt="Layout Builder de Invoice en anglais avec Groups dans le panneau Elements et les champs groupés dans le canevas"><figcaption>La liste Groups et le canevas de la mise en page Invoice.</figcaption></figure>

Ouvrez **Fields** pour trouver les champs de document disponibles. Utilisez sa zone de recherche lorsque la liste est longue, puis faites glisser le champ vers le groupe souhaité dans le canevas. Les champs déjà placés dans la mise en page peuvent apparaître comme indisponibles dans la liste.

<figure><img src="../../../../../.gitbook/assets/dbdc177-layout-fields-en.png" alt="Panneau Fields du Layout Builder en anglais avec la recherche et les champs Invoice disponibles"><figcaption>Recherchez parmi les champs disponibles avant d'en placer un.</figcaption></figure>

Ouvrez **Form Elements** pour les contrôles visuels tels que Text, Label, Check Box, séparateur, Button et Sub Group. Faites glisser l'élément dont vous avez besoin dans le canevas, puis vérifiez ses **Properties**.

<figure><img src="../../../../../.gitbook/assets/dbdc177-layout-form-elements-en.png" alt="Panneau Form Elements du Layout Builder en anglais répertoriant les textes, libellés, cases à cocher, boutons et sous-groupes"><figcaption>La palette Form Elements actuelle.</figcaption></figure>

## Organiser et enregistrer

- Sélectionnez le titre d'un groupe dans le canevas pour le modifier. Le **+** au-dessus du canevas ajoute un groupe ; l'icône d'accolades adjacente ouvre le formulaire de groupe JSON avancé.
- Survolez un groupe pour accéder aux actions copier le JSON, monter, descendre, supprimer et à la poignée de déplacement. Pour réorganiser les champs, faites-les glisser dans un groupe ou d'un groupe à l'autre.
- Sélectionnez un champ dans le canevas pour ouvrir **Properties**. Son icône de suppression le retire de cette mise en page. Pour configurer la validation, l'OCR ou la correspondance, utilisez les [paramètres Fields](../fields/configuring-field-properties-1.md) distincts.
- Sélectionnez **Save** dans la barre supérieure après la modification. Consultez [Save and Apply Changes](save-and-apply-changes.md) avant d'utiliser les autres actions de la barre supérieure, notamment la génération de modèles, les modèles par défaut et l'application d'une mise en page aux origines.
