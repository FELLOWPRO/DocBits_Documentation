# public.fellow\_kv\_table\_column\_rule

## Tabelle `public.fellow_kv_table_column_rule`

### Spalten

* `id`: internal
* `docType`: internal
* `tableName`: internal
* `dlfName`: internal
* `multi_line`: boolean
* `filterID1`: internal
* `filterID2`: internal
* `filterID3`: internal
* `tfidf_doc_id`: internal
* `tfidf_id`: internal
* `valuePattern`: internal
* `coordsY0`: integer
* `coordsY1`: integer
* `coordsX0`: integer
* `coordsX1`: integer
* `normalizedY0`: numeric
* `normalizedY1`: numeric
* `normalizedX0`: numeric
* `normalizedX1`: numeric
* `width`: integer
* `height`: integer
* `patternLeft`: internal
* `patternRight`: internal
* `patternAbove`: internal
* `patternBelow`: internal
* `wordLeft`: internal
* `wordAbove`: internal
* `ruleWeight`: integer
* `user_id`: integer
* `org_id`: ID to organisation
* `created_on`: timestamp with time zone
* `last_modified_on`: timestamp with time zone
* `is_deleted`: boolean
* `is_new`: boolean

### Analyse & Beschreibung

## Technical Documentation for `public.fellow_kv_table_column_rule`

### Introduction

The `public.fellow_kv_table_column_rule` table appears to be designed for storing rules and patterns for processing or extracting data from documents. This is inferred from the presence of fields such as `docType`, `tableName`, `dlfName`, and various pattern and coordinate-related fields. The table seems to facilitate the application of rules to different document types, enabling pattern recognition and data extraction from structured documents like invoices or contracts.

### Column Descriptions

#### id

* **Meaning**: Unique identifier for each rule.
* **Role**: Primary key.
* **Typical Contents**: UUID strings.
* **Note**: Essential for identifying each row uniquely.

#### docType

* **Meaning**: Type of document the rule applies to.
* **Role**: Descriptive field.
* **Typical Contents**: Document types like 'INVOICE', 'CONTRACT'.
* **Note**: Helps categorize rules by document type.

#### tableName

* **Meaning**: Name of the table where the rule is applied.
* **Role**: Descriptive field.
* **Typical Contents**: Table names like 'INVOICE\_TABLE'.
* **Note**: Indicates the context within which the rule is applied.

#### dlfName

* **Meaning**: Specific field or column name in the document.
* **Role**: Descriptive field.
* **Typical Contents**: Field names such as 'COUNTRY\_ORIGIN'.
* **Note**: Specifies the target field for data extraction.

#### multi\_line

* **Meaning**: Indicates whether the rule applies to multiline text.
* **Role**: Boolean flag.
* **Typical Contents**: `True` or `False`.
* **Note**: Useful for handling multiline text fields.

#### filterID1, filterID2, filterID3

* **Meaning**: Filters or conditions for applying the rule.
* **Role**: Descriptive or conditional fields.
* **Typical Contents**: Possibly strings representing filter conditions.
* **Note**: Used to refine rule application based on certain conditions.

#### tfidf\_doc\_id, tfidf\_id

* **Meaning**: Identifiers related to TF-IDF processing.
* **Role**: Foreign key-like roles or identifiers.
* **Typical Contents**: UUID strings.
* **Note**: Likely related to text analysis and feature extraction.

#### valuePattern

* **Meaning**: Regex pattern for value extraction.
* **Role**: Pattern field.
* **Typical Contents**: Regular expressions.
* **Note**: Defines the pattern used to identify and extract values.

#### coordsY0, coordsY1, coordsX0, coordsX1

* **Meaning**: Coordinates defining the bounding box for extraction.
* **Role**: Coordinate fields.
* **Typical Contents**: Integers representing pixel positions.
* **Note**: Define the area of interest in a document for data extraction.

#### normalizedY0, normalizedY1, normalizedX0, normalizedX1

* **Meaning**: Normalized coordinates for extraction.
* **Role**: Coordinate fields.
* **Typical Contents**: Numeric values representing proportional positions.
* **Note**: Used for resolution-independent area definitions.

#### width, height

* **Meaning**: Dimensions of the area defined by the coordinates.
* **Role**: Dimensional fields.
* **Typical Contents**: Integer values.
* **Note**: Helps in defining the size of the extraction area.

#### patternLeft, patternRight, patternAbove, patternBelow

* **Meaning**: Contextual patterns surrounding the target data.
* **Role**: Pattern fields.
* **Typical Contents**: Regular expressions.
* **Note**: Provide context for where data is located relative to other text.

#### wordLeft, wordAbove

* **Meaning**: Specific words located near the target data.
* **Role**: Contextual fields.
* **Typical Contents**: Specific words or phrases.
* **Note**: Helps in refining the search for target data based on nearby words.

#### ruleWeight

* **Meaning**: Significance or priority of the rule.
* **Role**: Weight or priority field.
* **Typical Contents**: Integer values.
* **Note**: Higher values might indicate higher priority or importance.

#### user\_id

* **Meaning**: Identifier of the user who created or modified the rule.
* **Role**: Foreign key.
* **Typical Contents**: Integer values.
* **Note**: Links the rule to a specific user.

#### org\_id

* **Meaning**: Identifier of the organization associated with the rule.
* **Role**: Foreign key.
* **Typical Contents**: UUID strings.
* **Note**: Associates the rule with an organization.

#### created\_on

* **Meaning**: Timestamp of when the rule was created.
* **Role**: Technical field.
* **Typical Contents**: Timestamp with time zone.
* **Note**: Useful for tracking the creation history of the rule.

#### last\_modified\_on

* **Meaning**: Timestamp of the last modification of the rule.
* **Role**: Technical field.
* **Typical Contents**: Timestamp with time zone or `None`.
* **Note**: Tracks changes to the rule over time.

#### is\_deleted

* **Meaning**: Indicates whether the rule is marked as deleted.
* **Role**: Boolean flag.
* **Typical Contents**: `True` or `False`.
* **Note**: Used for soft deletion of rules.

#### is\_new

* **Meaning**: Indicates whether the rule is newly created.
* **Role**: Boolean flag.
* **Typical Contents**: `True` or `False`.
* **Note**: Helps in identifying recently added rules.
