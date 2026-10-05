---
description: Configurar el inicio de sesión único (SSO) de DocBits con un proveedor de identidad SAML.
---

# Configuración de inicio de sesión único (SSO)

Configurar el SSO en DocBits requiere unos pocos pasos de preparación y configuración. Esta es una guía paso a paso:

**Acceso a los ajustes de SSO:**

* Inicie sesión en su cuenta de DocBits como administrador.
* Vaya a **Ajustes** y abra **Integración y SSO**.

**Configuración de los parámetros de SSO:**

![Pantalla actual de Integración y SSO de DocBits en la organización de prueba Sandbox en español, con la ID de entidad del proveedor de servicios, la URL SSO, la URL SLO y las descargas del certificado y de los metadatos.](../../../../../.gitbook/assets/dbdc-336-infor-v2-sso-settings-es.png)

* Introduzca los parámetros de SSO necesarios, como la ID de entidad, la URL de cierre de sesión único (SLO) y la URL de inicio de sesión único (SSO).
* La ID de entidad es un identificador único de su servicio o aplicación.
* La URL SLO es la URL que se usa para el cierre de sesión único y desconecta a los usuarios de todos los servicios cuando es necesario.
* La URL SSO es la URL que redirige a los usuarios al proveedor de servicios de identidad para la autenticación.

**Descarga de certificados y metadatos:**

* El proveedor de servicios de identidad (IdP) suele proporcionar un certificado que DocBits usa para verificar la respuesta de autenticación SAML.
* Descargue el certificado con **Descargar certificado** y guárdelo de forma segura.
* La descarga de metadatos (**Descargar metadatos**) contiene toda la información de configuración necesaria para la integración SSO, como la ID de entidad, la URL SSO, la información del certificado y más.
* Descargue los metadatos y guárdelos localmente o facilítelos al proveedor de servicios de identidad.

**Configuración del proveedor de servicios de identidad (IdP):**

* Inicie sesión en el proveedor de servicios de identidad y configure la aplicación o el servicio para la integración SAML.
* Use los metadatos descargados o los parámetros de SSO introducidos manualmente para añadir DocBits como aplicación o servicio de confianza.
* Asegúrese de que la configuración del IdP coincide con los parámetros de SSO especificados en DocBits.
* En la sección **Configuración del proveedor de servicios de identidad**, introduzca el **ID de inquilino**, suba el archivo de metadatos del IdP con **Subir archivo** y seleccione **Configurar**.

**Prueba de la integración SSO:**

* Una vez completada la configuración, pruebe la integración SSO para comprobar que los usuarios pueden iniciar sesión en DocBits mediante SSO.
* Verifique también que el cierre de sesión único funciona correctamente: cierre sesión en DocBits y compruebe que también se cierra en los demás servicios conectados.

Guías detalladas por proveedor: [Configuración SSO de Infor](sso-configuration/README.md) con las páginas [V1](sso-configuration/v1.md), [V2](sso-configuration/v2.md) y [Azure SSO](sso-configuration/azure-sso.md).

Una configuración correcta del SSO permite a los usuarios iniciar sesión en DocBits con sus credenciales existentes, lo que mejora la experiencia de usuario y aumenta la seguridad.
