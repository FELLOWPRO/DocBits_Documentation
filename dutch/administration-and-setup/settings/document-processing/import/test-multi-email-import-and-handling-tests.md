# Test: Multi Email Import and Handling Tests

## What's Being Tested?

These tests ensure that our email import system works correctly. The main goals are to:

1. **Send emails** with attachments.
2. **Receive and move emails** to specific folders.
3. **Check if emails are read or unread.**
4. **Import emails into our system.**
5. **Clean up** by deleting emails and imported documents afterward.

## Steps Involved

1. **Setup:**
   * **Get Environment Settings:** Load the email server details and credentials from environment variables.
   * **Encrypt Email Password:** Securely encrypt the email password.
2. **Send and Manage Emails:**
   * **Send Emails:** Use an SMTP function to send emails with specific subjects and attachments.
   * **Move Emails:** Use IMAP functions to move emails to the target folder.
   * **List Folders:** Check if the target folder exists.
   * **Delete Emails:** Clean up emails by deleting them from folders.
   * **Check Email Status:** Verify if emails are marked as unread or read.
3.  **Test Sequence**

    **Initial Setup:**

    * **Check Connection:** Verify connection to the email server and get the connection ID.
    * **Login Test:** Confirm that logging in with stored credentials works.
    * **Folder Check:** Ensure the target folder exists on the email server.

    **Email Operations:**

    * **Send Test Emails:** Send three emails with unique subjects.
    * **Retrieve Email IDs:** Get the IDs of the sent emails from the inbox.
    * **Move Emails:** Move these emails from the inbox to the target folder.
    * **Check Email Status:** Ensure the emails in the target folder are marked as unread.

    **Email Importing:**

    * **Fetch Emails:** Import emails from the target folder into our system.
    * **Check Imported Emails:** Ensure the imported emails are correctly fetched and logged.

    **Log Verification:**

    * **Check Import Logs:** Verify that the subjects of the sent emails are recorded in the import logs.

    **Cleanup:**

    * **Delete Imported Documents:** Remove the documents that were imported from the emails.
    * **Delete Emails:** Clean up by deleting the sent and moved emails from the folders.

### Detailed Explanation of Each Test

* **Setup and Initialization:**
  * **Initialize Shared Data:** Prepare shared data for tests.
* **Email Connection Tests:**
  * **Get Connection ID:** Check if we can connect to the email server and get an ID for the connection.
  * **Login Verification:** Ensure that logging in to the email server works properly.
* **Folder Verification Tests:**
  * **Check Target Folder:** Make sure the target folder exists on the email server.
  * **Verify Folder Listing:** Ensure the list of folders from the server matches our expectations.
* **Email Sending and ID Retrieval:**
  * **Send Emails:** Send three test emails with specific subjects and attachments.
  * **Get Email IDs:** Retrieve the unique IDs of these sent emails from the inbox.
* **Email Moving and Status Checking:**
  * **Move Emails to Folder:** Move the test emails from the inbox to the target folder.
  * **Check Unread Status:** Ensure the emails are marked as unread after moving.
* **Email Fetching and Response Validation:**
  * **Fetch Emails from Folder:** Import the emails from the target folder into our system.
  * **Validate Fetched Emails:** Confirm that the fetched emails match the sent emails.
* **Import Log Verification:**
  * **Fetch Import Log:** Retrieve the log of imported emails.
  * **Check Email Subjects in Log:** Ensure the subjects of the test emails are present in the import log.
* **Cleanup:**
  * **Delete Imported Documents:** Remove the documents that were imported from the emails.
  * **Delete Emails:** Delete the test emails from the inbox and the target folder to keep everything clean.

\\
