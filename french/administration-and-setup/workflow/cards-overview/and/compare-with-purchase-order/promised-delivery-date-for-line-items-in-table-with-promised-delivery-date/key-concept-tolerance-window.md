# Concept clé : la fenêtre de tolérance

Avant d'examiner les opérateurs, il est important de comprendre comment la fenêtre de tolérance est calculée.

## Qu'est-ce qu'une fenêtre de tolérance ?

La fenêtre de tolérance définit une plage de dates acceptables autour de la date de livraison promise du bon de commande.

**Exemple :**

* Date du bon de commande : **9 janvier**
* Jours de tolérance : **3**
* Fenêtre de tolérance : **6 janvier → 12 janvier**

> <mark style="color:red;">Seuls les</mark> <mark style="color:red;"></mark><mark style="color:red;">**Allowed Tolerance Days**</mark> <mark style="color:red;"></mark><mark style="color:red;">sélectionnés (jours de la semaine) sont comptabilisés lors du calcul de cette fenêtre.</mark>

### Exemple de chronologie visuelle

```
← Passé                          Futur →
|-----|-----|-----|-----|-----|-----|-----|
     6 Jan      9 Jan      12 Jan
   (Début)    (Date BC)    (Fin)
```

### Comportement des opérateurs expliqué par l'exemple

* **Equals (=)**
  * **Signification :**\
    La date de livraison de la ligne doit se situer _à l'intérieur_ de la fenêtre de tolérance.
  * **Dates valides :**
    * Toute date entre le **6 janv. et le 12 janv.** (inclus)
  * **Dates invalides :**
    * Toute date **antérieure au 6 janv.**
    * Toute date **postérieure au 12 janv.**
* **Not Equals (≠)**
  * **Signification :**\
    La date de livraison de la ligne doit se situer _en dehors_ de la fenêtre de tolérance.
  * **Dates valides :**
    * Toute date **antérieure au 6 janv.**
    * Toute date **postérieure au 12 janv.**
  * **Dates invalides :**
    * Les dates entre le **6 janv. et le 12 janv.**
* **Greater or Equals (≥)**
  * **Signification :**\
    La date de livraison de la ligne doit être égale ou postérieure au **début de la fenêtre de tolérance**.
  * **Dates valides :**
    * **6 janv. → toute date future**
  * **Dates invalides :**
    * Toute date **antérieure au 6 janv.**
  * <mark style="color:red;">**Important :**</mark>\
    Cet opérateur autorise les dates _à l'intérieur_ de la fenêtre de tolérance **et au-delà**.
* **Lesser or Equals (≤)**
  * **Signification :**\
    La date de livraison de la ligne doit être égale ou antérieure à la **fin de la fenêtre de tolérance**.
  * **Dates valides :**
    * Toute date passée jusqu'au **12 janv.**
  * **Dates invalides :**
    * Toute date **postérieure au 12 janv.**
* **Greater Than (>)**
  * **Signification :**\
    La date de livraison de la ligne doit être _strictement postérieure_ à la fenêtre de tolérance.
  * **Dates valides :**
    * **13 janv. → toute date future**
  * **Dates invalides :**
    * Toute date **égale ou antérieure au 12 janv.**
* **Lesser Than (<)**
  * **Signification :**\
    La date de livraison de la ligne doit être _strictement antérieure_ à la fenêtre de tolérance.
  * **Dates valides :**
    * Toute date **antérieure au 6 janv.**
  * **Dates invalides :**
    * Toute date **égale ou postérieure au 6 janv.**

## Comment les « Allowed Tolerance Days » affectent la fenêtre de tolérance

Lors du calcul de la fenêtre de tolérance, **seuls les jours de la semaine sélectionnés sont comptabilisés**.\
Les jours non sélectionnés (comme les week-ends ou les jours de semaine exclus) sont **entièrement ignorés**.

#### Exemple : calcul de tolérance basé sur les jours de la semaine

**Configuration :**

* Date du bon de commande : **mercredi 9 janvier**
* Jours de tolérance : **3**
* Allowed Tolerance Days : **lundi, mardi, mercredi, jeudi, vendredi**
* Week-ends (samedi, dimanche) : **non sélectionnés**

#### Calcul étape par étape

À partir de la date du BC (**9 janv.**) :

**Décompte vers l'arrière (3 jours de tolérance) :**

* Mardi 8 janv. → **Jour 1**
* Lundi 7 janv. → **Jour 2**
* Dimanche 6 janv. → _Ignoré (non autorisé)_
* Samedi 5 janv. → _Ignoré (non autorisé)_
* Vendredi 4 janv. → **Jour 3**

➡ **Date de début de tolérance : vendredi 4 janvier**

**Décompte vers l'avant (3 jours de tolérance) :**

* Jeudi 10 janv. → **Jour 1**
* Vendredi 11 janv. → **Jour 2**
* Samedi 12 janv. → _Ignoré_
* Dimanche 13 janv. → _Ignoré_
* Lundi 14 janv. → **Jour 3**

➡ **Date de fin de tolérance : lundi 14 janvier**

#### Fenêtre de tolérance résultante

```
4 janvier  →  14 janvier
```

#### Pourquoi c'est important

Si les Allowed Tolerance Days sont mal configurés :

* Les dates de livraison peuvent apparaître **valides ou invalides de manière inattendue**
* Les livraisons anticipées ou tardives peuvent ne pas être détectées correctement
