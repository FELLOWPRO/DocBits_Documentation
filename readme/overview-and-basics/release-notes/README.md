# Release Notes

## **Release R1.1 — June 2026**

> **Sandbox Availability:** 25th June 2026

### New Features:

* **ZUGFeRD 2.5 / Factur-X 1.09 Support:**\
  Added support for the new ZUGFeRD 2.5 e-invoice standard (equivalent to Factur-X 1.09, the FeRD/FNFE-MPE common publication of June 2026). All five profiles are covered — MINIMUM, BASIC WL, BASIC, EN 16931 and EXTENDED — with classification, field extraction, transformation and preview. The EXTENDED profile recognises the new 2.5 fields: payment means and BIC, third-party payee (factor), and the allowance/charge tax-exemption reason. Unmarked Factur-X/ZUGFeRD CII invoices now default to the newest 2.5 handling.

## **Release R1.0 13/14 June 2026**

> **Sandbox Availability:** 28th April 2026

### New Features:

* **Activity Logging / Access Audit:**\
  Detailed activity logging and access audit trail across the application for compliance and monitoring. Different type of logging for all microservices and based on time range.

* **Global Quick Search:**\
  Press Cmd+K / Ctrl+K from anywhere in the app to search across 200+ routes and 40+ in-page features. Shows top 8 results with fuzzy matching, arrow key navigation, and links to the full App Index Page.

* **Sitemap (App Index Page):**\
  Searchable index page cataloging every navigable page and in-page feature (dialogs, sidebars, panels) across DocBits. Organized into 18 categories with type filters, category pills, URL-synced search, and permission-gated entries shown as locked for non-admin users.

* **Analytics Dashboard:**\
  Comprehensive document processing analytics with Executive Overview, API Metrics, Quality Metrics, Processing Performance, Document Flow Analytics, Activity Log, Event Log, and Audit Trail.

* **Dashboard Export Functionality:**\
  New dashboard export functionality allowing a list export in CSV or XLSX formats.

* **Full-Text Search / DocSearch:**\
  AI-driven vector search across all indexed documents with real-time vendor filtering, "Find Similar" feature, and configurable indexing settings.

* **Supplier Delivery Statistics:**\
  New views providing insights into supplier-related document processing metrics.

* **Debug Collector:**\
  Press Ctrl+Shift+P to capture a full debug snapshot including API calls, WebSocket state, errors, console logs, performance metrics, and environment info. Snapshots can be copied to clipboard or sent directly as a support ticket with an HTML-formatted report and attached JSON file.

* **AI Agents (DocNet):**\
  Autonomous background agents that automatically process incoming emails — classifying, extracting, and routing documents without manual intervention. Agents work through assigned tasks independently and escalate to users via approval requests when human judgment is needed. Includes a dedicated agent dashboard for monitoring activity and performance.

* **New E-Documents:**\
  Over 80 new global e-invoice types and 40+ new formats including XRechnung 3.0.2, ZUGFeRD 2.2/2.3.2, Factur-X variants, and Asia-Pacific PINT Credit Notes. 100% classification and extraction coverage.

* **AI Script Chat:**\
  AI-powered chat assistant for basic script development with real-time streaming responses.

* **Script Versioning:**\
  Full version history for scripts with change tracking, comparison, and restore capabilities. Provides version management to scripts similar to how versions of E-Docs are maintained.

* **Export History in Dashboard Actions:**\
  Access export history for a document directly from the dashboard action menu.

* **Generic API Exporter (APS450, GLS840):**\
  Configurable generic API export target via a Mapping-File-configuration, for flexible integration with external systems. Support for APS450 and GLS840 were implemented.

* **Multiple Export Configurations:**\
  Support for multiple active export configurations per document type with execution ordering and a re-export button for retrying from the failed step.

* **New Watchdog Version:**\
  Complete rework of the WatchDog Settings page. Added new quality of life features, including current WatchDog Status, guide and commands for installing, XSLT-template configuration and a setting for autoupdate. Also implemented the functionality for WatchDog to handle multiple configurations at the same time.

* **Vertex Integration:**\
  Consumer Use Tax integration via Vertex for automated tax calculation and compliance during document processing.

* **UI Redesign & Settings Rework:**\
  Comprehensive UI refresh across the application. Redesigned login and auth pages. Redesigned settings area with collapsible sidebar, organized subcategories, anchor-based navigation, context help panel, and status tracking badges. Document scripts UI changes. Document flow new UI. Enhanced List of Values UI.

* **Idea Board:**\
  Feature request board for users to submit, discuss, and vote on new features, enhancements, bugfixes needed, etc. with rich text editor and image support.

* **API Key Management:**\
  Dedicated settings page for creating, viewing, and managing multiple API keys.

* **Master Data Lookup Search Functionality:**\
  Improved Master Data search capability by providing suitable search options based on selected fields.

* **User Activity Chart:**\
  Visual chart displaying user activity patterns and engagement metrics. Dashboard for login activity with trend comparison charts, daily/weekly aggregation, and GeoLite2-based geolocation.

* **User Login History:**\
  Users Detail View with login history.

* **Customizable Sidebar:**\
  Drag-and-drop reordering, show/hide toggle, and pin-to-top for sidebar menu items. Preferences are persisted per user with a "Reset to default" option. Respects feature flags.

* **Video Carousel:**\
  Autoplay video carousel on the prepare-dashboard page showing short animated product tip videos (Global Search, Keyboard Shortcuts, Document Upload, Table Customization). Two-column layout with videos on the left and dashboard preparation on the right. Auto-redirect pauses while users browse videos.

* **Advanced Workflow Designer:**\
  Visual, node-based automation builder with drag-and-drop canvas for multi-step processing pipelines. Supports wait steps, parallel paths, reusable templates, Or condition cards, manual test/run button, "Test from Here" partial execution, and per-node execution logs with visual flow highlighting showing exactly which nodes were executed.

* **Workflow KPI Dashboard:**\
  Key metrics dashboard for monitoring workflow execution.

* **Workflow Partner Card SDK:**\
  SDK for third-party developers to build custom workflow cards, with AI-powered review, sandboxed validation, and getting-started documentation.

* **Workflow Test Manager:**\
  Automated test manager for workflows, allowing administrators to create and run tests individually or in bulk.

### Enhancements:

* **Database (All Modules) — Migration of ID Columns:**\
  All DocBits "ID" database columns were internally migrated from strings to dedicated ID-type (UUID7). Underlying Postgres database has been migrated to V18 to support this enhancement.

* **Document Processing — Further Enhancements:**\
  Changing the export logic related to maximum amount of pages to consider — now the whole document will be exported. During the document validation the user will have the option to override the default maximum pages limit for this specific document. The computation of Pending Document Counter has been enhanced.

* **Services Versions, Status & Deployment Date:**\
  Service availability status provided in the "Service Versions" popup.

* **Language Expansion:**\
  Support expanded to 22 languages with updated language selector.

* **Access Control Design on Field Level:**\
  Redesigned/improved access control with clearer activation state, field level access, consistent rule handling, and simplified group-based permissions. Fixes conflicting rules between Access Control and View Permissions, shows import owner in the UI, and applies access control consistently across field validation, AI-extracted tables, and all views.

* **Activity Stream for All Screens:**\
  Activity stream now available on all document processing screens (Ready for Validation, PO Matching, Accounting, Quote Details, Reject) — not just Pending Approval. Moved to a consistent right-panel position across all screens.

* **Document Flow Page:**\
  Dedicated page for visualizing and tracking the document processing flow, showing status transitions and progress through the pipeline.

* **Dual Monitor Mode (Global User Setting):**\
  Dual monitor mode moved to a global user setting, persistent across sessions.

