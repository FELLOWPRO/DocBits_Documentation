# Send HTTPS Request

<figure><img src="../../../../.gitbook/assets/image (4) (1) (1) (1) (1) (1).png" alt="" width="563"><figcaption></figcaption></figure>

## **Purpose:**

This DocBits card is designed to facilitate interaction with external systems by sending HTTPS requests to specified URLs. It enables workflows to perform actions like data retrieval, updates, or deletion by making API calls, ensuring seamless integration with external services.

## **Functionality:**

* **HTTPS Request Execution:** The card sends a request to a specified URL using the configured HTTP method (e.g., GET, POST, PUT, DELETE).
* **Headers and Parameters:** Users can include custom headers and query parameters to ensure the request meets the requirements of the external API.
* **Request Data:** Allows users to define the data payload (if applicable) to be sent with the request, such as JSON or form-encoded data.
* **Response Evaluation:** The workflow checks if the received status code matches the expected value, ensuring successful communication before proceeding.
* **Supported HTTP Methods:**
  * GET: Retrieves data from the specified URL.
  * POST: Submits data to the specified URL to create resources.
  * PUT: Updates existing resources at the specified URL.
  * DELETE: Removes resources from the specified URL.

## **Usage:**

This card is particularly useful in scenarios where workflows need to interact with external APIs for data exchange, such as sending updates to a CRM, retrieving order statuses, or posting new entries to a database.

## **Example Scenario:**

* A user configures the card to send a POST request to an external order management system with a payload containing new order details. Custom headers are added to include API authentication tokens. The card is set to continue only if the response status code is 201 (Created). If the status code differs, the workflow triggers an error notification for manual intervention.

By using the "Send HTTPS Request" card, organizations can automate external integrations, improve communication between systems, and streamline complex workflows.
