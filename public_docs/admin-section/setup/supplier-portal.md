# Portal de Proveedores

### Activación <a href="#activation" id="activation"></a>

Desde el Panel de Control, selecciona Configuración.

![](../../.gitbook/assets/1\_Dashboard.png)

Procesamiento de Documentos → Módulo

<div align="left">

<figure><img src="../../.gitbook/assets/2_Settings.png" alt="" width="375"><figcaption></figcaption></figure>

</div>

A continuación, activa el Portal de Proveedores habilitando el control deslizante.

<div align="left">

<figure><img src="../../.gitbook/assets/3_Activate_Supplier_Portal.png" alt="" width="375"><figcaption></figcaption></figure>

</div>

Además, también hay controles deslizantes para el Portal de Proveedores con Diseño, así como Campos Adicionales de Invitación para el Portal de Proveedores.

Portal de Proveedores con Diseño: Habilitar esto te permite crear diseños personalizados para el portal de proveedores, lo que significa que puedes personalizar la información requerida según la ubicación geográfica u otros criterios de los proveedores que deseas invitar. Esto se discutirá con más profundidad más adelante.

Campos Adicionales de Invitación para el Portal de Proveedores: Esta opción te permite agregar campos adicionales a la invitación que envías a los proveedores, una lista de campos se pone a tu disposición como se muestra a continuación.

<div align="left">

<figure><img src="../../.gitbook/assets/4_Additional_Fields_List.png" alt="" width="375"><figcaption></figcaption></figure>

</div>

### Configuración de Proveedores <a href="#supplier-settings" id="supplier-settings"></a>

Una vez que se ha habilitado la función del Portal de Proveedores, se vuelve disponible una nueva área de Configuración. Si desplazas hacia abajo en la lista de Configuración, verás lo siguiente.

<div align="left">

<figure><img src="../../.gitbook/assets/5_Supplier_Settings.png" alt="" width="375"><figcaption></figcaption></figure>

</div>

En esta sección, tienes acceso a lo siguiente.

<div align="left">

<figure><img src="../../.gitbook/assets/7_Supplier_Groups_1.png" alt="" width="375"><figcaption></figcaption></figure>

</div>

#### Permisos de Proveedores <a href="#supplier-permissions" id="supplier-permissions"></a>

Aquí es donde puedes gestionar todos los proveedores agrupándolos, facilitando la gestión de todos los proveedores. También se pueden asignar usuarios a los diferentes grupos de proveedores que creas en esta área.

**Grupo de Proveedores**

Para facilitar la gestión de todos los proveedores, en esta sección, puedes crear grupos y asignar proveedores a estos grupos según su ubicación geográfica, tipo de proveedor, etc. ¡La elección es tuya!

<div align="left">

<figure><img src="../../.gitbook/assets/7_Supplier_Groups_1 (2).png" alt="" width="375"><figcaption></figcaption></figure>

</div>

Para crear un nuevo grupo de proveedores, haz clic en el botón +Nuevo en la esquina superior derecha de tu pantalla.

<div align="left">

<figure><img src="../../.gitbook/assets/8_Supplier_Groups_2.png" alt="" width="375"><figcaption></figcaption></figure>

</div>

Luego simplemente asigna a este grupo un nombre que describa con precisión a los proveedores que se asignarán a este grupo.

<div align="left">

<figure><img src="../../.gitbook/assets/9_Supplier_Groups_3.png" alt="" width="375"><figcaption></figcaption></figure>

</div>

**Asignación de Usuario y Grupo de Proveedores**

Todos los grupos de proveedores que has creado se mostrarán aquí, ya que aquí puedes asignar usuarios de DocBits a los grupos de proveedores que creas.

<div align="left">

<figure><img src="../../.gitbook/assets/10_Group_Mapping_1.png" alt="" width="375"><figcaption></figcaption></figure>

</div>

