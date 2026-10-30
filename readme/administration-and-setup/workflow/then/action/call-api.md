# Call Api

<figure><img src="../../../../.gitbook/assets/Then_Call_API.png" alt="" width="563"><figcaption></figcaption></figure>

## Purpose:

The **"Call API"** workflow card allows users to make HTTP requests to specified API endpoints directly from the workflow. This card supports various HTTP methods and enables dynamic interaction with external systems by sending parameters and data. It streamlines integration with third-party services and custom APIs, ensuring seamless communication.

## Components of the Card:

1. **API Endpoint**
   * **Description:** The target endpoint of the **DocBits API** that this card will interact with.
   * **Detail:** A text field where users specify the endpoint for the API request.
2. **HTTP Method**
   * **Description:** The type of HTTP request to be made.
   * **Options:**
     1. **GET:** Retrieves data from the specified endpoint.
     2. **POST:** Sends data to the endpoint.
     3. **PUT:** Updates existing data at the endpoint.
     4. **DELETE:** Removes data at the endpoint.
3. **Parameters**
   * **Description:** Query parameters to be included in the API request.
   * **Detail:** A text field or list for entering key-value pairs for the request URL.
4. **Data**
   1. **Description:** The payload to be sent in the body of the API request (applicable for POST and PUT methods).
   2. **Detail:** A field for entering the data in JSON.

## Functionality:

**Condition Evaluation:** The system evaluates the conditions defined in the "Where" and "And Sections":

* If both conditions are **true**, the API request is executed as configured.
* If either condition is **false**, the card does not execute, and no API call is made.

**API Request Execution:**

* The card sends the HTTP request to the specified endpoint using the selected method.
* Any provided parameters are appended to the URL, and the data is included in the request body (if applicable).

## Setup and Configuration:

1. **Define API Endpoint:**\
   Enter the URL of the API you wish to call.
2. **Select HTTP Method:**\
   Choose one of the supported methods (GET, POST, PUT, DELETE) based on your API's requirements.
3. **Provide Parameters:**\
   Add any required query parameters as key-value pairs.
4. **Include Data (if applicable):**\
   For POST or PUT methods, specify the data to be sent in the request body.
5. **Condition Configuration:**\
   Configure the "Where" and "And Sections" to define when the API call should occur.

## Conclusion:

The **"Call API"** workflow card enhances workflow automation by enabling direct interaction with external systems. By providing flexible configurations for endpoints, methods, and data, it ensures workflows can integrate seamlessly with third-party APIs or custom backends. The ability to conditionally execute API calls ensures precision and efficiency in automating external communications.

***
