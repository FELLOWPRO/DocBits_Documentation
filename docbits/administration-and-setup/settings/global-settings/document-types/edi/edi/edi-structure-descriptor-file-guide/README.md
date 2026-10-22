# EDI Structure Descriptor File Guide

## **1. Overview**

The **Structure Descriptor File** defines how repeating EDI segments (e.g., `N1`–`N4`) are grouped into structured JSON. It ensures:

* **Accurate parsing** of related elements as single units.
* **Consistent output** for downstream systems.

_For a full example with segment details, see_ [_Structure Descriptor Example_](edi-structure-descriptor.md)_._

## **2. Access & Basic Editing**

#### **Accessing the File**

1.  **Settings** → **Document Type** → \[Your Document (e.g., _Purchase Order_)] → **E-Doc.**\\

    <figure><img src="../../../../../../../.gitbook/assets/site-all-edi-list-en.png" alt="Existing EDI format with its four configured attributes."><figcaption><p>Existing EDI format with its four configured attributes.</p></figcaption></figure>
2. Under **E-Doc**, select your format (e.g., _EDI_ ).
3.  Click **Structure Descriptor**.\\

    <figure><img src="../../../../../../../.gitbook/assets/site-all-edi-detail-en.png" alt="Active STRUCTUREDESCRIPTOR attribute: JSON structure descriptor in the read-only editor."><figcaption><p>Active STRUCTUREDESCRIPTOR attribute: JSON structure descriptor in the read-only editor.</p></figcaption></figure>

#### **Draft Management**

* **Create a Draft**: Click the ✏️ pencil icon to begin editing.
* **Delete Drafts**: Use the 🗑️ trashcan icon to remove unused drafts.
* **Activate Changes**: Click the ✅ checkmark icon to approve and publish your changes.
  * <mark style="color:red;">**Note**</mark>: Activating a new version will **automatically deactivate** the previous one.

## 3. Preview Function (Preview Parsed XML)

The **Preview Function** allows you to test and preview how an uploaded EDI file is parsed using the current Structure Descriptor File.

#### Usage

* Upload an EDI file via the standard upload flow.
* Copy the **Document ID** of the uploaded file.
* Navigate to the **Structure Descriptor File** interface.
*   Open the **Preview Function.**\\

    <div align="left"></div>
* Enter the **Document ID** into the field and press **Test**.
* The resulting **structured XML output** will be displayed.

This is especially useful for debugging mappings and validating structural groupings in real time.



## 6. Video Walkthrough

A video guide for this file type is available on the [Videos page.](../edi-videos.md)\
Use it to follow along with setup, editing, and previewing.


The views show an existing configuration and version. Settings vary by document type and format. Validate changes in a draft before activation.
