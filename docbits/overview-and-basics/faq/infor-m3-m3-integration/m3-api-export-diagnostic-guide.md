# M3 API Export Diagnostic Guide

### 1. Initial Setup

Before you begin troubleshooting, ensure you’re familiar with the expected inputs for the M3 endpoint you're working with.

#### 1.1 Access M3 API Documentation

* Log in to **M3**.
* Go to **API Section → API Documentation**.
* Locate and select the relevant endpoint (e.g., `APS450MI` for invoice-related exports).
* Choose the appropriate function (e.g., `Add`).

#### 1.2 Understand API Requirements

* Review all **required fields** in the API documentation.
* Pay attention to important fields like:
  * `DIVI`
  * `ACDT` (accounting date)
  * `CUCD` (currency code)
  * `SINO` (supplier invoice number)
* Confirm field **data types**, **casing**, and **formatting rules** (e.g., `YYYY-MM-DD` for dates).



### 2. Testing API Calls Directly in M3

This step verifies that the M3 API behaves as expected using manual inputs.

#### 2.1 Generate a Test Request in M3

* In the M3 API Documentation tool:
  * Fill in test data for required fields.
  * Click **Run** to execute the request.
  * Copy the resulting **cURL** and **JSON body**.

#### 2.2 Debug Using Postman

* Open **Postman** and create a new **POST** request.
* Paste the JSON body or cURL.
* Add necessary headers (e.g., authorization).
* Click **Send** and observe the result:
  * `200 OK`: The request was successful.
  * Error: Review the message for details on what went wrong.



### 3. Comparing M3 API with DocBits Mapping

Once you’ve confirmed the API works with test data, compare it to what DocBits is actually sending.

#### 3.1 Export Sample Data from DocBits

*   Open the **DocBits API documentation**:

    Use the **/export/get\_infor\_export\_api\_json** endpoint.
* Enter the **Document ID** of a problematic document.
* Run the export to view the **JSON payload** that DocBits will send to M3.

#### 3.2 Compare API Payloads

* Place the **M3 test JSON** and the **DocBits export JSON** side by side.
* Check for:
  * **Field Names**: Ensure names match _exactly_, including case (`DIVI` ≠ `divi`).
  * **Data Types**: Verify strings, numbers, and dates are properly formatted.
  * **Missing Fields**: Identify any fields present in M3’s request but missing in DocBits.



### 4. Troubleshooting Common Issues

| Issue                           | Likely Cause                              | Fix                                                             |
| ------------------------------- | ----------------------------------------- | --------------------------------------------------------------- |
| Missing field error             | A required field is not mapped in DocBits | Add the missing field in the DocBits export configuration.      |
| Field casing mismatch (`DIVI`)  | M3 is case-sensitive                      | Use the correct casing in the field mapping.                    |
| Invalid `accountingDate` format | Wrong or missing date                     | Adjust to the format expected by M3 (e.g., `YYYY-MM-DD`).       |
| Unexpected API error            | Extra or unrecognized fields              | Compare with known working payloads and clean unnecessary data. |

### 5. If Issues Persist

If the issue isn’t resolved after following the above steps:

1. **Document** the problem:
   * Error message and status code
   * Sample M3 request and DocBits export JSON
2. **Summarize** your troubleshooting:
   * What you’ve tried
   * Key differences observed between test and failing payloads
3. **Escalate** to a developer:
   * Include all data and findings
   * Highlight suspected problem areas
