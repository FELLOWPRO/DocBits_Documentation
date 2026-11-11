# Importation

## Aperçu

Vous avez besoin d'un compte administrateur pour créer une connexion. Utilisez **Import** pour configurer l'importation automatique de documents depuis un serveur FTP/SFTP, une boîte aux lettres connectée ou l'adresse e-mail entrante DocBits. Vérifiez l'organisation et l'environnement actuels avant de saisir les détails de connexion.

<figure><img src="../../../../.gitbook/assets/import-settings-overview-fr-20261109.png" alt="Page des paramètres d'importation avec le schéma Import Pipeline, la liste FTP Import avec un bouton New et la liste Email Import avec un bouton New"><figcaption><p>La page Import : le schéma Import Pipeline en lecture seule, la liste FTP Import et la liste Email Import, chacune avec son propre bouton <strong>New</strong>.</p></figcaption></figure>

## Comment y accéder

1. Accédez à **Settings** → **Document Processing** → **Import**.
2. Développez la section requise. **FTP Import** et **Email Import** disposent chacune de son propre bouton **New**.

## **Document Settings**

La page Import actuelle contient **Import Pipeline**, **FTP Import**, **Email Import** et, lorsqu'il est activé, **Inbound Emails**. Le découpage des pages, les conditions de paiement par défaut et les champs de format de date ne sont pas des contrôles dans cette vue Import.

**Import Pipeline** affiche la topologie de routage FTP/SFTP, y compris les régions source et cible. Vérifiez tout avertissement affiché avant de modifier une connexion. L'onglet **Email** du pipeline affiche actuellement un message annonçant une disponibilité prochaine ; il n'affiche pas de schéma de traitement des e-mails.

## **FTP Import**

<figure><img src="../../../../.gitbook/assets/dbdc-179-ftp-overview-en-20261030.png" alt="Tableau FTP Import avec le bouton New et des colonnes pour le type, le serveur, le nom d'utilisateur, le port, la sous-organisation et le répertoire"><figcaption><p>Utilisez New dans FTP Import pour ajouter une connexion serveur. Les lignes de connexion existantes sont masquées dans cet exemple.</p></figcaption></figure>

### Conditions requises

* Un serveur FTP, FTPS ou SFTP accessible par le service d'importation.
* L'adresse du serveur, le protocole, le port, le nom d'utilisateur et le mot de passe fournis par votre administrateur.
* Un répertoire d'importation et, si un archivage est requis, un répertoire d'archive approuvé.

### Ajouter une nouvelle connexion

1. Cliquez sur **New** dans **FTP Import**.
2. Saisissez les paramètres de connexion. Un nouveau formulaire démarre avec **SFTP** et le port **22** ; remplacez ces valeurs lorsque votre serveur utilise un autre protocole ou un autre port.

<figure><img src="../../../../.gitbook/assets/dbdc-179-ftp-blank-form-en-20261030.png" alt="Formulaire de nouvelle connexion FTP affichant SFTP, le port 22, les champs de répertoire, les paramètres de nouvelle tentative ainsi que Save et Cancel"><figcaption><p>Saisissez les détails du serveur et de connexion, puis vérifiez les répertoires, le routage et les paramètres de nouvelle tentative. Les champs mot de passe et clé API sont masqués ; cet exemple n'a pas été enregistré.</p></figcaption></figure>

* **Type**, **Server name**, **Port**, **Username** et **Password** identifient et authentifient la connexion au serveur.
* **Primary Directory** définit le répertoire de base. **Import Directory** sélectionne le dossier à traiter ; la sélection du dossier devient disponible une fois la connexion enregistrée.
* **Document Type** et **Sub-Organizations** contrôlent l'affectation. **File name matching patterns** limite les noms de fichiers pris en compte.
* **Archive after Import** permet de déplacer les fichiers traités vers le répertoire d'archive indiqué. **Include Subfolder Files** étend le traitement aux sous-dossiers.
* **Retry interval (min)**, **Retry duration (hours)** et **Notification emails (comma-separated)** contrôlent le comportement des nouvelles tentatives et des notifications. Les valeurs par défaut illustrées sont 60 minutes et 48 heures.
* **API Key** utilise la clé d'abonnement d'application existante de l'organisation. L'icône en forme d'œil affiche ou masque cette clé ; l'icône de copie la copie dans le presse-papiers. Ces contrôles ne créent pas de nouvelle clé. Gardez-la confidentielle ; ne l'incluez pas dans les captures d'écran ou les messages au support.

