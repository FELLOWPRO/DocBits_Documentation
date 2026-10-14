# Test: Email Import and Handling Tests

## Purpose

These tests ensure that our system can handle email importing correctly. This includes sending emails, receiving and moving them to specific folders, checking if they are read or unread, importing them into the system, and performing cleanup afterward.

## Test Steps

1. **Setup:**
   * **Get Environment Settings:** Load necessary details like email server information and credentials from environment variables.
   * **Encrypt Email Password:** Securely encrypt the email password for safe usage.
2. **Email Sending and Management:**
   * **Send an Email:** Use an SMTP function to send an email with a specific subject and attachment.
   * **Move the Email:** Use IMAP functions to move the email to a target folder.
   * **List Folders:** Ensure the target folder exists.
   * **Delete the Email:** Clean up by deleting the email from the folder.
   * **Check Email Status:** Verify if the email is marked as read or unread.
3.  **Test Sequence**

    **Initial Setup:**

    * **Check Connection:** Verify connection to the email server and get the connection ID.
    * **Login Test:** Confirm that logging in with stored credentials works.
    * **Folder Check:** Ensure the target folder exists on the email server.

    **Email Operations:**

    * **Send a Test Email:** Send an email with a specific subject.
    * **Retrieve Email ID:** Get the ID of the sent email from the inbox.
    * **Move the Email:** Move the email from the inbox to the target folder.
    * **Check Email Status:** Ensure the email in the target folder is marked as unread.

    **Email Importing:**

    * **Fetch the Email:** Import the email from the target folder into our system.
    * **Check Imported Email:** Ensure the imported email is correctly fetched and logged.

    **Log Verification:**

    * **Check Import Log:** Verify that the subject of the sent email is recorded in the import log.

    **Cleanup:**

    * **Delete Imported Document:** Remove the document that was imported from the email.
    * **Delete the Email:** Delete the sent and moved email from the folders to keep everything clean.

## Detailed Explanation of Each Test

* **Setup and Initialization:**
  * **Initialize Shared Data:** Prepare shared data for tests.
* **Email Connection Tests:**
  * **Get Connection ID:** Check if we can connect to the email server and get an ID for the connection.
  * **Login Verification:** Ensure that logging in to the email server works properly.
* **Folder Verification Tests:**
  * **Check Target Folder:** Make sure the target folder exists on the email server.
  * **Verify Folder Listing:** Ensure the list of folders from the server matches our expectations.
* **Email Sending and ID Retrieval:**
  * **Send an Email:** Send a test email with a specific subject and attachment.
  * **Get Email ID:** Retrieve the unique ID of this sent email from the inbox.
* **Email Moving and Status Checking:**
  * **Move Email to Folder:** Move the test email from the inbox to the target folder.
  * **Check Unread Status:** Ensure the email is marked as unread after moving.
* **Email Fetching and Response Validation:**
  * **Fetch Email from Folder:** Import the email from the target folder into our system.
  * **Validate Fetched Email:** Confirm that the fetched email is present in the response.
* **Import Log Verification:**
  * **Fetch Import Log:** Retrieve the log of imported emails.
  * **Check Email Subject in Log:** Ensure the subject of the test email is present in the import log.
* **Cleanup:**
  * **Delete Imported Document:** Remove the document that was imported from the email.
  * **Delete the Email:** Delete the test email from the inbox and the target folder to keep everything clean.

\\
