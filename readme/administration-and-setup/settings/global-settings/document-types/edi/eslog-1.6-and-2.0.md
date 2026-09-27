# eSLOG 1.6 and 2.0

## Supported eSLOG Invoice Versions

Currently, **eSLOG Invoice versions 1.6 and 2.0** are supported.

For official eSLOG documentation, you can refer to [this link](https://epos.si/en/eslog).

Both eSLOG versions are enabled by default.

## Steps to Modify eSLOG Configuration

**Configure eSLOG:**

* Navigate to **Settings → Global Settings → Document Types → Invoice**.
*   Click on **E-Doc**.\\

    <figure><img src="../../../../../.gitbook/assets/zugferd_1.png" alt=""><figcaption></figcaption></figure>
* A list of all available e-docs will appear.
*   Locate the eSLOG version you want to modify.\\

    <figure><img src="../../../../../.gitbook/assets/image (383).png" alt=""><figcaption></figcaption></figure>

## **Transformation and XML Path Configuration:**

In the **transformation settings**, you can define the path to locate specific information within the XML file and save it in a new structure, making it easier to access the data.\
**Note:** If you use this functionality, you must use the newly created XML paths, not the original XML paths, in the **Preview** and **Extraction Path**.

### **Steps to Modify Transformation File:**

1. Open the **Transformation**.
2. Create a new draft by clicking the **pencil icon**.
3. Select the newly created draft.
4. Either create a new field or modify an existing one.
5. Set the desired path for data extraction.
6. Click **Save**.

## Preview PDF Configuration

The **Preview PDF Configuration** is used to generate a user-readable version of the document. You can customize it with HTML to match your needs.

### **Steps to Modify Preview File:**

1. Open the **Preview**.
2. Create a new draft by clicking the **pencil icon**.
3. Select the newly created draft.
4. Either create a new field or modify an existing one.
5. Set the desired path for data extraction.
6. Click **Save**.

## Extraction Paths Configuration

The **Extraction Paths Configuration** is used to extract data and populate fields in the **validation screen**, such as the invoice table or fields configured in the invoice layout.

### **Steps to Modify** **Extraction Paths**:

1. Open the **Extraction Paths**.
2. Create a new draft by clicking the **pencil icon**.
3. Select the newly created draft.
4. Create a new field or modify an existing one.
5.  The left side represents the **DocBits field ID**, which can be found in the **Settings → Global Settings → Document Types → Invoice → Fields**.\\

    <figure><img src="../../../../../.gitbook/assets/zugferd_3.png" alt=""><figcaption></figcaption></figure>

    <figure><img src="../../../../../.gitbook/assets/zugferd_4.png" alt=""><figcaption></figcaption></figure>
6. The right side represents the **path to the field** created in the Transformation.
7. Click **Save**.
