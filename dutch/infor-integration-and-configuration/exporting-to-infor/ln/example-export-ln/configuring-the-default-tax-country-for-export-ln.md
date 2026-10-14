# Configuring the Default Tax Country for Export LN

### Overview

The default Tax Country for export is set to **DE (Germany)** to prevent export errors. This can be changed in the mapping file by either:

* Defining a different static value.
* Mapping it dynamically to a field in DocBits.

<mark style="color:red;">**Note:**</mark> If the specified field does not exist or is empty, the export will default back to **DE**.

### Steps to Modify the Tax Country

#### 1. Obtain the Mapping File

* Navigate to **DocBits → Settings → Document Processing → Export**.
* Open the export configuration you want to modify.
*   Click on **Download** to obtain the mapping file.\


    <figure><img src="../../../../.gitbook/assets/iScreen Shoter - Google Chrome - 250220120028.jpg" alt=""><figcaption></figcaption></figure>
* Open the file in a text editor.

#### 2. Modify the Mapping File

Choose one of the two options below and apply the necessary changes.

**Option 1: Static Value**

To set a static Tax Country value, follow these steps:

1.  Define a new static field by adding `,TaxCountry` to the `StaticFields` line.

    ```properties
    StaticFields=FinancialCompany...,TaxCountry
    ```
2.  Set the country code by adding the following line:

    ```properties
    SF_TaxCountry=CountryCode
    ```

    Replace `CountryCode` with the actual country code, e.g., `ES` for Spain or `DE` for Germany:

    ```properties
    SF_TaxCountry=ES
    ```

**Example:**

```properties
StaticFields=FinancialCompany,TaxCountry
SF_TaxCountry=FR
```

<figure><img src="../../../../.gitbook/assets/image (415).png" alt=""><figcaption></figcaption></figure>

**Option 2: Dynamic Mapping from DocBits Field**

To dynamically map the Tax Country from a field in DocBits:

1.  Add `,TaxCountry` to the `HeaderFields` line:

    ```properties
    HeaderFields=SupplierCode,...,TaxCountry
    ```
2.  Define the corresponding field mapping:

    ```properties
    HF_TaxCountry=DocBits_Field_name
    ```

    Replace `DocBits_Field_Name` with the actual field name in DocBits:

    ```properties
    HF_TaxCountry=tax_country_1
    ```

**Example:**

```properties
HeaderFields=SupplierCode,TaxCountry
HF_TaxCountry=tax_country_1
```

<figure><img src="../../../../.gitbook/assets/image (412).png" alt=""><figcaption></figcaption></figure>

### Summary

* If the Tax Country is **not defined or the field is empty**, it defaults to **DE**.
* **Use a static value** if the Tax Country remains constant for all exports.
* **Use a dynamic field mapping** if the Tax Country varies per document.

By following these steps, you can successfully modify the Tax Country mapping to fit your needs.





