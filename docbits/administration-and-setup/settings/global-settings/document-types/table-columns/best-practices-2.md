# Best practices

## Keep the default columns for amounts and quantities

The line-item checks (*quantity × unit price = line total*) and PO matching look for the default columns `QUANTITY`, `UNIT_PRICE`, `TOTAL_AMOUNT`, `ITEM_NUMBER`. If you create your own columns for these values instead, the checks do not run and PO matching reports missing mandatory columns. Rename the *title* if the wording does not suit you; keep the column.

## Hide, don't delete

Default columns you do not need are hidden, not deleted; they cannot be deleted anyway. For your own columns, hiding is also the safer choice while you are not sure whether a script or an export mapping still references the column.

## Mark as required only what blocks export

Every required column has to be filled in every row before a user can approve the document. Use it for values the ERP rejects when missing (for example the cost centre in an accounting export), not for values that are merely useful.

## Use *Read Only* for looked-up values

Values that a script or a master-data lookup writes into the table (article description from the item master, tax code from the supplier) should be read-only, so users correct the source instead of the copy.

## Use AI per column, not per supplier

For a supplier with trained rules, most columns come out right from the rules. If one column is unreliable (long descriptions that wrap, a discount that sometimes sits in a different place), set *Use AI* on that column only. The rules keep the rest.

## Name columns for the ERP, not for the document

The *Column name* ends up in export mappings and scripts. `COST_CENTRE` is easier to map than `KST` and does not change when a supplier prints it differently.

## Test on a restarted document

After a change, restart one existing document of the document type and open it: the new column appears, the hidden one is gone, required cells are marked. Only then roll it out to users.

## One table per line-item structure

Create a second table only when a document type really has two independent tables (for example item lines and a separate charges table). Extra empty tables show up on every document of the type.