* **Layout Builder Enhancements:**\
  Support for hidden and read-only fields with visual indicators, resizable panel divider, and field length settings. Apply the Default Layout to multiple origins without visiting each one individually.

## **Release HotFix 3 16th April 2026**

### DocBits Enhancements:

* **QR Code Extraction for Polish Invoices:**\
  DocBits now supports QR code extraction specifically for Polish invoices, improving automated data capture for documents originating from Poland.

### Bug Fixes:

* Fixed an issue where auto export failed when PO matching had already taken place but the purchase order was not associated with the document.
* Fixed an issue where unit prices were incorrectly rounded for invoices with packaging units (Verpackungseinheiten / VPE).
* Fixed an issue where export error messages from ION/MEC (e.g., Acknowledge.PurchaseOrder failures) were not displayed in DocBits, showing "Exported" status despite the export having failed.
* Fixed an issue where the unit price on the approval screen was incorrect when AI table extraction was used.
* Fixed an issue where the Total Matching script threw an error on the validation screen.
* Fixed an issue where document processing failed with an error ("UserAuthentication object has no setter for 'org_id'").
* Fixed an issue where table training was not working for specific vendors, with columns landing in hidden columns instead of mapped fields.
* Fixed an issue where PO matching failed on large invoices (10+ pages) due to the multipart request size limit being exceeded.
* Fixed an issue where script-populated column values were not persisted after a document restart.
* Fixed an issue where the "Ignore Table Validation" toggle showed as active (green) in the UI but was actually deactivated in the background.
* Fixed an issue where document quality was significantly degraded after import.
* Fixed an issue where microservice versions and deployment dates displayed in the app were inconsistent across environments after a complete deployment push.
* Fixed an issue where barcode extraction failed due to an error when building the user authentication object from task data.
* Fixed an issue where supplier contact details were emptied when saving in the supplier portal.
* Fixed an issue where documents ran into a NoneType error on export.
* Fixed an issue where the email body was not included when the first attached file was a PNG or JPEG image.
* Fixed an issue where the email body was missing for several documents.
* Fixed an issue where the DocBits Operator "ai-exporting" did not produce export results in the target systems (LN/D3).

## **Release HotFix 2 31st March 2026**

### DocBits Enhancements:

* **Hybrid PDF Processing — User-Controlled XML Extraction:**\
  When a PDF contains embedded XML data, users can now choose whether DocBits should use the embedded XML for extraction or process the document as a standard PDF. This gives organizations full control over how hybrid documents are handled, ensuring the extraction method best suited to their workflow is applied.

* **AP Assignment Code on Approval Screen:**\
  The AP Manager Approval page now includes an AP Assignment Code field, integrated with Infor M3 CRS620. This allows approvers to review and confirm assignment codes directly during the approval process without switching to external systems.

* **PO Total Matching with Document Total:**\
  DocBits now supports matching the purchase order total against the total on the document, providing an additional validation layer during PO matching to catch discrepancies earlier in the process.

* **Supplier Item Number and VPE Update:**\
  DocBits now supports updating Supplier Item Number and VPE (Verpackungseinheit / packaging unit) fields during document processing, with the values being synchronized back to M3 upon export.

* **Improved Document Layout Classification:**\
  The document layout ID (tfidf_id) is now generated based on header text only, excluding footer text. This improves classification accuracy by preventing footer content from influencing document type detection.

* **Export & Next Button:**\
  A new "Export & Next" button has been added, allowing users to export the current document and immediately proceed to the next one in the queue, streamlining the review and export workflow.

* **Approval Process for Cost Invoices:**\
  The approval process for cost invoices has been enhanced with improved routing and validation logic.

### Bug Fixes:

* Fixed an issue where the Infor SFTP export failed with an error due to an incorrect library command.
* Fixed an issue where boolean checkboxes could not be displayed on the approval screen.
* Fixed an issue where UNMU messages were sent even when there were no mismatches in the purchase unit.
* Fixed an issue where sales tax was incorrectly classified as a charge on the PO Matching screen, resulting in a negative unsettled amount.
* Fixed an issue where the export failed when the purchase unit was not set in the order confirmation but was present in the purchase order.
* Fixed an issue where the email body was missing for several documents.
* Fixed an issue where the Supplier Item Number was not visible on the approval screen and updates were not sent to M3.
* Fixed an issue where the supplier export to Infor returned an error.
* Fixed an issue where PO Matching produced errors during processing.
* Fixed an issue where the `findAll` function was not working correctly in document scripts.
* Fixed an issue where the Watchdog "Updated By" column incorrectly showed the Fellow Admin user instead of the actual user.
* Fixed an issue where BOD-Mapping could not be configured in the Watchdog UI.
* Fixed an issue where charges were incorrectly shown as unsettled amounts instead of being displayed as charges.
* Fixed an issue where auto-matching did not work for multi-line invoices despite a matching configuration being in place.
* Fixed an issue where a hyphen ("-") in the item number was considered during PO matching for the purchase order but ignored on the invoice, causing a false mismatch.
* Fixed an issue where both PDF and XML files were uploaded to the export folder even when the "Export PDF" toggle was disabled.
* Fixed an issue where a missing status on the workflow card prevented documents from progressing through the workflow.
* Fixed an issue where document quality was significantly degraded after import.
* Fixed an issue where the PO Match screen threw an error ("Cannot read properties of null").
* Fixed an issue where the default list of values could not be edited.
* Fixed an issue where the workflow could not read the field status properly, causing incorrect routing.
* Fixed an issue where inbound email imports failed with an error.
* Fixed an issue where missing lines were not arriving correctly in M3 during export.
* Fixed an issue where coded and approved invoices were occasionally not being updated to "approved" status in M3 via the APS110 API.
* Fixed an issue with the Multi Banking configuration not working correctly.
* Fixed multiple issues with shared dashboard display and save behavior.
* Fixed an issue where the Supplier Item Number field was limited to 30 characters, preventing longer values from being stored.
* Fixed an issue where unit price and unit price per values caused an error during export.
* Fixed an issue where PO lines with an excluded status (e.g., "Closed") could still be dragged and matched on the PO Matching screen despite being excluded by matching rules.

### Configuration Changes:

* Updated email templates to remove the "Go to Task" button.
* Adjusted scripts and mandatory field settings on costing elements.

## **Release HotFix 1 16th March 2026**

### DocBits Enhancements:

* **Document History in SFTP Export:**\
  DocBits now supports including the full document history as part of the exported XML payload when exporting to SFTP. This feature is configurable via the Export Settings and provides downstream systems with a complete audit trail of every status change and action taken on a document within DocBits — including who made the change, when it occurred, and what the previous and current statuses were. This is particularly valuable for compliance, traceability, and operational analysis.
* **Charges Update on Order Confirmation for Infor On Premise:**\
  Infor On Premise customers can now process Order Confirmations that include charges directly within DocBits. The charges are fully updated through the export, making the end-to-end Order Confirmation process seamless and removing the need for manual adjustments downstream.
*   **Apply Default Layout to All Origins:**\
    A new **Apply Default Layout to Origins** button has been introduced in the layout configuration screen. Administrators can now push the Default layout to all origins within an organization in a single action, eliminating the time-consuming manual process of copying and pasting layout JSON across each origin individually. This is especially useful during new customer onboarding where multiple origins need to be configured consistently.

    <figure><img src="../../.gitbook/assets/image (5).png" alt=""><figcaption></figcaption></figure>
*   **Document Type Selection for FTP Import:**\
    FTP import configurations now support per-folder document type assignment. When configuring an FTP import, users can specify which document type — such as Invoice or Order Confirmation — should be applied to all documents imported from that folder. Documents are automatically classified upon import, removing the need for manual document type assignment after ingestion. This supports organizations that manage multiple document types across different sub-organizations and folders.

    <figure><img src="../../.gitbook/assets/image (4).png" alt=""><figcaption></figcaption></figure>
