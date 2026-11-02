# Prueba: importación de archivos 1

## Objetivo

Estas pruebas están diseñadas para garantizar que nuestro sistema de importación de archivos funcione correctamente. Probamos específicamente la importación de archivos PDF y TIFF al sistema, asegurándonos de que se procesen y almacenen correctamente.

#### Preparación y limpieza de las pruebas

* **Setup:**
  * Antes de cada prueba, registramos un mensaje de configuración.
  * **Limpieza:** Después de cada prueba, limpiamos eliminando cualquier documento creado por el usuario de prueba de la base de datos para garantizar que ningún dato sobrante afecte las pruebas posteriores.

#### Escenarios de prueba

1. **Import PDF File:**
   * **Prueba de importación de PDF (`test_import_pdf`):**
     * Import a PDF file (`FellowBananaInvoice.pdf`) into the system.
     * **Resultado esperado:** El archivo debería importarse correctamente y devolver un ID de documento.
2. **Import TIFF File:**
   * **Prueba de importación de TIFF (`test_import_tiff`):**
     * Import a TIFF file (`TIFF_FILE.TIF`) into the system.
     * **Resultado esperado:** El archivo debería importarse correctamente y devolver un ID de documento.

## Explicación detallada de cada prueba

* **Configuración y limpieza:**
  * **Registro:** Se registra un mensaje de configuración y limpieza para cada prueba.
  * **Limpieza de base de datos (`clean_documents`):** Elimina cualquier documento creado por el usuario de prueba de la base de datos para mantener un estado limpio.
*   **Pruebas de importación de archivos:**

    **Import PDF File:**

    * **Cargar usuario:** Carga el usuario de prueba.
    * **Ruta del archivo:** Especifique la ruta al archivo PDF (`tests/files/pdfs/FellowBananaInvoice.pdf`).
    * **Importar archivo:** Utilice la clase `FileImporter` para importar el archivo PDF.
    * **Respuesta de verificación:** Asegúrese de que la respuesta sea una lista que contenga un mensaje de éxito y un ID de documento.

    **Import TIFF File:**

    * **Cargar usuario:** Carga el usuario de prueba.
    * **Ruta del archivo:** Especifique la ruta al archivo TIFF (`tests/files/pdfs/TIFF_FILE.TIF`).
    * **Importar archivo:** Utilice la clase `FileImporter` para importar el archivo TIFF.
    * **Respuesta de verificación:** Asegúrese de que la respuesta sea una lista que contenga un mensaje de éxito y un ID de documento.

## Estructura del código

* **Registro de eventos:** Se utiliza para registrar mensajes de depuración durante la configuración, limpieza y ejecución de pruebas.
* **Utilidad de base de datos:** Ejecuta consultas sin devolver resultados para la limpieza.
* **File Importer:** Handles the import of files into the system.
* **Fixtures de prueba:** fixture `set_up` para gestionar la configuración y la limpieza de las pruebas.
* **Tests:**
  * `test_import_pdf`: Prueba la importación de un archivo PDF.
  * `test_import_tiff`: Prueba la importación de un archivo TIFF.

#### Resumen

Estas pruebas garantizan que nuestra funcionalidad de importación de archivos funcione como se espera para los archivos PDF y TIFF. Siguiendo este enfoque, verificamos que los archivos se importen correctamente y que el sistema pueda manejar diferentes tipos de archivos sin problemas.


