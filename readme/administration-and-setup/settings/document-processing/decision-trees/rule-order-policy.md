# Rule Order Policy

This policy applies rules in the order they appear in the decision tree and returns the result of the rule that matches first.

**Example:**

| Rule | Condition            | Return Group |
| ---- | -------------------- | ------------ |
| 1    | Total Amount <= 1000 | GROUP_1     |
| 2    | Total Amount <= 2000 | GROUP_2     |
| 3    | Total Amount <= 3000 | GROUP_3     |
| 4    | Total Amount <= 4000 | GROUP_4     |
| 5    | Total Amount <= 5000 | GROUP_5     |

Given that the input value is **Total Amount = 2500**, the evaluation of the rules would be:

* **Rule 1**: Total Amount <= 1000 (does not match)
* **Rule 2**: Total Amount <= 2000 (does not match)
* **Rule 3**: Total Amount <= 3000 (matches)
* **Rule 4**: Total Amount <= 4000 (matches)
* **Rule 5**: Total Amount <= 5000 (matches)

Under **Rule Order**, the tree will process the rules in the order they are listed. So, the matching rules will be:

* **Rule 3**: GROUP_3
* **Rule 4**: GROUP_4
* **Rule 5**: GROUP_5

**Result**: **GROUP_3**, **GROUP_4**, **GROUP_5**
