# Gravité des règles

> Dans cette version, certains textes de l’interface peuvent encore être en anglais ou mal traduits. Le guide explique leur sens ; les captures montrent l’interface sans modification.

Chaque règle de validation a une gravité. Vous pouvez modifier la gravité de chaque règle pour votre organisation. Cette page fait partie de [Validation des factures électroniques](./). Seuls les administrateurs de l'organisation peuvent modifier les gravités.

<figure><img src="../../../../../.gitbook/assets/einvoice-rule-table-fr.png" alt="Tableau des règles avec les libellés réels de l’interface. Dans cette version, certains textes de l’interface peuvent encore être en anglais ou mal traduits. Le guide explique leur sens ; les captures montrent l’interface sans modification."><figcaption><p>Tableau des règles avec les libellés réels de l’interface. Dans cette version, certains textes de l’interface peuvent encore être en anglais ou mal traduits. Le guide explique leur sens ; les captures montrent l’interface sans modification.</p></figcaption></figure>

Le tableau des règles répertorie toutes les règles de validation (plus de 1 600 au total). Filtrez par **Layer**, **Profile** ou **Version**, ou recherchez par code ou champ. Pour chaque règle, vous pouvez remplacer la **Severity** dans le menu déroulant afin de l'adapter à la politique de votre organisation — par exemple, rétrograder une règle de `ERROR` à `WARNING` pour qu'elle ne rejette plus le document.

La signification de **FATAL**, **ERROR**, **WARNING** et **INFO** est expliquée sur [Configuration de la validation et versions acceptées](validation-setup.md#profils-acceptes-et-modele-de-gravite). Une gravité modifiée apparaît aussi dans le [rapport de validation](validation-report.md) dans la colonne **Your organisation**.
