# NOVA — Major Release

**Version snapshot: 16 October 2026**

NOVA adds guided document validation, more ways to improve automation, clearer e-invoice checks and better control over imports and document processing. These notes describe the customer-facing additions in the service versions listed below, compared with the last published [VESTA hotfix, R1.0.15 of 14 October 2026](incremental-updates-14-october-2026.md), including earlier VESTA hotfixes.

The snapshot identifies the builds covered by these notes. For availability in your sandbox or production environment and switching between channels, see the [DocBits release lifecycle](../docbits-release-lifecycle-strategy.md). Features that have an organisation or document-type switch still need to be enabled by an administrator.

## What changes for a VESTA customer?

| Area | Already available in VESTA | What NOVA adds |
| --- | --- | --- |
| Assistance | Settings Assistant and Header Field Check | A Validation Assistant inside documents, suggested actions, explanations and a separate chat window. |
| Automation analysis | Touchless Intelligence, supplier diagnosis and change proposals | Proposals learned from repeated corrections, improvement requests, an administrator review view, a consulting report and follow-up measurement. |
| Rules and layouts | Rule engines; some management controls required a beta link | Direct access to the management controls, richer layout selection, transformations after lookup and more accessible execution logs. |
| E-invoices | E-document validation and a rule catalogue | A clearer report organised by validation level, policy controls, change history and rejection from the report. |
| Imports | Email and FTP/SFTP import | A setup wizard, detailed FTP steps, retry settings, failure notifications, delete-after-import and proactive import-health guidance. |
| Processing | Page limits, PO matching and export | Restart with a selected page count, matching in both directions, and separate Exported and Finished statuses. |

## Validation Assistant: help with the document in front of you

* **Find what blocks progress.** Ask why a document cannot continue. The assistant identifies the affected fields, explains the problem and offers a jump to the field or table cell. It uses the current document and the user's access rights.
* **Review suggested corrections in context.** Where supported, reviewers can apply a proposed field or table value, use a master-data candidate, repeat a lookup or open the relevant matching screen. Form changes remain subject to the document's normal review and save process. Read-only documents and users without edit permission do not get editing actions.
* **Ask about matching and accounting.** The assistant can explain the purchase order or accounting context when opened on those screens. Changes to the validation form are made on the validation screen.
* **Understand an improvement before using it.** Explanations connect a proposed rule or setting to the document's actual values. They can include a diagram and a narrated explanation in the user's language when available. Suggestions are kept focused on the current document.
* **Work with the chat in a separate window.** Pop out the conversation while reviewing the document. Actions that change the form stay in the document window.
* **See more detail behind extracted values.** The value-origin view adds details such as OCR versus the PDF text layer, extraction-rule matching and the lookup that supplied a value. The AI table explanation adds more actionable setup advice and clearer counts.

An organisation administrator enables the Validation Assistant separately from the Settings Assistant under **Settings → Company Information → Assistants**.

## Turn repeated corrections into automation improvements

The existing [Touchless Intelligence](../../administration-and-setup/touchless-intelligence.md) dashboard gains a review and follow-up process:

* **Learned rule proposals.** Repeated manual corrections can suggest a transformation rule. Administrators see what it would write, the supporting examples and the documents on which it would replace a value the team had accepted. A proposal is reviewed before becoming an active rule.
* **Improvement requests from reviewers.** Users can submit an improvement from the document assistant for an administrator to review in Touchless Intelligence. The request keeps its explanation and decision together.
* **Measure what happened after activation.** For supported transformation rules, DocBits compares manual corrections before and after activation and shows the touchless rate alongside them. Measurement uses 14-day periods and identifies insufficient data rather than inventing an improvement. Changing a rule starts a new measurement for that revision.
* **Consulting report.** Administrators can generate a ranked view of improvement opportunities across extraction, master data, purchase order matching, accounting, settings and the processing flow. Estimated impact is labelled as an estimate until it has been measured.
* **Supplier-specific matching advice.** Repeated supplier and item matching problems can inform proposals for tolerances or matching rules. Advice distinguishes a missing purchase order from a rule or tolerance issue.
* **Follow-up summaries.** A weekly administrator summary brings together open improvement requests, leading opportunities and completed measurements when there is something to report. Requesters can be notified when a measured result is available.

## Settings Assistant: more actions and import-health guidance

The [Settings Assistant](../../administration-and-setup/settings/global-settings/company-information/settings-assistant.md) already shipped in VESTA. NOVA extends it with:

* **Proactive import-health cards.** Failed email and FTP connections appear in separate channel cards, with an expandable list of affected configurations, their retry or disabled state and the reported reason. Administrators can open import settings or ask for help from the card.
* **Visible deactivation history.** Where recorded, a disabled import shows when it was switched off and by whom.
* **Additional reviewed actions.** Administrators can preview and confirm supported changes such as activating document types, renaming a group, changing a lookup field's search mode, deleting a field or creating an inactive custom-validation rule from the catalogue.
* **Manage failing import connections.** Supported cards can switch off or delete a connection after confirmation. Reversible actions offer an undo; permanent deletion is identified as such.
* **Page explanations.** Selected settings pages offer videos with captions and transcripts, including layouts, users, sub-organisations, transformation rules and e-invoice validation where a language version is available.

