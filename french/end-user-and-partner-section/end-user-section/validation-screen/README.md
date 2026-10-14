# Écran de validation

{% embed url="https://youtu.be/CmmQIxOaF6E?si=gYE-U-Jv4dLPi2xT" %}

## Vue d'ensemble

<figure><img src="../../../.gitbook/assets/validation_screen1.png" alt=""><figcaption></figcaption></figure>

### Origine du Document (Document Origin)

{% embed url="https://youtu.be/-m45XGiIeig" %}
DocBits Origin Setting Explained: Country Standards for Dates & Number Formats
{% endembed %}

### **Bouton Enregistrer:**

<figure><img src="../../../.gitbook/assets/validation_screen2.png" alt=""><figcaption></figcaption></figure>

* **Bouton Enregistrer:**
  * **Objectif :** Enregistre l'état actuel du document ou du script en cours de travail.
  * **Cas d'utilisation :** Après avoir apporté des modifications ou des annotations à un document, utilisez ce bouton pour vous assurer que toutes les modifications sont enregistrées.

### **Ajouter des règles spéciales:**

<figure><img src="../../../.gitbook/assets/validation_screen3.png" alt=""><figcaption></figcaption></figure>

<figure><img src="../../../.gitbook/assets/validation_screen4.png" alt=""><figcaption></figcaption></figure>

* **Ajouter des règles spéciales / Ajouter un script dans DocBits :**
  * **Objectif :** Permet aux utilisateurs de mettre en œuvre des règles ou des scripts spécifiques qui personnalisent le traitement des documents.
  * **Cas d'utilisation :** Utilisez cette fonctionnalité pour automatiser des tâches telles que l'extraction de données ou la validation de format, améliorant ainsi l'efficacité du flux de travail.

{% hint style="info" %}
Voir ici ajouter [Script dans DocBits](../../../administration-and-setup/settings/global-settings/document-types/script/scripting-in-docbits/)
{% endhint %}

### **Champs flous:**

<figure><img src="../../../.gitbook/assets/validation_screen5.png" alt=""><figcaption></figcaption></figure>

* **Champs flous:**
  * **Objectif:** Aide à identifier et corriger les champs où les données peuvent ne pas correspondre parfaitement mais sont suffisamment proches.
  * **Cas d'utilisation:** Utile dans les processus de validation de données où des correspondances exactes ne sont pas toujours possibles, comme des noms ou adresses légèrement mal orthographiés.

### **Champs obligatoires:**

<figure><img src="../../../.gitbook/assets/validation_screen6.png" alt=""><figcaption></figcaption></figure>

Il y a des champs requis pour une édition ultérieure, ceux-ci peuvent être modifiés dans les paramètres.

Utilisez l'info-bulle pour savoir si:

* Est-ce un champ obligatoire (requis)
* Validation requise
* Faible confiance
* Inadéquation du montant total des taxes

**Champs obligatoires:**

* **Objectif :** Identifie les champs obligatoires dans les documents qui doivent être remplis ou corrigés avant un traitement ultérieur.
* **Cas d'utilisation :** Assure que les données essentielles sont capturées avec précision, maintenant l'intégrité des données et la conformité aux règles de l'entreprise.

<figure><img src="https://lh7-us.googleusercontent.com/3-ZXi-fUcWlM0nUaOAQbY7bynchbIN30JReKRdijyMFvX_GIHrnbcismANdOi6UfYa6GCPvk9wnOixya0E_rBk3V8hQduS-gBZJi4k0Kq8jeN93DxC2w5J-YRqeV9IkVB6oiH8tm0-y7gWJO_8fBplo" alt=""><figcaption></figcaption></figure>

## Tableau extrait (éléments de ligne)

<figure><img src="../../../.gitbook/assets/validation_screen_line_items_table.png" alt="Tableau des éléments de ligne sur l'écran de validation avec la barre d'outils du tableau"><figcaption><p>Le tableau extrait sous les champs d'en-tête</p></figcaption></figure>

