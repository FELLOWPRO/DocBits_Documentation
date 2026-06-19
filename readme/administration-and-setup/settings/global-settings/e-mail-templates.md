# E-Mail templates

## **Overview**

Email Templates allow you to customize automated email notifications sent from DocBits. Templates can include dynamic fields (e.g., `{{FieldID}}`), images, and HTML formatting.

## **Accessing Email Templates**

1.  Navigate to:\n    **Settings → Global Settings → Email Templates**\

    <figure><img src="../../../.gitbook/assets/email_templates_menu_navigation.png" alt="Email Templates Menu Navigation"><figcaption></figcaption></figure>
2. The dashboard displays all templates with:
   * **Name**
   * **Subject**
   * **Last Modified** date
   * **Actions** (Edit or Delete).

<figure><img src="../../../.gitbook/assets/email_templates_dashboard_list.png" alt="Email Templates Dashboard List"><figcaption></figcaption></figure>

## **Creating a New Template**

#### **1 Basic Setup**

* Click **New**.
* Fill in the fields on the right:
  * **Name**: Template identifier (e.g., "Document Error").
  * **Subject**: Email subject line (e.g., "Action Required: Document Error").
  *   **Document Type**: Select from the dropdown (e.g., "Invoice").\

      <div align="center"><figure><img src="../../../.gitbook/assets/create_new_email_template_form.png" alt="Create New Email Template Form"><figcaption></figcaption></figure></div>

You can also enable **Include Document As Attachment** to attach the source document to the email.

#### **2 Template Editor**

* **Menu**: Format text, add links, or insert tables.
* **HTML Editor**: Click the `<>` icon to edit raw HTML.
* **Add Images**: Use the **Upload** function.
*   **Dynamic Fields:** Insert document field values by

    * **Variable Field Option**: Select from a dropdown.
    * **Manual Entry**: Type `{{FieldID}}` (e.g., `{{InvoiceNumber}}`).

    <figure><img src="../../../.gitbook/assets/email_templates_4.png" alt=""><figcaption></figcaption></figure>

#### **3 Saving**

* Click **Save** to store the template.

## **Sending a Test Email**

1.  Open the template and click **Send Test**.\

    <figure><img src="../../../.gitbook/assets/send_test_email_button.png" alt="Send Test Email Button"><figcaption></figcaption></figure>
2. Enter:
   * **Recipient Email** (required).
   * **Field Values** (optional; mock data for placeholders).\
     \
     ![](<../../../.gitbook/assets/test_email_configuration_dialog.png>)
3. Review the test email and adjust the template if needed.

## **Using Templates in Notifications**

Saved templates can be linked to [**Email Notification**](email-notification/) workflows (e.g., approval reminders, status updates).