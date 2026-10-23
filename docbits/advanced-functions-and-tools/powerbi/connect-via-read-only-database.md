# Connect via Read-Only Database

This guide walks you through connecting **DocBits’ Read-Only Database to Power BI Desktop** using the **PostgreSQL ODBC driver**. It covers driver installation, ODBC configuration, Power BI integration, and scheduled refresh.

{% embed url="https://youtu.be/O1MtuXf_R_M" %}
{% endembed %}

#### 1. Install the PostgreSQL ODBC Driver

* Download the latest PostgreSQL ODBC driver (**psqlODBC**) from the official site:
  * [https://www.postgresql.org/ftp/odbc/releases/](https://www.postgresql.org/ftp/odbc/releases/)
* Run the installer and follow the setup wizard.

#### 2. Configure the ODBC Data Source

* Open **ODBC Data Source Administrator (64-bit)** via Control Panel or Windows Search.
* Go to the **System DSN** tab and click **Add**.
* Select **PostgreSQL Unicode(x64)** driver from the list and click **Finish**.
* Fill in the required fields with credentials from:\n  **DocBits → Settings → Document Processing → Module → AI Dashboard → Read-Only DB Access**

<figure><img src="../../.gitbook/assets/connect_read_only_4.png" alt="DocBits Read-Only DB Access panel showing username, password, database, host, port fields and the available tables list"><figcaption></figcaption></figure>

**Required Fields:**

* **Name:** A name for the connection (e.g., `Sandbox-Read_Only`)
* **Server:** Copy the host value from DocBits
* **Port:** Copy the port value from DocBits
* **Database:** Copy the database name from DocBits
* **Username:** Copy the username from DocBits
* **Password:** Copy the password from DocBits
* **SSL Mode:** Set to **Require** (ensures encrypted communication)

#### 3. Connect Read-Only DB to Power BI

* Open **Power BI Desktop**.
*   Select **Get Data** → **ODBC** → **Connect**.

    <figure><img src="../../.gitbook/assets/powerbi_get_data_odbc.png" alt="Power BI Get Data ODBC"><figcaption></figcaption></figure>
* From the DSN list, select your configured source (e.g., `Sandbox-Read_Only`).

<figure><img src="../../.gitbook/assets/connect_read_only_3.png" alt="Power BI From ODBC dialog with the Data source name (DSN) dropdown and Advanced options"><figcaption></figcaption></figure>

* Click **OK**. Enter credentials again if prompted.
  * If `password authentication failed for user` appears, verify the host, database, username and password. Enter the actual password in the credential dialog. Curly-brace escaping in an ODBC connection string is driver syntax; it is not a general fix for failed authentication.

#### 4. Load and Transform Data

* In the **Navigator** pane, expand the schema list.
* Open the **`public`** schema.
* Select the tables you want to import.

![Power BI Navigator pane showing the ODBC data source dsn-Sandbox-Read_Only with the public schema and its tables listed](../../.gitbook/assets/connect_read_only_1.png)

![Power BI Navigator with sandbox-doc2api tables such as supplier group, supplier header and task assignment, with Select Related Tables, Load and Transform Data buttons](../../.gitbook/assets/connect_read_only_2.png)

* Choose:
  * **Load** → Import directly into Power BI
  * **Transform Data** → Open Power Query for shaping and filtering before loading

#### 5. Visualize Your Data

* Use the Power BI report canvas to build dashboards.
* Drag fields, add slicers, choose chart types, and apply DAX calculations.
* Use **Power Query Editor** to clean or join data before creating visuals.
* Reference: [Power BI Documentation](https://learn.microsoft.com/en-us/power-bi/)

#### 6. Enable Scheduled Refresh (Optional)

Scheduled refresh depends on the workspace license/capacity, connector and connection mode. For this ODBC connection, configure a reachable gateway with the appropriate driver, DSN and credentials; check the current requirements in the official documentation.

* To keep your reports in sync with PostgreSQL:
* Publish your `.pbix` file to **Power BI Service**.
* Install the **Power BI Gateway** (Standard mode) on a machine with network access to PostgreSQL.
* In Power BI Service:
  * Open the semantic model → **Refresh** → **Schedule refresh** (the location can differ in older versions)
  * Map your DSN and provide credentials
* More informations [here](https://learn.microsoft.com/en-us/power-bi/connect-data/service-gateway-deployment-guidance).&#x20;

#### 7. Example Dashboards & Data Views&#x20;

<div><figure><img src="../../.gitbook/assets/powerbi_dashboard_example_1.png" alt="Power BI Dashboard Example 1"><figcaption></figcaption></figure> <figure><img src="../../.gitbook/assets/powerbi_dashboard_example_2.png" alt="Power BI Dashboard Example 2"><figcaption></figcaption></figure> <figure><img src="../../.gitbook/assets/powerbi_dashboard_example_3.png" alt="Power BI Dashboard Example 3"><figcaption></figcaption></figure> <figure><img src="../../.gitbook/assets/powerbi_dashboard_example_4.png" alt="Power BI Dashboard Example 4"><figcaption></figcaption></figure></div>

[Official documentation — ODBC](https://learn.microsoft.com/en-us/power-query/connectors/odbc)

[Official documentation — psqlODBC](https://odbc.postgresql.org/docs/config-opt.html)

[Official documentation — Power BI](https://learn.microsoft.com/en-us/power-bi/connect-data/refresh-scheduled-refresh)
