# Iniciar una carga inicial de proveedores desde Infor M3

Use este procedimiento solo después de que su administrador de Infor haya confirmado la empresa, la división, el BOD `SupplierPartyMaster` y la ruta de ION de DocBits. Una carga inicial sin restricciones puede enviar todos los proveedores aptos, por lo que conviene acordar primero una selección reducida. Las once capturas de Infor M3 que aparecen a continuación son ejemplos históricos; compárelas con su propio entorno antes de ejecutar un trabajo. Esta actualización de la página no ejecutó ningún trabajo de M3 ni importó proveedores en DocBits.

Infor documenta el [procedimiento de carga inicial EVS006](https://docs.infor.com/m3core/latest/en-us/useradminlib_cloud/m3cecoreag_cloud/hmo1553266924239.html) y las [opciones de selección y ejecución de EVS007](https://docs.infor.com/m3udi/16.x/en-us/m3beud/appfoundhs/spl1567531742751.html). Si las etiquetas son distintas en su entorno, siga el procedimiento aprobado por su administrador.

* [ ] Abra Infor OS y la aplicación M3 con una cuenta autorizada para cargas iniciales. Confirme la empresa y la división previstas antes de continuar.

<figure><img src="../../../.gitbook/assets/6cf93500-2e90-4cfc-a9fb-5873e5dcb953.png" alt="Pantalla de inicio de Infor M3 con el menú de módulos a la izquierda y la lista Recientes con EVS006 Initial Load y BOD Processor Administration"><figcaption><p>Ejemplo histórico: pantalla de inicio de Infor M3 con EVS006 Initial Load y BOD Processor Administration en la lista Recientes.</p></figcaption></figure>

* [ ] Abra **Initial Load. Open (EVS006)** con la búsqueda de programas de su entorno.

<figure><img src="../../../.gitbook/assets/f77b242e-eb2f-43b6-8a2e-03d264198e0c.png" alt="Cuadro de diálogo Search and Start de Infor M3 con el campo de entrada vacío y el botón OK"><figcaption><p>Ejemplo histórico: cuadro de diálogo Search and Start de Infor M3 con su campo de entrada y el botón OK.</p></figcaption></figure>

* [ ] En EVS006, cree una definición de carga inicial para **SupplierPartyMaster**. El ejemplo histórico usa **CIDMAS** como tabla. Pida al administrador de M3 que confirme si esa combinación de BOD y tabla es válida en su versión y en su integración.

<figure><img src="../../../.gitbook/assets/827a9dbb-c974-4da7-9bd3-f8e87adad60f.png" alt="Cuadro de diálogo Search and Start con el valor evs006 escrito en el campo de entrada"><figcaption><p>Ejemplo histórico: Search and Start con EVS006 escrito en el campo de entrada.</p></figcaption></figure>

<figure><img src="../../../.gitbook/assets/e30c7b86-dcfb-41d2-bd32-447b60e4581b.png" alt="Lista Initial Load de EVS006 con el sustantivo BOD SupplierPartyMaster y la tabla CIDMAS ya rellenados"><figcaption><p>Ejemplo histórico: lista Initial Load de EVS006 con SupplierPartyMaster como sustantivo BOD y CIDMAS como tabla.</p></figcaption></figure>

* [ ] Seleccione **Create** y revise la definición antes de continuar.

<figure><img src="../../../.gitbook/assets/30eee6b2-24ed-4e1f-8812-1304e7dede8e.png" alt="Lista de EVS006 con el botón Create de la barra de herramientas resaltado en rojo"><figcaption><p>Ejemplo histórico: lista de EVS006 con el botón Create de la barra de herramientas resaltado.</p></figcaption></figure>

<figure><img src="../../../.gitbook/assets/461b72d3-d576-4c92-95c2-d175183088af.png" alt="Panel de creación de EVS006 para la tabla CIDMAS con el campo de descripción BOD todavía vacío"><figcaption><p>Ejemplo histórico: panel de creación de EVS006 para CIDMAS con el campo de descripción BOD aún vacío.</p></figcaption></figure>

* [ ] Introduzca una **BOD Description** clara, por ejemplo **SupplierPartyMaster initial load for DocBits**.

<figure><img src="../../../.gitbook/assets/4dc345a8-8eca-4e03-800a-37a670f8792e.png" alt="Panel de creación de EVS006 con la descripción BOD establecida en SupplierPartyMaster"><figcaption><p>Ejemplo histórico: panel de creación de EVS006 con SupplierPartyMaster escrito como descripción BOD.</p></figcaption></figure>

* [ ] Seleccione **Next** y defina la selección acordada cuando esté disponible. Infor recomienda usar criterios de selección para no generar demasiados eventos.

<figure><img src="../../../.gitbook/assets/315aa54b-f0bd-4057-a1ed-e476c9000725.png" alt="Panel de creación de EVS006 con el botón Next resaltado en la esquina inferior derecha"><figcaption><p>Ejemplo histórico: panel de creación de EVS006 con el botón Next resaltado.</p></figcaption></figure>

* [ ] Continúe con la configuración de la ejecución. Revise de nuevo la empresa, la división y la selección.

<figure><img src="../../../.gitbook/assets/c0ff3fe1-a393-43cc-96a5-3e0cb1d878b7.png" alt="Cuadro de diálogo de texto en EVS006 con campos de bloque de texto vacíos y el botón Next"><figcaption><p>Ejemplo histórico: cuadro de diálogo de texto de EVS006 con los campos de bloque de texto y el botón Next.</p></figcaption></figure>

* [ ] En la definición de SupplierPartyMaster, elija **Related → Run**. Se abre **Initial Load Job. Open (EVS007)**; esto todavía no demuestra que DocBits haya recibido los datos.

<figure><img src="../../../.gitbook/assets/d819fdd5-5b4a-48ef-9412-f211c0d2355f.png" alt="Lista de EVS006 con el menú contextual abierto sobre la fila SupplierPartyMaster y la opción Related > Run"><figcaption><p>Ejemplo histórico: lista de EVS006 con el menú Related → Run abierto sobre la fila SupplierPartyMaster.</p></figcaption></figure>

* [ ] Elija **Sync** solo si el flujo de ION receptor espera Sync.SupplierPartyMaster. Confirme los filtros y el destino antes de enviar EVS007. Una carga inicial completa puede generar muchos eventos.

<figure><img src="../../../.gitbook/assets/m3-supplier-initial-load-job-historical-id-masked-20261102.png" alt="Trabajo Initial Load Job de EVS007 para CIDMAS y SupplierPartyMaster con el verbo BOD Sync y el estado 1-Pending"><figcaption><p>Ejemplo histórico: Initial Load Job de EVS007 con CIDMAS, SupplierPartyMaster, Sync y el estado 1-Pending. El identificador del trabajo está oculto; el estado pendiente no demuestra una importación completada.</p></figcaption></figure>

## Verificar el resultado

Después de una ejecución autorizada, compruebe **Related → History** en EVS006 para ver el número de registros procesados y los posibles errores. A continuación, verifique el mensaje de SupplierPartyMaster en Infor ION y confirme que llegó a la organización de DocBits configurada. Solo entonces busque un proveedor concreto en DocBits en **Ajustes → Búsqueda de datos maestros → Proveedor**. Utilice el campo de búsqueda y el número o el nombre del proveedor; no dé por hecho que todos los proveedores de M3 han llegado solo porque se haya enviado el trabajo.

<figure><img src="../../../.gitbook/assets/m3-supplier-master-data-es-20261112.png" alt="DocBits Sandbox 11.27.7: Ajustes, Búsqueda de datos maestros con la pestaña Proveedor, el campo Búsqueda por columna y el campo Buscar Cadena; las filas SUP-1001 a SUP-1010 son datos de ejemplo inventados"><figcaption><p>DocBits Sandbox 11.27.7: Ajustes → Búsqueda de datos maestros con la pestaña Proveedor, el campo Búsqueda por columna y el campo Buscar Cadena. Las filas SUP-1001 a SUP-1010 son datos de ejemplo inventados y no demuestran ninguna importación desde M3.</p></figcaption></figure>

La captura muestra datos de ejemplo inventados que ya existían en el entorno de pruebas Test A. Durante esta actualización de la documentación no había ningún entorno de M3 conectado. Si el proveedor esperado no aparece, compare el historial de EVS006, el enrutamiento de ION y la organización de DocBits antes de repetir la carga. En esta tabla, la aplicación todavía muestra algunos encabezados de columna en inglés, como Supplier Id y Supplier Name; son etiquetas de la interfaz y no forman parte de la guía.

### Alternativa: Panel de proveedores

Si utiliza el portal de proveedores, los proveedores importados también aparecen en **Panel De Proveedores**, porque ambas vistas leen los mismos datos maestros de proveedores. Busque por nombre o número de proveedor en el campo **Búsqueda por nombre, número**. El acceso y el registro en ese portal se describen en la [guía del Portal de proveedores](../../../administration-and-setup/setup/supplier-portal/README.md).

<figure><img src="../../../.gitbook/assets/m3-supplier-management-search-es-20261112.png" alt="DocBits Sandbox 11.27.7: Panel De Proveedores con las pestañas Todos los proveedores (8), Pendiente de aprobación (2) y Registro pendiente (2), el campo Búsqueda por nombre, número y ocho filas de ejemplo inventadas"><figcaption><p>DocBits Sandbox 11.27.7: Panel De Proveedores con el campo Búsqueda por nombre, número y las pestañas de estado. Las ocho filas, sus números y sus nombres son datos de ejemplo inventados y no demuestran ninguna importación desde M3. Los estados de la columna Estado Del Proveedor siguen apareciendo en inglés (approved, pending_approval, pending_registration, open, rejected).</p></figcaption></figure>
