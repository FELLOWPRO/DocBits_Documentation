# Tableau de bord

## Aperçu

Les paramètres du tableau de bord sont conçus pour aider les administrateurs à contrôler la présentation des données et l'interaction au sein du tableau de bord DocBits. Ces paramètres déterminent quelles informations sont immédiatement disponibles lors de la connexion, garantissant que les utilisateurs ont un accès rapide aux données les plus pertinentes pour leurs tâches.

![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/dashboard_settings_1.png)

## Accéder aux Paramètres du Tableau de bord

Pour accéder aux paramètres du tableau de bord, naviguez vers :\
**Paramètres → Paramètres globaux → Tableau de bord**

![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/settings_dashboard.png)

## **Général**

* **Réinitialiser les filtres** : Permet de configurer quand les filtres du tableau de bord doivent être réinitialisés, par exemple après le téléchargement de documents, le redémarrage de documents ou l'exportation de documents. Cela aide à maintenir une vue propre des données selon les étapes spécifiques du flux de travail.
* **Données du tableau de bord** :
  * **Chargement automatique du tableau de bord** : Contrôle si le tableau de bord doit charger automatiquement les données lors de l'accès de l'utilisateur, ce qui peut aider à réduire les temps de chargement et à améliorer l'expérience utilisateur en ne chargeant les données que lorsque cela est nécessaire.
  *   **Exporter les données du tableau de bord** : Cette fonctionnalité ajoute un nouveau bouton **Exporter** à la barre d'outils du tableau de bord, vous permettant d'exporter la vue actuelle du tableau de bord en tant que fichier **.csv** ou **.xlsx**.

      ![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/dashboard_settings_3.png)

## **Historique des exportations**

Dans l'**Historique des exportations**, vous verrez un tableau répertoriant toutes les exportations passées avec des informations clés sur chaque demande.

![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/dashboard_settings_4.png)

Les détails suivants sont inclus :

* **E-mail** : L'adresse e-mail à partir de laquelle l'exportation a été demandée.
* **Statut** : Le statut actuel de l'exportation (En attente, Terminé).
* **Demandé le** : La date et l'heure auxquelles l'exportation a été initiée.
* **Terminé le** : La date et l'heure auxquelles l'exportation a été complétée.
* **Format** : Le format de fichier utilisé pour l'exportation (CSV, XLSX).
* **Filtres utilisés** : Tous les filtres qui ont été appliqués au tableau de bord au moment de l'exportation.

<mark style="color:red;">**Remarque**</mark> : Pour exporter des tableaux, l'option Exporter les données du tableau de bord dans la section [Général](./#general) doit être active.

## **Action**

* **Attribuer à** : Cette fonctionnalité permet aux utilisateurs de définir des autorisations pour l'attribution de documents.
  * **Uniquement pour les Admin** : Seuls les utilisateurs administrateurs peuvent attribuer des documents, indépendamment des autorisations accordées aux utilisateurs non administrateurs.
  * **Tous les utilisateurs** : Tous les utilisateurs qui ont reçu les [autorisations](../groups-users-and-permissions/groups-and-permissions/activating-permissions.md) nécessaires peuvent attribuer des documents.
* **Redémarrer** : Cette fonctionnalité permet aux utilisateurs de définir des autorisations pour redémarrer des documents.
  * **Uniquement pour les Admin** : Seuls les utilisateurs ayant des privilèges d'administrateur peuvent redémarrer des documents, indépendamment des autorisations accordées aux utilisateurs non administrateurs.
  * **Uniquement Admin et Attribué** : Seuls les utilisateurs ayant des privilèges d'administrateur et l'utilisateur attribué peuvent redémarrer le document.
  * **Tous les utilisateurs** : Tous les utilisateurs qui ont reçu les [autorisations](../groups-users-and-permissions/groups-and-permissions/activating-permissions.md) nécessaires peuvent redémarrer des documents.

![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/dashboard_settings_2.png)

## **Filtres**

* **Filtre d'état Style** : Détermine le style de présentation des filtres d'état, qui peut être défini par défaut ou personnalisé selon l'orientation opérationnelle des utilisateurs.
* **Filtre d'état personnalisé** : Permet la création et l'application de filtres personnalisés qui peuvent cibler des statuts de documents spécifiques comme "Nouveau", "Validation", ou "Exportation". Cela permet aux utilisateurs d'accéder rapidement aux documents à des étapes spécifiques de traitement.

![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/dashboard_settings_5.png)

## Advance Shipment Dashboard

* **Visibilité des commandes livrées** : Cette fonctionnalité permet à l'utilisateur de spécifier la durée pendant laquelle les commandes livrées seront visibles.

![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/dashboard_settings_6.png)

Ces paramètres de tableau de bord sont cruciaux pour garantir que la plateforme DocBits soit aussi réactive et utile que possible, fournissant aux utilisateurs un outil puissant pour surveiller et gérer les activités de traitement de documents directement depuis le tableau de bord.
