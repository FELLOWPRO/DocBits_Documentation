# Classification et extraction

<figure><img src="../../../../.gitbook/assets/classification-general-fr-20261104.png" alt="Onglet Général avec les paramètres de traitement. Le motif de code-barres propre à l&#x27;organisation est masqué ; aucun paramètre n&#x27;a été modifié."><figcaption><p>Onglet Général avec les paramètres de traitement. Le motif de code-barres propre à l&#x27;organisation est masqué ; aucun paramètre n&#x27;a été modifié.</p></figcaption></figure>

[AI Table](../../../../end-user-and-partner-section/end-user-section/ai-table/README.md) · [Structured Output pour les tableaux](../../../../end-user-and-partner-section/end-user-section/ai-table/structured-output.md)

## Quel paramètre fonctionne à quelle étape du processus ?

<figure><img src="../../../../.gitbook/assets/process-extraction-fr-20261028.png" alt="Du fichier aux données reconnues: Affichez séparément le type de document, la source de données et le chemin d&#x27;extraction."><figcaption><p>Affichez séparément le type de document, la source de données et le chemin d&#x27;extraction. Le diagramme est schématique ; les paramètres actifs de votre organisation déterminent le comportement réel.</p></figcaption></figure>

La classification répond à la question **« De quel type de document s'agit-il ?**. L'extraction répond **« Quelles valeurs contient-il ?**. Les paramètres de cette page affectent différents points de traitement et ne doivent pas être compris comme un seul commutateur AI.

1. **Préparer la saisie :** Pour PDFs, le texte existant ou OCR peut être utilisé ; les documents électroniques pris en charge peuvent fournir des valeurs structurées. Une division activée peut séparer un document entrant en fonction du code-barres ou des critères QR configurés.
2. **Déterminer le type de document :** Les règles et modèles de classification attribuent aux documents un type et, si nécessaire, un sous-type. Cette affectation doit être distinguée de l'extraction ultérieure de champs et de tables.
3. **Extraire les valeurs :** Les tables peuvent suivre différents chemins en fonction de la configuration et des règles enregistrées applicables. Les champs d'en-tête ont leurs propres indicateurs de source. Le modèle d’IA sélectionné n’explique donc pas à lui seul chaque valeur de ligne ou de champ.
4. **Tracez le résultat :** Dans l'écran de validation, vérifiez quel onglet du tableau contient les lignes et quel indicateur de source possède un champ d'en-tête. Si une étape de traitement est manquante, lisez les journaux de documents avant de modifier les paramètres.

### Distinguer le chemin des règles et le chemin de l'IA

Des règles de table enregistrées appropriées peuvent déterminer l'extraction de table pour le modèle ou le fournisseur concerné. Sans règles adaptées, le chemin AI peut être utilisé lorsque l’extraction de table AI est activée. Les colonnes individuelles peuvent avoir leurs propres options d'IA. Une source AI pour un champ d’en-tête ne signifie pas que la table entière provient de l’AI.

