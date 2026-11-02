# Supplier BOD Mapping

This page documents how DocBits ingests Infor M3 supplier master data through the `SyncSupplierPartyMaster` and `SyncRemitToPartyMaster` BODs. Both BODs populate the same `SUPPLIER` master-data table in DocBits.

{% file src="../../../../.gitbook/assets/Sync.SupplierPartyMaster.pdf" %}
SupplierPartyMaster — original BOD mapping reference (PDF)
{% endfile %}

{% file src="../../../../.gitbook/assets/Sync.RemitToPartyMaster.pdf" %}
RemitToPartyMaster — original BOD mapping reference (PDF)
{% endfile %}

## Key principles

- **CONO + SUNO is the match key.** A `supplier_header` row in DocBits is uniquely identified by `(customer_number = sharedCONO, supplier_number = sharedSUNO)`. This allows a single DocBits organisation to consolidate multiple M3 companies.
- **`variationID` protects against out-of-order BODs.** M3 can emit the same master-data record multiple times in quick succession; the incoming `variationID` must be greater than the stored value for an update to be accepted. Both BODs track their `variationID` independently (`variation_id_supplier_bod`, `variation_id_remit_to_party`).
- **No silent overwriting.** SupplierPartyMaster and RemitToPartyMaster share several fields (name, phone, VAT, bank, status). Each BOD only updates the fields it owns and only if its `variationID` advances. Within the shared set, the most recently received BOD (per BOD type) wins.
- **Multi-bank sync is preference-gated.** Default behaviour: the last `FinancialParty` is written to `bank_id` on the header. With the preference `ALLOW_MULTIPLE_SUPPLIER_ACCOUNTS_SYNC` enabled, every `FinancialParty` entry is persisted to `supplier_account` (IBAN, account ID, currency code, preference indicator).
- **Optional CONO suffix stripping.** Some M3 installations append a division suffix to the company number (e.g. `100_01`). The preference `EXCLUDE_DIVISION_FOR_CUSTOMER_NUMBER` strips trailing `_*` so DocBits keys remain consistent. Be aware that with the stripping enabled, multiple per-division RemitToPartyMaster BODs collapse onto a single match key — and the BOD with the highest `variationID` wins. See the FAQ "*What happens when one RemitToPartyMaster BOD is emitted per division?*" below.

## Sync.SupplierPartyMaster

→ DocBits Master Data Lookup Table: **SUPPLIER**

```python
header_mappings = {
            "sharedCONO": "//DataArea/Sync/AccountingEntityID",
            "sharedSUNO": "//SupplierPartyMaster/PartyIDs/ID",
            "variationID": "//SupplierPartyMaster/PartyIDs/ID/@variationID",
            "supplierName": "//SupplierPartyMaster/Name",
            "phone": '//Communication[ChannelCode="Phone"]/DialNumber',
            "vatNo": "//SupplierPartyMaster/PartyIDs/TaxID",
            "paymentTermId": "//SupplierPartyMaster/PaymentTermID",
            "paymentMethodCode": "//SupplierPartyMaster/PaymentMethodCode",
            "buyerPersonReferenceId": "//SupplierPartyMaster/BuyerPersonReference/IDs/ID",
            "buyerPersonReference": "//SupplierPartyMaster/BuyerPersonReference/Name",
            "supplier_category": "//SupplierPartyMaster/Classification/Codes/Code[@listID='Supplier Categories']",
            "supplier_group": "//SupplierPartyMaster/Classification/Codes/Code[@listID='Supplier Group']",
            "discount_terms_description": "//SupplierPartyMaster/UserArea/Property/NameValue[@name='eam.UDFCHAR06']",
            "status": "//SupplierPartyMaster/Status/Code",
            "bank_id": "//SupplierPartyMaster/FinancialParty[last()]/FinancialAccount/ID",
        }
```

### Field reference

