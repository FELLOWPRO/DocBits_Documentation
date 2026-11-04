# Triggering Prompts with a Workflow



This guide explains how to configure a DocBits workflow to automatically trigger a saved prompt. This allows you to integrate Operator prompts into document processing flows without manual input.


### Step 1: Create a Prompt

Before linking a prompt to a workflow:

* Ensure your prompt is already created
* Include all necessary **variables** in the prompt body.

If you need help writing or saving prompts, refer to the [Prompt Writing Guide](../prompt-writing-guide.md) and [Operator Interface Overview](../).

### Step 2: Set Up the Workflow

Before configuring the Operator Prompt card, make sure your workflow is properly created.

1. Navigate to the **Workflow Builder** in the DocBits interface.
2. Create a new workflow or open an existing one.
3. Define the **trigger conditions**—these determine when the workflow will start (e.g., document type, status, field presence, etc.).
4. Add the necessary **action steps** to your workflow as needed.

<div align="left"><figure><img src="../../../.gitbook/assets/workflow_setup_example.png" alt="Workflow Setup Example"><figcaption></figcaption></figure></div>

### Step 3: Configure the Operator Prompt Card in the Workflow

In the Workflow Builder, use the **Operator Prompt card** to configure a prompt that should execute when the workflow's conditions are met.

<div align="left"><figure><img src="../../../.gitbook/assets/operator_prompt_card_configuration.png" alt="Operator Prompt Card Configuration"><figcaption></figcaption></figure></div>

#### Key Configuration Options

* **Script:**
  Select the saved **Organization Prompt** to be executed.
* **Script Data (Variables):**
  If the selected prompt contains variables, define their values here using key-value pairs.
  * If a variable is left empty here, the system will attempt to automatically populate it **from the document**.
  * For this to work, the variable name in the prompt must **exactly match** the **field ID** of the document attribute.
* **Max Steps:**
  Define the maximum number of steps the operator is allowed to execute during this prompt.
* **Max Retries:**
  Set how many times the system should retry the prompt in case of failure.
* **Execution Mode:**
  Choose whether the prompt should run:
  * **In the Cloud**
  * **On-Premises** (required if your ERP or target system is hosted locally)