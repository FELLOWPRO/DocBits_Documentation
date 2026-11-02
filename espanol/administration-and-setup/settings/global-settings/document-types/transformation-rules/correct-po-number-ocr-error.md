# Corregir un error de OCR en un número de pedido

El tercer carácter de `06O123` es la **letra O**. Si la extracción produce `060123`, utilice una transformación condicional de prefijo para corregir este patrón conocido sin un script personalizado.

## Configurar la corrección del prefijo

1. Abra **Configuración → Tipos de documento → engranaje → Reglas de transformación → Administrar reglas de transformación**. Un administrador de la organización debe habilitar la función para el tipo seleccionado.
2. Cree una regla de **campo de cabecera** con **Número de pedido (`Purchase Order`)** como destino. Lea del **propio campo**.
3. En la ejecución condicional, seleccione el número de pedido, **empieza por** y `060`.
4. Elimine el paso inicial de recorte. Añada **Afijo → Quitar prefijo → `060`** y después **Afijo → Añadir prefijo → `06O`**. Introduzca la O mayúscula en el segundo paso. La condición limita ambos pasos al prefijo afectado; los demás caracteres se conservan.
5. Compruebe la vista previa, guarde la regla y vuelva a abrirla. Pruebe un documento, guárdelo y recárguelo para verificar el número de pedido persistido.

## Comprobar el resultado

| Entrada de ejemplo | Resultado esperado | Motivo |
| --- | --- | --- |
| `060123` | `06O123` | Prefijo afectado |
| `060987` | `06O987` | Otro valor afectado; se conserva el sufijo |
| `06O123` | `06O123` | Ya es correcto; la condición no coincide |
| `160123` | `160123` | Prefijo distinto; la condición no coincide |
| `1060123` | `1060123` | `060` dentro del valor no es un prefijo coincidente |

Este ejemplo corrige un patrón de extracción conocido. No demuestra la precisión del OCR, la existencia del pedido ni el éxito de su conciliación. Utilice la regla solo cuando la convención de numeración exija `06O`: también cambiaría un prefijo `060` legítimo. Añada condiciones de proveedor cuando la convención solo corresponda a determinados proveedores.

## ¿Por qué dos pasos de afijo?

El editor actual exige un campo de origen separado para pasos dependientes de la posición, como **Buscar y reemplazar**, incluso con **Ejecutar solo una vez por documento** activado. Los dos pasos de prefijo funcionan sobre el mismo campo. Tras la corrección, el valor ya no empieza por `060`, por lo que la condición evita nuevas modificaciones al guardar de nuevo.