Sous les champs d'en-tête, DocBits affiche le tableau des éléments de ligne du document : une ligne par ligne de facture, une colonne par [colonne de tableau](../../../administration-and-setup/settings/global-settings/document-types/table-columns.md) configurée pour le type de document. Lorsqu'un type de document comporte plusieurs tableaux (par exemple les articles et les frais), chaque tableau a son propre onglet au-dessus de la grille.

### D'où vient le tableau

Au-dessus de la grille figure un onglet par chemin d'extraction activé dans l'organisation :

| Onglet | Signification |
|---|---|
| **Tableau extrait** | Extraction basée sur des règles (paramètre *Extraction de tableaux*). Pour un fournisseur dont le tableau a été entraîné, ces lignes proviennent des règles enregistrées et sont extraites de la même manière sur chaque document de ce fournisseur ; pour un fournisseur non entraîné, l'onglet peut être vide. |
| **Tableau extrait par IA** | L'extraction de tableau par IA (paramètre *Extraction de tableaux par IA*). Rempli lorsque le fournisseur n'a pas de règles enregistrées, et pour les colonnes marquées *Utiliser l'IA* même lorsque des règles existent. Une info-bulle *AI table not found* sur l'onglet signifie que l'IA n'a rien renvoyé pour ce document. |
| **Tableaux de bon de commande** | Uniquement dans le générateur de mise en page : les lignes du bon de commande utilisées pour la correspondance. |

Si aucun de ces onglets n'apparaît, les deux paramètres de tableau sont désactivés pour l'organisation (Paramètres → Traitement des documents → Classification et extraction). Le niveau d'IA qui lit le tableau est défini par organisation et peut être remplacé par fournisseur, voir [Modèle d'IA spécifique au fournisseur](supplier-specific-ai-model-for-field-and-table-extraction.md).

### Travailler dans le tableau

* **Modifier une cellule** : cliquez dedans et saisissez la valeur. Les colonnes de type montant, nombre et date sont validées pendant la saisie.
* **Ajouter une nouvelle ligne de tableau** : ajoute une ligne vide à la fin. Utilisez-la lorsqu'une ligne n'a pas été reconnue.
* **Supprimer une ligne** : l'icône de corbeille en fin de ligne.
* **Ajouter les colonnes mappées vides** : affiche les colonnes configurées que l'IA a laissées vides, afin de les remplir à la main.
* **Restaurer une colonne de tableau** : rétablit une colonne que vous aviez retirée de la vue pour ce document.
* **Supprimer le tableau** : efface toutes les lignes de ce tableau sur ce document. La configuration n'est pas modifiée.
* **Ajouter une nouvelle colonne de tableau** (administrateurs) : la même boîte de dialogue que dans les paramètres des colonnes de tableau, sans quitter le document.
* **Étiquettes** (tableau AI uniquement) : de courtes indications textuelles pour l'IA, par exemple *« la dernière colonne est le montant net »*. Voir [Étiquettes de tableau AI](../ai-table/ai-table-tags.md).
* **Appliquer** / **Enregistrer** / **Supprimer** à côté des étiquettes : *Appliquer* relance le tableau AI pour ce document avec les étiquettes et les modifications de colonnes que vous avez faites, sans rien enregistrer (si le document comporte des lignes rapprochées avec un bon de commande, DocBits avertit que ces correspondances seront supprimées) ; *Enregistrer les règles* enregistre le mappage de colonnes et les étiquettes actuels pour ce fournisseur ; *Supprimer les règles* les supprime et relance l'extraction par IA pour ce document.
* **Exporter** : télécharge le tableau sous forme de fichier CSV.
* **Aller à la vue d'extraction de tableau** : ouvre l'entraînement de tableau pour ce document. Utilisez-la lorsque le même fournisseur donne systématiquement de mauvais résultats : tracez le tableau une fois, mappez les colonnes et cliquez sur *Enregistrer les règles* ; à partir de là, les lignes apparaissent dans l'onglet *Tableau extrait*. Voir [Training Line Fields / Table Training](../../../administration-and-setup/setup/document-training/training-line-fields-table-training/README.md).

