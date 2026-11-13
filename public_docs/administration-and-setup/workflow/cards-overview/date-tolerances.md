# Date Tolerances

Several workflow cards compare a date with a reference date and accept a tolerance of a number of days. They all calculate the tolerance the same way. This page explains that calculation, what each operator means, how the **Allowed Tolerance Days** work, and how to combine two cards for ranges such as "today or tomorrow".

The cards that use this calculation:

* [Table Date to Current Date](and/table/table-date-to-current-date.md) – a date in a document table compared with the current date.
* [Promised delivery date for line items in table with promised delivery date](and/compare-with-purchase-order/promised-delivery-date-for-line-items-in-table-with-promised-delivery-date/README.md) – promised delivery dates of line items compared with the current date.
* [Promised Delivery Date on Purchase Order](and/compare-with-purchase-order/promised-delivery-date-on-purchase-order.md) – delivery dates of line items compared with the delivery date on the purchase order.

{% embed url="https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/date-tolerances/v1/en.mp4" %}

**Video:** Date tolerances and range checks · 2:13 · [Captions (WebVTT)](https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/date-tolerances/v1/en.vtt)

<details>

<summary>Transcript</summary>

**Dates with a tolerance** · [0:00](https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/date-tolerances/v1/en.mp4#t=0.25)

Several workflow cards compare a date with a reference date and accept a tolerance in days. All of them count that tolerance the same way.

**The tolerance window** · [0:11](https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/date-tolerances/v1/en.mp4#t=11.583)

From the reference date, the tolerance is counted backwards and forwards. The result is a window, and both of its ends belong to it.

**Two days: Tuesday to Saturday** · [0:21](https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/date-tolerances/v1/en.mp4#t=21.95)

With two days around Thursday the twenty-second, the window runs from Tuesday the twentieth to Saturday the twenty-fourth. Today is the date on the DocBits servers, in U T C.

**Six operators, one window** · [0:35](https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/date-tolerances/v1/en.mp4#t=35.683)

Equals accepts dates inside the window, Not Equals dates outside it. Greater or Equals starts at the beginning of the window, Greater Than after its end. Less or Equals and Less Than work the other way round.

**Operator, days and weekdays** · [0:51](https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/date-tolerances/v1/en.mp4#t=51.083)

In the card, choose the operator, the tolerance in days, and the weekdays that are counted.

**Only selected weekdays count** · [1:04](https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/date-tolerances/v1/en.mp4#t=64.616)

Allowed tolerance days only count the selected weekdays. With Monday to Friday selected, one day after Friday is Monday, so the window runs from Thursday to Monday.

**Ranges need two cards** · [1:17](https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/date-tolerances/v1/en.mp4#t=77.95)

One card cannot accept exactly today or tomorrow, because its window reaches equally far in both directions. Two cards, one after the other, can.

**Equals 1 day, then Greater or Equals 0 days** · [1:31](https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/date-tolerances/v1/en.mp4#t=91.983)

The first card, Equals with one day, accepts yesterday, today and tomorrow. The second, Greater or Equals with zero days, accepts today and every later day. Only today and tomorrow pass both.

**Exclude a day with Not Equals** · [1:45](https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/date-tolerances/v1/en.mp4#t=105.716)

To leave out one day, add a Not Equals card with zero days. Here, Equals with three days and Greater or Equals with zero days give today up to three days ahead, and Not Equals removes today.

**Three cards, one range** · [2:00](https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/date-tolerances/v1/en.mp4#t=120.083)

In the designer, the three cards follow each other on the success path. The workflow continues only when all three succeed: from tomorrow up to three days ahead.

</details>

## The Tolerance Window

From the reference date, the tolerance is counted backwards and forwards. The result is a **tolerance window**: from the start date to the end date, both included.

* With a tolerance of **0 days**, the window is only the reference date itself.
* With a tolerance of **2 days**, the window reaches 2 days before and 2 days after the reference date.
* The **current date** is the date on the DocBits servers, which run in **UTC**.

Each operator compares the date with this window:

| Operator | True when the date is … |
|---|---|
| **Equals** | inside the window |
| **Not Equals** | outside the window |
| **Greater or Equals** | on or after the **start** of the window |
| **Greater Than** | after the **end** of the window |
| **Less or Equals** | on or before the **end** of the window |
| **Less Than** | before the **start** of the window |

Note that the tolerance also widens **Greater or Equals** and **Less or Equals**: with 2 days, **Greater or Equals** already accepts a date 2 days before the reference date.

<figure><img src="../../../.gitbook/assets/date-tolerance-operators-en.png" alt="Tolerance window of 2 days around a Thursday and the days each operator accepts"><figcaption><p>Reference date Thursday 22, 2 days tolerance: the window runs from Tuesday 20 to Saturday 24.</p></figcaption></figure>

## Allowed Tolerance Days

Cards that offer **Allowed Tolerance Days** only count the selected weekdays when the window is calculated. Weekdays that are not selected are skipped while counting, but they stay inside the window.

**Example:** reference date Friday, 1 day tolerance, only Monday to Friday selected. Counting backwards reaches Thursday. Counting forwards skips Saturday and Sunday and reaches Monday. The window is **Thursday to Monday**.

**Table Date to Current Date** adds one more check: the date in the table also has to fall on one of the selected weekdays. A Saturday inside the window is therefore not accepted by this card. The two other cards do not have this extra check.

<figure><img src="../../../.gitbook/assets/date-tolerance-weekdays-en.png" alt="Window of 1 day around a Friday with only Monday to Friday counted"><figcaption><p>Only Monday to Friday are counted, so 1 day after Friday is Monday.</p></figcaption></figure>

## Example: Today or Tomorrow

A single card cannot accept exactly "today or tomorrow", because the window always reaches the same number of days in both directions. Two cards one after the other can:

1. **Equals** with **1 day** tolerance accepts yesterday, today and tomorrow.
2. **Greater or Equals** with **0 days** tolerance accepts today and every later day.

Only dates that pass both cards remain: **today and tomorrow**.

<figure><img src="../../../.gitbook/assets/date-tolerance-today-or-tomorrow-en.png" alt="Equals with 1 day and Greater or Equals with 0 days, together accepting today and tomorrow"><figcaption><p>Today is Thursday 22: together the two cards accept Thursday 22 and Friday 23.</p></figcaption></figure>

The same way, other ranges can be built:

| Range | First card | Second card |
|---|---|---|
| Today or tomorrow | **Equals**, 1 day | **Greater or Equals**, 0 days |
| Yesterday or today | **Equals**, 1 day | **Less or Equals**, 0 days |
| Today up to 3 days ahead | **Equals**, 3 days | **Greater or Equals**, 0 days |
| Not today | **Not Equals**, 0 days | – |
| From the day after tomorrow | **Greater Than**, 1 day | – |

When only Monday to Friday are selected as **Allowed Tolerance Days**, "tomorrow" on a Friday is the following Monday.

## Conclusion

All date cards with a tolerance use one window around the reference date. Knowing where the window starts and ends makes it clear what each operator accepts, and two cards together can cover ranges that a single card cannot.