Utilisez **Cancel** ou l'icône de fermeture pour quitter un formulaire de nouvelle connexion sans l'enregistrer.

3. Vérifiez les valeurs et cliquez sur **Save** lorsque la connexion est prête à être créée.
4. Dans le menu **Actions** de la ligne enregistrée, choisissez **Activate** lorsque les importations sont autorisées à s'exécuter.

### Actions pour FTP

Le menu **Actions** de la connexion enregistrée propose :

* **Test Connection** : contacter le serveur configuré pour vérifier la connexion.
* **Connection Logs** : consulter les tentatives de connexion et les erreurs.
* **Activate/Deactivate** : activer ou arrêter le traitement automatique pour cette connexion.
* **Edit** : modifier sa configuration.
* **Delete** : supprimer la connexion.

Le test, l'activation, la modification et la suppression affectent une connexion réelle. Vérifiez la ligne et l'organisation sélectionnées avant de les utiliser.

## **Email Import**

Une boîte aux lettres connectée est distincte de l'adresse e-mail entrante DocBits décrite dans le tutoriel ci-dessous. Choisissez la méthode adaptée à votre processus.

<figure><img src="../../../../.gitbook/assets/dbdc-179-email-overview-en-20261030.png" alt="Tableau Email Import avec New, l'icône du journal d'importation et les colonnes de configuration de la boîte aux lettres"><figcaption><p>Utilisez New pour une connexion de boîte aux lettres ou l'icône de journal pour consulter les importations. Les lignes de connexion existantes et le lien d'information sont masqués.</p></figcaption></figure>

<mark style="color:red;">**Note**</mark>: Seuls les documents des types de fichiers suivants seront importés :

* `.pdf`
* `.tiff` / `.tif`
* `.eml`
* `.dat`
* `.xml`
* `.edi`
* `.purchaseorder`

{% hint style="info" %}
**Comment les pièces jointes sont reconnues**

Outre les extensions de fichiers listées ci-dessus, DocBits identifie également un document par son **contenu réel** (signature de fichier), et pas uniquement par le type de contenu déclaré par le système de messagerie expéditeur. Cela compte pour les messages **transférés** : les serveurs de messagerie ou passerelles intermédiaires réétiquettent fréquemment une pièce jointe avec un type générique (`application/octet-stream`) au lieu, par exemple, de `application/pdf` ou `application/xml`. DocBits reconnaît et importe néanmoins correctement ces pièces jointes.

* Les messages **`.eml` transférés** et les pièces jointes Outlook **`winmail.dat`** (TNEF) sont décompressés et les documents qu'ils contiennent sont importés.
* **Encodage XML:** lorsqu'une facture XML est réétiquetée avec un type générique (`application/octet-stream`), DocBits la reconnaît grâce à sa déclaration `<?xml`, en tolérant une marque d'ordre des octets (BOM) **UTF-8** ou **UTF-16** (LE/BE) placée en tête — actuellement, seuls ces encodages BOM sont détectés automatiquement à partir du contenu. Une pièce jointe qui conserve un nom de fichier `.xml` est importée quel que soit son encodage.
* **Ignorées:** les images intégrées qui accompagnent un message (logos de signature / graphiques incorporés — PNG, JPG, GIF, BMP) sont ignorées silencieusement et ne sont **pas** comptées comme des importations échouées.

Si une pièce jointe ne peut pas être importée et que l'option **“Reply to this email if import can not be done”** est activée pour l'adresse entrante, l'adresse de réponse configurée est notifiée.
{% endhint %}

### Ajouter une nouvelle connexion IMAP

1. Cliquez sur **New** dans **Email Import** et sélectionnez **IMAP** sous **Protocol**.
2. Dans **Email Server Setup**, saisissez le nom du serveur, le port, le chiffrement, le nom d'utilisateur, l'adresse e-mail et le mot de passe. Utilisez les valeurs requises par votre fournisseur de messagerie ; le 993 affiché est un exemple de port, et non un paramètre complété.

<figure><img src="../../../../.gitbook/assets/dbdc-179-email-imap-step1-en-20261030.png" alt="Email Server Setup IMAP avec protocole, serveur, port, chiffrement, identifiants de compte et Next"><figcaption><p>Complétez les champs serveur et compte requis avant Next. La zone du mot de passe est masquée ; aucun identifiant de boîte aux lettres n'a été soumis dans cet exemple.</p></figcaption></figure>

