# Create an Infor ION API endpoint for DocBits exports

An Infor administrator configures the API Gateway endpoint for the **specific DocBits environment and organisation**. The old screenshots on this page showed one historical Infor tenant, a fixed `api.docbits.com` example and an older DocBits Export form. Use the approved target URL, API key and OpenAPI document for your actual environment. No Infor tenant was connected or endpoint saved for this update.

## Before you start

Collect the target DocBits API URL, the approved API key and its header name, the OpenAPI URL, and the intended Infor and DocBits environments from your integration administrator. Keep keys and `.ionapi` files out of tickets, screenshots and the Git repository. Confirm that a test endpoint cannot route to production.

## Configure Infor API Gateway

1. In **Available APIs**, create a **Custom or Non-Infor** API suite for the target environment. See Infor's [API suite instructions](https://docs.infor.com/inforos/2025.x/en-us/useradminlib_cloud/apigatewayag_cloud/gyy1489512842881.html).
2. Add an endpoint to the suite with the approved **Target Endpoint URL**. Select the authentication type required by that endpoint. For **API Key**, Infor asks for a **Key Name** and **Key Value**; use the name specified by the DocBits API contract and the key issued for this organisation. See Infor's [endpoint fields](https://docs.infor.com/inforos/2024.x/en-us/useradminlib_cloud/apigatewayag_cloud/bmg1489588707659.html). Do not copy a key from a different environment.
3. Add the environment's OpenAPI/Swagger URL under the endpoint's **Documentation** settings, following Infor's [documentation instructions](https://docs.infor.com/ionapi/2021-x/en-us/ionapiag_cloud/tzr1489597424134.html). Verify that the endpoint appears in [API metadata](https://docs.infor.com/ionapi/latest/en-us/ionapiag_cloud/tdr1489674063627.html).
4. With the Infor administrator, verify the target URL, authentication, proxy path and a safe non-production call before using the endpoint in an ION document flow. Saving an API suite alone does not prove that a document was delivered.

## Configure export in DocBits

In the intended DocBits organisation, open **Settings → Export** and select **New**. The English Sandbox Test A organisation shown below has no saved configuration.

![Current English DocBits Sandbox Export list with New action and no saved configuration.](../../.gitbook/assets/dbdc-197-export-list-en.png)

Enter a **Configuration Title**, choose the **Document Type**, and select a **Sub-Organization** only if needed. Set **Export** to **Infor** and **Infor Type** to **Infor IDM + ION BOD**. The current form then asks for **Deployment Type** (**CLOUD** or **ON-PREMISE**), an **ION API File** (`.ionapi`, required), **IDM Mapping File** (`.properties`) and **BOD Mapping File** (`.properties`). Obtain these tenant-specific files from the administrator. The screenshot deliberately leaves all uploads empty.

![Current English DocBits Sandbox Infor IDM + ION BOD export form with deployment choices and empty ION API, IDM and BOD file uploads.](../../.gitbook/assets/dbdc-197-export-ion-bod-en.png)

After the administrator validates the ION route, save the configuration and test one non-production document. Check its status in DocBits and Infor ION. A saved form or API metadata entry does not prove a successful export.
