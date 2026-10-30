# Continue with a chance

<figure><img src="../../../../.gitbook/assets/image (49).png" alt="" width="563"><figcaption></figcaption></figure>

## **Purpose:**

This DocBits card introduces a probabilistic condition, allowing workflows to continue with a set likelihood. The card is useful for testing scenarios, randomized selections, or controlled variability within processes.

## **Functionality:**

* **Conditional Continuation:** This card continues the workflow based on a specified probability, set by the user as a percentage value. The card generates a random outcome and compares it against the given percentage, creating a controlled chance for workflow continuation.
* **Chance Percentage:** Users specify a percentage value (0-100%) that represents the probability of the workflow continuing. For example:
  * **0%:** Workflow will never continue.
  * **50%:** Workflow has a 50/50 chance of continuing.
  * **100%:** Workflow will always continue.

## **Usage:**

This card is useful in scenarios where randomized workflow paths are needed, such as A/B testing, controlled sampling, or process simulation. It can also be applied to add variability in automated workflows.

## **Example Scenario:**

* A user configures the card with a **chance of 30%**. When the workflow reaches this card, there is a 30% probability that the workflow will proceed to the next step. This setup is ideal for scenarios where random sampling or partial processing is desired.

By using the "Conditional Continuation" card, organizations can introduce controlled randomness into workflows, facilitate process experiments, and enhance decision-making with probabilistic conditions.
