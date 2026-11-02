# Notre Système de Priorité des Documents

Dans notre système de traitement des documents, nous gérons un grand volume de documents provenant de plusieurs clients chaque jour. Pour garantir que les documents de chaque client soient traités en temps voulu, nous avons mis en place un système de priorité sophistiqué. Ce système ajuste dynamiquement les priorités en fonction du nombre de documents en attente qu'un client a, assurant ainsi **l'équité** et **l'efficacité**. Plongeons dans le fonctionnement de ce système de priorité et quand le compteur de tâches est réinitialisé.

**Concepts Clés du Système de Priorité**

Notre système de priorité repose sur quelques concepts clés :

1. **Documents en Attente** : Il s'agit d'un compte des documents qu'un client a soumis mais qui n'ont pas encore été traités.
2. **Intervalle de Réinitialisation** : Le système réinitialise périodiquement le compte des documents en attente à zéro pour s'assurer qu'aucun client ne puisse monopoliser indéfiniment les ressources de traitement.

**Comment la Priorité est Déterminée**

Voici une explication étape par étape de la façon dont la priorité pour le traitement des documents est déterminée :

1. **Suivi des Documents en Attente** : Chaque client a un compte de documents en attente. Ce compte nous aide à savoir combien de documents attendent d'être traités pour chaque client.
2. **Réinitialisation du Compte** : Pour maintenir l'équité, nous réinitialisons le compte des documents en attente à zéro si un certain temps (l'intervalle de réinitialisation) s'est écoulé depuis la dernière mise à jour. Cet intervalle est fixé par défaut à 1500 secondes (ou 25 minutes).
3. **Mise à Jour du Compte** : Si l'intervalle de réinitialisation n'est pas écoulé, nous réduisons le compte des documents en attente d'un chaque fois que nous vérifions, simulant le traitement d'un document.
4. **Définition des Priorités** : La priorité pour le traitement des tâches est basée sur le nombre de documents en attente. Moins il y a de documents en attente, plus la priorité est élevée, ce qui signifie que ces tâches seront traitées plus tôt. Nous avons des seuils spécifiques pour attribuer des niveaux de priorité de 1 (priorité la plus élevée) à 9 (priorité la plus basse).

**Niveaux de Priorité**

Les niveaux de priorité sont attribués en fonction du compte des documents en attente comme suit :

* **Priorité 9** : Si le compte des documents en attente est inférieur à -20
* **Priorité 8** : Si le compte des documents en attente est inférieur à -14
* **Priorité 7** : Si le compte des documents en attente est inférieur à -12
* **Priorité 6** : Si le compte des documents en attente est inférieur à -10
* **Priorité 5** : Si le compte des documents en attente est inférieur à -8
* **Priorité 4** : Si le compte des documents en attente est inférieur à -6
* **Priorité 3** : Si le compte des documents en attente est inférieur à -4
* **Priorité 2** : Si le compte des documents en attente est inférieur à -2
* **Priorité 1** : Si le compte des documents en attente est supérieur ou égal à -2

{% hint style="info" %}
En termes plus simples, à mesure que le nombre de documents en attente augmente, le niveau de priorité diminue, ce qui signifie que ces documents sont traités plus tard par rapport à d'autres avec des priorités plus élevées.
{% endhint %}

**Quand le Compteur est Réinitialisé**

Le compteur des documents en attente est réinitialisé à zéro si plus que l'intervalle de réinitialisation (**1500** secondes) s'est écoulé depuis la dernière mise à jour. Ce mécanisme garantit qu'aucun client ne puisse accumuler indéfiniment des documents en attente et monopoliser les ressources du système. En réinitialisant périodiquement le compteur, nous garantissons que chaque client obtienne une part équitable de temps de traitement.
