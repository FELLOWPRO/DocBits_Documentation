---
hidden: true
---

# Comparaison entre la confirmation de commande et le bon de commande

Utilisez **Comparaison des bons de commande** dans le Constructeur de flux de travail lorsqu'une confirmation de commande doit être vérifiée par rapport à son bon de commande. Ajoutez la carte sous **Et....**, puis choisissez les données de commande, un opérateur et ce qui doit se produire avec le résultat. Les captures ci-dessous montrent deux versions disponibles de la carte dans l'interface en français. Leurs champs sont encore des espaces réservés ; configurez-les pour votre propre flux de travail avant d'enregistrer.

## Écrire le résultat dans un champ

<figure><img src="../../../../.gitbook/assets/workflow-card-qa-20261021-card-77711a53d4d0-fr.png" alt="Champs de la carte dans la version affichée. Les champs ne sont pas encore renseignés." width="563"><figcaption><p>Champs de la carte dans la version affichée. Les champs ne sont pas encore renseignés.</p></figcaption></figure>

Choisissez **Données de commande** dans la confirmation de commande et un **Opérateur** pour la comparaison avec le bon de commande. Saisissez le **Texte** à écrire, sélectionnez le **Nom du champ** et choisissez le **Résultat de la condition** qui doit déclencher l'écriture.

## Comparer les données

<figure><img src="../../../../.gitbook/assets/workflow-card-qa-20261021-card-d49578e0648e-fr.png" alt="Champs de la carte dans la version affichée. Les champs ne sont pas encore renseignés." width="563"><figcaption><p>Champs de la carte dans la version affichée. Les champs ne sont pas encore renseignés.</p></figcaption></figure>

Choisissez **N'importe quel/Tous** pour décider si une ou toutes les conditions sélectionnées doivent correspondre. Sélectionnez ensuite les **Données de commande**, l'**Opérateur** et les **Données comparatives** pour la comparaison avec le bon de commande.

Pour les étapes environnantes, voir [Flux de travail](../..) et [Comparaison des bons de commande](.).

<!-- workflow-card-practical-example-20261021 -->

## Exemple pratique

**Quand utiliser :** Vérifiez une confirmation de commande par rapport à son bon de commande lié.

**Configuration :** Utilisez une commande de démonstration et une confirmation avec le même fournisseur, la même référence d'article et les mêmes valeurs comparées. Sélectionnez le sens de comparaison prévu et les champs proposés par cette version.

**Résultat attendu et contre-exemple :** La comparaison correspondante réussit. Modifiez une valeur d'élément comparé dans un scénario de test distinct et vérifiez qu'elle est détectée ; une commande liée manquante est un problème de données distinct.

Il s’agit d’une configuration illustrative et du résultat attendu. Utilisez les champs, utilisateurs et groupes configurés dans votre organisation de test ; cela ne veut pas dire que cet exemple a été exécuté.
