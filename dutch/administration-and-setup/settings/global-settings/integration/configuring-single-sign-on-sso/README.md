# Configuring Single Sign-On (SSO)

Configuring Single Sign-On (SSO) in DocBits requires a few steps to set up and configure. Here is a step-by-step guide:

**Accessing SSO settings:**

<figure><img src="../../../../../.gitbook/assets/docbits_sso_access_settings.png" alt="Docbits Sso Access Settings"><figcaption></figcaption></figure>

* Log in to your DocBits account as an administrator.
* Navigate to settings and look for Single Sign-On or SSO.

**Configuring SSO parameters:**

<figure><img src="../../../../../.gitbook/assets/docbits_sso_config_params.png" alt="Docbits Sso Config Params"><figcaption><p>SSO Service Provider Settings</p></figcaption></figure>

* Enter the required SSO parameters such as the Entity ID, Single Log-Out (SLO) URL, and Single Sign-On (SSO) URL.
* The Entity ID is a unique identifier for your service or application.
* The SLO URL is the URL used for Single Log-Out to log users out of all services when needed.
* The SSO URL is the URL that will redirect users to the Identity Provider for authentication.

**Download certificates and metadata:**

<figure><img src="../../../../../.gitbook/assets/docbits_sso_cert_metadata.png" alt="Docbits Sso Cert Metadata"><figcaption></figcaption></figure>

* The identity provider (IdP) typically provides a certificate that DocBits uses to verify the SAML authentication response.
* Download the certificate and store it securely.
* The metadata download contains all the necessary configuration information for SSO integration. This includes information such as the entity ID, SSO URL, certificate information, and more.
* Download the metadata and store it locally or provide it to the identity provider.

**Identity provider (IdP) configuration:**

<figure><img src="../../../../../.gitbook/assets/docbits_sso_idp_config.png" alt="Docbits Sso Idp Config"><figcaption><p>Identity Service Provider Settings</p></figcaption></figure>

* Log in to the identity provider and configure the application or service for SAML integration.
* Use the downloaded metadata or the manually entered SSO parameters to add DocBits as a trusted application or service.
* Make sure the IdP's configuration matches the SSO parameters specified in DocBits.

**Testing SSO integration:**

* After the configuration is complete, perform a test of the SSO integration to ensure that users can successfully log in to DocBits using SSO.
* Also, verify that Single Log-Out is working properly by logging out of DocBits and ensuring that you are logged out of other connected services as well.

Setting up SSO properly allows users to seamlessly log in to Docbits using their existing credentials, improving the user experience and increasing security.
