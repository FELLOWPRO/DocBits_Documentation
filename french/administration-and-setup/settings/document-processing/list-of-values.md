# Listes de valeurs

## Tutoriel vidéo : données de base et listes de valeurs

{% embed url="https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/master-data-lists-admin/v1/fr.mp4" %}
Sources de données de base, listes de valeurs et paramètres des données de base dans DocBits
{% endembed %}

La vidéo présente les sources de données de base, les listes de valeurs et les paramètres des données de base d'un type de document.

Les listes de valeurs proposent des options prédéfinies pour les champs des documents. Un champ peut utiliser une liste pendant la validation. Les libellés peuvent être traduits ; la valeur technique reste identique dans toutes les langues.

## Ouvrir les listes

Dans les paramètres, ouvrir les données de référence et les listes de valeurs. Sélectionner une liste pour consulter ses entrées. Les noms configurés sont masqués dans l’image.

<figure><img src="../../../.gitbook/assets/s150-list_of_values_1-fr.png" alt="Vue des listes de valeurs avec les noms configurés masqués."><figcaption><p>Vue des listes de valeurs avec les noms configurés masqués.</p></figcaption></figure>

## Créer une liste

1. Choisir la création d’une nouvelle liste.
2. Saisir un nom et, si nécessaire, limiter la liste à une sous-organisation.
3. Vérifier les informations avant d’enregistrer.

Les listes standard sont fournies par le système et ne peuvent pas être supprimées. Avant de supprimer une liste personnalisée, vérifier quels champs l’utilisent : l’action peut prendre effet immédiatement.

## Ajouter et modifier les entrées

Ouvrir la liste prévue et ajouter une ligne. Vérifier les propriétés de chaque entrée :

| Propriété | Signification |
| --- | --- |
| Valeur | Valeur technique stockée par DocBits, identique dans toutes les langues. |
| Libellé | Texte affiché dans la langue choisie. Sans libellé pour la langue active, la valeur technique est affichée. |
| Langue | Langue du libellé. |
| Sous-organisations | Périmètre de disponibilité de l’entrée ; sans restriction, elle s’applique à toutes les sous-organisations. |
| Synonymes | Variantes associées à la valeur, par exemple EURO et € pour EUR. Confirmer chaque synonyme dans le champ prévu. |

Vérifier toutes les propriétés avant d’enregistrer. Les commandes de modification et de suppression dépendent des droits et de l’entrée sélectionnée. Les entrées système ne peuvent pas être supprimées.

## Importer un fichier CSV

Ouvrir les actions de la liste prévue et l’import CSV. Sélectionner le fichier et le séparateur approprié, par exemple `;` ou `,`. Vérifier la structure et le contenu du fichier avant de lancer l’import.

## Ajouter des traductions

Pour une entrée, ajouter une langue et saisir le libellé prévu. Répéter pour les autres langues nécessaires, puis vérifier et enregistrer. Les entrées système peuvent recevoir des libellés traduits même lorsqu’elles ne peuvent pas être supprimées.

La traduction du libellé ne modifie pas la valeur technique. Après les modifications prévues, vérifier le champ en validation dans la langue souhaitée. L’image montre la consultation des listes ; elle ne prouve aucune modification enregistrée ni aucun import exécuté.
