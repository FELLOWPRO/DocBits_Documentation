# Estrategia del ciclo de vida de versiones de DocBits

DocBits utiliza dos canales de versiones, **VESTA** y **NOVA**, para introducir nuevas versiones y dar a su organización tiempo para evaluarlas antes de adoptarlas. Durante la producción en paralelo, usted decide si cambia a la nueva versión y cuándo hacerlo. A continuación, FELLOWPRO gestiona la transición (rollover) que la convierte en la versión de producción común para todos los clientes.

Los números de versión de esta guía (R1.0.x, R1.1.x y R1.2) son ilustrativos. El mismo ciclo de vida se repite con las versiones sucesivas; `x` representa las actualizaciones dentro de una serie de versiones.

## Canales de versiones

| Canal     | Función en el ciclo de vida                                                                                                                                                                                               |
| --------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **VESTA** | Proporciona la versión de producción actual.                                                                                                                                                                              |
| **NOVA**  | Proporciona la próxima versión a medida que avanza por las fases de desarrollo, pruebas y disponibilidad en producción. Durante la producción en paralelo, tanto NOVA como VESTA ofrecen versiones de producción activas. |

## Resumen del ciclo de vida

![Ciclo de vida de versiones de DocBits en tres fases con VESTA y NOVA](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/docbits-release-lifecycle-strategy.png)

Cada ciclo consta de tres fases. Posteriormente, una transición gestionada por FELLOWPRO incorpora la versión de producción de NOVA a VESTA e inicia el siguiente ciclo.

| Fase                              | VESTA                | NOVA                 | Qué significa para su organización                                                                           |
| --------------------------------- | -------------------- | -------------------- | ------------------------------------------------------------------------------------------------------------ |
| **1. Desarrollo**                 | R1.0.x en producción | R1.1 en desarrollo   | Siga utilizando VESTA mientras se prepara la próxima versión.                                                |
| **2. QA y pruebas de aceptación** | R1.0.x en producción | R1.1 en QA y UAT     | Evalúe la próxima versión en el entorno sandbox de NOVA mientras el trabajo de producción continúa en VESTA. |
| **3. Producción en paralelo**     | R1.0.x en producción | R1.1.x en producción | Permanezca en VESTA o cambie a NOVA de forma independiente cuando esté preparado.                            |

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
2. Decida cuándo está preparada su organización para utilizarla en producción.
3. Cambie de VESTA a NOVA mediante el ajuste **Release Channel** de la aplicación DocBits.

Este cambio se realiza en modalidad de autoservicio. FELLOWPRO no selecciona qué clientes deben pasar a NOVA. Puede seguir utilizando VESTA durante toda la producción en paralelo y adoptar la nueva versión mediante la transición posterior.

## Transición de versiones y el siguiente ciclo

FELLOWPRO gestiona la transición una vez que la versión de NOVA está preparada para convertirse en la versión de producción común y se ha obtenido la aceptación de la transición prevista por parte de todos los clientes:

**NOVA R1.1.x → VESTA R1.1.x**

### Anuncio anticipado y aceptación de los clientes

FELLOWPRO anuncia la transición prevista a todos los clientes con antelación por correo electrónico y solicita su aceptación de la transición. Le invitamos a ponerse en contacto con FELLOWPRO para comunicar cualquier inquietud u objeción, de modo que pueda tratarse antes de la transición. La transición y la reutilización de NOVA solo se llevan a cabo una vez que la versión está preparada y todos los clientes han aceptado la transición prevista.

### Qué cambia con la transición

| Cambio                                                | Resultado                                                                                                             |
| ----------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------- |
| **La versión de NOVA pasa a ser la versión de VESTA** | R1.1.x pasa a ser la versión de producción común en VESTA para todos los clientes.                                    |
| **La versión anterior se retira**                     | R1.0.x se da de baja y deja de estar disponible a través de cualquiera de los dos canales o por cualquier otro medio. |
| **NOVA se reutiliza para la próxima versión**         | El desarrollo de R1.2 comienza en NOVA, lo que inicia la fase 1 del siguiente ciclo.                                  |

A continuación, las mismas tres fases se repiten con los nuevos números de versión.

El siguiente diagrama ilustra con mayor detalle el ciclo de versiones descrito anteriormente.

![Ciclo de versiones detallado de DocBits con VESTA y NOVA](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/docbits-release-lifecycle-strategy-details.png)

### Frecuencia de las versiones

FELLOWPRO prevé actualmente un ciclo de versiones de aproximadamente **3–4 meses**. Este intervalo refleja nuestra estimación de planificación actual; no constituye un calendario fijo, una duración máxima del ciclo ni una garantía de fecha de publicación o de transición.

El momento de cada transición y de la reutilización de NOVA depende tanto de **que la versión esté preparada como de la aceptación de la transición prevista por parte de todos los clientes**. Si se necesita más tiempo para que la versión esté preparada, para atender las inquietudes de los clientes o para obtener la aceptación de cada uno de ellos, el ciclo se ampliará y podrá durar más de cuatro meses.

FELLOWPRO comunica con antelación cada transición prevista. Cualquier plazo orientativo queda sujeto al cumplimiento de estas condiciones.

## Responsabilidades y elección del cliente

| Transición                                   | Quién la gestiona | Qué esperar                                                                                                                                                                                                                                     |
| -------------------------------------------- | ----------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Cambio de VESTA a NOVA durante la fase 3** | Su organización   | Evalúe NOVA en el entorno sandbox y decida si cambia y cuándo hacerlo mediante el ajuste Release Channel de la aplicación.                                                                                                                      |
| **Transición de NOVA R1.1.x a VESTA R1.1.x** | FELLOWPRO         | Revise el anuncio anticipado por correo electrónico, comunique cualquier inquietud u objeción y confirme su aceptación de la transición prevista. FELLOWPRO procede una vez que la versión está preparada y todos los clientes la han aceptado. |

## Preguntas frecuentes

### ¿Podemos permanecer en VESTA mientras NOVA está disponible en producción?

Sí. Durante la fase 3, puede permanecer en VESTA o cambiar a NOVA cuando su organización esté preparada. En la transición posterior, la nueva versión pasa a ser VESTA y la versión anterior se retira.

### ¿Cómo cambiamos a NOVA?

Una vez que NOVA esté disponible en producción, utilice el ajuste **Release Channel** de la aplicación DocBits. Su organización toma esta decisión de forma independiente, en función de sus necesidades y de su evaluación de la versión en el entorno sandbox de NOVA.

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

### ¿Está garantizada una nueva versión cada tres o cuatro meses?

No. La frecuencia aproximada de 3–4 meses es una estimación de planificación actual, no un calendario garantizado ni una duración máxima. La transición y la reutilización de NOVA requieren tanto que la versión esté preparada como la aceptación de todos los clientes. Si alguna de estas condiciones requiere más tiempo, el ciclo se ampliará y podrá superar los cuatro meses. FELLOWPRO comunica con antelación cada transición prevista.