| DocBits field | M3 source | Description |
|---|---|---|
| `sharedCONO` | M3 company number | Maps to `customer_number` on `supplier_header`. Part of the match key. |
| `sharedSUNO` | `CIDMAS.IDSUNO` | M3 supplier number. Part of the match key. |
| `variationID` | BOD attribute | Stored as `variation_id_supplier_bod`. Incoming BODs are accepted only if their `variationID` exceeds the stored value. A missing attribute is treated as `0` (force-update). |
| `supplierName` | `CIDMAS.IDSUNM` | Supplier display name. |
| `phone` | `CIDMAS.PHNO/PHN2/IDTFNO` | Phone number from the `Phone` communication channel. |
| `vatNo` | `CIDMAS.IDVRNO` | VAT identifier. Read from `PartyIDs/TaxID` (no `@schemeName` filter in the M3 ingest path). **OPEN** — when M3 emits multiple `TaxID` elements with different `@schemeName` values (e.g. `VatCode`, `TaxIdentificationNumber`), the first occurrence wins. A configurable `schemeName` filter is planned; share an example BOD so we can pin down the right default. <!-- tracked in DOCB-12313 --> |
| `paymentTermId` | `CIDVEN.IITEPY` | Payment-terms identifier. |
| `paymentMethodCode` | — | Payment method code, when supplied. |
| `buyerPersonReferenceId` / `buyerPersonReference` | `CIDVEN.IIBUYE` / `CSYUSR.CRRENM` | Assigned buyer (M3 user) reference and display name. |
| `supplier_category` | — | Read from `Classification/Codes/Code[@listID='Supplier Categories']`. Optional UserArea extension; left NULL by stock M3 installations. |
| `supplier_group` | `CIDVEN.IISUCL` | Supplier classification group. |
| `discount_terms_description` | — | Optional UserArea extension (`eam.UDFCHAR06`) used by DocBits' discount-date calculator. When the supplier provides a discount-days value here, DocBits combines it with the invoice date to produce a discount due date for the AP team. |
| `status` | `CIDMAS.IDSTAT` | Supplier active/inactive status, taken from `SupplierPartyMaster/Status/Code`. |
| `bank_id` | `CBANAC.BCBKNO` | Default bank account, taken from the *last* `FinancialParty`. Enable `ALLOW_MULTIPLE_SUPPLIER_ACCOUNTS_SYNC` to sync every `FinancialParty` into the `supplier_account` table instead. |

## Sync.RemitToPartyMaster

→ DocBits Master Data Lookup Table: **SUPPLIER**

```python
header_mappings = {
            "sharedCONO": "//DataArea/Sync/AccountingEntityID",
            "sharedSUNO": "//RemitToPartyMaster/PartyIDs/ID",
            "variationID": "//RemitToPartyMaster/PartyIDs/ID/@variationID",
            "supplierName": "//RemitToPartyMaster/Name",
            "phone": '//Communication[ChannelCode="Phone"]/DialNumber',
            "vatNo": "//RemitToPartyMaster/PartyIDs/TaxID",
            "bank_id": "//RemitToPartyMaster/FinancialParty[last()]/FinancialAccount/ID",
            "status": "//RemitToPartyMaster/Status/Code",
        }
```

### Field reference

| DocBits field | M3 source | Description |
|---|---|---|
| `sharedCONO` / `sharedSUNO` | M3 company / `CIDMAS.IDSUNO` | Same semantics as on `SupplierPartyMaster`. Joins onto the same `supplier_header` row. |
| `variationID` | BOD attribute | Stored as `variation_id_remit_to_party` — tracked independently from the SupplierPartyMaster `variationID`. |
| `supplierName` | `CIDMAS.IDSUNM` | Remit-to display name. Writes to the shared `supplier_name` column. |
| `phone` | `CIDREF.IRPHNO` | Phone number from the remit-to communication block. |
| `vatNo` | `CIDMAS.IDCORG` | VAT identifier on the remit-to party. Same `@schemeName` limitation as on the SupplierPartyMaster — first occurrence wins. <!-- tracked in DOCB-12313 --> |
| `bank_id` | `CBANAC.BCBKNO` | Remit-to bank account (`FinancialParty[last()]`). Same multi-bank preference applies. |
| `status` | `CIDMAS.IDSTAT` | Remit-to active/inactive status. |

