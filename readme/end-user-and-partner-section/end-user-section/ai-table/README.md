# Tableau AI

Le Tableau extrait par IA est le tableau des éléments de ligne que DocBits lit avec l'IA lorsqu'un fournisseur ne dispose pas de règles de tableau entraînées. Il apparaît sur l'écran de validation, sous les champs d'en-tête. Cette page explique quand vous l'obtenez, comment le relancer et comment orienter ce qu'il extrait.

## Quand obtenez-vous le tableau AI

* Un administrateur a activé **Extraction de tableaux par IA** (Paramètres → Traitement des documents → Classification et extraction). Si l'option est désactivée, la zone du tableau affiche *AI Table will display here. Enable in …*.
* Le fournisseur n'a **aucune règle enregistrée**. Dès que quelqu'un entraîne le tableau du fournisseur et clique sur *Enregistrer les règles*, les règles enregistrées remplacent le tableau AI pour ce fournisseur ; les lignes apparaissent alors dans l'onglet *Tableau extrait* au lieu de l'onglet *Tableau extrait par IA*.
* Exception : les colonnes marquées **Utiliser l'IA** dans les paramètres des colonnes de tableau sont remplies par l'IA même pour les fournisseurs disposant de règles enregistrées, voir la section « Utiliser l'IA par colonne » ci-dessous.

Le niveau d'IA qui lit le tableau (Fast, Full, Nexus) est défini par organisation et peut être remplacé par fournisseur sous *Plus de paramètres* sur l'écran de validation, voir [Modèle d'IA spécifique au fournisseur](../validation-screen/supplier-specific-ai-model-for-field-and-table-extraction.md).

## Réextraire le tableau AI

Utilisez cette procédure lorsque des lignes manquent ou qu'une colonne est décalée et que vous souhaitez que l'IA réessaie, par exemple après avoir ajouté une [étiquette](ai-table-tags.md) :

1. Ajoutez ou modifiez des [étiquettes](ai-table-tags.md) dans le champ sous le tableau et cliquez sur **Appliquer**. L'IA reconstruit le tableau pour ce document avec vos étiquettes et vos modifications de colonnes ; rien n'est encore enregistré pour le fournisseur. Si le document comporte des lignes rapprochées avec un bon de commande, DocBits avertit que la reconstruction supprime ces correspondances.
2. Le résultat vous convient ? Cliquez sur **Enregistrer** (*Enregistrer les règles*) pour que le prochain document de ce fournisseur soit extrait de la même manière.
3. Pour repartir de zéro, cliquez sur **Supprimer** (*Supprimer les règles*) : DocBits confirme *Rules has been deleted successfully* et relance l'extraction par IA sans aucune étiquette ni règle de formatage enregistrée.

*Supprimer les règles* supprime les étiquettes et les règles de formatage enregistrées pour ce fournisseur, pas la configuration des colonnes de tableau. Pour réextraire l'ensemble du document (en-tête et tableau) après qu'un administrateur a modifié des paramètres ou des colonnes, utilisez plutôt *Redémarrer* dans le menu du document sur le tableau de bord.

## Utiliser l'IA par colonne

Chaque colonne de tableau possède un indicateur **Utiliser l'IA** (Paramètres → Paramètres globaux → Types de documents → [Colonnes de tableau](../../../administration-and-setup/settings/global-settings/document-types/table-columns.md)). Lorsqu'il est activé, l'IA remplit cette colonne même si le fournisseur dispose de règles enregistrées ; les autres colonnes continuent de provenir des règles. Cas d'usage typique : une colonne de description en texte libre que les règles entraînées capturent mal, ou une valeur qui change de place sur la page.

Gardez à l'esprit que l'IA devine alors cette colonne à partir de la ligne entière. Si elle y place systématiquement la mauvaise valeur (par exemple le total de ligne dans *Frais*), le contrôle du total de ligne échoue sur chaque ligne. Dans ce cas, désactivez *Utiliser l'IA* pour cette colonne, ou ajoutez une étiquette qui indique à l'IA ce que représente la colonne.

## Extraction structurée

Lorsque **Utiliser l'extraction structurée (IA)** est activé dans les paramètres de l'organisation, l'IA renvoie le tableau dans une structure fixe qui correspond directement aux colonnes de tableau configurées, au lieu de reprendre les en-têtes de colonnes du fournisseur. Les noms de colonnes correspondent alors toujours à votre configuration ; une colonne imprimée par le fournisseur mais que vous n'avez pas configurée n'est pas extraite. Demandez à votre administrateur de l'activer lorsque les en-têtes des fournisseurs varient beaucoup et que vous passez du temps à remapper.

## Travailler avec le tableau extrait

Voici les principales capacités et instructions d'utilisation :

* **Suppression de colonnes** : Si certaines colonnes du tableau extrait ne sont pas nécessaires, les utilisateurs peuvent facilement les supprimer en cliquant sur l'icône "Supprimer la colonne" (représentée par trois points verticaux) à côté de l'en-tête de la colonne. Cela permet de désencombrer le tableau et de se concentrer uniquement sur les informations pertinentes.

<figure><img src="../../../.gitbook/assets/ai-table1.png" alt=""><figcaption></figcaption></figure>

* **Changement de format de devise** : Le format de la devise peut être modifié en sélectionnant le format souhaité dans le menu déroulant à côté du champ "Devise". Cela garantit que les valeurs monétaires sont affichées dans le format préféré, facilitant ainsi l'interprétation et l'analyse des données financières.

<figure><img src="../../../.gitbook/assets/ai-table2.png" alt=""><figcaption></figcaption></figure>

* **Affichage/Masquage des colonnes non mappées** : Par défaut, seules les colonnes mappées (colonnes avec des données extraites) sont visibles dans le tableau. Cependant, les utilisateurs peuvent choisir d'afficher ou de masquer les colonnes non mappées en cliquant sur le bouton "Masquer les colonnes non mappées" ou "Afficher les colonnes non mappées" en bas du tableau. Cette fonctionnalité est utile lorsque les utilisateurs souhaitent examiner toutes les colonnes disponibles, même si elles ne contiennent pas actuellement de données.

<figure><img src="../../../.gitbook/assets/ai-table3.png" alt=""><figcaption></figcaption></figure>

* **Modification des en-têtes de tableau** : Les en-têtes de tableau (noms de colonnes) peuvent être modifiés en cliquant sur l'en-tête et en saisissant le nom souhaité. Cette fonctionnalité permet aux utilisateurs de personnaliser les noms de colonnes pour mieux s'aligner sur leur terminologie ou leurs préférences, rendant les données plus lisibles et compréhensibles.

<figure><img src="../../../.gitbook/assets/ai-table4.png" alt=""><figcaption></figcaption></figure>

* **Enregistrer vos modifications** : **Enregistrer** à côté des étiquettes (info-bulle *Enregistrer les règles*) stocke le mappage de colonnes, les colonnes masquées et les étiquettes actuels pour ce fournisseur. Le prochain document du fournisseur est extrait avec ces réglages.

Ces fonctionnalités vous donnent le contrôle sur les données extraites. Lorsque le même fournisseur nécessite les mêmes corrections à chaque fois, entraînez plutôt le tableau une fois ([Training Line Fields / Table Training](../../../administration-and-setup/setup/document-training/training-line-fields-table-training/README.md)) ; le tableau AI n'est alors plus utilisé pour ce fournisseur.