Le guide de diagnostic [Quel chemin d’extraction a été utilisé ?](../../../../overview-and-basics/faq/document-processing/which-extraction-path-was-used.md) explique les onglets, les identifiants de source et les journaux. La page [Modèle d'IA](ai-model.md) explique la norme de l'organisation et les remplacements liés aux modèles.

## Vue d'ensemble

Dans les paramètres **Classification et extraction**, vous pouvez :

* Activer la **division des documents** sur la base des codes QR
* Configurer le **formatage des montants**
* Configurer l'**extraction de tableaux**
* Activer ou désactiver le traitement des fichiers **ZUGFeRD** non pris en charge
* Définir des règles de classification spécifiques
* Suivre les **modèles d'IA** entraînés sur mesure utilisés dans le processus de classification

Cette page décrit en détail tous les paramètres disponibles.

## **Accéder aux paramètres de classification et d'extraction**

Pour accéder aux paramètres **Classification et extraction**, allez dans :\
**Paramètres → Traitement des documents → Classification et extraction**


## Division des documents

Dans la section **Division des documents**, vous pouvez configurer si un document téléversé doit être divisé en plusieurs documents dès qu'un **code-barres** apparaît sur l'une de ses pages.

Pour activer cette fonctionnalité :

1. Allez dans la section **Division des documents**.
2.  Ouvrez le menu déroulant.

    
3.  Sélectionnez **Diviser par code-barres/code QR**.

    

Vous aurez ensuite la possibilité de :

* Sélectionner un ou plusieurs types de codes-barres à détecter.
*   Indiquer un motif regex auquel le code-barres doit correspondre pour déclencher la division du document.

    

Après une division réussie, le document parent est supprimé et les pages se poursuivent sous forme de documents distincts qui partagent le même lot.

<figure><img src="../../../../.gitbook/assets/anatomy-barcode-split.svg" alt="Illustration isométrique de huit feuilles dans un bac, avec un scanner qui lit un code-barres sur la feuille 6. Des intercalaires se dressent devant les feuilles 3 et 6 et répartissent les feuilles en trois documents ; un élastique entoure l'ensemble du bac."><figcaption><p>Exemple avec le motif <code>^INV\d{6}$</code> : les codes des feuilles 3 et 6 correspondent et chacun démarre un nouveau document, le code de la feuille 4 ne correspond pas et ne divise rien, et l'élastique représente le lot que partagent les documents obtenus.</p></figcaption></figure>

## Formatage des montants

Dans la section **Formatage des montants**, vous disposez de deux options :

* **Autoriser l'arrondi lors de la comparaison des montants :**\
  Si cette option est activée, une tolérance de ±0,5 est admise lors de la comparaison des montants.\
  Si elle est désactivée, une tolérance par défaut de ±0,05 s'applique.
* **Exiger une correspondance exacte pour la comparaison des montants :**\
  Si cette option est activée, les montants doivent correspondre exactement, sans aucune tolérance.\
  Si elle est désactivée, une tolérance de ±0,05 est admise.

<mark style="color:red;">**Remarque**</mark> : une seule de ces deux options peut être active à la fois.

## Extraction de tableaux

{% hint style="info" %}
**Prérequis pour une extraction de tableaux fonctionnelle**

* Le type de document dispose de **colonnes de tableau** (Paramètres → Paramètres globaux → Types de documents → [Colonnes de tableau](../../global-settings/document-types/table-columns/README.md)). Sans colonnes, il n'y a rien dans quoi extraire.
* **Extraction de tableaux** ou **Extraction de tableaux par IA** est activée ci-dessous, pour toute l'organisation.
* Le document contient du texte lisible : l'OCR a été exécuté, ou l'E-Text est utilisé pour les PDF nativement numériques ([Paramètres de l'OCR](../ocr-settings.md)).
* L'entraînement et les modèles d'IA sont définis **par fournisseur**. Un tableau entraîné ne s'applique qu'aux documents du fournisseur sur lequel il a été entraîné.
{% endhint %}

Vous pouvez extraire les tableaux des documents en activant soit **Extraction de tableaux**, soit **Extraction de tableaux par IA**. Un tableau entraîné (qu'il soit basé sur l'IA ou manuel) est toujours lié à un fournisseur précis.

**Extraction de tableaux :** active l'extraction de tableaux basée sur des règles. Les tableaux sont entraînés par fournisseur sur l'écran de validation (*Aller à la vue d'extraction de tableau*).\
En savoir plus sur l'entraînement [ici](../../../setup/document-training/training-line-fields-table-training/defining-tables-and-columns.md).

**Extraction de tableaux par IA :** utilise l'IA pour extraire le tableau de n'importe quel fournisseur sans entraînement. Si les résultats pour un fournisseur ne sont pas assez précis, entraînez le tableau de ce fournisseur ; les règles enregistrées prennent alors le pas sur l'IA pour ce fournisseur.

**Utiliser l'extraction de tableaux Vision (IA) :** l'IA lit l'image de la page au lieu de la couche de texte. Utile pour les documents numérisés et les tableaux sans structure de texte claire ; plus lent. Le menu déroulant à côté de l'interrupteur détermine l'intensité avec laquelle l'image de la page est utilisée :

* **Désactivé (texte uniquement)** – Seule la couche de texte est utilisée. C'est le réglage par défaut.
* **Images uniquement** – Seule l'image de la page est lue.
* **Hybride (texte et images)** – La couche de texte et l'image de la page sont combinées dans la même requête.
* **Auto (décidé par document)** – DocBits décide par document si la couche de texte suffit.

Le mode est stocké sous la clé de préférence `TABLE_EXTRACTION_VISION_MODE` ; l'ancien interrupteur `TABLE_EXTRACTION_USE_VISION` subsiste et équivaut en pratique à *Images uniquement*.

**Utiliser l'extraction structurée (IA):** Le commutateur définit la valeur d'organisation de la sortie structurée. Les colonnes demandées dépendent de Par défaut/Oui/Non dans Use AI, des dérogations et de l'apprentissage fournisseur. Le guide complet explique configuration, aperçu et exemple. [Structured Output pour les tableaux](../../../../end-user-and-partner-section/end-user-section/ai-table/structured-output.md).

**Extraction de tableaux pour le calcul des coûts :** lorsque cette option est activée, DocBits peut extraire les éléments de coût des tableaux au niveau des lignes et les classer en conséquence.\
Explication détaillée [ici](table-extraction-for-costing-element.md).

**Extraction automatique du code fiscal :** lorsque cette option est activée, le système remplit automatiquement le champ **Code fiscal** sur l'écran de validation, à condition qu'un champ de code fiscal soit configuré.\
Plus d'informations sur ce paramètre [ici](auto-extract-tax-code.md).

**Enregistrer les règles d'extraction (administrateurs uniquement) :** seuls les administrateurs peuvent cliquer sur *Enregistrer les règles* dans l'entraînement de tableau. Activez cette option lorsque des utilisateurs enregistrent régulièrement des règles qui cassent l'extraction d'un fournisseur.

**Modèle AI :** définit le modèle d'organisation pour l'extraction de champs et de tables. Le menu propose Full, Fast, Nexus, Nexus Flash, Auto et Auto Nexus. Vérifiez la disponibilité, la qualité, la durée d’exécution et le coût avec des documents représentatifs. Un niveau n’est pas toujours le plus précis ou le plus rapide pour chaque document. Les remplacements de modèles peuvent remplacer le paramètre d'organisation. Le tableau sous le sélecteur montre :

* Quels **fournisseurs** utilisent quel modèle d'IA
* S'ils utilisent l'extraction structurée (IA) et l'E-Text
* Des options pour supprimer une entrée et ainsi réinitialiser le fournisseur au réglage par défaut

Ce paramètre est expliqué en détail [ici](ai-model.md).

### Pourquoi le tableau est-il différent d'un fournisseur à l'autre ?

Le traitement des tables dépend des règles et paramètres enregistrés dans le contexte du fournisseur ou du modèle concerné :

* **Règles enregistrées** (entraînement de tableau) : position du tableau et mappage de ses colonnes sur la mise en page de ce fournisseur.
* **Étiquettes de tableau AI et règles de formatage** : indications que l'utilisateur a enregistrées pour le tableau AI de ce fournisseur.
* **Modèle d'IA spécifique au modèle :** La sélection effectuée sur l'écran de validation est enregistrée par organisation et par modèle d'extraction actuel. Cela ne modifie pas automatiquement tous les modèles du même fournisseur. Sans remplacement, le paramètre d’organisation applicable est utilisé.

Ainsi, le fournisseur A, qui dispose de règles enregistrées, affiche un tableau déterministe dans l'onglet *Tableau extrait* de l'écran de validation, tandis que le fournisseur B, sans règles, obtient le *Tableau extrait par IA*. Pour que le fournisseur B se comporte comme A, entraînez une fois le tableau de B. Pour réinitialiser un fournisseur, supprimez ses règles sur l'écran de validation ou réinitialisez ses données d'entraînement dans le tableau Modèle d'IA.

### Clés de préférence

Chaque option de cette section est stockée sous forme de préférence d'organisation. Utilisez la clé lorsque vous définissez la valeur via l'API (`/preferences/set_preference`), un script ou le DocBits MCP (`get_preference` / `set_preference`).

| Paramètre (libellé dans l'interface) | Clé de préférence | Valeurs |
|---|---|---|
| Extraction de tableaux | `TABLE_EXTRACTION_SETTING` | `true` / `false` |
| Extraction de tableaux par IA | `USE_AI_TABLE_EXTRACTION` | `true` / `false` |
| Utiliser l'extraction de tableaux Vision (IA) | `TABLE_EXTRACTION_VISION_MODE` | `off` (par défaut), `vision`, `hybrid`, `auto` |
| Utiliser l'extraction de tableaux Vision (IA) – ancien interrupteur | `TABLE_EXTRACTION_USE_VISION` | `true` / `false` ; équivaut en pratique à `vision` |
| Utiliser l'extraction structurée (IA) | `USE_STRUCTURED_EXTRACTION` | `true` / `false` |
| Extraction de tableaux pour le calcul des coûts | `CHARGES_TABLE_EXTRACTION` | `true` / `false` |
| Extraction automatique du code fiscal | `AUTO_EXTRACT_TAX_CODE` | `true` / `false` |
| Enregistrer les règles d'extraction (administrateurs uniquement) | `ONLY_ADMIN_CAN_SAVE_RULES` | `true` / `false` |
| Modèle d'IA | `AI_MODEL` | `gpt-6-sol` (Full), `gpt-6-luna` (Fast), `qwen3.8-max` (Nexus), `glm-5.3-flash` (Nexus Flash), `auto` (Auto), `auto-nexus` (Auto Nexus) |
| Version de l'extraction de tableaux (boîte de dialogue de confirmation) | `TBL_EXT_VERSION` | chaîne de version |
| Paramètres de l'OCR → Utiliser les données IA pour les tableaux si disponibles | `USE_AI_DATA_FOR_TABLE` | `true` / `false` |
| Paramètres de l'OCR → Utiliser l'E-Text si disponible | `USE_ETEXT_IF_AVAILABLE` | `true` / `false` |

Remarques :

* Les préférences booléennes sont stockées sous forme de chaînes `true` / `false` ; une clé jamais définie compte comme `false`. Si vous envoyez `1` ou `0`, DocBits stocke `true` / `false`.
* `AI_MODEL` non défini équivaut à **Fast**.
* Un `TABLE_EXTRACTION_VISION_MODE` non défini est déduit de l'ancien interrupteur `TABLE_EXTRACTION_USE_VISION` : `true` donne `vision`, toute autre valeur donne `off`.
* La modification d'une clé prend effet pour les documents traités ensuite. Redémarrez un document pour le réextraire avec le nouveau paramètre.
* Les remplacements de modèles diffèrent des préférences de l'organisation. Le guide AI Model explique la portée exacte.

## Document électronique

**Traiter les PDF ZUGFeRD non pris en charge :** si cette option est activée, les versions **ZUGFeRD** non prises en charge sont traitées comme des PDF standard et le XML intégré est ignoré.

La liste des versions **ZUGFeRD** prises en charge est disponible [ici](../../global-settings/document-types/edi/zugferd/README.md).

## **Règles de classification**

Dans la section **Règles de classification**, vous pouvez définir des motifs **regex** et des critères spécifiques pour aider le système à classer automatiquement les documents lors du traitement.

Pour accéder à cette section, cliquez sur l'onglet **Règles de classification** en haut de la page.


### **Ajouter une nouvelle règle de classification**

Pour créer une nouvelle règle :

1.  Cliquez sur **Ajouter** dans le coin supérieur droit.

    
2. Renseignez les champs suivants :
   * **Motif** : le motif regex que le système doit rechercher pour déclencher la classification.
   * **Type** : l'endroit où le motif doit être recherché (par exemple **Code-barres**).
   * **Sous-organisation** _(facultatif)_ : indique à quelle sous-organisation la règle s'applique.
   * **Type de document** : le type de document à attribuer lorsque le motif correspond.
   *   **Sous-type de document** _(facultatif)_ : indique un sous-type pour une classification plus fine.

       
3.  Cliquez sur **Enregistrer** pour enregistrer votre règle de classification.

    

### **Modifier une règle de classification**

Pour modifier une règle existante :

1.  Cliquez sur les trois points dans la colonne **Actions**.

    
2.  Sélectionnez **Modifier**.

    
3. Apportez les modifications souhaitées.
4.  Cliquez sur **Enregistrer** pour appliquer les mises à jour.

    

### **Supprimer une règle de classification**

Pour supprimer une règle :

1.  Cliquez sur les trois points dans la colonne **Actions**.

    
2.  Sélectionnez **Supprimer**.

    

## Modèles d'IA

La section **Modèles d'IA** affiche tous les modèles entraînés sur mesure qui ont été spécifiquement ajustés à vos besoins.

### Accéder à la section Modèles d'IA

Pour ouvrir cette section, cliquez sur l'onglet **Modèles d'IA** situé en haut de la page.


### Catégories de modèles

Les modèles sont organisés par catégories. Sous le nom de chaque catégorie figure le nombre de modèles qu'elle contient.\
Cliquez sur une catégorie pour afficher ses détails.


En haut de la page de la catégorie sélectionnée, vous verrez les informations clés de chaque modèle :

* **Type** : le type de modèle.
* **Première page uniquement** : indique si le modèle ne traite que la première page d'un document.
* **Version** : le numéro de version du modèle.

### Tableau des modèles

Tous les modèles d'une catégorie sont répertoriés dans un tableau qui contient les informations suivantes :

* **Nom** : le nom du modèle.
* **Modèle suivant** : le modèle qui traitera ensuite la sortie du modèle actuel.
* **Type de document** : le type de document principal attribué par le modèle lors de la classification.
* **Sous-types de document** : les sous-types dans lesquels le document est ensuite classé.
* **Priorité** : le niveau de priorité qui détermine la position du modèle dans la file de classification.


### Modifier un modèle

Pour modifier un modèle :

1.  Cliquez sur l'icône de crayon dans la colonne **Actions** à côté du modèle à modifier.

    
2. Mettez à jour les champs disponibles :
   * **Modèle suivant** : sélectionnez le modèle qui doit traiter la sortie du modèle actuel.
   * **Type de document** : choisissez le type de document dans lequel le modèle doit classer l'entrée.
3.  Cliquez sur **Enregistrer** pour appliquer vos modifications.

    

<figure><img src="../../../../.gitbook/assets/structured-output-settings-fr-20261104.png" alt="Commandes actuelles d&#x27;extraction. Structured Output est désactivé dans cette configuration existante ; aucun aperçu de schéma n&#x27;est donc affiché. Aucun paramètre d&#x27;extraction n&#x27;a été modifié."><figcaption><p>Commandes actuelles d&#x27;extraction. Structured Output est désactivé dans cette configuration existante ; aucun aperçu de schéma n&#x27;est donc affiché. Aucun paramètre d&#x27;extraction n&#x27;a été modifié.</p></figcaption></figure>
