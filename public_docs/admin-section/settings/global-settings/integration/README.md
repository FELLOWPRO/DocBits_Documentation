# Integración

<figure><img src="../../../../.gitbook/assets/Bildschirmfoto 2024-05-08 um 08.39.14.png" alt=""><figcaption></figcaption></figure>

## Clave de API

* **Clave**: Este es el identificador único utilizado por aplicaciones externas para acceder a la API de Docbits. Es crucial para autenticar las solicitudes realizadas a Docbits desde otro software.
* Se pueden realizar acciones como ver, regenerar o copiar la clave de API aquí, dependiendo de las necesidades específicas y los protocolos de seguridad.

## Configuración del Proveedor de Servicios SSO (Inicio de Sesión Único)

* **ID de Entidad**: Este es el identificador de Docbits como proveedor de servicios en la configuración de SSO. Identifica de manera única a Docbits dentro del marco de SSO.
* **URL de Cierre de Sesión Única (SLO)**: La URL a la que se envían las sesiones de SSO para cerrar la sesión simultáneamente en todas las aplicaciones conectadas a través de SSO.
* **URL de SSO**: La URL utilizada para iniciar el proceso de inicio de sesión único.
* Se pueden realizar acciones como "Descargar Certificado" y "Descargar Metadatos" para obtener los certificados de seguridad necesarios e información de metadatos utilizada en la configuración y mantenimiento de la integración de SSO.

{% hint style="info" %}
Ver [Configuración de SSO](../../../setup/sso-configuration/)
{% endhint %}

## Configuración del Proveedor de Servicios de Identidad

* **ID de Inquilino**: Esto puede ser utilizado cuando Docbits se integra con servicios en la nube que requieren un identificador de inquilino para gestionar datos y configuraciones de acceso específicas de la empresa que utiliza Docbits.
* **Subir archivo**: Permite al administrador subir archivos de configuración u otros archivos necesarios que faciliten la integración con un proveedor de identidad.
* **Configurar**: Un botón para aplicar o actualizar la configuración después de realizar cambios o subir nuevas configuraciones.
