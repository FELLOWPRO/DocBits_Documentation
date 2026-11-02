# Priority Policy

Choosing this option allows you to set priorities for each rule. The lower the selected number, the higher the priority (i.e., priority 1 has the highest priority). Rules are evaluated based on their priority order. The highest priority matching rule will be applied.

**Example:**

<table><thead><tr><th width="137">Rule</th><th width="110">Priority</th><th width="268">Condition</th><th>Return Group</th></tr></thead><tbody><tr><td>1</td><td>5</td><td>Total Amount &#x3C;= 1000</td><td>GROUP_1</td></tr><tr><td>2</td><td>4</td><td>Total Amount &#x3C;= 2000</td><td>GROUP_2</td></tr><tr><td>3</td><td>3</td><td>Total Amount &#x3C;= 3000</td><td>GROUP_3</td></tr><tr><td>4</td><td>2</td><td>Total Amount &#x3C;= 4000</td><td>GROUP_4</td></tr><tr><td>5</td><td>1</td><td>Total Amount &#x3C;= 5000</td><td>GROUP_5</td></tr></tbody></table>

If the total amount is **1500**, the rules evaluated will be:

* **Rule 1**: Total Amount <= 1000 (does not match)
* **Rule 2**: Total Amount <= 2000 (matches)
* **Rule 3**: Total Amount <= 3000 (matches)
* **Rule 4**: Total Amount <= 4000 (matches)
* **Rule 5**: Total Amount <= 5000 (matches)

Since the priority is applied in the order **5, 4, 3, 2, 1**, the highest priority matching rule will be **Rule 5** (**GROUP_5**). The decision tree will return **GROUP_5** because **Rule 5** has the highest priority (priority 1).
