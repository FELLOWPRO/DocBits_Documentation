---
description: Créer une copie distincte d'une règle de validation personnalisée existante pour un type de document.
---

# Dupliquer une règle de validation personnalisée

Utilisez **Duplicata** lorsqu'une règle constitue un bon point de départ et que vous souhaitez une copie distincte. DocBits copie la définition de la règle ; vous choisissez le nom et la clé de la nouvelle règle. La règle d'origine reste dans la liste.

1. Ouvrez **Paramètres → Types de Documents**, sélectionnez le type de document à configurer, activez la fonction **Règles de validation personnalisées**, puis choisissez **Gérer les règles de validation**. La page affiche le type de document sélectionné au-dessus des cartes de règles. Voir [Types de Document](README.md) pour les autres paramètres disponibles.
2. Recherchez la règle source. Si la liste est longue, utilisez le champ de recherche ou les filtres de portée et de statut. Ouvrez le menu à trois points de la règle et sélectionnez **Duplicata**. Vous pouvez copier une règle par défaut du système ou une règle sur mesure.
3. Dans **NOM DE LA RÈGLE**, conservez le nom proposé se terminant par « Copy » ou saisissez un nom plus clair. La **CLÉ DE RÈGLE** est générée à partir de ce nom. Sélectionnez l'icône crayon si vous devez modifier la clé vous-même.
4. Sélectionnez **Duplicata** pour créer la règle distincte. DocBits actualise la liste après l'enregistrement. Sélectionnez **Annuler** pour fermer la fenêtre sans créer de copie.

<figure><img src="../../../../.gitbook/assets/custom_validation_rule_duplicate_fr.png" alt="Fenêtre française « Règle en double » avec les champs NOM DE LA RÈGLE et CLÉ DE RÈGLE, l'icône crayon et les boutons Annuler et Duplicata"><figcaption><p>La fenêtre française « Règle en double » dans l'organisation de test DocBits Sandbox. Le nom copié et la clé peuvent être modifiés avant de sélectionner Duplicata.</p></figcaption></figure>

Le bouton **Duplicata** exige un nom et une clé. Si l'enregistrement échoue, DocBits affiche un message d'erreur ; corrigez le nom ou la clé, puis réessayez. Vérifiez la nouvelle règle avant de l'activer ou de la modifier, car une copie démarre avec la définition de la règle source.
