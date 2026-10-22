# Importer des données : entraînement du modèle

Préparez des documents représentatifs des formats, langues et types que votre organisation doit traiter. Utilisez uniquement des fichiers dans les formats acceptés par votre installation. Évitez les doublons et séparez les documents d’entraînement des documents réservés à l’évaluation.

## Accéder à l’import

Dans les paramètres du type de document concerné, ouvrez l’entraînement du modèle, puis choisissez **Importer**.

<figure><img src="../../../../../.gitbook/assets/site-extra-model-training-overview-fr.png" alt="Vue de l’entraînement du modèle avec les commandes Importer, Entraîner le modèle et Test de classification. Aucun entraînement ni test n’a été exécuté ; cette vue ne présente pas un résultat de précision. Le titre de colonne Name reste en anglais dans le produit."><figcaption><p>Vue de l’entraînement du modèle avec les commandes Importer, Entraîner le modèle et Test de classification. Aucun entraînement ni test n’a été exécuté ; cette vue ne présente pas un résultat de précision. Le titre de colonne Name reste en anglais dans le produit.</p></figcaption></figure>

## Choisir le format et les fichiers

Choisissez le format des montants et des dates correspondant réellement aux fichiers, puis sélectionnez les documents à importer. Par exemple, `1.234,56` et `1,234.56` n’utilisent pas les mêmes séparateurs ; une date comme `05/06/2026` doit être interprétée selon le format choisi.

<figure><img src="../../../../../.gitbook/assets/s150-image-85-1-fr.png" alt="Fenêtre d’import des documents : format des montants et des dates. Le libellé de l’interface « Téléchargeur » désigne ici un envoi vers DocBits ; aucun fichier n’a été envoyé pendant la capture."><figcaption><p>Fenêtre d’import des documents : format des montants et des dates. Le libellé de l’interface « Téléchargeur » désigne ici un envoi vers DocBits ; aucun fichier n’a été envoyé pendant la capture.</p></figcaption></figure>

Vérifiez la sélection avant de lancer l’import. Attendez la fin du traitement et contrôlez les erreurs ainsi que le type de document attribué. Corrigez les exemples mal classés ou mal extraits avant de les utiliser pour l’entraînement.

## Entraîner et évaluer

Une fois les données contrôlées, utilisez la commande **Entraîner le modèle** selon les droits et fonctions de votre version. Évaluez ensuite le résultat sur un échantillon distinct : l’ajout de documents ne garantit pas à lui seul une meilleure précision. Consultez [Tester le modèle](testing-the-model.md).
