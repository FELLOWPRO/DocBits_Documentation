# How to Create Database Access for a Specific Organization User

### **1. Login to the Docbits** <a href="#id-1.-login-to-the-docbits" id="id-1.-login-to-the-docbits"></a>

1. Go to your application login page.
2. Enter your credentials (username and password) to log in.

### **2. Access the Settings** <a href="#id-2.-access-the-settings" id="id-2.-access-the-settings"></a>

1. Once logged in, locate the **Settings** icon (gear ⚙️) on the left-hand sidebar.
2. Click on **Settings** to open the system configuration panel.

### **3. Open the Document Processing Module** <a href="#id-3.-open-the-document-processing-module" id="id-3.-open-the-document-processing-module"></a>

1. In the **Settings**, locate the **Document Processing** section.
2. Under **Document Processing**, find and click on the **Module** option.
   * This will open the relevant module configuration page where you can proceed with creation of user for database.

### 4. Steps to Enable and Access the AI Document and Database User: <a href="#id-4.-steps-to-enable-and-access-the-ai-document-and-database-user" id="id-4.-steps-to-enable-and-access-the-ai-document-and-database-user"></a>

1. **Toggle Features**:
   * Use the toggles on the right to enable or disable specific features:
     * **AI Document Warehouse**: Toggle this to enable access to AI-related features.
     * **DB Access**: Toggle this to grant database access to user.
2. **Database Credentials**:
   * The dashboard provides the following database connection details:
     * **Username**: A unique username is displayed
     * **Password**: Ensure the password is securely stored or copied.
     * **Database**: Is the name of the Database
     * **Host**: Host Name
     * **Port**: Is the Port
     * **SSL Mode:** The connection requires `sslmode=require` for secure communication.
3. **Copying Credentials**:
   * Use the copy icons next to each field to quickly copy the credentials for use in your database client or application.
4. **Connection via DBeaver**:
   * Connect via Host
     * choose PostgreSQL
     * Fill in the required information
     * change to the SSL tab and check Use SSL. Move down to SSL mode and select require
   * Connect via URL
     * Fill in the required information:\n - replace Host with the provided host information\n - replace Port with the provided port information\n - replace Database with the provided database information\n - for Username select the provided username information\n - for Password select the provided password information
5. **Test the Connection**:
   * Click the **"Test Connection"** button to ensure the credentials and connection details are correct.
   * If the test is successful, proceed to connect.
6. **Explore the Database**:
   * Once connected, navigate to the **schema** or **tables** section in your database client.
   * Check the available tables.
