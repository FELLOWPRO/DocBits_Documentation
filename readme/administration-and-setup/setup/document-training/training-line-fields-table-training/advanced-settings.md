# Advanced Settings

In some documents, table structures can be complex—spanning multiple lines, containing grouped information, or including unnecessary extra rows. The _Advanced Settings_ in training mode allow you to fine-tune table extraction for such cases, improving accuracy and consistency.

To access these settings, activate **Training Mode** and click the **Settings** gear icon in the top action bar:

<figure><img src="../../../../.gitbook/assets/a-training-line-fields-table-training-advanced-settings-gear-en-20261006.png" alt="Table extraction screen in training mode with the mouse over the Settings gear icon in the top action bar."><figcaption><p>The Settings gear in the training mode action bar opens the Advanced Settings.</p></figcaption></figure>

### Header Row Count

**Use this setting to define how many lines make up the table header.**

Some tables have multi-line headers. For example, this table’s header spans two lines:

<figure><img src="../../../../.gitbook/assets/a-training-line-fields-table-training-advanced-settings-header-two-lines-en-20261006.png" alt="Invoice table whose header spans two lines (Preis / in EUR and Betrag / in EUR)."><figcaption><p>A table header that spans two lines.</p></figcaption></figure>

Set the **Header row count** to match:

<figure><img src="../../../../.gitbook/assets/a-training-line-fields-table-training-advanced-settings-header-row-count-en-20261006.png" alt="Settings dialog with Header row count set to 2."><figcaption><p>Header row count set to 2 in the Settings dialog.</p></figcaption></figure>

#### Why is this important?

If you don’t set this, DocBits may treat the second line as data instead of part of the header, leading to extraction errors:

**Before:**

<figure><img src="../../../../.gitbook/assets/a-training-line-fields-table-training-advanced-settings-header-before-en-20261006.png" alt="Extracted table with a wrong header row count: the second header line appears as a data row and the column headers are not mapped."><figcaption><p>Before: the second header line is treated as data.</p></figcaption></figure>

After:

<figure><img src="../../../../.gitbook/assets/a-training-line-fields-table-training-advanced-settings-header-after-en-20261006.png" alt="Extracted table with Header row count 2: columns are mapped to Position, Description, Quantity, Unit Price and Net Amount and the rows are correct."><figcaption><p>After: header and data rows are separated correctly.</p></figcaption></figure>

### Move Extra Rows to Trash

**Use this to discard unwanted multi-line entries, such as overflow descriptions.**

In this example, the description spills into multiple rows, but only the first line is relevant:

<figure><img src="../../../../.gitbook/assets/a-training-line-fields-table-training-advanced-settings-overflow-doc-en-20261006.png" alt="Invoice table where the description of each item continues on additional text lines below the item."><figcaption><p>The description spills into several lines of which only the first is relevant.</p></figcaption></figure>

Enable **Move Extra Rows to Trash** to remove the overflow:

<figure><img src="../../../../.gitbook/assets/a-training-line-fields-table-training-advanced-settings-move-extra-rows-en-20261006.png" alt="Settings dialog with Move Extra Rows to set to Trash."><figcaption><p>Move Extra Rows to Trash enabled.</p></figcaption></figure>

**Result after mapping:**

<figure><img src="../../../../.gitbook/assets/a-training-line-fields-table-training-advanced-settings-trash-result-en-20261006.png" alt="Extracted table with three clean rows after the extra description lines were moved to trash and the columns were mapped."><figcaption><p>Result after mapping: only the relevant rows remain.</p></figcaption></figure>



### Minimum Grouped Rows

**Use this when rows need to be grouped together under one main row (e.g. line items with multiple sub-lines).**

Here, only three out of six rows are relevant. Two key columns are mapped (e.g. Position, Description), while others are treated as custom fields.

Start by setting **Header row count** and the **Minimum grouped rows**:

<figure><img src="../../../../.gitbook/assets/a-training-line-fields-table-training-advanced-settings-min-grouped-en-20261006.png" alt="Settings dialog with Header row count 2 and the Advanced Settings section expanded showing Minimum grouped rows set to 2."><figcaption><p>Header row count and Minimum grouped rows set in the Settings dialog.</p></figcaption></figure>

Also enable **Move Extra Rows to Trash** to clean up irrelevant data:

<figure><img src="../../../../.gitbook/assets/a-training-line-fields-table-training-advanced-settings-min-grouped-trash-en-20261006.png" alt="Settings dialog with Header row count 2, Move Extra Rows to Trash and Minimum grouped rows 2."><figcaption><p>Move Extra Rows to Trash enabled in addition.</p></figcaption></figure>

Then define the grouping key column, e.g. _Position_:

<figure><img src="../../../../.gitbook/assets/a-training-line-fields-table-training-advanced-settings-group-key-en-20261006.png" alt="Extracted table with the column menu of the Position column open showing Delete column, Group rows and Regex."><figcaption><p>Choose Group rows in the column menu of the grouping key column (Position).</p></figcaption></figure>

**Result:**

<figure><img src="../../../../.gitbook/assets/a-training-line-fields-table-training-advanced-settings-grouped-result-en-20261006.png" alt="Extracted table with three grouped rows after grouping by Position and trashing extra rows."><figcaption><p>Result: the six physical rows are grouped into three line items.</p></figcaption></figure>

### Reverse Grouping

**Use this when the grouping row appears&#x20;**_**after**_**&#x20;the rows it should group.**

If the row that should be grouped with other data appears _above_ the grouping key, enable this option:

<figure><img src="../../../../.gitbook/assets/a-training-line-fields-table-training-advanced-settings-reverse-doc-en-20261006.png" alt="Invoice table in which the description line stands above the line that carries position, quantity and amounts."><figcaption><p>The grouping row appears after the rows it should group.</p></figcaption></figure>

Enable **Reverse grouping**, group by a main column (e.g. Net amount), and use **Move Extra Rows to Trash** if needed:

<figure><img src="../../../../.gitbook/assets/a-training-line-fields-table-training-advanced-settings-reverse-dialog-en-20261006.png" alt="Settings dialog with Reverse grouping checked, Move Extra Rows to Trash and Header row count 2."><figcaption><p>Reverse grouping enabled together with Move Extra Rows to Trash.</p></figcaption></figure>

**Final result:**\


<figure><img src="../../../../.gitbook/assets/a-training-line-fields-table-training-advanced-settings-reverse-result-en-20261006.png" alt="Extracted table with three rows after reverse grouping by the amount column."><figcaption><p>Final result with reverse grouping.</p></figcaption></figure>

### Summary

Use the _Advanced Settings_ to teach DocBits how to accurately handle more complex or inconsistent table structures. These settings improve extraction precision by accounting for:

* Multi-line headers
* Multi-row descriptions
* Grouped line items
* Reverse order of grouped data

Enabling these options during training ensures DocBits remembers the correct layout for future documents from the same supplier.
