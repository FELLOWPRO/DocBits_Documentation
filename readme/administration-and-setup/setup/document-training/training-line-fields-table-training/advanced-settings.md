# Advanced Settings

In some documents, table structures can be complex—spanning multiple lines, containing grouped information, or including unnecessary extra rows. The _Advanced Settings_ in training mode allow you to fine-tune table extraction for such cases, improving accuracy and consistency.

To access these settings, activate **Training Mode** and click the **Settings** gear icon in the top action bar:

<figure><img src="../../../../.gitbook/assets/a-training-line-fields-table-training-advanced-settings-gear-en-20261014.png" alt="Table extraction screen in training mode with the mouse over the Settings gear icon in the top action bar."><figcaption><p>The Settings gear in the training mode action bar opens the Advanced Settings.</p></figcaption></figure>

The Settings dialog holds every option described on this page. Expand the **Advanced Settings** section to reach the grouping options, which stay collapsed until you open them:

<figure><img src="../../../../.gitbook/assets/a-training-line-fields-table-training-advanced-settings-max-rows-en-20261014.png" alt="Settings dialog with Header row count 2 and the Advanced Settings section expanded showing Minimum grouped rows 2, Maximum grouped rows 3, Distinct group columns, Reverse grouping and Split text."><figcaption><p>The Advanced Settings section with all grouping options.</p></figcaption></figure>

Each option is described in its own section below, together with the effect it has on the extracted table.

### Header Row Count

**Use this setting to define how many lines make up the table header.**

Some tables have multi-line headers. For example, this table’s header spans two lines:

<figure><img src="../../../../.gitbook/assets/a-training-line-fields-table-training-advanced-settings-header-two-lines-en-20261014.png" alt="Invoice table whose header spans two lines (Preis / in EUR and Betrag / in EUR)."><figcaption><p>A table header that spans two lines.</p></figcaption></figure>

Set the **Header row count** to match:

<figure><img src="../../../../.gitbook/assets/a-training-line-fields-table-training-advanced-settings-header-row-count-en-20261014.png" alt="Settings dialog with Header row count set to 2."><figcaption><p>Header row count set to 2 in the Settings dialog.</p></figcaption></figure>

#### Why is this important?

If you don’t set this, DocBits may treat the second line as data instead of part of the header, leading to extraction errors:

**Before:**

<figure><img src="../../../../.gitbook/assets/a-training-line-fields-table-training-advanced-settings-header-before-en-20261014.png" alt="Extracted table with a wrong header row count: the second header line appears as a data row and the column headers are not mapped."><figcaption><p>Before: the second header line is treated as data.</p></figcaption></figure>

After:

<figure><img src="../../../../.gitbook/assets/a-training-line-fields-table-training-advanced-settings-header-after-en-20261014.png" alt="Extracted table with Header row count 2: columns are mapped to Position, Description, Quantity, Unit Price and Net Amount and the rows are correct."><figcaption><p>After: header and data rows are separated correctly.</p></figcaption></figure>

### Move Extra Rows to Trash

**Use this to discard unwanted multi-line entries, such as overflow descriptions.**

In this example, the description spills into multiple rows, but only the first line is relevant:

<figure><img src="../../../../.gitbook/assets/a-training-line-fields-table-training-advanced-settings-overflow-doc-en-20261014.png" alt="Invoice table where the description of each item continues on additional text lines below the item."><figcaption><p>The description spills into several lines of which only the first is relevant.</p></figcaption></figure>

Set **Move Extra Rows to** to **Trash** to remove the overflow:

<figure><img src="../../../../.gitbook/assets/a-training-line-fields-table-training-advanced-settings-move-extra-rows-en-20261014.png" alt="Settings dialog with Move Extra Rows to set to Trash."><figcaption><p>Move Extra Rows to set to Trash.</p></figcaption></figure>

**Result after mapping:**

<figure><img src="../../../../.gitbook/assets/a-training-line-fields-table-training-advanced-settings-trash-result-en-20261014.png" alt="Table extraction screen: the source document shows each item description spilling over two lines, while the extracted table on the right already contains one clean row per item."><figcaption><p>Result after mapping: the overflow lines are gone and only the relevant rows remain.</p></figcaption></figure>

### Minimum Grouped Rows

**Use this when rows need to be grouped together under one main row (e.g. line items with multiple sub-lines).**

Here, only three out of six rows are relevant. Two key columns are mapped (e.g. Position, Description), while others are treated as custom fields.

Start by setting **Header row count** and the **Minimum grouped rows** — the smallest number of rows that must belong to a group before DocBits merges them:

<figure><img src="../../../../.gitbook/assets/a-training-line-fields-table-training-advanced-settings-min-grouped-en-20261014.png" alt="Settings dialog with Header row count 2 and the Advanced Settings section expanded showing Minimum grouped rows set to 2."><figcaption><p>Header row count and Minimum grouped rows set in the Settings dialog.</p></figcaption></figure>

Also set **Move Extra Rows to** to **Trash** to clean up irrelevant data:

<figure><img src="../../../../.gitbook/assets/a-training-line-fields-table-training-advanced-settings-min-grouped-trash-en-20261014.png" alt="Settings dialog with Header row count 2, Move Extra Rows to Trash and Minimum grouped rows 2."><figcaption><p>Move Extra Rows to set to Trash in addition.</p></figcaption></figure>

Then define the grouping key column, e.g. _Position_, by opening the column menu of that column and choosing **Group rows**:

