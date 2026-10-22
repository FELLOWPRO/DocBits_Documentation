# Prueba: importación y gestión del correo electrónico

## ¿Qué se prueba?

Estas pruebas garantizan que nuestro sistema de importación de correo electrónico funcione correctamente. Los principales objetivos son:

1. **Enviar correos electrónicos** con archivos adjuntos.
2. **Recibir y mover correos electrónicos** a carpetas específicas.
3. **Compruebe si los correos electrónicos están leídos o no leídos.**
4. **Importar correos electrónicos a nuestro sistema.**
5. **Limpie** eliminando correos electrónicos y documentos importados posteriormente.

## Pasos necesarios

1. **Setup:**
   * **Obtener configuración del entorno:** Cargue los detalles y las credenciales del servidor de correo electrónico desde las variables de entorno.
   * **Cifrar contraseña de correo electrónico:** Cifre de forma segura la contraseña de correo electrónico.
2. **Enviar y administrar correos electrónicos:**
   * **Enviar correos electrónicos:** Utilice una función SMTP para enviar correos electrónicos con asuntos y archivos adjuntos específicos.
   * **Mover correos electrónicos:** Utilice las funciones IMAP para mover correos electrónicos a la carpeta de destino.
   * **Listar carpetas:** Compruebe si la carpeta de destino existe.
   * **Eliminar correos electrónicos:** Limpia los correos electrónicos eliminándolos de las carpetas.
   * **Verificar el estado del correo electrónico:** Verifique si los correos electrónicos están marcados como leídos o no leídos.
3.  **Test Sequence**

    **Initial Setup:**

    * **Verificar conexión:** Verifique la conexión al servidor de correo electrónico y obtenga el ID de la conexión.
    * **Prueba de inicio de sesión:** Confirme que el inicio de sesión con las credenciales almacenadas funciona.
    * **Comprobación de carpeta:** Asegúrese de que la carpeta de destino exista en el servidor de correo electrónico.

    **Email Operations:**

    * **Enviar correos electrónicos de prueba:** Envíe tres correos electrónicos con asuntos únicos.
    * **Recuperar ID de correo electrónico:** Obtenga los ID de los correos electrónicos enviados desde la bandeja de entrada.
    * **Mover correos electrónicos:** Mueva estos correos electrónicos desde la bandeja de entrada a la carpeta de destino.
    * **Verificar el estado del correo electrónico:** Asegúrese de que los correos electrónicos en la carpeta de destino estén marcados como no leídos.

    **Email Importing:**

    * **Obtener correos electrónicos:** Importar correos electrónicos de la carpeta de destino a nuestro sistema.
    * **Verificar correos electrónicos importados:** Asegúrese de que los correos electrónicos importados se obtengan y registren correctamente.

    **Log Verification:**

    * **Verificar registros de importación:** Verifique que los asuntos de los correos electrónicos enviados estén registrados en los registros de importación.

    **Cleanup:**

    * **Eliminar documentos importados:** Elimina los documentos que se importaron de los correos electrónicos.
    * **Eliminar correos electrónicos:** Limpie eliminando los correos electrónicos enviados y movidos de las carpetas.

### Explicación detallada de cada prueba

* **Configuración e inicialización:**
  * **Inicializar datos compartidos:** Preparar datos compartidos para las pruebas.
* **Pruebas de conexión de correo electrónico:**
  * **Obtener ID de conexión:** Comprobar si podemos conectarnos al servidor de correo electrónico y obtener un ID para la conexión.
  * **Verificación de inicio de sesión:** Asegúrese de que el inicio de sesión en el servidor de correo electrónico funcione correctamente.
* **Pruebas de verificación de carpetas:**
  * **Verificar la carpeta de destino:** Asegúrese de que la carpeta de destino exista en el servidor de correo electrónico.
  * **Verificar lista de carpetas:** Asegúrese de que la lista de carpetas del servidor coincida con nuestras expectativas.
* **Envío y recuperación de ID del correo electrónico:**
  * **Enviar correos electrónicos:** Envíe tres correos electrónicos de prueba con asuntos y archivos adjuntos específicos.
  * **Obtener ID de correo electrónico:** Recupere los ID únicos de estos correos electrónicos enviados desde la bandeja de entrada.
* **Movimiento de correo electrónico y verificación de estado:**
  * **Mover correos electrónicos a la carpeta:** Mueva los correos electrónicos de prueba de la bandeja de entrada a la carpeta de destino.
  * **Verificar estado no leído:** Asegúrese de que los correos electrónicos estén marcados como no leídos después de moverse.
* **Obtención de correo electrónico y validación de respuesta:**
  * **Obtener correos electrónicos de la carpeta:** Importar los correos electrónicos de la carpeta de destino a nuestro sistema.
  * **Validar correos electrónicos recuperados:** Confirme que los correos electrónicos recuperados coincidan con los correos electrónicos enviados.
* **Verificación de registro de importación:**
  * **Recuperar registro de importación:** Recupera el registro de correos electrónicos importados.
  * **Verifique los asuntos de los correos electrónicos en el registro:** Asegúrese de que los asuntos de los correos electrónicos de prueba estén presentes en el registro de importación.
* **Cleanup:**
  * **Eliminar documentos importados:** Elimina los documentos que se importaron de los correos electrónicos.
  * **Eliminar correos electrónicos:** Elimina los correos electrónicos de prueba de la bandeja de entrada y de la carpeta de destino para mantener todo limpio.

\


