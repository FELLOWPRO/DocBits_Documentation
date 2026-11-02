# Cómo crear acceso a la base de datos para un usuario específico de la organización

### **1. Inicie sesión en Docbits** <a href="#id-1.-login-to-the-docbits" id="id-1.-login-to-the-docbits"></a>

1. Vaya a la página de inicio de sesión de su aplicación.
2. Introduzca sus credenciales (nombre de usuario y contraseña) para iniciar sesión.

### **2. Acceda a Configuración** <a href="#id-2.-access-the-settings" id="id-2.-access-the-settings"></a>

1. Una vez iniciada la sesión, localice el icono de **Settings** (engranaje ⚙️) en la barra lateral izquierda.
2. Haga clic en **Settings** para abrir el panel de configuración del sistema.

### **3. Abra el módulo Procesamiento de documentos** <a href="#id-3.-open-the-document-processing-module" id="id-3.-open-the-document-processing-module"></a>

1. En **Settings**, localice la sección **Document Processing**.
2. Dentro de **Document Processing**, busque y haga clic en la opción **Module**.
   * Se abrirá la página de configuración del módulo correspondiente, donde podrá proceder con la creación del usuario para la base de datos.

### 4. Pasos para activar y acceder al usuario de AI Document y de base de datos: <a href="#id-4.-steps-to-enable-and-access-the-ai-document-and-database-user" id="id-4.-steps-to-enable-and-access-the-ai-document-and-database-user"></a>

1. **Active las funciones**:
   * Utilice los interruptores de la derecha para activar o desactivar funciones específicas:
     * **AI Document Warehouse**: actívelo para habilitar el acceso a las funciones relacionadas con la IA.
     * **DB Access**: actívelo para conceder acceso a la base de datos al usuario.
2. **Credenciales de la base de datos**:
   * El panel proporciona los siguientes datos de conexión a la base de datos:
     * **Username**: se muestra un nombre de usuario único.
     * **Password**: asegúrese de guardar o copiar la contraseña de forma segura.
     * **Database**: es el nombre de la base de datos.
     * **Host**: nombre del host.
     * **Port**: es el puerto.
     * **SSL Mode:** la conexión requiere `sslmode=require` para una comunicación segura.
3. **Copia de credenciales**:
   * Utilice los iconos de copiar junto a cada campo para copiar rápidamente las credenciales y usarlas en su cliente de base de datos o aplicación.
4. **Conexión mediante DBeaver**:
   * Conexión mediante Host
     * elija PostgreSQL
     * Rellene la información necesaria
     * cambie a la pestaña SSL y marque Use SSL. Desplácese hacia abajo hasta SSL mode y seleccione require
   * Conexión mediante URL
     * Rellene la información necesaria:\n - sustituya Host por la información de host proporcionada\n - sustituya Port por la información de puerto proporcionada\n - sustituya Database por la información de base de datos proporcionada\n - en Username seleccione la información de nombre de usuario proporcionada\n - en Password seleccione la información de contraseña proporcionada
5. **Pruebe la conexión**:
   * Haga clic en el botón **"Test Connection"** para comprobar que las credenciales y los datos de conexión son correctos.
   * Si la prueba es satisfactoria, proceda a conectarse.
6. **Explore la base de datos**:
   * Una vez conectado, vaya a la sección de **esquemas** o **tablas** de su cliente de base de datos.
   * Compruebe las tablas disponibles.
