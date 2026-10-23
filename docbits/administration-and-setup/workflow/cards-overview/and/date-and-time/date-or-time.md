# Date or Time

<figure><img src="../../../../../.gitbook/assets/workflow-card-runtime-window-20261023-en.png" alt="Version 2 example: Is, 2026-11-01 09:00:00 to 2026-11-01 17:00:00 (UTC)." width="650"><figcaption>Version 2 example: Is, 2026-11-01 09:00:00 to 2026-11-01 17:00:00 (UTC).</figcaption></figure>

## What this card checks

This condition compares the **current UTC date and time when the workflow reaches the card** with two configured bounds. Use it under **And → Date & Time** to restrict a following action to a planned time window.

## Configuration

Choose `is` for a time inside the window or `isnot` for a time outside it. Enter the start and end as explicit UTC date/time values. For a same-day window with the start before the end, both bounds are included.

## Practical example

<!-- workflow-card-practical-example-20261023 -->

**When to use:** Allow a maintenance follow-up only during a planned window.

**Configuration:** Select `is`, start `2026-11-01 09:00:00` and end `2026-11-01 17:00:00`, all in UTC.

**Expected result:** A workflow reaching this card at `2026-11-01 10:00:00` UTC meets the condition. At `2026-11-01 18:00:00` UTC it does not. Configure the workflow trigger and the following action separately.

## Timezone and overnight limits

Use UTC values throughout. Adding a timezone suffix does not convert a local time to UTC in the reviewed version 2 parser.

For an overnight window such as `22:00:00` to `04:00:00`, the reviewed version 2 implementation excludes the exact start and end instants from `is`. Check both boundaries before using an overnight rule. The example above uses a same-day window.
