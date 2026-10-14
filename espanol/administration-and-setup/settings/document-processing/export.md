# Exportar

## Descripción general

La página de Exportación muestra todas las configuraciones de exportación configuradas, incluyendo si están activas o inactivas. Desde aquí, los usuarios pueden:

* Ver y gestionar las configuraciones de exportación existentes
* Crear nuevas conexiones de exportación (por ejemplo, a **Infor**, **Infor & IDM**, **Webhook** o **SFTP**)
* Editar o eliminar configuraciones de exportación existentes

## Dónde encontrarlo

Puede encontrarlo en: **Configuración** → **Procesamiento de documentos** → **Exportar**

![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/export_settings_menu_access.png)

## **Uso de la página de Exportación**

Cuando abra la página de Exportación, verá una lista de todas las configuraciones de exportación existentes.

Cada fila en la lista muestra:

* **Indicador de estado**
  * **Verde** significa que la exportación está activa
  * **Rojo** significa que la exportación está desactivada
* **Nombre** – el nombre de la configuración de exportación
* **Tipo de documento** – el tipo de documento para el que está configurada la exportación
* **Suborganización** – si la exportación está limitada a una suborganización específica
* **Método de exportación** – dónde se enviará el documento (por ejemplo, Infor, IDM, SFTP)
* **Acciones** – botones para **editar, eliminar** o **activar/desactivar** la configuración

![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/export_list_view.png)

#### **Reglas importantes para la configuración de exportación**

Para cada **tipo de documento** **dentro de una organización o suborganización determinada**, se aplican las siguientes reglas:

* Solo puede tener **una exportación Infor activa**
* Solo puede tener **una exportación no-Infor activa** (por ejemplo, Webhook, SFTP)

Sin embargo, es posible tener:

* **Una exportación Infor activa** _y_ **una exportación no-Infor activa** al mismo tiempo para el mismo tipo de documento
* **Diferentes configuraciones de exportación para diferentes suborganizaciones** — por ejemplo, una exportación Infor para Sub-Org A y otra exportación Infor para Sub-Org B

## **Crear una nueva exportación**

Para crear una nueva exportación:

1. Haga clic en el botón **"Nuevo"**. ![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/export_create_new_button.png)
2. Seleccione el **Tipo de exportación** que desea configurar (por ejemplo, Infor, IDM, SFTP).
3. Complete los campos requeridos según el tipo de exportación.
4. Guarde la configuración.

## Opciones de exportación

#### Webhook

<details>

<summary>Webhook</summary>

![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/export_webhook_configuration.png)

**Descripciones de campos**

* **Title** El nombre de la configuración de exportación. Aparecerá en la lista de exportación.
* **Sub-Organization** _(opcional)_ Un menú desplegable con todas las suborganizaciones disponibles.
  * Si se deja vacío: se aplica a la organización principal.
  * Si se selecciona: la exportación solo se aplicará a la suborganización elegida.
* **Document Type** Menú desplegable que lista todos los tipos de documentos disponibles. Esto determina a qué tipo de documento se aplica esta configuración de exportación.
* **Export URL** La URL de destino donde se debe exportar el documento.

</details>

#### SFTP

<details>

<summary>SFTP</summary>

![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/export_sftp_configuration.png)

**Descripciones de campos**

* **Title** El nombre de la configuración de exportación. Aparecerá en la lista de exportación.
* **Sub-Organization** _(opcional)_ Un menú desplegable con todas las suborganizaciones disponibles.
  * Si se deja vacío: se aplica a la organización principal.
  * Si se selecciona: la exportación solo se aplicará a la suborganización elegida.
