# Appeler l’API DocBits

<figure><img src="../../../../.gitbook/assets/workflow-card-qa-20261021-card-6a1c780ee588-fr.png" alt="Champs de la carte dans la version affichée. Les champs ne sont pas encore renseignés. Certains libellés de cette version de la carte ont encore une traduction incomplète ou incorrecte dans l’interface. Les explications de cette page emploient les termes corrects." width="563"><figcaption><p>Champs de la carte dans la version affichée. Les champs ne sont pas encore renseignés. Certains libellés de cette version de la carte ont encore une traduction incomplète ou incorrecte dans l’interface. Les explications de cette page emploient les termes corrects.</p></figcaption></figure>

<!-- workflow-card-api-guide-contract-20261022 -->

Carte observée : `call_api`, modèle `6ca5e621-af72-4f55-aa2e-b3caa288722a`, version `1`. Utilisez la version réellement proposée dans votre organisation.

## Objectif

Utilisez `call_api` pour appeler un point de terminaison de l’API DocBits configurée. Le chemin relatif est ajouté à son adresse de base. Une URL externe arbitraire ne configure pas une intégration avec une autre API.

## Configuration

Renseignez le chemin, la méthode HTTP, les paramètres de requête et les données acceptées par le point de terminaison. La requête utilise le contexte de l’utilisateur DocBits courant. Les valeurs absentes de `org_id` et `triggered_by_docflow` sont ajoutées automatiquement. Les objets de paramètres et de données, ou leur représentation textuelle prise en charge, doivent respecter le format de cette version. Elle ne propose pas de correspondance générale des champs d’une réponse JSON.

## Résultat et limites

Le texte de réponse est converti en booléen : `true`, `1`, `yes` ou `on` seuls donnent vrai ; une réponse non reconnue, y compris un objet JSON arbitraire, donne faux par défaut. Le statut HTTP ne détermine pas à lui seul ce booléen. Un délai dépassé ou une erreur de requête donne faux. Le test de carte simule l’appel et renvoie vrai sans envoyer la requête ; il ne démontre ni authentification, ni connectivité, ni comportement du point de terminaison.



## Exemple pratique

Utilisez cette carte après les conditions nécessaires pour obtenir un booléen d’un point de terminaison configuré de l’API DocBits. Pour un test isolé, choisissez un point existant, documenté et en lecture seule, avec le contrat de réponse booléen voulu et la méthode adaptée, par exemple `GET`. Utilisez uniquement ses paramètres de démonstration pris en charge.

Résultat attendu et contre-exemple : une réponse HTTP `200` hypothétique dont le texte intégral est `true` donne vrai ; `false` donne faux. Un objet tel que `{"approved": true}` n’est pas automatiquement converti en vrai. Vérifiez séparément la réponse réelle et les journaux. Exemple vérifié dans le code d’exécution ; aucun appel ni workflow n’a été exécuté.

## Dépannage

La carte de requête HTTPS utilise une URL HTTPS configurée et ses propres en-têtes. `call_api` utilise un chemin relatif de l’API DocBits et le contexte de l’utilisateur courant ; son résultat vient du texte de réponse. Choisissez selon le point de terminaison et le contrat de réponse, non selon une distinction entre API simple et complexe.

[Référence](call-api.md)
