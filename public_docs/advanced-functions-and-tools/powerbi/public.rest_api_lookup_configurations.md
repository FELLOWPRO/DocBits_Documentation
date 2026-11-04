# public.rest\_api\_lookup\_configurations

## Tabelle `public.rest_api_lookup_configurations`

### Spalten

* `id`: internal
* `org_id`: ID to organisation
* `sub_org_id`: internal
* `data_key`: internal
* `url`: internal
* `method`: internal
* `params`: text
* `headers`: text
* `body`: text
* `body_type`: internal
* `authentication_type`: internal
* `authentication_json`: text
* `data_base_path`: internal
* `column_paths`: text
* `created_by`: integer
* `created_on`: timestamp with time zone
* `last_modified_on`: timestamp with time zone
* `is_deleted`: boolean
* `deleted_on`: timestamp with time zone
* `is_template`: boolean
* `is_dynamic`: boolean

### Analyse & Beschreibung

## Technical Documentation: `public.rest_api_lookup_configurations` Table

### Introduction

The `public.rest_api_lookup_configurations` table is designed to store configurations for REST API lookups within an organization. This table holds essential information for performing API requests, including details about the endpoints, authentication methods, and request/response configurations. It appears to be used for dynamically constructing API calls and parsing their results.

### Column Descriptions

#### id

* **Meaning**: A unique identifier for each configuration entry.
* **Role**: Primary key.
* **Typical Contents**: UUID strings like `5e9b3637-79a1-4535-99cf-9247dfa48960`.
* **Note**: This is the unique key for identifying a specific API lookup configuration.

#### org\_id

* **Meaning**: Identifier for the organization that owns the configuration.
* **Role**: Foreign key.
* **Typical Contents**: UUID strings representing organization IDs.
* **Note**: Links the configuration to an organization.

#### sub\_org\_id

* **Meaning**: Identifier for a sub-organization within the primary organization.
* **Role**: Foreign key.
* **Typical Contents**: UUID strings representing sub-organization IDs.
* **Note**: Allows further granularity within organizations.

#### data\_key

* **Meaning**: A label or key for identifying the data or API endpoint.
* **Role**: Descriptive field.
* **Typical Contents**: Descriptive text like `bank_codes`.
* **Note**: Used to distinguish between different types of data or end points.

#### url

* **Meaning**: The URL of the API endpoint to be called.
* **Role**: Descriptive field.
* **Typical Contents**: URL strings like `/M3/m3api-rest/v2/execute/CRS692MI/LstByID`.
* **Note**: Represents the endpoint to which the HTTP request is sent.

#### method

* **Meaning**: HTTP method used for the API request.
* **Role**: Descriptive field.
* **Typical Contents**: Common HTTP methods like `GET`.
* **Note**: Dictates the type of HTTP request to be performed.

#### params

* **Meaning**: Parameters to be included in the API request.
* **Role**: Configuration field.
* **Typical Contents**: JSON or key-value pairs (often `None` if not used).
* **Note**: Contains dynamic parameters for the request.

#### headers

* **Meaning**: HTTP headers to be included in the request.
* **Role**: Configuration field.
* **Typical Contents**: JSON or text data (often `None` if not used).
* **Note**: Used to include additional metadata in the request.

#### body

* **Meaning**: The body of the HTTP request.
* **Role**: Configuration field.
* **Typical Contents**: JSON data or other serialized data (often `None` if not used).
* **Note**: Contains the payload for POST/PUT requests.

#### body\_type

* **Meaning**: Specifies the format of the request body.
* **Role**: Descriptive field.
* **Typical Contents**: MIME types like `application/json`.
* **Note**: Indicates the content type of the body.

#### authentication\_type

* **Meaning**: Type of authentication used for the API request.
* **Role**: Descriptive field.
* **Typical Contents**: Authentication methods like `ionapi`.
* **Note**: Determines how the request will be authenticated.

#### authentication\_json

* **Meaning**: Details of the authentication configuration in JSON format.
* **Role**: Configuration field.
* **Typical Contents**: JSON strings with authentication information.
* **Note**: Contains credentials and endpoint details for authentication.

#### data\_base\_path

* **Meaning**: Path within the API response to extract data from.
* **Role**: Configuration field.
* **Typical Contents**: JSON path expressions like `$[results][0][records]`.
* **Note**: Used to parse the API response data.

#### column\_paths

* **Meaning**: Maps data fields to columns for extraction.
* **Role**: Configuration field.
* **Typical Contents**: JSON strings mapping API response fields to column names.
* **Note**: Facilitates data extraction from the API response.

#### created\_by

* **Meaning**: Identifier of the user who created the configuration.
* **Role**: Technical field.
* **Typical Contents**: Integer IDs like `1`.
* **Note**: Tracks the creator of the configuration entry.

#### created\_on

* **Meaning**: Timestamp when the configuration was created.
* **Role**: Technical field.
* **Typical Contents**: Timestamps like `2024-01-24T09:14:24.788788Z`.
* **Note**: Indicates the creation date and time.

#### last\_modified\_on

* **Meaning**: Timestamp of the last modification.
* **Role**: Technical field.
* **Typical Contents**: Timestamps (often `None` if not modified).
* **Note**: Records the last update time.

#### is\_deleted

* **Meaning**: Flag indicating if a configuration is marked as deleted.
* **Role**: Technical field.
* **Typical Contents**: Boolean values like `False`.
* **Note**: Used to soft delete configurations.

#### deleted\_on

* **Meaning**: Timestamp when the configuration was marked as deleted.
* **Role**: Technical field.
* **Typical Contents**: Timestamps (often a placeholder if not deleted).
* **Note**: Records when the configuration was marked as deleted.

#### is\_template

* **Meaning**: Indicates if the configuration serves as a template.
* **Role**: Descriptive field.
* **Typical Contents**: Boolean values like `True`.
* **Note**: Identifies templates for reuse.

#### is\_dynamic

* **Meaning**: Specifies if the configuration is dynamic.
* **Role**: Descriptive field.
* **Typical Contents**: Boolean values like `False`.
* **Note**: Determines if the configuration adjusts to changing data.
