# Configurer les notifications par courriel

Les notifications par courriel peuvent avertir des destinataires lorsqu'un document atteint un statut donné. Avant de créer une notification, vérifiez qu'un [modèle de courriel](../e-mail-templates.md) existe pour le type de document que vous souhaitez utiliser.

## Ouvrir la liste des notifications

Dans **Paramètres**, choisissez **COMMUNICATION ET NOTIFICATIONS → Notifications par e-mail pour le statut du document**. La liste affiche les règles existantes avec leur type de document, leur statut, leur priorité, leur délai, leur destinataire et leur dernière modification. Sélectionnez **Nouveau** pour créer une règle.

<figure><img src="../../../../.gitbook/assets/dbdc1166-notifications-list-fr-20261112.png" alt="Liste des notifications par e-mail dans les paramètres, avec le bouton Nouveau au-dessus du tableau des règles"><figcaption><p>Sélectionnez Nouveau pour configurer une notification par courriel.</p></figcaption></figure>

## Configurer une règle

La boîte de dialogue **Nouveau** contient les contrôles suivants :

| Contrôle | Que saisir |
| --- | --- |
| **Nom** | Un nom que vous reconnaîtrez dans la liste des notifications. Utilisez des lettres, des chiffres et des espaces. |
| **Type de document** | Le type de document auquel cette règle s'applique. Choisissez-le avant de sélectionner un modèle. |
| **Sous-organisation** | Limite la règle à une sous-organisation. Si vous n'en choisissez aucune, la liste affiche **Toutes les sous-organisations**. |
| **Sélectionner un modèle de courrier électronique** | Un modèle pour le type de document choisi. Le sélecteur n'est pas disponible tant que les modèles correspondants ne sont pas chargés. |
| **Statut du document** | Le statut du document qui déclenche la notification. |
| **Priorité** | La valeur de priorité de cette règle de notification. |
| **Unité de temps** et **Délai** | Le temps d'attente avant l'envoi. Pour les minutes, le délai doit être d'au moins cinq ; saisissez un nombre entier. |
| **Ne pas répéter / Répéter** | Activez **Répéter** si la notification doit être envoyée de nouveau tant que la condition reste remplie. |
| **Envoi d'un courrier électronique à l'utilisateur/groupe désigné** | Envoie l'avis au destinataire désigné sur le document au lieu d'une adresse fixe. Cela masque **Adresse email**. |
| **Adresse email** | Saisissez une adresse valide lorsque l'option du destinataire désigné est désactivée. |
| **Renvoyer la notification de réaffectation** | Envoie de nouveau l'avis si le document est affecté à une autre personne. |

<figure><img src="../../../../.gitbook/assets/dbdc1166-notifications-create-fr-20261112.png" alt="Boîte de dialogue Nouveau d'une notification par e-mail avec nom, type de document, sous-organisation, modèle de courrier, statut, priorité, unité de temps, délai, destinataire et le bouton Enregistrer"><figcaption><p>Choisissez un type de document et son modèle de courrier, puis définissez le déclencheur et le destinataire.</p></figcaption></figure>

Lorsque **Envoi d'un courrier électronique à l'utilisateur/groupe désigné** est sélectionné, le champ **Adresse email** disparaît. L'interrupteur de répétition change alors d'intitulé, de **Ne pas répéter** à **Répéter**.

<figure><img src="../../../../.gitbook/assets/dbdc1166-notifications-recipient-repeat-fr-20261112.png" alt="Boîte de dialogue de notification avec l'interrupteur Répéter activé et l'option Envoi d'un courrier électronique à l'utilisateur/groupe désigné cochée ; le nom Facture approuvee est une donnée d'exemple inventée"><figcaption><p>Utilisez l'option du destinataire désigné lorsque le titulaire du document doit recevoir le courriel. Le nom « Facture approuvee » est une donnée d'exemple inventée.</p></figcaption></figure>

Sélectionnez **Enregistrer** pour ajouter la règle à la liste, ou **Annuler** pour abandonner le brouillon. Si **Sélectionner un modèle de courrier électronique** ne propose aucun choix, créez d'abord un modèle pour le type de document sélectionné, puis revenez à cette boîte de dialogue.
