# Test your BOD connection with Postman

## Overview

This page explains how to verify the successful processing of your BOD (Business Object Document) using Postman. You will test the relevant API endpoint by sending a request with your BOD mapping file. Follow the steps below to complete the process.

## Accessing Your API Key and BOD Mapping File

### Retrieving Your API Key

1.  Go to **Settings → Global Settings → Integration & SSO**.

    <figure><img src="../../.gitbook/assets/settings_integration.png" alt="DocBits Settings page with Global Settings expanded and an arrow pointing at the Integration &amp; SSO entry"><figcaption></figcaption></figure>
2.  You can either manually copy your **API key** or click the copy button to copy it to your clipboard.

    <figure><img src="../../.gitbook/assets/test_bod_connection_postman_1.png" alt="Integration &amp; SSO settings with the API Key section expanded and an arrow pointing at the copy button next to the Key field"><figcaption></figcaption></figure>

### **Downloading the BOD Mapping File**

1.  Go to **Settings → Document Processing → Export**.

    <figure><img src="../../.gitbook/assets/settings_export.png" alt="DocBits Settings page with Document Processing expanded and an arrow pointing at the Export entry"><figcaption></figcaption></figure>
2.  In the **Actions** column of the relevant export entry, click the three-dot menu and select **Edit**.

    <figure><img src="../../.gitbook/assets/test_bod_connection_postman_2.png" alt="Export settings list with the actions menu open and an arrow pointing at Edit, next to Deactivate and Delete"><figcaption></figcaption></figure>
3.  Locate the **BOD Mapping File** and click the **Download** button to save it.

    <figure><img src="../../.gitbook/assets/test_bod_connection_postman_3.png" alt="Infor ION export dialog with Title, Sub-Organizations, Document Type and mapping file fields, an arrow at the BOD-Mapping File Download link"><figcaption></figcaption></figure>

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

    <figure><img src="../../.gitbook/assets/test_bod_connection_postman_4.png" alt="Postman start screen with an arrow and highlight on the Import button"><figcaption></figcaption></figure>

    <figure><img src="../../.gitbook/assets/test_bod_connection_postman_5.png" alt="Postman Import dialog with an arrow pointing at the Paste cURL to import field"><figcaption></figcaption></figure>
2.  **Set the API Key**\
    Go to the **Headers** tab, locate the `X-API-KEY` header, and paste your API key into the **Value** column.

    <figure><img src="../../.gitbook/assets/test_bod_connection_postman_6.png" alt="Postman POST request to the purchase_order_bod endpoint with the Headers tab showing accept and an empty X-API-KEY value"><figcaption></figcaption></figure>
3.  **Upload the BOD File**\
    Go to the **Body** tab, locate the `file` key, then click **Select Files** in the **Value** column and upload your BOD XML file.

    <figure><img src="../../.gitbook/assets/test_bod_connection_postman_7.png" alt="Postman request Body tab with form-data selected and org_id, sub_org_id, file and custom_fields_mapping keys, arrow at Select Files"><figcaption></figcaption></figure>
4.  **Send the Request**\
    Click **Send** to make the API call.

    <figure><img src="../../.gitbook/assets/test_bod_connection_postman_8.png" alt="Postman request with the Authorization tab set to No Auth and an arrow pointing at the Send button"><figcaption></figcaption></figure>
5.  **Verify the Response**\
    Check the response to confirm that your BOD was processed successfully.

    <figure><img src="../../.gitbook/assets/test_bod_connection_postman_9.png" alt="Postman response showing status 200 OK with JSON success true and message BOD processed successfully"><figcaption></figcaption></figure>
