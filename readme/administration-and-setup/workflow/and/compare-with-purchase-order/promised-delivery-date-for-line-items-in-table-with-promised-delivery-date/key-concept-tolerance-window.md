# Key Concept: Tolerance Window

Before looking at operators, it is important to understand how the tolerance window is calculated.

## What is a tolerance window?

The tolerance window defines a range of acceptable dates around the purchase order promised delivery date.

**Example:**

* Purchase Order Date: **9 January**
* Tolerance Days: **3**
* Tolerance Window: **6 January → 12 January**

> <mark style="color:red;">Only the selected</mark> <mark style="color:red;"></mark><mark style="color:red;">**Allowed Tolerance Days**</mark> <mark style="color:red;"></mark><mark style="color:red;">(weekdays) are counted when calculating this window.</mark>

### Visual Timeline Example

```
← Past                           Future →
|-----|-----|-----|-----|-----|-----|-----|
     6 Jan      9 Jan      12 Jan
   (Start)    (PO Date)     (End)
```

### Operator Behavior Explained with Examples

* **Equals (=)**
  * **Meaning:**\
    The line item delivery date must fall _inside_ the tolerance window.
  * **Valid Dates:**
    * Any date between **6 Jan and 12 Jan** (inclusive)
  * **Invalid Dates:**
    * Any date **before 6 Jan**
    * Any date **after 12 Jan**
* **Not Equals (≠)**
  * **Meaning:**\
    The line item delivery date must fall _outside_ the tolerance window.
  * **Valid Dates:**
    * Any date **before 6 Jan**
    * Any date **after 12 Jan**
  * **Invalid Dates:**
    * Dates between **6 Jan and 12 Jan**
* **Greater or Equals (≥)**
  * **Meaning:**\
    The line item delivery date must be on or after the **start of the tolerance window**.
  * **Valid Dates:**
    * **6 Jan → any future date**
  * **Invalid Dates:**
    * Any date **before 6 Jan**
  * <mark style="color:red;">**Important:**</mark>\
    This operator allows dates _inside_ the tolerance window **and beyond it**.
* **Lesser or Equals (≤)**
  * **Meaning:**\
    The line item delivery date must be on or before the **end of the tolerance window**.
  * **Valid Dates:**
    * Any past date up to **12 Jan**
  * **Invalid Dates:**
    * Any date **after 12 Jan**
* **Greater Than (>)**
  * **Meaning:**\
    The line item delivery date must be _strictly after_ the tolerance window.
  * **Valid Dates:**
    * **13 Jan → any future date**
  * **Invalid Dates:**
    * Any date **on or before 12 Jan**
* **Lesser Than (<)**
  * **Meaning:**\
    The line item delivery date must be _strictly before_ the tolerance window.
  * **Valid Dates:**
    * Any date **before 6 Jan**
  * **Invalid Dates:**
    * Any date **on or after 6 Jan**

## How “Allowed Tolerance Days” Affect the Tolerance Window

When calculating the tolerance window, **only the selected weekdays are counted**.\
Days that are not selected (such as weekends or excluded weekdays) are **skipped entirely**

#### Example: Weekday-Based Tolerance Calculation

**Configuration:**

* Purchase Order Date: **Wednesday, 9 January**
* Tolerance Days: **3**
* Allowed Tolerance Days: **Monday, Tuesday, Wednesday, Thursday, Friday**
* Weekends (Saturday, Sunday): **Not selected**

#### Step-by-Step Calculation

Starting from the PO date (**9 Jan**):

**Counting backward (3 tolerance days):**

* Tuesday, 8 Jan → **Day 1**
* Monday, 7 Jan → **Day 2**
* Sunday, 6 Jan → _Skipped (not allowed)_
* Saturday, 5 Jan → _Skipped (not allowed)_
* Friday, 4 Jan → **Day 3**

➡ **Tolerance start date: Friday, 4 January**

**Counting forward (3 tolerance days):**

* Thursday, 10 Jan → **Day 1**
* Friday, 11 Jan → **Day 2**
* Saturday, 12 Jan → _Skipped_
* Sunday, 13 Jan → _Skipped_
* Monday, 14 Jan → **Day 3**

➡ **Tolerance end date: Monday, 14 January**

#### Resulting Tolerance Window

```
4 January  →  14 January
```

#### Why This Matters

If Allowed Tolerance Days are configured incorrectly:

* Delivery dates may appear **unexpectedly valid or invalid**
* Early or late deliveries may not be detected correctly
