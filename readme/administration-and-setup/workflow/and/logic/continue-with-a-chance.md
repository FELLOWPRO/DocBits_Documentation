# Continue with a chance

<figure><img src="../../../../.gitbook/assets/image (49).png" alt="" width="563"><figcaption></figcaption></figure>

## **Objectif :**

Cette carte DocBits introduit une condition probabiliste, permettant aux workflows de se poursuivre avec une probabilité définie. La carte est utile pour les scénarios de test, les sélections aléatoires ou la variabilité contrôlée au sein des processus.

## **Fonctionnalité :**

* **Poursuite conditionnelle :** cette carte poursuit le workflow en fonction d'une probabilité spécifiée, définie par l'utilisateur sous forme de valeur en pourcentage. La carte génère un résultat aléatoire et le compare au pourcentage indiqué, créant une probabilité contrôlée de poursuite du workflow.
* **Pourcentage de probabilité :** les utilisateurs spécifient une valeur en pourcentage (0-100 %) qui représente la probabilité que le workflow se poursuive. Par exemple :
  * **0 % :** le workflow ne se poursuivra jamais.
  * **50 % :** le workflow a une chance sur deux de se poursuivre.
  * **100 % :** le workflow se poursuivra toujours.

## **Utilisation :**

Cette carte est utile dans les scénarios nécessitant des chemins de workflow aléatoires, comme les tests A/B, l'échantillonnage contrôlé ou la simulation de processus. Elle peut également être utilisée pour ajouter de la variabilité dans des workflows automatisés.

## **Scénario d'exemple :**

* Un utilisateur configure la carte avec une **probabilité de 30 %**. Lorsque le workflow atteint cette carte, il y a une probabilité de 30 % que le workflow passe à l'étape suivante. Cette configuration est idéale pour les scénarios où un échantillonnage aléatoire ou un traitement partiel est souhaité.

En utilisant la carte « Conditional Continuation », les organisations peuvent introduire une part d'aléatoire contrôlée dans les workflows, faciliter les expériences de processus et améliorer la prise de décision grâce à des conditions probabilistes.
