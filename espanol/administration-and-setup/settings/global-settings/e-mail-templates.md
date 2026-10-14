# Plantillas de correo electrónico

## **Visión general**

Las plantillas de correo electrónico le permiten personalizar las notificaciones por correo electrónico automatizadas enviadas desde DocBits. Las plantillas pueden incluir campos dinámicos (por ejemplo, `{{FieldID}}`), imágenes y formato HTML.

## **Acceso a las plantillas de correo electrónico**

1.  Navega a: **Configuración → Configuración global → Plantillas de correo electrónico**

    ![](https://docs.docbits.com/~gitbook/image?url=https%3A%2F%2F578966019-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FT2n2w4uDCJvv7CJ5zrdk%252Fuploads%252FWzjaI1Jinpw0PQHCuwM0%252Fimage.png%3Falt%3Dmedia%26token%3D21f7af41-6ebe-4e25-952f-9ae0b11cade2\&width=768\&dpr=4\&quality=100\&sign=ae789081\&sv=2)
2. El panel muestra todas las plantillas con:
   * **Nombre**
   * **Asunto**
   * Fecha de **Última modificación**
   * **Acciones** (Editar o Eliminar).

![](https://docs.docbits.com/~gitbook/image?url=https%3A%2F%2F578966019-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FT2n2w4uDCJvv7CJ5zrdk%252Fuploads%252FENN4zipGg75mpi2OooPP%252Fimage.png%3Falt%3Dmedia%26token%3Ddff6d8a8-e5b3-4e52-bee1-e311daba7b64\&width=768\&dpr=4\&quality=100\&sign=4202a84f\&sv=2)

## **Creación de una nueva plantilla**

### **1 Configuración básica**

* Haz clic en **Nuevo**.
* Completa los campos a la derecha:
  * **Nombre**: Identificador de la plantilla (por ejemplo, "Error de documento").
  * **Asunto**: Línea de asunto del correo electrónico (por ejemplo, "Acción requerida: Error de documento").
  *   **Tipo de documento**: Selecciona del menú desplegable (por ejemplo, "Factura").

      ![](https://docs.docbits.com/~gitbook/image?url=https%3A%2F%2F578966019-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FT2n2w4uDCJvv7CJ5zrdk%252Fuploads%252FXzmfZBIoyoDS7tTz1qo4%252Fimage.png%3Falt%3Dmedia%26token%3D24547984-2406-41b5-95d6-0f7f45e06258\&width=768\&dpr=4\&quality=100\&sign=f7aa9b89\&sv=2)

### **2 Editor de plantillas**

* **Menú**: Formatea texto, agrega enlaces o inserta tablas.
* **Editor HTML**: Haz clic en el icono `<>` para editar HTML en bruto.
* **Agregar imágenes**: Utiliza la función **Subir**.
*   **Campos dinámicos:** Inserta valores de campo de documento mediante

    * **Opción de campo variable**: Selecciona de un menú desplegable.
    * **Entrada manual**: Escribe `{{FieldID}}` (por ejemplo, `{{NumeroFactura}}`).

    ![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/email_templates_4.png)

### **3 Guardar**

* Haz clic en **Guardar** para almacenar la plantilla.

## **Envío de un correo electrónico de prueba**

1.  Abre la plantilla y haz clic en **Enviar prueba**.

    ![](https://docs.docbits.com/~gitbook/image?url=https%3A%2F%2F578966019-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FT2n2w4uDCJvv7CJ5zrdk%252Fuploads%252FZTskZNsVfWj6IwBmwoR5%252Fimage.png%3Falt%3Dmedia%26token%3D62229942-2ee7-4d58-833c-eb863b18f2d3\&width=768\&dpr=4\&quality=100\&sign=b804f787\&sv=2)
2. Ingresa:
   * **Correo electrónico del destinatario** (obligatorio).
   * **Valores de campo** (opcional; datos simulados para marcadores de posición). ![](https://docs.docbits.com/~gitbook/image?url=https%3A%2F%2F578966019-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FT2n2w4uDCJvv7CJ5zrdk%252Fuploads%252FO2yw8EgefTPSCIhxUFH6%252Fimage.png%3Falt%3Dmedia%26token%3D2acc0067-3698-4565-92d8-6c4ddabe497c\&width=300\&dpr=4\&quality=100\&sign=461ae8e7\&sv=2)
3. Revisa el correo electrónico de prueba y ajusta la plantilla si es necesario.

## **Uso de plantillas en notificaciones**

Las plantillas guardadas pueden vincularse a flujos de trabajo de [**Notificación por correo electrónico**](../supplier-setting/) (por ejemplo, recordatorios de aprobación, actualizaciones de estado).
