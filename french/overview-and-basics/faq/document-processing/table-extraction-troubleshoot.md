# Dépannage de l'extraction de table

## **Étape 1 : Ouvrir la vue OCR pour les mauvais résultats d'extraction**

Si les résultats de l'entraînement d'extraction de table ne sont pas bons :

1. Ouvrez la **vue OCR** en cliquant sur l'icône de la loupe avec **OCR** écrit dessus.
2. Passez en revue les résultats de l'extraction et voyez si le processus OCR peut améliorer la capture des données.
3. Si les résultats semblent toujours mauvais, essayez un autre document pour vérifier si le problème est spécifique au document.
4. Si le problème est spécifique au document, utilisez un autre document pour l'extraction.
   * Si le problème persiste, suivez les étapes suivantes.

## **Étape 2 : Vérifier la disponibilité de l'E-Text**

1. Vérifiez si le document contient de l'**e-text** disponible.
   * Vous pouvez vérifier cela en utilisant un outil comme **Adobe Acrobat**.
   * Si le document contient de l'e-text, suivez **l'Étape 3**.
   * Si le document ne contient pas d'e-text, suivez **l'Étape 4**.

## **Étape 3 : Activer l'extraction de l'E-Text**

Si le document contient de l'e-text, vous avez deux options :

1. **Activer l'extraction de l'e-text pour ce fournisseur uniquement** :
   * Revenez à la **Validation des champs des documents**.
   * Cliquez sur le carré avec les trois points dans la barre d'outils de gauche.
   * Ici, activez l'option **Utiliser l'e-text si disponible** pour l'activer uniquement pour ce fournisseur.
2. **Activer l'extraction de l'e-text pour tous les fournisseurs** :
   * Allez dans **Paramètres** > **Traitement de document** > **Paramètres OCR**.
   * Dans cette section, vous trouverez l'option **Utiliser l'e-text si disponible** et pouvez l'activer pour tous les fournisseurs.
3. Après avoir activé l'extraction de l'e-text, réessayez l'**entraînement d'extraction de table**.
   * Si les résultats s'améliorent, le problème est résolu.
   * Si les résultats ne sont toujours pas bons, passez à **l'Étape 4**.

## **Étape 4 : Pas d'E-Text disponible - Changer la version de l'OCR AI**

Si le document ne contient pas d'e-text disponible :

1. Allez dans **Paramètres** > **Traitement de document** > **Paramètres OCR**.
2. Changez la **Version de l'OCR AI** pour une version différente.
3. Retournez à l'**Entraînement d'extraction de table** et réessayez.
4. Si le résultat est meilleur :
   * Vérifiez d'autres documents provenant de différents fournisseurs pour vous assurer que les résultats d'extraction pour ces fournisseurs ne sont pas impactés par ce changement.
   * **Soyez prudent, car ce changement peut affecter les résultats d'extraction d'autres fournisseurs.**
   * Ce changement peut avoir un impact sur d'autres fournisseurs, alors assurez-vous de vérifier les résultats minutieusement pour vous assurer qu'il n'affecte pas négativement les extractions de documents d'autres fournisseurs.
5. Si le résultat n'a pas été amélioré après avoir changé la version de l'OCR AI, veuillez **nous contacter** pour obtenir une assistance supplémentaire.

## Messages sur le tableau

L'extraction peut sembler correcte alors que le document refuse toujours d'être approuvé. Voici les messages que DocBits affiche sur ou sous le tableau des éléments de ligne, ce qui les déclenche et comment les faire disparaître.

