# E-mails entrants

### Aperçu

DocBits peut récupérer les documents directement depuis l'e-mail, sans téléversement manuel. Il existe **deux façons** d'importer des documents par e-mail, toutes deux dans **Paramètres → Traitement des documents → Importer** :

| Méthode | Fonctionnement | Idéal pour |
|---------|----------------|------------|
| **Compte d'import e-mail** | DocBits se connecte à une boîte aux lettres qui vous appartient (**IMAP**, **OAuth Office365** ou **OAuth Office365 – Tenant**) et importe les documents qu'il y trouve. | Une boîte dédiée qui reçoit déjà vos documents (p. ex. `factures@votreentreprise.com`). |
| **E-mails transférés (E-mails entrants)** | DocBits vous fournit une adresse unique ; tout expéditeur autorisé peut y **transférer** des documents. | Le transfert ponctuel depuis de nombreux expéditeurs sans partager les identifiants de la boîte. |

Vous pouvez utiliser chaque méthode séparément ou les deux ensemble.

### Méthode 1 — Connecter une boîte aux lettres (Import e-mail)

Allez dans **Paramètres → Traitement des documents → Importer** et ouvrez la section **Import e-mail**. Cliquez sur **Nouveau** pour ajouter une connexion de boîte aux lettres.

<figure><img src="../../../../.gitbook/assets/inbound_emails_email_import_entry.png" alt="Section Import e-mail avec le bouton Nouveau"><figcaption><p>Dans la section Import e-mail, cliquez sur <strong>Nouveau</strong> pour connecter une boîte aux lettres.</p></figcaption></figure>

L'assistant de configuration s'ouvre. Le premier champ, **Protocole**, détermine comment DocBits se connecte — choisissez **IMAP**, **OAuth Office365** ou **OAuth Office365 – Tenant**.

<figure><img src="../../../../.gitbook/assets/inbound_emails_protocol_select.png" alt="Liste déroulante Protocole avec IMAP, OAuth Office365 et OAuth Office365 - Tenant"><figcaption><p>La liste <strong>Protocole</strong> propose les trois types de connexion.</p></figcaption></figure>

#### IMAP

Pour une boîte standard, choisissez **IMAP** et renseignez les détails du serveur et les identifiants du compte :

* **Nom du serveur** et **Port** (par défaut `993`) de votre serveur de messagerie.
* **Chiffrement** — `SSL`, `TLS` ou `None`.
* **Nom d'utilisateur**, **e-mail** et **mot de passe** de la boîte.

<figure><img src="../../../../.gitbook/assets/inbound_emails_imap.png" alt="Formulaire de connexion IMAP avec serveur, port, chiffrement et identifiants"><figcaption><p>Le formulaire IMAP : la connexion au serveur de messagerie plus les identifiants de la boîte.</p></figcaption></figure>

#### OAuth Office365

Pour une boîte aux lettres d'un seul utilisateur Microsoft 365, choisissez **OAuth Office365**. Au lieu d'un mot de passe, vous autorisez DocBits via Microsoft : choisissez la cible du **Routage des documents**, puis cliquez sur **Authentifier** et terminez la connexion Microsoft.

<figure><img src="../../../../.gitbook/assets/inbound_emails_o365.png" alt="Formulaire OAuth Office365 avec Routage des documents et un bouton Authentifier"><figcaption><p>OAuth Office365 se connecte via la connexion Microsoft — aucun mot de passe n'est stocké dans DocBits.</p></figcaption></figure>

#### OAuth Office365 – Tenant

Pour vous connecter au niveau du locataire (organisation) via une inscription d'application Azure, choisissez **OAuth Office365 – Tenant** et saisissez les identifiants Azure : **ID de locataire** (Tenant ID), **ID d'application cliente** (Client App ID) et **Valeur d'application cliente** (secret client). Utilisez **Tester la connexion** pour vérifier, puis **Enregistrer**.

<figure><img src="../../../../.gitbook/assets/inbound_emails_o365_tenant.png" alt="Configuration du locataire Azure avec ID de locataire, ID d'application cliente et Valeur d'application cliente"><figcaption><p>OAuth Office365 – Tenant utilise une inscription d'application Azure (ID de locataire, ID d'application cliente, secret client).</p></figcaption></figure>