* **Export to GLS840 for Infor On Premise**:\
  DocBits now supports exporting documents to the GLS840 program for Infor On Premise customers, expanding the range of supported export targets for on-premise environments.
*   **UI Enhancements for Watchdog and Export Configuration:**\
    The Watchdog configuration and Export configuration screens have been refreshed with an improved user interface, offering a cleaner layout and a more intuitive experience for administrators managing these settings.

    <figure><img src="../../.gitbook/assets/image (1).png" alt=""><figcaption></figcaption></figure>



    <figure><img src="../../.gitbook/assets/image (2).png" alt=""><figcaption></figcaption></figure>

### Bug Fixes:

* Fixed an issue where users with valid viewing rights were unable to view documents — permission logic has been refactored with an access-level check replacing the previous group-based filtering approach.
* Improved exception handling across multiple areas of the application for greater stability.
* Resolved an issue where boolean type columns were not handled correctly during field extraction.
* Fixed an async authentication issue in the file upload endpoint.
* Resolved UI display issues for the PO table on the validation screen.
* Updated the script template to include change-tracking comments for better auditability.
* Fixed an issue with dropdown fields not behaving correctly on the validation screen.
* Fixed an issue where the sub-organisation field was not pre-filled when updating document assignments from the dashboard.

## **Release Winter Summit 10th December 2025**

### DocBits Enhancements:

*   **Enhanced PO-Matching Rule Customization:**\
    DocBits now provides more granular and customizable control over purchase order matching rules. Administrators can configure precisely which columns should be evaluated during the matching process for each document type, ensuring that only the most relevant fields are considered. In addition, tolerances can be defined at the column level, allowing for greater flexibility when handling minor discrepancies. Each rule can also be configured to apply to manual matching, automatic matching, or both, giving teams the ability to tailor the matching workflow to their exact operational requirements. These enhancements significantly improve the adaptability and precision of the purchase order matching process.

    <figure><img src="../../.gitbook/assets/release_notes_12_2025_3.png" alt=""><figcaption></figcaption></figure>
*   **Support for Multiple Supplier Financial Accounts:**\
    DocBits now supports managing multiple financial accounts for suppliers through the RemitToPartyMaster BOD provided by Infor. This enhancement allows organizations to maintain several remit-to account records for a single supplier, improving flexibility and accuracy in payment processing. A new configuration setting has been introduced to enable or disable this capability, allowing administrators to activate the feature based on their operational needs.

    <figure><img src="../../.gitbook/assets/release_notes_12_2025_1.png" alt=""><figcaption></figcaption></figure>
*   **Add User Access to OCR Extraction Results:**\
    The **OCR View** button on the Field Validation screen is now available to all users who have validation access, rather than being limited to administrators. With this update, any authorized user can review OCR extraction results directly, making it easier to validate data accuracy and monitor overall OCR performance. This enhancement promotes greater transparency and improves the efficiency of the validation workflow.

    <figure><img src="../../.gitbook/assets/release_notes_12_2025_2.png" alt=""><figcaption></figcaption></figure>
* **Dynamic Column Rendering in Approval Screens:**\
  Enhanced approval views to dynamically display only the columns configured for comparison in each organization’s database preferences. Previously, some of the organization specific columns would appear empty when not configured for comparison, causing confusion. Now, approval views only show fields that are actively being compared. This provides clearer, organization-specific approval screens without empty or irrelevant columns.
* **Order Type Field Added to Master Data Lookup**:\
  Purchase order header list now includes an "Order Type" column in master data lookup, providing additional categorization capabilities.
* **Custom Filter Dashboard Improvements:**\
  The dashboard sharing functionality has been enhanced to provide greater flexibility for shared users. Individuals who have dashboards shared with them can now adjust and edit the dashboard filters, enabling them to tailor the displayed information to their specific needs. This improvement supports a more personalized and interactive viewing experience, ensuring that users can easily refine the data insights most relevant to their tasks.
* **Customizable Prefixes for Approval Screen Columns:**\
  A new configurable option has been introduced to display prefixes before document columns on approval screens. This feature can be managed directly within the layout builder, giving administrators full control over whether prefixes are shown and which document types they apply to. By enabling this option, users gain clearer context and improved readability when reviewing documents during the approval process.

### General Improvements

* Improved error logging for poorly trained tables in table extraction.
* Added a sharing limit for dashboards of up to 10 users or 5 groups, along with a clear error message when the limit is reached.
* Improved error handling for custom dashboards when a user attempts to create a dashboard with a name that already exists.

### Bug Fixes:

* Fixed an issue where emails appeared to send successfully from the Supplier Details section but were not delivered to recipients.
* Fixed an issue where Dropdown fields added to approval/rejection screens didn't display.
* Fixed an issue where all exported documents were marked as last updated by wrong user.
* Fixed an issue where documents showed "Workflow in Progress" status but no workflows executed and log stayed empty.
* Fixed an issue where unrelated users were being assigned to documents at export time without performing any work on them.
* Fixed an issue where users with correct permissions were unable to reject assigned documents and received errors.
* Fixed an issue where document flow icons were not displaying for some organizations.
* Fixed an issue where a popup appeared when uploading documents with drag and drop to the dashboard.
* Fixed an issue where E-TEXT flags were showing as enabled in the UI even though API response showed all values as false.
* Fixed an issue where an error occurred when uploading documents containing blank pages.
* Resolved an issue where task hyperlinks in email notifications did not redirect users to the correct approval screen.
* Resolved an issue where selecting the cross sub-organization caused the Master Data Lookup to show no suppliers. Users can now correctly view cross-organizational supplier data.

## Release Autumn Summit 22nd October 2025

### DocBits enhancements:

*   **Email Template Design Improvements:**

    The email template editor has been redesigned to provide a clearer structure and smoother experience. Selecting document fields is now more intuitive, and attachments can be included directly within templates. These improvements make it faster and easier to create professional, tailored emails.

    <figure><img src="../../.gitbook/assets/image (310).png" alt=""><figcaption></figcaption></figure>
*   **Dashboard Enhancements:**

    The dashboard has been extended to improve navigation and customization. With new tabs, users can switch more quickly between different document types, reducing the time spent searching for the right view.

    <figure><img src="../../.gitbook/assets/image (474) (1).png" alt=""><figcaption></figcaption></figure>
*   **Custom FilterDashboards:**\
    In addition, dashboards can now be customized and filtered according to individual preferences. These custom dashboards can also be shared with colleagues, making it\
    easier to create consistent team-wide reporting views.

    <figure><img src="../../.gitbook/assets/image (477).png" alt=""><figcaption></figcaption></figure>
*   **Email Notification Logs:**

    A new logging feature is available for all email notifications. Users can now review a history of sent notifications, making it easier to verify deliveries and troubleshoot issues if emails are not received.
*   **E-Invoice Support: e-SLOG 1.6 & 2.0:**

    Support for additional e-invoice formats has been introduced. The system can now process and generate e-SLOG versions 1.6 and 2.0, expanding compatibility with partners and regulatory requirements.
*   **Duplicate Detection Enhancements:**

    Duplicate detection has been upgraded with two powerful configuration options. The **Duplicate Detection Interval** allows you to define a time range to check for duplicates more precisely, while the **Disallow Export of Duplicates** setting automatically prevents the export of documents that are detected as duplicates. Together, these enhancements provide more control and ensure higher data accuracy.

    <figure><img src="../../.gitbook/assets/image (478).png" alt=""><figcaption></figcaption></figure>
*   **Decision Tree Enhancements:**

    Decision trees are now more versatile, with the ability to return document field values. This allows for more advanced automation logic, enabling workflows to make decisions based on actual document data.
