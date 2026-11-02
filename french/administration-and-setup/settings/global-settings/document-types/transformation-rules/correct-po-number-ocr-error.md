# Corriger une erreur OCR dans un numéro de commande

Le troisième caractère de `06O123` est la **lettre O**. Si l'extraction produit `060123`, utilisez une transformation conditionnelle de préfixe pour corriger ce schéma connu sans script personnalisé.

## Configurer la correction du préfixe

1. Ouvrez **Paramètres → Types de documents → roue dentée → Règles de transformation → Gérer les règles de transformation**. Un administrateur de l'organisation doit activer la fonction pour le type sélectionné.
2. Créez une règle de **champ d'en-tête** avec le **Numéro de commande (`Purchase Order`)** comme cible. Lisez depuis **le champ lui-même**.
3. Pour l'exécution conditionnelle, sélectionnez le numéro de commande, **commence par** et `060`.
4. Supprimez l'étape initiale de suppression des espaces. Ajoutez **Affixe → Retirer le préfixe → `060`**, puis **Affixe → Ajouter le préfixe → `06O`**. Saisissez la lettre O majuscule dans la deuxième étape. La condition limite les deux opérations au préfixe concerné ; les autres caractères sont conservés.
5. Vérifiez l'aperçu, enregistrez la règle et rouvrez-la. Testez un document, enregistrez-le, puis rechargez-le pour vérifier le numéro de commande conservé.

## Vérifier le résultat

| Exemple d'entrée | Résultat attendu | Raison |
| --- | --- | --- |
| `060123` | `06O123` | Préfixe concerné |
| `060987` | `06O987` | Autre valeur concernée ; suffixe conservé |
| `06O123` | `06O123` | Déjà correct ; condition non satisfaite |
| `160123` | `160123` | Préfixe différent ; condition non satisfaite |
| `1060123` | `1060123` | `060` à l'intérieur de la valeur n'est pas un préfixe correspondant |

Cet exemple corrige un schéma d'extraction connu. Il ne prouve ni la précision de l'OCR, ni l'existence de la commande, ni la réussite du rapprochement. Utilisez la règle uniquement si la convention de numérotation exige `06O` : un préfixe `060` légitime serait également modifié. Ajoutez des conditions fournisseur si la convention ne s'applique qu'à certains fournisseurs.

## Pourquoi deux étapes d'affixe ?

L'éditeur actuel exige un champ source distinct pour les étapes dépendant de la position, comme **Rechercher et remplacer**, même avec **Exécuter une seule fois par document** activé. Les deux étapes de préfixe fonctionnent sur le même champ. Après correction, la valeur ne commence plus par `060` : la condition empêche donc une nouvelle modification lors des enregistrements suivants.
