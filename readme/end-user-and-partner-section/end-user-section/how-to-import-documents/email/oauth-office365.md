# OAuth Office365

{% embed url="https://youtu.be/Vvy38N_5g3Y" %}

Aquí solo necesitas ingresar la suborganización deseada y presionar 'Autenticar'

<figure><img src="../../../../.gitbook/assets/a-email-oauth-office365-authenticate-es-20261009.png" alt="Cuadro de diálogo Configuración del servidor de correo electrónico con el protocolo OAuth Office365, el Enrutamiento de documentos y el botón Autenticar."><figcaption><p>Elige el enrutamiento y presiona Autenticar.</p></figcaption></figure>

Serás llevado a esta página de Microsoft y necesitarás ingresar un código.

Este código se puede encontrar haciendo clic en DocBits y el código se mostrará allí como se muestra a continuación, simplemente copia el código e ingrésalo en la página de Microsoft. Después necesitarás ingresar tus propias credenciales de Microsoft.

<figure><img src="../../../../.gitbook/assets/a-email-oauth-office365-code-es-20261009.png" alt="Cuadro de diálogo Configuración del servidor de correo electrónico con el código de autenticación de Microsoft y el botón Copiar, junto al botón Finalizar la autenticación."><figcaption><p>El código de Microsoft se muestra en DocBits.</p></figcaption></figure>

Presiona el botón **Finalizar la autenticación** y serás llevado a este menú

<figure><img src="../../../../.gitbook/assets/a-email-oauth-office365-options-es-20261009.png" alt="Cuadro de diálogo Configuración del servidor de correo electrónico después de la autenticación, con las opciones Usar carpeta, Usar buzón compartido y Mover correos electrónicos a otra carpeta."><figcaption><p>Opciones después de finalizar la autenticación.</p></figcaption></figure>

**Usar Carpeta**

Si estás usando una carpeta que no sea tu bandeja de entrada, ingresa el nombre de la carpeta después de habilitar el control deslizante.

**Usar Buzón Compartido**

Si deseas que la importación de correos electrónicos acceda a una bandeja de entrada o carpeta de un buzón compartido, ingresa la dirección de correo electrónico aquí después de habilitar el control deslizante.

**Mover correos electrónicos importados a la papelera**

Si deseas importar todos los correos electrónicos, no solo los no leídos, y que se muevan a la papelera, entonces activa esto. De lo contrario, solo revisará los correos electrónicos no leídos, importará los documentos, marcará el correo electrónico como leído y lo dejará en su lugar actual.

En caso de que recibas un mensaje de error que indique que no tienes los derechos para establecer tal conexión, alguien con derechos de administrador dentro de Azure deberá autorizar esta conexión. Para obtener más información, visita la siguiente página: [https://learn.microsoft.com/en-us/entra/identity/enterprise-apps/grant-admin-consent?pivots=portal#grant-tenant-wide-admin-consent-in-enterprise-apps](https://learn.microsoft.com/en-us/entra/identity/enterprise-apps/grant-admin-consent?pivots=portal#grant-tenant-wide-admin-consent-in-enterprise-apps)
