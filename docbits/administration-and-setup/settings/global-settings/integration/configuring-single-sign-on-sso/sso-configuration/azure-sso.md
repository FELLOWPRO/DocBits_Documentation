---
description: Using DocBis with your Microsoft Login without using a (separate) password
---

# Azure SSO

### Create SAML SSO in Azure AD

Perform the following steps to add SAML SSO in Azure AD:

*   In Azure, go to your \`Azure Active Directory\` console

    ![Azure portal home page with Azure Active Directory in the favorites of the left navigation](https://docbits.com/wp-content/uploads/2023/09/DocBits_Azure_1.png)
* In the left panel, click \`Enterprise applications\`

![Left navigation of Azure Active Directory with the Manage group and the entry Enterprise applications](https://docbits.com/wp-content/uploads/2023/09/DocBits_Azure_2.png)

* Click \`+ New application

<figure><img src="../../../../../../.gitbook/assets/image (311).png" alt="Enterprise applications page in Azure Active Directory with the All applications list and the New application button"><figcaption></figcaption></figure>

* Click \`+ Create your own application\`

<div align="left"><figure><img src="../../../../../../.gitbook/assets/image (312).png" alt="Browse Azure AD Gallery dialog with the buttons Create your own application and Request new gallery app and the search field Search application"><figcaption></figcaption></figure></div>

* Enter a name for your application. Keep the remaining default selections.

<figure><img src="https://docbits.com/wp-content/uploads/2023/09/DocBits_Azure_5.png" alt="Create your own application dialog with the name MyApplication and the selected option Integrate any other application you don't find in the gallery"><figcaption></figcaption></figure>

* Click on \`Create\`

### Assign Users to the SSO Configuration

Next, assign users or groups to the SSO configuration.

**Important**: You should already have created users and groups in Azure AD. If you don’t have any users or groups, create them now before proceeding.

* Under \`Getting Started\`, click \`Assign Users and Groups\`.
* Click \`+ Add user\`

<figure><img src="https://docbits.com/wp-content/uploads/2023/09/DocBits_Azure_6.png" alt="Users and groups page of the application MyApplication with the buttons Add user, Edit, Remove and Update and the message No application assignments found" width="563"><figcaption></figcaption></figure>

* Select the users and groups you want to assign to this SSO configuration. These users will be able to authenticated in DocBits (using SSO).

<figure><img src="https://docbits.com/wp-content/uploads/2023/09/DocBits_Azure_7.png" alt="User selection panel with several users listed and the section Selected"><figcaption></figcaption></figure>

* Click \`Select\`
* When you’re satisfied with your selection, click \`Assign\`

![Add Assignment dialog of the tenant chimdustries with the message 2 users selected and 2 groups selected](https://docbits.com/wp-content/uploads/2023/09/DocBits_Azure_8.png)

<div align="left"><figure><img src="../../../../../../.gitbook/assets/image (313).png" alt="Assign button highlighted with a green border in the assignment dialog of Azure Active Directory"><figcaption></figcaption></figure></div>

* Go to the \`Groups\` view list and find the assigned groups.

### Set up SSO in Azure

Next, you need to finish setting up single-sign-on in Azure.\\

* In the left panel, click \`Single sign-on\`

![Left navigation of the enterprise application MyApplication with the entry Single sign-on](https://docbits.com/wp-content/uploads/2023/09/DocBits_Azure_10.png)

* Click \`SAML\`

![Single sign-on page with the tile SAML and the text Rich and secure authentication to applications using the SAML protocol](https://docbits.com/wp-content/uploads/2023/09/DocBits_Azure_11.png)

* Click \`Upload metadata file\`

![SAML-based Sign-on page with the links Upload metadata file and Set up Single Sign-On](https://docbits.com/wp-content/uploads/2023/09/DocBits_Azure_12.png)

* Upload the DocBits **metadata.xml**, which you can find in the Settings menu **Integration** under **SSO Service Provider Settings** of your DocBits account.

<figure><img src="https://docbits.com/wp-content/uploads/2023/09/DocBits_Azure_Metadata-1024x216.png" alt="SSO Service Provider Settings in DocBits with the Entity ID, the SLO Uri and the SSO Uri and the buttons Certificate Download and Download Metadata"><figcaption></figcaption></figure>

* Edit the \`Basic SAML Configuration\`

<figure><img src="https://docbits.com/wp-content/uploads/2023/09/DocBits_Azure_13.png" alt="Set up Single Sign-On with SAML page with the section Basic SAML Configuration and the fields Identifier Entity ID, Reply URL, Sign on URL, Relay State and Logout Url"><figcaption></figcaption></figure>

* Check if the \`Entity ID\`, \`ACS URL\`, \`Sign on URL\` and \`Logout URL\` are populated right.

<figure><img src="https://docbits.com/wp-content/uploads/2023/09/DocBits_Azure_13.1.png" alt="Basic SAML Configuration in Azure with the description texts, the Identifier Entity ID set to the SAML metadata URL of the tenant and the Reply URL as Assertion Consumer Service URL"><figcaption></figcaption></figure>

* Download the newly generated **Federation Metadata XML**.

<figure><img src="https://docbits.com/wp-content/uploads/2023/09/DocBits_Azure_14.png" alt="SAML Signing Certificate section with the status Active, the thumbprint, the expiration date, the notification email and the download links Certificate Raw and Federation Metadata XML"><figcaption></figcaption></figure>

* Upload the FederationMetadata.xml into the **Identity Service Provider Settings** of your DocBits account which you can find in the Settings menu **Integration**.

\\

<figure><img src="https://docbits.com/wp-content/uploads/2023/09/DocBits_Azure_15-1024x204.png" alt="Identity Service Provider Settings in DocBits with the Tenant ID, the buttons Upload file and Import and the entry for the existing file"><figcaption></figcaption></figure>
