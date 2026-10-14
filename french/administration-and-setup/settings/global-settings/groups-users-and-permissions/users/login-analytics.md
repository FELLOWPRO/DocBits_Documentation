# Statistiques de connexion

Les **Statistiques de connexion** offrent aux administrateurs une vue en lecture seule, à l'échelle de toute l'organisation, indiquant *quand* et *à quelle fréquence* les utilisateurs se connectent à DocBits. Elles répondent à des questions telles que « les connexions sont-elles en hausse ? », « combien d'utilisateurs distincts ont été actifs ce mois-ci ? » et « quand surviennent les pics d'utilisation ? » — sans jamais exposer les identifiants ni les données personnelles d'un utilisateur en particulier.

> **Accès :** ouvrez **Paramètres → Organisation et accès → Utilisateurs** et cliquez sur le bouton **Statistiques de connexion** dans le coin supérieur droit (`/settings/login-analytics`).

<figure><img src="../../../../../.gitbook/assets/login_analytics_overview.png" alt="Login Analytics page with the activity chart and summary cards"><figcaption><p>Activité de connexion de l'organisation sur la période sélectionnée</p></figcaption></figure>

## Plage de temps

Choisissez la période à analyser à l'aide du sélecteur situé en haut à droite : **7D**, **30D**, **90D**, **180D**, **Année** ou **Personnalisé** pour une plage de dates libre. Tous les éléments de la page — le graphique et les cartes de synthèse — sont recalculés en fonction de la période choisie.

La bannière **Informations sur les données** rappelle la fenêtre exacte affichée (par ex. *Affichage des données du 19.05.2026 au 18.06.2026*), de sorte que l'on sait toujours clairement à quelles dates correspondent les chiffres.

## Graphique d'activité de connexion

Le graphique trace deux séries sur la période sélectionnée :

| Série | Signification |
|--------|-------------|
| **Connexions totales** | Le nombre de connexions par jour, y compris les connexions répétées d'une même personne. |
| **Utilisateurs uniques** | Le nombre d'utilisateurs *distincts* qui se sont connectés ce jour-là. |

Survolez n'importe quel point pour lire la valeur exacte de ce jour. Les pics révèlent vos journées les plus chargées ; une courbe **Utilisateurs uniques** plate sous une courbe **Connexions totales** en dents de scie signifie que quelques personnes se sont connectées de nombreuses fois.

## Cartes de synthèse

Sous le graphique, trois cartes résument l'ensemble de la période sélectionnée :

| Carte | Signification |
|------|-------------|
| **Connexions totales** | Toutes les connexions sur la période. |
| **Utilisateurs uniques** | Les utilisateurs distincts qui se sont connectés au moins une fois. |
| **Moy./jour** | Le nombre moyen de connexions par jour sur la période. |

## Confidentialité

Les Statistiques de connexion ne présentent que des chiffres **agrégés** — des décomptes et des tendances pour l'organisation dans son ensemble. Elles ne répertorient ni les utilisateurs individuels, ni les adresses e-mail, ni les adresses IP. Pour consulter ou modifier le compte d'une personne en particulier, utilisez plutôt la page [Utilisateurs](README.md).
