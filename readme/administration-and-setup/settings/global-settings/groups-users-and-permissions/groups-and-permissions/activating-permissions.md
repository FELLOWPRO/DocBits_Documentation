# Activating Permissions

{% embed url="https://youtu.be/xE4RQnbOMug" %}
DocBits Groups & Permissions Tutorial: Set User Roles, Access Rights & Secure Your Workspace
{% endembed %}

Enabling or disabling the permission system using the switch has various effects on the functionality in DocBits.

## **Enabling the permission system:**

<figure><img src="../../../../../.gitbook/assets/image (174).png" alt=""><figcaption></figcaption></figure>

* When the permission system is enabled, the access permissions for users and groups are applied.
* Users are only granted access to the resources they are explicitly authorized to access based on the permissions assigned.
* Administrators can manage the permissions for individual users and groups and ensure that only authorized people can view or edit the data.

<figure><img src="../../../../../.gitbook/assets/image (176).png" alt=""><figcaption></figcaption></figure>

## Only Assigned Documents

<figure><img src="../../../../../.gitbook/assets/image (346).png" alt=""><figcaption></figcaption></figure>

The **Only Assigned Documents** toggle button controls the visibility of documents for users based on their group assignments. When enabled, users can only view documents that are specifically assigned to them or a group they belong to. When disabled, users with the appropriate view permission can see all documents, regardless of assignment.

#### Functionality

* **Off State (Default)**:
  * When the toggle is off, users who are part of a group can view all documents if they have the appropriate view permission. Document assignment does not affect visibility.
* **On State**:
  * When the toggle is on, users can only view documents that are explicitly assigned to them or a group they are a part of. This enforces stricter document visibility based on group assignments.

#### Example Scenario

1. **Default (Off State)**:
   * A user who is part of the "Sales" group can see all documents in the system that they have permission to view, even if they are not assigned to those documents.
2. **Enabled (On State)**:
   * A user in the "Sales" group can only view documents that are assigned to them or the "Sales" group, restricting access to documents outside of their assignments.

## Disabling the permission system:

<figure><img src="../../../../../.gitbook/assets/image (173).png" alt=""><figcaption></figcaption></figure>

* When the permission system is disabled, all access permissions are removed and users typically have unrestricted access to all resources.
* This can be useful when open collaboration is temporarily required without the restrictions of access control.
* However, there may be an increased risk of data leakage or unauthorized access as users may be able to access sensitive information they are not authorized to access.

Enabling or disabling the permission system is an important decision based on the security requirements and the way the organization operates. In environments where privacy and access control are critical, it is common to leave the permission system enabled to ensure data integrity and confidentiality. In other cases, disabling the permission system may be temporarily necessary to facilitate collaboration, but should be used with caution to minimize potential security risks.
