# Si el país está en el campo

<figure><img src="../../../../.gitbook/assets/workflow-card-qa-20261021-card-70b0b5860da5-es.png" alt="Campos de la tarjeta en la versión mostrada. Los campos aún no están configurados." width="563"><figcaption><p>Campos de la tarjeta en la versión mostrada. Los campos aún no están configurados.</p></figcaption></figure>

Utilice esta condición cuando un paso de procesamiento adicional deba depender de un grupo de países. El ejemplo comprueba si el país de un campo del documento pertenece a la Unión Europea.

**Ubicación:** Flujo estándar → condiciones adicionales (AND) → Campo del documento. Configure la acción posterior por separado en THEN.

## Configuración — versión 2

| Ajuste | Valor |
| --- | --- |
| Campo | Un campo de texto existente que contenga el nombre del país |
| Operador | `is` |
| Región | Unión Europea (UE) |
| Valor de continuación | `true` |

<!-- workflow-card-practical-example-20261021 -->

## Ejemplo práctico

| Valor del país en el campo | Condición esperada |
| --- | --- |
| `Germany` | Se cumple |
| `United States` | No se cumple |

Los nombres de países mostrados como código son valores de entrada fijos para este ejemplo.

## Límites y comprobaciones

`false` no invierte la comparación. Con ese ajuste, ni siquiera un país coincidente produce una condición positiva. Para comprobar la condición contraria, seleccione `isnot` con `true`.

Gestione por separado los campos ausentes y los valores de país vacíos; pueden devolver un resultado de datos faltantes en lugar de una falta de coincidencia normal.

La revisión del código fuente de la versión de desarrollo del 22 de octubre de 2026 muestra un error de conversión para entradas ISO como `DE` y `DEU`. Por eso, estos ejemplos utilizan nombres de países completos. Compruebe por separado el tratamiento de códigos ISO en su versión instalada.

Los grupos disponibles, incluidos UE, Schengen y NAFTA, proceden de la implementación de la tarjeta. Compruebe qué países incluye su versión antes de utilizar un grupo en una regla de negocio.
