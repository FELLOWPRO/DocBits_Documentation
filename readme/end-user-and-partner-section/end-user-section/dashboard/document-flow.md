# Flux De Documents

**Flux de documents** affiche les étapes de traitement d'un document. Utilisez-le pour voir quelles étapes sont terminées, laquelle est en attente et combien de temps le traitement a pris. L'exemple ci-dessous utilise une facture synthétique dans le Sandbox en français.

## Ouvrir depuis le tableau de bord

Sur le [tableau de bord](../dashboard/), trouvez le document. Dans sa colonne **Actions**, sélectionnez les trois points, puis **flux de documents**. Cette option ouvre le flux du document ; elle ne modifie pas le document.

<figure><img src="../../../.gitbook/assets/document-flow-dashboard-menu-fr-20261008.png" alt="Tableau de bord en français avec le menu Actions ouvert pour une facture synthétique ; flux de documents figure sous Attribuer à."><figcaption>Choisissez flux de documents dans le menu Actions du document.</figcaption></figure>

## Ouvrir depuis la Validation Des Champs

Ouvrez le document. Dans **[Validation Des Champs](../validation-screen/)**, sélectionnez les trois points dans la barre d'actions de droite, puis **Flux de documents** sous **Plus d'options**.

<figure><img src="../../../.gitbook/assets/document-flow-validation-menu-fr-20261008.png" alt="Écran Validation Des Champs en français montrant le menu Plus d'options et son entrée Flux de documents à côté d'une facture synthétique."><figcaption>Le même flux est disponible depuis la vue du document.</figcaption></figure>

## Lire le flux

**Process Statistics** à gauche résume le nombre d'étapes, les étapes terminées et en attente, les redémarrages, la durée totale, l'état actuel et la progression globale. Chaque carte numérotée montre une étape de traitement et son état actuel. Faites défiler vers le bas pour voir les étapes suivantes.

<figure><img src="../../../.gitbook/assets/document-flow-overview-fr-20261008.png" alt="Flux de documents en français avec Process Statistics à gauche et les premières cartes d'étapes numérotées : IMPORTÉ, OCR_COMPLETED et CLASSÉ."><figcaption>Les premières étapes du flux d'une facture synthétique.</figcaption></figure>

<figure><img src="../../../.gitbook/assets/document-flow-later-steps-fr-20261008.png" alt="Flux de documents en français après le défilement ; les cartes suivantes incluent FIELDS_EXTRACTED, TABLES_EXTRACTED, TRANSFORMED, METADATA_POPULATED, LOOKUP_COMPLETED et waiting_for_valid."><figcaption>Faites défiler pour suivre la séquence jusqu'aux étapes suivantes.</figcaption></figure>

Sélectionnez une carte d'étape pour ouvrir **Step Details** à gauche. Elle affiche le module et son statut. Un panneau **Task Logs** peut également s'ouvrir à droite ; les détails des journaux dépendent de ce qui est disponible pour cette tâche. Sélectionnez **×** dans Step Details pour fermer le panneau.

<figure><img src="../../../.gitbook/assets/document-flow-step-details-fr-20261008.png" alt="Flux de documents en français avec la carte OCR_COMPLETED sélectionnée ; Step Details sous Process Statistics montre le module OCR_COMPLETED et le statut Completed."><figcaption>Step Details explique le statut du module sélectionné.</figcaption></figure>