*   **New Workflow Cards:**

    Two new workflow cards expand automation capabilities. The first allows you to check whether a document belongs to a specific sub-organization, making it easier to handle multi-entity setups. The second introduces a delivery date tolerance check, which compares delivery dates against the current date in business days to help manage and enforce delivery requirements more effectively.
*   **CSV Export Improvements:**

    The CSV export feature has been significantly improved. Instead of only exporting the documents displayed on the current page, the system now exports all documents in a dataset. Each export creates a log entry, and the resulting CSV is automatically sent via email, providing a more complete and reliable export process.
*   **Purchase Order Deletion Timeframe:**

    A new configuration option allows administrators to define a timeframe for purchase order deletion. This improvement adds flexibility and control over data retention policies, ensuring purchase orders are only removed when appropriate.

### Bug Fixes

* Fixed an issue where old data was included when exporting documents.
* Corrected the filter for Export Errors, which previously showed other statuses as well.
* Resolved a table-validation mismatch where “Unit Price” triggered errors but “Unit Price Per” did not, despite values being correct.
* Fixed a problem where adding a new column to the dashboard failed.
* Corrected an issue where tasks were not visible in the dashboard task column.
* Fixed random sorting behavior so that lists now follow a consistent order.
* Resolved an issue where changing the column size could not be stopped.
* Fixed a bug preventing manual line matching in the PO-Matching screen.
* Corrected an issue where the email attachment option was reset after saving.
* Fixed a problem where auto accounting initially displayed database IDs when opened for the first time.
* Corrected fuzzy field behavior so values are no longer overwritten incorrectly.
* Fixed an issue where fields in auto account disappeared after deleting content.
* Corrected a bug where the user could not rename “First Name” and “Last Name” in the settings popup.
* Resolved a problem where documents could get stuck in “workflow in progress.”
* Fixed a menu icon color issue where selected organization colors were not applied correctly.
* Corrected an issue where QR codes were sometimes not recognized.
* Fixed a problem where accounts could not be removed with backspace to enter a different one.
* Resolved a language mix-up after logging in following the production push.

## Release **Summer Bloom** July 2025

### DocBits enhancements:

* **Filter Option for Email Import Log:**\
  Users now have the ability to filter the import logs and sort the table for a clearer, more efficient overview. This enhancement streamlines the process of identifying and managing email entries, improving troubleshooting and overall log management.
*   **Multi-Language Support for List of Values :**\
    We've expanded multi-language capabilities to the List of Values feature. Administrators can now define labels in multiple languages, ensuring that the correct label is automatically displayed based on the user's system language settings. This enhancement promotes greater accessibility and localization, making it easier for users worldwide to interact with the platform in their native language.

    <figure><img src="../../.gitbook/assets/image (13) (1) (1) (1) (2).png" alt=""><figcaption></figcaption></figure>
* **User Detail Enhancements in Settings:**\
  The settings interface now displays comprehensive user information. Administrators can easily view group affiliations, sub-organization details, and additional key data, enabling better management of user roles and a clearer understanding of team structures. Furthermore Admins can now create a System Admin for the Organization.
* **Auto Accounting Information on the Approval Screen:**\
  The approval screen now presents auto accounting details alongside invoice information. This improvement provides deeper insight into transaction data, facilitating smoother review processes and more informed decision-making regarding invoices.
* **Task Counter for Documents on the Dashboard View:**\
  Documents on the dashboard can now indicate open tasks associated with them and display the total number of pending tasks. This feature provides users with a quick overview of outstanding actions, improving task management and workflow efficiency.
