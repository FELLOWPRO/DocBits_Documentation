# Cartes logiques : variables, conversions, JSON et déclencheurs

<figure><img src="../../../.gitbook/assets/workflow-card-qa-20261021-category-e019409102f9-fr.png" alt="Cartes de conversion et JSON dans la bibliothèque. Les cartes de variables d’organisation nécessitent Advanced Builder ; les modèles visibles dépendent aussi de la version. Certains libellés de cette version de la carte ont encore une traduction incomplète ou incorrecte dans l’interface. Les explications de cette page emploient les termes corrects."><figcaption><p>Cartes de conversion et JSON dans la bibliothèque. Les cartes de variables d’organisation nécessitent Advanced Builder ; les modèles visibles dépendent aussi de la version. Certains libellés de cette version de la carte ont encore une traduction incomplète ou incorrecte dans l’interface. Les explications de cette page emploient les termes corrects.</p></figcaption></figure>

Utilisez ces cartes dans Advanced Workflow Builder où la carte sélectionnée est disponible. La visibilité de la carte dépend de votre version et des modèles activés. Les références ci-dessous décrivent la version 2. Gardez à l'esprit la version stockée dans un flux de travail existant lorsque vous comparez ses champs avec ce guide.

## Choisissez le bon magasin de valeur

Une variable de workflow d'organisation sélectionnée dans le panneau Variables est partagée entre les workflows et est enregistrée indépendamment du canevas. Une balise nommée utilisée par les cartes de conversion, JSON et de comparaison de balises appartient au contexte d'exécution actuel. La création d'une balise ne crée pas de variable d'organisation. Entrez le nom de la balise sans préfixe de stockage interne. Un champ de document est une troisième source de données distincte.

Une variable d'organisation et une balise d'exécution restent distinctes même lorsque leurs noms correspondent. Sélectionnez un champ de variable compatible ou fournissez explicitement la valeur attendue par la carte réceptrice. Voir [Variables](../advanced-workflow/variables.md) pour la portée de l'organisation et la persistance immédiate.

## Actions variables de l'organisation

Créez d'abord la variable avec le type correct et sélectionnez-la sur la carte. Une référence de variable absente rapporte `MISSING_VARIABLE`. Les cartes qui définissent des variables enregistrent la valeur précédente et la nouvelle dans le journal de la carte. Évitez les données personnelles ou confidentielles réelles dans les valeurs de test et les journaux partagés.

| Carte | Entrée requise | Résultat et exemple | Échec ou cas limite |
| --- | --- | --- | --- |
| `ACTION_LOGIC_SET_TEXT_VAR` | Variable de texte et `value` | Stocke le texte ; par exemple, définissez une étiquette de routage sur `review`. | Une valeur manquante est différente d'une valeur de texte intentionnellement vide. |
| `ACTION_LOGIC_SET_NUMBER_VAR` | Variable de type Nombre et numérique `value` | Stocke un nombre fini ; par exemple, définissez un seuil sur `1000.50`. | Les textes numériques non valides, l'infini et NaN sont rejetés. Utilisez un point décimal, sans symbole monétaire. |
| `ACTION_LOGIC_CALC_NUMBER` | Variable numérique et `expression` | Stocke le résultat arithmétique ; `(100 + 20) / 2` donne `60`. | Prend en charge les littéraux numériques, les parenthèses, `+`, `-`, `*`, `/`, `%` et `**`. Les noms, appels de fonction et références de champs de document ne sont pas acceptés dans l'expression. Les expressions non valides ou la division par zéro échouent. |
| `ACTION_LOGIC_SET_BOOLEAN_VAR` | Variable Oui/Non et `value` | Définit l'indicateur sur Oui ou Non. | Utilisez la valeur booléenne proposée par la carte plutôt qu'un synonyme en texte libre traduit. |
| `ACTION_LOGIC_INVERT_BOOLEAN` | Variable oui/non | Inverse sa valeur actuelle ; Oui devient Non. | Initialisez la variable avant de vous appuyer sur un premier résultat particulier. |

### Action de référence de document

