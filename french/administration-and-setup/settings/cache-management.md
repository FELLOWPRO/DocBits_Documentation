# Gestion du cache

<figure><img src="../../.gitbook/assets/cache_management.png" alt="Gestion du cache"><figcaption><p>Page de gestion du cache</p></figcaption></figure>

La gestion du cache contrôle le nettoyage automatique du cache pour les données fréquemment consultées. L'activation du cache améliore les performances en réduisant les appels d'API répétés.

## Vider le cache

Cliquez sur le bouton **Clear Cache** (en haut à droite) pour invalider immédiatement et manuellement toutes les données mises en cache.

## Tableau du cache

| Colonne | Description |
|--------|-------------|
| **Object** | Le type de données mises en cache (par exemple, Receive Delivery Cache, Purchase Order Cache). |
| **Status** | Bouton permettant d'activer ou de désactiver la mise en cache pour cet objet. |
| **TTL** | Durée de vie (Time to Live) en minutes : durée pendant laquelle les données mises en cache restent valides avant d'être actualisées automatiquement. Définissez `0` pour désactiver l'expiration automatique. |

## Caches disponibles

| Cache | Description |
|-------|-------------|
| **Receive Delivery Cache** | Met en cache les données de réception de livraison utilisées lors du rapprochement avec les commandes d'achat. |
| **Purchase Order Cache** | Met en cache les données des commandes d'achat pour accélérer la recherche pendant le traitement des documents. |
| **Task and Notification Cache** | Met en cache le nombre de tâches et les données de notification affichés dans le tableau de bord. |
