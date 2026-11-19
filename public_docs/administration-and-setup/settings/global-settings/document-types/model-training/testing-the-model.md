# Tester le modèle

## Évaluez avec des documents de test indépendants

<figure><picture><source srcset="../../../../../.gitbook/assets/intro-process-05-modelltest-fr-dark-20261029.png" media="(prefers-color-scheme: dark)"><img src="../../../../../.gitbook/assets/intro-process-05-modelltest-fr-light-20261029.png" alt="Évaluez avec des documents de test indépendants"></picture><figcaption><p>Évaluez avec des documents de test indépendants</p></figcaption></figure>

Les données d’entraînement et les documents de test servent à des fins différentes. Pour les documents de test indépendants, définissez les types de documents et les valeurs de champ attendus, puis comparez-les aux prédictions. Enregistrez la version du modèle, l'échantillon, les écarts et les défaillances techniques. Apportez des améliorations ciblées et répétez le test avec le même protocole d’évaluation. Les valeurs indiquées sont un exemple et non une mesure de précision.


Utilisez des documents représentatifs qui n’ont pas servi à entraîner le modèle. Préparez pour chacun les réponses attendues : type de document et, si vous évaluez l’extraction, valeurs des champs.

## Réaliser l’évaluation

1. Ouvrez l’entraînement du modèle pour le type de document à examiner.
2. Choisissez le test de classification si votre version propose cette fonction.
3. Sélectionnez l’échantillon et lancez l’évaluation avec les options disponibles.
4. Attendez la fin et consignez les résultats et les erreurs. Un échec technique ou une évaluation incomplète ne constitue pas une classification correcte.

<figure><img src="../../../../../.gitbook/assets/testing-the-model-overview-fr-20261113.png" alt="Entraînement du modèle du type de document Facture en français, version 11.27.7, avec des valeurs d’exemple : les indicateurs Échantillon entraîné, Exporté, Société ∑ et Global ∑, les actions Importer, Entraîner le modèle et Test de classification ainsi que la liste des documents d’entraînement. Aucun entraînement n’a été lancé."><figcaption><p>Entraînement du modèle du type de document Facture en français, version 11.27.7, avec des valeurs d’exemple : les actions Importer, Entraîner le modèle et Test de classification ainsi que la liste des documents d’entraînement ; aucun entraînement n’a été lancé.</p></figcaption></figure>

La vue propose trois actions et la liste des documents d’entraînement. Les pages suivantes décrivent où mène chaque action :

- **Importer** ouvre la sélection de nouvelles données d’entraînement : [Importer des documents d’exemple pour l’entraînement du modèle](import-data-model-training.md).
- **Entraîner le modèle** démarre l’entraînement pour le type de document : [Objectif et utilisation : entraînement du modèle](purpose-and-use-model-training.md).
- **Test de classification** lance le contrôle décrit dans la section « Réaliser l’évaluation » ci-dessus.
- Les indicateurs **Échantillon entraîné**, **Exporté**, **Société ∑** et **Global ∑** sont expliqués dans [Entraînement du modèle](README.md).
- Le menu de la colonne **Actions** supprime un document d’entraînement : [Gérer les données d’entraînement](manage-training-data.md).

## Interpréter les résultats

Comparez les prédictions aux réponses attendues et analysez les erreurs par catégorie et format. Si vous calculez l’exactitude, la précision, le rappel ou le score F1, indiquez la taille de l’échantillon et les catégories évaluées. N’attribuez pas au produit des métriques que votre version n’affiche pas ; vous pouvez les calculer séparément à partir des résultats enregistrés ou exportés.

Les règles de classification et d’extraction sont des configurations distinctes de l’entraînement. Vérifiez leur effet lorsqu’elles interviennent dans le traitement ; ne modifiez pas une règle uniquement pour masquer une erreur de l’échantillon de test.

## Corriger et répéter

Corrigez les données d’entraînement, les étiquettes ou les réglages réellement disponibles, puis entraînez de nouveau le modèle si nécessaire. Répétez le même protocole et conservez un échantillon indépendant. Consignez la version, les données, les résultats et les régressions. Un bon résultat sur l’échantillon ne garantit pas les mêmes performances sur tous les documents futurs.