## Rules and layouts: direct access and better diagnostics

* **Management controls without a beta link.** Manage Layouts, Custom Validation Rules and Transformation Rules are visible in NOVA's document-type advanced settings. Their enable switches remain under administrator control. The underlying rule engines are not new to NOVA; the wider access and refinements are.
* **Use values supplied by master data.** The transformation-rule option **Also run after master data lookup** lets an opted-in rule run after a lookup has populated fields, before purchase order matching. For example, a rule can use a supplier ID that only becomes known through the lookup.
* **Inspect rule execution from the dashboard.** Open a document's rule logs to see the validation, transformation and layout-selection rules involved. Selection rules have a log-execution option; rule editors can be opened by their identifier.
* **Choose layouts with more context.** The layout picker supports search and a preview of layout content. Selection rules can target approval layouts, and layout management fixes improve creating and cloning organisation layouts.
* **Clearer rule editing.** Conditions such as “is one of” support multiple selected values. Rule editors use the available screen width, and validation messages identify incomplete rule data more clearly. Copying standard line or table validation rules preserves the required table information.

See [Custom Validation Rules](../../administration-and-setup/settings/global-settings/document-types/custom-validation-rules.md), [Transformation Rules](../../administration-and-setup/settings/global-settings/document-types/transformation-rules.md) and [Layout Selection Rules](../../administration-and-setup/settings/global-settings/document-types/layout-manager/layout-selection-rules.md).

## E-Invoice Validation: clearer findings and policy controls

* **A report organised by validation level.** Findings are grouped into syntax, schema, business rules, cross-check rules and country-specific rules, with additional groups for other standards checks and value checks. Messages and summaries use the user's language where translations are available.
* **More complete checks and clearer results.** The updated validator and report distinguish errors, warnings and the effective severity after organisation-specific configuration. The page is named **E-Invoice Validation**.
* **Policies by document type.** Administrators can review whether e-invoice validation is enabled and whether failures block processing. The policy view identifies subtype overrides, and policy changes are recorded in a change history.
* **Reject with a recorded reason.** An authorised reviewer can reject an eligible document from the validation report. The report prepares a reason from its errors for the reviewer to check before confirming.
* **Further format corrections.** EDNA utility CII invoices are recognised, and corrections to XRechnung VAT mapping improve how relevant invoice values reach DocBits fields.

See [E-Document Validation Rules](../../administration-and-setup/settings/document-processing/e-documents/validation-rules.md).

## FTP/SFTP and email imports

* **Guided FTP/SFTP setup.** The connection wizard separates server details, import options and configuration. Connection checks and clearer errors help administrators identify an incorrect connection or a missing source folder.
* **Import logs by step.** Review the progress of a file through the FTP import, including upload and the configured action on the source file.
* **Configurable retry and notification behaviour.** Set the interval between later retries, how long to keep retrying and notification recipients. When the retry window is exhausted, the connection can be disabled automatically and recipients notified; the wizard shows the deactivation notice.
* **Delete after successful import.** In addition to retaining or archiving source files, administrators can choose to delete them from the FTP/SFTP server after a successful import. Archiving and deletion are separate alternatives.
* **More reliable import recovery.** Overlapping FTP runs are prevented from uploading the same source file twice. Editing a connection preserves its stored password unless it is replaced. Email handling does not mark a message for deletion when copying it failed.
* **Signed email support.** Opaque-signed S/MIME messages containing invoices can be unpacked rather than skipped.
* **Email configuration history and state.** Import settings show who last saved or activated a configuration. The inbound-email switch reflects the stored active state, including a newly saved configuration.

See [FTP Import](../../end-user-and-partner-section/end-user-section/how-to-import-documents/ftp.md) and [Test an FTP Import Connection](../../administration-and-setup/settings/document-processing/import/test-ftp-import-connection.md).

## Document processing and extraction

* **Restart with a chosen page count.** The dashboard adds a restart action that lets reviewers specify how many pages to process for that document, within its actual page count.
* **See the processing limit.** The dashboard can show processed versus total pages for a limited document. The organisation's **Pages to process** setting is grouped under Document Processing in **Classify & Extract**.
* **Control extraction of hidden fields.** Administrators can choose whether hidden fields take part in extraction through the **Extract hidden fields** setting.
* **Faster work on larger batches.** Bulk document restarts, master-data CSV imports, PDF processing and rule-based field extraction receive performance improvements.
* **More resilient AI extraction.** Timeouts are reported as timeouts, and supported model failures can fall back to another available model. Additional fixes handle repeated keys in AI output, configured field synonyms and empty saved table definitions.
* **Keep the value just entered.** Saving a table cell without first clicking elsewhere preserves the typed value. Dates with OCR-confused month names are handled more reliably.

## Purchase order matching, approval and export

