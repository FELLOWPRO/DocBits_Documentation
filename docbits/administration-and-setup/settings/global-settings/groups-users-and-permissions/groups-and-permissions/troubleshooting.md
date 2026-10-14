# Troubleshooting Access Control & Permissions Issues

If users are experiencing unexpected access restrictions—such as missing documents, inability to edit fields, or denied actions—use the following checklist to identify and resolve the issue based on how permissions are configured in DocBits.

### 1. Verify If Access Control Is Enabled

Access Control settings only apply if the feature is **enabled**.

* Navigate to: `Settings` > `Document Processing` > `Module`.
* Ensure the **Access Control** switch is turned **on**.
* If disabled, all users typically have unrestricted access regardless of group or field permissions.

### 2. Check Group Assignments

Ensure the user is correctly assigned to the appropriate group(s):

* Navigate to: `Settings` > `Global Settings` > `Groups, Users and Permissions`.
* Select **Groups and Permissions**.
* Confirm the user is listed under the expected group.
* If the group uses specific access control, missing group assignment will block access to documents and actions.

### 3. Review Group Access Permissions

Access is granted per document type and per action:

* In the **Access Control** screen for the group, check the document type (e.g., Invoice, Purchase Order).
* Validate permissions like:
  * **List**, **View**, **Edit**, **Delete**, **Mass Update**
  * **Approval Levels** (1st, 2nd), **Unlock Document**
* Ensure the access level is not limited to **Owner** or **Admin** unless appropriate.

### 4. Confirm Field-Level Permissions

Access can also be restricted at the **field level**, which may block editing or visibility:

* In the group’s Access Control configuration, navigate to the document type and check field-level settings.
* Confirm whether fields are set to:
  * **Read/Write**, **Read Only**, **Owner Write**, **None**
* Adjust if necessary based on the user's role.

### 5. Check the "Only Assigned Documents" Setting

This global setting limits document visibility:

* Navigate to: `Settings` > `Global Settings` > `Groups, Users and Permissions`.
* If **Only Assigned Documents** is **enabled**, users can only see documents explicitly assigned to them or their group.
* If users can’t see expected documents:
  * Check document assignments.
  * Disable the setting temporarily to test if it’s the root cause.

### 6. Test with a Known-Working User or Group

To isolate the issue:

* Log in with a user from a group that has confirmed access.
* Compare document visibility and available actions.
* This helps determine if the issue is user-specific, group-specific, or system-wide.

### 7. Recheck Document Assignments

If “Only Assigned Documents” is **enabled**, ensure:

* The document is **assigned** to the user or one of their groups.
* Use the assignment controls in the document detail view to make or review assignments.

### 8. Reset or Reconfigure Permissions

If permissions were recently changed or users were moved between groups:

* Reconfirm that Access Control settings reflect the new group configurations.
* Adjust field and document permissions as needed.
* If unsure, create a test group with broad permissions and test access behavior before applying changes to live groups.
