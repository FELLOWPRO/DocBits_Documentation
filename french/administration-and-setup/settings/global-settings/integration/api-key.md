# Clé API

<figure><img src="https://lh7-us.googleusercontent.com/ulCymk1gu-de14qTaFfJwTEmAUp7DY000A40P3nTgRIb7pYXolCbh_GPJvRib5haIH75dPFewY5tJQ0xNbGP3wdSOgCxu7gdVBwlvxkHFcP_3HM3R15zuuBOZM2jEdFxlp2CpV1VDfktmLFSSw4BuLs" alt=""><figcaption></figcaption></figure>

### Clé API

* **Clé :** Il s'agit de l'identifiant unique utilisé par les applications externes pour accéder à l'API de DocBits. Elle est essentielle pour authentifier les requêtes adressées à DocBits depuis d'autres logiciels.
* Des actions telles qu'afficher, régénérer ou copier la clé API peuvent être effectuées ici, en fonction des besoins spécifiques et des protocoles de sécurité.

### Paramètres du fournisseur de services SSO (authentification unique)

* **Entity ID :** Il s'agit de l'identifiant de DocBits en tant que fournisseur de services dans la configuration SSO. Il identifie de manière unique DocBits au sein du cadre SSO.
* **URL SLO (déconnexion unique) :** L'URL à laquelle les sessions SSO sont envoyées pour se déconnecter simultanément de toutes les applications connectées via SSO.
* **URL SSO :** L'URL utilisée pour initier le processus d'authentification unique.
* Des actions telles que « Télécharger le certificat » et « Télécharger les métadonnées » sont disponibles pour obtenir les certificats de sécurité et les informations de métadonnées nécessaires à la configuration et à la maintenance de l'intégration SSO.

{% hint style="info" %}
Voir Configurer le SSO
{% endhint %}

### Paramètres du fournisseur de services d'identité

* Tenant ID : Cet identifiant peut être utilisé lorsque DocBits s'intègre à des services cloud qui nécessitent un identifiant de locataire pour gérer les données et les configurations d'accès spécifiques à l'entreprise utilisant DocBits.
* Téléverser un fichier : Permet à l'administrateur de téléverser des fichiers de configuration ou d'autres fichiers nécessaires facilitant l'intégration avec un fournisseur d'identité.
* Configurer : Un bouton permettant d'appliquer ou de mettre à jour les paramètres après avoir effectué des modifications ou téléversé de nouvelles configurations.
