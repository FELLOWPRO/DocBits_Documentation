# Guía de diagnóstico de exportación de la API M3

### 1. Configuración inicial

Antes de comenzar a solucionar problemas, asegúrese de estar familiarizado con las entradas esperadas para el punto final de M3 con el que está trabajando.

#### 1.1 Acceder a la documentación de la API de M3

* Inicie sesión en **M3**.
* Vaya a **Sección de API → Documentación de la API**.
* Localice y seleccione el punto final relevante (por ejemplo, `APS450MI` para exportaciones relacionadas con facturas).
* Elija la función apropiada (por ejemplo, `Add`).

#### 1.2 Comprender los requisitos de la API

* Revise todos los **campos requeridos** en la documentación de la API.
* Preste atención a campos importantes como:
  * `DIVI`
  * `ACDT` (fecha contable)
  * `CUCD` (código de moneda)
  * `SINO` (número de factura del proveedor)
* Confirme los **tipos de datos** de los campos, **mayúsculas y minúsculas**, y las **reglas de formato** (por ejemplo, `AAAA-MM-DD` para fechas).

### 2. Pruebas de llamadas a la API directamente en M3

Este paso verifica que la API de M3 se comporte según lo esperado utilizando entradas manuales.

#### 2.1 Generar una solicitud de prueba en M3

* En la herramienta de Documentación de la API de M3:
  * Complete los datos de prueba para los campos requeridos.
  * Haga clic en **Ejecutar** para ejecutar la solicitud.
  * Copie el **cURL** resultante y el **cuerpo JSON**.

#### 2.2 Depurar usando Postman

* Abra **Postman** y cree una nueva solicitud **POST**.
* Pegue el cuerpo JSON o cURL.
* Agregue encabezados necesarios (por ejemplo, autorización).
* Haga clic en **Enviar** y observe el resultado:
  * `200 OK`: La solicitud fue exitosa.
  * Error: Revise el mensaje para obtener detalles sobre lo que salió mal.

### 3. Comparar la API de M3 con la asignación de DocBits

Una vez que haya confirmado que la API funciona con datos de prueba, compárelo con lo que DocBits está enviando realmente.

#### 3.1 Exportar datos de muestra desde DocBits

*   Abra la **documentación de la API de DocBits**:

    Utilice el punto final **/export/get\_infor\_export\_api\_json**.
* Ingrese el **ID del documento** de un documento problemático.
* Ejecute la exportación para ver la **carga JSON** que DocBits enviará a M3.

#### 3.2 Comparar las cargas de la API

* Coloque el **JSON de prueba de M3** y el **JSON de exportación de DocBits** uno al lado del otro.
* Verifique:
  * **Nombres de campo**: Asegúrese de que los nombres coincidan _exactamente_, incluyendo mayúsculas (`DIVI` ≠ `divi`).
  * **Tipos de datos**: Verifique que las cadenas, números y fechas estén formateados correctamente.
  * **Campos faltantes**: Identifique cualquier campo presente en la solicitud de M3 pero ausente en DocBits.

### 4. Solución de problemas de problemas comunes

| Problema                                     | Causa probable                                | Solución                                                                 |
| -------------------------------------------- | --------------------------------------------- | ------------------------------------------------------------------------ |
| Error de campo faltante                      | Un campo requerido no está mapeado en DocBits | Agregue el campo faltante en la configuración de exportación de DocBits. |
| Desajuste de mayúsculas en el campo (`DIVI`) | M3 distingue entre mayúsculas y minúsculas    | Utilice la mayúscula correcta en la asignación del campo.                |
| Formato de `accountingDate` inválido         | Fecha incorrecta o faltante                   | Ajuste al formato esperado por M3 (por ejemplo, `AAAA-MM-DD`).           |
| Error inesperado de la API                   | Campos adicionales o no reconocidos           | Compare con cargas de trabajo conocidas y limpie los datos innecesarios. |

### 5. Si los problemas persisten

Si el problema no se resuelve después de seguir los pasos anteriores:

1. **Documente** el problema:
   * Mensaje de error y código de estado
   * Solicitud de M3 de muestra y JSON de exportación de DocBits
2. **Resuma** su solución de problemas:
   * Lo que ha intentado
   * Diferencias clave observadas entre las cargas de prueba y las fallidas
3. **Escale** a un desarrollador:
   * Incluya todos los datos y hallazgos
   * Destaque áreas de problema sospechosas
