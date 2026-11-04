# Test: FTP Import Connection

#### Purpose

These tests ensure that our FTP import system works correctly. We verify that we can add a new FTP import connection, test the connection, activate/deactivate it, and clean it up afterward.



{% embed url="https://grafana.polydocs.io/d-solo/b6ad3a9c-260c-46a3-9ade-47691e743d4d/docbits?from=1715746603760&orgId=1&panelId=84&refresh=1m&to=1715768203760" %}

## Test Scenarios

1. **Setup:**
   * **Environment Variables:** Load necessary details like FTP server information and credentials from environment variables.
2.  **FTP Connection Tests:**

    **Add New Connection:**

    * **Test Add New FTP Import Connection (`test_add_new_ftp_import_connection`):**
      * Add a new FTP import connection with the given credentials and server details.
      * **Expected Outcome:** The connection should be added successfully.

    **Deactivate Connection:**

    * **Test Deactivate FTP Import Connection (`test_deactivate_ftp_import_connection`):**
      * Deactivate the newly added FTP import connection.
      * **Expected Outcome:** The connection should be deactivated successfully.

    **Test Connection:**

    * **Test FTP Connection (`test_test_ftp_connection`):**
      * Test if the FTP import connection can successfully connect to the FTP server.
      * **Expected Outcome:** The connection should be tested successfully.

    **Check Connection in List:**

    * **Test Check FTP Connection in List (`test_check_ftp_connection_in_list`):**
      * Check if the newly added FTP import connection is present in the list of connections.
      * **Expected Outcome:** The connection should be found in the list.

    **Check Connection Deactivated:**

    * **Test Check FTP Connection Deactivated (`test_check_ftp_connection_deactivated`):**
      * Verify that the FTP import connection is marked as inactive in the list.
      * **Expected Outcome:** The connection should be inactive.

    **Add Test Folder:**

    * **Test Add Test Folder to Connection (`test_add_test_folder_to_connection`):**
      * Add a default directory (test folder) to the FTP import connection.
      * **Expected Outcome:** The default directory should be added successfully.

    **Reactivate Connection:**

    * **Test Reactivate FTP Import Connection (`test_reactivate_ftp_import_connection`):**
      * Reactivate the previously deactivated FTP import connection.
      * **Expected Outcome:** The connection should be reactivated successfully.

    **Check Connection Reactivated:**

    * **Test Check FTP Connection Reactivated (`test_check_ftp_connection_reactivated`):**
      * Verify that the FTP import connection is marked as active in the list.
      * **Expected Outcome:** The connection should be active.

    **Cleanup:**

    * **Test Cleanup FTP Import (`test_cleanup_ftp_import`):**
      * Delete the FTP import connection to clean up after the tests.
      * **Expected Outcome:** The connection should be deleted successfully.

## Detailed Explanation of Each Test

* **Setup and Initialization:**
  * **Initialize Shared Data:** Prepare shared data for tests.
* **FTP Connection Tests:**
  * **Add New Connection:** Add a new FTP import connection with the provided credentials and server details.
  * **Deactivate Connection:** Deactivate the newly added FTP import connection.
  * **Test Connection:** Test if the FTP import connection can successfully connect to the FTP server.
  * **Check Connection in List:** Verify that the new FTP import connection is present in the list of connections.
  * **Check Connection Deactivated:** Confirm that the FTP import connection is marked as inactive in the list.
  * **Add Test Folder:** Add a default directory (test folder) to the FTP import connection.
  * **Reactivate Connection:** Reactivate the previously deactivated FTP import connection.
  * **Check Connection Reactivated:** Ensure that the FTP import connection is marked as active in the list.
  * **Cleanup:** Delete the FTP import connection to clean up after the tests.

\


