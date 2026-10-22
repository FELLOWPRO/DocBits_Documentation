# Groupes, utilisateurs et autorisations

## Créer un groupe et tester l’accès aux documents

Les autorisations de groupe étant déjà activées, créez un groupe de vérification et ajoutez un utilisateur de test sans droits administrateur. Autorisez la liste, la consultation et la modification des factures attribuées ; laissez la suppression, les modifications en masse et les approbations désactivées. Enregistrez et rouvrez les réglages, puis connectez-vous comme utilisateur ordinaire : la facture attribuée est visible, contrairement au document témoin non attribué.

{% embed url="https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/groups-permissions-admin/v1/fr.mp4" %}

[Voir avec les sous-titres](https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/groups-permissions-admin/v1/fr.html)

Ces paramètres répondent à trois questions différentes : qui peut se connecter, dans quelle sous-organisation la personne travaille, et ce que son groupe est autorisé à faire.

| Si vous devez… | Ouvrez… |
| --- | --- |
| Ajouter ou modifier le compte d'une personne | **Paramètres de la table** → **Utilisateurs** ; lisez ensuite [Users](users/README.md). |
| Organiser les accès entre les unités de l'entreprise | **Paramètres de la table** → **Sous-organisations** ; lisez ensuite [Sub-Organizations](sub-organizations/README.md). |
| Contrôler l'accès par groupe | **Paramètres de la table** → **Groupes et Autorisations** ; lisez ensuite [Groups and Permissions](groups-and-permissions/README.md). |

<figure><img src="../../../../.gitbook/assets/prior-t008-fr.png" alt="Panneau de sélection des groupes."><figcaption><p>Panneau de sélection des groupes.</p></figcaption></figure>

Si un utilisateur ne voit pas un document ou une action, vérifiez d'abord son compte et son organisation. Vérifiez ensuite les autorisations du groupe concerné. Utilisez un compte de test non administrateur pour confirmer l'accès dont disposera réellement un utilisateur normal avant de modifier une organisation en production.
