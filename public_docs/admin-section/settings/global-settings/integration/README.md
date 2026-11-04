# Intégration

<figure><img src="../../../../.gitbook/assets/Bildschirmfoto 2024-05-08 um 08.39.14.png" alt=""><figcaption></figcaption></figure>

## Clé API

* **Clé**: Il s'agit de l'identifiant unique utilisé par les applications externes pour accéder à l'API de Docbits. Il est crucial pour authentifier les requêtes effectuées vers Docbits à partir d'autres logiciels.
* Des actions telles que la visualisation, la régénération ou la copie de la clé API peuvent être effectuées ici, en fonction des besoins spécifiques et des protocoles de sécurité.

## Paramètres du Fournisseur de Services SSO (Authentification Unique)

* **ID de l'entité**: Il s'agit de l'identifiant de Docbits en tant que fournisseur de services dans la configuration SSO. Il identifie de manière unique Docbits au sein du cadre SSO.
* **URL de déconnexion unique (SLO - Single Logout)**: L'URL vers laquelle les sessions SSO sont envoyées pour se déconnecter simultanément de toutes les applications connectées via SSO.
* **URL SSO**: L'URL utilisée pour initier le processus d'authentification unique.
* Des actions telles que "Télécharger le certificat" et "Télécharger les métadonnées" sont disponibles pour obtenir les certificats de sécurité nécessaires et les informations de métadonnées utilisées pour configurer et maintenir l'intégration SSO.

{% hint style="info" %}
Voir [Configuration SSO](../../../setup/sso-configuration/)
{% endhint %}

## Paramètres du Fournisseur de Services d'Identité

* **ID du locataire**: Cela peut être utilisé lorsque Docbits s'intègre avec des services cloud qui nécessitent un identifiant de locataire pour gérer les données et les configurations d'accès spécifiques à l'entreprise utilisant Docbits.
* **Téléverser un fichier**: Permet à l'administrateur de téléverser des fichiers de configuration ou d'autres fichiers nécessaires facilitant l'intégration avec un fournisseur d'identité.
* **Configurer**: Un bouton pour appliquer ou mettre à jour les paramètres après avoir apporté des modifications ou téléchargé de nouvelles configurations.
