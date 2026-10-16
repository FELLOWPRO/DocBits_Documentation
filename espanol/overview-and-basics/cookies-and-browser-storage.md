# Cookies y almacenamiento del navegador

Revisado el **16 de octubre de 2026** para la pregunta **4.15**. El sitio público, la aplicación DocBits y esta documentación utilizan cookies y servicios diferentes.

## Política y finalidades

La [Política de privacidad de DocBits](https://docbits.com/en/privacy-policy/) contiene los apartados **Cookies** y **Consent with Borlabs Cookie**. Describe el registro del consentimiento, funciones esenciales, protección contra bots, Google Analytics, publicidad y Leadfeeder. Los análisis pueden generar informes sobre visitas, páginas, interacciones y rendimiento; la recopilación no se limita a datos anónimos agregados. La política del sitio no determina por sí sola el inventario de cookies de la aplicación.

## Inventario de cookies

**Observado** indica una visita nueva sin iniciar sesión ni seleccionar consentimientos opcionales. **Código** indica código o configuración de infraestructura revisados; no confirma los atributos de todas las respuestas en producción.

| Cookie / ámbito | Finalidad y duración | Evidencia y atributos de seguridad |
| --- | --- | --- |
| `__cf_bm` / sitio y aplicación | Protección de Cloudflare contra bots; 30 minutos de inactividad | Observado: `Secure`, `HttpOnly`, `SameSite=None`. [Cloudflare](https://developers.cloudflare.com/fundamentals/reference/policies-compliances/cloudflare-cookies/) cifra la información sobre bots, salvo la información temporal. |
| `pll_language` / sitio | Preferencia de idioma; aproximadamente un año | Observado: `Secure`, accesible mediante JavaScript, `SameSite=Lax`. |
| `_lfa` / sitio | Análisis de visitantes y empresas mediante Leadfeeder; aproximadamente un año | Observado: accesible mediante JavaScript, `SameSite=Lax`, **sin atributo `Secure`** en esta visita. |
| Cookie de consentimiento Borlabs / sitio | Guarda consentimientos y retiradas | Declarada en la política; nombre, atributos efectivos y duración no verificados en esta visita. |
| `session` / autenticación | Estado de sesión de los procesos de autenticación | Valores predeterminados del código: `Secure`, `HttpOnly`, `SameSite=None`; sesión Flask firmada, no cifrada. La configuración del despliegue puede sustituirlos. |
| `dbx_td` / autenticación | Recuerda un dispositivo de confianza, si se selecciona tras una MFA correcta; 30 días | Código: `Secure`, `HttpOnly`, `SameSite=None`; token aleatorio cuyo hash se guarda en el servidor. |
| `prod-sticky` / balanceo en producción | Dirige solicitudes al mismo backend; duración configurada de 300 segundos | Configuración de infraestructura verificada; atributos del navegador no verificados. |
| `dontAsk` / aplicación | Recuerda una preferencia sobre un aviso; sin caducidad explícita en la llamada revisada | Código: accesible mediante JavaScript; sin opción explícita `Secure` o `SameSite` en esa llamada. |

No se observaron cookies al visitar la documentación en un contexto nuevo. Es una observación fechada, no un inventario completo de sesiones autenticadas, funciones opcionales o contenido externo. La política enumera otros servicios analíticos y publicitarios cuyas cookies no se confirmaron en esta visita. El inventario completo y la aplicación del consentimiento requieren comprobar esos procesos por separado.

## Seguridad y análisis

`Secure` limita el envío a HTTPS. `HttpOnly` impide la lectura mediante JavaScript. `SameSite` controla el envío entre sitios. Estos atributos no cifran el contenido. No sería correcto afirmar que todas las cookies están cifradas o tienen idéntica protección. Los endpoints públicos admiten TLS 1.2 y 1.3; consulte [Almacenamiento seguro de credenciales](secure-storage-of-credentials.md).

El almacenamiento del navegador también se utiliza independientemente de las cookies. La configuración de Grafana Faro admite seguimiento persistente de sesiones, errores, métricas de rendimiento y trazas, con identificadores de usuario y organización cuando están disponibles. La recopilación depende de la configuración desplegada del colector. No debe describirse como análisis de cookies exclusivamente anónimo y agregado. Las preferencias de idioma también utilizan almacenamiento local.

Puede borrar cookies y almacenamiento desde el navegador; esto puede eliminar preferencias y el reconocimiento de dispositivos de confianza. Para un inventario actualizado o consultas de privacidad: **compliance@fellowpro.com**.
