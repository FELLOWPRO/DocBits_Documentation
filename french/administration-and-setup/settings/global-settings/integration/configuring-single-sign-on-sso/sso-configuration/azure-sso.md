---
description: Utiliser DocBits avec votre connexion Microsoft sans utiliser de mot de passe (distinct)
---

# SSO Azure

### Créer un SSO SAML dans Azure AD

Effectuez les étapes suivantes pour ajouter le SSO SAML dans Azure AD :

*   Dans Azure, accédez à votre console \`Azure Active Directory\`

    ![Page d'accueil du portail Azure avec Azure Active Directory dans les favoris de la navigation de gauche](https://docbits.com/wp-content/uploads/2023/09/DocBits_Azure_1.png)
* Dans le panneau de gauche, cliquez sur \`Enterprise applications\`

![Navigation de gauche d'Azure Active Directory avec le groupe Gérer et l'entrée Applications d'entreprise](https://docbits.com/wp-content/uploads/2023/09/DocBits_Azure_2.png)

* Cliquez sur \`+ New application

<figure><img src="../../../../../../.gitbook/assets/image (213).png" alt="Page Applications d'entreprise d'Azure Active Directory avec la liste Toutes les applications et le bouton Nouvelle application"><figcaption></figcaption></figure>

* Cliquez sur \`+ Create your own application\`

<div align="left"><figure><img src="../../../../../../.gitbook/assets/image (215).png" alt="Boîte de dialogue Parcourir la galerie Azure AD avec les boutons Créer votre propre application et Demander une nouvelle application de la galerie et le champ de recherche Rechercher une application"><figcaption></figcaption></figure></div>

* Saisissez un nom pour votre application. Conservez les autres sélections par défaut.

<figure><img src="https://docbits.com/wp-content/uploads/2023/09/DocBits_Azure_5.png" alt="Boîte de dialogue Créer votre propre application avec le nom MyApplication et l'option sélectionnée Intégrer une autre application que vous ne trouvez pas dans la galerie"><figcaption></figcaption></figure>

* Cliquez sur \`Create\`

### Attribuer des utilisateurs à la configuration SSO

Ensuite, attribuez des utilisateurs ou des groupes à la configuration SSO.

**Important** : Vous devez avoir déjà créé des utilisateurs et des groupes dans Azure AD. Si vous n'avez aucun utilisateur ni groupe, créez-les maintenant avant de continuer.

* Sous \`Getting Started\`, cliquez sur \`Assign Users and Groups\`.
* Cliquez sur \`+ Add user\`

<figure><img src="https://docbits.com/wp-content/uploads/2023/09/DocBits_Azure_6.png" alt="Page Utilisateurs et groupes de l'application MyApplication avec les boutons Ajouter un utilisateur, Modifier, Supprimer et Mettre à jour et le message Aucune affectation d'application trouvée" width="563"><figcaption></figcaption></figure>

* Sélectionnez les utilisateurs et les groupes que vous souhaitez attribuer à cette configuration SSO. Ces utilisateurs pourront s'authentifier dans DocBits (à l'aide du SSO).

<figure><img src="https://docbits.com/wp-content/uploads/2023/09/DocBits_Azure_7.png" alt="Panneau de sélection des utilisateurs avec plusieurs utilisateurs listés et la section Sélectionné"><figcaption></figcaption></figure>

* Cliquez sur \`Select\`
* Lorsque vous êtes satisfait de votre sélection, cliquez sur \`Assign\`

![Boîte de dialogue Ajouter une affectation du locataire chimdustries avec le message 2 utilisateurs sélectionnés et 2 groupes sélectionnés](https://docbits.com/wp-content/uploads/2023/09/DocBits_Azure_8.png)

<div align="left"><figure><img src="../../../../../../.gitbook/assets/image (216) (1).png" alt="Bouton Attribuer mis en évidence par un contour vert dans la boîte de dialogue d'affectation d'Azure Active Directory"><figcaption></figcaption></figure></div>

* Accédez à la liste des \`Groups\` et recherchez les groupes attribués.

### Configurer le SSO dans Azure

Ensuite, vous devez terminer la configuration de l'authentification unique dans Azure.\\

* Dans le panneau de gauche, cliquez sur \`Single sign-on\`

![Navigation de gauche de l'application d'entreprise MyApplication avec l'entrée Authentification unique](https://docbits.com/wp-content/uploads/2023/09/DocBits_Azure_10.png)

* Cliquez sur \`SAML\`

![Page Authentification unique avec la tuile SAML et le texte Authentification riche et sécurisée des applications via le protocole SAML](https://docbits.com/wp-content/uploads/2023/09/DocBits_Azure_11.png)

* Cliquez sur \`Upload metadata file\`

![Page Connexion basée sur SAML avec les liens Charger le fichier de métadonnées et Configurer l'authentification unique](https://docbits.com/wp-content/uploads/2023/09/DocBits_Azure_12.png)

* Téléversez le fichier **metadata.xml** de DocBits, que vous trouverez dans le menu Paramètres **Intégration** sous **Paramètres du fournisseur de services SSO** de votre compte DocBits.

<figure><img src="https://docbits.com/wp-content/uploads/2023/09/DocBits_Azure_Metadata-1024x216.png" alt="Paramètres du fournisseur de services SSO dans DocBits avec l'Entity ID, l'URI SLO et l'URI SSO ainsi que les boutons Télécharger le certificat et Télécharger les métadonnées"><figcaption></figcaption></figure>

* Modifiez la \`Basic SAML Configuration\`

<figure><img src="https://docbits.com/wp-content/uploads/2023/09/DocBits_Azure_13.png" alt="Page Configurer l'authentification unique avec SAML avec la section Configuration SAML de base et les champs Identificateur Entity ID, URL de réponse, URL de connexion, État de relais et URL de déconnexion"><figcaption></figcaption></figure>

* Vérifiez que les champs \`Entity ID\`, \`ACS URL\`, \`Sign on URL\` et \`Logout URL\` sont correctement renseignés.

<figure><img src="https://docbits.com/wp-content/uploads/2023/09/DocBits_Azure_13.1.png" alt="Configuration SAML de base dans Azure avec les textes descriptifs, l'Identificateur Entity ID défini sur l'URL des métadonnées SAML du locataire et l'URL de réponse comme Assertion Consumer Service URL"><figcaption></figcaption></figure>

* Téléchargez le fichier **Federation Metadata XML** nouvellement généré.

<figure><img src="https://docbits.com/wp-content/uploads/2023/09/DocBits_Azure_14.png" alt="Section Certificat de signature SAML avec l'état Actif, l'empreinte, la date d'expiration, l'adresse e-mail de notification et les liens de téléchargement Certificat brut et XML de métadonnées de fédération"><figcaption></figcaption></figure>

* Téléversez le fichier FederationMetadata.xml dans les **Paramètres du fournisseur de services d'identité** de votre compte DocBits, que vous trouverez dans le menu Paramètres **Intégration**.

\\

<figure><img src="https://docbits.com/wp-content/uploads/2023/09/DocBits_Azure_15-1024x204.png" alt="Paramètres du fournisseur de services d'identité dans DocBits avec le Tenant ID, les boutons Charger un fichier et Importer et l'entrée du fichier existant"><figcaption></figcaption></figure>
