# Functions

**Functional Documentation**

This module contains functions for manipulating document data and performing various operations related to document fields.

## **Functions**

1. ### **set\_field\_value(document\_data, field\_name, value)**
   * Description: Sets the value of a field in the document data.
   * Parameters:
     * `document_data` (dict): The document data containing field information.
     * `field_name` (str): The name of the field to set.
     * `value`: The value to set for the field.
   *   Example:

       `set_field_value(document_data, "name", "John Doe")`
2. ### **set\_date\_value(document\_data, field\_name, value)**
   * Description: Sets the value of a date field in the document data.
   * Parameters:
     * `document_data` (dict): The document data containing field information.
     * `field_name` (str): The name of the date field to set.
     * `value`: The date value to set in ISO format (e.g., "2020-12-31").
   *   Example:

       `set_date_value(document_data, "date_of_birth", "1990-05-15")`
3. ### **set\_amount\_value(document\_data, field\_name, value)**
   * Description: Sets the value of an amount field in the document data.
   * Parameters and example usage similar to `set_field_value`.
4. ### **set\_is\_required(document\_data, field\_name, value)**
   * Description: Sets the 'is\_required' attribute of a field in the document data.
   * Parameters and example usage similar to `set_field_value`.
5. ### **set\_force\_validation(document\_data, field\_name, value)**
   * Description: Sets the 'force\_validation' attribute of a field in the document data.
   * Parameters and example usage similar to `set_field_value`.
6. ### **set\_field\_attribute(document\_data, field\_name, attribute\_name, value)**
   * Description: Sets a custom attribute of a field in the document data.
   * Parameters:
     * `attribute_name` (str): The name of the attribute to set.
     * `value`: The value to set for the attribute.
   *   Example:

       `set_field_attribute(document_data, "address", "is_verified", True)`
7. ### **get\_field\_value(document\_data, field\_name, default\_value=None, is\_clean=False)**
   * Description: Gets the value of a field from the document data.
   * Parameters and example usage similar to `set_field_value`.
8. ### **create\_new\_field(field\_name, value="")**
   * Description: Creates a new field with the specified name and value.
   * Parameters:
     * `field_name` (str): The name of the field to create.
     * `value`: The initial value for the field (default is an empty string).
   *   Example:

       `create_new_field("address", "123 Main St")`
9. ### **delete\_field(document\_data, field\_name)**
   * Description: Deletes a field from the document data.
   * Parameters and example usage similar to `set_field_value`.
10. ### **update\_document\_status\_with\_doc\_id(doc\_id, user, org\_id, status, message=None, doc\_classification\_class=None)**
    * Description: Updates the status of a document with the specified ID.
    * Parameters:
      * `doc_id` (str): The ID of the document to update.
      * `user`: The user performing the update (either user ID or UserAuthentication object).
      * `org_id`: The ID of the organization to which the document belongs.
      * `status` (str): The new status of the document.
      * `message`: Optional message associated with the status update.
      * `doc_classification_class`: Optional document classification class.
    *   Example:

        `update_document_status_with_doc_id("123456", user, org_id, "approved", "Document approved")`
11. ### **is\_supplier\_valid(user: UserAuthentication, filter\_data\_json, sub\_org\_id=None)**
    * Description: Checks if a supplier is valid based on the provided criteria.
    * Parameters:
      * `user` (UserAuthentication): The authenticated user.
      * `filter_data_json`: Filter criteria for validating the supplier.
      * `sub_org_id`: Optional sub-organization ID for filtering.
    *   Example:

        `is_supplier_valid(user, {"name": "Supplier Inc."})`
12. ### **set\_field\_as\_invalid(document\_data, field\_name, message, code=None)**
    * Description: Marks a field as invalid in the document data.
    * Parameters:
      * `document_data` (dict): The document data containing field information.
      * `field_name` (str): The name of the field to mark as invalid.
      * `message` (str): The validation message for the field.
      * `code` (optional): Error code for the validation (default is None).
    *   Example:

        `set_field_as_invalid(document_data, "email", "Invalid email format", "EMAIL_FORMAT_INVALID")`
13. ### **compare\_values(value1, value2)**
    * Description: Compares two values for equality, handling various data types.
    * Parameters:
      * `value1`: The first value to compare.
      * `value2`: The second value to compare.
    *   Example:

        `compare_values(10, "10")`

\

