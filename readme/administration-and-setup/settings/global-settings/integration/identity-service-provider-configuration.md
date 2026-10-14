# Configuration du fournisseur de services d'identité

La configuration du fournisseur de services d'identité (IdP) pour l'intégration avec DocBits nécessite quelques étapes spécifiques. Voici un guide pour y parvenir :

<figure><img src="../../../../.gitbook/assets/image (83).png" alt=""><figcaption></figcaption></figure>

**Accéder à l'interface de configuration de l'IdP**

* Connectez-vous à votre fournisseur de services d'identité (IdP) en tant qu'administrateur.
* Naviguez vers l'interface de paramètres ou de configuration dédiée à la gestion des intégrations SAML.

**Saisir le Tenant ID :**

* Recherchez la section qui permet de configurer de nouvelles intégrations SAML.
* Saisissez le tenant ID DocBits. Cet ID identifie votre compte DocBits auprès de l'IdP et permet une communication sécurisée entre les deux systèmes.

**Importer les fichiers requis :**

* DocBits exige généralement de télécharger des métadonnées ou d'ajouter des détails de configuration spécifiques. Consultez la documentation de votre IdP pour connaître les étapes requises.
* Téléchargez le fichier de métadonnées DocBits ou importez-le dans le menu de configuration de votre IdP. Vous pouvez aussi saisir manuellement les détails de configuration requis, selon ce que prend en charge votre IdP.

**Configurer les paramètres d'intégration :**

* Assurez-vous que les paramètres d'intégration, tels que l'URL SSO, l'Entity ID et le certificat SAML, sont corrects.
* Vérifiez que l'URL de déconnexion unique (SLO) et les autres paramètres requis sont correctement configurés. Ils sont essentiels pour une authentification et une déconnexion fluides via SAML.

**Vérifier la configuration :**

* Prenez le temps de vous assurer que toutes les informations saisies sont correctes et qu'il n'y a ni fautes de frappe ni erreurs de configuration.
* Effectuez des tests pour vous assurer que les utilisateurs peuvent se connecter à DocBits via SAML et que la déconnexion unique fonctionne correctement.

**Considérations de sécurité :**

* Assurez-vous que tous les fichiers transférés et les détails de configuration sont traités de manière sécurisée afin d'éviter les fuites de données ou les accès non autorisés.
* Protégez les informations sensibles telles que les certificats SAML et les identifiants contre les accès non autorisés et conservez-les dans un endroit sûr.
