# Modifier et enregistrer des modèles Regex

## Guide pour modifier les modèles existants et importance de tester ces modifications afin de s'assurer qu'elles fonctionnent comme prévu sans casser les fonctionnalités existantes.

**Pour modifier des modèles regex existants et vous assurer que les changements fonctionnent comme prévu sans casser les fonctionnalités existantes, vous pouvez suivre le guide ci-dessous :**

<figure><img src="../../../../../.gitbook/assets/Bildschirmfoto 2024-05-22 um 12.46.56.png" alt=""><figcaption><p>Settings: Document Type</p></figcaption></figure>

<figure><img src="../../../../../.gitbook/assets/Bildschirmfoto 2024-05-22 um 14.18.25.png" alt=""><figcaption></figcaption></figure>

**Analyser le modèle existant :**

* Examinez le modèle regex existant pour comprendre quelles données il capture et comment il fonctionne.
* Identifiez les parties du modèle qui doivent être modifiées et l'impact de ces modifications sur les données capturées.

**Par exemple : le montant de la facture doit être lu :**

*   (?<=Rechnungsbetrag:)\[\s]\*((((\d+)\[,.]{1,10})+\d{0,2})|(\d+(?!,)))

    Rechnungsbetrag: 100.00
*   Lire le montant avec le point comme séparateur des milliers, mais NE PAS laisser passer le point

    \[\d.]_\[,\d]_

    Caractères autorisés : 0123456789,
*   La valeur « P32180 » doit être lue. Le mot d'ancrage est ici « Invoice Date ».

    (?<=InvoiceDate )\[\s]\*P\d{5}

    Customer number Invoice number Invoice date P32180 613976 05/13/2019

<figure><img src="../../../../../.gitbook/assets/image (108).png" alt=""><figcaption></figcaption></figure>

**Documenter les modifications :**

* Prenez des notes sur les modifications que vous prévoyez d'apporter au modèle regex.
* Notez les nouveaux motifs que vous prévoyez d'ajouter et les parties du modèle existant qui devront éventuellement être modifiées ou supprimées.

**Préparer les données de test :**

* Rassemblez des données de test représentatives des différents types de données que le modèle regex capture habituellement.
* Assurez-vous que vos données de test couvrent à la fois les cas typiques et les cas limites afin de vérifier la robustesse de vos modifications.

**Modifier le modèle regex :**

* Apportez au modèle regex les modifications prévues.
* Cela peut inclure l'ajout de nouveaux motifs, la suppression ou l'ajustement de parties existantes, ou l'optimisation du modèle pour de meilleures performances.

**Tester les modifications :**

* Appliquez le modèle regex mis à jour à vos données de test et examinez attentivement les résultats.
* Vérifiez que le modèle capture toujours correctement les données souhaitées et qu'il n'y a pas d'effets inattendus sur d'autres parties des données ou du système.

**Déboguer et adapter :**

* Si les résultats des tests ne sont pas ceux attendus ou si des problèmes inattendus surviennent, examinez attentivement vos modifications et effectuez d'autres ajustements si nécessaire.
* Cela peut inclure l'annulation de certaines modifications ou l'ajout d'ajustements supplémentaires pour résoudre le problème.

**Documenter les modifications :**

* Mettez à jour la documentation de votre modèle regex pour refléter les modifications apportées.
* Décrivez les motifs mis à jour et les raisons des modifications effectuées afin d'aider les autres développeurs à comprendre et à utiliser le modèle.

**Enregistrer les modifications :**

* Une fois certain que les modifications sont réussies et fonctionnent comme prévu, enregistrez le modèle regex mis à jour dans votre base de code ou vos fichiers de configuration afin qu'il soit disponible pour une utilisation future.

<figure><img src="../../../../../.gitbook/assets/image (109).png" alt=""><figcaption><p>Save Changes</p></figcaption></figure>

En suivant ces étapes et en testant soigneusement les modifications des modèles regex, vous vous assurez que votre modèle regex continue de fonctionner correctement tout en répondant aux nouvelles exigences.