* **Supplier-Based AI Model Selection:**\
  Users can now select the AI model used for data extraction on a per-supplier basis. This enhancement allows for fine-tuned optimization, ensuring better extraction accuracy for different suppliers and improving overall data processing results. [Learn more](https://docs.docbits.com/end-user-and-partner-section/end-user-section/validation-screen#supplier-based-ai-model)
* **Enhanced Workflow Logs for Decision Tree Cards:**\
  The logs now display the output of the decision tree, making it easier to track and understand how decisions were made within workflows.
*   **Introduction of New Auto-Testing Setup to Enhance System Functionality and Stability:**

    We are excited to announce the implementation of a new automated testing system designed to improve the overall functionality and reliability of our platform. This new setup will run consistent, thorough checks on our system to identify any issues before they impact your experience. By automating these tests, we can ensure faster responses to potential problems and maintain the highest standards of quality for our system.
* **Microservices Architecture Implementation:**\
  We've restructured the platform by splitting core components into dedicated microservices. This architectural shift enhances scalability, improves system performance, and enables faster, more modular development and deployment cycles.
*   **Walkthrough:**\
    A guided walkthrough is now available to help users navigate and understand different parts of the application more easily. This is especially useful for onboarding new users or exploring unfamiliar features.

    <figure><img src="../../.gitbook/assets/image (430) (1).png" alt=""><figcaption></figcaption></figure>
* **Decision Tree Improvements:**\
  Enhancements have been made to the decision tree interface, including a more intuitive row addition feature — now located at the top of the tree — to simplify maintenance and editing.
* **DocOperator**\
  New AI-powered tools like DocOperator help automate repetitive tasks, improving efficiency and reducing manual effort across document workflows.
*   **Electronic Document Preview Option:**\
    A preview feature has been added for electronic documents (eDocs), allowing users to test and view changes directly within the settings before deploying them.\\

    <figure><img src="../../.gitbook/assets/image (3) (1) (1) (1) (1) (1).png" alt=""><figcaption></figcaption></figure>
* **New Language Support – Chinese:**\
  DocBits now supports Chinese, expanding accessibility and localization options for users across global markets.
* **Improved Task Dashboard:**\
  The task dashboard has been enhanced to display a larger number of tasks at once, giving users a clearer overview and improving task tracking.
*   **PO Matching Improvements:**

    Added visual indicators for different matching states

    New setting to ignore already matched PO lines per document type

    Improved auto-check for PO updates to ensure consistency
* **Layout Builder Improvements:**\
  You can now search for both field names and field titles, making it faster and easier to configure and locate layout components.
* **Export and Next Button in Approval Screen:**\
  A new button has been added to the approval screen that allows users to export a document and automatically proceed to the next one in the “Ready for Validation” queue.
* **New Workflow Cards:**\
  New workflow cards have been introduced, including ones for running workflows on new purchase orders and quote-related events. These provide more automation options.
*   **Watchdog Improvements:**\
    Watchdog configuration has been moved into the main application UI, making it easier to manage. Additional functionalities have also been introduced for better monitoring and control.\\

    <figure><img src="../../.gitbook/assets/image (4) (1) (1) (1) (1).png" alt=""><figcaption></figcaption></figure>
* **Line Rejection Enhancements:**\
  Rejecting a line item now requires users to provide a reason, ensuring better traceability and accountability in review workflows.
* **Supplier AI Model List in Settings:**\
  A new settings view displays the AI models assigned to specific suppliers, along with an option to reset them. This improves transparency and manageability of supplier-based AI configurations.
*   **Document Log Improvements:**\
    The document logs now include more detailed information to support better auditing and troubleshooting.

    <figure><img src="../../.gitbook/assets/image (5) (1) (1) (1) (1).png" alt=""><figcaption></figcaption></figure>
* **PNG and JPG Support:**\
  You can now upload PNG and JPG files, which will automatically be converted into PDF format for processing.
* **IDM Export Document Format Configuration:**\
  The export format for PDFs in IDM can now be configured, giving users more control over how documents are generated.
* **New eDoc Type – EDIFACT INVOIC02:**\
  We now support the EDIFACT INVOIC02 electronic document type, expanding compatibility with standardized invoice formats.
*   **Email Notification and Template Options**

    DocBits now offers enhanced control over email notifications, including:

    * **Timed Resend:** Automatically resend notification emails after a defined period if no action is taken, ensuring that tasks aren't missed.
    * **Resend on Reassignment:** Notifications can also be triggered when tasks are reassigned, keeping users up to date with changes in responsibility.
    * **Custom Email Templates:** Administrators can now create and manage email templates to customize subject lines, message content, and formatting. This allows for personalized, context-aware notifications that match your organization’s communication style.

    These additions improve communication efficiency and reduce delays in document handling workflows.
*   **PO Status on Dashboard**

    The dashboard now includes an option to display the **status of linked purchase orders (POs)** directly within document overviews. This enhancement provides users with at-a-glance insight into PO progress—such as received or invoiced—enabling quicker decision-making and better alignment between documents and procurement processes.

### Bug Fixes

* Resolved an issue where tasks were not appearing on the validation/approval screen.
* Fixed the positioning of the Next/Previous button so that it remains static.
* Fixed scrolling issues in the script and decision tree views, ensuring that action buttons remain stationary during scroll.
* Removed the origin country field from e-invoices.
* Fixed an issue with the task counter displaying an inaccurate number of tasks.
* Added missing translations.
* Corrected custom fields to display descriptive names instead of IDs.
* Resolved an issue where documents were downloaded with an incorrect file name.
* Fixed sorting inconsistencies in the invoice line table within PO matching.
* Fixed an issue affecting task creation functionality.
* Fixed an issue in PO matching where the invoice table sorting would reset when matching a line.
* Resolved auto accounting issues by ensuring booking references split correctly when an amount is divided.
* Updated the ClickHouse host information.
* Resolved an issue where duplicate documents were not recognized as duplicates.
* Fixed export issues caused by booking references that were too long.
* Fixed the predictions given for auto accounting.
* Resolved an issue where readonly checkboxes where not readonly
* Fixed an issue where Users can be added to a sub-organization twice
* Fixed an issue where changing the sub-organization for a document caused to reset the assigned user or group
* Resolved some issues with auto.accounting Screen
* Fixed an issue where users are unable to add FTP configuration
* Fixed an issue with the SSO login
* Fixed some issues related to Inbound Emails
* Fixed an issue with documents getting a wrong name when downloading them
* Fixed an wissue where the decision tree returns incorrect result

## Release Hot Fix Winter Frost 10th April 2025

### DocBits enhancements:

* **Enhanced `set_column_date_value` Script Function:**\
  The `set_column_date_value` function now includes support for the `skip_weekend` option, allowing date values to automatically skip weekends when applied.
* **Improved File Upload Support:**\
  PNG and JPEG files can now be uploaded directly and are automatically converted into PDF format for streamlined document handling.
* **Watchdog Functionality Upgrades:**
  * Now supports export to **Enaio** for better system integration.
  * Enhanced parsing capabilities to extract information from `Sync.ContentDocument` XML structures, enabling more efficient data processing.

### Bug Fixes

* Fixed an issue on a script function.
* Resolved an issue where Purchase orders had a wrong status after they where updated

## Release Hot Fix Winter Frost 17th March 2025

### Bug Fixes

* Improved the shortcuts.

## Release Hot Fix Winter Frost 11th March 2025

### DocBits enhancements:

* **Improved Data Extraction:** Added an option to extract the **Purchase Order** or **Item Number** from a line above or below.
* **Expanded Cross Sub-Organizations Access:** Non-admin users can now also access the **Cross Sub-Organizations** feature. [Learn more](https://docs.docbits.com/administration-and-setup/settings/global-settings/groups-users-and-permissions/sub-organizations#cross-sub-organisations-access)

### **Bug Fixes:**

* Fixed an issue where users could not be added to a group.
* Fixed an issue with email import failures.
* Resolved an issue with the field training on documents with more than page
* Fixed an issue where scripts didn’t work properly.
* Resolved an issue where document data didn't get displayed correctly
* Fixed an issue with the auto update purchase order setting
* Fixed an issue where the subscription tokens got displayed wrong
* Resolved an issue where the task screen displayed an outdated document version
* Fixed an issue that caused documents to not change their status

## Release Hot Fix Winter Frost 3rd February 2025

### **DocBits Enhancements:**

* **Support for ISO-8859-1 for ZUGFeRD:** Improved compatibility for invoices using ISO-8859-1 character encoding.
* **Optimized Logging System:** Enhanced tracking and diagnostics for quicker issue identification and resolution.

## Release Winter Frost 22nd January 2025

#### New Features

### Support for ZUGFeRD 2.1 and Newer

DocBits now includes full support for ZUGFeRD versions 2.1 and above, enabling seamless handling and processing of ZUGFeRD-compliant electronic invoices. The integration ensures:

* **Compatibility**: DocBits is capable of managing ZUGFeRD invoices in both their structured (XML) and unstructured (PDF) formats, maintaining compliance with EU standards such as EN 16931 for e-invoicing.
* **Efficiency**: Users can effortlessly import, validate, and extract data from ZUGFeRD e-invoices, minimizing manual data entry and reducing processing time.
* **Flexibility**: Whether you're working with basic, comfort, or extended profiles within the ZUGFeRD standard, DocBits provides tools to manage each level of invoice complexity.
* **Future-Proofing**: With support for newer versions, DocBits ensures that businesses remain compliant with evolving e-invoicing regulations across EU member states and beyond.

By incorporating ZUGFeRD 2.1 and newer standards, DocBits simplifies cross-border transactions and aligns with modern business needs, making it an essential tool for organizations prioritizing digital transformation and regulatory compliance. [Learn more](https://docs.docbits.com/administration-and-setup/settings/global-settings/document-types/edi/zugferd-1.0-2.1-and-2.3)

### External API Integration for Enhanced Document Processing

DocBits introduces an advanced capability to leverage external APIs during document processing, enhancing the completeness and accuracy of extracted data. This feature significantly reduces manual input by populating missing fields with accurate, up-to-date information retrieved in real time from trusted sources. It ensures that documents are processed faster and with greater consistency.

### Cross Sub-Organizations Access

For organizations with multiple sub-organizations enabled, DocBits now introduces the Cross Sub-Organizations feature. This enhancement empowers administrative users to streamline their document management across all sub-organizations under a single umbrella. Admin users can now access and view all documents from every sub-organisation without needing to switch sub-organization. This centralized visibility enables admins to see all the documents for all the sub-organisations, making it easy to locate specific files while still maintaining a bird’s-eye view. [Learn more](https://docs.docbits.com/administration-and-setup/settings/global-settings/groups-users-and-permissions/sub-organizations#cross-sub-organisations-access)

<figure><img src="../../.gitbook/assets/CrossSubOrganisations.png" alt=""><figcaption></figcaption></figure>

### Document Visibility Based on Group Permissions

DocBits introduces enhanced document visibility controls, enabling more precise access management for non-admin users through group-based permissions. This feature allows administrators to define which documents are visible to specific users or groups, ensuring streamlined workflows and improved data security. Admin users can assign documents to specific groups, granting visibility only to users within those groups. This ensures that users see only the documents relevant to their role or team, reducing clutter and enhancing focus. [Learn more](https://docs.docbits.com/administration-and-setup/settings/global-settings/groups-users-and-permissions/groups-and-permissions)

<figure><img src="../../.gitbook/assets/Group Based Permission.png" alt=""><figcaption></figcaption></figure>

### Sequential Workflow and Approval History

DocBits introduces a powerful Sequential Workflow and Approval History feature, designed to enhance document processing efficiency and accountability. By enabling documents to follow a predefined decision tree, this feature ensures orderly review and approval while maintaining a complete record of actions taken. Sequential Workflow Management:

* Documents can be assigned to multiple users in a predefined sequence, ensuring that each stage of review or validation occurs in the correct order.
* Each user in the workflow is notified when it's their turn to act on the document, reducing confusion and delays.
* Workflows can be customized to match specific business processes

**Approval History:**

* A complete log of all actions taken on the document is available in the Validation and Approval views. This includes:
  * User actions (e.g., "approved" "rejected")
  * Timestamps for each action
  * Comments or notes added by users during review
* The history ensures transparency and provides an audit trail for compliance and troubleshooting. [Learn more](https://docs.docbits.com/administration-and-setup/settings/global-settings/document-types/more-settings/approval-history)

<figure><img src="../../.gitbook/assets/Approval History.png" alt=""><figcaption></figcaption></figure>

### SFTP/FTP Documents Archive Enhancement

The SFTP/FTP Documents Archive enhancement in DocBits builds on the existing import functionality, introducing a seamless method for archiving files after they’ve been processed. A new setting in the FTP import configuration allows users to enable or disable file archiving. Once files are successfully ingested and processed in DocBits, they will be automatically archived to a designated folder on the SFTP/FTP server if the option is enabled. This ensures processed files are preserved for record-keeping without cluttering the active import directories. [Learn more](https://docs.docbits.com/end-user-and-partner-section/end-user-section/how-to-import-documents/ftp)

<figure><img src="../../.gitbook/assets/SFTPArchieve.png" alt=""><figcaption></figcaption></figure>

### Multiple Tax Section for Tax Type and Export to LN

This feature enhances tax handling capabilities by enabling detailed classification and export of tax information to Infor LN (Full Tax, Reduced Tax, Tax Free). This allows for better alignment with complex tax structures and ensures seamless integration with accounting systems.

**Multiple Tax Sections per Type**:

* DocBits now supports the addition of multiple tax sections under each tax type, such as:
  * Full Tax: Standard VAT or sales tax rates.
  * Reduced Tax: Lower rates for specific goods or services (e.g., essential items).
  * Tax-Free: Exemptions for eligible transactions.
* These sections allow precise categorization of tax amounts, ensuring compliance with tax regulations and accounting standards.

**Dynamic Auto Accounting Integration**:

* Based on the data extracted during document processing, the relevant tax sections are automatically displayed on the Auto Accounting Screen.
* This ensures that users can validate and adjust tax entries quickly without manual calculation or re-entry, streamlining the workflow.

**Export to Infor LN**:

* The tax data, including all relevant sections and classifications, is seamlessly exported to Infor LN, ensuring consistency between document processing in - DocBits and the enterprise resource planning (ERP) system.
* Exported data is linked to the respective cost lines in Infor LN, maintaining clear traceability and accurate financial reporting.

<figure><img src="../../.gitbook/assets/MultipleTaxLInes.png" alt=""><figcaption></figcaption></figure>

<figure><img src="../../.gitbook/assets/MultipleTaxLineAuto Accounting.png" alt=""><figcaption></figcaption></figure>

### Dashboard Enhancements

DocBits has introduced significant updates to the dashboard, focusing on usability, efficiency, and improved data visibility. These enhancements include a new "Assigned To Group" filter and an optimized UI for Document Logs, making it easier for users to interact with and manage their documents.

### PO Matching Enhancements

DocBits introduces several usability improvements to the PO Matching Screen, designed to streamline the process of matching purchase order (PO) lines with invoices. These enhancements offer more intuitive controls for multi-line selection and provide clear visual indicators for handling outdated PO data.

**Ctrl + Click for Individual Line Selection**:

* Users can now hold the Ctrl key and click on specific lines to select multiple, non-contiguous rows on the PO matching screen.

**Shift + Click for Range Selection**:

* Users can select a range of rows by holding the Shift key, clicking on the first row, and then clicking on the last row. All rows in between the first and last selection will be automatically selected.

**Automatic Outdated Data Detection**:

* If the PO data associated with an invoice is old (based on system settings), an icon will be displayed to notify the user. This visual indicator ensures that users are aware of stale data that may not reflect the latest updates in the purchase order.

### Bug Fixes

* Resolved an issue to ensure all possible values are displayed correctly during auto-accounting processes
* Improved the user interface of Workflow Logs to make navigation and usability more intuitive
* Updated the document fields to display additional information, such as required and hidden flags, directly in the user interface
* Added visibility of group descriptions in the group settings
* Displayed length restrictions for group names during creation to prevent errors
* Addressed issues in the decision tree testing functionality and resolved translation inconsistencies
* Improved the search functionality in Workflow Logs for more accurate and effective search results
* Fixed an issue to prevent users from inadvertently deleting e-document drafts
* Resolved bugs in the email import process to ensure seamless integration and data handling
* Fixed issues with saving AI-generated tags, ensuring consistent data retention
* Corrected a sorting issue that occurred when applying sorting across different pages of the dashboard
* Enhanced the document counter to accurately display the number of documents processed by DocBits
* Improved translations throughout the application to enhance usability for different languages

## Release Hot Fix Feast 17th December 2024

### **DocBits Enhancements:**

#### Email Import Enhancements

* Users can now seamlessly import XML and EDI files through the Email Import feature.

## Release Hot Fix Feast 27th November 2024

### DocBits Enhancements:

#### Enhanced PO Optimisation

* **Optimised Saving Mechanism**: The saving process has been streamlined to occur only after the user completes the matching, reducing redundant saves and improving efficiency.
* **Enhanced Asynchronous Export**: Export functionality now runs asynchronously, ensuring smoother operations and an improved overall user experience.

#### Workflow Enhancements

The workflow functionality has been upgraded to provide a better user experience:

* **Improved Logs**: Workflow logs now feature a cleaner, more intuitive interface, making it easier to review and understand process details.
* **Enhanced Responsiveness**: Workflow execution processes are optimized for faster and more reliable performance, enabling quicker task completion and reduced delays.

#### Improved Application Caching

We’ve implemented advanced caching strategies across the application to optimize data retrieval and reduce load times. These improvements enhance overall usability by ensuring smoother navigation and a more responsive user experience, particularly for frequently accessed features.

#### Dashboard and UI Upgrades

* **Dashboard Enhancements**: The dashboard has been revamped with an improved layout and additional features to simplify navigation and enhance visibility of key metrics.
* **UI Improvements**: The user interface across the application has been refined for a more modern, intuitive, and user-friendly experience, making it easier for users to accomplish their tasks with minimal effort.

### Bug Fixes:

1. Enhanced the fuzzy logic to ensure more accurate and reliable data population following extraction.
2. Fixed known bugs affecting groups and permissions, ensuring seamless access management and role functionality.
3. Addressed inconsistencies in translations across the application, improving clarity and localization.
4. Resolved layout-related issues, ensuring a consistent and optimized user interface across all configurations.
5. Corrected errors in master data lookup functionality, ensuring accurate and reliable data retrieval.
6. Resolved issues with email import functionality across all available options, ensuring smooth and error-free operations.

## Release Feast 4th November 2024

### New Features:

#### Email Import Enhancements

Configured IMAP email settings to automatically send notifications for import results. Successful import notifications will confirm the files processed, while failure alerts will include the filenames and specific error details for prompt troubleshooting.

<figure><img src="../../.gitbook/assets/EmailImport.png" alt=""><figcaption><p>Email Import Configurations</p></figcaption></figure>

#### Master Data Lookup Revamping

Revamped the master data lookup settings with refined categorization, enabling faster and more precise retrieval of diverse master data types. This improvement streamlines data access by organizing master data into distinct categories, significantly boosting search efficiency and accuracy. Users can now locate the relevant data more quickly, enhancing productivity and decision-making across the application

<figure><img src="../../.gitbook/assets/MasterDataLookup.png" alt=""><figcaption><p>Master Data</p></figcaption></figure>

#### Performance Improvements

Implemented a robust caching mechanism to significantly boost application performance, especially under high request loads. This improvement reduces server processing time by temporarily storing frequently accessed data, enabling faster response times and a smoother user experience. The new caching system efficiently manages increased traffic, ensuring reliable and scalable performance even during peak usage periods

#### Document Lock Feature Enhancement

Upgraded the document locking functionality to prevent simultaneous edits, ensuring data integrity and minimising conflicts. Now, documents are automatically locked during active editing, providing users with clear indicators when a document is in use and preventing others from making changes until the edit session is complete. This enhancement streamlines collaborative workflows and reduces the risk of data overwrites.

#### Navigation and User Experience Improvements

* **Breadcrumb Navigation**: Added breadcrumb trails across application pages to enhance navigation, allowing users to easily track and return to previous sections for a more intuitive browsing experience.
* **Streamlined User Interface**: Removed the "new version" pop-up notification to create a smoother, uninterrupted workflow, reducing distractions and improving overall usability.

### Bug Fixes:

* Resolved user-specific problems, such as attachment failures from encrypted or signed emails.
* Fixed card display and flow problems.
* Corrected routing issues with Next/Previous buttons.
* Addressed bugs related to decision tree tables.
* Updated UI for the password field to improve usability.
* Fixed issues with the task counter not displaying correctly.
* Corrected a user interface problem with the AI table.
* Resolved errors with document extraction during table training.
* Added a warning when a PO is matched during reformatting, and ensured matched rows are removed.
* Fixed date formatting, ensuring data loads correctly by day and week filters, and ensured document types are properly displayed.
* Corrected the display of documents on dual monitors.
* Fixed a problem where unlinking one PO line would remove all lines.
* Resolved incorrect translations across the application.
* Fixed the issue where lengthy descriptions in rule management caused scrolling on the list.
* FeastRestored missing "Assign-To" functionality for non-admin users.

## Release Harvest 9th September 2024

#### New Features

### Duplicate Invoice handling

This feature allows users to identify if documents are duplicated across their system. This feature works by analyzing document fields that can be configured by the user. By selecting specific fields, users can customize the detection criteria to suit their needs, ensuring that only relevant duplicates are flagged. This helps to maintain data integrity and reduces the clutter of redundant documents, streamlining document management processes.

{% embed url="https://youtu.be/8CdBu7HN47I" %}

### Decision Tree

The decision tree is a tool used to automate decision-making in a workflow by mapping out choices and their outcomes. By integrating decision trees, you can ensure consistent decisions based on specific criteria, streamline processes, and reduce errors. This approach enhances efficiency by automating complex decision points within the workflow.

{% embed url="https://youtu.be/E7cx8BDGTI0" %}

### Choosing AI Models

DocBits now allows users to switch between different AI models to better suit their needs. You can choose the AI model that best fits your specific use case, whether it's for document analysis, data extraction, or text classification. This flexibility enables you to optimize performance and achieve more accurate results, tailoring the AI's capabilities to your organization's unique requirements.

{% embed url="https://youtu.be/YvgEVagPepY" %}

### Choosing OCR Version

DocBits now offers the ability to change the OCR (Optical Character Recognition) version used within the platform. Users can select different OCR versions based on their specific needs, ensuring better accuracy and compatibility with various document types. This feature allows for more precise text extraction from images and scanned documents, improving overall data quality and workflow efficiency.

{% embed url="https://youtu.be/zkW8zj0H5Ko" %}

## Release Sunset 12th August 2024

### New Features:

## Rule Manager

[rule-manager](../../administration-and-setup/settings/document-processing/rule-manager/ "mention") provides the flexibility to create and edit conflict resolution rules tialored for DocBits invoicing system. These rules are designed to automatically handle discrepancies between invoice details and purchase order (PO) data, ensuring accurate financial reconciliation. The system applies these rules to process invoice lines, charges, and taxes, and generates appropriate adjustments or notes when necessary.

<figure><img src="../../.gitbook/assets/RuleManager.png" alt=""><figcaption><p>Rule Manager</p></figcaption></figure>

### Syncing Data Using Stream

BOD syncing from Infor utilizes AWS Stream for real-time data processing, enhancing efficiency and significantly reducing data syncing time.

### XRechnung

DocBits now processes XRechnung (electronic invoices) seamlessly by first creating a user-friendly PDF, streamlining and simplifying the invoice processing workflow.

<figure><img src="../../.gitbook/assets/XRECHNUNG.png" alt=""><figcaption></figcaption></figure>

### Bug Fixes:

1. PO Match Button Visibility\
   Issue: PO Match button is available when there is no table or the table is deleted.\
   Status: On field validation, PO Match will be hidden if there is no table or the table is deleted
2. Table Drag & Drop Sorting\
   Issue: Table Drag & drop for sorting on all Lists/Dashboards\
   Resolution: User can now drag and drop to sort the table
3. Validation Screen Toolbar\
   Issue: Validation screen: toolbar right side not scrollable\
   Resolution: Fixed
4. Horizontal Scroll\
   Issue: Horizontal Scroll on Approval Screen\
   Resolution: Fixed
5. Approval Screen Decision Clearing\
   Issue: Ability to clear the approve/reject decision on approval screen\
   Resolution: Fixed
6. Task Display on Approval Screen\
   Issue: Task shown on the Approval Screen\
   Resolution: Toolbar is available which shows the tasks count of open/in progress
7. PO Match Table Size\
   Issue: PO Match table gets smaller after matching a line\
   Resolution: Fixed
8. Task Assignment based on Item Procurement Group\
   Issue: Translation for procurement group assignment\
   Resolution: Fixed
9. Supplier Name and Id in Task Creation\
   Issue: Adding Supplier Name and Id in Task creation\
   Resolution: Supplier Name and Id will be picked from the document
10. Document Subtype Copy\
    Issue: Click on Copy Document Subtype from sub document type setting was not working\
    Resolution: Fixed
11. New Label Field\
    Issue: New Label field in list of values to add label along with value and synonym\
    Resolution: Fixed
12. Country Origin Card in Workflow\
    Issue: New Card in workflow that checks country origin of a supplier and create a task or continue porcessing docuemtn accordingly\
    Resolution: Fixed
13. Dark Mode Fix on settings searchbar\
    Issue: This issue was previously identified\
    Resolution: Fixed
14. Extracted Table Column Visibility Indicator\
    Issue: Indicator if Columns are hidden in extracted table on Field validation\
    Resolution: Fixed
15. Dashboard Assignment for Admins\
    Issue: Make Assign to on the dashboard only for admins\
    Resolution: Fixed
16. Document Split Visibility\
    Issue: Show Document split only when more pages\
    Resolution: Fixed
17. Invoice Dashboard Columns\
    Issue: Additional columns on invoice dashboard\
    Resolution: Fixed
18. Field Validation Script Deactivation\
    Issue: Field Validation- Deactivate script was not working correctly\
    Resolution: Fixed
19. Approval Layout Button Customization\
    Issue: Cannot change the button type and style on approval layout builder\
    Resolution: Fixed
20. Data Sync Table\
    Issue: Data Sync Table in settings\
    Resolution: Fixed
21. Dashboard Analytics Total Display\
    Issue: Dashboard Analytics- display wrong total number\
    Resolution: Fixed

## Release Firework Juli 8th, 2024

### New Features

**Line Charges Export to M3**

• Export line charges to M3 with appropriate costing elements as per your business needs.

**PO & Invoice Discrepancy Handling**

• Smart handling of discrepancies in quantity, prices, charges, and tax.

### Key Bug Resolutions

#### 1. PO Search Functionality

• Issue: PO search was not working.

• Status: This issue has been identified and will not be addressed in this release.

#### 2. PO Matching Connection

• Issue: PO matching connection was not removing as expected.

• Resolution: Fixed to ensure seamless PO matching operations.

#### 3. Exported Document Alerts

• Issue: Exported documents had alerts for costing elements even when the system was not set up for it.

• Resolution: Corrected to prevent unnecessary alerts, ensuring accurate document exports.

#### 4. Advance Shipment EDI View

• Issue: Advance shipment EDI view showed IDs in the title.

• Resolution: Titles now display correctly, improving data readability.

#### 5. Calculation Errors in Split by Total Issue

• Issue: Calculation errors occurred when lines were split further.

• Resolution: Fixed to ensure accurate calculations in all scenarios.

#### 6. PO Screen Table Display

• Issue: No table was showing on the PO screen.

• Resolution: Display issue resolved to ensure tables appear correctly.

#### 7. Auto Export on Order Confirmation

• Issue: Auto export was not working.

• Resolution: Functionality restored to ensure automatic exports operate smoothly.

#### 8. Mismatch Issue on PO

• Issue: Mismatch issue on PO showed despite everything being identical on the Delivery Note.

• Resolution: Resolved to ensure accurate mismatch detection.

#### 9. Report Download Issues

• Issue: Reports were not downloading.

• Resolution: Fixed to enable seamless report downloads.

#### 10. Incorrect Total and Net Amounts

• Issue: Total and Net amounts were showing incorrect values.

• Resolution: Values corrected to ensure financial accuracy.

#### 11. Invoice Date Format on Dashboard

• Issue: Invoice Date column had wrong format values.

• Resolution: Dates now display in the correct format, enhancing usability.

#### 12. Workflow Delays at “Ready for Validation”

• Issue: Workflow delays occurred at “Ready for Validation” until feedback from Doc2flow.

• Resolution: Workflow timing improved for faster validation processes.

## Next Release Firework Juli 8th, 2024

### Problem:

The existing system lacks automated rules for accurately matching and processing invoice charges against purchase orders (POs). This manual process can lead to discrepancies, as illustrated in the screenshots, where invoice charges and POs need reconciliation for correct invoicing.

<div><figure><img src="../../.gitbook/assets/Bildschirmfoto 2024-06-07 um 17.11.37.png" alt=""><figcaption></figcaption></figure> <figure><img src="../../.gitbook/assets/Bildschirmfoto 2024-06-07 um 17.11.46.png" alt=""><figcaption><p>Rule Manager DocBits</p></figcaption></figure></div>

### Solution:

With the new Rule Manager in DocBits, launching in July, you can automate this process:

#### 1. Create Rules:

Define criteria (e.g., Quantity > PO Quantity) for invoice line items.

#### 2. Set Actions:

Map fields and actions to export data seamlessly to Infor.

#### 3. Test Rules:

Validate rules with sample data to ensure accuracy.

## Junebug Release Notes - June 10th, 2024

This update brings exciting new features and bug fixes to Junebug:

**New Features:**

* **Automated Charge Extraction:** Junebug now automatically extracts and maps charges within your Docbit documents. This eliminates manual data entry and streamlines your workflow.
* **Portal Export to Infor IDM:** The new Portal allows you to effortlessly export supplier documents directly to Infor IDM. This simplifies shipment processing and reduces manual intervention.
* **Origin Identification (AI):** Junebug introduces a powerful AI feature that automatically learns the origin of documents. This saves you time and effort in document classification.
*

```
<div><figure><img src="../../.gitbook/assets/POShipmentTable.png" alt=""><figcaption></figcaption></figure> <figure><img src="../../.gitbook/assets/ApprovalScreen2.png" alt=""><figcaption></figcaption></figure> <figure><img src="../../.gitbook/assets/ApprovalScreen1.png" alt=""><figcaption></figcaption></figure></div>
```

**Bug Fixes:**

* **QR Code Fix:** An issue that previously caused problems with QR code processing has been resolved.
* **Non-EDI Document Handling:** Junebug now handles non-EDI documents more effectively.

<figure><img src="../../.gitbook/assets/EDI810-Invoice.png" alt=""><figcaption></figcaption></figure>

Hotfix - 5 Juni [**Priority System**](../../end-user-and-partner-section/end-user-section/our-document-priority-system.md)

## Next Release - Junebug Release 10th June 2024

Sandbox Freeze - 3th June 2024

<figure><img src="../../.gitbook/assets/Bildschirmfoto 2024-05-08 um 20.37.35.png" alt=""><figcaption></figcaption></figure>

In the upcoming release, a significant enhancement to the classification and extraction capabilities will be introduced, specifically aimed at table lines within documents. This new feature allows users to define whether a line in a table represents a charge. This functionality is particularly useful in detailed financial documents, such as invoices, where distinguishing between different types of transactions—such as charges, taxes, or fees—is crucial for accurate processing and record-keeping.

**Key Points for Release Notes:**

* **Enhanced Table Line Classification**: Users can now specify if a particular line in a document table is a charge, improving the accuracy and granularity of data extraction.

## Maypole Release 5.55.8.10 - ( 17th May )

### Release Notes - Web App

#### New Features:

▪ Workflow Card Translation: Enhancements in the workflow, including card translation for better localization support.

▪ Email Import Logging: Added detailed logging for email imports to enhance troubleshooting and monitoring.

▪ Broken Fuzzy Screen Fix: Resolved an issue with broken fuzzy screen display across various interfaces.

▪ Accounting Updates: Enhanced the accounting process by removing outdated accounting methods and integrating charges more efficiently.

#### Improvements:

▪ Ruiz Workflow Enhancements: Fixed bugs related to workflow navigation, particularly involving hidden steps.

▪ User Interface Adjustments: Improved user interface elements such as cash discount terms under payment terms for better clarity and user experience.

▪ Performance Enhancements: Various backend improvements to enhance system performance and stability.

#### Bug Fixes:

▪ Approval Stamp Issue: Fixed critical issues surrounding the approval stamp process to ensure compliance and correct functionality.

▪ Key Addition: Added necessary keys back to the system to ensure data integrity and system functionality.

▪ Master Data Field Adjustment: Addressed an issue in the master data field to align with user requirements.

#### Technical:

▪ Version Updates: Routine updates to various system components to align with current standards and technologies.

▪ Merge Activities: Numerous merges to integrate features, fixes, and enhancements from multiple development branches into the main branch.

### What's New - API

▪ Cache Management Enhancements: Updated the get\_receive\_delivery\_cache to improve performance and reliability.

▪ New Features for Sales Orders: Introduced a preview feature for sales orders, enhancing the visualization and management of order data.

▪ Document Handling Improvements: Added automated test jobs for demotesting and sandbox environments to ensure robustness.

▪ Enhanced Cache Functionality: Added field\_id to further enhance the caching mechanisms.

#### Fixes and Improvements

▪ Office Email Import Adjustments: Made necessary adjustments to the Office Email Import feature to enhance functionality.

▪ Development Enhancements: Multiple merges from dev to main branches ensuring synchronization and stability across environments.

#### Miscellaneous

▪ Configuration Updates: Various updates to the configuration files improving the system setup and parameters.

### Release Notes - Workflow

#### Enhancements:

▪ Implemented a new workflow test that can now be enabled during import, allowing for more flexible testing scenarios.

▪ Enhanced the logging functionality for action cards, making debugging and monitoring more efficient.

▪ Improved compatibility for field comparison cards with date and enum types, ensuring smoother comparisons and validations.

▪ Updated the tax card and modified the return processes for action cards to streamline operations.

#### Fixes:

▪ Addressed issues with the document status updates, ensuring they are accurately reflected in the system.

▪ Fixed the calculation for the comparison card involving unit price and quantity to correctly handle discrepancies.

▪ Resolved multiple minor bugs and made stability improvements.

#### Operational Changes:

▪ Merged multiple development stages into the sandbox and stage branches, reflecting a significant integration of new features and fixes.