`ACTION_LOGIC_SET_DOCUMENT_VAR` stocke l'ID du document actuel dans une variable de document sélectionnée. Il nécessite un document à jour ; sans celui-ci, il rapporte `NO_DOCUMENT`. Un flux de travail déclenché reçoit l'ID du document, et non un objet document sérialisé. L'implémentation vérifiée n'a pas de modèle de carte d'interface utilisateur prédéfini pour cette action, ne vous attendez donc pas à ce qu'elle apparaisse dans chaque sélecteur de carte. Utilisez-le uniquement si votre administrateur confirme qu'un modèle correspondant est disponible ; la saisie d'un identifiant de document dans le formulaire de création de variable ne constitue pas un substitut.

## Balises et conversions de types

Ces actions utilisent des noms de balises dans le contexte d'exécution actuel. Produisez la balise d’entrée avant de la lire. Une balise d'entrée manquante ou un nom manquant signale `MISSING_VARIABLE` ; une conversion numérique non valide signale une erreur de configuration. Le résultat est une balise nouvelle ou écrasée, et non un champ de document extrait.

| Carte | Entrées | Résultat et exemple |
| --- | --- | --- |
| `ACTION_LOGIC_CREATE_TEXT_TAG` | `tag_name`, `value` | Crée une balise de texte ; `raw_amount` avec la valeur `125.50`. Une valeur de texte vide est autorisée. |
| `ACTION_LOGIC_CONVERT_TO_NUMBER` | `input_tag`, `output_tag` | Convertit `125.50` en nombre `125.5`. Un booléen devient `1` ou `0`. Un texte tel que `EUR 125,50` n'est pas une saisie numérique valide. |
| `ACTION_LOGIC_CONVERT_TO_TEXT` | `input_tag`, `output_tag` | Convertit la valeur stockée en texte. Il ne formate pas une devise ni ne localise les séparateurs décimaux. |
| `ACTION_LOGIC_CONVERT_TO_BOOLEAN` | `input_tag`, `output_tag` | Convertit directement un booléen existant ; un nombre différent de zéro devient vrai et zéro devient faux. Utilisez `true` ou `false` pour une saisie de texte prévisible et testez d'autres représentations acceptées. |

### Exemple de conversion

1. Créez la balise de texte `raw_amount` avec la valeur `125.50`.
2. Convertissez `raw_amount` en Nombre, en écrivant en `amount_number`.
3. Utilisez un nombre supérieur à avec `tag_name` défini sur `amount_number` et `value` défini sur `100`.
4. Vérifiez que la condition réussit pour `125.50`, échoue pour `100` et signale une erreur de conversion pour `EUR 125,50` à l'étape 2.

## Lire les valeurs de JSON

Les trois cartes lues prennent `json_text`, `json_path` et `output_tag`. Malgré son nom, `json_text` est le nom d'une balise contenant du JSON, pas une boîte permettant de coller un document JSON littéral. Produisez d'abord cette balise, par exemple avec Créer une balise de texte.

Les chemins sont des clés séparées par des points et des index de liste de base zéro : `invoice.lines.0.amount`. N'utilisez pas la syntaxe JSONPath telle que `$.invoice.lines[0].amount`. Si une clé est manquante, un index n'est pas valide ou JSON n'est pas valide, le résultat est `ERROR_CARD_SETUP` ; une balise source manquante signale `MISSING_VARIABLE`.

| Carte | Sortie |
| --- | --- |
| `ACTION_LOGIC_JSON_TO_NUMBER` | Valeur numérique ; le texte numérique est converti et un booléen devient `1` ou `0`. Un texte numérique non valide échoue. |
| `ACTION_LOGIC_JSON_TO_TEXT` | Représentation textuelle de la valeur sélectionnée. Ce n'est pas une promesse de sérialisation JSON pour les objets imbriqués. |
| `ACTION_LOGIC_JSON_TO_BOOLEAN` | Un booléen ; le texte `true`, `1` ou `yes` est vrai après la mise en minuscule, tandis que les autres textes sont faux. Les nombres suivent leur valeur zéro/non nulle. |

Pour une balise `payload` contenant le JSON suivant, la lecture de `invoice.lines.0.amount` dans `amount` avec JSON pour numéroter produit `125.5` :

```json
{"invoice":{"lines":[{"amount":"125.50"}],"approved":false}}
```

Testez également un chemin inexistant, un index hors plage et un JSON mal formé. Un échec de lecture ne doit pas être traité comme un zéro valide ou une approbation réussie.

## Mettre à jour JSON