## How the two BODs interact on the shared `SUPPLIER` table

Both BODs populate the same `supplier_header` row. For the fields they share (`supplierName`, `phone`, `vatNo`, `bank_id`, `status`), DocBits applies the following rules:

1. Match the row by `(customer_number = sharedCONO, supplier_number = sharedSUNO)`.
2. Compare the incoming `variationID` to the stored `variationID` *for the same BOD type*.
3. If the incoming `variationID` is greater (or `0`, meaning force-update), update the fields owned by that BOD. Otherwise discard the BOD.
4. The other BOD type's `variationID` is not touched, and its previously stored values remain in place.

`supplier_address` and `supplier_account` rows associated with the supplier are deleted and re-inserted on update, so secondary tables always reflect the most recent BOD. This has a side effect when M3 emits one RemitToPartyMaster BOD *per division* (some tenants do this when bank connections are maintained on an empty division as well as on specific divisions): after `EXCLUDE_DIVISION_FOR_CUSTOMER_NUMBER` strips the division suffix, every per-division BOD targets the same `(customer_number, supplier_number)` key. The BOD with the highest `variationID` wins. If that "winning" BOD belongs to a division without bank connections, the bank accounts of the previous BOD are wiped on re-insert.

## Common questions

### Why does DocBits track CONO if all my suppliers come from one M3 company?

CONO routing is mandatory because DocBits is multi-tenant by design: an organisation can ingest BODs from multiple M3 companies. CONO is part of the match key so suppliers from different companies cannot collide. If you only have one company you can ignore the value, but the key column is still populated.

### Both BODs write to the same supplier row — does the latest BOD overwrite everything?

No. Each BOD type only owns the fields it sends, and updates are gated by an independent `variationID`. A SupplierPartyMaster that changes only the supplier name does not roll back the phone number that a later RemitToPartyMaster had written.

### `Supplier Categories` and `eam.UDFCHAR06` are never delivered by my M3 — what should I do?

Both are optional UserArea extensions. Without the extension the columns stay NULL and no DocBits feature depends on them. Enable the discount-date logic only when your M3 is configured to emit `eam.UDFCHAR06`.

### Should `vatNo` filter for `schemeName='TaxIdentificationNumber'`?

The M3 BOD ingest path currently reads `PartyIDs/TaxID` without a `schemeName` filter. The filter is used in the e-invoice XSLT paths (Facturae, XRechnung, KSeF), not in the M3 ingest. When M3 emits multiple `TaxID` elements with different `@schemeName` values, the first occurrence wins — which can yield incorrect VAT identifiers. A configurable filter is planned; a sample BOD from your tenant helps us nail down the right default `schemeName`. <!-- tracked in DOCB-12313 -->

### What happens when one RemitToPartyMaster BOD is emitted per division?

Some M3 tenants maintain bank connections both on an empty division and on specific divisions, which causes M3 to emit a separate RemitToPartyMaster BOD per division. The match key in DocBits is `(customer_number = sharedCONO, supplier_number = sharedSUNO)` — division is not part of it.

- With `EXCLUDE_DIVISION_FOR_CUSTOMER_NUMBER` enabled, the per-division BODs collapse onto the same row. The BOD with the highest `variationID` wins, and `supplier_account` rows are re-inserted from that BOD only. If the winning BOD originates from a division without bank connections, previously stored bank accounts are wiped.
- With the preference disabled (CONO retains its division suffix), the per-division BODs target distinct keys and coexist.

If your tenant ships per-division RemitToPartyMaster BODs and depends on the consolidated bank list, contact us with an example so we can plan a refinement.

### I want every supplier bank account synced, not just the last one. How?

Enable the preference `ALLOW_MULTIPLE_SUPPLIER_ACCOUNTS_SYNC`. With the flag on, every `FinancialParty` entry on the BOD is persisted to the `supplier_account` table (IBAN, financial-account ID, currency code, preference indicator). The legacy `bank_id` header column continues to hold the last entry for backwards compatibility.
