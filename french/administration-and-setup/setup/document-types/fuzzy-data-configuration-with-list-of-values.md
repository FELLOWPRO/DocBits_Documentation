---
hidden: true
---

# Configuration des données floues avec une liste de valeurs

### **Vue d'ensemble**

Chaque type de document possède ses propres configurations de liste de valeurs (LoV), qui doivent être définies séparément. Contrairement aux **données floues avec données de référence**, la **liste de valeurs** n'est pas fournie avec des groupes de recherche par défaut.

### Pour configurer une liste de valeurs, naviguez vers :

Settings → Global Settings → Document Types → Invoice → Fields → Master Data Settings → LOV Master Data

### **Créer une nouvelle configuration de liste de valeurs**

Il existe deux façons de créer une configuration de liste de valeurs :

**1. Dupliquer une recherche existante**

* Cela copie toutes les informations et tous les champs d'un groupe existant.
* Vous n'avez qu'à indiquer un **nouveau nom**.

**2. Créer une recherche de zéro**

* Cliquez sur **« Create List of Values »**.
* Renseignez les informations requises :
  * **Configuration Name** → Nom de la liste de valeurs.
  * **Lookup Table** → La table dont les valeurs seront récupérées.
  * **Conflict Handler** → Choisissez l'une des options :
    * Best Score
    * Return None
    * Return First
  * **Context Type** → Détermine si la LoV s'applique au niveau **Header** ou **Line**.
  * **Match All** → _(Plus de détails nécessaires)_

### **Gérer les champs d'un groupe de liste de valeurs**

Chaque groupe LoV contient des champs qui peuvent être **ajoutés, supprimés ou modifiés.**

**Ajouter un nouveau champ**

Pour ajouter un nouveau champ dans un groupe :

* Cliquez sur **« Create »** dans le groupe concerné.
* Indiquez les informations suivantes :
  * **Lookup Field** → Le nom de la colonne de la table de recherche.
  * **Validation Field** → Le champ DocBits correspondant.
  * **Parent Field** → _(Plus de détails nécessaires)_
  * **Search Operator** → Choisissez l'une des options :
    * Smart
    * Contains
    * Exact
    * Starts with
    * Ends with
  * **Cases à cocher :**
    * **Auto Trigger** → Lorsque cette option est activée, si un autre champ d'une configuration de recherche différente partage la même colonne, ce champ sera mis à jour **automatiquement** chaque fois que l'autre champ est mis à jour.
    * **Searchable** → Active le champ comme champ **List of Values**, permettant des recherches dans la table de recherche.

#### **Dernière étape : ajouter les champs à la mise en page**

Après avoir configuré les champs de la liste de valeurs, **veillez à les ajouter à la mise en page avec le Layout Builder**. Si les champs ne sont pas ajoutés à la mise en page, ils ne seront pas disponibles.
