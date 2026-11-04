# Our Document Priority System

In our document processing system, we handle a large volume of documents from multiple customers daily. To ensure that every customer's documents are processed in a timely manner, we have implemented a sophisticated priority system. This system dynamically adjusts priorities based on the number of pending documents a customer has, ensuring **fairness** and **efficiency**. Let's dive into how this priority system works and when the task counter is reset.

**Key Concepts of the Priority System**

Our priority system revolves around a few key concepts:

1. **Pending Documents**: This is a count of the documents a customer has submitted but are yet to be processed.
2. **Reset Interval**: The system periodically resets the pending document count to zero to ensure that no customer can monopolize the processing resources indefinitely.

**How the Priority is Determined**

Here's a step-by-step explanation of how the priority for processing documents is determined:

1. **Tracking Pending Docuemnts**: Each customer has a count of pending documents. This count helps us know how many documents are waiting to be processed for each customer.
2. **Resetting the Count**: To maintain fairness, we reset the pending documents count to zero if a set amount of time (the reset interval) has passed since the last update. This interval is set to 1500 seconds (or 25 minutes) by default.
3. **Updating the Count**: If the reset interval hasn't passed, we reduce the pending documents count by one each time we check, simulating the processing of a document.
4. **Setting Priorities**: The priority for processing tasks is based on the number of pending documents. The fewer the pending documents, the higher the priority, meaning those tasks will be processed sooner. We have specific thresholds to assign priority levels from 1 (highest priority) to 9 (lowest priority).

**Priority Levels**

The priority levels are assigned based on the pending documents count as follows:

* **Priority 9**: If the pending documents count is less than -20
* **Priority 8**: If the pending documents count is less than -14
* **Priority 7**: If the pending documents count is less than -12
* **Priority 6**: If the pending documents count is less than -10
* **Priority 5**: If the pending documents count is less than -8
* **Priority 4**: If the pending documents count is less than -6
* **Priority 3**: If the pending documents count is less than -4
* **Priority 2**: If the pending documents count is less than -2
* **Priority 1**: If the pending documents count is greater than or equal to -2

{% hint style="info" %}
In simpler terms, as the number of pending documents increases, the priority level lowers, meaning those documents are processed later compared to others with higher priorities.
{% endhint %}

**When the Counter is Reset**

The pending documents counter is reset to zero if more than the reset interval (**1500** seconds) has passed since the last update. This mechanism ensures that no customer can accumulate pending documents endlessly and hog the system resources. By periodically resetting the counter, we guarantee that every customer gets a fair share of processing time.
