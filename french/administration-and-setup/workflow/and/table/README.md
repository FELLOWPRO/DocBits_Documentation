# Tableau

Les cartes de cette catégorie dans le sélecteur **Ajouter une carte** du Workflow Builder :

<figure><img src="../../../../.gitbook/assets/workflow-card-qa-20261021-category-526dc164847b-fr.png" alt="Cartes disponibles dans la catégorie sélectionnée. Renseignez les champs avant utilisation. Certains libellés de cette version de la carte ont encore une traduction incomplète ou incorrecte dans l’interface. Les explications de cette page emploient les termes corrects."><figcaption><p>Cartes disponibles dans la catégorie sélectionnée. Renseignez les champs avant utilisation. Certains libellés de cette version de la carte ont encore une traduction incomplète ou incorrecte dans l’interface. Les explications de cette page emploient les termes corrects.</p></figcaption></figure>

<!-- workflow-card-example-condition_table_column_exists-20261021 -->

### La table du document contient une colonne

<figure><img src="../../../../.gitbook/assets/workflow-card-qa-20261021-card-extra-bf66d05be645-fr.png" alt="Champs de la carte dans la version affichée. Les champs ne sont pas encore renseignés." width="563"><figcaption><p>Champs de la carte dans la version affichée. Les champs ne sont pas encore renseignés.</p></figcaption></figure>

`CONDITION_TABLE_COLUMN_EXISTS` · version 2

Sélectionnez la table `lines`, la colonne `article_number` et l'opérateur existe. Une table remplie contenant cette colonne passe ; la même table sans la colonne échoue à la comparaison d'existence. Un tableau absent ou vide peut produire un résultat de données manquantes et ne constitue pas la preuve d'une comparaison négative réussie.

<!-- workflow-card-example-condition_compare_table_date_to_current_date-20261021 -->

### Dates dans un tableau par rapport à la date de référence

<figure><img src="../../../../.gitbook/assets/workflow-card-qa-20261021-card-extra-05a199670bd2-fr.png" alt="Champs de la carte dans la version affichée. Les champs ne sont pas encore renseignés." width="563"><figcaption><p>Champs de la carte dans la version affichée. Les champs ne sont pas encore renseignés.</p></figcaption></figure>

`CONDITION_COMPARE_TABLE_DATE_TO_CURRENT_DATE` · version 2

Pour la date de référence `2026-10-21`, comparez le tableau `lines`, la colonne `delivery_date`, plus tard que, Tout et la tolérance zéro jour. Les lignes datées `2026-10-22` et `2026-10-23` satisfont à la comparaison. Une ligne datée de `2026-10-20` fait échouer All. Testez les dates manquantes et invalides séparément.
