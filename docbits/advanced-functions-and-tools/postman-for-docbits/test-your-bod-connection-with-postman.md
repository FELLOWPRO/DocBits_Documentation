# Test your BOD connection with Postman

## Overview

This page explains how to verify the successful processing of your BOD (Business Object Document) using Postman. You will test the relevant API endpoint by sending a request with your BOD mapping file. Follow the steps below to complete the process.

## Accessing Your API Key and BOD Mapping File

### Retrieving Your API Key

1.  Go to **Settings → Global Settings → Integration & SSO**.

    <figure><img src="../../.gitbook/assets/settings_integration.png" alt="Settings page in DocBits with the Global Settings navigation open and Integrations &amp; SSO highlighted among Document Types and Email Templates"><figcaption></figcaption></figure>
2.  You can either manually copy your **API key** or click the copy button to copy it to your clipboard.

    <figure><img src="../../.gitbook/assets/test_bod_connection_postman_1.png" alt="Integration &amp; SSO page in DocBits showing the API Key field with its copy button above the SSO Service Provider Settings section"><figcaption></figcaption></figure>

### **Downloading the BOD Mapping File**

1.  Go to **Settings → Document Processing → Export**.

    <figure><img src="../../.gitbook/assets/settings_export.png" alt="Settings page in DocBits with the Document Processing navigation open listing Import, OCR Settings, Classification and Extraction and Module"><figcaption></figcaption></figure>
2.  In the **Actions** column of the relevant export entry, click the three-dot menu and select **Edit**.

    <figure><img src="../../.gitbook/assets/test_bod_connection_postman_2.png" alt="Export settings page in DocBits with the rows google Invoice webhook and Infor LN Test Invoice and the Actions menu open"><figcaption></figcaption></figure>
3.  Locate the **BOD Mapping File** and click the **Download** button to save it.

    <figure><img src="../../.gitbook/assets/test_bod_connection_postman_3.png" alt="Infor ION dialog with the Title Test field and the ION-Mapping File, IDM Mapping File and BOD-Mapping File download buttons"><figcaption></figcaption></figure>

## Test the Endpoint in Postman

1.  **Paste the cURL Command in Postman**

    Open Postman and paste the following cURL command into the **Import** section. Postman will automatically configure the request.

    ```bash
    curl -X 'POST' \
      'https://api.docbits.com/prod-api/import/purchase_order_bod' \
      -H 'accept: application/json' \
      -H 'X-API-KEY:' \
      -H 'Content-Type: multipart/form-data' \
      -F 'org_id=' \
      -F 'sub_org_id=' \
      -F 'file=@file.xml;type=text/xml' \
      -F 'custom_fields_mapping='
    ```

    <figure><img src="../../.gitbook/assets/test_bod_connection_postman_4.png" alt="Postman workspace with the welcome screen, History tab and the Create a new request option"><figcaption></figcaption></figure>

    <figure><img src="../../.gitbook/assets/test_bod_connection_postman_5.png" alt="Postman Import dialog with the paste cURL field open to import the BOD request"><figcaption></figcaption></figure>
2.  **Set the API Key**\
    Go to the **Headers** tab, locate the `X-API-KEY` header, and paste your API key into the **Value** column.

    <figure><img src="../../.gitbook/assets/test_bod_connection_postman_6.png" alt="Postman request for https://api.docbits.com/prod-api/import/purchase_order_bod with the Headers tab and the X-API-KEY row"><figcaption></figcaption></figure>
3.  **Upload the BOD File**\
    Go to the **Body** tab, locate the `file` key, then click **Select Files** in the **Value** column and upload your BOD XML file.

    <figure><img src="../../.gitbook/assets/test_bod_connection_postman_7.png" alt="Postman request Body tab with form-data keys org_id, sub_org_id, file with Select Files and custom_fields_mapping"><figcaption></figcaption></figure>
4.  **Send the Request**\
    Click **Send** to make the API call.

    <figure><img src="../../.gitbook/assets/test_bod_connection_postman_8.png" alt="Postman request with the Authorization tab open and No Auth selected"><figcaption></figcaption></figure>
5.  **Verify the Response**\
    Check the response to confirm that your BOD was processed successfully.

    <figure><img src="../../.gitbook/assets/test_bod_connection_postman_9.png" alt="Postman response pane with Status 200 OK and the body message BOD processed successfully"><figcaption></figcaption></figure>
