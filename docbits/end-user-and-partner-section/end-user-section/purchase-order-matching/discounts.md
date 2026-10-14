# Discounts

## **Overview**

If your extracted table contains the **Discount** or **Discount Percentage** column, **DocBits** will automatically apply the corresponding discount to the Unit Price during processing in the [**Purchase Order Matching screen**](./).

## Exceptions

Discounts will not be automatically applied when the multi-match feature is used. More information about the multi match feature can be found [here](./#multi-matches).

## Discount Calculation

When a **Discount** is present, the discounted unit price is calculated by subtracting the discount amount from the unit price:

```
UNIT_PRICE_DISCOUNTED = UNIT_PRICE - DISCOUNT
```

## Discount Percentage Calculation

When a **Discount Percentage** is present, the discounted unit price is calculated using the following formula:

```
UNIT_PRICE_DISCOUNTED = UNIT_PRICE * (1 - DISCOUNT_PERCENT / 100)
```

## Rounding

All discounted unit price results are rounded to four decimal places for consistency in downstream processing.
