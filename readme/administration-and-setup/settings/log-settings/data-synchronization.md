# Comprobar la sincronización de datos

Utilice esta vista cuando falte un proveedor, pedido u otro registro maestro. Muestra la fecha de sincronización registrada por tipo de datos en la organización actual, no el contenido de todos los registros importados.

## Paso a paso

1. Confirme organización, suborganización pertinente y empresa de origen del ERP.
2. Abra **Configuración → Registro de actividad → Sincronización de datos**. Las versiones anteriores la sitúan en la configuración de registros.
3. Localice el tipo en **Data Type** y lea **Last Synchronization Time** con su formato de fecha. Las actualizaciones más recientes aparecen primero.
4. Compare la fecha con el cambio esperado en origen. Una actualización reciente de proveedores no demuestra que los pedidos estén actualizados.
5. Busque el identificador que falta en los datos maestros o pedidos. Compare empresa, número de proveedor/pedido e identificadores de línea con el origen.
6. Revise el canal de importación y sus registros: mensaje de origen, organización de destino, asignación y respuesta. Corrija la causa en la integración; esta vista no dispone de botón para iniciar o reintentar la sincronización.
7. Tras la actualización corregida, recargue la vista y vuelva a abrir la búsqueda o documento. Compruebe la fecha y los valores reales.

## Interpretar el resultado

| Observación | Siguiente comprobación |
| --- | --- |
| Sin filas | Organización, configuración de importación y sincronizaciones registradas. Vacío no significa correcto. |
| Un tipo está desactualizado | Investigue ese flujo independientemente de las demás filas. |
| Aviso de datos antiguos | El aviso actual puede aparecer sin filas o cuando todas las actualizaciones superan dos semanas. Su proceso puede exigir datos mucho más recientes. |
| Fecha reciente y registro ausente | Alcance del origen, identificadores, contenido del mensaje, asignación y respuesta. La fecha no demuestra integridad. |

Para soporte, conserve entorno, organización, tipo de datos, identificador, fecha esperada y error o ID de seguimiento exacto con pruebas pertinentes y anonimizadas.

Consulte [Importar datos maestros](../../../infor-integration-and-configuration/importing-customer-master-data/README.md), [Registro de actividad](README.md) y [Consulta de datos maestros](../document-processing/master-data-lookup.md).