L'icône de copie à côté de **Password** copie le mot de passe saisi dans le presse-papiers. **Cancel** ou l'icône de fermeture quitte cet assistant de nouvelle connexion sans l'enregistrer.

3. Cliquez sur **Next** pour ouvrir **Options**. Choisissez si vous souhaitez **Merge attached documents** ou **Block duplicate filename import**. **Email Notification** active un e-mail de confirmation après l'importation ; activez-le uniquement lorsque ce comportement est souhaité.

<figure><img src="../../../../.gitbook/assets/dbdc-179-email-imap-options-en-20261030.png" alt="Étape Options IMAP affichant la fusion des pièces jointes, le filtrage des noms de fichiers en double, la notification par e-mail, Back et Next"><figcaption><p>Options sépare le comportement d'importation de la notification par e-mail. Les deux cases à cocher et l'interrupteur de notification sont désactivés dans cet exemple non enregistré.</p></figcaption></figure>

4. Cliquez sur **Next** pour ouvrir **Config**. Sélectionnez les **Sub-Organizations** requises, vérifiez la **API Key** existante, définissez le destinataire des erreurs d'importation et vérifiez **Document Routing**. Développez **Advanced Settings** uniquement lorsque le processus nécessite des options supplémentaires.

<figure><img src="../../../../.gitbook/assets/dbdc-179-email-imap-config-en-20261030.png" alt="Étape Config IMAP avec organisation, clé API masquée, notifications d'erreur, routage des documents, Advanced Settings et Save"><figcaption><p>Config réunit l'affectation à l'organisation, la clé existante, les notifications d'erreur et le routage. La clé est masquée et Save n'a pas été utilisé.</p></figcaption></figure>

Dans **Config**, l'icône en forme d'œil affiche ou masque la **API Key** existante, et **Copy** la copie dans le presse-papiers. Aucun de ces deux contrôles ne génère de nouvelle clé.

5. Cliquez sur **Save** lorsque la configuration est prête. Utilisez ensuite **Activate** dans le menu **Actions** de la connexion enregistrée pour démarrer le traitement automatique.

Pour une connexion IMAP enregistrée, **Edit** propose des options de dossier et de traitement après importation. Sélectionnez le dossier source et le dossier de destination des e-mails déplacés uniquement après la création de la connexion et lorsque les dossiers disponibles peuvent être chargés.

### Actions pour IMAP

Le menu **Actions** de la connexion enregistrée propose **Test Connection**, **Connection Logs**, **Import Log**, **Activate/Deactivate**, **Edit** et **Delete**. Le test de connexion contacte la boîte aux lettres configurée ; l'activation active le traitement. Consultez les journaux avant de réessayer une importation échouée.

### Ajouter une nouvelle connexion OAuth Office365

1. Cliquez sur **New** dans **Email Import** et sélectionnez **OAuth Office365** sous **Protocol**. Pour une application de locataire gérée par un administrateur, sélectionnez **OAuth Office365 - Tenant** et suivez [O365 Tenant](o365-tenant.md).
2. Vérifiez **Document Routing** avant l'authentification.

<figure><img src="../../../../.gitbook/assets/dbdc-179-email-oauth-before-authentication-en-20261030.png" alt="Configuration OAuth Office365 affichant Document Routing et le bouton Authenticate avant l'authentification Microsoft"><figcaption><p>Sélectionnez la route avant Authenticate. Cette vue précède la connexion ; aucune authentification Microsoft n'a été démarrée.</p></figcaption></figure>

3. Cliquez sur **Authenticate** lorsque la connexion à la boîte aux lettres est autorisée. Effectuez la connexion par code d'appareil Microsoft avec le code affiché par DocBits, puis revenez et sélectionnez **Finish Authentication**.
4. Après l'authentification, vérifiez les options d'organisation, de dossier, de boîte aux lettres partagée, de dossier de déplacement et de notification d'erreur proposées pour la connexion. Utilisez **Next** pour continuer vers **Config** lorsqu'elle devient disponible, puis enregistrez les paramètres souhaités.
5. Activez la connexion enregistrée lorsque des importations automatiques doivent s'exécuter. **Import**, lorsqu'il est proposé pour une connexion enregistrée, démarre une importation réelle ; utilisez-le délibérément.

### Actions pour OAuth Office365

Le menu **Actions** de la connexion enregistrée propose **Connection Logs**, **Import Log**, **Activate/Deactivate**, **Edit** et **Delete**. La désactivation arrête le traitement automatique ; la suppression retire la configuration.

### Import Log

