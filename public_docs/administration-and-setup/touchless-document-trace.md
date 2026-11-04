# Touchless Intelligence : Trace du document

Saisissez un ID de document dans **ID du document** (Document ID), ou ouvrez un document d'exemple depuis un cluster, pour voir **ce qui est arrivé à ce document**.

L'en-tête affiche le fichier, son statut (par exemple **En cours**), l'exécution que vous consultez et son premier bloqueur, ainsi qu'un bouton **Document** avec l'ID du document.

<figure><img src="../.gitbook/assets/touchless-nova-trace-overview-fr.png" alt="Dev NOVA : parcours et valeurs enregistrées lors de la première exécution de test"><figcaption><p>Nouvelle capture sur Dev NOVA 11.0.3, le 4 novembre 2026. La facture fictive s’arrête à la validation des champs. Classification, recherche du fournisseur et extraction de l’en-tête et du tableau contiennent des valeurs réellement enregistrées. Les cartes montrent le document et son historique. Il s’agit de l’interface du produit en fonctionnement. Dans cette version, les noms d’étape du parcours restent en anglais ; Validation sur le terrain désigne ici la validation des champs et Historique des courses désigne les exécutions, sans rapport avec des courses.</p></figcaption></figure>

Le **Chemin du pipeline** affiche 14 étapes : Réception, Classification, Validation du document électronique, Identification du fournisseur, Reconnaissance de texte, Extraction de l'en-tête, Extraction du tableau, Validation des champs, Recherche du BC, Rapprochement des lignes de BC, Approbation, Routage du workflow, Exportation, Accusé de réception de l'ERP. Chaque étape porte un seul état :

| État | Signification |
| --- | --- |
| **Passé** (vert) | L'étape s'est bien déroulée |
| **Arrêté ici** (orange) | L'étape a bloqué le document |
| **Non atteint** | Étape située après le premier blocage dans le parcours ; vérifier les éventuelles exécutions supplémentaires dans le journal |
| **Aucun enregistrement** (en pointillés) | Aucune donnée n'a été enregistrée pour cette étape |
| **Sans objet** | L'étape ne s'applique pas à ce document |

### Journal des étapes

Le **journal des étapes** sous le chemin liste les mêmes étapes avec ce que chacune a enregistré. Un point de statut et le mot de statut se trouvent à gauche et à droite de chaque ligne.

* Chaque valeur est une **puce de valeur** : un nombre avec son unité, par exemple **Confiance 100 %**, **Seuil 60 %**, **Règles en échec 0**, **8 champs manquants** ou **0 écart de correspondance**. Les pourcentages sont affichés en `97 %`, jamais en `0.97`.
* **Détails** ouvre la liste complète des valeurs enregistrées par une étape, y compris les alternatives qu'elle a envisagées.
* L'étape qui a bloqué le document en indique la raison, par exemple **Échec de la validation des champs**.
* Une valeur qu'aucune étape n'a enregistrée s'affiche comme **Non enregistré**, jamais comme une valeur inventée. Les valeurs sont des nombres et des termes fixes, jamais du texte du document.
* **Afficher les diagnostics bruts** active les données brutes lorsque le support les demande.

<figure><img src="../.gitbook/assets/touchless-nova-trace-stage-log-fr.png" alt="Dev NOVA : journal avec confiance, valeurs d’extraction et validation bloquée"><figcaption><p>Première exécution réelle : confiance de classification de 100 %, 0 fournisseur candidat, 1 ligne et 7 écarts de correspondance. Une étape réussie confirme son exécution, pas l’identification du fournisseur ni l’exactitude de toutes les valeurs. La validation signale un champ obligatoire manquant.</p></figcaption></figure>

### Exécutions et changements

Le sélecteur permet de choisir une tentative ; l’historique indique son résultat et son premier blocage. Les différences enregistrées comparent l’exécution sélectionnée à la précédente, pas automatiquement à l’exécution actuelle. Chaque différence porte son unité ; des valeurs identiques restent inchangées.

La carte Document présente le type, le fournisseur, le numéro de facture, la commande, les pages et la méthode d’analyse enregistrée. Ici, Manuel correspond au type fourni lors de l’import de test. Les 100 % ne prouvent donc pas indépendamment la précision d’une classification automatique.

### Lire les détails du fournisseur et du tableau

<figure><img src="../.gitbook/assets/touchless-nova-trace-supplier-fr.png" alt="Dev NOVA : identifiants détectés, recherche dans les données de référence et attribution du fournisseur"><figcaption><p>Le nom figure sur la facture et fait l’objet d’une recherche dans les données de référence, sans fournisseur attribué. Cette facture ne contient ni numéro de TVA, ni IBAN, ni adresse e-mail, ni GLN. L’absence de correspondance dans les données de référence diffère d’une valeur non trouvée sur la facture. Pour les identifiants non recherchés, le libellé Aucune correspondance trouvée ne prouve pas une recherche : aucune tentative de rapprochement n’a eu lieu.</p></figcaption></figure>

