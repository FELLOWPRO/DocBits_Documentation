# Script

<figure><img src="../../../../../.gitbook/assets/Bildschirmfoto 2024-05-08 um 09.43.25.png" alt=""><figcaption></figcaption></figure>

{% embed url="https://youtu.be/n8NpWWIjmlA" %}
DocBits Document Scripts Explained: Automate Custom Logic in Your Document Workflow
{% endembed %}

#### Overview

Scripts in Docbits are typically written in a scripting language supported by the system Python. They are triggered during the document processing workflow to apply complex business logic or to ensure data integrity and accuracy before the data is further processed or stored.

#### Key Features and Options

1. **Script Management**:
   * **Name**: Each script is given a unique name for identification.
   * **Document Type**: Associates the script with a specific document type, determining which documents the script will be applied to.
   * **Trigger On**: Defines when the script is triggered (e.g., on document upload, before data export, after data validation).
   * **Active/Inactive Status**: Allows administrators to activate or deactivate scripts without deleting them, providing flexibility in testing and deployment.
2. **Script Editor**:
   * Provides an interface where scripts can be written and edited. The editor typically supports syntax highlighting, error highlighting, and other features to assist in script development.
   * **Example Script**: Scripts can include operations such as looping through invoice lines to validate totals or to remove entries that do not meet certain criteria.

<figure><img src="../../../../../.gitbook/assets/Bildschirmfoto 2024-05-08 um 09.43.37.png" alt=""><figcaption></figcaption></figure>
