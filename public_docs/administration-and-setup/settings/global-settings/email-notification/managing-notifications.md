# Gestion des notifications

Ouvrez **Paramètres → Notifications par e-mail pour le statut du document** pour afficher les règles de votre organisation. Une règle relie un statut de document à un modèle d'e-mail et à un destinataire. L'exemple ci-dessous utilise une règle de démonstration pour les factures et reste **inactive** dans le bac à sable DocBits.

## Exemple : une facture est prête pour la validation

Avant de créer une règle, préparez un modèle d'e-mail pour **Invoice** sous **Paramètres → Modèles d'e-mails**. Dans cet exemple, le modèle s'appelle **Docs Demo Invoice Notification**. Le modèle fournit l'objet et le message de l'e-mail.

1. Sélectionnez **+ Nouveau** sur la page **Notifications par e-mail pour le statut du document**.
2. Saisissez **Docs Demo Invoice Validation** comme nom, sélectionnez **Invoice** comme type de document et choisissez le modèle d'e-mail préparé.
3. Choisissez **Ready for validation** comme statut et **Moyen** comme priorité. Définissez **Unité de temps** sur **MINUTES** et **Délai** sur **10**. Le délai minimum en minutes est de cinq.
4. Sélectionnez **Envoi d'un courrier électronique à l'utilisateur/groupe désigné**. Activez **Ne pas répéter** si le message ne doit être envoyé qu'une seule fois. Vérifiez le destinataire et le minutage, puis sélectionnez **Enregistrer**.

<figure><img src="../../../../.gitbook/assets/dbdc-641-example-form-fr-20261110.png" alt="Dialogue de modification d'une règle de notification : nom Docs Demo Invoice Validation, type de document Invoice, modèle Docs Demo Invoice Notification, statut Ready for validation, priorité Moyen, unité de temps MINUTES, délai 10 et envoi à l'utilisateur désigné activé"><figcaption><p>Une règle enregistrée, ouverte pour modification. Ses valeurs montrent quand et à qui la notification serait envoyée.</p></figcaption></figure>

La règle apparaît désormais dans la liste. Le menu **Actions** d'une règle inactive propose **Activer**. Vérifiez le nom, le type de document, le statut, le délai et le destinataire dans votre propre liste avant d'activer une règle.

<figure><img src="../../../../.gitbook/assets/dbdc-641-example-list-fr-20261110.png" alt="Liste des notifications par e-mail pour le statut du document avec les colonnes Nom, Type De Document, Sous-Organisation, Statut Du Document, Priorité, Délai, Envoyer Par E-Mail À, Dernière Modification Par, Dernière Modification En Date Du et Actions"><figcaption><p>La liste affiche vos règles enregistrées avec le type de document, le statut, la priorité, le délai et le destinataire.</p></figcaption></figure>

## Modifier, activer ou supprimer une règle

Ouvrez le menu **Actions** de la ligne. **Éditer** ouvre la règle et ses valeurs actuelles. **Activer** active cette règle inactive ; une règle active propose **Désactiver** à la place. **Journaux** ouvre l'historique de ses notifications. **Supprimer** supprime la règle après confirmation. Vérifiez les destinataires et le minutage avant d'activer ou de modifier une règle.

<figure><img src="../../../../.gitbook/assets/dbdc-641-example-actions-fr-20261110.png" alt="Menu Actions d'une règle inactive avec Éditer, Activer, Journaux et Supprimer"><figcaption><p>Les actions disponibles dépendent de l'état actif de la règle.</p></figcaption></figure>

Si la liste affiche **Aucun enregistrement trouvé !**, créez d'abord une règle. Si les listes **Type de document** ou de modèles d'e-mail sont vides, configurez un type de document actif et un modèle correspondant avant de revenir à ce formulaire.

Pour la configuration initiale, voir [Configurer les notifications par courriel](configuring-notifications.md). Si les e-mails n'arrivent pas comme prévu, voir [Dépannage](troubleshooting.md).
