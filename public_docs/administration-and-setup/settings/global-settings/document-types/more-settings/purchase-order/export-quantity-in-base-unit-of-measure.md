# Export quantity in base unit of measure

The switch **Export quantity in base unit of measure** sits in the **Purchase Order** section of a document type's **More Settings**. It changes the quantity and the unit price that the Infor LN export writes for matched purchase order lines.

Open it under **Settings → Document Types**, select the gear icon (**More Settings**) on the document type card and expand **Purchase Order**.

## What the switch does

* **Off:** DocBits exports the quantity and the unit price in the unit of the invoice.
* **On:** DocBits converts the quantity and the unit price of every matched purchase order line to the base unit of measure of that purchase order line, using its conversion factor, and writes the base unit code instead of the invoiced unit code.

A line without a conversion factor is exported unchanged, so a missing factor does not block the export.

{% hint style="info" %}
The conversion applies to the Infor LN export only. Other export targets keep the invoiced unit.
{% endhint %}

## When to use it

Turn the switch on when the Infor LN instance expects order quantities in the base unit of measure. The conversion uses the factor stored on the purchase order line, not a factor that DocBits calculates from the item master.

Settings can affect live documents. Check the result with a test document before you save the change in production. The switch changes the exported values; it does not change how invoice and purchase order lines are matched.

## Related pages

* [Purchase Order](README.md)
* [Export not matched PO lines](export-not-matched-po-lines.md)
* [Alternate Export](alternate-export.md)

<!-- Documentation review 2026-11-27: switch label, help text and behaviour checked against DocBits_Web src/pages/Settings/Components/DocTypes/PO.vue on origin/sandbox-nova (DOP-53, commit feb262ab89, contained in the deployed NOVA build 11.24.8). -->