{% hint style="info" %}
Si le tableau a été extrait par l'IA et que vous ouvrez l'entraînement de tableau, DocBits demande *Table is already extracted by AI. Do you want to train manually?* Une fois les règles enregistrées, le tableau AI n'est plus utilisé pour ce fournisseur.
{% endhint %}

### Réextraire le tableau

* **Même document, tableau AI :** ajoutez ou modifiez des étiquettes et cliquez sur **Appliquer** ; le tableau AI est reconstruit pour ce document uniquement. Pour supprimer aussi les étiquettes et le formatage enregistrés pour le fournisseur, cliquez sur **Supprimer** (*Supprimer les règles*) : DocBits confirme *Rules has been deleted successfully* et relance l'extraction par IA.
* **Même document, règles entraînées :** ouvrez *Aller à la vue d'extraction de tableau*, corrigez le tableau et cliquez sur *Enregistrer et réextraire*.
* **Document entier (en-tête et tableau) :** Tableau de bord → menu du document → *Redémarrer*. Nécessaire après qu'un administrateur a modifié les colonnes de tableau ou les paramètres d'extraction.

### Ce qui bloque l'approbation

Le tableau est contrôlé lors de l'enregistrement ou de l'approbation. Une cellule rouge ou un message sous le tableau signifie l'une des situations suivantes :

| Message | Cause | Que faire |
|---|---|---|
| Colonne obligatoire vide | Une colonne marquée *Obligatoire* n'a pas de valeur dans cette ligne. | Remplissez la cellule, ou demandez à un administrateur si la colonne doit vraiment être obligatoire. |
| *Line total does not match quantity x unit price (expected …, got …)* | `quantité × prix unitaire + frais − remise` s'écarte du total de ligne de plus de 0,02. Souvent, l'une des quatre valeurs a été lue dans la mauvaise colonne. | Corrigez la valeur erronée par rapport au document ; si une colonne telle que *Frais* est systématiquement remplie avec la mauvaise valeur, prévenez votre administrateur (voir la section Dépannage de la page [Colonnes de tableau](../../../administration-and-setup/settings/global-settings/document-types/table-columns.md)). |
| *Line items add up to … but the net total is …* | La somme des totaux de ligne diffère du montant net de l'en-tête. | Recherchez une ligne manquante ou en double, ou un montant d'en-tête mal lu. |
| *Line Item Table is missing Mandatory column for PO* | La correspondance de bon de commande nécessite le numéro d'article, le prix unitaire, la quantité et le montant total ; l'une de ces colonnes est masquée. | Administrateur : réaffichez la colonne sous Colonnes de tableau. |

Un administrateur peut désactiver tous les contrôles de tableau pour un type de document avec *Ignorer la validation du tableau* (Types de documents → Plus de paramètres) ; les écarts de ligne et les colonnes obligatoires vides ne sont alors plus signalés.

En savoir plus sur les contrôles : [Vérifications automatiques sur l'écran de validation](automatic-checks-on-the-validation-screen.md) et [Dépannage de l'extraction de table](../../../overview-and-basics/faq/document-processing/table-extraction-troubleshoot.md).

### **Loupe:**

<figure><img src="../../../.gitbook/assets/validation_screen7.png" alt="" width="118"><figcaption></figcaption></figure>

* **Loupe:**
  * **Objectif:** Fournit une vue agrandie d'une zone sélectionnée du document.
  * **Cas d'utilisation:** Aide à examiner les détails fins ou les petits textes dans les documents, assurant l'exactitude de la saisie ou de la révision des données.

<figure><img src="../../../.gitbook/assets/validation_screen8.png" alt="" width="329"><figcaption></figcaption></figure>

