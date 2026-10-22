# Solución de problemas habituales

Estos son los pasos de resolución de problemas para los incidentes habituales al integrar DocBits con un Identity Service Provider (IdP) u otros servicios:

* **Verifique la configuración:** asegúrese de que los ajustes de integración en DocBits estén configurados correctamente y coincidan con los requisitos de su Identity Service Provider. En particular, compruebe la SSO URL, el Entity ID y los certificados.
* **Supervise los registros:** supervise los registros tanto en DocBits como en el Identity Service Provider para identificar mensajes de error o advertencias. Estos registros pueden dar pistas sobre dónde se encuentra el problema.
* **Verifique las conexiones de red:** asegúrese de que no haya problemas de red que puedan afectar a la comunicación entre DocBits y su Identity Service Provider. Compruebe la configuración del firewall, las configuraciones de DNS y las reglas de acceso a la red.
* **Pruebe los procesos de SSO:** realice inicios de sesión de prueba mediante Single Sign-On (SSO) para asegurarse de que los usuarios se autentican correctamente y son redirigidos a DocBits. Anote cualquier mensaje de error o problema de redirección.
* **Compruebe los permisos:** asegúrese de que los usuarios de DocBits tengan los permisos necesarios para acceder a las funciones o recursos correspondientes. Revise la asignación de grupos y roles.
* **Actualice los certificados:** asegúrese de que los certificados SAML y los metadatos estén actualizados en ambos lados. Si un certificado ha caducado, debe actualizarlo y volver a probar la integración.
* **Póngase en contacto con el soporte:** si no puede identificar la causa del problema, póngase en contacto con el soporte de DocBits o con su proveedor de identidad. Pueden ayudarle a resolver el problema y ofrecerle orientación específica para su configuración.

Si sigue estos pasos de resolución de problemas, podrá identificar y resolver rápidamente los problemas más comunes durante la integración entre DocBits y su identity service provider.
