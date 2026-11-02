# Prueba: conexión de importación FTP

#### Objetivo

Estas pruebas aseguran que nuestro sistema de importación FTP funcione correctamente. Verificamos que podemos agregar una nueva conexión de importación FTP, probar la conexión, activarla/desactivarla y limpiarla después.



{% embed url="https://grafana.polydocs.io/d-solo/b6ad3a9c-260c-46a3-9ade-47691e743d4d/docbits?from=1715746603760&orgId=1&panelId=84&refresh=1m&to=1715768203760" %}

## Escenarios de prueba

1. **Setup:**
   * **Variables de entorno:** Cargue los detalles necesarios como información del servidor FTP y credenciales de las variables de entorno.
2.  **FTP Connection Tests:**

    **Agregar nueva conexión:**

    * **Prueba Agregar nuevo FTP Conexión de importación (`test_add_new_ftp_import_connection`):**
      * Agregue una nueva conexión de importación FTP con las credenciales y los detalles del servidor proporcionados.
      * **Resultado esperado:** La conexión debería agregarse correctamente.

    **Deactivate Connection:**

    * **Prueba Desactivar FTP Importar Conexión (`test_deactivate_ftp_import_connection`):**
      * Desactive la conexión de importación FTP recién agregada.
      * **Resultado esperado:** La conexión debería desactivarse correctamente.

    **Test Connection:**

    * **Prueba de conexión FTP (`test_test_ftp_connection`):**
      * Pruebe si la conexión de importación FTP puede conectarse correctamente al servidor FTP.
      * **Resultado esperado:** La conexión debe probarse correctamente.

    **Verificar conexión en la lista:**

    * **Comprobación de prueba FTP Conexión en la lista (`test_check_ftp_connection_in_list`):**
      * Compruebe si la conexión de importación FTP recién agregada está presente en la lista de conexiones.
      * **Resultado esperado:** La conexión debería encontrarse en la lista.

    **Verificar conexión desactivada:**

    * **Comprobación de prueba FTP Conexión desactivada (`test_check_ftp_connection_deactivated`):**
      * Verifique que la conexión de importación FTP esté marcada como inactiva en la lista.
      * **Resultado esperado:** La conexión debe estar inactiva.

    **Agregar carpeta de prueba:**

    * **Prueba Agregar carpeta de prueba a la conexión (`test_add_test_folder_to_connection`):**
      * Agregue un directorio predeterminado (carpeta de prueba) a la conexión de importación FTP.
      * **Resultado esperado:** El directorio predeterminado debería agregarse correctamente.

    **Reactivate Connection:**

    * **Prueba Reactivar FTP Importar Conexión (`test_reactivate_ftp_import_connection`):**
      * Reactive la conexión de importación FTP previamente desactivada.
      * **Resultado esperado:** La conexión debería reactivarse correctamente.

    **Verificar conexión reactivada:**

    * **Comprobación de prueba FTP Conexión reactivada (`test_check_ftp_connection_reactivated`):**
      * Verifique que la conexión de importación FTP esté marcada como activa en la lista.
      * **Resultado esperado:** La conexión debería estar activa.

    **Cleanup:**

    * **Prueba de limpieza de la importación FTP (`test_cleanup_ftp_import`):**
      * Elimine la conexión de importación FTP para limpiarla después de las pruebas.
      * **Resultado esperado:** La conexión debería eliminarse correctamente.

## Explicación detallada de cada prueba

* **Configuración e inicialización:**
  * **Inicializar datos compartidos:** Preparar datos compartidos para las pruebas.
* **FTP Connection Tests:**
  * **Agregar nueva conexión:** Agregue una nueva conexión de importación FTP con las credenciales proporcionadas y los detalles del servidor.
  * **Desactivar conexión:** Desactiva la conexión de importación FTP recién agregada.
  * **Probar conexión:** Pruebe si la conexión de importación FTP puede conectarse correctamente al servidor FTP.
  * **Verificar conexión en la lista:** Verifique que la nueva conexión de importación FTP esté presente en la lista de conexiones.
  * **Verificar conexión desactivada:** Confirme que la conexión de importación FTP esté marcada como inactiva en la lista.
  * **Agregar carpeta de prueba:** Agregue un directorio predeterminado (carpeta de prueba) a la conexión de importación FTP.
  * **Reactivar Conexión:** Reactiva la conexión de importación FTP previamente desactivada.
  * **Verificar conexión reactivada:** Asegúrese de que la conexión de importación FTP esté marcada como activa en la lista.
  * **Limpieza:** Elimine la conexión de importación FTP para limpiar después de las pruebas.

\


