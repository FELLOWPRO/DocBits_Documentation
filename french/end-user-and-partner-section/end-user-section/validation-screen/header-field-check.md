---
description: >-
  D'où vient la valeur d'un champ d'en-tête et comment elle est créée :
  l'explication derrière le Contrôle des champs d'en-tête sur l'écran de
  validation.
---

# Contrôle des champs d'en-tête : d'où viennent les données

Le bouton **Contrôle des champs d'en-tête** se trouve à côté de **Enregistrer** sur l'écran de validation. Il ouvre le rapport *D'où vient chaque valeur ?* : pour chaque champ d'en-tête, il montre ce qui figurait sur le document, ce qui a modifié la valeur en chemin, ce que DocBits affiche maintenant et pourquoi.

Cette page explique comment une valeur est créée et ce que signifie chaque source. Aucune connaissance d'expert n'est nécessaire.

{% hint style="info" %}
Le Contrôle des champs d'en-tête fait partie du module **Analytics**. Si le bouton est grisé, un administrateur peut l'accorder à votre rôle sous **Paramètres › Rôles**.
{% endhint %}

## Une valeur est toujours créée dans cet ordre

| Étape | Ce qui se passe |
| --- | --- |
| **1. Lire** | La valeur est lue dans le document — par une règle entraînée, par l'IA ou directement depuis une facture électronique. |
| **2. Transformer** | Les scripts et les règles de transformation du client modifient la valeur lue : la raccourcir, la compléter, adapter son format. |
| **3. Rechercher** | La valeur est recherchée dans les données de base. Si quelque chose est trouvé, l'enregistrement des données de base remplace la valeur lue. |
| **4. Afficher** | L'utilisateur ne voit que le résultat. Ce qui s'est passé en chemin est montré par le Contrôle des champs d'en-tête. |

Les étapes 2 et 3 ne s'exécutent pas toujours — mais lorsqu'elles s'exécutent, elles modifient la valeur. C'est précisément de là que viennent la plupart des cas signalés.

## Les sources — ce que chacune signifie

Les icônes sont les mêmes que celles du rapport dans la colonne **Action** et dans la barre de filtres en haut.

### Règle entraînée

DocBits mémorise où se trouve un champ sur ce type de document, parce que quelqu'un l'y a un jour marqué.

* **Exemple :** fournisseur « Bornemann » — toujours au même endroit, en haut à gauche.
* **En cas d'erreur :** marquez le bon emplacement sur le document et enregistrez — la règle en tire des enseignements.

### IA

Pas de modèle fixe. L'IA lit le document comme une personne et décide elle-même quel texte appartient à quel champ.

* **Exemple :** date de facture, montants, conditions de paiement.
* **En cas d'erreur :** corrigez-la. On peut l'activer et la désactiver sous **Paramètres › Champs d'en-tête OCR**.

### Facture électronique

Avec XRechnung ou ZUGFeRD, rien n'est reconnu : la valeur est déjà un champ de données dans le document et est reprise directement.

* **Exemple :** numéro de facture issu du champ XML de l'expéditeur.
* **En cas d'erreur :** l'erreur vient de l'expéditeur. DocBits montre exactement de quel champ XML provient la valeur.

### Script / règle de transformation

Après la lecture, la logique du client intervient et remodèle la valeur. Le document reste le même — la valeur non.

* **Exemple :** `1001 / LS 206776` devient `1001`.
* **En cas d'erreur :** ne la cherchez pas sur le document. Vérifiez **Paramètres › Scripts** ou **Règles de transformation**.

### Données de base

La valeur lue est recherchée dans vos propres données — commandes, fournisseurs. Une correspondance remplace la valeur et entraîne d'autres champs avec elle.

* **Exemple :** `1001` trouve la commande `06O051001` — et le fournisseur et l'acheteur proviennent alors aussi de là.
* **En cas d'erreur :** vérifiez **Paramètres › Configuration du Lookup**. Elle indique si la recherche est exacte ou accepte aussi les correspondances partielles.

### Calculé

Non pas lu, mais calculé à partir d'autres champs.

* **Exemple :** date d'échéance à partir de la date de facture plus les conditions de paiement.
* **En cas d'erreur :** en général, l'un des champs à partir desquels le calcul est fait est incorrect.

### Code-barres

Lu à partir d'un code-barres ou d'un code QR sur le document.

* **Exemple :** le numéro de facture est encodé dans le code QR.
* **En cas d'erreur :** vérifiez les paramètres de code-barres du type de document.

## Ce qui est le plus souvent mal compris

{% hint style="warning" %}
Lorsqu'un champ contient soudain une valeur qui n'apparaît pas ainsi sur le document, ce n'est presque jamais l'IA, mais l'étape 2 ou l'étape 3. Le plus souvent, la correspondance dans les données de base, qui accepte aussi les correspondances partielles : `1001` correspond à `06O051001`, et avec la commande trouvée, le fournisseur change lui aussi.
{% endhint %}

Dans le rapport, un tel champ est marqué en rouge. La colonne **Action** montre l'enregistrement des données de base avec une pastille rouge *correspondance partielle uniquement*, et la partie correspondante de la valeur est surlignée.

## Lire le rapport

* **Pastilles d'état** en haut comptent les champs venus tels quels du document, modifiés en chemin, ou absents du document sous cette forme. Cliquez sur une pastille pour n'afficher que ces champs ; cliquez à nouveau pour tout afficher.
* **Filtre de source :** la rangée d'icônes montre chaque méthode d'extraction. Cliquez sur l'une d'elles pour n'afficher que les champs qui y sont passés.
* **Action :** chaque étape que la valeur a traversée, avec l'icône de sa source. L'étape dont provient la valeur actuelle est surlignée. Survolez pour voir ce que chaque étape a fait, de quelle valeur à quelle valeur.
* **Motif :** l'état du champ. L'icône (i) explique pourquoi la valeur est ce qu'elle est. Si elle indique *Le champ n'existait pas*, le champ n'était pas présent sur le document.
* Les valeurs longues sont abrégées par … — survolez pour voir la valeur complète.