* **Document Type** Menú desplegable que lista todos los tipos de documentos disponibles. Esto determina a qué tipo de documento se aplica esta configuración de exportación.
* **Username** El nombre de usuario utilizado para autenticarse en el servidor SFTP.
* **Password** La contraseña correspondiente para la cuenta SFTP. Asegúrese de que la cuenta tenga acceso de escritura a la carpeta especificada.
* **Server URL** El nombre de host o dirección IP del servidor SFTP de destino.
* **Port** El puerto utilizado para conectarse al servidor SFTP.
* **Folder** La ruta en el servidor SFTP donde se deben cargar los documentos (por ejemplo, `/incoming/invoices/`). Debe existir y ser escribible.
*   **XSLT File (Opcional)**

    El **archivo XSLT** permite la transformación del formato de exportación predeterminado de DocBits.

    * **Cuándo usar:** Solo si el sistema receptor requiere una estructura diferente o un formato específico que difiere del predeterminado de DocBits.
    * **Déjelo vacío** si el formato de exportación predeterminado cumple con los requisitos.



**Configuración avanzada:**

* **Filename Export Mode** Especifica si el archivo exportado conserva su nombre de archivo original o se renombra usando el ID de documento de DocBits.
* **Include Document History** Cuando está habilitado, el archivo exportado incluirá el historial del documento basado en los registros disponibles en el panel de control.

![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/export_sftp_2.png)

![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/export_sftp_3.png)

</details>

#### Exportación Infor a SFTP

<details>

<summary>Exportación Infor a SFTP</summary>

![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/export_infor_sftp_configuration.png)

**Descripciones de campos**

* **Title** El nombre de la configuración de exportación. Aparecerá en la lista de exportación.
* **Sub-Organization** _(opcional)_ Un menú desplegable con todas las suborganizaciones disponibles.
  * Si se deja vacío: se aplica a la organización principal.
  * Si se selecciona: la exportación solo se aplicará a la suborganización elegida.
* **Document Type** Menú desplegable que lista todos los tipos de documentos disponibles. Esto determina a qué tipo de documento se aplica esta configuración de exportación.
* **IDM Mapping File** Seleccione un archivo de mapeo del administrador de archivos. [¿Necesita ayuda para crear uno? Ver la Guía de Mapeo IDM](../../../infor-integration-and-configuration/exporting-to-infor/creating-an-idm-mapping-file.md)
* **BOD Mapping File** Seleccione un archivo de mapeo del administrador de archivos. [¿Necesita ayuda para crear uno? Ver la Guía de Mapeo BOD](../../../infor-integration-and-configuration/exporting-to-infor/creating-a-bod-mapping-file.md)
* **Folder** La ruta en el servidor SFTP donde se deben cargar los documentos (por ejemplo, `/incoming/invoices/`). Debe existir y ser escribible.

</details>

#### **SMB**

<details>

<summary>SMB</summary>

![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/export_smb_configuration.png)

**Descripciones de campos**

* **Title** El nombre de la configuración de exportación. Aparecerá en la lista de exportación.
* **Sub-Organization** _(opcional)_ Un menú desplegable con todas las suborganizaciones disponibles.
  * Si se deja vacío: se aplica a la organización principal.
  * Si se selecciona: la exportación solo se aplicará a la suborganización elegida.
* **Document Type** Menú desplegable que lista todos los tipos de documentos disponibles. Esto determina a qué tipo de documento se aplica esta configuración de exportación.
* **Username** El nombre de usuario utilizado para conectarse al recurso compartido SMB.
* **Password** La contraseña correspondiente para la autenticación SMB.
* **Server URL** La dirección del servidor SMB.
* **Port** Número de puerto utilizado para acceder al recurso compartido SMB.
* **Folder** La ruta de la carpeta dentro del recurso compartido SMB donde se deben guardar los documentos (por ejemplo, `/incoming/invoices/`). Debe existir y ser escribible.
*   **JPL Mapping File (Opcional)**

    El **archivo JPL** se utiliza para definir una transformación de los datos exportados antes de que se escriban en el recurso compartido SMB.

    * **Cuándo usar:** Solo cuando los datos del documento exportado necesitan ajustarse para coincidir con el formato externo o las expectativas del sistema.
    * **Déjelo vacío** si no es necesaria ninguna transformación.

</details>

#### **Infor IDM**

<details>

<summary>Infor IDM</summary>

