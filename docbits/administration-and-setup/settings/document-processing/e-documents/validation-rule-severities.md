# Rule severities

Every validation rule has a severity. You can change the severity of each rule for your organisation. This page belongs to [E-Invoice Validation](validation-rules.md). Only organisation administrators can change the severities.

<figure><img src="../../../../.gitbook/assets/edoc_validation_rules_table.png" alt="The validation-rule table"><figcaption><p>The full rule table with per-rule severity override</p></figcaption></figure>

The rule table lists every validation rule (over 1,600 in total). Filter by **Layer**, **Profile** or **Version**, or search by code or field. For each rule you can override the **Severity** from the dropdown to match your organization's policy — for example, downgrading a rule from `ERROR` to `WARNING` so it no longer rejects the document.

The meaning of **FATAL**, **ERROR**, **WARNING** and **INFO** is explained on [Validation setup and accepted versions](validation-setup.md#accepted-profiles-and-severity-model). A changed severity also appears in the [validation report](validation-report.md) in the column **Your organisation**.
