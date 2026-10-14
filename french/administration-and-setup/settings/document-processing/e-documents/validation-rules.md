# Règles de validation

<figure><img src="../../../../.gitbook/assets/edoc_validation_rules_setup.png" alt="Configuration de validation et versions acceptées"><figcaption><p>Configuration de validation et versions XRechnung acceptées</p></figcaption></figure>

La page **Règles de validation** (**Documents électroniques → Règles**) contrôle la manière dont DocBits valide les factures électroniques entrantes. Elle repose sur l'ensemble de règles officiel **KoSIT XRechnung + ZUGFeRD** ainsi que sur les codes de résultat internes du validateur, et vous permet de remplacer la gravité de chaque règle pour votre organisation.

## Configuration de la validation

La carte **Configuration de la validation** affiche votre profil de validation actuel (par exemple *B2G — Public Sector Receiver*). Cliquez sur **Modifier les réponses** pour relancer l'assistant de configuration et changer la norme par rapport à laquelle vous validez.

## Versions XRechnung acceptées

La porte **Versions XRechnung acceptées** répertorie chaque version de XRechnung. Cochez les versions que vous acceptez : les documents dont le CustomizationID est en dehors de cette liste sont rejetés avec `VAL-VERSION-NOT-ALLOWED` avant toute autre vérification. Une liste vide signifie « tout accepter ». Chaque version est étiquetée **current**, **deprecated** ou **EOL** avec sa date de publication.

## Profils acceptés et modèle de gravité

<figure><img src="../../../../.gitbook/assets/edoc_validation_rules_severity.png" alt="Profils acceptés et légende des gravités"><figcaption><p>Profils acceptés et signification de chaque gravité</p></figcaption></figure>

Choisissez les **profils** que vous acceptez (BASIC WL, BASIC, EN 16931 / COMFORT, EXTENDED, XRECHNUNG (CIUS)) à l'aide de **Tout accepter** / **Effacer**, puis **Enregistrer**.

Chaque règle de validation a une **gravité** qui détermine ce qui se passe lorsqu'elle se déclenche :

| Gravité | Effet |
|---------|-------|
| **FATAL** | Arrête immédiatement le traitement. Aucune couche suivante n'est vérifiée ; le document passe en Erreur. |
| **ERROR** | Le document est rejeté. Les autres résultats du même document sont tout de même affichés ; la notification au fournisseur (si activée) se déclenche. |
| **WARNING** | Apparaît dans le rapport de validation, mais le document poursuit normalement le flux. |
| **INFO** | Journal d'audit uniquement. Aucun effet visible pour l'utilisateur ni rejet. |

## Remplacer la gravité des règles

<figure><img src="../../../../.gitbook/assets/edoc_validation_rules_table.png" alt="Le tableau des règles de validation"><figcaption><p>Le tableau complet des règles avec remplacement de gravité par règle</p></figcaption></figure>

Le tableau des règles répertorie toutes les règles de validation (plus de 1 600 au total). Filtrez par **Couche (Layer)**, **Profil** ou **Version**, ou recherchez par code ou champ. Pour chaque règle, vous pouvez remplacer la **Gravité** dans le menu déroulant afin de l'adapter à la politique de votre organisation — par exemple, rétrograder une règle de `ERROR` à `WARNING` pour qu'elle ne rejette plus le document.
