# Editing and Saving Regex Patterns

## Guide to modifying existing patterns and the importance of testing those changes to ensure they work as expected without breaking existing functionality.

**To edit existing regex patterns and ensure the changes work as expected without breaking existing functionality, you can follow the guide below:**

<figure><img src="../../../../../.gitbook/assets/docbits_regex_edit_settings.png" alt="Docbits Regex Edit Settings"><figcaption><p>Settings: Document Type</p></figcaption></figure>

<figure><img src="../../../../../.gitbook/assets/docbits_regex_pattern_analysis.png" alt="Docbits Regex Pattern Analysis"><figcaption></figcaption></figure>

**Analyze the existing pattern:**

* Examine the existing regex pattern to understand what data it captures and how it works.
* Identify the parts of the pattern that need to be changed and the impact of those changes on the data captured.

**For example: The invoice amount is to be read out:**

*   (?<=Rechnungsbetrag:)\[\s]\*((((\d+)\[,.]{1,10})+\d{0,2})|(\d+(?!,)))

    Rechnungsbetrag: 100.00
*   Read the amount with 1000s dot but NOT pass the dot

    \[\d.]_\[,\d]_

    Allowed characters: 0123456789,
*   The value "P32180" is to be read out. Anchor word here is "Invoice Date".

    (?<=InvoiceDate )\[\s]\*P\d{5}

    Customer number Invoice number Invoice date P32180 613976 05/13/2019

<figure><img src="../../../../../.gitbook/assets/docbits_regex_customer_invoice_example.png" alt="Docbits Regex Customer Invoice Example"><figcaption></figcaption></figure>

**Document the changes:**

* Take notes about the changes you plan to make to the regex pattern.
* Note what new patterns you plan to add and what parts of the existing pattern may need to be changed or removed.

**Prepare test data:**

* Collect test data that is representative of the different types of data the regex pattern typically captures.
* Make sure your test data covers both typical and edge cases to verify the robustness of your changes.

**Make changes to the regex pattern:**

* Make the planned changes to the regex pattern.
* This may include adding new patterns, removing or adjusting existing parts, or optimizing the pattern for better performance.

**Test the changes:**

* Apply the updated regex pattern to your test data and carefully review the results.
* Verify that the pattern still correctly captures the desired data and that there are no unexpected impacts on other parts of the data or system.

**Debugging and adapting:**

* If test results are not as expected or unexpected issues occur, carefully review your changes and make further adjustments as needed.
* This may include reverting certain changes or adding additional adjustments to fix the problem.

**Document the changes:**

* Update the documentation of your regex pattern to reflect the changes made.
* Describe the updated patterns and the reasons for the changes made to help other developers understand and use the pattern.

**Saving the changes:**

* Once you are sure that the changes are successful and work as expected, save the updated regex pattern to your code base or configuration files to ensure they are available for future use.

<figure><img src="../../../../../.gitbook/assets/docbits_regex_save_changes.png" alt="Docbits Regex Save Changes"><figcaption><p>Save Changes</p></figcaption></figure>

By following these steps and carefully testing changes to regex patterns, you can ensure that your regex pattern continues to work correctly while meeting new requirements.
