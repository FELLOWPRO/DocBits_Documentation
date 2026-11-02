# Configuración del proveedor de servicios de identidad

Configurar el Identity Service Provider (IdP) para integrarlo con DocBits requiere algunos pasos específicos. Esta es una guía para hacerlo:

<figure><img src="../../../../.gitbook/assets/image (83).png" alt=""><figcaption></figcaption></figure>

**Acceder a la interfaz de configuración del IdP**

* Inicie sesión en su Identity Service Provider (IdP) como administrador.
* Navegue a la interfaz de ajustes o configuración dedicada a la gestión de integraciones SAML.

**Introducir el Tenant ID:**

* Busque la sección que permite configurar nuevas integraciones SAML.
* Introduzca el tenant ID de DocBits. Este ID identifica su cuenta de DocBits ante el IdP y permite una comunicación segura entre ambos sistemas.

**Importar los archivos necesarios:**

* DocBits normalmente requiere descargar metadatos o añadir detalles de configuración específicos. Consulte la documentación de su IdP para saber qué pasos son necesarios.
* Descargue el archivo de metadatos de DocBits o impórtelo en el menú de configuración de su IdP. Como alternativa, puede introducir manualmente los detalles de configuración necesarios, según lo que admita su IdP.

**Configurar los ajustes de la integración:**

* Asegúrese de que los ajustes de la integración, como la SSO URL, el Entity ID y el certificado SAML, sean correctos.
* Compruebe que la Single Log-Out (SLO) URL y los demás parámetros necesarios estén configurados correctamente. Son fundamentales para una autenticación y un cierre de sesión fluidos mediante SAML.

**Verificar la configuración:**

* Dedique tiempo a asegurarse de que toda la información introducida sea correcta y de que no haya errores tipográficos ni de configuración.
* Realice pruebas para garantizar que los usuarios puedan iniciar sesión correctamente en DocBits mediante SAML y que Single Log-Out funcione correctamente.

**Consideraciones de seguridad:**

* Asegúrese de que todos los archivos transferidos y los detalles de configuración se gestionen de forma segura para evitar fugas de datos o accesos no autorizados.
* Proteja la información sensible, como los certificados SAML y las credenciales, frente a accesos no autorizados y almacénela en un lugar seguro.
