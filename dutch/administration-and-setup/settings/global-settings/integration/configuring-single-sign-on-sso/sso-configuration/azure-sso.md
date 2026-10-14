---
description: Using DocBis with your Microsoft Login without using a (separate) password
---

# Azure SSO

### Create SAML SSO in Azure AD

Perform the following steps to add SAML SSO in Azure AD:

*   In Azure, go to your \`Azure Active Directory\` console

    ![](https://docbits.com/wp-content/uploads/2023/09/DocBits_Azure_1.png)
* In the left panel, click \`Enterprise applications\`

![](https://docbits.com/wp-content/uploads/2023/09/DocBits_Azure_2.png)

* Click \`+ New application

<figure><img src="../../../../../../.gitbook/assets/docbits_azure_sso_new_app_2.png" alt="Docbits Azure Sso New App 2"><figcaption></figcaption></figure>

* Click \`+ Create your own application\`

<div align="left"><figure><img src="../../../../../../.gitbook/assets/docbits_azure_sso_create_own_app_2.png" alt="Docbits Azure Sso Create Own App 2"><figcaption></figcaption></figure></div>

* Enter a name for your application. Keep the remaining default selections.

<figure><img src="https://docbits.com/wp-content/uploads/2023/09/DocBits_Azure_5.png" alt=""><figcaption></figcaption></figure>

* Click on \`Create\`

### Assign Users to the SSO Configuration

Next, assign users or groups to the SSO configuration.

**Important**: You should already have created users and groups in Azure AD. If you don’t have any users or groups, create them now before proceeding.

* Under \`Getting Started\`, click \`Assign Users and Groups\`.
* Click \`+ Add user\`

<figure><img src="https://docbits.com/wp-content/uploads/2023/09/DocBits_Azure_6.png" alt="" width="563"><figcaption></figcaption></figure>

* Select the users and groups you want to assign to this SSO configuration. These users will be able to authenticated in DocBits (using SSO).

<figure><img src="https://docbits.com/wp-content/uploads/2023/09/DocBits_Azure_7.png" alt=""><figcaption></figcaption></figure>

* Click \`Select\`
* When you’re satisfied with your selection, click \`Assign\`

![](https://docbits.com/wp-content/uploads/2023/09/DocBits_Azure_8.png)

<div align="left"><figure><img src="../../../../../../.gitbook/assets/docbits_azure_sso_groups.png" alt="Docbits Azure Sso Groups"><figcaption></figcaption></figure></div>

* Go to the \`Groups\` view list and find the assigned groups.

### Set up SSO in Azure

Next, you need to finish setting up single-sign-on in Azure.\\

* In the left panel, click \`Single sign-on\`

![](https://docbits.com/wp-content/uploads/2023/09/DocBits_Azure_10.png)

* Click \`SAML\`

![](https://docbits.com/wp-content/uploads/2023/09/DocBits_Azure_11.png)

* Click \`Upload metadata file\`

![](https://docbits.com/wp-content/uploads/2023/09/DocBits_Azure_12.png)

* Upload the DocBits **metadata.xml**, which you can find in the Settings menu **Integration** under **SSO Service Provider Settings** of your DocBits account.

<figure><img src="https://docbits.com/wp-content/uploads/2023/09/DocBits_Azure_Metadata-1024x216.png" alt=""><figcaption></figcaption></figure>

* Edit the \`Basic SAML Configuration\`

<figure><img src="https://docbits.com/wp-content/uploads/2023/09/DocBits_Azure_13.png" alt=""><figcaption></figcaption></figure>

* Check if the \`Entity ID\`, \`ACS URL\`, \`Sign on URL\` and \`Logout URL\` are populated right.

<figure><img src="https://docbits.com/wp-content/uploads/2023/09/DocBits_Azure_13.1.png" alt=""><figcaption></figcaption></figure>

* Download the newly generated **Federation Metadata XML**.

<figure><img src="https://docbits.com/wp-content/uploads/2023/09/DocBits_Azure_14.png" alt=""><figcaption></figcaption></figure>

* Upload the FederationMetadata.xml into the **Identity Service Provider Settings** of your DocBits account which you can find in the Settings menu **Integration**.

\\

<figure><img src="https://docbits.com/wp-content/uploads/2023/09/DocBits_Azure_15-1024x204.png" alt=""><figcaption></figcaption></figure>
