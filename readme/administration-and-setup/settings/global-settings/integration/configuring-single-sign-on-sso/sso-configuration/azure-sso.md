---
description: Utiliser DocBits avec votre connexion Microsoft sans utiliser de mot de passe (distinct)
---

# SSO Azure

### Créer un SSO SAML dans Azure AD

Effectuez les étapes suivantes pour ajouter le SSO SAML dans Azure AD :

*   Dans Azure, accédez à votre console \`Azure Active Directory\`

    ![Volet de navigation du portail Azure avec des favoris tels que Resource groups, All resources et Azure Active Directory](https://docbits.com/wp-content/uploads/2023/09/DocBits_Azure_1.png)
* Dans le panneau de gauche, cliquez sur \`Enterprise applications\`

![Panneau gauche d'Azure Active Directory avec les entrées Manage Users, Groups, Roles and administrators et Enterprise applications](https://docbits.com/wp-content/uploads/2023/09/DocBits_Azure_2.png)

* Cliquez sur \`+ New application

<figure><img src="../../../../../../.gitbook/assets/image (213).png" alt="Boîte de dialogue Add Assignment dans Azure avec 2 users selected, 2 groups selected et Select Role défini sur User"><figcaption></figcaption></figure>

* Cliquez sur \`+ Create your own application\`

<div align="left"><figure><img src="../../../../../../.gitbook/assets/image (215).png" alt="Menu de vue d'ensemble de l'application d'entreprise dans Azure avec les entrées Manage Properties, Owners, Users and groups, Single sign-on et Provisioning"><figcaption></figcaption></figure></div>

* Saisissez un nom pour votre application. Conservez les autres sélections par défaut.

<figure><img src="https://docbits.com/wp-content/uploads/2023/09/DocBits_Azure_5.png" alt="Boîte de dialogue Create your own application dans Azure avec le nom d'application MyApplication et les options d'intégration d'application"><figcaption></figcaption></figure>

* Cliquez sur \`Create\`

### Attribuer des utilisateurs à la configuration SSO

Ensuite, attribuez des utilisateurs ou des groupes à la configuration SSO.

**Important** : Vous devez avoir déjà créé des utilisateurs et des groupes dans Azure AD. Si vous n'avez aucun utilisateur ni groupe, créez-les maintenant avant de continuer.

* Sous \`Getting Started\`, cliquez sur \`Assign Users and Groups\`.
* Cliquez sur \`+ Add user\`

<figure><img src="https://docbits.com/wp-content/uploads/2023/09/DocBits_Azure_6.png" alt="Page Users and groups de MyApplication dans Azure avec les boutons Add user, Edit et Remove et une liste Display Name vide" width="563"><figcaption></figcaption></figure>

* Sélectionnez les utilisateurs et les groupes que vous souhaitez attribuer à cette configuration SSO. Ces utilisateurs pourront s'authentifier dans DocBits (à l'aide du SSO).

<figure><img src="https://docbits.com/wp-content/uploads/2023/09/DocBits_Azure_7.png" alt="Panneau de sélection d'utilisateurs et de groupes dans Azure avec une liste d'utilisateurs Daniel et un panneau Selected items"><figcaption></figcaption></figure>

* Cliquez sur \`Select\`
* Lorsque vous êtes satisfait de votre sélection, cliquez sur \`Assign\`

![Boîte de dialogue Add Assignment dans Azure avec 2 users selected, 2 groups selected et Select Role défini sur User](https://docbits.com/wp-content/uploads/2023/09/DocBits_Azure_8.png)

<div align="left"><figure><img src="../../../../../../.gitbook/assets/image (216) (1).png" alt="Boîte de dialogue Create your own application dans Azure avec le nom d'application MyApplication et les options d'intégration d'application"><figcaption></figcaption></figure></div>

* Accédez à la liste des \`Groups\` et recherchez les groupes attribués.

### Configurer le SSO dans Azure

Ensuite, vous devez terminer la configuration de l'authentification unique dans Azure.\\

* Dans le panneau de gauche, cliquez sur \`Single sign-on\`

![Menu de vue d'ensemble de l'application d'entreprise dans Azure avec les entrées Manage Properties, Owners, Users and groups, Single sign-on et Provisioning](https://docbits.com/wp-content/uploads/2023/09/DocBits_Azure_10.png)

* Cliquez sur \`SAML\`

![Carte d'option SAML dans Azure décrivant une authentification riche et sécurisée avec le protocole Security Assertion Markup Language](https://docbits.com/wp-content/uploads/2023/09/DocBits_Azure_11.png)

* Cliquez sur \`Upload metadata file\`

![Panneau SAML-based Sign-on dans Azure avec Upload metadata file et Set up Single Sign-On](https://docbits.com/wp-content/uploads/2023/09/DocBits_Azure_12.png)

* Téléversez le fichier **metadata.xml** de DocBits, que vous trouverez dans le menu Paramètres **Intégration** sous **Paramètres du fournisseur de services SSO** de votre compte DocBits.

<figure><img src="https://docbits.com/wp-content/uploads/2023/09/DocBits_Azure_Metadata-1024x216.png" alt="Page SSO Service Provider Settings avec le Tenant ID, l'Entity ID et les champs SSO Url, SLO Url et Metadata Url"><figcaption></figcaption></figure>

* Modifiez la \`Basic SAML Configuration\`

<figure><img src="https://docbits.com/wp-content/uploads/2023/09/DocBits_Azure_13.png" alt="Écran de configuration de l'authentification unique SAML affichant Basic SAML Configuration avec Identifier, Reply URL, Sign on URL et Logout Url"><figcaption></figcaption></figure>

* Vérifiez que les champs \`Entity ID\`, \`ACS URL\`, \`Sign on URL\` et \`Logout URL\` sont correctement renseignés.

<figure><img src="https://docbits.com/wp-content/uploads/2023/09/DocBits_Azure_13.1.png" alt="Éditeur de Basic SAML Configuration dans Azure avec les champs Identifier, Reply URL, Sign on URL, Relay State et Logout Url ainsi que Save"><figcaption></figcaption></figure>

* Téléchargez le fichier **Federation Metadata XML** nouvellement généré.

<figure><img src="https://docbits.com/wp-content/uploads/2023/09/DocBits_Azure_14.png" alt="Section SAML Signing Certificate dans Azure avec empreinte, date d'expiration et liens de téléchargement pour Certificate (Raw) et Federation Metadata XML"><figcaption></figcaption></figure>

* Téléversez le fichier FederationMetadata.xml dans les **Paramètres du fournisseur de services d'identité** de votre compte DocBits, que vous trouverez dans le menu Paramètres **Intégration**.

\\

<figure><img src="https://docbits.com/wp-content/uploads/2023/09/DocBits_Azure_15-1024x204.png" alt="Boîte de dialogue Identity Service Provider Settings dans DocBits avec le Tenant ID FELLOWPRO_PRD et le bouton Upload file"><figcaption></figcaption></figure>
