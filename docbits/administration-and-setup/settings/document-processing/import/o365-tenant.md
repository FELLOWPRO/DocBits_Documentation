# O365 Tenant

## Register App on Azure AD

<mark style="color:red;">**Note**</mark>: The permissions may require authorization from an administrator.

1. Sign in to the [Azure Portal](https://portal.azure.com/) using your credentials.
2. From Azure services, locate and open Azure Active Directory (also known as Azure AD).

<figure><img src="../../../../.gitbook/assets/o365_tenant_1.png" alt="Azure portal page with the Azure Active Directory entry and the service search bar"><figcaption></figcaption></figure>

3. Under the **Manage** section, select **App registrations**.

<figure><img src="../../../../.gitbook/assets/o365_tenant_2.png" alt="Azure Active Directory overview page with the left Manage menu open and App registrations highlighted"><figcaption></figcaption></figure>

4. In the App registrations screen, click **+ New registration**.

<figure><img src="../../../../.gitbook/assets/o365_tenant_3.png" alt="App registrations screen in Azure with the New registration button in the toolbar and the list of registered apps"><figcaption></figcaption></figure>

5. The **Register an application** screen displays. Enter the user-facing display name for the App in **Name**.

<figure><img src="../../../../.gitbook/assets/o365_tenant_4.png" alt="Register an application screen in the Azure Portal with the Name field empty for the new app"><figcaption></figcaption></figure>

6. Select one of the following account types depending on your needs:

* **Accounts in any organizational directory (Any Azure AD directory Multitenant) and personal Microsoft accounts (e.g. Skype, Xbox)**
* **Accounts in any organizational directory (Any Azure AD directory Multitenant)**

<figure><img src="../../../../.gitbook/assets/o365_tenant_5.png" alt="Register an application screen with the supported account type radio options for organizational directories and personal Microsoft accounts"><figcaption></figcaption></figure>

7. Leave the option **Redirect URI (optional)** as is.

<figure><img src="../../../../.gitbook/assets/o365_tenant_6.png" alt="Register an application screen with the Redirect URI (optional) section left unchanged at the bottom"><figcaption></figcaption></figure>

8. Click **Register** to complete the App registration. This will return you to the screen for the new App.
9. In the App screen, locate the **Application (client) ID**. Copy it to be used when configuring email import for **DocBits**.

<figure><img src="../../../../.gitbook/assets/o365_tenant_7.png" alt="Registered app overview page showing the Display name Ephesoft OAuth2 App and the Application client ID"><figcaption></figcaption></figure>

10. From left panel, select **Certificates & secrets**:

<figure><img src="../../../../.gitbook/assets/o365_tenant_8.png" alt="Registered app overview page with Certificates and secrets selected in the Manage section of the left panel"><figcaption></figcaption></figure>

11. In the **Certificates & secrets** screen, click on **+ New client secret** button under **Client secrets** section:

<figure><img src="../../../../.gitbook/assets/o365_tenant_9.png" alt="Certificates &amp; secrets screen with the Client secrets section and the + New client secret button"><figcaption></figcaption></figure>

12. In the **Add a client secret** dialog box, click the **Add** button:

<figure><img src="../../../../.gitbook/assets/o365_tenant_10.png" alt="Add a client secret dialog with the Description and Expires fields and the Add button"><figcaption></figcaption></figure>

It is recommended to fill in a description to identify this secret among many (as of now the limit is 2 secrets per App).

<figure><img src="../../../../.gitbook/assets/o365_tenant_11.png" alt="Client secrets list showing the new secret with its description, Value and Expires columns"><figcaption></figcaption></figure>

<mark style="color:red;">**Note**</mark>: Select this expiration date according to your company policy. Once expired, a new client secret will need to be created and specified for each email configuration where it was used previously.

13. The newly generated client secret will be visible. Copy this client secret to be used when configuring email import for DocBits

<figure><img src="../../../../.gitbook/assets/o365_tenant_12.png" alt="Client secrets section of Certificates &amp; secrets with the generated secret Value ready to copy"><figcaption></figcaption></figure>

**Important:** Ensure that you have copied the client secret as the client secret will not display again once it is closed.

14. Select **Authentication** on the left panel. This will present the **Authentication** screen on the right-hand side.

<figure><img src="../../../../.gitbook/assets/o365_tenant_13.png" alt="App registration Authentication screen opened from the left panel with the platform settings on the right"><figcaption></figcaption></figure>

15. In the **Advanced settings** section, click **Yes** for **Default client type**.

<figure><img src="../../../../.gitbook/assets/o365_tenant_14.png" alt="Advanced settings section of the Authentication screen with the Default client type option set to Yes"><figcaption></figcaption></figure>

16. Click **Save** to confirm changes.

<figure><img src="../../../../.gitbook/assets/o365_tenant_15.png" alt="App registration top bar with the Save button highlighted after enabling the default client type"><figcaption></figcaption></figure>

17. Select **API permissions** on the left panel. This will present the API permissions screen.

<figure><img src="../../../../.gitbook/assets/o365_tenant_16.png" alt="API permissions screen opened from the left panel showing Configured permissions for the app"><figcaption></figcaption></figure>

18. By default the **User.Read** permission from **Microsoft Graph** is present, leave this as is.

<figure><img src="../../../../.gitbook/assets/o365_tenant_17.png" alt="Configured permissions list showing the default User.Read delegated permission for Microsoft Graph"><figcaption></figcaption></figure>

<mark style="color:red;">**Note**</mark>: This is a required permission. If this permission is not available, then add the permission with the steps mentioned below for **Mail.ReadWrite** permission.

19. Click **+ Add a permission**.This will open the **Request API permissions** panel.

<figure><img src="../../../../.gitbook/assets/o365_tenant_18.png" alt="Request API permissions panel with Microsoft APIs, APIs my organization uses and the + Add a permission flow"><figcaption></figcaption></figure>

20. Click **Microsoft Graph**.

<figure><img src="../../../../.gitbook/assets/o365_tenant_19.png" alt="Request API permissions panel with Microsoft Graph highlighted among the commonly used Microsoft APIs"><figcaption></figcaption></figure>

21. From the two sub-categories, select **App Permissions**.

<figure><img src="../../../../.gitbook/assets/o365_tenant_20.png" alt="Request API permissions panel for Microsoft Graph with the Delegated permissions and Application permissions options"><figcaption></figcaption></figure>

22. Type **Mail.ReadWrite** in the search box. Select the **Mail.ReadWrite** checkbox for the permission.

<figure><img src="../../../../.gitbook/assets/o365_tenant_21.png" alt="Application permissions search box with Mail.ReadWrite typed and the Mail.ReadWrite permission checkbox selected"><figcaption></figcaption></figure>

23. This will enable the **Add permissions** button at the bottom of the panel. Click **Add permissions**.

<figure><img src="../../../../.gitbook/assets/o365_tenant_22.png" alt="Request API permissions panel with the Mail.ReadWrite permission selected and the Add permissions button at the bottom"><figcaption></figcaption></figure>

24. This will add the **Mail.ReadWrite** permission to the list of **Configured permissions** for the App.

<mark style="color:red;">**Note**</mark>: Administrator permissions may be required. The administrator will have to authorize the App for using these permissions. Once authorized the granted status will be indicated as follows:

<figure><img src="../../../../.gitbook/assets/o365_tenant_23.png" alt="Configured permissions list with the Mail.ReadWrite application permission added and its granted status shown"><figcaption></figcaption></figure>