* **Match in either direction.** Select document lines and connect them to purchase order lines, or start from the purchase order lines. This is useful when many delivery-note lines relate to one purchase order line.
* **Preserve one-to-many line detail.** A matching configuration can now retain an individual sub-line for each document line when several lines match one purchase order line. This option is off by default. Generic API export can group requests by configured line columns, supporting deliveries or containers that need separate target records.
* **Configure last-line fallback.** Organisations can control whether the remaining document and purchase order line may be matched by the single-line fallback.
* **More accurate matching and display.** Fixes preserve the correct price basis for package-converted matches, inherit the purchase order line's status on schedule rows and show received quantities from receipt lines.
* **Prevent premature approval and duplicate work.** The final approval is blocked while relevant purchase order discrepancies remain unapproved. Repeated workflow execution does not create another open task for the same group, and duplicate-export checks run before approval.
* **Separate Exported from Finished.** Export actions can select the status after a successful export. **Exported** has its own dashboard badge. Organisations that enable the finished-document lock prevent ordinary workflows or restarts from reopening finished documents; authorised overrides are recorded.
* **Clearer workflow troubleshooting.** A dashboard filter finds documents held back by the workflow execution limit. Workflow runs can be inspected in a popup, and a refused status change names the document's status.
* **Additional export fixes.** M3 validation and approval retries are adjusted, and conditional supplier export configurations are handled correctly.

## Everyday usability and access

* **More dependable navigation.** Updated document addresses have redirects for older links. NOVA deep links keep the intended channel through sign-in, and loading progress shows which part of the page is being prepared.
* **Personal working preferences.** Purchase order column order is saved per user, and the approval screen remembers the user's open sidebar panel.
* **More reliable task and dashboard views.** Tasks without an assignee can be listed, opened and assigned. The task board reloads when the selected organisation is ready, custom dashboard date ranges are applied correctly, and duplicate document rows are avoided.
* **Better labels and logs.** Administrators can edit field and table-column translation keys. Document-log columns can be resized, custom dashboard columns handle mixed-case field identifiers, and long labels and filenames fit more consistently.
* **Notification scope.** Document-status email rules can be limited to a sub-organisation.
* **Supplier onboarding.** Supplier Portal registration magic links remain valid for **21 days instead of 7 days**.
* **Sign-in reliability.** SAML sign-in no longer reuses expired or revoked sessions. Management sign-in supports the required MFA step, and inactive memberships cannot receive a new set-password invitation.
* **Idea Board images.** Uploaded images are stored and served separately from the idea description, improving image handling.
* **Controlled channel switching.** The Release Channel setting can be made read-only when switching is not enabled for the environment. Follow the release announcement for availability.

## Features already announced in VESTA

NOVA also carries existing capabilities. The following are **not** being announced as new in this major release:

* The original Settings Assistant, its documentation search and basic preview/confirm/undo flow.
* Fast, Full, Nexus and Auto AI tiers and the vision-mode setting.
* The Header Field Check and the original value-origin report.
* The first Touchless Intelligence release, supplier diagnosis, bulk analysis and the purchase order decision diagram.
* The underlying validation, transformation and layout-selection rule engines.
* Earlier dashboard search improvements, MFA, verified organisation email domains, charge tolerance and the increase of the workflow execution limit to 50.

See the [14 October VESTA hotfix](incremental-updates-14-october-2026.md), [15 September hotfix](incremental-updates-15-september-2026.md) and [earlier release notes](README.md#vesta-hotfix-releases) for those announcements.

## NOVA service versions

These are the versions and deployment timestamps in the **16 October 2026 snapshot**. The timestamps describe individual service deployments, not a separate release date for every feature.

| Service | Version | Deployment timestamp |
| --- | --- | --- |
| API Service | `13.26.5` | 16.10.2026 11:57:49 |
| Auth Bridge | `0.5.11` | 08.10.2026 10:56:15 |
| Auth Service | `1.84.3` | 16.10.2026 12:19:50 |
| Auto Accounting | `1.23.6` | 15.09.2026 09:42:57 |
| Barcode Service | `1.20.3` | 15.10.2026 14:17:18 |
| Docflow Service | `2.13.9` | 15.10.2026 16:14:37 |
| Docnet Service | `1.59.1` | 12.10.2026 00:59:12 |
| Email Service | `1.44.4` | 16.10.2026 11:44:58 |
| Extraction Service | `1.63.1` | 15.10.2026 19:34:17 |
| FTP Service | `1.37.4` | 15.10.2026 10:42:01 |
| Fulltext Service | `1.46.1` | 12.10.2026 05:16:16 |
| Ideas Service | `0.5.6` | 14.10.2026 12:06:00 |
| OCR Service | `1.11.8` | 12.10.2026 01:00:00 |
| Operator Service | `1.45.0` | 12.10.2026 09:35:25 |
| PO Match Service | `1.65.7` | 14.10.2026 16:14:20 |
| Web App | `10.72.2` | 16.10.2026 12:04:41 |

Version numbers advance independently on the two channels. A larger number does not by itself mean that a service has a new customer feature. The reviewed Auto Accounting, Barcode, Docnet, Fulltext, OCR and Operator changes are maintenance or processing-reliability changes; they do not introduce a separate customer workflow in this comparison. Auth Bridge updates improve the reliability of cross-region account synchronisation.
