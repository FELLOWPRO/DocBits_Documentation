---
hidden: true
noIndex: true
---

# FTP

If you would like to integrate your SFTP with DocBits in order to import documents.

Requirements

* Correctly configured, Linux compatible SFTP Server
* SFTP Hostname, Username and Password
* Dedicated Import folder

**Import Configuration**

From the Dashboard, open Settings and navigate to Import. Under FTP Import, select to add a new configuration.

<figure><img src="../../../.gitbook/assets/ftp1.png" alt="Add New FTP Configuration"><figcaption></figcaption></figure>

Enter SFTP credentials in the given spaces and select save (The API Key field will automatically be filled with the API Key of the environment you are working on).

<figure><img src="../../../.gitbook/assets/ftp_import_configuration_form.png" alt="FTP Import Configuration Form"><figcaption></figcaption></figure>

Once you have entered all the necessary details of your SFTP, click SAVE.

### **FTP File Archiving**

1. **Enable File Archiving**
   * Locate the "File Archiving" option.
   * Toggle the switch to the "On" position to enable archiving.
2. **Select the Archive Directory**
   * Once the "File Archiving" switch is enabled, a field will appear allowing you to specify the directory path for archived files.
   * Select the desired folder path on the SFTP/FTP server where the archived files should be stored.
3. **Save Changes**
   * Click the **Save** button to apply the changes.

<figure><img src="../../../.gitbook/assets/ftp_3.png" alt="FTP File Archiving Settings"><figcaption></figcaption></figure>
