# Panel de proveedores

## Descripción general

Esta página explica cómo activar y usar el **Panel de proveedores**, así como dónde encontrar todos los ajustes relevantes. El Panel de proveedores te permite invitar a proveedores a **DocBits**. Una vez que se concede el acceso, los proveedores pueden iniciar sesión para ver el estado de sus **Órdenes de compra** y **Facturas** directamente dentro de **DocBits**.

## Cómo activar el Panel de proveedores

1.  Ve a **Ajustes → Procesamiento de documentos → Módulo**.

    ![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/settings_module.png)
2.  En la sección **Envío y proveedor**, habilita la opción **Panel de proveedores**.

    ![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/supplier_portal_1.png)

## Configuración del proveedor

Una vez que la función **Panel de proveedores** está habilitada, aparecerá una nueva sección de **Configuración del proveedor** en la parte inferior del menú **Ajustes**.

![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/settings_suppplier_settings.png)

[**Configuración general del proveedor**](../../settings/supplier-setting/supplier-general-settings.md): Aquí puedes personalizar el **Panel de proveedores** subiendo el logotipo de tu empresa—que se mostrará en el encabezado de todas las plantillas de correo electrónico—y gestionando documentos legales como los Términos de uso y la Política de privacidad.

[**Plantillas de correo electrónico**](../../settings/supplier-setting/editing-email-templates.md)**:** Aquí puedes crear y probar las plantillas de correo electrónico de invitación que se enviarán a los proveedores invitados.

[**Diseño del proveedor**](../../settings/supplier-setting/supplier-layout.md)**:** Aquí puedes crear y gestionar los diseños que definen qué información deben proporcionar los nuevos proveedores durante el proceso de registro.

[**Configuración de exportación**](../../settings/supplier-setting/export-configuration-for-supplier-portal-for-m3.md): Aquí puedes definir cómo se mapean y sincronizan los datos entre el **Panel de proveedores** y el sistema **Infor M3** utilizando archivos de mapeo ION e IDM.

[**Permisos para proveedores**](../../settings/supplier-setting/supplier-permissions.md): Aquí puedes configurar los permisos que tendrán los proveedores dentro del **Panel de proveedores**. También puedes agrupar proveedores, facilitando la gestión del acceso y los ajustes entre múltiples proveedores.

Una guía detallada de todas las configuraciones del proveedor se puede encontrar [aquí](../../settings/supplier-setting/).

## Panel de proveedores <a href="#supplier-permissions" id="supplier-permissions"></a>

Puedes acceder al **Panel de proveedores** desde el menú de la izquierda, como se muestra a continuación.

![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/supplier_portal_2.png)

Todos los proveedores que has creado se muestran aquí.

## Filtrar por proveedores

Puedes buscar proveedores por N**ombre** o N**úmero**, o usar los filtros avanzados para reducir los resultados por:

* **Grupos de proveedores**
* **Estado**
* **Creado el**

También puedes especificar cuántos proveedores deben mostrarse por página.

![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/supplier_portal_9.png)

Además, puedes filtrar rápidamente por los estados **Pendiente de aprobación** o **Registro pendiente** haciendo clic en la categoría correspondiente a la izquierda de la barra de filtros.

![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/10.png)

## Estado del proveedor

Si estás utilizando el **Panel de proveedores**, es importante entender los diferentes estados que pueden tener los proveedores. A continuación se muestra una lista de todos los posibles estados de los proveedores y sus significados:

* **Open**: Proveedor existente que aún no ha sido invitado al panel.
* **Registro pendiente**: El proveedor ha sido invitado pero aún no ha completado el proceso de registro.
* **A la espera de las aportaciones de los proveedores**: El registro está completo, pero se requieren más aportaciones o cambios por parte del proveedor.
* **Pendiente de aprobación**: El proveedor ha completado el registro y está a la espera de la primera aprobación.
* **Pendiente de aprobación de AP**: El proveedor ha recibido la primera aprobación y está a la espera de una segunda aprobación (Cuentas por pagar).
* **Aprobado**: El proveedor ha completado el proceso y ha sido completamente aprobado.
* **Rechazado**: El registro o la aprobación del proveedor ha sido rechazado.

## Herramientas en el Panel de proveedores

A la derecha de la barra de búsqueda, encontrarás varias herramientas que te ayudarán a interactuar y gestionar el panel de manera más eficiente.

### Refrescar tabla <a href="#refresh-table" id="refresh-table"></a>

![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/supplier_portal_3.png)

Haz clic en este botón para refrescar el panel y cargar los datos y estados más actualizados.

### Establecer columnas de tabla para la organización <a href="#set-table-columns-for-organization" id="set-table-columns-for-organization"></a>

![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/supplier_portal_4.png)

Haz clic en este botón para abrir un menú donde puedes gestionar la visibilidad de las columnas en la tabla de órdenes de compra. Usa las casillas de verificación y los botones de flecha para mover columnas entre las secciones visibles y ocultas. También puedes reordenar columnas arrastrando y soltando los nombres de las columnas. Haz clic en **Hecho** para guardar tus cambios.

![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/supplier_portal_7.png)

### Analítica <a href="#analytics" id="analytics"></a>

![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/supplier_portal_5.png)

Hacer clic en este botón abrirá una nueva sección que muestra cuántos proveedores están a punto de expirar y cuándo.\
Haz clic en cualquier categoría para aplicar un filtro y ver solo esos proveedores.

![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/supplier_portal_8.png)

## Crear proveedor y enviar correo electrónico de registro

### **Para crear un nuevo proveedor:**

1.  Haz clic en el ícono de más (+) en la esquina superior derecha.

    ![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/supplier_portal_6.png)
2.  Completa los campos requeridos y luego haz clic en **Guardar**.

    ![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/supplier_portal_11.png)
3. El proveedor recibirá automáticamente un correo electrónico con un enlace para crear su cuenta.

### **Para enviar un correo electrónico de registro a un proveedor existente:**

1. Localiza al proveedor en el **Panel de proveedores**.
2. Haz clic en el menú de tres puntos en la columna de **Comportamiento**.
3.  Selecciona **Magic Link**.

    ![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/supplier_portal_12.png)
4. Verifica los detalles del proveedor.
5.  Haz clic en **Enviar** para enviar el enlace de registro por correo electrónico.

    ![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/supplier_portal_13.png)

## ¿Cómo funciona el proceso de registro para el proveedor?

Después de que se envía un correo electrónico de invitación, el proveedor debe completar el proceso de registro para acceder al **Panel de proveedores**.

Una guía detallada paso a paso sobre el proceso de registro se puede encontrar [aquí](supplier-registration.md).
