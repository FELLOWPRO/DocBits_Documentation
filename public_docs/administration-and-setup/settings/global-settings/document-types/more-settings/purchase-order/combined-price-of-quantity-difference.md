<figure><img src="../../../../.gitbook/assets/docbits_combined_price_card.png" alt="DocBits Combined Price Tarjeta" width="563"><figcaption></figcaption></figure>

<figure><img src="../../../../.gitbook/assets/docbits_workflow_compare_two_fields.png" alt="Docbits Workflow Compare Two Fields" width="563"><figcaption></figcaption></figure>

## **Propósito**:

Esta tarjeta de flujo de trabajo evalúa el precio combinado de una diferencia de cantidad, comparándolo con un valor especificado. Ayuda a automatizar acciones basadas en discrepancias de precio y cantidad a través de documentos relacionados, mejorando los flujos de trabajo de adquisición y recepción. La **Versión 4** amplía esta funcionalidad permitiendo comparaciones entre diferentes entidades como la orden de compra, cantidades recibidas y el documento mismo, añadiendo más flexibilidad y control al flujo de trabajo.

## **Componentes de la Tarjeta**:

1. **Operador**:
   * **Descripción:** La condición para comparar el precio combinado con un valor especificado.
   * **Opciones:**
     * **Igual a (=)**: Verifica si el precio combinado coincide con el valor especificado.
     * **No es igual a (≠)**: Asegura que el precio combinado sea diferente del valor especificado.
     * **Mayor que (>)**: Verifica si el precio combinado es mayor que el valor especificado.
     * **Mayor o igual que (≥)**: Verifica si el precio combinado es mayor o igual que el valor especificado.
     * **Menor que (<)**: Verifica si el precio combinado es menor que el valor especificado.
     * **Menor o igual que (≤)**: Verifica si el precio combinado es menor o igual que el valor especificado.
2. **Valor**:
   * **Descripción:** Especifica el valor contra el cual se comparará el precio combinado del valor de la cantidad.
   * **Detalle:** El valor debe ser un valor numérico.

## **Componentes Adicionales en la Versión 4**:

* **Tipo de Comparación**: Selecciona las entidades a comparar. Las opciones incluyen:
  * **Orden de Compra a Documento**: Compara las cantidades y precios entre la orden de compra y el documento relacionado.
  * **Recibido a Documento**: Compara las cantidades recibidas con las cantidades en el documento.
  * **Orden de Compra a Recibido**: Compara las cantidades de la orden de compra con las cantidades recibidas.

## **Funcionalidad**:

* **Evaluación de la Condición**: Calcula el precio combinado multiplicando la diferencia de cantidad por el precio unitario y lo compara con el valor especificado utilizando el operador seleccionado.
  La **Versión 4** añade la opción de comparar entidades adicionales basadas en la configuración del usuario, como orden de compra a recibido u orden de compra a documento.
* **Ejecución de la Acción**: Basándose en si el precio combinado cumple con la condición especificada, el flujo de trabajo continuará con condiciones verdaderas o falsas para activar acciones o detener el flujo de trabajo. La **Versión 4** también permite una ejecución de acciones más dinámica, donde el tipo de condición (por ejemplo, orden de compra a recibido) influye en el siguiente paso.

## **Configuración**:

* **Versión 3**: Los usuarios configuran la tarjeta seleccionando los campos del documento para la diferencia de cantidad y el precio unitario. Luego se elige el operador para definir cómo se comparará el precio combinado con el valor especificado. Finalmente, los usuarios establecen la condición de continuar (verdadero o falso), que dicta el siguiente paso en el flujo de trabajo.
* **Versión 4**: Además de la configuración en la **Versión 3**, los usuarios tienen una opción adicional para configurar el **Tipo de Comparación**. Esto define qué entidades se compararán, como **Orden de Compra a Documento**, **Recibido a Documento** u **Orden de Compra a Recibido**.

## **Escenario de Ejemplo**:

* Una factura muestra 50 unidades de un producto a $100 cada una, totalizando $5000. La orden de compra relacionada autorizó una compra de $4500 para 45 unidades. La diferencia de cantidad es de 5 unidades, y el precio combinado de la diferencia es de $500. La tarjeta compara la cantidad de la orden de compra (45 unidades) con la cantidad recibida (50 unidades) y verifica si el precio combinado es mayor a $400 (el valor especificado). Utilizando el operador **Mayor que (>)**, la tarjeta identifica la discrepancia y la marca para que el equipo de finanzas la revise.

## **Conclusión**:

La **Versión 3** de la tarjeta de flujo de trabajo "Precio Combinado de Diferencia de Cantidad" ofrece un enfoque directo para comparar discrepancias de cantidad y activar acciones basadas en umbrales de precio.
La **Versión 4** amplía esta funcionalidad permitiendo comparaciones entre diferentes entidades (orden de compra, recibido, documento), proporcionando más flexibilidad y control sobre el flujo de trabajo. Las organizaciones ahora pueden automatizar escenarios más complejos y aplicar un control más estricto sobre sus procesos de adquisición y recepción.
