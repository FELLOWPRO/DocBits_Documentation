# Import

## Overview

In the **Importar** settings, you can configure document-specific options for importing, or set up automated imports via FTP or email. This page provides a detailed overview of all available settings.

## How to Access

1.  Navigate to **Ajustes** -> **Procesamiento de Documentos** -> **Importar**

    <figure><img src="../../../../.gitbook/assets/s150-ftp_0-es.png" alt="Resumen de las conexiones de importación FTP."><figcaption><p>Resumen de las conexiones de importación FTP.</p></figcaption></figure>

## **Restricción de importación de la página del documento**

* **Restringir a las páginas**: This setting allows you to limit the processing to a certain number of pages per document. The default is **60 pages**, meaning documents exceeding this limit will be trimmed to **60 pages**, and any **remaining pages will be discarded.**
* **Términos de pago días**: Defines the default payment terms (in days) that can be applied to documents.
* **Patrón de fecha**: Sets the pattern for how dates should be recognized and formatted within imported documents.

<figure><img src="../../../../.gitbook/assets/document_settins_1.png" alt=""><figcaption></figcaption></figure>

## **Importación ftp**

### Requirements

To use FTP for importing data automatically, ensure the following requirements are met:

* Correctly configured, Linux compatible FTP Server
* FTP Hostname, Username and Password
* Dedicated Import folder

### Add new connection

1.  To add a new connection, click the **Agregar** button in the FTP section.


2.  Enter your FTP credentials in the designated fields. The API Key field will be filled in automatically.

    * **Type:** Specifies the FTP protocol to use. You can choose between **FTP**, **FTPS**, or **SFTP**.
    * **Port:** Specifies the port number to be used for the selected FTP protocol.
    * **Server Name (required):** The address of the server from which documents will be retrieved.
    * **Username (required):** The login name used to access the FTP server.
    * **Password (required):** The password associated with the username for accessing the FTP server.
    * **File name matching patterns:** To specify which files to import based on their names.
    * **Sub-Organizations:** Select which sub-organization the FTP import should apply to.
    * **API Key (required):** This field will be automatically filled based on the organization you are logged into.
    * **Primary Directory:** Specifies the directory on the FTP server from which files will be imported.
    * **Import Directory:** Allows you to specify a subdirectory within the primary directory from which files will be imported.
    * **Archive After Import:** Allows you to archive files after import. Once activated, you can specify the directory where files should be moved after a successful import.
    * **Include Subfolder Files:** When enabled, subdirectories within the main directory will also be searched for files to import.


3. Once you have entered all the necessary details of your FTP, click **SAVE**.
4. After saving your connection, you can activate it by clicking the three dots in the **Action** column of your connection, then selecting **Activar**.

### Actions for FTP

You can click the three dots in the **Action** column to access the following options for your connection:

<figure><img src="../../../../.gitbook/assets/s150-ftp_5-es.png" alt="Configuración del servidor en el asistente de importación FTP."><figcaption><p>Configuración del servidor en el asistente de importación FTP.</p></figcaption></figure>

* **Test Connection:** Tests the connection to your FTP server.
* **Connection Logs:** Opens the logs for your FTP connection, including error messages if any issues occur.
* **Activate/Deactivate:** Activates/deactivates your connection.
* **Edit:** Allows you to make changes to your connection.
* **Delete:** Deletes your connection.

## **Importación de correo electrónico**

You can set up an email import that automatically imports documents from your inbox as soon as they arrive. You can choose to configure either an IMAP or an OAuth connection

<mark style="color:red;">**Nota**</mark>:  Only documents with the following file types will be imported:

* `.pdf`
* `.tiff` / `.tif`
* `.eml`
* `.dat`
* `.xml`
* `.edi`
* `.purchaseorder`

{% hint style="info" %}
**How attachments are recognised**

In addition to the file extensions listed above, DocBits also identifies a document by its **actual file content** (file signature), not only by the content type declared by the sending mail system. This matters for **forwarded** mails: intermediate mail servers/gateways frequently re-label an attachment with a generic type (`application/octet-stream`) instead of, for example, `application/pdf` or `application/xml`. DocBits still recognises and imports such attachments correctly.

* **Forwarded `.eml`** messages and Outlook **`winmail.dat`** (TNEF) attachments are unpacked and the documents inside them are imported.
* **Codificación XML:** Cuando una factura XML se reetiqueta con un tipo genérico (`application/octet-stream`), DocBits la reconoce por su declaración `<?xml`, tolerando una marca de orden de bytes (BOM) **UTF-8** o **UTF-16** (LE/BE) inicial — actualmente solo estas codificaciones BOM se detectan automáticamente a partir del contenido. Un archivo adjunto que conserva un nombre `.xml` se importa independientemente de su codificación.
* **Ignored:** inline images that ride along in a mail (signature logos / embedded graphics — PNG, JPG, GIF, BMP) are skipped silently and are **no** counted as failed imports.

