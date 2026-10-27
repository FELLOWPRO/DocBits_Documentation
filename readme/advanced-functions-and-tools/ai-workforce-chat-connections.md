# Connecter AI Workforce à Teams et Discord

Vous devez disposer d'un abonnement AI Workforce actif, des droits de gestion des connexions et de l'accès au tenant Teams ou serveur Discord prévu. Résolvez d'abord toute exigence d'abonnement affichée avec votre administrateur.

## Microsoft Teams

1. Ouvrez **AI Workforce → Paramètres → Intégrations**.
2. Choisissez **+ → Connecter Teams**. DocBits génère un code et affiche sa durée de validité restante.
3. Suivez l'instruction associée au code dans le bon environnement Teams. Gardez-le confidentiel et terminez l'association avant expiration.
4. Attendez la confirmation. Vérifiez le nom et le mode de bot partagé ou personnalisé dans la liste.
5. Activez une connexion inactive si elle doit recevoir du travail. Enregistrée et active sont des états différents.
6. Envoyez une demande de test sans conséquence depuis le contexte Teams prévu. Vérifiez mission, source et organisation dans DocBits ainsi que les approbations humaines nécessaires dans la boîte de réception.

Pour un bot géré par votre entreprise, choisissez l'option personnalisée puis saisissez nom, identifiant du tenant, identifiant et secret de l'application. Les secrets restent dans le formulaire d'identifiants, jamais dans les instructions ou captures.

## Discord

1. Sous **Intégrations → +**, choisissez la connexion Discord.
2. Si proposé, ajoutez le bot au bon serveur avec un administrateur autorisé.
3. Saisissez un nom explicite et le bon **Guild ID**. Il identifie le serveur, pas le canal.
4. Créez la connexion, vérifiez l'entrée et activez-la si nécessaire.
5. Envoyez un test sans conséquence puis vérifiez mission, source et organisation obtenues.

## Diagnostiquer

Si le code Teams expire, générez-en un nouveau et suivez sa nouvelle instruction. Si aucun travail n'arrive, vérifiez activation, tenant/serveur, accès du bot et erreurs. Une connexion établie ne prouve pas une mission terminée.

Voir [AI Workforce](ai_workforce/README.md) pour missions, droits et approbations. Les connexions de discussion sont distinctes de l'importation par courriel et de la connexion Microsoft.
