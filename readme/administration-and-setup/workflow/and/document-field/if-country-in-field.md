# Si el país está en el campo

<figure><img src="../../../../.gitbook/assets/workflow_card_condition_field_country_code_continue_v2-es-es.png" alt="Si el país está en el campo, Versión 2" width="634"><figcaption><p>Versión 2</p></figcaption></figure>

Uso previsto: un paso de procesamiento adicional depende de un grupo de países. El siguiente ejemplo describe una regla de pertenencia a la Unión Europea.

## Limitación actual — código fuente revisado el 22 de octubre de 2026

Las pruebas locales del código fuente con el tipo nativo de la selección de región fallan antes de comparar el país y devuelven `missing_variable` o `error`. Los nombres completos de países no evitan este problema. No se ha verificado una ejecución correcta en el backend desplegado para esta versión.

**Ubicación:** Flujo estándar → condiciones adicionales (AND) → Campo del documento. Configure la acción posterior por separado en THEN.

## Configuración — versión 2

| Ajuste | Valor |
| --- | --- |
| Campo | Un campo de texto existente que contenga el nombre del país |
| Operador | `is` |
| Región | Unión Europea (UE) |
| Valor de continuación | `true` |

<!-- workflow-card-practical-example-20261021 -->

## Ejemplo previsto — compruebe la corrección antes de usarlo

Compruebe la corrección y ambos casos del ejemplo en su versión instalada antes de activar esta regla. La tabla describe la regla de negocio prevista, no una ejecución correcta confirmada.

| Valor del país en el campo | Agrupación de países prevista |
| --- | --- |
| `Germany` | Dentro de la UE |
| `United States` | Fuera de la UE |

Los nombres de países mostrados como código son valores de entrada fijos para este ejemplo.

## Límites y comprobaciones

`false` no invierte la comparación. Con ese ajuste, ni siquiera un país coincidente produce una condición positiva. Para comprobar la condición contraria, seleccione `isnot` con `true`.

Gestione por separado los campos ausentes y los valores de país vacíos; pueden devolver un resultado de datos faltantes en lugar de una falta de coincidencia normal.

El problema de conversión ISO para entradas como `DE` y `DEU` es independiente. Sustituir los códigos ISO por nombres completos de países no resuelve el error de selección de región.

Los grupos disponibles, incluidos UE, Schengen y NAFTA, proceden de la implementación de la tarjeta. Compruebe qué países incluye su versión antes de utilizar un grupo en una regla de negocio.
