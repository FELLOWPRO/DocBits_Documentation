# Validation des factures électroniques

{% embed url="https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/einvoice-validation/v1/fr.mp4" %}

La page **Validation des factures électroniques** (**Settings → E-Documents → E-Invoice Validation**, chemin `/settings/einvoice-validation` ; anciennement nommée _Validation Rules_) détermine comment DocBits valide les factures électroniques entrantes. Elle s'appuie sur le jeu de règles officiel **KoSIT XRechnung + ZUGFeRD** et sur les codes de constat internes du validateur, et permet de surcharger la gravité de chaque règle pour votre organisation.

> Cette page concerne les **factures électroniques** (XRechnung, ZUGFeRD, Factur-X). Elle n'est pas identique à **Data Validation Rules**, qui contrôlent les champs extraits des documents.

## Contenu de cette page

<figure><img src="../../../../../.gitbook/assets/einvoice-validation-settings-fr-20261104.png" alt="Validation et blocage par type de document. Les noms configurés sont masqués. Exemple de l'environnement de développement."><figcaption><p>Validation et blocage par type de document. Les noms configurés sont masqués. Exemple de l'environnement de développement.</p></figcaption></figure>

| Sujet | Ce qu'il fait | Pour qui |
| ----------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------- |
| [Configuration de la validation et versions acceptées](validation-setup.md) | L'assistant de configuration, les versions de XRechnung acceptées, les profils acceptés et ce que signifie chaque gravité. | Administrateurs de l'organisation |
| [Gravité des règles](validation-rule-severities.md) | Le tableau des règles : modifier la gravité de chaque règle pour votre organisation. | Administrateurs de l'organisation |
| [Validation par type de document](validation-per-document-type.md) | Activer la validation (**Enabled**) et décider si un contrôle en échec bloque le document (**Blocking**). Chaque changement demande une confirmation. | Administrateurs de l'organisation |
| [Journal des modifications](validation-change-log.md) | Chaque changement des paramètres : quand, qui, quelle règle, de → à. | Administrateurs de l'organisation |
| [L'écran d'erreur d'une facture électronique rejetée](validation-error-screen.md) | Ce que vous voyez quand vous téléversez un XML incorrect : l'explication, la ligne fautive et l'étape suivante. | Toutes les personnes qui traitent des factures |
| [Rapport de validation](validation-report.md) | Ce qu'un utilisateur voit quand une facture échoue : les constats en langage clair. Il s'ouvre depuis le document, pas depuis cette page. | Toutes les personnes qui traitent des factures |
| [Étape suivante et rejet d'un document](validation-next-step-and-reject.md) | Que faire après avoir lu le rapport, les téléchargements du rapport et **Reject document**. | Toutes les personnes qui traitent des factures |