Les quatre cartes d'écriture prennent `json_tag`, `json_path` et `value`. `json_tag` nomme une balise existante contenant du JSON. Ils mettent à jour cette balise avec du JSON sérialisé. La même syntaxe de chemin séparé par des points s'applique ; Des clés d'objet intermédiaires manquantes peuvent être créées, mais les index de liste doivent identifier les éléments existants. Ils n’étendent pas de liste et ne prennent pas en charge les chemins génériques.

| Carte | Valeur et effet |
| --- | --- |
| `ACTION_LOGIC_JSON_SET_NUMBER` | Une valeur numérique, telle que `125.5` ; stocke un numéro JSON. Un texte numérique non valide échoue. |
| `ACTION_LOGIC_JSON_SET_TEXT` | Texte, tel que `review` ; stocke une chaîne JSON. |
| `ACTION_LOGIC_JSON_SET_BOOLEAN` | Le texte `true`, `1` ou `yes` est défini sur vrai après la mise en minuscule ; un autre texte définit false. Préférez `true` et `false`. |
| `ACTION_LOGIC_JSON_SET_JSON` | JSON valide, tel que `{"status":"review"}` ; insère cette valeur analysée, pas son texte cité. JSON invalide échoue. |

Par exemple, définissez le chemin `invoice.approved` sur `true` dans `payload` avec JSON défini sur Boolean. Lisez ensuite le même chemin avec JSON vers Boolean et vérifiez vrai. Une balise source manquante, un JSON non valide ou un chemin non valide doivent être diagnostiqués dans le journal de la carte avant de continuer.

## Conditions

Les six conditions ci-dessous sont la version 2. Une condition fausse est un résultat commercial, et non une action réussie ou une erreur d'exécution. Dans une séquence de conditions de style standard, cela empêche les actions suivantes : dans un workflow avancé, connectez le résultat à la branche prévue.

| Carte | Champs | Évaluation et limite importante |
| --- | --- | --- |
| `CONDITION_LOGIC_VALUE_EQUALS` | `tag_name`, `value` | Compare exactement les représentations textuelles, y compris la casse. Ne l'utilisez pas comme contrôle de présence : un tag manquant n'est pas automatiquement signalé comme une erreur. |
| `CONDITION_LOGIC_BOOLEAN_IS` | `tag_name` | Vérifie si la balise est vraie. Une balise manquante est évaluée comme fausse. Utilisez un vrai booléen pour des résultats fiables. |
| `CONDITION_LOGIC_TEXT_CONTAINS` | `tag_name`, `value` | Recherche de sous-chaînes sensibles à la casse. Une balise manquante est traitée comme du texte vide. Une chaîne de recherche vide correspond ; définissez toujours la valeur de recherche délibérément. |
| `CONDITION_LOGIC_NUMBER_LESS` | `tag_name`, numérique `value` | Strictement moins que. Une balise manquante ou une valeur de comparaison omise est par défaut nulle ; des données numériques invalides sont une erreur de configuration. |
| `CONDITION_LOGIC_NUMBER_GREATER` | `tag_name`, numérique `value` | Strictement supérieur à. Une valeur égale au seuil ne satisfait pas à cette condition. Les mêmes valeurs par défaut de zéro et le même comportement d'erreur numérique s'appliquent. |
| `CONDITION_LOGIC_EXPRESSION` | `value1`, `operator`, `value2` | Prend en charge `==`, `!=`, `<`, `<=`, `>`, `>=`, `contains`, `not_contains`. Il essaie d'abord une comparaison numérique, puis compare le texte. Il ne s'agit pas d'un champ d'expression Python arbitraire. |

Pour un nombre supérieur à `100`, testez `99`, `100` et `101`. Pour le texte contient `ABC`, testez `ABC`, `abc` et une recherche vide. Vérifiez à la fois la branche et le journal ; un nœud gris a été ignoré et ne prouve aucune comparaison réussie.

## Déclencheurs

| Carte | Configuration | Quand ça correspond |
| --- | --- | --- |
| `CONDITION_LOGIC_VAR_CHANGED` | Sélectionnez une variable d'organisation. La référence stockée utilise son ID, donc renommer la variable ne modifie pas intentionnellement la cible. | Les valeurs de variable actuelles et précédentes fournies diffèrent. Répéter la même valeur n’est pas un changement. Une référence de variable manquante signale `MISSING_VARIABLE`. |
| `CONDITION_LOGIC_WEBHOOK_EVENT` | Facultatif `event_name`. | Une charge utile webhook est présente dans le contexte d’exécution du workflow. Avec un nom, la valeur `event` de la charge utile doit correspondre exactement ; sans nom, aucun événement webhook fourni correspond. Aucun événement ne signifie faux. |

