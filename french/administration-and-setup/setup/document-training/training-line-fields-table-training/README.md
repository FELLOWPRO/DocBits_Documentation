# Entraînement des champs de ligne et des tableaux

## Entraînement des tableaux : quand et comment l’utiliser

DocBits utilise par défaut l'extraction de table basée sur AI, qui fonctionne entre les fournisseurs. Cependant, lorsque vous avez besoin de plus de contrôle sur la façon dont les lignes de détail sont extraits pour un fournisseur spécifique, vous pouvez utiliser **entraînement des tableaux** pour définir la structure manuellement.

#### &#x20;**Important : entraînement propre au fournisseur**

L’entraînement des tableaux est **spécifique à chaque fournisseur**. Si vous entraînez une mise en page de tableau pour un fournisseur, les règles s'appliquent uniquement aux documents de ce fournisseur.\
D'autres fournisseurs continueront à utiliser l'extraction de table basée sur AI à moins d'être formés séparément.

#### Quand utiliser l’entraînement des tableaux ?

Utilisez entraînement des tableaux **uniquement lorsque la mise en page du document est stable** et que vous souhaitez garantir une extraction cohérente et de haute qualité. Il convient particulièrement aux fournisseurs qui :

* Utilisez un **format de facture fixe** dans le temps.
* Exiger un **un mappage précis** des lignes de détail avec des champs spécifiques.
* Sont des **fournisseurs à gros volume**, pour lesquels une automatisation cohérente est précieuse.

#### Quand ne pas utiliser l’entraînement des tableaux

Évitez d’utiliser entraînement des tableaux si :

* Le fournisseur **modifie fréquemment la présentation de sa facture** (par exemple, tous les deux mois).
* Vous ne recevez pas régulièrement des documents de ce fournisseur.
* L'extraction par défaut AI fonctionne **assez bien** sans formation manuelle.

Dans de tels cas, recycler la table à plusieurs reprises serait inefficace et prendrait beaucoup de temps.



## Utilisation :

Le **Mode d’entraînement** est utilisé pour apprendre à DocBits comment extraire correctement les lignes de détail de la mise en page du document d'un fournisseur spécifique.

Lorsque vous êtes en mode Entraînement, vous définissez :

* **Où se trouve le tableau** sur le document.
* **Quelles zones correspondent à chaque colonne** (par exemple, Quantité, Description, Prix unitaire).

Ce mode crée un **modèle d'extraction réutilisable** pour ce fournisseur, de sorte que les futurs documents avec la même mise en page seront traités automatiquement — pas besoin de nouvel entraînement.

**Key Characteristics:**

* **Les colonnes mappées sont en lecture seule** — vous ne pouvez pas modifier manuellement le texte.
* Vous **ne pouvez pas ajouter ou supprimer des lignes**.
* L'accent est mis sur la cartographie des positions , et non sur la correction des valeurs.
* Une fois que vous avez fini de mapper le tableau et ses colonnes, cliquez sur **“Save Rules”** pour que DocBits apprenne et applique cet entraînement à des documents similaires provenant du même fournisseur.



Le **Mode de correction** vous permet de **corriger les erreurs d'extraction** dans les données du tableau du document actuel. Il est utilisé lorsque DocBits a déjà tenté d'extraire le tableau, mais que les résultats nécessitent de petites corrections.

Use Correction Mode when:

* Certaines valeurs **sont manquantes ou mal alignées**.
* Une **ligne vide ou en double** a été extraite et doit être supprimée.

**Ce que vous pouvez faire en mode correction :**

* **Ajustez manuellement les valeurs** dans les colonnes mappées (par exemple, corrigez les mauvais placements).
* **Supprimez les lignes** qui ne devraient pas faire partie du tableau.
* **Ajoutez les lignes** qui ont été entièrement manquées lors de l'extraction.
