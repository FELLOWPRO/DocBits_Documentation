# Quel chemin d'extraction a été utilisé ?

« Pourquoi ce tableau ressemble-t-il à cela ? » : on y répond en déterminant _ce que_ DocBits a fait pour ce document : règles enregistrées, tableau AI, quel niveau d'IA, et à quel endroit cela a échoué. Cette page est la liste de contrôle que le support et les partenaires utilisent avant de modifier la moindre configuration.

## 1. Regardez les onglets sur l'écran de validation

Ouvrez le document et regardez les onglets au-dessus du tableau des éléments de ligne :

| Ce que vous voyez                                                                  | Chemin                                                                                                                                                                                                                                                 |
| ---------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| Des lignes dans l'onglet **Tableau extrait**                                       | Chemin basé sur des règles. Le fournisseur dispose d'un tableau entraîné ; les lignes proviennent des règles de coordonnées enregistrées et l'IA n'est pas intervenue (sauf pour les colonnes marquées _Utiliser l'IA_).                               |
| Des lignes dans l'onglet **Tableau extrait par IA**, champ _Étiquettes_ en dessous | Chemin IA. Aucune règle enregistrée ne correspondait ; l'extraction de tableau par IA a produit les lignes, avec le niveau d'IA de l'organisation ou celui défini pour ce fournisseur sous _Plus de paramètres_ → _Modèle AI basé sur le fournisseur_. |
| Info-bulle _AI table not found_ sur l'onglet IA                                    | Le chemin IA s'est exécuté et n'a rien renvoyé pour ce document.                                                                                                                                                                                       |
| Aucun onglet de tableau                                                            | Les deux paramètres de tableau sont désactivés pour l'organisation ; rien n'a extrait le tableau.                                                                                                                                                      |
| _No line items yet_                                                                | Le chemin s'est exécuté mais n'a trouvé aucune ligne (pas de texte lisible, pas de tableau sur la page, ou les règles ne correspondaient pas à cette mise en page).                                                                                    |

Les champs d'en-tête portent leur propre badge de source à côté de la valeur : _Extracted using AI_, _Learned from validated AI extraction_, _Extracted using saved rules (FELLOW\_KV2)_, _Extracted from electronic document_, _Calculated from vendor master data_. Ces badges décrivent le champ d'en-tête, pas le tableau.

## 2. Vérifiez la configuration du fournisseur

* **Paramètres → Traitement des documents → Classification et extraction → Modèle d'IA** : le tableau sous le sélecteur liste chaque fournisseur disposant d'un modèle ou d'un entraînement enregistré. Un fournisseur de cette liste avec des _données d'entraînement_ a des règles enregistrées ; _réinitialiser les données d'entraînement_ les supprime.
* **Paramètres → Traitement des documents → Paramètres de l'OCR** : _Utiliser l'E-Text si disponible_ et _Utiliser les données IA pour les tableaux_ changent le texte que l'extraction voit. Un fournisseur peut remplacer le réglage E-Text sous _Plus de paramètres_ sur l'écran de validation.
* **Paramètres → Paramètres globaux → Types de documents → Colonnes de tableau** : indicateurs Masquée, Obligatoire et _Utiliser l'IA_. Une colonne masquée n'est jamais remplie ; une colonne _Utiliser l'IA_ est remplie par l'IA même pour les fournisseurs disposant de règles.

## 3. Reproduire sans l'interface (API / MCP)

Avec un accès API ou MCP, vous pouvez poser les mêmes questions par programmation :

| Question                                                    | Outil                                                                                                                                                                                                                 |
| ----------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Ce tableau a-t-il été produit par l'IA ?                    | `get_extracted_tables(doc_id)` : chaque tableau porte `is_ai_table: true/false`.                                                                                                                                      |
| Que donnent les règles, que donne l'IA ?                    | `get_table_extraction_report(doc_id, mode="nonai")`, puis de nouveau avec `mode="ai"` ; le rapport montre la structure configurée, les lignes extraites et l'aperçu de la page pour chaque chemin. Comparez les deux. |
| Quelles colonnes sont configurées, avec quels indicateurs ? | `get_table_config(doc_type)`                                                                                                                                                                                          |
| Le niveau d'IA a-t-il une incidence ?                       | `compare_table_extraction_models(doc_id)` exécute deux niveaux sur le même document (nécessite un document avec un numéro de fournisseur).                                                                            |
| Refaire l'extraction sur ce document                        | `extract_table_ai(doc_id)` (IA) ou `restart_document(doc_id)` (pipeline complet).                                                                                                                                     |
| Qu'a consigné le pipeline pour ce document ?                | `get_document_logs(doc_id)`                                                                                                                                                                                           |

Les outils du DocBits MCP sont décrits sous [DocBits MCP](https://docs.docbits.com/advanced-functions-and-tools/docbits-mcp) (documentation en anglais).

## 4. Lisez les journaux

**Paramètres → Paramètres de journal** (journalisation des activités) affiche les événements de tous les services. Pour une question de tableau :

* Filtrez par nom de fichier ou ID du document dans _Rechercher dans les journaux_.
* Utilisez le filtre _Service_ : l'extraction elle-même s'exécute dans le service d'extraction et les workers Celery, pas dans le service `api`. Si vous ne voyez que des lignes `api`, élargissez le filtre.
* Une exécution normale consigne, dans l'ordre : document reçu → OCR / E-Text → classification → extraction des champs → extraction du tableau (recherche des règles, puis IA si aucune règle ne correspond) → validation → changement de statut. L'étape qui manque ou qui signale une erreur est celle à examiner.

## 5. Trancher : configuration, données ou bug

| Symptôme                                                                                   | Cause la plus probable                                                                                        | Étape suivante                                                                                                          |
| ------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------- |
| Tableau correct pour le fournisseur A, erroné pour le fournisseur B, même type de document | Par fournisseur : B n'a pas de règles, ou d'anciennes règles qui ne correspondent plus à la mise en page de B | Entraînez une fois le tableau de B (ou supprimez les règles de B pour que l'IA prenne le relais).                       |
| Tableau erroné pour tous les fournisseurs depuis une certaine date                         | Un paramètre d'organisation a changé (niveau d'IA, extraction structurée, vision, colonnes de tableau)        | Comparez les paramètres avec la date du changement ; redémarrez un document pour confirmer.                             |
| Même document : chemin des règles vide, chemin IA correct                                  | Les règles ne correspondent pas à cette variante de mise en page                                              | Réentraînez avec ce document, ou supprimez les règles.                                                                  |
| Même document : les deux chemins vides                                                     | Pas de texte lisible (scan sans texte OCR, PDF image uniquement)                                              | Vue OCR sur l'écran de validation ; activez l'E-Text si le PDF a une couche de texte ; essayez une autre version d'OCR. |
| Une colonne erronée sur chaque ligne, le reste correct                                     | Mappage de colonne ou indicateur _Utiliser l'IA_                                                              | Paramètres des colonnes de tableau ; remappez dans l'entraînement de tableau.                                           |
| Lignes manquantes aux sauts de page ou après un sous-total                                 | Mise en page que l'IA ou les règles n'ont pas suivie                                                          | Entraînez le tableau avec un document multipage ; ajoutez une étiquette telle que _« le tableau continue en page 2 »_.  |
| Étape d'extraction absente des journaux, document bloqué en _running_                      | Infrastructure (file d'attente des workers), pas la configuration                                             | Vérifiez les tâches en attente (`get_pending_tasks_detail` via MCP) et contactez le support avec l'ID du document.      |

## Que transmettre au support

* L'ID du document et l'organisation
* L'onglet qui contient les lignes (Tableau extrait / Tableau extrait par IA / aucun) et le niveau d'IA utilisé
* Si le fournisseur dispose de règles enregistrées et la date de leur dernier enregistrement
* Un exemple de document où cela fonctionne et un où cela ne fonctionne pas, si vous avez les deux

## Pages associées

* [Dépannage de l'extraction de table](table-extraction-troubleshoot.md) : qualité d'extraction, OCR, E-Text, messages sur le tableau
* [Training Line Fields / Table Training](../../../administration-and-setup/setup/document-training/training-line-fields-table-training/)
* [Tableau AI](../../../end-user-and-partner-section/end-user-section/ai-table/)
* [Paramètres de journal](../../../administration-and-setup/settings/log-settings/)
