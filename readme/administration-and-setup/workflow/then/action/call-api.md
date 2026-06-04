# Call Api

<figure><img src="../../../../.gitbook/assets/Then_Call_API.png" alt="" width="563"><figcaption></figcaption></figure>

## Objectif :

La carte de workflow **« Call API »** permet aux utilisateurs d'effectuer des requêtes HTTP vers des points de terminaison d'API spécifiés directement depuis le workflow. Cette carte prend en charge diverses méthodes HTTP et permet une interaction dynamique avec des systèmes externes en envoyant des paramètres et des données. Elle rationalise l'intégration avec des services tiers et des API personnalisées, garantissant une communication fluide.

## Composants de la carte :

1. **API Endpoint**
   * **Description :** le point de terminaison cible de l'**API DocBits** avec lequel cette carte interagira.
   * **Détail :** un champ de texte où les utilisateurs spécifient le point de terminaison de la requête d'API.
2. **HTTP Method**
   * **Description :** le type de requête HTTP à effectuer.
   * **Options :**
     1. **GET :** récupère des données depuis le point de terminaison spécifié.
     2. **POST :** envoie des données au point de terminaison.
     3. **PUT :** met à jour des données existantes au point de terminaison.
     4. **DELETE :** supprime des données au point de terminaison.
3. **Parameters**
   * **Description :** les paramètres de requête à inclure dans la requête d'API.
   * **Détail :** un champ de texte ou une liste pour saisir des paires clé-valeur pour l'URL de la requête.
4. **Data**
   1. **Description :** la charge utile à envoyer dans le corps de la requête d'API (applicable aux méthodes POST et PUT).
   2. **Détail :** un champ pour saisir les données au format JSON.

## Fonctionnalité :

**Évaluation de la condition :** le système évalue les conditions définies dans les sections « Where » et « And » :

* Si les deux conditions sont **vraies**, la requête d'API est exécutée telle que configurée.
* Si l'une des conditions est **fausse**, la carte ne s'exécute pas et aucun appel d'API n'est effectué.

**Exécution de la requête d'API :**

* La carte envoie la requête HTTP au point de terminaison spécifié à l'aide de la méthode sélectionnée.
* Tous les paramètres fournis sont ajoutés à l'URL, et les données sont incluses dans le corps de la requête (le cas échéant).

## Mise en place et configuration :

1. **Définir le point de terminaison de l'API :**\
   Saisissez l'URL de l'API que vous souhaitez appeler.
2. **Sélectionner la méthode HTTP :**\
   Choisissez l'une des méthodes prises en charge (GET, POST, PUT, DELETE) selon les exigences de votre API.
3. **Fournir les paramètres :**\
   Ajoutez tous les paramètres de requête requis sous forme de paires clé-valeur.
4. **Inclure les données (le cas échéant) :**\
   Pour les méthodes POST ou PUT, spécifiez les données à envoyer dans le corps de la requête.
5. **Configuration des conditions :**\
   Configurez les sections « Where » et « And » pour définir quand l'appel d'API doit avoir lieu.

## Conclusion :

La carte de workflow **« Call API »** améliore l'automatisation du workflow en permettant une interaction directe avec des systèmes externes. En offrant des configurations flexibles pour les points de terminaison, les méthodes et les données, elle garantit que les workflows peuvent s'intégrer en toute fluidité à des API tierces ou à des backends personnalisés. La possibilité d'exécuter conditionnellement les appels d'API assure précision et efficacité dans l'automatisation des communications externes.

***
