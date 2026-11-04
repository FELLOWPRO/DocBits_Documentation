# On‑Premise Execution Flow

For customers running DocBits Operator on‑premises, the following sequence describes how a processed document triggers and executes an Operator prompt via the local DocBits Agent.

1. **Document Uploade & Processing**\
   A document is uploaded into DocBits and goes through the standard processing (Extraction, validation, etc.).
2. **Workflow Trigger**\
   Once processing completes, a configured Workflow in DocBits evaluates its trigger conditions. When those conditions are met, the Workflow creates a new **Operator Task**.
3. **Task Creation & Dispatch**
   * The workflow sends the script text, variables, max‑steps, max‑retries as a task payload to the shared Work Pool.
4. **Agent Polling Loop**
   * An on‑prem DocBits Agent (installed in the customer environment) polls the Work Pool every 5 minutes. If no tasks are found, the agent remains idle and retries after the interval.
5. **Task Execution**
   * When a task appears in the Work Pool, the Agent retrieves it and begins execution.
6. **Log Generation**
   * For each step—success or failure—the agent records detailed logs (actions, statuses, timestamps). Upon completion, it compiles the full log and final status.
7. **Result Return & Display**
   * The agent sends the logs and status back to DocBits. The originating workflow’s run history is updated, and users can review details in the **Workflow Logs** tab.