Utilisez l'icône de journal en haut à droite de **Email Import** pour consulter les importations de l'ensemble des connexions de boîte aux lettres configurées. Utilisez l'action **Import Log** d'une ligne enregistrée pour cette connexion. Vérifiez l'objet, l'expéditeur, le statut et les détails d'erreur disponibles avant de décider de réessayer.

## Inbound Emails

Les deux captures d'écran du tutoriel ci-dessous montrent l'adresse DocBits entrante et ses journaux. Cela est distinct des connexions de boîte aux lettres présentées ci-dessus.

* Utilisez l'icône de copie à côté de **E-Mail** pour copier l'adresse de réception affichée pour l'organisation et l'environnement actuels.
* **Add** insère une autre ligne d'expéditeur autorisé dans le formulaire. Choisissez son expéditeur et la sous-organisation souhaitée, puis utilisez **Save** pour enregistrer la configuration. L'ajout d'une ligne seule ne l'enregistre pas.
* **Logs** ouvre le journal des e-mails entrants. **Errors** filtre les erreurs ; **Inbound** et **Outbound** sélectionnent le sens des messages.
* Développez une ligne de journal avec son chevron pour inspecter les détails de la pièce jointe. L'icône de copie à côté de l'ID de trace copie cet ID pour le dépannage. **Original email**, lorsqu'il est disponible pour une ligne entrante, télécharge le message d'origine sélectionné sous forme de fichier `.eml` ; il ne relance pas l'importation.

## Tutoriel vidéo : Boîte de réception et recherche d'erreurs

{% embed url="https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/email-import-admin/v2/fr.mp4" %}
Boîte de réception et recherche d'erreurs
{% endembed %}

[Regarder avec sous-titres et navigation par chapitres](https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/email-import-admin/v2/fr.html)

Certains libellés natifs du produit peuvent rester dans une autre langue. Les identifiants techniques des champs sont conservés.

Sous les paramètres et l'importation, j'utilise l'adresse DocBits entrante dans cet exemple. Une boîte aux lettres directement connectée est une méthode d'importation distincte. Pour cette formation, je travaille dans une organisation de démonstration dédiée avec des factures synthétiques. Les notifications restent désactivées.

Je vérifie d'abord l'adresse de réception affichée et le périmètre. L'adresse appartient exactement à cette organisation et à son environnement. Pour une autre entreprise ou un environnement de production, j'utilise toujours l'adresse qui y est réellement affichée.

Ici, je limite la boîte de réception à notre expéditeur de test approuvé. Je ne sélectionne l'affectation à une sous-organisation que si elle relève du processus prévu. J'enregistre le paramètre et je le rouvre. L'expéditeur autorisé a été conservé ; les e-mails de réponse automatique restent désactivés dans cette formation.

<figure><img src="../../../../.gitbook/assets/admin-save-en-accounting-email-v1.png" alt="Expéditeur autorisé enregistré avec notifications désactivées"><figcaption><p>Expéditeur autorisé enregistré avec notifications désactivées</p></figcaption></figure>

Pour cette formation, un message de test a été soumis directement au traitement des e-mails entrants de DocBits. Ce test ne confirme pas une livraison d'e-mail externe. Dans le journal, je vérifie l'objet, l'expéditeur et la pièce jointe importée correspondants. Je contrôle ensuite le document réellement créé.

J'ouvre le document correspondant et je compare la pièce jointe PDF avec la facture dans DocBits. Le nom du fichier, le numéro de facture, le fournisseur et le montant doivent correspondre. Une importation réussie ne dit rien sur une approbation ou une écriture ERP.

Un deuxième test contrôlé provient d'un expéditeur non approuvé. Dans le journal, je recherche spécifiquement cet e-mail entrant et j'active le filtre d'erreur. Les détails nomment l'expéditeur rejeté. Je vérifie la cause à l'aide de l'objet et de l'ID de trace, au lieu de déclencher l'importation plusieurs fois.

Dans un cas réel, je clarifie d'abord si cet expéditeur est même autorisé. Une modification approuvée de la liste des expéditeurs est enregistrée puis vérifiée à nouveau. Ensuite, je contrôle un nouvel e-mail entrant de test unique jusqu'au document créé. Pour les erreurs techniques, je transmets l'ID de trace et le message d'erreur concret.

<figure><img src="../../../../.gitbook/assets/admin-error-en-accounting-email-v1.png" alt="Importation échouée avec pièce jointe, motif et trace"><figcaption><p>Importation échouée avec pièce jointe, motif et trace</p></figcaption></figure>
