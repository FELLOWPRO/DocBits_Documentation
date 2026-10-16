---
description: Hashes de contraseñas, almacenamiento de claves API, TLS, acceso a credenciales y recuperación de cuentas en DocBits.
---

# Almacenamiento seguro de credenciales

DocBits trata las contraseñas de inicio de sesión, las claves API de DocBits, la información de las cuentas y las credenciales de sistemas conectados según su finalidad. Esta página explica la protección y la recuperación del acceso en cada caso.

## Contraseñas de inicio de sesión

DocBits almacena las contraseñas de inicio de sesión como **hashes unidireccionales con sal**. La autenticación comprueba la contraseña introducida frente al hash almacenado. La contraseña original no se guarda en un formato que permita descifrarla y recuperarla.

Por tanto, los administradores y el soporte de DocBits no pueden recuperar la contraseña existente en texto claro a partir del hash almacenado. Si un usuario olvida su contraseña, debe restablecerla para volver a iniciar sesión mediante contraseña.

### Restablecer la contraseña

1. Seleccione **¿Has olvidado tu contraseña?** en la pantalla de inicio de sesión.
2. Introduzca la dirección de correo electrónico asociada a la cuenta.
3. Abra el enlace de restablecimiento enviado a esa dirección.
4. Establezca una contraseña nueva e inicie sesión con ella.

Los enlaces de restablecimiento caducan. Si el enlace ha caducado, solicite uno nuevo. El procedimiento establece una contraseña nueva; no revela la anterior. Consulte las instrucciones completas en [Obtener acceso e iniciar sesión](../end-user-and-partner-section/end-user-section/getting-access-and-signing-in.md).

Las cuentas con SSO o una clave de acceso (passkey) configurados pueden utilizar ese método alternativo. En el caso de SSO, el proveedor de identidad gestiona la recuperación de la contraseña. Consulte [Autenticación de dos factores](two-factor-authentication.md).

## Claves API de DocBits

Las claves creadas mediante la **Gestión de claves API** se muestran completas una sola vez, al crearlas. DocBits almacena un hash unidireccional de la clave y un prefijo corto para identificarla. El prefijo y los metadatos siguen visibles en la lista de gestión; la clave original completa no se puede recuperar a partir de su hash.

Ni los administradores ni el soporte de DocBits pueden consultar la clave completa después de su creación. Si pierde una clave, revóquela y cree otra. Cada clave puede tener una fecha de caducidad y puede revocarse por separado. Consulte [Gestión de claves API](../administration-and-setup/settings/global-settings/integration/api-key-management.md).

## Datos de la cuenta y credenciales de sistemas conectados

Los nombres, las direcciones de correo, los roles y el estado de la cuenta son información que los administradores autorizados de la organización pueden consultar y gestionar. Son distintos del secreto utilizado para autenticarse. Consulte [Usuarios](../administration-and-setup/settings/global-settings/groups-users-and-permissions/users/README.md).

Las credenciales de sistemas conectados, como una cuenta de servicio ERP, un buzón o un servidor SFTP, también son distintas de una contraseña de DocBits o una clave API emitida por DocBits. Un conector puede necesitar el secreto utilizable para autenticarse en el sistema externo. Por ello, su almacenamiento y sus controles de acceso deben evaluarse para cada conector.

La imposibilidad de recuperar una contraseña o una clave API de DocBits almacenada como hash **no** significa que toda la información de las cuentas o todos los secretos de integración sean inaccesibles para el proveedor. Cualquier afirmación sobre el acceso del personal a las credenciales de integración requiere confirmar los controles operativos de acceso correspondientes.

## Cifrado en tránsito

Los siguientes puntos de conexión públicos de DocBits admiten **TLS 1.2 y TLS 1.3** mediante HTTPS. Las comprobaciones del **16 de octubre de 2026** confirmaron el rechazo de TLS 1.0 y TLS 1.1.

| Punto de conexión | Finalidad | Versiones TLS verificadas |
| --- | --- | --- |
| `app.docbits.com` | Aplicación web | TLS 1.2 y TLS 1.3 |
| `auth.docbits.com` | Servicio de autenticación | TLS 1.2 y TLS 1.3 |
| `api.docbits.com` | API | TLS 1.2 y TLS 1.3 |