| Message | Cause | Solution |
|---|---|---|
| **Colonne obligatoire vide** (cellule marquée en rouge, nom de la colonne dans l'info-bulle) | Une colonne marquée *Obligatoire* dans les paramètres des colonnes de tableau n'a pas de valeur dans cette ligne. | Remplissez la cellule. Si la valeur n'existe jamais pour ce type de document, un administrateur décoche *Obligatoire* sous Paramètres → Types de documents → Colonnes de tableau et vous redémarrez le document. |
| **Line total does not match quantity x unit price (expected …, got …)** | DocBits contrôle chaque ligne : `TOTAL_AMOUNT = QUANTITY × UNIT_PRICE + CHARGES`, moins `DISCOUNT`, ou × (100 − `DISCOUNT_PERCENT`) / 100, ou moins `DISCOUNT_PER_UNIT × QUANTITY`, selon la colonne de remise renseignée. Un écart supérieur à 0,02 déclenche le message. Le contrôle ne s'exécute que lorsque la quantité, le prix unitaire et le total sont tous renseignés. | Comparez les quatre valeurs avec le document. En général, l'une d'elles a été lue dans la mauvaise colonne ; une valeur de frais ou de remise dans la mauvaise cellule est le cas le plus fréquent. Corrigez la cellule ; le message disparaît à l'enregistrement. |
| **Line total does not match quantity x unit price minus discount / minus percentage discount / minus per-unit discount** | Même contrôle, avec la colonne de remise renseignée. | Comme ci-dessus ; vérifiez d'abord la cellule de remise. |
| **Line items add up to … but the net total is …** (avertissement) | La somme de toutes les cellules `TOTAL_AMOUNT` diffère du montant net de l'en-tête. | Recherchez une ligne manquante, une ligne en double ou un montant net d'en-tête mal lu. Un avertissement ne bloque pas l'approbation. |
| **Total does not add up: expected …, got …** (en-tête) | Net + taxe (+ frais de port dans les mises en page américaines) diffère du total de l'en-tête. | Contrôle d'en-tête, pas un problème de tableau : corrigez les montants de l'en-tête. |
| **Line Item Table is missing Mandatory column for PO like (Item Number, Unit Price, Quantity and Total amount)** | La correspondance de bon de commande nécessite ces quatre colonnes par défaut et l'une d'elles est masquée ou remplacée par une colonne personnalisée. | Administrateur : réaffichez la colonne par défaut sous Colonnes de tableau, ou mappez la valeur sur celle-ci dans l'entraînement de tableau. |
| **Table is already extracted by AI. Do you want to train manually?** | Vous avez ouvert l'entraînement de tableau pour un fournisseur dont le tableau provient de l'IA. | Confirmez pour entraîner ; les règles enregistrées remplacent alors le tableau AI pour ce fournisseur. Annulez pour conserver le tableau AI. |
| **AI Table will display here. Enable in …** | L'extraction de tableau par IA est désactivée pour l'organisation. | Administrateur : Paramètres → Traitement des documents → Classification et extraction → *Extraction de tableaux par IA*. |
| **No line items yet** | Rien n'a été extrait : aucune règle pour ce fournisseur et l'IA n'a trouvé aucun tableau, ou le document ne contient pas de texte lisible. | Suivez les Étapes 1 à 4 ci-dessus (vue OCR, E-Text). Entraînez ensuite le tableau une fois, ou ajoutez les lignes manuellement avec *Ajouter une nouvelle ligne de tableau*. |

### L'IA remplit systématiquement une colonne avec la mauvaise valeur

Exemple rencontré en pratique : l'IA écrit le total de ligne dans `CHARGES`. Chaque ligne échoue alors au contrôle du total de ligne, car les frais s'ajoutent à quantité × prix unitaire.

1. Si le fournisseur dispose de règles enregistrées, décochez *Utiliser l'IA* sur cette colonne (Paramètres → Types de documents → Colonnes de tableau) pour que les règles la remplissent.
2. Si le fournisseur n'a pas de règles, entraînez le tableau une fois afin que la colonne soit liée à sa position sur la page, ou masquez la colonne si le fournisseur n'imprime jamais cette valeur.
3. Ajoutez une [étiquette de tableau AI](../../../end-user-and-partner-section/end-user-section/ai-table/ai-table-tags.md) telle que *« la colonne des frais est vide chez ce fournisseur »* ; les étiquettes sont enregistrées par fournisseur.

### Désactiver les contrôles de tableau

Paramètres → Types de documents → *votre type* → Plus de paramètres → **Ignorer la validation du tableau** marque le tableau de chaque document de ce type comme valide : les écarts de total de ligne et les colonnes obligatoires vides ne sont plus signalés. Les contrôles d'en-tête (total = net + taxe) restent actifs. N'utilisez cette option que pour les types de document dont les tableaux sont informatifs et ne sont pas exportés vers l'ERP.
