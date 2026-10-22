# Tester le modèle

Un test doit mesurer le résultat sur des documents représentatifs qui n’ont pas servi à l’entraînement. Préparez pour chacun les réponses attendues : type de document et, pour une évaluation de l’extraction, valeurs des champs.

## Exécuter le test

1. Ouvrez l’entraînement du type de document à évaluer.
2. Choisissez **Test de classification** lorsque cette commande est disponible dans votre version.
3. Sélectionnez l’échantillon de test et lancez l’évaluation selon les options proposées.
4. Attendez la fin du traitement et relevez les résultats et les erreurs. Une erreur technique ou un test incomplet ne vaut pas une classification correcte.

<figure><img src="../../../../../.gitbook/assets/site-extra-model-training-overview-fr.png" alt="Vue de l’entraînement du modèle avec les commandes Importer, Entraîner le modèle et Test de classification. Aucun entraînement ni test n’a été exécuté ; cette vue ne présente pas un résultat de précision. Le titre de colonne Name reste en anglais dans le produit."><figcaption><p>Vue de l’entraînement du modèle avec les commandes Importer, Entraîner le modèle et Test de classification. Aucun entraînement ni test n’a été exécuté ; cette vue ne présente pas un résultat de précision. Le titre de colonne Name reste en anglais dans le produit.</p></figcaption></figure>

## Interpréter les résultats

Comparez les prédictions aux réponses attendues. Relevez les erreurs par type de document et par format. Si vous calculez l’exactitude, la précision, le rappel ou le score F1, indiquez aussi la taille de l’échantillon et les catégories évaluées. N’attribuez pas au produit une métrique que l’écran de votre version ne fournit pas : vous pouvez la calculer séparément à partir des résultats exportés ou relevés.

Les règles de classification et d’extraction sont des réglages distincts de l’entraînement. Vérifiez leur effet si elles interviennent dans le traitement ; ne modifiez pas une règle simplement pour masquer un échec sur l’échantillon de test.

## Corriger puis refaire le test

Corrigez les données d’entraînement, leurs libellés ou les paramètres réellement accessibles dans votre installation, puis entraînez à nouveau si nécessaire. Refaites le test avec le même protocole et conservez un échantillon indépendant. Documentez la version, les données utilisées, les résultats et les régressions. Une bonne performance sur cet échantillon ne garantit pas le même résultat sur tous les futurs documents.
