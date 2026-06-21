# Clave de API

<figure><img src="https://lh7-us.googleusercontent.com/ulCymk1gu-de14qTaFfJwTEmAUp7DY000A40P3nTgRIb7pYXolCbh_GPJvRib5haIH75dPFewY5tJQ0xNbGP3wdSOgCxu7gdVBwlvxkHFcP_3HM3R15zuuBOZM2jEdFxlp2CpV1VDfktmLFSSw4BuLs" alt=""><figcaption></figcaption></figure>

### Clave de API

* **Clave:** Es el identificador único que utilizan las aplicaciones externas para acceder a la API de DocBits. Es fundamental para autenticar las solicitudes que se realizan a DocBits desde otro software.
* Aquí se pueden realizar acciones como ver, regenerar o copiar la clave de API, según las necesidades específicas y los protocolos de seguridad.

### Configuración del proveedor de servicios SSO (Single Sign-On)

* **Entity ID:** Es el identificador de DocBits como proveedor de servicios en la configuración de SSO. Identifica de forma única a DocBits dentro del marco de SSO.
* **URL de SLO (Single Logout):** La URL a la que se envían las sesiones de SSO para cerrar la sesión simultáneamente en todas las aplicaciones conectadas a través de SSO.
* **URL de SSO: La URL** utilizada para iniciar el proceso de inicio de sesión único.
* Aquí están disponibles acciones como "Descargar certificado" y "Descargar metadatos" para obtener los certificados de seguridad y la información de metadatos necesarios que se utilizan para configurar y mantener la integración de SSO.

{% hint style="info" %}
Consulte Configurar SSO
{% endhint %}

### Configuración del proveedor de servicios de identidad

* Tenant ID: Esto puede utilizarse cuando DocBits se integra con servicios en la nube que requieren un identificador de inquilino para gestionar los datos y las configuraciones de acceso específicas de la empresa que utiliza DocBits.
* Cargar archivo: Permite al administrador cargar archivos de configuración u otros archivos necesarios que facilitan la integración con un proveedor de identidad.
* Configurar: Un botón para aplicar o actualizar la configuración después de realizar cambios o cargar nuevas configuraciones.