If an attachment cannot be imported and the option **“Reply to this email if import can not be done”** is enabled for the inbound address, the configured reply address is notified.
{% endhint %}

### Add new IMAP connection

1.  To add a new IMAP connection, click the **Agregar** button in the **Importación de correo electrónico** section.


2. Select IMAP as the protocol.
3. Enter your email credentials in the designated fields. The API Key field will be filled automatically.
   * **Encryption:** Select the type of encryption to use — either **SSL** or **TLS**.
   * **Server name:** The address of the email server.
   * **Username:** The identifier used for your mail import configuration in DocBits.
   * **E-mail:** The email address used for importing documents into the system.
   * **Password:** The password associated with the provided email address.
   * **Sub-Organizations:** Select the sub-organization to which the email import should apply.
   * **API Key:** This field will be automatically filled based on the organization you are logged into.
   * **Send Import Error Notice to this Email Address:** Specify an email address to receive error notifications if something goes wrong during the import process.
   * **Port:** Specifies the port number to be used for the selected email import configuration.
   * **Folder:** Select a folder from which the documents will be imported.\
     <mark style="color:red;">**Nota**</mark>: The **Carpeta** option becomes available only after you have successfully created an IMAP connection. To add a folder after creation, click the three dots in the **Action** column, then select **Editar**. The option should now be available.
   * **Move Emails to Other Folder:** When enabled, allows you to specify a folder where emails will be moved after a successful import.\
     <mark style="color:red;">**Nota**</mark>: The **Move Emails to Other Folder** option becomes available only after you have successfully created an IMAP connection. To activate this setting, click the three dots in the **Action** column, then select **Editar**. The option should now be available.
   * **Merge Attached Documents:** Combines multiple attached documents into a single document.
   * **Send Email to Sender after Import:** Sends a confirmation email to the original sender after the import is complete. Once activated, you can specify the subject and body of the email.
   * **Block Duplicate Filename Import:** Prevents import if a document with the same name already exists.
4. After saving your connection, you can activate it by clicking the three dots in the **Action** column of your connection, then selecting **Activar**.

### Actions for IMAP

You can click the three dots in the **Action** column to access the following options for your connection:


* **Test Connection:** Tests the connection to your IMAP client.
* **Connection Logs:** Opens the logs for your email connection, including any error messages that occur during the process.
* **Import Log:** Opens the logs of past imports for the respective connection, including any error messages that occurred during the process.
* **Activate/Deactivate:** Activates/deactivates your connection.
* **Edit:** Allows you to make changes to your connection.
* **Delete:** Deletes your connection.

### Add new OAuth Office365 connection

1.  To add a new OAuth Office365 connection, click the **Agregar** button in the **Importación de correo electrónico** section.


2.  Select **OAuth Office365** as the protocol, then click on **Autenticar**.


3.  You will be redirected to a Microsoft page where you’ll be asked to enter a code. To retrieve this code, return to DocBits—the code will be displayed there, as shown below. Copy the code and enter it on the Microsoft page. Afterward, you will be prompted to enter your Microsoft credentials.


4. Follow the steps on the Microsoft page. Once you're done, return to DocBits and click **Finish Authentication**.
5.  You can now configure the following settings:

    * **Sub-Organizations:** Select the sub-organization to which the email import should apply.
    * **Use Folder:** Select a folder from which the documents will be imported.
    * **Use Shared Mailbox:** Specify the shared email address from which documents should be imported.
    * **Move Email to other folder:** Specify a folder to which emails should be moved after a successful import.
    * **Send Import Error Notice to this Email-Address:** Specify an email address to receive error notifications if something goes wrong during the import process.


6. Once you’ve configured the desired behavior, you can either start importing emails by clicking **Importar** or save your changes by clicking **Guardar**.
7.  After saving your connection, you can activate it by clicking the three dots in the **Action** column of your connection, then selecting **Activar**.


### Actions for OAuth Office365

You can click the three dots in the **Action** column to access the following options for your connection:


* **Connection Logs:** Opens the logs for your email connection, including any error messages that occur during the process.
* **Import Log:** Opens the logs of past imports for the respective connection, including any error messages that occurred during the process.
* **Activate/Deactivate:** Activates/deactivates your connection.
* **Edit:** Allows you to make changes to your connection.
* **Delete:** Deletes your connection.

### Import Log

You can view the import log of all created email connections, including any error messages that occurred during the process, by clicking the **Registro de importación** button in the top-right corner of the Email Import section.


You can filter the logs by subject or sender, sort columns in ascending or descending order by clicking the column headers, and rearrange columns using drag-and-drop.
