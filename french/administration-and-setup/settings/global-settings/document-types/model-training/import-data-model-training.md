# Importer des données : entraînement du modèle

Préparez des documents représentatifs des formats, langues et types traités par votre organisation. Utilisez les formats de fichiers acceptés par votre installation. Écartez les doublons et séparez les documents destinés à l’entraînement de ceux réservés à l’évaluation.

## Ouvrir l’importation

Ouvrez l’entraînement du modèle dans les réglages du type de document concerné, puis la fonction d’importation.

<figure><img src="../../../../../.gitbook/assets/site-extra-model-training-overview-fr.png" alt="Vue générale de l’entraînement du modèle dans la version illustrée. Aucune importation, aucun entraînement ni test de performance n’a été lancé."><figcaption><p>Vue générale de l’entraînement du modèle dans la version illustrée. Aucune importation, aucun entraînement ni test de performance n’a été lancé.</p></figcaption></figure>

## Choisir les formats et les fichiers

Sélectionnez le format des montants et des dates adapté aux documents, puis les fichiers à importer. Par exemple, `1.234,56` et `1,234.56` utilisent des séparateurs différents ; `05/06/2026` doit également être interprété selon le format choisi.

<figure><img src="../../../../../.gitbook/assets/site-extra-model-import-dialog-fr.png" alt="Formulaire d’importation sans fichier sélectionné. Le titre natif Téléchargeur de documents Téléchargeur contient une répétition ; il s’agit de l’importation des documents. Aucun fichier n’a été envoyé."><figcaption><p>Formulaire d’importation sans fichier sélectionné. Le titre natif Téléchargeur de documents Téléchargeur contient une répétition ; il s’agit de l’importation des documents. Aucun fichier n’a été envoyé.</p></figcaption></figure>

Vérifiez votre sélection avant de lancer l’importation. Attendez la fin du traitement et contrôlez les erreurs ainsi que le type de document affecté. Corrigez les erreurs de classification et d’extraction avant d’utiliser les exemples pour l’entraînement.

## Entraîner et évaluer

Utilisez les fonctions et autorisations disponibles dans votre version. Évaluez ensuite le résultat avec un échantillon indépendant. Ajouter des documents ne garantit pas à lui seul une amélioration de la précision. Consultez [Tester le modèle](testing-the-model.md).

Les illustrations montrent les contrôles disponibles et un formulaire vide : aucun fichier n’a été envoyé, aucun entraînement n’a été lancé et aucun résultat de performance n’a été mesuré pendant cette vérification.
