# Opérateur DocBits

## Aperçu

L'**Opérateur DocBits** est un assistant d'automatisation alimenté par l'IA conçu pour simplifier les tâches répétitives dans vos flux de travail. Les utilisateurs créent des _invites_ - des instructions étape par étape améliorées avec des variables - qui guident l'IA pour naviguer, saisir des données et cliquer à travers les interfaces automatiquement. Cela réduit les efforts manuels et accélère les opérations routinières.

## Activation de l'Opérateur DocBits

Pour activer l'Opérateur DocBits, suivez ces étapes :

1. **Accéder aux Paramètres**:
   * Depuis le Tableau de bord, accédez aux **Paramètres**.
   *   Sélectionnez **Traitement de document** puis choisissez **Module**.

       ![](https://docs.docbits.com/~gitbook/image?url=https%3A%2F%2F578966019-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FT2n2w4uDCJvv7CJ5zrdk%252Fuploads%252F4Yyo7aXyVeWyfJHclHpK%252Fimage.png%3Falt%3Dmedia%26token%3D0071c149-3ea8-452b-a2e3-0fbbc9d3b496\&width=768\&dpr=4\&quality=100\&sign=23009aa7\&sv=2)
2. **Activer la Fonctionnalité**:
   * Faites défiler pour localiser l'option **Opérateur DocBits**.
   *   Basculez le curseur pour activer l'**Opérateur DocBits**.

       <div align="left"><img src="https://docs.docbits.com/~gitbook/image?url=https%3A%2F%2F578966019-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FT2n2w4uDCJvv7CJ5zrdk%252Fuploads%252FyqNyGI2OelO415pf3RHN%252Fimage.png%3Falt%3Dmedia%26token%3D8899a256-a1d6-486f-aaf6-b8e244f9b348&#x26;width=768&#x26;dpr=4&#x26;quality=100&#x26;sign=ce097a28&#x26;sv=2" alt="" width="563"></div>

## Accès à l'Interface

*   Une fois la fonctionnalité activée, ouvrez l'**Opérateur DocBits** depuis le menu de navigation principal.

    ![](https://docs.docbits.com/~gitbook/image?url=https%3A%2F%2F578966019-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FT2n2w4uDCJvv7CJ5zrdk%252Fuploads%252FS67AFPuaQ3CNXQ7Oe80V%252Fimage.png%3Falt%3Dmedia%26token%3D6b6d6782-cc16-48e6-8622-5c596ac54f57\&width=768\&dpr=4\&quality=100\&sign=e6d0fd8e\&sv=2)

### **1. Saisie de l'Invite**

En bas de l'écran, il y a un champ de saisie étiqueté _"Entrez votre invite ici..."_. C'est là que les utilisateurs écrivent des instructions pour que l'opérateur suive.

À côté du champ de saisie se trouvent plusieurs boutons de contrôle :

* **Variables de l'Invite** – Ouvre une fenêtre contextuelle où vous pouvez saisir des paires clé-valeur utilisées dans l'invite. Les variables sont écrites entre accolades, comme `{numéro_de_facture}` ou `{url}`. Ces valeurs s'appliquent uniquement à l'invite actuelle dans le champ de saisie.
* **Enregistrer l'Invite** – Enregistre l'invite actuelle. Choisissez de l'enregistrer soit comme :
  * **Invite d'Organisation** – Modifiable au sein de votre organisation ; inclut à la fois l'invite et les valeurs de variables définies.
  * **Invite Globale** – Partagée entre tous les locataires ; inclut uniquement l'invite et les espaces réservés de variables (aucune valeur n'est enregistrée).
* **Effacer la Conversation** – Efface la conversation actuelle avec l'opérateur, mais laisse l'invite dans le champ de saisie inchangée. Utile lors de la réutilisation ou de l'amélioration d'une invite.

Pour des conseils détaillés sur la rédaction d'invites efficaces - y compris la syntaxe, les variables et les exemples - veuillez consulter le [**Guide de Rédaction des Invites**](prompt-writing-guide.md).

### **2. Navigation dans la Barre Latérale**

Utilisez l'icône en haut à gauche pour ouvrir ou fermer la barre latérale. La barre latérale affiche les invites enregistrées, organisées en deux catégories :

<div align="left"><img src="https://docs.docbits.com/~gitbook/image?url=https%3A%2F%2F578966019-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FT2n2w4uDCJvv7CJ5zrdk%252Fuploads%252Fm08uq4Kqj0SEZWSnlnoS%252Fimage.png%3Falt%3Dmedia%26token%3D4ba4542a-a707-4907-ae5e-b06286af8240&#x26;width=768&#x26;dpr=4&#x26;quality=100&#x26;sign=ef6b0706&#x26;sv=2" alt="" width="375"></div>

* **Invites d'Organisation**: Modifiables et réutilisables au sein de votre organisation.
* **Invites Globales**: Partagées entre tous les locataires. Elles ne peuvent pas stocker de variables et ne peuvent pas être modifiées ou supprimées.
  *   Une invite globale est toujours modifiable et supprimable par l'**organisation qui l'a créée**, où elle apparaît sous Invites d'Organisation.

      <div align="left"><img src="https://docs.docbits.com/~gitbook/image?url=https%3A%2F%2F578966019-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FT2n2w4uDCJvv7CJ5zrdk%252Fuploads%252FlVnXjwtnxAtqsftRvYUi%252Fimage.png%3Falt%3Dmedia%26token%3D60b3d0dd-3eee-40a8-b447-c9e91087a27d&#x26;width=768&#x26;dpr=4&#x26;quality=100&#x26;sign=f9b364a&#x26;sv=2" alt="" width="375"></div>
* **Fonctionnalité de Recherche:** une barre de recherche en haut de la barre latérale permet aux utilisateurs de trouver rapidement des invites enregistrées par nom ou mot-clé.
* **Référence des Icônes:** Chaque invite enregistrée a un ensemble d'icônes d'action
  * **Flèche** – Démarrer l'invite
  * **Stylo** – Modifier l'invite (disponible uniquement pour les invites de votre propre organisation)
  * **Poubelle** – Supprimer l'invite (disponible uniquement pour les invites de votre propre organisation)

### 3. Enregistrer l'Invite

En cliquant sur le bouton **Enregistrer l'Invite**, une fenêtre contextuelle s'ouvre où vous pouvez enregistrer l'invite actuelle pour une utilisation future.

<div align="left"><img src="https://docs.docbits.com/~gitbook/image?url=https%3A%2F%2F578966019-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FT2n2w4uDCJvv7CJ5zrdk%252Fuploads%252FgrBpDnbo80nPkozFhgCE%252Fimage.png%3Falt%3Dmedia%26token%3Dd31c06fc-dcd0-4fbe-9e1e-6c5bc001e4bb&#x26;width=768&#x26;dpr=4&#x26;quality=100&#x26;sign=900c948&#x26;sv=2" alt="" width="375"></div>

#### **Champs de la Fenêtre Contextuelle d'Enregistrement de l'Invite**

* **Nom de l'Invite:** Entrez un nom pour identifier l'invite.
* **Enregistrer l'Invite Publiquement (Case à cocher):** Lorsqu'elle est cochée, l'invite sera enregistrée en tant qu'**Invite Globale**. Les Invites Globales sont partagées entre tous les locataires et ne peuvent pas stocker de **valeurs** de variables (seulement des **noms** de variables).
* **Modifier les Variables:** Ouvre la [**Fenêtre Contextuelle des Variables d'Invite**](prompt-writing-guide.md) pour revoir ou ajuster les définitions des variables avant l'enregistrement.

**Actions**

* **Annuler:** Ferme la fenêtre contextuelle sans enregistrer.
* **Enregistrer:** Enregistre l'invite en utilisant le nom spécifié et le paramètre de visibilité.

### 4. Contrôles d'Exécution de l'Invite

Lorsqu'une invite est en cours d'exécution, les utilisateurs disposent de plusieurs options de contrôle pour gérer ou intervenir dans le processus d'exécution :

* **Mettre en Pause l'Invite:** Interrompt temporairement l'exécution actuelle. Utile si vous souhaitez observer l'état actuel ou préparer le système pour les prochaines étapes. ![](https://docs.docbits.com/~gitbook/image?url=https%3A%2F%2F578966019-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FT2n2w4uDCJvv7CJ5zrdk%252Fuploads%252FzG9U15jmVTb202efDR5l%252Fimage.png%3Falt%3Dmedia%26token%3Dee52f250-15d4-4139-b612-ba5ff1876841\&width=300\&dpr=4\&quality=100\&sign=329efe81\&sv=2)
* **Reprendre l'Invite:** Continue l'exécution à partir du point où elle a été mise en pause. ![](https://docs.docbits.com/~gitbook/image?url=https%3A%2F%2F578966019-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FT2n2w4uDCJvv7CJ5zrdk%252Fuploads%252FewGCZ9wSXt7VsvS8RjZH%252Fimage.png%3Falt%3Dmedia%26token%3D92ec27df-07b4-4e9f-a125-6f0a87d9db47\&width=300\&dpr=4\&quality=100\&sign=8e03589c\&sv=2)
* **Annuler l'Invite:** Arrête complètement l'exécution et réinitialise la session. Cela est utile si l'invite doit être interrompue ou redémarrée en raison d'un comportement incorrect ou de modifications dans les entrées.\
  ![](https://docs.docbits.com/~gitbook/image?url=https%3A%2F%2F578966019-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FT2n2w4uDCJvv7CJ5zrdk%252Fuploads%252FYUKk03iazolJlx6reOO3%252Fimage.png%3Falt%3Dmedia%26token%3Da722c82b-e4c1-4c23-8c56-a31f2685cce7\&width=300\&dpr=4\&quality=100\&sign=170c122e\&sv=2)
* **Prendre le Contrôle:** Permet à l'utilisateur d'intervenir manuellement en interagissant directement avec le système. Cela est utile si l'opérateur est bloqué ou interprète mal une étape. Prendre le contrôle met automatiquement en pause l'invite et passe en mode manuel jusqu'à ce que vous choisissiez de reprendre ou d'annuler.

### 5. Vue Détaillée de l'Opérateur

Une fois une invite démarrée, un bouton supplémentaire devient disponible permettant aux utilisateurs de passer à une **vue d'exécution détaillée**.\
![](https://docs.docbits.com/~gitbook/image?url=https%3A%2F%2F578966019-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FT2n2w4uDCJvv7CJ5zrdk%252Fuploads%252F9kObRWZFb3woomL045KL%252FDetailed%2520view%2520.jpg%3Falt%3Dmedia%26token%3Dbd0f94e2-84f2-4fd0-ae89-82408e85e03a\&width=300\&dpr=4\&quality=100\&sign=3aefc79\&sv=2)

* **Ouvrir la Vue Détaillée:** Ce bouton vous emmène vers une vue dédiée qui montre, étape par étape, ce que l'opérateur fait en temps réel.

Dans la vue détaillée, les utilisateurs peuvent :

* Surveiller chaque action effectuée (par exemple, clics, saisies, attentes).
* Voir quelle étape est actuellement active.
* Identifier où des problèmes surviennent si l'invite rencontre des problèmes.
* Utiliser les mêmes actions de **Pause**, **Reprise**, **Annulation** et **Prise de Contrôle**.
