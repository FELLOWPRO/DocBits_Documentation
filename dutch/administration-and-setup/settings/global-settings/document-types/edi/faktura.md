# Faktura

## Display attribute on every line item

If you want to display a specific attribute (like the Purchase Order number) on every line item, follow the steps below. The approach will differ depending on whether you need the attribute in the JSON extraction or in the XSL output.

<figure><img src="../../../../../.gitbook/assets/Screenshot 2025-01-28 at 14.33.16.png" alt=""><figcaption></figcaption></figure>

### Method 1: Display Attribute in the JSON Extraction (DocBits config)

1. Go to **Settings**
2. Go to **Document Types**
3. Select **Invoice/E-Doc**

<figure><img src="../../../../../.gitbook/assets/Screenshot 2025-01-28 at 15.07.58.png" alt=""><figcaption></figcaption></figure>

4. Open the **"FATTURAPA"** tab
5. Click on **JSON**

<figure><img src="../../../../../.gitbook/assets/Screenshot 2025-01-28 at 15.01.13.png" alt=""><figcaption></figcaption></figure>

6. To create a draft, click the **pen** icon

<figure><img src="../../../../../.gitbook/assets/Screenshot 2025-01-28 at 14.58.56.png" alt=""><figcaption></figcaption></figure>

7. Inside the `"tables"` array, add the specific column you want to display by providing a name and path:

```
{ 
"name": "PURCHASE_ORDER",    
"path":"path_to_source" 
}
```

**NOTE:**  E-documents will always have the origin set to **Great Britain**, so the amounts will be saved in international format, using a **dot (.)** as the decimal separator.

8. Save the draft

<figure><img src="../../../../../.gitbook/assets/Screenshot 2025-01-28 at 15.11.04.png" alt=""><figcaption></figcaption></figure>

9. Make sure that your draft is the **active** one.

<figure><img src="../../../../../.gitbook/assets/Screenshot 2025-01-28 at 16.03.50.png" alt=""><figcaption></figcaption></figure>

### Method 2: Display Attribute in the XSL Output (HTML/PDF preview)

1. Go to **Settings**
2. Go to **Document Types**
3. Select **Invoice/E-Doc**

<figure><img src="../../../../../.gitbook/assets/Screenshot 2025-01-28 at 15.07.58.png" alt=""><figcaption></figcaption></figure>

4. Open the **"FATTURAPA"** tab
5. **Click on XLST**

<figure><img src="../../../../../.gitbook/assets/Screenshot 2025-01-28 at 15.23.06.png" alt=""><figcaption></figcaption></figure>

6. To create a draft, click the **pen** icon

<figure><img src="../../../../../.gitbook/assets/Screenshot 2025-01-28 at 14.58.56.png" alt=""><figcaption></figcaption></figure>

7. In the `<xsl:for-each select="path">` block that generates the table rows, add a snippet like this where you want the attribute to appear (e.g., in its own column):

```
<tr>
    <!-- Other columns ... -->

    <td>
        <!-- PO number -->
        <xsl:variable name="variable_name" select="value" />
        <xsl:value-of 
            select="path_to_attribute" 
        />
    </td>
</tr>
```

**NOTE:**  E-documents will always have the origin set to **Great Britain**, so the amounts will be saved in international format, using a **dot (.)** as the decimal separator.

8. Save the draft

<figure><img src="../../../../../.gitbook/assets/Screenshot 2025-01-28 at 15.11.04.png" alt=""><figcaption></figcaption></figure>

9. Make sure that your draft is the **active** one.

<figure><img src="../../../../../.gitbook/assets/Screenshot 2025-01-28 at 16.03.50.png" alt=""><figcaption></figcaption></figure>
