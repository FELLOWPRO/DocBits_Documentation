# Identity Service Provider Configuration

Configuring the Identity Service Provider (IdP) to integrate with DocBits requires a few specific steps.Here is a guide to doing that:

<figure><img src="../../../../.gitbook/assets/image (199).png" alt="Identity Service Provider Settings screen with an Upload file field and an Import button"><figcaption></figcaption></figure>

**Accessing the IdP configuration interface**

* Log in to your Identity Service Provider (IdP) as an administrator.
* Navigate to the settings or configuration interface dedicated to managing SAML integrations.

**Entering the Tenant ID:**

* Look for the section that allows configuration for new SAML integrations.
* Enter the DocBits tenant ID. This ID identifies your Docbits account to the IdP and enables secure communication between the two systems.

**Importing the required files:**

* DocBits usually requires downloading metadata or adding specific configuration details. Check your IdP's documentation to see what steps are required.
* Download the DocBits metadata file or import it into your IdP's configuration menu. Alternatively, you can manually enter the required configuration details, depending on what your IdP supports.

**Configure integration settings:**

* Make sure the integration settings, such as the SSO URL, Entity ID, and SAML certificate, are correct.
* Check that the Single Log-Out (SLO) URL and other required parameters are configured correctly. These are critical for smooth authentication and logout via SAML.

**Verify configuration:**

* Take time to make sure all information entered is correct and that there are no typos or misconfigurations.
* Run tests to ensure that users can successfully log into Docbits via SAML and that Single Log-Out is working properly.

**Security considerations:**

* Make sure all transferred files and configuration details are handled securely to avoid data leaks or unauthorized access.
* Protect sensitive information such as SAML certificates and credentials from unauthorized access and store them in a safe location.