### ¿Qué tipos de cifrado se admiten en tránsito?

| Pregunta | Respuesta para los puntos de conexión públicos anteriores |
| --- | --- |
| ¿Se admite TLS 1.1? | **No.** Se rechazan las conexiones con TLS 1.1. |
| ¿Se admite TLS 1.2? | **Sí.** |
| ¿Se admite TLS 1.3? | **Sí.** |

Los siguientes métodos de cifrado se negociaron correctamente en **los tres puntos de conexión**, en pruebas con validación del certificado realizadas el 16 de octubre de 2026:

| Método de cifrado | Longitud de la clave simétrica | Versiones TLS verificadas |
| --- | --- | --- |
| AES-128-GCM | 128 bits | TLS 1.2 y TLS 1.3 |
| AES-256-GCM | 256 bits | TLS 1.2 y TLS 1.3 |
| ChaCha20-Poly1305 | 256 bits | TLS 1.3 |

Estos métodos proporcionan cifrado autenticado, que protege la confidencialidad y la integridad de los datos en tránsito. El método negociado depende de las capacidades y la configuración del cliente y del servidor. Las longitudes indicadas corresponden a las claves simétricas de cifrado de datos, independientemente del tamaño de las claves de los certificados. Los conjuntos de cifrado TLS 1.2 probados utilizan ECDHE para el intercambio de claves efímeras.

Esta verificación cubre las conexiones a estos puntos de conexión públicos, incluidas las de clientes u otros servidores. No establece la configuración de protocolo o cifrado de cada conexión interna entre servicios, conexión a bases de datos, punto de conexión regional o integración externa. Estas conexiones requieren confirmación para el despliegue y la integración correspondientes.

## Cifrado de la información almacenada de las cuentas

El uso de hashes para contraseñas y claves API es un control distinto del cifrado de bases de datos, volúmenes de almacenamiento, objetos y copias de seguridad. Los controles descritos no demuestran que cada nombre de usuario, campo de cuenta o secreto de integración se cifre individualmente, ni que todos los datos almacenados utilicen un algoritmo de cifrado determinado.

Para un requisito que abarque toda la información de las cuentas de clientes, solicite a FELLOWPRO AG una declaración específica del despliegue sobre los almacenes de datos y las copias de seguridad pertinentes, los métodos de cifrado, la gestión de claves y el acceso del personal. Un modelo de alojamiento en la nube o serverless no demuestra por sí solo estas propiedades.

## Respuesta a un cuestionario de seguridad de un cliente

El siguiente texto describe el alcance confirmado:

> Las contraseñas de DocBits se almacenan como hashes unidireccionales con sal. Los administradores y el soporte de DocBits no pueden recuperar la contraseña original en texto claro a partir del hash almacenado. Quienes olviden su contraseña deben establecer una nueva mediante el procedimiento de restablecimiento por correo electrónico para volver a iniciar sesión con contraseña. SSO o las claves de acceso configurados ofrecen métodos alternativos de inicio de sesión.
>
> Las claves creadas mediante la Gestión de claves API de DocBits se muestran una sola vez y se almacenan como hashes unidireccionales. Ni los administradores ni el soporte de DocBits pueden recuperar la clave completa posteriormente. Las claves perdidas deben revocarse y sustituirse.
>
> Los puntos de conexión públicos de la aplicación web, la autenticación y la API de DocBits indicados anteriormente admiten HTTPS con TLS 1.2 y TLS 1.3; TLS 1.0 y TLS 1.1 se rechazaron en las comprobaciones del 16 de octubre de 2026. Se verificaron AES-128-GCM con 128 bits y AES-256-GCM con 256 bits en TLS 1.2 y TLS 1.3, y ChaCha20-Poly1305 con 256 bits en TLS 1.3. Esta declaración abarca las conexiones a esos puntos de conexión. El cifrado de toda la información almacenada de las cuentas y las copias de seguridad, la protección de cada conexión interna entre servidores y el acceso del personal a las credenciales de integraciones externas requieren confirmación por separado para el despliegue correspondiente.
