# Touchless Intelligence : Trace du document

Saisissez un ID de document dans **ID du document** (Document ID), ou ouvrez un document d'exemple depuis un cluster, pour voir **ce qui est arrivé à ce document**.

<figure><img src="../.gitbook/assets/touchless-document-trace.png" alt="La page Trace du document avec le parcours du pipeline en 14 étapes et l'étape arrêtée Validation des champs"><figcaption><p>La trace du document : le parcours du pipeline avec l'étape où le document s'est arrêté, ce que cette étape avait en main, et l'historique des exécutions en dessous.</p></figcaption></figure>

En haut, vous voyez le **parcours du pipeline** avec 14 étapes : Réception, Classification, Validation du document électronique, Identification du fournisseur, Reconnaissance de texte, Extraction de l'en-tête, Extraction du tableau, Validation des champs, Recherche du BC, Rapprochement des lignes de BC, Approbation, Routage du workflow, Exportation, Accusé de réception de l'ERP. Chaque case a un état :

| État | Signification |
| --- | --- |
| **réussie** (vert) | L'étape s'est bien déroulée |
| **arrêté ici** (rouge) | L'étape a bloqué le document |
| **ignorée ou sans objet** | L'étape ne s'applique pas à ce document |
| **non atteinte** | Le document n'est jamais allé aussi loin |
| **inconnu** (en pointillés) | Rien n'a été enregistré pour cette étape |

Sous le parcours, une phrase nomme la cause. Dans la capture d'écran : *Ce document s'est arrêté à l'étape 8 « Validation des champs », car un champ obligatoire n'a pas été extrait.* Le bloc **Ce que cette étape avait en main** (What this stage had in its hands) liste les faits : **Nombre de champs invalides 5** et les champs (`delivery_date`, `email`, `invoice_sub_type`, `payment_terms`, `supplier_id`), la règle (**REQUIRED**) et les codes de validation. Le bloc **Analyse** indique si elle est **basée sur des règles** ou rédigée par l'IA.

L'**historique des exécutions** en dessous liste chaque exécution (**Exécution 1 · Première exécution**, puis chaque redémarrage) avec chaque étape et ses faits enregistrés. Si le document a été corrigé et redémarré, une note rappelle qu'il **reste compté comme traité manuellement**.

**Exemple.** Les documents d'un fournisseur s'arrêtent tous à l'étape 8. Dans la trace, vous voyez à chaque fois les mêmes cinq champs invalides. Ce n'est pas un problème d'extraction de documents isolés, mais une valeur par défaut manquante dans votre configuration de champs : corrigez-la une fois et tout le cluster est récupérable.

## Pages connexes

* [Touchless Intelligence](touchless-intelligence.md)
* [Diagnostic fournisseur et clusters de problèmes](touchless-supplier-diagnosis.md)
* [Diagnostic du rapprochement avec le BC](touchless-po-matching-diagnosis.md)