### **Ouvrir une nouvelle fenêtre:**

<figure><img src="../../../.gitbook/assets/validation_screen9.png" alt="" width="130"><figcaption></figcaption></figure>

* **Ouvrir une nouvelle fenêtre:**
  * **Objectif:** Ouvre une nouvelle fenêtre pour une comparaison de documents côte à côte ou pour le multitâche.
  * **Cas d'utilisation:** Utile lors de la comparaison de deux documents ou lors de la consultation d'informations supplémentaires sans quitter le document actuel.

### **Raccourcis clavier:**

<figure><img src="../../../.gitbook/assets/validation_screen10.png" alt="" width="145"><figcaption></figcaption></figure>

* **Raccourcis clavier:**
  * **Objectif:** Permet aux utilisateurs d'effectuer des actions rapidement à l'aide de combinaisons de touches.
  * **Cas d'utilisation:** Améliore la rapidité et l'efficacité de la navigation et du traitement des documents en minimisant la dépendance à la navigation à la souris.

<figure><img src="../../../.gitbook/assets/validation_screen11.png" alt="" width="239"><figcaption></figcaption></figure>

### **Tâches:**

<figure><img src="../../../.gitbook/assets/validation_screen12.png" alt="" width="55"><figcaption></figcaption></figure>

Pour partager des informations internes, vous pouvez créer des tâches et les attribuer à un employé ou un groupe spécifique au sein de l'entreprise.

* **Tâches:**
  * **Objectif:** Permet aux utilisateurs de créer des tâches liées aux documents et de les attribuer aux membres de l'équipe.
  * **Cas d'utilisation:** Facilite la collaboration et la gestion des tâches au sein des équipes, assurant que chacun connaît ses responsabilités.

<figure><img src="../../../.gitbook/assets/validation_screen13.png" alt="" width="218"><figcaption></figcaption></figure>

### **Mode annotation:**

<figure><img src="../../../.gitbook/assets/validation_screen_annotation_mode.png" alt="Annotation Mode Button" width="187"><figcaption></figcaption></figure>

<figure><img src="../../../.gitbook/assets/annotation_mode_example.png" alt="Annotation Mode Example"><figcaption></figcaption></figure>

{% embed url="https://youtu.be/ay0gGtwlqRE" %}
DocBits Annotation Mode Tutorial: Add Notes in Validation & Download With/Without Annotations
{% endembed %}

You can leave annotations on a document. This can be helpful to leave information for other users who further edit this document.

* **Mode annotation:**
  * **Objectif :** Permet aux utilisateurs de laisser des notes ou des annotations directement sur le document.
  * **Cas d'utilisation:** Utile pour fournir des commentaires, des instructions ou des notes importantes à d'autres membres de l'équipe qui travailleront sur le document plus tard.

### **Fusionner:**

<figure><img src="../../../.gitbook/assets/validation_screen16.png" alt="" width="60"><figcaption></figcaption></figure>

Les documents peuvent être fusionnés ici, par exemple si une page d'une facture manquait, ces pages peuvent être fusionnées plus tard de cette manière sans que le document entier doive être supprimé ou re-téléchargé.

* **Fusionner des documents:**
  * **Objectif:** Combine plusieurs documents en un seul fichier.
  * **Cas d'utilisation:** Pratique dans les scénarios où des parties d'un document sont numérisées séparément et doivent être consolidées.

### **Vue OCR:**

<figure><img src="../../../.gitbook/assets/validation_screen17.png" alt="" width="77"><figcaption></figcaption></figure>

Dans la vue OCR, le texte est automatiquement filtré du document. Cela est utilisé pour reconnaître des caractéristiques pertinentes, telles que le code postal, le numéro de contrat, le numéro de facture et le tri d'un document.

* **Vue OCR:**
  * **Objectif:** Reconnaît automatiquement le texte dans les documents à l'aide de la technologie de reconnaissance optique de caractères.
  * **Cas d'utilisation:** Rationalise le processus de numérisation des textes imprimés ou manuscrits, les rendant consultables et modifiables.