La sélection d’un événement Webhook ne crée pas de point de terminaison de webhook public ni son authentification. Votre intégration doit fournir l'événement via un point d'entrée configuré. Testez l'événement correspondant, un autre événement et aucun événement. Pour un déclencheur de variable, testez un changement de valeur réelle et une valeur inchangée, et évitez une chaîne qui réécrit à plusieurs reprises la même variable partagée.

## Tester et diagnostiquer

Validez le graphique, testez chaque branche avec une entrée représentative et inspectez les [Workflow Logs](../workflow-logs.md). Incluez les balises manquantes, les JSON non valides, les types de variables incorrects, les limites numériques et les fausses conditions. Un test sans document ne peut pas prouver une action dépendante du document. Revérifiez la version de la carte enregistrée et l'état activé avant de vous fier à l'exécution automatique.

<!-- workflow-card-logic-examples-20261021 -->

## Exemples concrets pour chaque carte logique

Il s'agit d'entrées illustratives et de résultats attendus pour la version 2. Utilisez des cartes de variable d'organisation uniquement lorsque Advanced Builder expose ses modèles.

| Carte | Exemple de configuration | Résultat attendu et contre-exemple |
| --- | --- | --- |
| `ACTION_LOGIC_SET_TEXT_VAR` | Définissez la variable de texte d'organisation `routing_label` sur `review`. | La variable partagée contient `review`. Un workflow ultérieur peut lire la même variable d'organisation. |
| `ACTION_LOGIC_SET_NUMBER_VAR` | Définissez la variable numérique `approval_limit` sur `1000.50`. | Il stocke le numérique `1000.5`. Le texte `EUR 1000,50` n'est pas une saisie numérique valide. |
| `ACTION_LOGIC_CALC_NUMBER` | Stockez l'expression `(100 + 20) / 2` dans la variable numérique `calculated_limit`. | Le résultat est `60`. Un nom de champ de document ou une division par zéro ne constituent pas un substitut valide. |
| `ACTION_LOGIC_SET_BOOLEAN_VAR` | Définissez la variable Oui/Non `review_required` sur le booléen proposé `true`. | Le drapeau de l'organisation est vrai. Utilisez Boolean `false` dans un cas séparé pour l'effacer. |
| `ACTION_LOGIC_INVERT_BOOLEAN` | Commencez par la variable d'organisation `demo_flag` égale à `true`. | Une exécution donne `false`. L'exécution à nouveau donne `true`, donc une exécution répétée n'est pas idempotente. |
| `ACTION_LOGIC_CREATE_TEXT_TAG` | Créez la balise d'exécution `raw_amount` avec le texte `125.50`. | La balise contient ce texte dans cette exécution ; il ne s'agit pas d'une nouvelle variable d'organisation ou d'un nouveau champ de document. |
| `ACTION_LOGIC_CONVERT_TO_NUMBER` | Convertissez la balise d'entrée `raw_amount`, contenant `125.50`, en balise de sortie `amount_number`. | La sortie est numérique `125.5`. `EUR 125,50` produit une erreur de conversion. |
| `ACTION_LOGIC_CONVERT_TO_TEXT` | Convertissez la balise numérique `amount_number` contenant `125.5` en `amount_text`. | La sortie est le texte `125.5` ; il n'est pas localisé sous forme de montant en devise. |
| `ACTION_LOGIC_CONVERT_TO_BOOLEAN` | Convertissez une balise d'entrée numérique contenant `1` en balise de sortie `has_value`. | La sortie est vraie. Le numérique `0` produit faux. |
| `ACTION_LOGIC_JSON_TO_NUMBER` | Créez la balise source `payload` avec `{"invoice":{"amount":"125.50"}}` ; lire le chemin `invoice.amount` vers `amount_number`. | La sortie est numérique `125.5`. Un chemin absent est une erreur et non un zéro valide. |
| `ACTION_LOGIC_JSON_TO_TEXT` | Utilisez la balise source `payload` contenant `{"invoice":{"status":"review"}}` et le chemin `invoice.status`. | La balise de sortie contient le texte `review`. |
| `ACTION_LOGIC_JSON_TO_BOOLEAN` | Utilisez la balise source `payload` contenant `{"invoice":{"approved":false}}` et le chemin `invoice.approved`. | La sortie est booléenne fausse. Un chemin manquant n'est pas la même chose qu'un chemin faux stocké. |
| `ACTION_LOGIC_JSON_SET_NUMBER` | Utilisez la balise JSON existante `payload` contenant `{"invoice":{}}` ; réglez `invoice.total` sur `125.5`. | La balise contient un total numérique JSON, et non une chaîne numérique entre guillemets. |
| `ACTION_LOGIC_JSON_SET_TEXT` | Utilisez la balise JSON existante `payload` contenant `{"invoice":{}}` ; réglez `invoice.status` sur `review`. | La valeur JSON stockée est une chaîne : `{"invoice":{"status":"review"}}`. |
| `ACTION_LOGIC_JSON_SET_BOOLEAN` | Utilisez la balise JSON existante `payload` contenant `{"invoice":{}}` ; définissez `invoice.approved` avec le texte `true`. | La valeur JSON stockée est booléenne vraie. Utilisez `false` pour l'effacer. |
| `ACTION_LOGIC_JSON_SET_JSON` | Utilisez la balise JSON existante `payload` contenant `{"invoice":{}}` ; définissez `invoice.metadata` sur un JSON `{"source":"demo"}` valide. | La valeur insérée est un objet. Un JSON invalide doit être signalé et non stocké en tant que mise à jour d'objet réussie. |
| `CONDITION_LOGIC_VALUE_EQUALS` | Créez la balise `route` avec le texte `review` et comparez-la avec `review`. | Ça passe. La comparaison avec `Review` échoue car la comparaison est sensible à la casse. |
| `CONDITION_LOGIC_BOOLEAN_IS` | Utilisez la balise `review_required` contenant le vrai booléen `true`. | Cela passe ; false ou une balise manquante n'établit pas un résultat vrai. |
| `CONDITION_LOGIC_TEXT_CONTAINS` | Utilisez la balise `note` avec le texte `manual review` et recherchez `review`. | Ça passe. La recherche de `REVIEW` majuscule échoue. Une chaîne de recherche vide correspond et doit être évitée sauf intentionnellement. |
| `CONDITION_LOGIC_NUMBER_LESS` | Utilisez la balise numérique `amount` égale à `50` et la valeur de comparaison `100`. | Ça passe. Une valeur de `100` échoue à la comparaison stricte inférieure à. |
| `CONDITION_LOGIC_NUMBER_GREATER` | Utilisez la balise numérique `amount` égale à `125` et la valeur de comparaison `100`. | Ça passe. `100` échoue à la comparaison stricte supérieure à. |
| `CONDITION_LOGIC_EXPRESSION` | Sélectionnez valeur1 `120`, opérateur `>` et valeur2 `100`. | La comparaison numérique réussit. Utilisez `80` comme valeur1 pour une fausse branche ; ce n'est pas une expression Python de forme libre. |
| `CONDITION_LOGIC_VAR_CHANGED` | Sélectionnez une variable d'organisation dont la valeur précédente est `new` et la valeur actuelle fournie est `review`. | L'événement à valeur modifiée correspond. Répéter `review` comme valeur précédente et actuelle ne correspond pas. |
| `CONDITION_LOGIC_WEBHOOK_EVENT` | Sélectionnez le nom de l'événement `invoice.ready` et fournissez un événement d'intégration configuré avec la charge utile `{"event":"invoice.ready"}`. | Cela correspond. `{"event":"invoice.updated"}` et aucun événement ne correspondent. La carte ne crée pas de point de terminaison webhook. |

L'action facultative de référence de document `ACTION_LOGIC_SET_DOCUMENT_VAR` n'a pas de modèle prédéfini dans la source vérifiée. Si votre administrateur fournit un modèle pris en charge, sélectionnez une variable de document et exécutez-le avec un document de démonstration actuel : il stocke cet ID de document. Sans document, il rapporte `NO_DOCUMENT`. Ne la traitez pas comme une carte disponible simplement parce que l'implémentation existe.
