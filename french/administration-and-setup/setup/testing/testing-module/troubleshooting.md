# Dépannage

## Je ne trouve pas Testing dans les paramètres

La page n'est affichée qu'aux administrateurs de l'organisation. Adressez-vous à un administrateur de votre organisation.

## La page indique que Testing est désactivé

Un administrateur de l'organisation doit activer **Activer Testing pour l'organisation** en haut de la page.
Tant que ce n'est pas fait, rien ne s'exécute, pas même depuis un assistant IA ou depuis l'extérieur.

## Mon exécution a échoué

Ouvrez le journal dans l'onglet **Journaux** et regardez la première étape en échec ainsi que son code d'erreur :

| Ce que vous voyez | Signification habituelle | Que faire |
|---|---|---|
| Un élément est introuvable ou n'est pas visible | La page est différente dans votre organisation, ou se charge lentement | Ouvrez vous-même la page et vérifiez-la ; adaptez votre propre modèle, ou vérifiez les valeurs de l'entrée |
| Un champ ou un statut ne correspond pas | Le document a une autre valeur que celle attendue par l'entrée | Vérifiez le document ; corrigez la valeur attendue dans l'entrée |
| La page n'a pas pu être ouverte | ID de document incorrect, ou autorisation manquante | Vérifiez l'ID dans l'entrée et les autorisations de l'utilisateur qui a démarré l'onglet |
| Délai d'attente dépassé | L'étape ou l'ensemble du test a pris trop de temps | Relancez ; si le problème se répète, vérifiez les performances de la page |
| Bloqué par l'environnement | Le test écrit des données dans un environnement client | Confirmez le démarrage, ou exécutez-le dans un environnement de test |

## Mon exécution est « Bloqué »

L'exécution n'a pas pu être évaluée : certaines étapes ont été ignorées (par exemple une étape de capture d'écran, que le navigateur ne peut pas réaliser)
ou une confirmation est manquante. Une exécution bloquée n'est jamais comptée comme réussie. Supprimez l'étape de votre propre modèle, ou
redémarrez l'exécution avec la confirmation.

## « Enregistrez une session de navigateur pour démarrer » / aucun onglet n'accepte les démarrages

Les démarrages depuis un assistant IA ou depuis l'extérieur nécessitent un onglet de navigateur dans lequel **Autoriser les démarrages de l'extérieur** est activé. Ouvrez
l'onglet Entrées dans un onglet qui reste ouvert, activez cette option et utilisez son ID de session. Un rechargement met fin à l'enregistrement.

## L'exécution s'est arrêtée ou affiche Annulé / Non transmissible

L'onglet qui exécutait le test a été rechargé, fermé ou a perdu sa connexion, ou aucun onglet n'a répondu à temps. Gardez l'onglet ouvert
et au premier plan jusqu'à la fin de l'exécution, puis relancez. Un test comportant une étape **Recharger la page** se termine aussi de cette manière si la page ne revient pas en deux minutes environ
(voir [Rechargement et reprise](reload-and-resume.md)).

## « Les modèles Playwright ne peuvent pas encore être démarrés ici »

Les modèles dont l'**Exécuteur** est **Playwright** sont exécutés par votre automatisation de tests. Vous pouvez enregistrer des entrées pour eux, mais vous ne
pouvez pas les démarrer depuis cette page.

## Je ne peux pas supprimer un modèle

Seuls les modèles propres à votre organisation (**personnalisé**) peuvent être supprimés. Les modèles intégrés et par défaut ne le peuvent pas ; utilisez
**Modifier une copie** pour obtenir votre propre version.