<figure><img src="../../../.gitbook/assets/validation_screen18.png" alt=""><figcaption></figcaption></figure>

### **Créer un ticket:**

<figure><img src="../../../.gitbook/assets/validation_screen19.png" alt="" width="97"><figcaption></figcaption></figure>

Contrairement aux tâches qui sont transmises en interne au sein de l'entreprise, ce ticket de support est important pour nous notifier et créer immédiatement un ticket en cas d'erreurs et/ou de divergences. Cela rend le processus beaucoup plus facile car vous pouvez immédiatement envoyer le bug avec le document approprié. Il y a aussi l'option de définir la priorité, de prendre une capture d'écran du document ou d'en télécharger une.

* **Créer un ticket:**
  * **Objectif:** Permet aux utilisateurs de signaler des problèmes ou des divergences en créant un ticket de support.
  * **Cas d'utilisation:** Essentiel pour une résolution rapide des problèmes et des bugs, aidant à maintenir l'intégrité et le bon fonctionnement du système.

<figure><img src="../../../.gitbook/assets/validation_screen20.png" alt="" width="237"><figcaption></figcaption></figure>

### **Journaux de scripts de documents:**

<figure><img src="../../../.gitbook/assets/validation_screen21.png" alt="" width="160"><figcaption></figcaption></figure>

Les scripts peuvent être créés dans les paramètres sous Types de documents ; ces informations seront ensuite affichées ici.

* **Journaux de scripts de documents:**
  * **Objectif:** Affiche les journaux liés aux scripts qui ont été mis en œuvre pour différents types de documents.
  * **Cas d'utilisation:** Utile pour suivre et déboguer les actions des scripts sur les documents, aidant les utilisateurs à comprendre les processus automatisés et à corriger les éventuels problèmes.

<figure><img src="../../../.gitbook/assets/validation_screen22.png" alt=""><figcaption></figcaption></figure>

### **Plus de paramètres:**

<figure><img src="../../../.gitbook/assets/docbits_table_invoice_3.png" alt="DocBits Tableau Facture 3"><figcaption></figcaption></figure>

### **Flux de documents:**

Vous y trouverez le flux du document

* **Objectif:** Montre la séquence et la progression du traitement des documents dans le système.
* **Cas d'utilisation:** Aide à suivre le statut du document à travers différentes étapes, assurant que toutes les étapes de traitement nécessaires sont suivies.

### **Aller au modèle de mise en page:**

* Avec cette option, vous serez redirigé et pourrez éditer votre mise en page ou utiliser le modèle par défaut
* **Aller au modèle de mise en page:**
  * **Objectif:** Redirige les utilisateurs vers un éditeur de mise en page où ils peuvent modifier les modèles existants ou appliquer un modèle par défaut.
  * **Cas d'utilisation:** Permet la personnalisation des mises en page de documents pour répondre à des besoins ou préférences spécifiques de l'entreprise, améliorant l'alignement visuel et fonctionnel du document avec les normes de l'entreprise.

### Utiliser E-Text si Disponible

* **Objectif :** Permet à DocBits d'utiliser le texte électronique pour tous les documents d'un fournisseur spécifique si disponible, améliorant ainsi la précision de l'extraction.
* **Cas d'utilisation :** Améliore l'extraction de texte en tirant parti du texte intégré au lieu de l'OCR, ce qui peut conduire à des résultats plus précis pour ce fournisseur.

### [Modèle AI Basé sur le Fournisseur](supplier-specific-ai-model-for-field-and-table-extraction.md)

* **Objectif :** Permet de choisir entre trois modèles AI différents pour optimiser les résultats d'extraction pour un fournisseur spécifique.
* **Cas d'utilisation :** Assure une meilleure précision d'extraction en choisissant le modèle AI le plus adapté à la structure et au contenu des documents de chaque fournisseur.