![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/export_infor_idm_configuration.png)

**Descripciones de campos**

* **Title** El nombre de la configuración de exportación. Aparecerá en la lista de exportación.
* **Sub-Organization** _(opcional)_ Un menú desplegable con todas las suborganizaciones disponibles.
  * Si se deja vacío: se aplica a la organización principal.
  * Si se selecciona: la exportación solo se aplicará a la suborganización elegida.
* **Document Type** Menú desplegable que lista todos los tipos de documentos disponibles. Esto determina a qué tipo de documento se aplica esta configuración de exportación.
* **ION Mapping File** Seleccione un archivo de mapeo del administrador de archivos.
* **IDM Mapping File** Seleccione un archivo de mapeo del administrador de archivos. [¿Necesita ayuda para crear uno? Ver la Guía de Mapeo IDM](../../../infor-integration-and-configuration/exporting-to-infor/creating-an-idm-mapping-file.md)
* **Cloud / On-Prem Toggle** Un interruptor para indicar el tipo de implementación de Infor:
  * **Cloud**: Seleccione esto si es cliente de Infor CloudSuite.
  * **On-Prem**: Seleccione esto si Infor está alojado localmente.

</details>

#### **Infor ION**

<details>

<summary>Infor ION</summary>

![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/export_infor_ion_configuration.png)

**Descripciones de campos**

* **Title** El nombre de la configuración de exportación. Aparecerá en la lista de exportación.
* **Sub-Organization** _(opcional)_ Un menú desplegable con todas las suborganizaciones disponibles.
  * Si se deja vacío: se aplica a la organización principal.
  * Si se selecciona: la exportación solo se aplicará a la suborganización elegida.
* **Document Type** Menú desplegable que lista todos los tipos de documentos disponibles. Esto determina a qué tipo de documento se aplica esta configuración de exportación.
* **ION Mapping File** Seleccione un archivo de mapeo del administrador de archivos.
* **BOD Mapping File** Seleccione un archivo de mapeo del administrador de archivos. [¿Necesita ayuda para crear uno? Ver la Guía de Mapeo BOD](../../../infor-integration-and-configuration/exporting-to-infor/creating-a-bod-mapping-file.md)
* **Cloud / On-Prem Toggle** Un interruptor para indicar el tipo de implementación de Infor:
  * **Cloud**: Seleccione esto si es cliente de Infor CloudSuite.
  * **On-Prem**: Seleccione esto si Infor está alojado localmente.

</details>

#### Infor IDM + ION BOD

<details>

<summary>Infor IDM + ION BOD</summary>

![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/export_infor_idm_ion_bod_configuration.png)

**Descripciones de campos**

* **Title** El nombre de la configuración de exportación. Aparecerá en la lista de exportación.
* **Sub-Organization** _(opcional)_ Un menú desplegable con todas las suborganizaciones disponibles.
  * Si se deja vacío: se aplica a la organización principal.
  * Si se selecciona: la exportación solo se aplicará a la suborganización elegida.
* **Document Type** Menú desplegable que lista todos los tipos de documentos disponibles. Esto determina a qué tipo de documento se aplica esta configuración de exportación.
* **ION Mapping File** Seleccione un archivo de mapeo del administrador de archivos.
* **IDM Mapping File** Seleccione un archivo de mapeo del administrador de archivos. [¿Necesita ayuda para crear uno? Ver la Guía de Mapeo IDM](../../../infor-integration-and-configuration/exporting-to-infor/creating-an-idm-mapping-file.md)
* **BOD Mapping File** Seleccione un archivo de mapeo del administrador de archivos. [¿Necesita ayuda para crear uno? Ver la Guía de Mapeo BOD](../../../infor-integration-and-configuration/exporting-to-infor/creating-a-bod-mapping-file.md)
* **Cloud / On-Prem Toggle** Un interruptor para indicar el tipo de implementación de Infor:
  * **Cloud**: Seleccione esto si es cliente de Infor CloudSuite.
  * **On-Prem**: Seleccione esto si Infor está alojado localmente.