Vérifiez séparément si l’identifiant figure sur le document, s’il a été recherché et si un fournisseur a été attribué. Une étape verte ne répond pas à elle seule à ces trois questions.

<figure><img src="../.gitbook/assets/touchless-nova-trace-table-fr.png" alt="Dev NOVA : détails de la première exécution avec sept écarts de correspondance"><figcaption><p>Les détails signalent 7 écarts de correspondance pour 1 tableau et 1 ligne. Vérifiez le mappage des colonnes avant de conclure à un échec d’extraction. Le pied de comparaison ne constitue pas une référence valide pour la première exécution sélectionnée, qui n’a pas de prédécesseur.</p></figcaption></figure>

### Reconnaître une véritable relance

<figure><img src="../.gitbook/assets/touchless-nova-trace-runs-fr.png" alt="Dev NOVA : comparaison de deux exécutions réelles dont les valeurs enregistrées sont identiques"><figcaption><p>La même facture après une véritable relance manuelle, sans correction des champs. Une nouvelle exécution prouve une nouvelle tentative, pas une amélioration. Les valeurs identiques restent sans changement ; aucune différence n’a été inventée.</p></figcaption></figure>

Une relance manuelle constitue une intervention humaine. Ce cas ne sera classé AP Assisted qu’après une éventuelle réussite ultérieure. Tant qu’il est en cours, il est exclu du dénominateur des documents finalisés.

Limites des preuves. Ce cas ne démontre ni approbation métier, ni export réussi, ni confirmation ERP. L’ancien moteur de rapprochement ne fournit ici aucun parcours de décision enregistré ; ce n’est pas la preuve d’une comparaison avec Infor. Dans NOVA 11.0.3, le journal peut signaler une recherche de commande réussie après une validation bloquée alors que le parcours la présente comme étape suivante. Vérifiez les deux vues. Le résumé indique aussi que le numéro de facture n’est pas enregistré, bien qu’il figure dans l’extraction ; comparez l’original et les champs extraits.

## Distinguer extraction et données source

1. Comparez original et champs ou lignes extraits **avant correction manuelle**. Une valeur corrigée aujourd’hui ne prouve pas l’extraction initiale.
2. Lisez le premier blocage. Une étape réussie confirme son exécution, pas l’exactitude de chaque valeur.
3. Comparez commande importée et Infor actuel : unités, unités de prix et date d’import.
4. Distinguez original contre extraction, extraction correcte contre données importées, et Infor contre sa copie. Laissez la cause ouverte si les preuves manquent.
5. Vérifiez interventions, approbations, relances et résultat final.

**Exemple :** original et extraction indiquent 10,00 €, commande importée 9,00 €. C’est un écart avec la commande, pas une erreur d’extraction démontrée. Confirmez le prix convenu et corrigez la source ou l’import. Une relance manuelle suivie de réussite donne AP Assisted. Voir [les exemples et le calcul](touchless-intelligence.md).

Des champs manquants répétés prouvent un blocage récurrent, pas nécessairement une valeur par défaut absente. Examinez extraction, original, validation et configuration.

## Prouver l’extraction initiale et suivre les blocages successifs

1. Ouvrez le document depuis sa trace ; vérifiez son ID et l’exécution. Comparez numéro de commande, devise, quantités, unités, unités de prix, prix, montants des lignes et totaux pertinents.
2. Distinguez valeurs actuelles et valeurs avant correction. Utilisez une preuve historique de cette exécution. Changer d’exécution ne garantit pas la restitution de chaque ancienne cellule.
3. Si la valeur initiale manque, indiquez **non évaluable**, pas correcte. Définissez champs, lignes, sélection et taille de l’échantillon avant de communiquer sa qualité d’extraction.
4. Comparez copie importée, date d’import et Infor actuel pour distinguer source erronée et copie périmée.

Une exécution peut attendre une commande ; après l’import, une autre peut révéler un écart de prix. La première ne prouve pas qu’elle ait atteint ce contrôle ultérieur. Une relance humaine persiste après réussite comme AP Assisted ; un refus ERP définitif devient une exception prioritaire. **Non enregistré** signifie preuve manquante.

Les outils et la classification des actions humaines sont expliqués dans [Touchless avec MCP](touchless-mcp.md).

## Pages connexes

* [Touchless Intelligence](touchless-intelligence.md)
* [Diagnostic fournisseur et clusters de problèmes](touchless-supplier-diagnosis.md)
* [Diagnostic du rapprochement avec le BC](touchless-po-matching-diagnosis.md)

Les captures d'écran de cette page montrent l'interface en français.

<!-- Touchless documentation alignment 2026-11-04: extraction quality is distinct from process automation. KPI definition checked against DocBits_API c51f350c728acb8ac964098d15f7b006bce273f4; existing native screenshots and video sources preserved except unsafe historical list images. -->

<!-- Completion 2026-11-04: localized MCP examples, AP actions, original-value evidence and owned synthetic PO cards. -->

Les cinq nouvelles captures montrent l’interface localisée de Dev NOVA 11.0.3 et la même facture créée pour la documentation. Toute illustration distincte de l’original et de ses champs reste limitée à cette comparaison.
