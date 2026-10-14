# Editing Email Templates

<figure><img src="../../../.gitbook/assets/supplier_email_templates.png" alt="Supplier Email Templates"><figcaption><p>Supplier Email Templates Page</p></figcaption></figure>

### Overview

The Email Templates feature allows administrators to create and customize email communications that are automatically sent to suppliers. One of the key elements used in these templates is the `{{magic_link}}`, which provides a dynamic link tailored to each recipient.

#### What is `{{magic_link}}`?

The `{{magic_link}}` is a placeholder that is dynamically replaced with a unique URL when the email is sent. This URL usually directs the recipient to complete an action, such as registration, approval, or accessing a specific part of the supplier portal.

### Editing Email Templates

<figure><img src="../../../.gitbook/assets/Bildschirmfoto 2024-08-25 um 12.35.53.png" alt=""><figcaption></figcaption></figure>

#### Accessing the Email Template Editor

1. **Navigate to Email Templates**:
   * Go to the **Email Templates** section from the main menu.
2. **Select a Template to Edit**:
   * Choose the email template you want to edit by clicking on the template name (e.g., "Supplier Invitation Email").
3. **Edit the Template**:
   * The editor allows you to modify both the HTML code and the visual design of the email.
   * You can switch between visual editing and code editing using the provided tabs.

<figure><img src="../../../.gitbook/assets/Bildschirmfoto 2024-08-25 um 12.36.41.png" alt=""><figcaption></figcaption></figure>

#### Defining `{{magic_link}}` as a Link

To define `{{magic_link}}` as a clickable link in the email, you need to ensure that it is properly formatted in the HTML code of the template. Follow these steps:

1. **Locate the Link Section in the HTML Code**:
   * In the code editor, find the section where you want the magic link to appear. This is usually within an `<a>` (anchor) tag.
2.  **Insert the `{{magic_link}}` Placeholder**:

    * Replace the `href` attribute of the anchor tag with `{{magic_link}}`.
    * Ensure the link is styled appropriately for the email template. Here's an example:

    ```html
    <a href="{{magic_link}}" target="_blank" style="
        background-color: #B7184B;
        border-radius: 25px;
        font-family: 'Montserrat', Arial, sans-serif;
        font-size: 14px;
        font-weight: bold;
        padding: 12px 25px;
        color: #FFFFFF;
        text-decoration: none;
        display: inline-block;
        cursor: pointer;">
        Complete Registration
    </a>
    ```

### 3. Customize the Link Text:

• Modify the text between the opening \<a> and closing \</a> tags to reflect the action you want the user to take. For example, “Complete Registration” or “Access Your Account”.

4\. Save and Test the Template:

• After making the changes, click the Save button.

• You can use the Send Test button to send a test email to ensure that the link is working as expected.

## Best Practices for Using \{{magic\_link\}}

• Link Placement: Place the \{{magic\_link\}} prominently in the email to ensure it is easily accessible to recipients.

• Clear Call to Action: The text within the link should be a clear call to action, such as “Complete Registration” or “Confirm Your Email.”

• Styling: Ensure that the link is styled consistently with the rest of the email template and stands out visually.

• Testing: Always send a test email after editing the template to verify that the \{{magic\_link\}} resolves correctly and the styling is appropriate.

## Conclusion

By properly defining the \{{magic\_link\}} in your email templates, you can ensure that recipients receive a personalized and actionable email that guides them to the appropriate task within your supplier portal. This enhances the user experience and ensures smooth onboarding and communication processes.

\


This documentation provides step-by-step instructions for administrators on how to define and use the \{{magic\_link\}} in email templates, ensuring that emails are both functional and visually appealing.
