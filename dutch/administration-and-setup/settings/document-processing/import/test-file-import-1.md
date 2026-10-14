# Test: File Import 1

## Purpose

These tests are designed to ensure that our file import system works correctly. We specifically test the import of PDF and TIFF files into the system, ensuring that they are processed and stored successfully.

#### Test Setup and Cleanup

* **Setup:**
  * Before each test, we log a setup message.
  * **Cleanup:** After each test, we clean up by deleting any documents created by the test user from the database to ensure no leftover data affects subsequent tests.

#### Test Scenarios

1. **Import PDF File:**
   * **Test Import PDF (`test_import_pdf`):**
     * Import a PDF file (`FellowBananaInvoice.pdf`) into the system.
     * **Expected Outcome:** The file should be imported successfully, returning a document ID.
2. **Import TIFF File:**
   * **Test Import TIFF (`test_import_tiff`):**
     * Import a TIFF file (`TIFF_FILE.TIF`) into the system.
     * **Expected Outcome:** The file should be imported successfully, returning a document ID.

## Detailed Explanation of Each Test

* **Setup and Cleanup:**
  * **Logging:** A setup and cleanup message is logged for each test.
  * **Database Cleanup (`clean_documents`):** Deletes any documents created by the test user from the database to maintain a clean state.
*   **File Import Tests:**

    **Import PDF File:**

    * **Load User:** Load the test user.
    * **File Path:** Specify the path to the PDF file (`tests/files/pdfs/FellowBananaInvoice.pdf`).
    * **Import File:** Use the `FileImporter` class to import the PDF file.
    * **Check Response:** Ensure the response is a list containing a success message and a document ID.

    **Import TIFF File:**

    * **Load User:** Load the test user.
    * **File Path:** Specify the path to the TIFF file (`tests/files/pdfs/TIFF_FILE.TIF`).
    * **Import File:** Use the `FileImporter` class to import the TIFF file.
    * **Check Response:** Ensure the response is a list containing a success message and a document ID.

## Code Structure

* **Logger:** Used to log debug messages during setup, cleanup, and test execution.
* **Database Helper:** Executes queries without returning results for cleanup.
* **File Importer:** Handles the import of files into the system.
* **Fixtures:** `set_up` fixture to manage setup and cleanup for tests.
* **Tests:**
  * `test_import_pdf`: Tests importing a PDF file.
  * `test_import_tiff`: Tests importing a TIFF file.

#### Summary

These tests ensure that our file import functionality works as expected for both PDF and TIFF files. By following this approach, we verify that files are imported correctly and that the system can handle different file types without issues.
