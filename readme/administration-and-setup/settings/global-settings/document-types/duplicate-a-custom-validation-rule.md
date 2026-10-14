---
description: Créez une copie distincte d'une règle de validation personnalisée existante pour un type de document.
---

# Dupliquer une règle de validation personnalisée

Utilisez **Duplicate** lorsqu'une règle constitue un bon point de départ et que vous souhaitez en obtenir une copie distincte. DocBits copie la définition de la règle ; vous choisissez le nom et la clé de la nouvelle règle. La règle d'origine reste dans la liste.

1. Accédez à **Settings → Document Types**, ouvrez le type de document que vous souhaitez configurer, puis sélectionnez **Custom Validation Rules**. La page affiche le type de document sélectionné au-dessus des cartes de règles. Consultez [Types de documents](README.md) pour les autres paramètres disponibles à cet endroit.
2. Repérez la règle source. Utilisez le champ de recherche ou les filtres de portée et de statut si la liste est longue. Ouvrez son menu d'actions à trois points et sélectionnez **Duplicate**. Vous pouvez copier une règle système par défaut ou une règle personnalisée.
3. Dans **Rule Name**, conservez le nom suggéré se terminant par « Copy » ou saisissez un nom plus explicite. La **Rule Key** est générée à partir de ce nom. Sélectionnez l'icône en forme de crayon si vous devez modifier la clé vous-même.
4. Sélectionnez **Duplicate** pour créer la règle distincte. DocBits actualise la liste après l'enregistrement. Sélectionnez **Cancel** pour fermer la boîte de dialogue sans créer de copie.

<figure><img src="../../../../.gitbook/assets/custom_validation_rule_duplicate_en.png" alt="Boîte de dialogue Duplicate Rule en anglais avec Rule Name, Rule Key, icône en forme de crayon, boutons Cancel et Duplicate"><figcaption><p>La boîte de dialogue Duplicate Rule en anglais dans l'organisation de test DocBits Sandbox. Le nom et la clé copiés peuvent être modifiés avant de sélectionner Duplicate.</p></figcaption></figure>

Le bouton **Duplicate** nécessite à la fois un nom et une clé. Si l'enregistrement échoue, DocBits affiche une erreur ; corrigez le nom ou la clé et réessayez. Vérifiez la nouvelle règle avant de l'activer ou de la modifier, car une copie démarre avec la définition de la règle source.
