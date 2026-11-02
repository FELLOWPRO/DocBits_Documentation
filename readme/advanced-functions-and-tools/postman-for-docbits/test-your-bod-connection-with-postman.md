# Prueba tu conexión BOD con Postman

## Visión general

Esta página explica cómo verificar el procesamiento exitoso de tu BOD (Documento de Objeto de Negocio) utilizando Postman. Probarás el endpoint de API relevante enviando una solicitud con tu archivo de mapeo de BOD. Sigue los pasos a continuación para completar el proceso.

## Accediendo a tu Clave API y Archivo de mapeo de BOD

### Recuperando tu Clave API

1.  Ve a **Ajustes → Ajustes globales → Integración y SSO**.

    ![Página de ajustes en DocBits con la navegación Global Settings abierta e Integrations & SSO resaltado entre Document Types y Email Templates](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/settings_integration.png)
2.  Puedes copiar manualmente tu **clave API** o hacer clic en el botón de copiar para copiarla en tu portapapeles.

    ![Página Integration & SSO en DocBits que muestra el campo API Key con su botón de copiar encima de la sección SSO Service Provider Settings](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/test_bod_connection_postman_1.png)

### **Descargando el Archivo de mapeo de BOD**

1.  Ve a **Ajustes → Procesamiento de documentos → Exportar**.

    ![Página de ajustes en DocBits con la navegación Document Processing abierta, que muestra Import, OCR Settings, Classification and Extraction y Module](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/settings_export.png)
2.  En la columna de **Comportamiento** de la entrada de exportación relevante, haz clic en el menú de tres puntos y selecciona **Editar**.

    ![Página de Export settings en DocBits con las filas google Invoice webhook e Infor LN Test Invoice y el menú Actions abierto](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/test_bod_connection_postman_2.png)
3.  Localiza el **Archivo de mapeo de BOD** y haz clic en el botón **Descargar** para guardarlo.

    ![Diálogo de Infor ION con el campo Title Test y los botones de descarga de ION-Mapping File, IDM Mapping File y BOD-Mapping File](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/test_bod_connection_postman_3.png)

## Prueba el Endpoint en Postman

1.  **Pega el comando cURL en Postman**

    Abre Postman y pega el siguiente comando cURL en la sección **Import**. Postman configurará automáticamente la solicitud.

    ```bash
    curl -X 'POST' \
      'https://api.docbits.com/prod-api/import/purchase_order_bod' \
      -H 'accept: application/json' \
      -H 'X-API-KEY:' \
      -H 'Content-Type: multipart/form-data' \
      -F 'org_id=' \
      -F 'sub_org_id=' \
      -F 'file=@file.xml;type=text/xml' \
      -F 'custom_fields_mapping='
    ```

    ![Espacio de trabajo de Postman con la pantalla de bienvenida, la pestaña History y la opción Create a new request](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/test_bod_connection_postman_4.png)

    ![Diálogo Import de Postman con el campo de pegado de cURL abierto para importar la solicitud BOD](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/test_bod_connection_postman_5.png)
2.  **Configura la Clave API**\
    Ve a la pestaña **Headers**, localiza el encabezado `X-API-KEY` y pega tu clave API en la columna **Value**.

    ![Solicitud de Postman para https://api.docbits.com/prod-api/import/purchase_order_bod con la pestaña Headers y la fila X-API-KEY](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/test_bod_connection_postman_6.png)
3.  **Sube el archivo BOD**\
    Ve a la pestaña **Body**, localiza la clave `file`, luego haz clic en **Select Files** en la columna **Value** y sube tu archivo BOD XML.

    ![Pestaña Body de la petición de Postman con las claves form-data org_id, sub_org_id, file con Select Files y custom_fields_mapping](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/test_bod_connection_postman_7.png)
4.  **Envía la solicitud**\
    Haz clic en **Send** para realizar la llamada a la API.

    ![Solicitud de Postman con la pestaña Authorization abierta y No Auth seleccionado](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/test_bod_connection_postman_8.png)
5.  **Verifica la respuesta**\
    Revisa la respuesta para confirmar que tu BOD fue procesado exitosamente.

    ![Panel de respuesta de Postman con estado 200 OK y el mensaje del cuerpo BOD processed successfully](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/test_bod_connection_postman_9.png)
