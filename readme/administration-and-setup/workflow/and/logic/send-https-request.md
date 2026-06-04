# Send HTTPS Request

<figure><img src="../../../../.gitbook/assets/image (4) (1) (1) (1) (1) (1).png" alt="" width="563"><figcaption></figcaption></figure>

## **Objectif :**

Cette carte DocBits est conçue pour faciliter l'interaction avec des systèmes externes en envoyant des requêtes HTTPS vers des URL spécifiées. Elle permet aux workflows d'effectuer des actions telles que la récupération, la mise à jour ou la suppression de données en réalisant des appels d'API, garantissant une intégration fluide avec des services externes.

## **Fonctionnalité :**

* **Exécution de requête HTTPS :** la carte envoie une requête vers une URL spécifiée à l'aide de la méthode HTTP configurée (par ex. GET, POST, PUT, DELETE).
* **En-têtes et paramètres :** les utilisateurs peuvent inclure des en-têtes personnalisés et des paramètres de requête pour s'assurer que la requête respecte les exigences de l'API externe.
* **Données de la requête :** permet aux utilisateurs de définir la charge utile (le cas échéant) à envoyer avec la requête, comme des données JSON ou encodées sous forme de formulaire.
* **Évaluation de la réponse :** le workflow vérifie si le code de statut reçu correspond à la valeur attendue, garantissant une communication réussie avant de poursuivre.
* **Méthodes HTTP prises en charge :**
  * GET : récupère des données depuis l'URL spécifiée.
  * POST : soumet des données à l'URL spécifiée pour créer des ressources.
  * PUT : met à jour des ressources existantes à l'URL spécifiée.
  * DELETE : supprime des ressources de l'URL spécifiée.

## **Utilisation :**

Cette carte est particulièrement utile dans les scénarios où les workflows doivent interagir avec des API externes pour échanger des données, comme envoyer des mises à jour à un CRM, récupérer des statuts de commande ou publier de nouvelles entrées dans une base de données.

## **Scénario d'exemple :**

* Un utilisateur configure la carte pour envoyer une requête POST à un système externe de gestion des commandes avec une charge utile contenant les détails d'une nouvelle commande. Des en-têtes personnalisés sont ajoutés pour inclure des jetons d'authentification d'API. La carte est configurée pour ne se poursuivre que si le code de statut de la réponse est 201 (Created). Si le code de statut diffère, le workflow déclenche une notification d'erreur pour une intervention manuelle.

En utilisant la carte « Send HTTPS Request », les organisations peuvent automatiser les intégrations externes, améliorer la communication entre les systèmes et rationaliser les workflows complexes.
