# Autenticación de Dos Factores (Admin)

## Descripción general

Como administrador de la organización, puedes **exigir que todos los miembros usen la autenticación de dos factores (2FA)** cuando inicien sesión con una contraseña. Cuando el requisito está activado, un miembro que aún no haya configurado un segundo factor es guiado a través del registro antes de poder terminar de iniciar sesión.

Los inicios de sesión con inicio de sesión único (SSO) — Google, Microsoft, SAML — están **exentos**: su proveedor de identidad ya aplica su propia MFA, por lo que el requisito solo afecta a los inicios de sesión con contraseña.

Esta configuración se encuentra en **Configuración → Configuración Global → Información de la Empresa → Autenticación de dos factores** y está disponible únicamente para los administradores de la organización.

## Exige la MFA para tu organización

1. Ve a **Configuración → Configuración Global → Información de la Empresa**.
2. Abre la sección **Autenticación de dos factores**.
3. Activa **Requerir autenticación de dos factores para todos los miembros** y haz clic en **Guardar**.

<figure><img src="../../../../.gitbook/assets/mfa-admin-requirement.png" alt="The organisation MFA requirement toggle and adoption report"><figcaption><p>Activa el requisito para todos los miembros y supervisa la adopción más abajo.</p></figcaption></figure>

Una vez guardado, el cambio surte efecto en menos de un minuto. A partir de entonces:

* A un miembro **con** un segundo factor se le solicita después de su contraseña, como de costumbre.
* A un miembro **sin** un segundo factor se le exige registrar uno antes de recibir una sesión.
* Los inicios de sesión con SSO / redes sociales no se ven afectados.

{% hint style="warning" %}
Activar esto bloquea los inicios de sesión con contraseña para los miembros que no tienen un segundo factor hasta que completen el registro. Comunica el cambio a tu equipo y considera activarlo fuera de las horas pico.
{% endhint %}

## Informe de adopción de MFA

Debajo del interruptor, el panel de **adopción de MFA** muestra qué tan extendido está el uso de la 2FA en tu organización antes de que la apliques:

* el **porcentaje de adopción** general y una barra de progreso,
* cuántos de tus miembros tienen la 2FA activada (p. ej., *0 de 74 miembros*),
* un desglose por factor: **Autenticador**, **Correo electrónico** y **Clave de acceso**.

<figure><img src="../../../../.gitbook/assets/mfa-adoption-report.png" alt="The MFA adoption report"><figcaption><p>El informe de adopción de MFA: porcentaje general, miembros registrados y un desglose por factor.</p></figcaption></figure>

Úsalo para evaluar la preparación: primero impulsa la adopción y luego activa el requisito con menos miembros bloqueados en el paso de registro.

## Lo que ven los miembros

A un miembro al que se le exige registrarse se le envía a la configuración de 2FA en su próximo inicio de sesión y elige un método (aplicación de autenticación, código por correo electrónico o clave de acceso). Los pasos para el usuario final se describen en [Autenticación de Dos Factores (2FA)](../../../../overview-and-basics/two-factor-authentication.md).

## Controles de seguridad relacionados

El requisito de MFA de toda la organización complementa las protecciones integradas que siempre se aplican una vez que un usuario tiene la 2FA activada: códigos de inicio de sesión de un solo uso, una protección contra reintentos de TOTP, límites de intentos por desafío y por cuenta (una cuenta se bloquea temporalmente tras demasiados intentos fallidos), y la revocación automática de los dispositivos de confianza cuando un miembro cambia su contraseña.
