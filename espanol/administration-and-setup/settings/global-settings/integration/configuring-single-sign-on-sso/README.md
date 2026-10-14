# Configuración de inicio de sesión único (SSO)

Configurar el inicio de sesión único (SSO) en DocBits requiere unos pocos pasos de preparación y configuración. Esta es una guía paso a paso:

**Acceso a los ajustes de SSO:**

<figure><img src="../../../../../.gitbook/assets/image (82).png" alt=""><figcaption></figcaption></figure>

* Inicie sesión en su cuenta de DocBits como administrador.
* Vaya a los ajustes y busque Single Sign-On o SSO.

**Configuración de los parámetros de SSO:**

<figure><img src="../../../../../.gitbook/assets/image (79).png" alt=""><figcaption><p>Ajustes del proveedor de servicios SSO</p></figcaption></figure>

* Introduzca los parámetros de SSO necesarios, como la ID de entidad, la URL de cierre de sesión único (SLO) y la URL de inicio de sesión único (SSO).
* La ID de entidad es un identificador único de su servicio o aplicación.
* La URL SLO es la URL que se usa para el cierre de sesión único y desconecta a los usuarios de todos los servicios cuando es necesario.
* La URL SSO es la URL que redirige a los usuarios al proveedor de identidad para la autenticación.

**Descarga de certificados y metadatos:**

<figure><img src="../../../../../.gitbook/assets/image (80).png" alt=""><figcaption></figcaption></figure>

* El proveedor de identidad (IdP) suele proporcionar un certificado que DocBits usa para verificar la respuesta de autenticación SAML.
* Descargue el certificado y guárdelo de forma segura.
* La descarga de metadatos contiene toda la información de configuración necesaria para la integración SSO, como la ID de entidad, la URL SSO, la información del certificado y más.
* Descargue los metadatos y guárdelos localmente o facilítelos al proveedor de identidad.

**Configuración del proveedor de identidad (IdP):**

<figure><img src="../../../../../.gitbook/assets/image (81).png" alt=""><figcaption><p>Ajustes del proveedor de servicios de identidad</p></figcaption></figure>

* Inicie sesión en el proveedor de identidad y configure la aplicación o el servicio para la integración SAML.
* Use los metadatos descargados o los parámetros de SSO introducidos manualmente para añadir DocBits como aplicación o servicio de confianza.
* Asegúrese de que la configuración del IdP coincide con los parámetros de SSO especificados en DocBits.

**Prueba de la integración SSO:**

* Una vez completada la configuración, pruebe la integración SSO para comprobar que los usuarios pueden iniciar sesión en DocBits mediante SSO.
* Verifique también que el cierre de sesión único funciona correctamente: cierre sesión en DocBits y compruebe que también se cierra en los demás servicios conectados.

Una configuración correcta del SSO permite a los usuarios iniciar sesión en DocBits con sus credenciales existentes, lo que mejora la experiencia de usuario y aumenta la seguridad.
