# Estrategia del ciclo de vida de versiones de DocBits

Con el despliegue de la próxima versión menor R1.1, DocBits introducirá una nueva estrategia de ciclo de vida de versiones basada en dos canales de versiones: VESTA y NOVA.

**NOVA** es el canal para introducir nuevas versiones mayores y menores, como **Rx** y **Rx.y**. **VESTA** continúa proporcionando la versión de producción existente.

{% hint style="success" %}
**Importante: una única URL para VESTA y NOVA**

Continúe utilizando la URL habitual de su aplicación DocBits. VESTA y NOVA no tienen URL de acceso independientes: ambos canales de versiones se utilizan a través de la misma URL estándar que ya emplea para el entorno correspondiente.

Para cambiar de canal, vaya a **Settings > Company Information > Release Channel** y seleccione **VESTA** o **NOVA**. No es necesario cerrar sesión y volver a iniciarla. Su siguiente clic en la aplicación le lleva automáticamente a la versión del canal seleccionado.

Antes de cambiar, compruebe que ambos canales están preparados y disponibles en su entorno, como se explica en [Compruebe la disponibilidad del entorno antes de cambiar](#importante-compruebe-la-disponibilidad-del-entorno-antes-de-cambiar).
{% endhint %}

## Canales de versiones

| Canal | Función en el ciclo de vida |
| --- | --- |
| **VESTA** | Proporciona la versión de producción actual. |
| **NOVA** | Proporciona la próxima versión a medida que avanza por las fases de desarrollo, pruebas y disponibilidad en producción. Durante la producción en paralelo, tanto NOVA como VESTA ofrecen versiones de producción activas. |

## Resumen del ciclo de vida

![Ciclo de vida de versiones de DocBits en tres fases con VESTA y NOVA](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/docbits-release-lifecycle-strategy.png)

Cada ciclo consta de tres fases. Posteriormente, una transición gestionada por FELLOWPRO incorpora la versión de producción de NOVA a VESTA e inicia el siguiente ciclo.

| Fase | VESTA | NOVA | Qué significa para su organización |
| --- | --- | --- | --- |
| **1. Desarrollo** | R1.0.x en producción | R1.1 en desarrollo | Siga utilizando VESTA mientras se prepara la próxima versión. |
| **2. QA y pruebas de aceptación** | R1.0.x en producción | R1.1 en QA y UAT | Evalúe la próxima versión en el entorno sandbox de NOVA mientras el trabajo de producción continúa en VESTA. |
| **3. Producción en paralelo** | R1.0.x en producción | R1.1.x en producción | Permanezca en VESTA o cambie a NOVA de forma independiente cuando esté preparado. |

Tras la transición, todos los clientes utilizan VESTA R1.1.x, y NOVA se reutiliza para el desarrollo de R1.2. La fase 1 comienza de nuevo con estas versiones actualizadas.

### Fase 1 — Desarrollo

VESTA proporciona la versión de producción actual, R1.0.x, mientras la próxima versión, R1.1, se desarrolla en NOVA. Su organización continúa su trabajo diario en VESTA durante toda esta fase.

### Fase 2 — QA y pruebas de aceptación

La próxima versión de NOVA avanza por el aseguramiento de la calidad (QA) y las pruebas de aceptación del usuario (UAT). Usted puede evaluarla en el entorno sandbox de NOVA para valorar cómo se adaptan los cambios a los flujos de trabajo de su organización y prepararse para su adopción.

VESTA R1.0.x sigue siendo la versión de producción durante esta fase. Podrá cambiar a NOVA para su uso en producción una vez que esté disponible en la fase 3.

### Fase 3 — Producción en paralelo

VESTA R1.0.x y NOVA R1.1.x son ambas versiones de producción activas. Su organización decide si cambia a NOVA y cuándo hacerlo, en función de sus necesidades y de los resultados de su evaluación en el entorno sandbox.

Para adoptar NOVA durante esta fase:

1. Evalúe la versión en el entorno sandbox de NOVA.
2. Consulte el anuncio de la versión o confirme con el soporte de FELLOWPRO que ambos entornos de producción están preparados y disponibles para el cambio.
3. Decida cuándo está preparada su organización para utilizar la nueva versión en producción.
4. En DocBits, vaya a **Settings > Company Information > Release Channel** y seleccione **NOVA**.

Durante la producción en paralelo, también puede volver a VESTA yendo a **Settings > Company Information > Release Channel** y seleccionando **VESTA**.

El cambio de canal se realiza en modalidad de autoservicio. FELLOWPRO no selecciona qué clientes deben pasar a NOVA. Puede seguir utilizando VESTA durante toda la producción en paralelo y adoptar la nueva versión mediante la transición posterior.

## Transición de versiones y el siguiente ciclo

FELLOWPRO gestiona la transición una vez que la versión de NOVA está preparada para convertirse en la versión de producción común y se ha obtenido la aceptación de la transición prevista por parte de todos los clientes:

**NOVA R1.1.x → VESTA R1.1.x**

### Anuncio anticipado y aceptación de los clientes

FELLOWPRO anuncia la transición prevista a todos los clientes con antelación por correo electrónico y solicita su aceptación de la transición. Le invitamos a ponerse en contacto con FELLOWPRO para comunicar cualquier inquietud u objeción, de modo que pueda tratarse antes de la transición. La transición y la reutilización de NOVA solo se llevan a cabo una vez que la versión está preparada y todos los clientes han aceptado la transición prevista.

### Qué cambia con la transición

| Cambio | Resultado |
| --- | --- |
| **La versión de NOVA pasa a ser la versión de VESTA** | R1.1.x pasa a ser la versión de producción común en VESTA para todos los clientes. |
| **La versión anterior se retira** | R1.0.x se da de baja y deja de estar disponible a través de cualquiera de los dos canales o por cualquier otro medio. |
| **NOVA se reutiliza para la próxima versión** | El desarrollo de R1.2 comienza en NOVA, lo que inicia la fase 1 del siguiente ciclo. |

A continuación, las mismas tres fases se repiten con los nuevos números de versión.

El siguiente diagrama ilustra con mayor detalle el ciclo de versiones descrito anteriormente.

![Ciclo de versiones detallado de DocBits con VESTA y NOVA](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/docbits-release-lifecycle-strategy-details.png)

### Frecuencia de las versiones

La frecuencia prevista difiere entre las versiones mayores y menores introducidas a través de NOVA y los hotfixes aplicados a las versiones de producción en VESTA y NOVA.

#### Versiones mayores y menores a través de NOVA

FELLOWPRO prevé actualmente un ciclo de aproximadamente **3–4 meses para las versiones mayores y menores** introducidas a través del canal de versiones NOVA, como **Rx** y **Rx.y**. Esta estimación se aplica al ciclo de vida descrito anteriormente, incluida la posterior transición a VESTA y la reutilización de NOVA para la próxima versión. No describe la frecuencia de los hotfixes.

Este intervalo refleja nuestra estimación de planificación actual; no constituye un calendario fijo, una duración máxima del ciclo ni una garantía de fecha de publicación o de transición. El momento de cada transición y de la reutilización de NOVA depende tanto de **que la versión esté preparada como de la aceptación de la transición prevista por parte de todos los clientes**. Si se necesita más tiempo para que la versión esté preparada, para atender las inquietudes de los clientes o para obtener la aceptación de cada uno de ellos, el ciclo se ampliará y podrá durar más de cuatro meses.

FELLOWPRO comunica con antelación cada transición prevista. Cualquier plazo orientativo queda sujeto al cumplimiento de estas condiciones.

#### Hotfixes en la producción de VESTA

Se espera que los hotfixes de la versión de producción de VESTA se publiquen aproximadamente **una vez al mes, o a intervalos algo mayores**. Se trata de una frecuencia orientativa, no de un calendario fijo ni de una fecha de entrega garantizada.

#### Hotfixes de estabilización en la producción de NOVA

No es posible especificar una frecuencia general para los hotfixes de estabilización en la producción de NOVA. NOVA introduce versiones completamente nuevas, por lo que el momento y la frecuencia de estos hotfixes dependen de las necesidades de estabilización de cada versión concreta. Por ello, no siguen la frecuencia mensual orientativa de VESTA ni el ciclo de 3–4 meses de las versiones mayores y menores.

## Responsabilidades y elección del cliente

| Transición | Quién la gestiona | Qué esperar |
| --- | --- | --- |
| **Cambio entre VESTA y NOVA durante la fase 3** | Su organización | Evalúe NOVA en el entorno sandbox y decida si cambia y cuándo hacerlo. Utilice **Settings > Company Information > Release Channel** para seleccionar NOVA o volver a VESTA durante la producción en paralelo. |
| **Transición de NOVA R1.1.x a VESTA R1.1.x** | FELLOWPRO | Revise el anuncio anticipado por correo electrónico, comunique cualquier inquietud u objeción y confirme su aceptación de la transición prevista. FELLOWPRO procede una vez que la versión está preparada y todos los clientes la han aceptado. |

## Importante: compruebe la disponibilidad del entorno antes de cambiar

Cambie entre VESTA y NOVA mediante **Settings > Company Information > Release Channel** únicamente cuando las versiones estén disponibles en paralelo y listas para su uso en el **entorno correspondiente de ambos canales**. La disponibilidad en sandbox y en producción debe evaluarse por separado:

- **Sandbox:** Puede cambiar de VESTA Sandbox a NOVA Sandbox una vez que la nueva versión esté preparada y disponible en NOVA Sandbox, mientras VESTA Sandbox siga disponible. El mismo requisito de disponibilidad se aplica al volver atrás.
- **Producción:** Puede cambiar entre VESTA Production y NOVA Production solo mientras ambas versiones de producción estén preparadas y disponibles en paralelo. La disponibilidad en NOVA Sandbox no significa que NOVA Production esté lista para su uso.

Cambiar cuando el entorno correspondiente no está preparado o disponible puede interrumpir sus operaciones. FELLOWPRO envía correos electrónicos de anuncio de versión unos días antes de que las versiones estén disponibles en sandbox o en producción. Consulte estos anuncios antes de cambiar. Si no está seguro de si un cambio está disponible o es adecuado para su organización, póngase en contacto con el soporte de FELLOWPRO para obtener confirmación.

**Control de disponibilidad previsto:** FELLOWPRO está trabajando en un control Sí/No que permitirá al soporte establecer el ajuste Release Channel como de solo lectura o habilitar el cambio de canal con independencia de un despliegue de software. Cuando este control esté disponible, el soporte lo utilizará para habilitar el cambio cuando los entornos correspondientes estén preparados y para mantener el ajuste en solo lectura en caso contrario. Con ello se pretende que los clientes puedan cambiar de forma segura entre VESTA y NOVA cuando el ajuste esté habilitado. Hasta que se introduzca este control, un ajuste editable por sí solo no debe considerarse una confirmación de que el cambio es adecuado; siga los anuncios de versión o confirme con el soporte.

## Preguntas frecuentes

### ¿Cómo sabemos si es seguro cambiar entre VESTA y NOVA?

Consulte el anuncio de la versión del entorno que desea utilizar o pida al soporte de FELLOWPRO que confirme que el cambio es adecuado. Ambos entornos correspondientes deben estar preparados y disponibles en paralelo; que el sandbox esté preparado no confirma que lo esté producción. Consulte [Importante: compruebe la disponibilidad del entorno antes de cambiar](#importante-compruebe-la-disponibilidad-del-entorno-antes-de-cambiar) más arriba para obtener la guía completa, incluido el control previsto para habilitar o deshabilitar el cambio de canal.

### ¿Podemos permanecer en VESTA mientras NOVA está disponible en producción?

Sí. Durante la fase 3, puede permanecer en VESTA o cambiar a NOVA cuando su organización esté preparada. En la transición posterior, la nueva versión pasa a ser VESTA y la versión anterior se retira.

### ¿Cómo cambiamos a NOVA o volvemos a VESTA?

En primer lugar, compruebe que el entorno correspondiente está preparado y disponible en ambos canales, como se explica en [Compruebe la disponibilidad del entorno antes de cambiar](#importante-compruebe-la-disponibilidad-del-entorno-antes-de-cambiar). La disponibilidad en sandbox y en producción son independientes.

Durante la fase 3, vaya a **Settings > Company Information > Release Channel** en DocBits y seleccione **NOVA** para adoptar la nueva versión de producción, o **VESTA** para volver a la versión de producción actual de VESTA. Su organización toma esta decisión de forma independiente, en función de sus necesidades y de su evaluación de NOVA en el entorno sandbox. Esta elección se aplica mientras ambas versiones estén disponibles en paralelo; la versión anterior de VESTA se retira con la transición.

### ¿Cuándo está disponible NOVA para su uso en producción?

NOVA pasa a ser una versión de producción activa en la fase 3, después del desarrollo y de QA/UAT. Durante esta fase, VESTA y NOVA funcionan en producción en paralelo con distintas versiones del software.

### ¿Cómo nos enteraremos de la transición y podemos presentar objeciones?

FELLOWPRO envía con antelación un correo electrónico a todos los clientes y solicita su aceptación de la transición prevista. Le invitamos a comunicar a FELLOWPRO cualquier inquietud u objeción. La transición y la reutilización de NOVA solo se llevan a cabo una vez que la versión está preparada y se ha obtenido la aceptación de todos los clientes.

### ¿Podemos seguir utilizando R1.0.x después de la transición?

No. R1.0.x se da de baja con la transición y deja de estar disponible a través de cualquiera de los dos canales o por cualquier otro medio. R1.1.x pasa a ser la versión de producción común de VESTA para todos los clientes.

### ¿En qué se diferencia la transición de nuestro cambio a NOVA?

Su cambio a NOVA durante la fase 3 es una decisión de autoservicio sobre cuándo adoptar la nueva versión de producción. La transición es el paso posterior gestionado por FELLOWPRO: NOVA R1.1.x pasa a ser VESTA R1.1.x, la versión anterior se retira y comienza el siguiente ciclo.

### ¿Qué ocurre con NOVA después de la transición?

NOVA se reutiliza para el desarrollo de la próxima versión, R1.2 en este ejemplo. VESTA proporciona R1.1.x mientras NOVA vuelve a avanzar por el desarrollo, QA/UAT y la producción en paralelo.

### ¿Está garantizada una versión mayor o menor cada tres o cuatro meses?

No. La frecuencia aproximada de 3–4 meses para las versiones mayores y menores introducidas a través de NOVA es una estimación de planificación actual, no un calendario garantizado ni una duración máxima. La transición y la reutilización de NOVA requieren tanto que la versión esté preparada como la aceptación de todos los clientes. Si alguna de estas condiciones requiere más tiempo, el ciclo se ampliará y podrá superar los cuatro meses. FELLOWPRO comunica con antelación cada transición prevista.