Para asignar un nuevo usuario a un grupo de proveedores, haz clic en el botón +Nuevo y selecciona el usuario que deseas asignar.

<div align="left">

<figure><img src="../../.gitbook/assets/11_Group_Mapping_2.png" alt="" width="375"><figcaption></figcaption></figure>

</div>

Selecciona el usuario que deseas asignar al grupo de proveedores de la lista desplegable y luego haz clic en Agregar para asignar a ese usuario.

#### Política y Declaración de Privacidad <a href="#policy-and-privacy-statement" id="policy-and-privacy-statement"></a>

Aquí es donde puedes subir tu política y declaración de privacidad para los proveedores que invitarás a través del portal de proveedores. Para subir un documento, simplemente haz clic en Subir Documento en la esquina superior derecha de tu pantalla.

<div align="left">

<figure><img src="../../.gitbook/assets/12_Policy_and_Privacy_Statement.png" alt="" width="375"><figcaption></figcaption></figure>

</div>

#### Plantillas de Correo Electrónico <a href="#email-templates" id="email-templates"></a>

En esta sección puedes subir varias plantillas de correo electrónico, ya que estas serán la estructura de los correos electrónicos recibidos por el proveedor cuando lo invites a unirse al portal de proveedores. Las plantillas requeridas incluyen: invitación, aprobación, finalización de registro y rechazo, ya que estos son todos los posibles correos electrónicos que un proveedor podría recibir. Para subir una plantilla, haz clic en +Nuevo.

<div align="left">

<figure><img src="../../.gitbook/assets/13_Email_Templates.png" alt="" width="375"><figcaption></figcaption></figure>

</div>

#### Diseño del Proveedor <a href="#supplier-layout" id="supplier-layout"></a>

Puedes personalizar el diseño del formulario de registro que verán los proveedores que invites al registrarse en el portal de proveedores. Esto significa que puedes agregar o eliminar campos según lo que se requiera de los proveedores que invites. El generador de diseño del proveedor funciona exactamente igual que el generador de diseño del tipo de documento, para más información sobre esto, haz clic [aquí](document-types/layout-builder.md).

A continuación, puedes ver que puedes configurar múltiples diseños según tus necesidades.

<div align="left">

<figure><img src="../../.gitbook/assets/14_Supplier_Layout_1.png" alt="" width="375"><figcaption></figcaption></figure>

</div>

Dentro del diseño, puedes agregar listas desplegables que se pueden crear utilizando la función de [Lista de Valores](../settings/document-processing/list-of-values.md).

<div align="left">

<figure><img src="../../.gitbook/assets/15_Supplier_Layout_2.png" alt="" width="375"><figcaption></figcaption></figure>

</div>

**TEN EN CUENTA**

Solo se pueden usar valores que existan en INFOR en estas listas para que la exportación funcione. En el ejemplo mostrado arriba, los valores seleccionables para el campo "Grupo de Proveedores" existen todos dentro de INFOR. El mismo principio se aplica a todas las listas, ya sea para términos de pago, monedas, etc. Para asegurarte de que no haya problemas al exportar, primero consulta los valores almacenados en INFOR antes de configurar estas listas.

#### Configuración General del Proveedor <a href="#supplier-general-settings" id="supplier-general-settings"></a>

Aquí es donde puedes subir el logotipo de tu empresa o alternativo que se mostrará en el encabezado de todas las plantillas de correo electrónico enviadas, así como en la pantalla de inicio de sesión de DocBits una vez que los proveedores comiencen el proceso de registro. Si se deja vacío, se mostrará el logotipo estándar de DocBits.

#### Configuración de Exportación <a href="#export-configuration" id="export-configuration"></a>

Sube tu API de ION así como tu archivo de mapeo de IDM aquí y tu archivo de mapeo de M3 se generará a la derecha.

<div align="left">

<figure><img src="../../.gitbook/assets/16_Export_Config.png" alt="" width="375"><figcaption></figcaption></figure>

</div>

&#x20;