---
description: Using DocBis with your Microsoft Login without using a (separate) password
---

# Azure SSO

### Create SAML SSO in Azure AD

Perform the following steps to add SAML SSO in Azure AD:

*   In Azure, go to your \`Azure Active Directory\` console

    ![Azure portal navigation pane with favorites such as Resource groups, All resources and Azure Active Directory](https://docbits.com/wp-content/uploads/2023/09/DocBits_Azure_1.png)
* In the left panel, click \`Enterprise applications\`

![Azure Active Directory left panel with Manage entries Users, Groups, Roles and administrators and Enterprise applications](https://docbits.com/wp-content/uploads/2023/09/DocBits_Azure_2.png)

* Click \`+ New application

<figure><img src="../../../../../../.gitbook/assets/image (311).png" alt="Enterprise applications page in Azure AD with the New application button in the toolbar"><figcaption></figcaption></figure>

* Click \`+ Create your own application\`

<div align="left"><figure><img src="../../../../../../.gitbook/assets/image (312).png" alt="Azure AD Gallery page with the options Create your own application and Request new gallery app"><figcaption></figcaption></figure></div>

* Enter a name for your application. Keep the remaining default selections.

<figure><img src="https://docbits.com/wp-content/uploads/2023/09/DocBits_Azure_5.png" alt="Create your own application dialog in Azure with the app name MyApplication and the application integration options"><figcaption></figcaption></figure>

* Click on \`Create\`

### Assign Users to the SSO Configuration

Next, assign users or groups to the SSO configuration.

**Important**: You should already have created users and groups in Azure AD. If you don’t have any users or groups, create them now before proceeding.

* Under \`Getting Started\`, click \`Assign Users and Groups\`.
* Click \`+ Add user\`

<figure><img src="https://docbits.com/wp-content/uploads/2023/09/DocBits_Azure_6.png" alt="Users and groups page for MyApplication in Azure with Add user, Edit and Remove buttons and an empty Display Name list" width="563"><figcaption></figcaption></figure>

* Select the users and groups you want to assign to this SSO configuration. These users will be able to authenticated in DocBits (using SSO).

<figure><img src="https://docbits.com/wp-content/uploads/2023/09/DocBits_Azure_7.png" alt="Users and groups selection panel in Azure with a list of Daniel users and a Selected items panel"><figcaption></figcaption></figure>

* Click \`Select\`
* When you’re satisfied with your selection, click \`Assign\`

![Azure Add Assignment dialog with 2 users selected, 2 groups selected and Select Role set to User](https://docbits.com/wp-content/uploads/2023/09/DocBits_Azure_8.png)

<div align="left"><figure><img src="../../../../../../.gitbook/assets/image (313).png" alt="Assign button in Azure used to confirm the selected users and groups"><figcaption></figcaption></figure></div>

* Go to the \`Groups\` view list and find the assigned groups.

### Set up SSO in Azure

Next, you need to finish setting up single-sign-on in Azure.\\

* In the left panel, click \`Single sign-on\`

![Enterprise Application overview menu in Azure with Manage entries Properties, Owners, Users and groups, Single sign-on and Provisioning](https://docbits.com/wp-content/uploads/2023/09/DocBits_Azure_10.png)

* Click \`SAML\`

![SAML option card in Azure describing rich and secure authentication with the Security Assertion Markup Language protocol](https://docbits.com/wp-content/uploads/2023/09/DocBits_Azure_11.png)

* Click \`Upload metadata file\`

![SAML-based Sign-on panel in Azure with Upload metadata file and Set up Single Sign-On](https://docbits.com/wp-content/uploads/2023/09/DocBits_Azure_12.png)

* Upload the DocBits **metadata.xml**, which you can find in the Settings menu **Integration** under **SSO Service Provider Settings** of your DocBits account.

<figure><img src="https://docbits.com/wp-content/uploads/2023/09/DocBits_Azure_Metadata-1024x216.png" alt="SSO Service Provider Settings page with the Tenant ID, the Entity ID and the SSO Url, SLO Url and Metadata Url fields"><figcaption></figcaption></figure>

* Edit the \`Basic SAML Configuration\`

<figure><img src="https://docbits.com/wp-content/uploads/2023/09/DocBits_Azure_13.png" alt="Set up Single Sign-On with SAML screen showing Basic SAML Configuration with Identifier, Reply URL, Sign on URL and Logout Url"><figcaption></figcaption></figure>

* Check if the \`Entity ID\`, \`ACS URL\`, \`Sign on URL\` and \`Logout URL\` are populated right.

<figure><img src="https://docbits.com/wp-content/uploads/2023/09/DocBits_Azure_13.1.png" alt="Basic SAML Configuration editor in Azure with Identifier, Reply URL, Sign on URL, Relay State and Logout Url fields and Save"><figcaption></figcaption></figure>

* Download the newly generated **Federation Metadata XML**.

<figure><img src="https://docbits.com/wp-content/uploads/2023/09/DocBits_Azure_14.png" alt="SAML Signing Certificate section in Azure with thumbprint, expiration date and Download links for Certificate (Raw) and Federation Metadata XML"><figcaption></figcaption></figure>

* Upload the FederationMetadata.xml into the **Identity Service Provider Settings** of your DocBits account which you can find in the Settings menu **Integration**.

\\

<figure><img src="https://docbits.com/wp-content/uploads/2023/09/DocBits_Azure_15-1024x204.png" alt="Identity Service Provider Settings dialog in DocBits with the Tenant ID FELLOWPRO_PRD and the button Upload file"><figcaption></figcaption></figure>
