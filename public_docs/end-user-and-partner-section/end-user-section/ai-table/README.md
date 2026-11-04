# AI Table

AI Table permet de vérifier les lignes extraites, corriger les colonnes et enregistrer des instructions pour une mise en page fournisseur. Choisissez le guide adapté. Structured Output dispose de son propre guide : Par défaut/Oui/Non, dérogations, aperçu et exemple complet.

* [Paramètres et dérogations](configuration.md)
* [Structured Output pour les tableaux](structured-output.md)
* [Colonnes et corrections](columns-and-corrections.md)
* [Instructions IA](ai-instructions.md)
* [Étiquettes de tableau AI](ai-table-tags.md)
* [Expliquer l'extraction et diagnostiquer](explain-extraction.md)
* [Assistant et droits](assistant-and-permissions.md)

<figure><img src="../../../.gitbook/assets/anatomy-ai-table.svg" alt="Illustration isométrique d'un lecteur de tableau : une tête de lecture avec une cartouche d'instructions parcourt un tableau de document, un tableau de connexions branche chaque colonne renvoyée sur une colonne configurée, et les colonnes configurées se dressent comme des bacs avec chacun un bouton Use AI à trois positions."><figcaption><p>L'IA lit le tableau et renvoie des colonnes. Chaque colonne renvoyée est associée à une colonne de tableau configurée (une colonne renvoyée sans association reste masquée), chaque colonne configurée dispose de son propre réglage Use AI (Par défaut, Oui ou Non), et les instructions IA ainsi que <strong>Enregistrer comme formation</strong> déterminent la manière dont les documents suivants de cette mise en page fournisseur sont lus.</p></figcaption></figure>

## Quand obtenez-vous le tableau AI

* Un administrateur a activé **Extraction de table AI** (Paramètres → Traitement des documents → Classification et extraction, voir [Paramètres pour les administrateurs](#parametres-pour-les-administrateurs)). Si l'option est désactivée, la zone du tableau affiche *La table AI s'affichera ici. Activer dans …*.
* Vérifiez le texte lisible ou l'entrée Vision. Des règles classiques enregistrées peuvent encore déterminer le chemin effectif ; contrôlez [le chemin réellement utilisé](../../../overview-and-basics/faq/document-processing/which-extraction-path-was-used.md).
* Chaque colonne dispose d'une sélection Use AI à trois états. Vérifiez aussi la source effective et les règles fournisseur ; Structured Output ne remplace pas tous les tableaux issus de règles.

Le niveau d'IA qui lit le tableau (Fast, Full, Nexus) est défini par organisation et peut être remplacé par fournisseur, voir Modèle d'IA Spécifique au Fournisseur pour l'Extraction de Champs et de Tableaux.

## Le tableau AI en un coup d'œil

<figure><img src="../../../.gitbook/assets/ai-table-overview-fr.png" alt="Tableau extrait IA avec ses en-têtes de colonnes et quatre lignes"><figcaption><p>Les deux onglets, le Tableau extrait IA et ses en-têtes de colonnes.</p></figcaption></figure>

* **Onglets.** *Tableau extrait IA* est ce que l'IA a lu. *Tableau extrait* est le tableau classique issu des règles entraînées. L'onglet IA s'ouvre par défaut lorsque le document possède un tableau AI.
* **En-tête de colonne.** Chaque colonne affiche son nom, un petit symbole d'**origine** (survolez-le : *IA · cartographie*, *IA · synonyme*, etc. indiquent comment l'IA a associé la colonne), un menu **trois points** et, pour une colonne mappée, un **bouton de nom** sur lequel vous pouvez cliquer pour changer de quelle colonne il s'agit.
* **Boutons de ligne.** Le **x** au début d'une ligne supprime cette ligne. Un clic droit sur une ligne propose *Sélectionner comme coût supplémentaire* / *Remove as additional cost*.
* **Barre d'outils du pied de page.** Les icônes en bas de l'écran ajoutent ou masquent des colonnes et des lignes, voir [Barre d'outils du pied de page](#barre-doutils-du-pied-de-page).
* **Carte Instructions pour l'IA** sous le tableau : prompt, colonnes supplémentaires, **Test de changement**, **Appliquer**, **Enregistrer comme formation**, **Supprimer**, **Exporter**, voir [Donner des instructions à l'IA](#donner-des-instructions-a-lia).

{% hint style="info" %}
Les commandes de colonne ne fonctionnent que si vous pouvez modifier le document. Si elles sont grisées, le document est en lecture seule ou verrouillé dans une autre session. Lorsque le bandeau rouge indique que le document est verrouillé par votre propre utilisateur dans une autre session, **Déverrouiller** reprend le verrou.
{% endhint %}


## Paramètres pour les administrateurs

Poursuivre ici: [Paramètres et dérogations](configuration.md).

### Utiliser l'IA par colonne

Poursuivre ici: [Structured Output pour les tableaux](structured-output.md).

<a id="choisir-la-bonne-colonne-remappage"></a>
<a id="le-menu-trois-points"></a>
<a id="barre-doutils-du-pied-de-page"></a>

## Modifier une colonne

Poursuivre ici: [Colonnes et corrections](columns-and-corrections.md).

<a id="suggérer-avec-nexus"></a>
<a id="suggerer-avec-nexus"></a>
<a id="tester-appliquer-enregistrer--ce-que-fait-chaque-bouton"></a>

## Donner des instructions à l'IA

Poursuivre ici: [Instructions IA](ai-instructions.md).


## Voir ce que l'IA a fait

Poursuivre ici: [Expliquer l'extraction et diagnostiquer](explain-extraction.md).


## Exemples pratiques

Poursuivre ici: [Expliquer l'extraction et diagnostiquer](explain-extraction.md).

<a id="suggérer-une-règle-à-votre-administrateur"></a>
<a id="suggerer-une-regle-a-votre-administrateur"></a>

## L'Assistant et le tableau AI

Poursuivre ici: [Assistant et droits](assistant-and-permissions.md).


## Qui peut faire quoi

Poursuivre ici: [Assistant et droits](assistant-and-permissions.md).

## Pages associées

* [Étiquettes de tableau AI](ai-table-tags.md)
* [Formation des Champs de Ligne/Table de Formation](../../../administration-and-setup/setup/document-training/training-line-fields-table-training/README.md)
* [Touchless Intelligence](../../../administration-and-setup/touchless-intelligence.md)
