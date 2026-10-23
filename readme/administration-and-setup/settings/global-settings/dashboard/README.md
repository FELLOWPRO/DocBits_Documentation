# Panel

## Resumen

Los ajustes del Panel están diseñados para ayudar a los administradores a controlar la presentación de datos y la interacción dentro del panel de DocBits. Estos ajustes determinan qué información está disponible de inmediato al iniciar sesión, asegurando que los usuarios tengan acceso rápido a los datos más relevantes para sus tareas.

![Lista de documentos en italiano con el rango de nombres de documento de Delivery Note, Advance Ship Notice y Purchase Order y 2373 documentos en total](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/dashboard_settings_1.png)

## Accediendo a los Ajustes del Panel

Para acceder a los ajustes del panel, navega a:\
**Ajustes → Ajustes globales → Panel**

![Configuración general del dashboard en italiano con las opciones de restablecimiento de filtros tras la carga de documentos, el reinicio y la exportación](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/settings_dashboard.png)

## **General**

* **Restablecer filtros**: Permite la configuración de cuándo deben restablecerse los filtros del panel, como después de la carga de documentos, reinicio de documentos o exportación de documentos. Esto ayuda a mantener un lienzo limpio para la visualización de datos según las etapas específicas del flujo de trabajo.
* **Datos del tablero**:
  * **Cargar automáticamente el tablero de instrumentos**: Controla si el panel debe cargar automáticamente los datos al acceder el usuario, lo que puede ayudar a reducir los tiempos de carga y mejorar la experiencia del usuario al cargar datos solo cuando sea necesario.
  *   **Exportar datos del cuadro de mandos**: Esta función añade un nuevo botón de **Exportar** a la barra de herramientas del panel, permitiéndote exportar la vista actual del panel como un archivo **.csv** o **.xlsx**.

      ![Sección General de la configuración del dashboard con los interruptores Reset filters y las opciones de Dashboard data Auto refresh dashboard on document updates y Export Dashboard Data](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/dashboard_settings_3.png)

## **Historial de exportaciones**

En el **Historial de exportaciones**, verás una tabla que lista todas las exportaciones pasadas junto con información clave sobre cada solicitud.

![Sección Export History en la página de configuración del Dashboard con las columnas Email, Status, Requested At, Completed At, Format y Filters Used](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/dashboard_settings_4.png)

Los siguientes detalles están incluidos:

* **Correo electrónico**: La dirección de correo electrónico desde la cual se solicitó la exportación.
* **Estado**: El estado actual de la exportación (Pendiente, Completado).
* **Solicitado en**: La fecha y hora en que se inició la exportación.
* **Completado en**: La fecha y hora en que se completó la exportación.
* **Formato**: El formato de archivo utilizado para la exportación (CSV, XLSX).
* **Filtros utilizados**: Cualquier filtro que se aplicó al panel en el momento de la exportación.

<mark style="color:red;">**Nota**</mark>: Para exportar tablas, la opción Exportar datos del cuadro de mandos en la sección [General](./#general) debe estar activa.

## **Acción**

* **Asignar a**: Esta función permite a los usuarios definir permisos para la asignación de documentos.
  * **Solo para Admin**: Solo los usuarios administradores pueden asignar documentos, independientemente de los permisos otorgados a los usuarios no administradores.
  * **Todos los Usuarios**: Todos los usuarios que han recibido los [permisos](../groups-users-and-permissions/groups-and-permissions/activating-permissions.md) necesarios pueden asignar documentos.
* **Reanudar**: Esta función permite a los usuarios definir permisos para reiniciar documentos.
  * **Solo para Admin**: Solo los usuarios con privilegios de Admin pueden reiniciar documentos, independientemente de los permisos otorgados a los usuarios no administradores.
  * **Solo Admin y Asignado**: Solo los usuarios con privilegios de Admin y el usuario asignado pueden reiniciar el documento.
  * **Todos los Usuarios**: Todos los usuarios que han recibido los [permisos](../groups-users-and-permissions/groups-and-permissions/activating-permissions.md) necesarios pueden reiniciar documentos.

![Sección Action en la página de configuración del dashboard con Assign to y Restart configurados ambos en Only for Admin](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/dashboard_settings_2.png)

## **Filtros**

* **Estilo de filtro de estado**: Determina el estilo de presentación de los filtros de estado, que se puede establecer como predeterminado o personalizado según el enfoque operativo de los usuarios.
* **Filtro de estado personalizado**: Permite la creación y aplicación de filtros personalizados que pueden dirigirse a estados de documentos específicos como "Nuevo", "Validando" o "Exportando". Esto permite a los usuarios acceder rápidamente a documentos en etapas específicas de procesamiento.

![Página de configuración del dashboard que muestra la sección Filters con Status filter style y Custom status filter más la sección Advance Shipment Dashboard](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/dashboard_settings_5.png)

## Cuadro de mandos de envíos anticipados

* **Visibilidad de pedidos entregados**: Esta función permite al usuario especificar la duración durante la cual los pedidos entregados serán visibles.

![Sección Advance Shipment Dashboard en la página de configuración del dashboard con Delivered Orders Visibility establecido en 14 Days](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/dashboard_settings_6.png)

Estos ajustes del panel son cruciales para garantizar que la plataforma DocBits sea lo más receptiva y útil posible, proporcionando a los usuarios una herramienta poderosa para monitorear y gestionar actividades de procesamiento de documentos directamente desde el panel.
