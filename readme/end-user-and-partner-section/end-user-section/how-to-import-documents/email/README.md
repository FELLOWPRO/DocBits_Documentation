---
hidden: true
noIndex: true
---

# E-mail

DocBits peut importer des documents depuis la messagerie de deux façons. Les deux se configurent dans **Paramètres → Import** (Traitement des documents).

## Méthode 1 — Import par e-mail (connecter une boîte aux lettres)

Connectez un compte de messagerie et DocBits importe automatiquement les documents dès l'arrivée de nouveaux e-mails. Sur la page Import, ouvrez la section **Import par e-mail** et cliquez sur **+ Nouveau**.

<figure><img src="../../../../.gitbook/assets/email_import_section.png" alt="Section Import par e-mail"><figcaption>Import par e-mail — connecter une boîte aux lettres pour l'import automatique de documents</figcaption></figure>

Choisissez ensuite le protocole de votre boîte aux lettres :

* **IMAP** — voir [IMAP](imap.md)
* **OAuth (Office 365)** — voir [OAuth Office365](oauth-office365.md)

## Méthode 2 — E-mails entrants (transférer vers DocBits)

Transférez — ou envoyez directement — les e-mails à l'adresse de réception unique de votre organisation et DocBits importe automatiquement les pièces jointes. Aucune connexion de boîte aux lettres n'est nécessaire. Ouvrez la section **E-mails entrants** sur la page Import.

<figure><img src="../../../../.gitbook/assets/inbound_emails_section.png" alt="Section E-mails entrants"><figcaption>E-mails entrants — transférez vos documents vers votre adresse DocBits</figcaption></figure>

* **Info / E-mail** — l'adresse de réception unique de votre organisation (format `<org-id>@inbound.docbits.com`). Transférez vos documents à cette adresse ; utilisez l'icône de copie pour la copier.
* **Importer les documents uniquement depuis des e-mails prédéfinis** — lorsqu'elle est activée, seuls les e-mails des expéditeurs ajoutés à la liste blanche sont importés ; les e-mails de tout autre expéditeur sont ignorés.
* **Répondre à cet e-mail si l'import est impossible** — envoie une réponse automatique à l'expéditeur lorsque l'import échoue.
* **Notifier l'expéditeur en cas d'échec de l'import** — informe l'expéditeur si son e-mail n'a pas pu être importé.
* **Journaux** — ouvre le journal de traitement des e-mails entrants. Cliquez sur **Enregistrer** pour appliquer vos modifications.
