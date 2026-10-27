---
description: DocBits Workflow Engine
---

# Workflow

<figure><img src="../../.gitbook/assets/Bildschirmfoto 2024-03-12 um 19.42.57.png" alt="Empty workflow builder with a Workflow name field, Add Card slots under When, And and Then, and a Save button"><figcaption></figcaption></figure>

## DocBits Workflow Engine: Simplifying Process Automation

### Understand and prepare workflows <a id="workflow-orientation"></a>

Follow the real DocBits test account: eight workflow executions in the dashboard, two saved workflows with execution order 100/200, and three passing test scenarios. The tutorial also explains Standard and Advanced Workflows, licenses, templates and the Card SDK.

{% embed url="https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/workflow-orientation-admin/v1/en.mp4" %}

[Watch with subtitles](https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/workflow-orientation-admin/v1/en.html) · [Open video](https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/workflow-orientation-admin/v1/en.mp4) · [Subtitles (WebVTT)](https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/workflow-orientation-admin/v1/en.vtt) · [Transcript](https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/workflow-orientation-admin/v1/en.txt) · 3:35

<details>
<summary>Chapters and transcript</summary>

| Chapter | Start |
| --- | --- |
| Meet the administrator | [0:00](https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/workflow-orientation-admin/v1/en.mp4#t=0.000) |
| Organization and access | [0:02](https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/workflow-orientation-admin/v1/en.mp4#t=2.292) |
| Dashboard and filters | [0:16](https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/workflow-orientation-admin/v1/en.mp4#t=16.708) |
| Workflow List | [0:56](https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/workflow-orientation-admin/v1/en.mp4#t=56.875) |
| Execution order | [1:14](https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/workflow-orientation-admin/v1/en.mp4#t=74.083) |
| Standard Workflow | [1:34](https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/workflow-orientation-admin/v1/en.mp4#t=94.458) |
| Advanced Workflow | [1:49](https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/workflow-orientation-admin/v1/en.mp4#t=109.792) |
| Licenses | [2:08](https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/workflow-orientation-admin/v1/en.mp4#t=128.875) |
| Templates | [2:30](https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/workflow-orientation-admin/v1/en.mp4#t=150.667) |
| Test Manager | [2:45](https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/workflow-orientation-admin/v1/en.mp4#t=165.542) |
| Card SDK | [3:02](https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/workflow-orientation-admin/v1/en.mp4#t=182.875) |
| Preparation checklist | [3:18](https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/workflow-orientation-admin/v1/en.mp4#t=198.583) |

**Meet the administrator**

I look after DocBits here.

**Organization and access**

All right, I start by checking the organization at the top. These workflow settings belong to the selected organization. For this lesson I use our documentation test account.

**Dashboard and filters**

Workflow Dashboard gives me the overview. For this overview, I manually ran two training workflows eight times against a sample invoice. Here I see eight total runs and six successful runs. In two runs, the amount condition was not met. The success rate also counts these correctly completed checks. I filter by workflow name and check the date range. The counters and chart update for that selection. On the right, I switch between saved workflows and test scenarios. Test Manager runs are counted separately.

**Workflow List**

In Workflow List I manage individual workflows. I check the name, Standard or Advanced type, execution order, trigger and available actions. Search helps me find an existing workflow before creating another.

**Execution order**

Execution order matters when several workflows affect the same document. I check which workflow should run first and what data the next one needs. Here the invoice review has an order of one hundred and the next check has two hundred. Lower values run first.

**Standard Workflow**

For a linear rule I choose Standard Workflow. When defines the trigger, And adds conditions, and Then performs the actions. The card library provides the available building blocks.

**Advanced Workflow**

For alternative routes I use Advanced Workflow. This designer preview shows Start and explicit connections. Success, a false condition and an error can follow different routes. Card position alone does not define execution order.

**Licenses**

Under License I check the basic Workflow module and Advanced Workflow separately. Both are inactive here. The plan dialog shows available subscriptions. I close this inspection without changing the subscription. A designer preview is not an active workflow engine.

**Templates**

Templates help me reuse a starting point. I inspect the template library and its default-template option. I still check every field, recipient and action before using a template for my own process.

**Test Manager**

Test Manager holds saved test scenarios for Standard and Advanced workflows. After configuring a workflow, I add representative inputs and expected results. Run All Tests helps me check changes against those scenarios.

**Card SDK**

Card SDK is for custom extensions. Here developers can use a template, upload a package or import from GitHub. Ordinary workflow administration starts with the existing card library.

**Preparation checklist**

Before building, I confirm the organization, access, required license, document fields and intended result. I decide whether a linear rule is enough. The next lesson builds a Standard Workflow step by step.

</details>

### Introduction

In the realm of process automation, the DocBits Workflow Engine stands out for its straightforward and intuitive approach. This engine streamlines the creation and management of workflows through a clear and simple rule-based structure. The core principle behind its design is the "Easy When-And-Then" rule, which breaks down the automation process into three fundamental components: Trigger, Condition, and Action. This guide explains how each component functions within the system and how they work together to facilitate seamless automation.

### The "Easy When-And-Then" Rule Explained

The DocBits Workflow Engine operates on a basic yet powerful principle that makes workflow automation accessible to users of all skill levels. This principle is encapsulated in the "Easy When-And-Then" rule, which can be broken down as follows:

#### [When](./#when-trigger) (Trigger)

* **Definition**: The "When" component represents the _Trigger_ of the workflow. This is the event or condition that initiates the execution of the workflow. Triggers can be a variety of occurrences such as the arrival of a new email, a specific date and time, or the creation of a new document.
* **Example**: "When a new customer form is submitted..."

#### [And](./#and-condition) (Condition)

* **Definition**: The "And" component introduces the _Condition_ that must be met for the action to proceed. Conditions serve as filters or criteria that refine the trigger, ensuring that the workflow is executed only under certain circumstances.
* **Example**: "...and the customer is from the 'Enterprise' segment..."

#### [Then](./#then-action) (Action)

* **Definition**: Finally, the "Then" part specifies the _Action_ to be taken once the trigger occurs and the condition is satisfied. Actions are the tasks or operations executed by the workflow, such as sending an email, updating a database, or creating a task in a project management tool.
* **Example**: "...then assign the lead to the enterprise sales team and send a welcome email."

### Combining Components for Powerful Automations

By assembling these three components—Trigger, Condition, and Action—the DocBits Workflow Engine allows users to create highly customized and efficient workflows. This modular approach not only simplifies the process of setting up automations but also offers the flexibility to create complex workflows capable of handling a wide range of tasks and processes.

### Conclusion

The DocBits Workflow Engine's "Easy When-And-Then" rule exemplifies the engine's commitment to providing a user-friendly platform for automating processes. This straightforward rule, by breaking down automation into the essential elements of Trigger, Condition, and Action, makes it easier for users to conceptualize, create, and manage workflows. Whether you are new to workflow automation or an experienced professional, the DocBits Workflow Engine offers an efficient and accessible tool to enhance productivity and streamline operations.

## Learning path from beginner to expert

[Learning path from beginner to expert](workflow-learning-path.md). Work through the levels in order. Reading alone is insufficient: finish each level with your own configuration, a checkable expectation and evidence. P0 prevents basic execution mistakes; P1 develops data handling, business decisions and integrations.
