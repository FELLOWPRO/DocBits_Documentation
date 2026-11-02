# Création d'un point de terminaison ION API pour les exportations DocBits

Un administrateur Infor configure le point de terminaison API Gateway pour **l'environnement et l'organisation DocBits concernés**. Les anciennes images de cette page montraient un unique tenant Infor historique, un exemple figé `api.docbits.com` et un ancien formulaire d'exportation DocBits. Utilisez l'URL de destination, la clé d'API et le document OpenAPI approuvés pour votre environnement réel. Aucun tenant Infor n'a été connecté et aucun point de terminaison n'a été enregistré pour cette mise à jour.

## Avant de commencer

Rassemblez auprès de votre administrateur d'intégration l'URL de l'API DocBits de destination, la clé d'API approuvée et le nom de son en-tête, l'URL OpenAPI, ainsi que les environnements Infor et DocBits prévus. Gardez les clés et les fichiers `.ionapi` hors des tickets, des captures d'écran et du dépôt Git. Vérifiez qu'un point de terminaison de test ne peut pas router vers la production.

## Configurer Infor API Gateway

1. Dans **Available APIs**, créez une suite d'API de type **Custom or Non-Infor** pour l'environnement de destination. Consultez les [instructions d'Infor sur les suites d'API](https://docs.infor.com/inforos/2025.x/en-us/useradminlib_cloud/apigatewayag_cloud/gyy1489512842881.html).
2. Ajoutez à la suite un point de terminaison avec l'**URL de point de terminaison cible** approuvée. Sélectionnez le type d'authentification exigé par ce point de terminaison. Pour **API Key**, Infor demande un **Nom de la clé** et une **Valeur de la clé** ; utilisez le nom défini par le contrat de l'API DocBits et la clé émise pour cette organisation. Consultez les [champs du point de terminaison](https://docs.infor.com/inforos/2024.x/en-us/useradminlib_cloud/apigatewayag_cloud/bmg1489588707659.html) d'Infor. Ne copiez pas une clé d'un autre environnement.
3. Ajoutez l'URL OpenAPI/Swagger de l'environnement dans les paramètres **Documentation** du point de terminaison, en suivant les [instructions d'Infor sur la documentation](https://docs.infor.com/inforos/2025.x/en-us/useradminlib_cloud/apigatewayag_cloud/tzr1489597424134.html). Vérifiez que le point de terminaison apparaît dans les [métadonnées d'API](https://docs.infor.com/inforos/2025.x/en-us/useradminlib_cloud/apigatewayag_cloud/tdr1489674063627.html).
4. Avec l'administrateur Infor, vérifiez l'URL de destination, l'authentification, le chemin du proxy et un appel sûr hors production avant d'utiliser le point de terminaison dans un flux de documents ION. Enregistrer une suite d'API ne prouve pas à lui seul qu'un document a été livré.

## Configurer l'exportation dans DocBits

Dans l'organisation DocBits prévue, ouvrez **Paramètres → Exporter** et sélectionnez **Nouveau**. Les données des configurations existantes sont masquées dans l'image.

<figure><img src="../../.gitbook/assets/dbdc-40-export-list-fr-20261030.png" alt="Liste d&#x27;exportation actuelle en français avec Nouveau, l&#x27;avis d&#x27;exécution séquentielle et les en-têtes du tableau ; les données des configurations sont masquées."><figcaption><p>Nouveau ouvre une configuration non enregistrée. Les données des configurations existantes sont masquées dans cette capture native actuelle.</p></figcaption></figure>

Renseignez **Titre de la configuration**, choisissez **Type de document** et, si nécessaire, **Sous-organisation**. Dans **Exporter**, choisissez la valeur affichée **Informations** correspondant à Infor, puis **Infor IDM + ION BOD** dans **Type d'information**. L'exemple utilise **Facture**.

Dans **Type de déploiement**, choisissez le déploiement cloud ou sur site adapté à votre environnement. Le formulaire présente **Fichier API ION** (`.ionapi`, obligatoire), **Fichier de mappage IDM** (`.properties`) et **Fichier de cartographie de la BOD** (`.properties`). Demandez à l'administrateur les fichiers propres au tenant. Le titre, la sous-organisation et les trois zones d'envoi sont vides dans l'image. Dans ce formulaire, les zones portant le libellé **Cliquez pour télécharger** servent à choisir les fichiers locaux à charger.

<figure><img src="../../.gitbook/assets/dbdc-40-export-ion-bod-fr-20261030.png" alt="Formulaire actuel en français Infor IDM + ION BOD avec Facture, les choix de déploiement et trois zones d&#x27;envoi de fichiers vides."><figcaption><p>Formulaire natif actuel Infor IDM + ION BOD : Facture et le déploiement cloud sont sélectionnés ; le titre, la sous-organisation et les trois zones d'envoi sont vides. Le formulaire a été fermé avec Annuler, sans enregistrement.</p></figcaption></figure>

Une fois que l'administrateur a validé l'acheminement ION, enregistrez la configuration et testez un document hors production. Vérifiez son état dans DocBits et dans Infor ION. Un formulaire enregistré ou une entrée dans les métadonnées d'API ne prouve pas une exportation réussie.

La vérification de la documentation a uniquement consulté la liste et le nouveau formulaire. Aucun fichier envoyé, enregistrement, activation, test de connexion, accès à un tenant Infor ou export réel de document n'a été effectué.
