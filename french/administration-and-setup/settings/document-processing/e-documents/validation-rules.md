# Validation des factures électroniques

{% embed url="https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/einvoice-validation/v1/fr.mp4" %}

La page **Validation des factures électroniques** (**Paramètres → Documents électroniques → Validation des factures électroniques**, chemin `/settings/einvoice-validation` ; anciennement appelée *Règles de validation*) contrôle la manière dont DocBits valide les factures électroniques entrantes. Elle repose sur l'ensemble de règles officiel **KoSIT XRechnung + ZUGFeRD** ainsi que sur les codes de résultat internes du validateur, et vous permet de remplacer la gravité de chaque règle pour votre organisation.

> Cette page concerne les **factures électroniques** (XRechnung, ZUGFeRD, Factur-X). Elle ne doit pas être confondue avec les **règles de validation des données**, qui contrôlent les champs extraits des documents.

## Ce que contient cette page

<figure><img src="../../../../.gitbook/assets/einvoice-validation-settings-fr.png" alt="La page Validation des factures électroniques avec le tableau Validation pour chaque type de document"><figcaption><p>La page Validation des factures électroniques. L'onglet <strong>Règles et politique</strong> commence par le tableau <strong>Validation pour chaque type de document</strong>. Exemple d'organisation.</p></figcaption></figure>

| Sujet | Ce que cela permet | Qui |
| --- | --- | --- |
| [Configuration de la validation et versions acceptées](validation-setup.md) | L'assistant de configuration, les versions XRechnung acceptées, les profils acceptés et la signification de chaque gravité. | Administrateurs de l'organisation |
| [Gravité des règles](validation-rule-severities.md) | Le tableau des règles : modifiez la gravité de chaque règle pour votre organisation. | Administrateurs de l'organisation |
| [Validation pour chaque type de document](validation-per-document-type.md) | Activer la validation (**Activé**) et décider si un contrôle échoué arrête le document (**Blocage**). Chaque modification demande une confirmation. | Administrateurs de l'organisation |
| [Journal des modifications](validation-change-log.md) | Chaque modification des paramètres : quand, qui, quelle règle, de → à. | Administrateurs de l'organisation |
| [L'écran d'erreur d'une facture électronique rejetée](validation-error-screen.md) | Ce que vous voyez lorsque vous importez un XML erroné : l'explication, la ligne défectueuse et l'étape suivante. | Toutes les personnes qui traitent les factures |
| [Rapport de validation](validation-report.md) | Ce que voit un utilisateur lorsqu'une facture échoue : les résultats en langage clair. Il s'ouvre depuis le document, pas depuis cette page. | Toutes les personnes qui traitent les factures |
| [Étape suivante et rejet d'un document](validation-next-step-and-reject.md) | Que faire après la lecture du rapport, téléchargement du rapport et **Rejeter le document**. | Toutes les personnes qui traitent les factures |