{% hint style="info" %}
Le **Routage des documents** décide où vont les documents importés — **DocBits** (le tableau de bord standard) ou **AI Workforce**. Après la connexion, les étapes suivantes de l'assistant vous permettent de choisir le **dossier** depuis lequel importer, une **boîte partagée** facultative, et si les e-mails traités doivent être **déplacés** vers un autre dossier.
{% endhint %}

### Méthode 2 — Transférer des e-mails vers DocBits (E-mails entrants)

Cette méthode nécessite d'abord l'activation du module **E-mails entrants**. Allez dans **Paramètres → Traitement des documents → Module**, ouvrez la section **Type de document**, repérez **E-mails entrants** et activez le commutateur.

<figure><img src="../../../../.gitbook/assets/inbound_emails_1.png" alt="Activation du module E-mails entrants"><figcaption><p>Activez <strong>E-mails entrants</strong> dans Paramètres → Traitement des documents → Module.</p></figcaption></figure>

Une fois activé, une section **E-mails entrants** apparaît dans **Paramètres → Traitement des documents → Importer**. Elle contient tout le nécessaire pour recevoir des documents transférés :

<figure><img src="../../../../.gitbook/assets/inbound_emails_forward.png" alt="Section E-mails entrants : adresse d'import, expéditeurs prédéfinis et adresse de notification d'échec"><figcaption><p>La section E-mails entrants : votre adresse d'import, la liste des expéditeurs prédéfinis et l'adresse de notification d'échec.</p></figcaption></figure>

* **Adresse d'import** — une adresse unique générée par le système, au format `org_id@environment.inbound.docbits.com`. Transférez ou envoyez des documents à cette adresse et DocBits les importe automatiquement. Utilisez l'icône de copie pour la récupérer.
* **Importer les documents uniquement depuis des e-mails prédéfinis** — lorsqu'elle est activée, seules les adresses d'expéditeur listées ici sont acceptées ; les e-mails de tout autre expéditeur sont ignorés. Pour chaque expéditeur, vous pouvez choisir une **Sous-organisation** (laissez vide pour l'affecter à l'organisation principale). Utilisez **Ajouter** pour lister d'autres expéditeurs et **Supprimer** pour en retirer un.
* **Répondre à cet e-mail si l'import ne peut pas être effectué** — lorsqu'elle est activée, saisissez une adresse à notifier à chaque échec d'une tentative d'import, afin que les problèmes ne passent pas inaperçus.

Cliquez sur **Enregistrer** pour appliquer vos modifications.

{% hint style="info" %}
**Quelles pièces jointes sont importées ?** DocBits importe les pièces jointes de documents prises en charge — consultez [Importer → Import e-mail](../import/README.md#email-import) pour la liste complète des types de fichiers — et décompresse les messages `.eml` transférés pour importer les documents qu'ils contiennent. La détection repose également sur le **contenu réel du fichier**, de sorte que les pièces jointes qu'un serveur de messagerie de transfert ré-étiquette avec un type générique (`application/octet-stream`) sont tout de même importées correctement. Les images en ligne (logos de signature / graphiques intégrés) sont ignorées.
{% endhint %}

### Quelle méthode choisir

* **Utilisez un compte d'import e-mail** lorsque les documents arrivent déjà dans une boîte dédiée et que vous voulez que DocBits les récupère de lui-même — IMAP pour les serveurs de messagerie génériques, OAuth Office365 pour Microsoft 365.
* **Utilisez les e-mails transférés** lorsque des personnes doivent transférer des documents à la demande, ou lorsque vous ne voulez pas partager les identifiants de la boîte avec DocBits.
* **Combinez les deux** si certains documents arrivent dans une boîte fixe tandis que d'autres sont transférés ponctuellement.

{% hint style="info" %}
Restreindre les expéditeurs (Méthode 2) et choisir la bonne cible de **Routage des documents** (Méthode 1) sont les deux moyens les plus courants de garder un flux entrant propre — uniquement les documents attendus, dirigés là où vous le souhaitez.
{% endhint %}