<figure><img src="../../../../.gitbook/assets/a-training-line-fields-table-training-advanced-settings-group-key-en-20261014.png" alt="Extracted table with the column menu of the Position column open showing Delete column, Group rows and Regex."><figcaption><p>Choose Group rows in the column menu of the grouping key column (Position).</p></figcaption></figure>

Grouping itself, and the other column tools that work together with it (manual row selection, column mapping and regex), are covered step by step in [Structuring and Improving Table Extraction in DocBits](improving-table-extraction-with-regex.md).

**Result:**

<figure><img src="../../../../.gitbook/assets/a-training-line-fields-table-training-advanced-settings-grouped-result-en-20261014.png" alt="Table extraction screen: the source document holds six physical lines, two per item, and the extracted table on the right shows one grouped row per item."><figcaption><p>Result: the six physical rows are grouped into three line items.</p></figcaption></figure>

#### Maximum Grouped Rows

**Use this to cap how many rows one group may contain.** Its tooltip asks: _How many rows does your grouped column maximum have?_ It is the counterpart to Minimum grouped rows: a group that would need more rows than this number is not merged.

Leave it empty when groups may be any size. Set it when a document contains items with many sub-lines and you want DocBits to leave unusually large blocks ungrouped so you can inspect them yourself.

You set it in the same dialog area as Minimum grouped rows, directly below it:

<figure><img src="../../../../.gitbook/assets/a-training-line-fields-table-training-advanced-settings-max-rows-en-20261014.png" alt="Settings dialog with Minimum grouped rows set to 2 and Maximum grouped rows set to 3, Distinct group columns, Reverse grouping and Split text unchecked."><figcaption><p>Maximum grouped rows (here 3) sits directly below Minimum grouped rows.</p></figcaption></figure>

#### Distinct Group Columns

**Use this to keep only unique values in the grouping key column.**

The option's own tooltip in the app asks: _Do you want only unique values for your grouped column?_ Switch it on when several groups would carry the same value in the grouping key column and you want DocBits to keep that value only once, so the repeated groups show an empty key instead of the duplicate value.

It is a checkbox in the same section as Minimum grouped rows:

<figure><img src="../../../../.gitbook/assets/a-training-line-fields-table-training-advanced-settings-distinct-split-en-20261014.png" alt="Settings dialog with the Distinct group columns checkbox ticked below Maximum grouped rows."><figcaption><p>Distinct group columns is the checkbox below Maximum grouped rows.</p></figcaption></figure>

#### Reverse Grouping

**Use this when the grouping row appears&#x20;**_**after**_**&#x20;the rows it should group.**

The option's tooltip asks: _Do you want to combine all the rows above the grouped attribute?_ Enable it when the row that carries the grouping key (for example the position or amount) stands _below_ its continuation lines, so DocBits merges the rows above the key into the group instead of the rows below it:

<figure><img src="../../../../.gitbook/assets/a-training-line-fields-table-training-advanced-settings-reverse-doc-en-20261014.png" alt="Invoice table in which the description line stands above the line that carries position, quantity and amounts."><figcaption><p>The grouping row appears after the rows it should group.</p></figcaption></figure>

Enable **Reverse grouping**, group by a main column (e.g. Net amount), and set **Move Extra Rows to Trash** if needed:

<figure><img src="../../../../.gitbook/assets/a-training-line-fields-table-training-advanced-settings-reverse-dialog-en-20261014.png" alt="Settings dialog with Reverse grouping checked, Move Extra Rows to Trash and Header row count 2."><figcaption><p>Reverse grouping enabled together with Move Extra Rows to Trash.</p></figcaption></figure>

**Final result:**

<figure><img src="../../../../.gitbook/assets/a-training-line-fields-table-training-advanced-settings-reverse-result-en-20261014.png" alt="Extracted table with three rows after reverse grouping by the amount column."><figcaption><p>Final result with reverse grouping.</p></figcaption></figure>

#### Split Text

**Use this to split cell text exactly at the column separator.**

The option's tooltip asks: _Do you want to split the text exactly at the column separator?_ Switch it on when one extracted cell contains the text of two columns that the table separator did not separate. DocBits then re-extracts the table and cuts each value at the separator position you defined, instead of storing both values in one cell.

Because the split re-runs the extraction, DocBits asks you to confirm before it runs: the confirmation appears as soon as you tick the checkbox, and the split is applied only after you click **Proceed**.

The checkbox is the last option in the Advanced Settings section:

<figure><img src="../../../../.gitbook/assets/a-training-line-fields-table-training-advanced-settings-distinct-split-en-20261014.png" alt="Settings dialog with the Split text checkbox ticked as the last option of the Advanced Settings section."><figcaption><p>Split text is the last checkbox of the section.</p></figcaption></figure>

<figure><img src="../../../../.gitbook/assets/a-training-line-fields-table-training-advanced-settings-split-confirm-en-20261014.png" alt="Confirmation dialog asking 'Are you sure? Table will be extracted again' with the buttons Cancel and Proceed."><figcaption><p>Ticking Split text opens this confirmation; only Proceed applies the split.</p></figcaption></figure>

### Summary

Use the _Advanced Settings_ to teach DocBits how to accurately handle more complex or inconsistent table structures. These settings improve extraction precision by accounting for:

* Multi-line headers
* Multi-row descriptions
* Grouped line items
* Reverse order of grouped data
* Text that needs to be split at a column separator

Enabling these options during training ensures DocBits remembers the correct layout for future documents from the same supplier. Once the extraction looks right, store the configuration with the **Save Rules** action described in [Save and Delete Rules](save-and-delete-rules.md).
