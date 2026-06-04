# Send HTTPS request to

<figure><img src="../../../../.gitbook/assets/Then_Send_HTTPS_1.png" alt="" width="563"><figcaption></figcaption></figure>

## Objectif :

La carte de workflow **« Send HTTPS Request »** permet aux utilisateurs d'envoyer des requêtes HTTPS vers une URL spécifiée avec des en-têtes, des paramètres et une charge utile de données personnalisables. Cette carte est idéale pour intégrer des API externes ou des services web directement dans le workflow.

## Composants de la carte :

1. **URL**
   * **Description :** spécifie le point de terminaison où la requête HTTPS sera envoyée.
   * **Détail :** saisissez l'URL complète de l'API ou du service web auquel se connecter.
2. **Headers**
   * **Description :** définit les en-têtes à inclure dans la requête HTTPS.
   * **Détail :** fournissez des **paires clé-valeur** au **format JSON valide** pour spécifier des en-têtes tels que des jetons d'authentification ou des types de contenu. Exemple : {"Authorization": "Bearer example\_value"}
3. **Method**
   * **Description :** spécifie la méthode HTTP à utiliser pour la requête.
   * **Options :**
     * **GET :** récupère des données depuis le point de terminaison.
     * **POST :** envoie des données au point de terminaison pour créer ou mettre à jour des ressources.
     * **PUT :** met à jour des ressources existantes au point de terminaison.
     * **DELETE :** supprime des ressources du point de terminaison.
4. **Parameters**
   * **Description :** paires clé-valeur à inclure dans l'URL en tant que paramètres de requête.
   * **Détail :** utilisez-les pour envoyer des filtres ou des données supplémentaires requis par le point de terminaison, au format JSON valide. Voir l'exemple pour Headers.
5. **Data**
   * **Description :** le corps de la requête HTTPS.
   * **Détail :** fournissez la charge utile au format JSON valide. Voir l'exemple pour Headers.

## Fonctionnalité :

* **Évaluation de la condition :** la carte n'envoie la requête HTTPS que si les sections **« Where »** et **« And »** sont évaluées comme vraies.&#x20;
  * Si l'une des conditions est fausse, la requête n'est pas envoyée.
* **Exécution de la requête :**
  * Lorsque les conditions sont satisfaites, le système envoie la requête HTTPS avec les configurations spécifiées.

## Mise en place et configuration :

1. **Définir l'URL :** saisissez le point de terminaison où la requête HTTPS doit être envoyée.
2. **Définir les en-têtes :** fournissez les en-têtes requis sous forme de paires clé-valeur.
3. **Sélectionner la méthode HTTP :** choisissez la méthode appropriée (**GET**, **POST**, **PUT** ou **DELETE**) selon l'action à effectuer.
4. **Ajouter les paramètres :** spécifiez tous les paramètres de requête requis par le point de terminaison.
5. **Fournir la charge utile de données :** saisissez le corps de la requête au format requis (par ex. JSON) si nécessaire.
6. **Configurer les conditions :** définissez les sections **« Where »** et **« And »** pour garantir que la requête n'est envoyée que lorsque des conditions spécifiques sont satisfaites.

## Exemple de carte :

<figure><img src="../../../../.gitbook/assets/Then_Send_HTTPS_2.png" alt="" width="375"><figcaption></figcaption></figure>

## Conclusion :

La carte de workflow **« Send HTTPS Request »** simplifie l'intégration d'API en permettant aux utilisateurs d'effectuer des requêtes personnalisées vers des services externes directement depuis leurs workflows. En automatisant le processus d'envoi de requêtes HTTPS et la gestion des réponses, cette carte améliore la flexibilité et la fonctionnalité du workflow.
