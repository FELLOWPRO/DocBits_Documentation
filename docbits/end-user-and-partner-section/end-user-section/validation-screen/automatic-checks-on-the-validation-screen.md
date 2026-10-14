# Automatic Checks on the Validation Screen

## Overview

By default, specific fields in the field validation process are automatically checked by verifying their values using formulas based on other extracted values. On this page, you can find the forms used for these automatic calculations.

You can always verify the formula used by hovering over the info icon.

<figure><img src="../../../.gitbook/assets/automatic_checks_1 (1).png" alt=""><figcaption></figcaption></figure>

<mark style="color:red;">**Note:**</mark> The info icon is only visible if a value has been extracted for the corresponding field.

## Formulars for automatic checks:

### Net amount:

```
Net amount = Tax amount * 100 / Vat rate 
```

### Vat rate:

```
Vat rate = Tax amount * 100 / Net amount 
```

### Tax amount:

```
Tax amount = Net amount + Vat rate / 100
```

### Net amount reduced:

```
Net amount reduced = Reduced Tax amount * 100 / Vat rate reduced
```

### Vat rate reduced:

```
Vat rate reduced = Reduced Tax amount * 100 / Net amount reduced
```

### Tax amount reduced:

```
Tax amount reduced = Reduced Tax amount + Vat rate reduced / 100
```

### Total net amount:

```
Total net amount = Net amount + Reduced Tax amount + Net amount free
```

### Total net amount US:

```
Total net amount US = Net amount + Shipping charges + Misc. charges + Additional amount
```

### Total tax amount:

```
Total tax amount = Tax amount + Reduced Tax amount + Tax amount free 
```

### Total amount:

```
Total amount = Net amount + Tax Amount
```

<mark style="color:red;">**Note:**</mark> If the extracted value and the validated value do not match, the document cannot be processed further. An **Amounts Mismatch** error will appear for the corresponding field.
