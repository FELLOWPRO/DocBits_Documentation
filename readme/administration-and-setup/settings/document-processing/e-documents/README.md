# Documents électroniques

DocBits valide les factures électroniques entrantes (e-invoices) au regard des normes officielles — **XRechnung**, **ZUGFeRD** et **Factur-X** — et achemine les problèmes détectés vers le bon responsable. Le groupe de paramètres **Documents électroniques** (sous **Traitement des documents**) comporte deux pages :

* **[Règles de validation](validation-rules.md)** — choisissez les versions et profils de facture électronique que vous acceptez et définissez la gravité de chaque règle de validation pour votre organisation.
* **[Routage des notifications](notification-routing.md)** — associez les résultats de validation à l'agent AI Workforce qui doit les traiter.

Ensemble, elles vous permettent de décider **ce qui constitue un problème** sur une facture électronique entrante et **qui s'en charge**.

## Activer ou désactiver la validation des factures électroniques

Les deux pages Documents électroniques ne prennent effet qu'une fois la **validation des factures électroniques activée pour le type de document**. L'interrupteur se trouve sur le type de document lui-même, et non dans le menu Documents électroniques.

Accédez à **Paramètres → Types de document → Facture → Paramètres avancés** et ouvrez la section **Validation des factures électroniques**.

<figure><img src="../../../../.gitbook/assets/edoc_enable_validation_toggle.png" alt="Les interrupteurs de validation des factures électroniques sur le type de document Facture"><figcaption><p>Activez ou désactivez la validation des factures électroniques par type de document, avec notification facultative du fournisseur</p></figcaption></figure>

* **Valider les factures électroniques entrantes** — l'interrupteur principal. Lorsqu'il est **activé**, chaque facture téléversée est vérifiée selon les règles Schematron KoSIT XRechnung ainsi que les contrôles sémantiques L0 (PDF/A-3) et L4 (IBAN/TVA), avec les gravités que vous avez définies sur la page [Règles de validation](validation-rules.md). Les factures non valides sont bloquées. Lorsqu'il est **désactivé**, les factures ignorent entièrement la validation des factures électroniques et les pages Règles de validation et Routage des notifications n'ont aucun effet.
* **Notifier le fournisseur en cas de rejet** — apparaît une fois la validation activée. Lorsqu'il est **activé**, une facture rejetée déclenche un e-mail au fournisseur répertoriant les champs manquants ou incorrects afin qu'il puisse la réémettre. Qui reçoit et traite chaque résultat se configure sur la page [Routage des notifications](notification-routing.md).

> La validation des factures électroniques se configure **par type de document**. Elle s'applique aujourd'hui au type de document **Facture** ; activez-la sur chaque type de document à valider.
