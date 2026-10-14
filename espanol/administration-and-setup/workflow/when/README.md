

Las tarjetas de esta categoría en el selector **Add Card** del Workflow Builder:

<figure><img src="../../../.gitbook/assets/workflow_cards_when.png" alt="Workflow Builder card category"><figcaption><p>Las tarjetas de esta categoría.</p></figcaption></figure>
---
description: Configuración del disparador Cuando en los workflows DocBits
---

# Cuando

![](https://docs.docbits.com/~gitbook/image?url=https%3A%2F%2F578966019-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FT2n2w4uDCJvv7CJ5zrdk%252Fuploads%252FKwAT37pCkZRziNLyWMsL%252Fimage.png%3Falt%3Dmedia%26token%3Db95d040f-e9e6-496d-97cd-d2c8f1c30d60\&width=768\&dpr=4\&quality=100\&sign=c323483b\&sv=2)

#### Comprendiendo el "Cuando" en las Configuraciones de Flujo de Trabajo

**Propósito de "Cuando"**

* La sección "Cuando" en una configuración de flujo de trabajo define las condiciones de activación que inician una acción de flujo de trabajo particular. Estas condiciones se basan en criterios especificados relacionados con atributos de documentos o actividades de usuarios dentro del sistema ERP.

**Cómo Funciona**

* En tu interfaz, "Cuando" parece ser un punto de partida donde los usuarios pueden seleccionar diferentes tarjetas de activación. Cada tarjeta especifica condiciones bajo las cuales se ejecutarán acciones posteriores (definidas en la sección "Y").

**Tarjetas de Condición de Tipo de Documento**

* Las tarjetas con el icono de documento mostradas en la captura de pantalla son variaciones de condiciones de "Tipo de Documento", que se utilizan para activar flujos de trabajo basados en el tipo de documento que se está procesando. Aquí tienes un desglose de cada tipo de tarjeta de condición mostrada:
  * **Tipo de documento (Operador) uno de (Tipo)**: Esta tarjeta activa una acción cuando el tipo de un documento coincide con uno de los tipos especificados en una lista. El operador puede incluir opciones como "es" o "no es", permitiendo condiciones inclusivas o exclusivas.
  * **Tipo de documento (Operador) (Tipo)**: Esta variante más simple se activa en función de una sola condición de tipo de documento. Normalmente verificaría si el tipo de documento "es" o "no es" un tipo específico, sin la opción de seleccionar entre varios tipos.
  *

**Celery Beat**

* La tarjeta con el icono de reloj en la captura de pantalla es una condición de "Celery Beat", que se utiliza para activar flujos de trabajo basados en fecha y hora.

#### Configuración de una Tarjeta de Activación "Cuando"

1. **Selección del Tipo de Condición**: Los usuarios comienzan seleccionando un tipo de condición relevante para el flujo de trabajo que desean automatizar. En este caso, los tipos de documentos son el foco.
2. **Definición del Operador**: Los usuarios deben decidir el operador lógico, como "es" o "no es", que establece la base para comparar los tipos de documentos reales con las condiciones definidas.
3. **Especificación de Tipos de Documento**: Dependiendo de la tarjeta, los usuarios pueden seleccionar uno o varios tipos de documento que activarán el flujo de trabajo cuando se procesen documentos de esos tipos.
4. **Finalización de la Activación**: Una vez que se establece la condición, se convierte en la base para activar acciones específicas definidas en el flujo de trabajo. Si un documento cumple con la condición establecida, las acciones definidas se iniciarán automáticamente.

#### Aplicación Práctica

En la práctica, estas tarjetas de activación son cruciales para automatizar procesos como aprobaciones, notificaciones o cualquier procedimiento que dependa del tipo de documento que se esté manejando. Por ejemplo, si un tipo de documento "es" una "Factura" y coincide con las condiciones establecidas en la tarjeta "Cuando", el flujo de trabajo podría dirigir automáticamente el documento para su procesamiento de pago.

Esta configuración garantiza que los flujos de trabajo no solo sean eficientes, sino también adaptados a las necesidades operativas específicas de la organización, reduciendo la supervisión manual y acelerando los procesos de manejo de documentos.

En resumen, la parte "Cuando" de la configuración de tu flujo de trabajo se trata de establecer el escenario para acciones automatizadas basadas en condiciones específicas y predefinidas. Es una herramienta poderosa para garantizar que tu sistema ERP reaccione dinámicamente a las necesidades del negocio, mejorando tanto la productividad como la precisión en la gestión de documentos.
