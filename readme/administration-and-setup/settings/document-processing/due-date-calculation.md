# Due Date Calculation

<figure><img src="../../../.gitbook/assets/due_date_calc_overview.png" alt="Due Date Calculation settings"><figcaption><p>Due Date Calculation settings</p></figcaption></figure>

The **Due Date Calculation** page (**Document Processing → Due Date Calculation**) controls how DocBits computes invoice due dates, discount (Skonto) due dates and payment terms from the payment-term codes found on invoices.

## Show Calculated Fields

Enable **Show Calculated Fields** to make the auto-calculated invoice fields — due date, discount due date, payment terms and AP assignment code — appear in Field Settings and as variables in Quick Search and email templates. Custom document types are never affected.

## Invoice Due Date Calculation

### Weekend Handling

<figure><img src="../../../.gitbook/assets/due_date_calc_weekend_options.png" alt="Weekend convention options"><figcaption><p>Weekend convention options</p></figcaption></figure>

Choose how a due date that lands on a Saturday or Sunday is adjusted. This applies to **both** the invoice due date and the discount (Skonto) due date.

| Convention | Effect |
|------------|--------|
| **None** | Keep the calendar date (no adjustment). |
| **Following** | Move Sat/Sun to the next Monday. |
| **Preceding** | Move Sat/Sun to the previous Friday. |
| **Nearest** | Saturday → Friday, Sunday → Monday. |
| **Modified Following** | Next Monday, unless it crosses into the next month, then previous Friday. |

### AP Assignment Code

Map vendor payment terms to AP assignment codes for automated invoice routing by choosing the **AP Assignment Code Field**.

## Discount Term Overwrites

<figure><img src="../../../.gitbook/assets/due_date_calc_mappings.png" alt="Discount term overwrites"><figcaption><p>Discount term overwrites</p></figcaption></figure>

Use **Discount Term Overwrites** to map a specific prefix to a discount percentage and a number of days. Click **+ Add Mapping** to add a row with **Prefix**, **Percentage** and **Days**.

## Supported formats

<figure><img src="../../../.gitbook/assets/due_date_calc_formats.png" alt="Supported payment-term and discount formats"><figcaption><p>Supported payment-term and discount formats</p></figcaption></figure>

DocBits recognises the following payment-term and discount-term codes.

**Supported Payment Term Formats**

| Format | Example | Meaning |
|--------|---------|---------|
| Infor M3 | `N90`, `N30` | Net 90 / 30 days |
| Infor M3 | `NET` | Due on receipt |
| Infor M3 | `M20` | 20th of next month |
| Infor M3 | `E15` | End of month + 15 days |
| Infor LN | `030`, `30` | Net 30 days |
| Reversed | `14N`, `30N` | Net 14 / 30 days |
| Text Codes | `REC`, `DUE`, `COD` | Due on receipt |

**Discount Term Format** — discount terms encode early-payment discounts as 3-digit codes: the first digit is the discount percentage, the last two are the days within which to pay.

| Code | Meaning |
|------|---------|
| `210` | 2% discount if paid within 10 days |
| `130` | 1% discount if paid within 30 days |
| `545` | 5% discount if paid within 45 days |
| `0` | No discount |
