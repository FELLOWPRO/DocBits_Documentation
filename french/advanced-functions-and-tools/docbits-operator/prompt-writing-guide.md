# Guide d'écriture de prompt

Ce guide explique comment rédiger des prompts efficaces pour l'opérateur DocBits. Les prompts sont des instructions étape par étape qui dirigent l'opérateur pour effectuer des tâches spécifiques, telles que la navigation sur des pages web, l'interaction avec des éléments d'interface utilisateur et la saisie de données.

## Qu'est-ce qu'un Prompt?

Un prompt est une séquence d'instructions rédigées en texte qui guide l'opérateur pour exécuter un flux de travail. Les prompts peuvent inclure des commandes telles que cliquer sur des boutons, remplir des formulaires, attendre le chargement de pages ou d'éléments, et plus encore.

## Syntaxe et Structure du Prompt

* Chaque instruction doit être rédigée comme une étape numérotée.
* Utilisez un langage clair et concis pour décrire chaque action.
* Spécifiez les éléments d'interface utilisateur par leur nom, leur libellé ou leur numéro d'index pour assurer la précision.
* Utilisez une mise en forme cohérente pour améliorer la lisibilité.

## Utilisation de Variables dans les Prompts

Les variables vous permettent de rendre les prompts dynamiques en insérant différentes valeurs à l'exécution. Au lieu de coder en dur des valeurs comme des dates ou des numéros de document, utilisez des espaces réservés à l'intérieur de crochets, par exemple : `{invoice_number}`, `{url}`, ou `{purchase_order}`.

Cela rend les prompts réutilisables et adaptables à travers différents flux de travail ou ensembles de données.

### Comment Utiliser les Variables

* Écrivez les variables à l'intérieur de crochets dans votre texte de prompt :
  * Saisissez le numéro de facture : {invoice\_number} dans le champ 'Numéro de facture HP'.
* Chaque variable doit avoir un nom unique (par exemple, `invoice_number`, `url`, `document_type`).
* Les noms de variables ne doivent pas inclure d'espaces ou de caractères spéciaux (les tirets bas sont autorisés).
* Pour les flux de travail, les noms de variables doivent correspondre exactement aux identifiants de champ du document pour permettre la cartographie automatique des données.

## Popup des Variables de Prompt

Pour ouvrir le popup des variables de prompt, cliquez sur l'icône **roue dentée** située à côté du champ de saisie du prompt.

![](https://docs.docbits.com/~gitbook/image?url=https%3A%2F%2F578966019-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FT2n2w4uDCJvv7CJ5zrdk%252Fuploads%252FvEC6vmU6CCsAa36OK9V6%252Fimage.png%3Falt%3Dmedia%26token%3Dfd26ce70-0de4-4bdb-adf4-85d0052f9d53\&width=768\&dpr=4\&quality=100\&sign=fc29eaa3\&sv=2)

## Mise en Page et Contrôles du Popup

![](https://docs.docbits.com/~gitbook/image?url=https%3A%2F%2F578966019-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FT2n2w4uDCJvv7CJ5zrdk%252Fuploads%252FftlMKp0ql0miqBTdCtt3%252Fimage.png%3Falt%3Dmedia%26token%3D979b7c8e-0728-4a10-bb8a-3275203c4c3d\&width=768\&dpr=4\&quality=100\&sign=b07844a9\&sv=2)

* **Champ de Saisie de Clé :** Saisissez le nom de la variable ici (sans les crochets).
* **Champ de Saisie de Valeur :** Saisissez la valeur à utiliser pour cette variable lorsque le prompt s'exécute.
* **Enregistrer comme Sensible (Case à cocher) :** Lorsqu'elle est cochée, cela marque la valeur de la variable comme sensible. Les valeurs sensibles sont cryptées et masquées dans les flux de travail pour protéger les informations confidentielles des utilisateurs non autorisés.
* **Bouton Ajouter (+) :** Cliquez pour ajouter une autre ligne de saisie de paire clé-valeur.
* **Icône de Suppression (Poubelle) :** Lorsque plusieurs paires clé-valeur existent, toutes les paires, sauf la première, affichent une petite icône de poubelle pour supprimer cette paire spécifique.
* **Bouton Effacer :** Réinitialise le popup en effaçant toutes les paires clé-valeur et les valeurs saisies.
* **Bouton Enregistrer :** Enregistre toutes les variables définies et leurs valeurs pour le prompt actuel.
