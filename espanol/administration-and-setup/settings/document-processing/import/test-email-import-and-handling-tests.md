# Prueba: importación y gestión del correo electrónico

## Objetivo

Estas pruebas garantizan que nuestro sistema pueda manejar la importación de correo electrónico correctamente. Esto incluye enviar correos electrónicos, recibirlos y moverlos a carpetas específicas, verificar si están leídos o no, importarlos al sistema y realizar una limpieza posterior.

## Pasos de prueba

1. **Setup:**
   * **Obtener configuración del entorno:** Cargue los detalles necesarios, como información del servidor de correo electrónico y credenciales de las variables de entorno.
   * **Cifrar contraseña de correo electrónico:** Cifre de forma segura la contraseña de correo electrónico para un uso seguro.
2. **Envío y gestión de correo electrónico:**
   * **Enviar un correo electrónico:** Utilice una función SMTP para enviar un correo electrónico con un asunto y un archivo adjunto específicos.
   * **Mover el correo electrónico:** Utilice las funciones IMAP para mover el correo electrónico a una carpeta de destino.
   * **Listar carpetas:** Asegúrese de que exista la carpeta de destino.
   * **Eliminar el correo electrónico:** Limpie eliminando el correo electrónico de la carpeta.
   * **Verificar estado del correo electrónico:** Verifique si el correo electrónico está marcado como leído o no leído.
3.  **Test Sequence**

    **Initial Setup:**

    * **Verificar conexión:** Verifique la conexión al servidor de correo electrónico y obtenga el ID de la conexión.
    * **Prueba de inicio de sesión:** Confirme que el inicio de sesión con las credenciales almacenadas funciona.
    * **Comprobación de carpeta:** Asegúrese de que la carpeta de destino exista en el servidor de correo electrónico.

    **Email Operations:**

    * **Enviar un correo electrónico de prueba:** Envíe un correo electrónico con un asunto específico.
    * **Recuperar ID del correo electrónico:** Obtenga el ID del correo electrónico enviado desde la bandeja de entrada.
    * **Mover el correo electrónico:** Mueva el correo electrónico de la bandeja de entrada a la carpeta de destino.
    * **Verificar el estado del correo electrónico:** Asegúrese de que el correo electrónico en la carpeta de destino esté marcado como no leído.

    **Email Importing:**

    * **Recuperar el correo electrónico:** Importar el correo electrónico de la carpeta de destino a nuestro sistema.
    * **Verificar correo electrónico importado:** Asegúrese de que el correo electrónico importado se haya obtenido y registrado correctamente.

    **Log Verification:**

    * **Verificar registro de importación:** Verifique que el asunto del correo electrónico enviado esté registrado en el registro de importación.

    **Cleanup:**

    * **Eliminar documento importado:** Elimina el documento que se importó del correo electrónico.
    * **Eliminar el correo electrónico:** Elimina el correo electrónico enviado y movido de las carpetas para mantener todo limpio.

## Explicación detallada de cada prueba

* **Configuración e inicialización:**
  * **Inicializar datos compartidos:** Preparar datos compartidos para las pruebas.
* **Pruebas de conexión de correo electrónico:**
  * **Obtener ID de conexión:** Comprobar si podemos conectarnos al servidor de correo electrónico y obtener un ID para la conexión.
  * **Verificación de inicio de sesión:** Asegúrese de que el inicio de sesión en el servidor de correo electrónico funcione correctamente.
* **Pruebas de verificación de carpetas:**
  * **Verificar la carpeta de destino:** Asegúrese de que la carpeta de destino exista en el servidor de correo electrónico.
  * **Verificar lista de carpetas:** Asegúrese de que la lista de carpetas del servidor coincida con nuestras expectativas.
* **Envío y recuperación de ID del correo electrónico:**
  * **Enviar un correo electrónico:** Envíe un correo electrónico de prueba con un asunto y un archivo adjunto específicos.
  * **Obtener ID del correo electrónico:** Recupera el ID único de este correo electrónico enviado desde la bandeja de entrada.
* **Movimiento de correo electrónico y verificación de estado:**
  * **Mover correo electrónico a la carpeta:** Mueva el correo electrónico de prueba de la bandeja de entrada a la carpeta de destino.
  * **Verificar estado no leído:** Asegúrese de que el correo electrónico esté marcado como no leído después de moverse.
* **Obtención de correo electrónico y validación de respuesta:**
  * **Obtener correo electrónico de la carpeta:** Importar el correo electrónico de la carpeta de destino a nuestro sistema.
  * **Validar correo electrónico recuperado:** Confirme que el correo electrónico recuperado esté presente en la respuesta.
* **Verificación de registro de importación:**
  * **Recuperar registro de importación:** Recupera el registro de correos electrónicos importados.
  * **Verifique el asunto del correo electrónico en el registro:** Asegúrese de que el asunto del correo electrónico de prueba esté presente en el registro de importación.
* **Cleanup:**
  * **Eliminar documento importado:** Elimina el documento que se importó del correo electrónico.
  * **Eliminar el correo electrónico:** Elimina el correo electrónico de prueba de la bandeja de entrada y de la carpeta de destino para mantener todo limpio.

\


