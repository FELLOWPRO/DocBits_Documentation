---
description: Utiliser DocBits avec votre connexion Microsoft sans utiliser de mot de passe (distinct)
---

# Azure SSO

### Créer un SSO SAML dans Azure AD

Effectuez les étapes suivantes pour ajouter le SSO SAML dans Azure AD :

*   Dans Azure, accédez à votre console \`Azure Active Directory\`

    ![](https://docbits.com/wp-content/uploads/2023/09/DocBits_Azure_1.png)
* Dans le panneau de gauche, cliquez sur \`Enterprise applications\`

![](https://docbits.com/wp-content/uploads/2023/09/DocBits_Azure_2.png)

* Cliquez sur \`+ New application

<figure><img src="../../../../../../.gitbook/assets/image (213).png" alt=""><figcaption></figcaption></figure>

* Cliquez sur \`+ Create your own application\`

<div align="left"><figure><img src="../../../../../../.gitbook/assets/image (215).png" alt=""><figcaption></figcaption></figure></div>

* Saisissez un nom pour votre application. Conservez les autres sélections par défaut.

<figure><img src="https://docbits.com/wp-content/uploads/2023/09/DocBits_Azure_5.png" alt=""><figcaption></figcaption></figure>

* Cliquez sur \`Create\`

### Attribuer des utilisateurs à la configuration SSO

Ensuite, attribuez des utilisateurs ou des groupes à la configuration SSO.

**Important** : Vous devez avoir déjà créé des utilisateurs et des groupes dans Azure AD. Si vous n'avez aucun utilisateur ni groupe, créez-les maintenant avant de continuer.

* Sous \`Getting Started\`, cliquez sur \`Assign Users and Groups\`.
* Cliquez sur \`+ Add user\`

<figure><img src="https://docbits.com/wp-content/uploads/2023/09/DocBits_Azure_6.png" alt="" width="563"><figcaption></figcaption></figure>

* Sélectionnez les utilisateurs et les groupes que vous souhaitez attribuer à cette configuration SSO. Ces utilisateurs pourront s'authentifier dans DocBits (à l'aide du SSO).

<figure><img src="https://docbits.com/wp-content/uploads/2023/09/DocBits_Azure_7.png" alt=""><figcaption></figcaption></figure>

* Cliquez sur \`Select\`
* Lorsque vous êtes satisfait de votre sélection, cliquez sur \`Assign\`

![](https://docbits.com/wp-content/uploads/2023/09/DocBits_Azure_8.png)

<div align="left"><figure><img src="../../../../../../.gitbook/assets/image (216) (1).png" alt=""><figcaption></figcaption></figure></div>

* Accédez à la liste des \`Groups\` et recherchez les groupes attribués.

### Configurer le SSO dans Azure

Ensuite, vous devez terminer la configuration de l'authentification unique dans Azure.\\

* Dans le panneau de gauche, cliquez sur \`Single sign-on\`

![](https://docbits.com/wp-content/uploads/2023/09/DocBits_Azure_10.png)

* Cliquez sur \`SAML\`

![](https://docbits.com/wp-content/uploads/2023/09/DocBits_Azure_11.png)

* Cliquez sur \`Upload metadata file\`

![](https://docbits.com/wp-content/uploads/2023/09/DocBits_Azure_12.png)

* Téléversez le fichier **metadata.xml** de DocBits, que vous trouverez dans le menu Paramètres **Intégration** sous **Paramètres du fournisseur de services SSO** de votre compte DocBits.

<figure><img src="https://docbits.com/wp-content/uploads/2023/09/DocBits_Azure_Metadata-1024x216.png" alt=""><figcaption></figcaption></figure>

* Modifiez la \`Basic SAML Configuration\`

<figure><img src="https://docbits.com/wp-content/uploads/2023/09/DocBits_Azure_13.png" alt=""><figcaption></figcaption></figure>

* Vérifiez que les champs \`Entity ID\`, \`ACS URL\`, \`Sign on URL\` et \`Logout URL\` sont correctement renseignés.

<figure><img src="https://docbits.com/wp-content/uploads/2023/09/DocBits_Azure_13.1.png" alt=""><figcaption></figcaption></figure>

* Téléchargez le fichier **Federation Metadata XML** nouvellement généré.

<figure><img src="https://docbits.com/wp-content/uploads/2023/09/DocBits_Azure_14.png" alt=""><figcaption></figcaption></figure>

* Téléversez le fichier FederationMetadata.xml dans les **Paramètres du fournisseur de services d'identité** de votre compte DocBits, que vous trouverez dans le menu Paramètres **Intégration**.

\\

<figure><img src="https://docbits.com/wp-content/uploads/2023/09/DocBits_Azure_15-1024x204.png" alt=""><figcaption></figcaption></figure>