</details>

### Para clientes de Infor CloudSuite

#### Infor IDM + LN

<details>

<summary>Infor IDM + LN</summary>

![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/export_infor_idm_ln_configuration.png)

**Descripciones de campos**

* **Title** El nombre de la configuración de exportación. Aparecerá en la lista de exportación.
* **Sub-Organization** _(opcional)_ Un menú desplegable con todas las suborganizaciones disponibles.
  * Si se deja vacío: se aplica a la organización principal.
  * Si se selecciona: la exportación solo se aplicará a la suborganización elegida.
* **Document Type** Menú desplegable que lista todos los tipos de documentos disponibles. Esto determina a qué tipo de documento se aplica esta configuración de exportación.
* **ION Mapping File** Seleccione un archivo de mapeo del administrador de archivos.
* **IDM Mapping File** Seleccione un archivo de mapeo del administrador de archivos. [¿Necesita ayuda para crear uno? Ver la Guía de Mapeo IDM](../../../infor-integration-and-configuration/exporting-to-infor/creating-an-idm-mapping-file.md)
* **LN Mapping File** Seleccione un archivo de mapeo del administrador de archivos. [¿Necesita ayuda para crear uno? Ver el Ejemplo de Mapeo LN](../../../infor-integration-and-configuration/exporting-to-infor/ln/example-export-ln/)

</details>

#### Infor IDM + M3

<details>

<summary>Infor IDM + M3</summary>

![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/export_infor_idm_m3_configuration.png)

**Descripciones de campos**

* **Title** El nombre de la configuración de exportación. Aparecerá en la lista de exportación.
* **Sub-Organization** _(opcional)_ Un menú desplegable con todas las suborganizaciones disponibles.
  * Si se deja vacío: se aplica a la organización principal.
  * Si se selecciona: la exportación solo se aplicará a la suborganización elegida.
* **Document Type** Menú desplegable que lista todos los tipos de documentos disponibles. Esto determina a qué tipo de documento se aplica esta configuración de exportación.
* **ION Mapping File** Seleccione un archivo de mapeo del administrador de archivos.
* **IDM Mapping File** Seleccione un archivo de mapeo del administrador de archivos. [¿Necesita ayuda para crear uno? Ver la Guía de Mapeo IDM](../../../infor-integration-and-configuration/exporting-to-infor/creating-an-idm-mapping-file.md)
* **M3 Mapping File** Seleccione un archivo de mapeo del administrador de archivos. [¿Necesita ayuda para crear uno? Ver el Ejemplo de Mapeo M3](../../../infor-integration-and-configuration/exporting-to-infor/m3/example-export-m3.md)

</details>

#### Infor IDM + M3 (toml)

<details>

<summary>Infor IDM + M3 (toml)</summary>

![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/export_infor_idm_m3_toml_configuration.png)

**Descripciones de campos**

* **Title** El nombre de la configuración de exportación. Aparecerá en la lista de exportación.
* **Sub-Organization** _(opcional)_ Un menú desplegable con todas las suborganizaciones disponibles.
  * Si se deja vacío: se aplica a la organización principal.
  * Si se selecciona: la exportación solo se aplicará a la suborganización elegida.
* **Document Type** Menú desplegable que lista todos los tipos de documentos disponibles. Esto determina a qué tipo de documento se aplica esta configuración de exportación.
* **ION Mapping File** Seleccione un archivo de mapeo del administrador de archivos.
* **IDM Mapping File** Seleccione un archivo de mapeo del administrador de archivos. [¿Necesita ayuda para crear uno? Ver la Guía de Mapeo IDM](../../../infor-integration-and-configuration/exporting-to-infor/creating-an-idm-mapping-file.md)
* **M3 toml Mapping File** Seleccione un archivo de mapeo del administrador de archivos o use la opción seleccionar Toml para usar un toml creado con el gestor de reglas. [¿Necesita ayuda para crear uno? Ver la Guía del Gestor de Reglas](rule-manager/)

</details>
