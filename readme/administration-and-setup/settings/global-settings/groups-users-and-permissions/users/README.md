# Utilisateurs

<figure><img src="../../../../../.gitbook/assets/users_settings.png" alt="Gestion des utilisateurs"><figcaption><p>Page de gestion des utilisateurs</p></figcaption></figure>

La page Utilisateurs permet aux administrateurs de gérer tous les comptes utilisateurs de votre organisation DocBits. Vous pouvez y ajouter de nouveaux utilisateurs, attribuer des rôles et contrôler les accès.

## Liste des utilisateurs

Le tableau des utilisateurs affiche les colonnes suivantes :

| Colonne | Description |
|--------|-------------|
| **Nom** | Le nom complet de l'utilisateur. |
| **E-mail** | L'adresse e-mail de l'utilisateur, qui sert d'identifiant de connexion. |
| **Dernière connexion** | Date et heure de la connexion la plus récente de l'utilisateur. |
| **Admin** | Case à cocher indiquant si l'utilisateur dispose des privilèges d'administrateur. Les Admins peuvent accéder à tous les paramètres et gérer les autres utilisateurs. |
| **System Admin** | Case à cocher désignant l'unique System Admin de l'organisation — le compte que DocBits utilise pour les actions automatiques, en arrière-plan (comme les imports et exports automatisés). Un System Admin dispose toujours aussi des privilèges d'Admin. Consultez [Privilèges d'administration](admin-privileges.md#admin-vs-system-admin) pour comprendre la différence entre Admin et System Admin. |
| **Actif** | Case à cocher indiquant si le compte utilisateur est actuellement actif. Les utilisateurs inactifs ne peuvent pas se connecter. |
| **Actions** | Menu proposant des options telles que la modification des détails de l'utilisateur, la réinitialisation des mots de passe ou la désactivation du compte. |

Utilisez la barre de **Recherche** en haut pour retrouver rapidement des utilisateurs par nom ou par identifiant.

## Statistiques de connexion

Cliquez sur **Statistiques de connexion** pour consulter les données d'activité de connexion de l'ensemble de votre organisation, notamment la fréquence et les habitudes de connexion.

Consultez [Statistiques de connexion](login-analytics.md) pour le détail complet.

## Ajouter un nouvel utilisateur

1. Cliquez sur le bouton **Ajouter un utilisateur** en haut à droite.
2. Renseignez les informations requises :
   * **Nom d'utilisateur** : un nom unique pour l'utilisateur.
   * **Prénom** et **Nom** : le nom complet de l'utilisateur.
   * **Adresse e-mail** : utilisée pour la connexion et les notifications.
   * **Mot de passe** : doit respecter les règles de sécurité de votre organisation.
   * **Rôle de l'utilisateur** : attribuez le rôle approprié (Standard User, Admin ou System Admin).
3. Cliquez sur **Enregistrer** pour créer le compte utilisateur. Le nouvel utilisateur recevra une notification par e-mail contenant ses identifiants de connexion.

> **Remarque :** le rôle **System Admin** ne peut être choisi qu'au moment de la création d'un utilisateur — il ne peut pas être ajouté ni retiré par la suite. Chaque organisation ne peut avoir qu'un seul System Admin, et le choisir accorde automatiquement aussi les droits d'Admin. Consultez [Privilèges d'administration](admin-privileges.md#admin-vs-system-admin) pour savoir quand l'utiliser.
