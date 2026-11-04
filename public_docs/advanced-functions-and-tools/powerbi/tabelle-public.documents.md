# Tabelle public.documents

## Spalten

* `id`: internal
* `org_id`: ID to organisation
* `batch_id`: internal
* `doc_path`: internal
* `doc_type`: DOC Type
* `status`: internal
* `message`: text
* `export_attempts`: integer
* `last_attempted_on`: timestamp with time zone
* `next_attempt_on`: timestamp with time zone
* `assigned_to`: integer
* `created_by`: integer
* `created_on`: timestamp with time zone
* `last_modified_on`: timestamp with time zone
* `is_deleted`: boolean
* `task_id`: internal
* `filename`: internal
* `assigned_on`: timestamp with time zone
* `pages`: integer
* `auto_processed`: boolean
* `exception_info`: text
* `doc_language`: Language
* `is_trimmed`: boolean
* `doc_origin`: Doc Origin
* `doc_locale`: Doc Locale
* `is_doc2landing_doc`: boolean
* `extraction_time`: double precision
* `export_time`: double precision
* `po_all_matched`: boolean
* `restart_allowed`: boolean
* `table_version`: internal
* `force_ocr`: boolean
* `locked_by`: integer
* `locked_on`: timestamp with time zone
* `lock_renewed_on`: timestamp with time zone
* `lock_key`: internal
* `last_saved_by`: integer
* `last_saved_on`: timestamp with time zone
* `document_version`: integer
* `lock_session_key`: internal
* `sub_org_id`: internal
* `doc_source`: internal
* `sub_doc_type`: internal
* `assigned_to_group`: internal
* `status_changed_on`: timestamp with time zone
* `improve_quality`: boolean
* `priority`: integer
* `metadata_field`: json
* `doc_classification_label`: internal
* `doc_start_page`: integer
* `doc_classification_class`: internal
* `celery_task_token`: internal
* `celery_task_attempt`: integer
* `celery_task_priority`: integer
* `has_zugferd`: boolean
* `has_peppol`: boolean
* `timestamp_for_validation`: timestamp with time zone
* `exception_details`: text
* `has_annotated_version`: boolean
* `po_match_status`: internal
* `tr_ocr_extracted_data`: text
* `pending_workflow_execution`: boolean
* `extracted_document_id`: internal
* `extracted_supplier_id`: internal
* `classification_manually_corrected`: boolean
* `supplier_as_org_id`: internal
* `extracted_data_basic`: jsonb
* `celery_task_queue`: internal
* `extracted_data`: jsonb
* `extracted_data_jsonb`: jsonb
* `warnings`: jsonb

## Analyse & Beschreibung

```markdown
# Technical Documentation for `public.documents` Table

## Introduction

The `public.documents` table is designed to store and manage metadata and processing information related to document handling within an organization. This includes tracking document status, processing attempts, language, and other administrative details. The table is structured to support document classification, processing workflow, and user assignments, making it integral to the document management system.

## Column Descriptions

### id
- **Meaning**: Unique identifier for each document.
- **Role**: Primary key.
- **Typical Contents**: A UUID string representing the document.

### org_id
- **Meaning**: Identifier for the organization associated with the document.
- **Role**: Foreign key.
- **Typical Contents**: A UUID string representing the organization.

### batch_id
- **Meaning**: Identifier for the batch in which the document was processed.
- **Role**: Foreign key.
- **Typical Contents**: A UUID string representing the batch.

### doc_path
- **Meaning**: File path where the document is stored.
- **Role**: Technical field.
- **Typical Contents**: Path to the document file, e.g., `documents/{id}/{id}.pdf`.

### doc_type
- **Meaning**: Type of document being stored (e.g., invoice).
- **Role**: Document classification.
- **Typical Contents**: A string such as `INVOICE`.

### status
- **Meaning**: Current processing status of the document.
- **Role**: Workflow indicator.
- **Typical Contents**: A string indicating status, e.g., `ready_for_validation`.

### message
- **Meaning**: Information about the document's processing state or errors.
- **Role**: Descriptive field.
- **Typical Contents**: Text describing errors or messages related to document processing.

### export_attempts
- **Meaning**: Number of times an export attempt has been made for the document.
- **Role**: Processing tracking.
- **Typical Contents**: Integer count of export attempts.

### last_attempted_on
- **Meaning**: Timestamp of the last attempt to process or export the document.
- **Role**: Timestamp field.
- **Typical Contents**: Date and time with time zone.

### next_attempt_on
- **Meaning**: Scheduled timestamp for the next attempt to process or export the document.
- **Role**: Scheduling field.
- **Typical Contents**: Date and time with time zone.

### assigned_to
- **Meaning**: Identifier for the user assigned to this document.
- **Role**: Foreign key.
- **Typical Contents**: Integer representing the user ID.

### created_by
- **Meaning**: Identifier for the user who created or uploaded the document.
- **Role**: Foreign key.
- **Typical Contents**: Integer representing the user ID.

### created_on
- **Meaning**: Timestamp of when the document was created or uploaded.
- **Role**: Timestamp field.
- **Typical Contents**: Date and time with time zone.

### last_modified_on
- **Meaning**: Timestamp of the last modification made to the document record.
- **Role**: Timestamp field.
- **Typical Contents**: Date and time with time zone.

### is_deleted
- **Meaning**: Indicates whether the document is marked as deleted.
- **Role**: Logical deletion flag.
- **Typical Contents**: Boolean value (True or False).

### task_id
- **Meaning**: Identifier for the task associated with document processing.
- **Role**: Foreign key.
- **Typical Contents**: A UUID string representing the task.

### filename
- **Meaning**: Original filename of the document.
- **Role**: Descriptive field.
- **Typical Contents**: Name of the file, e.g., `document.pdf`.

### assigned_on
- **Meaning**: Timestamp when the document was assigned to a user.
- **Role**: Timestamp field.
- **Typical Contents**: Date and time with time zone.

### pages
- **Meaning**: Number of pages in the document.
- **Role**: Descriptive field.
- **Typical Contents**: Integer indicating the page count.

### auto_processed
- **Meaning**: Indicates if the document was automatically processed.
- **Role**: Processing status flag.
- **Typical Contents**: Boolean value (True or False).

### exception_info
- **Meaning**: Information on any exceptions encountered during processing.
- **Role**: Descriptive field.
- **Typical Contents**: Text describing processing exceptions.

### doc_language
- **Meaning**: Language of the document content.
- **Role**: Language classification.
- **Typical Contents**: ISO language code, e.g., `en`, `de`.

### is_trimmed
- **Meaning**: Indicates if the document has been trimmed or cropped.
- **Role**: Document modification flag.
- **Typical Contents**: Boolean value (True or False).

### doc_origin
- **Meaning**: Origin of the document, possibly indicating the country or source system.
- **Role**: Descriptive field.
- **Typical Contents**: Country code or origin identifier, e.g., `DE`.

### doc_locale
- **Meaning**: Locale settings of the document, indicating language and region.
- **Role**: Locale classification.
- **Typical Contents**: Locale string, e.g., `de_DE.ISO8859-1`.

### is_doc2landing_doc
- **Meaning**: Indicates if the document is related to a specific processing workflow (Doc2Landing).
- **Role**: Workflow flag.
- **Typical Contents**: Boolean value (True or False).

### extraction_time
- **Meaning**: Time taken to extract data from the document.
- **Role**: Performance metric.
- **Typical Contents**: Double precision value representing extraction time.

### export_time
- **Meaning**: Time taken to export the document.
- **Role**: Performance metric.
- **Typical Contents**: Double precision value representing export time.

### po_all_matched
- **Meaning**: Indicates if all purchase orders related to the document have been matched.
- **Role**: Matching status flag.
- **Typical Contents**: Boolean value (True or False).

### restart_allowed
- **Meaning**: Indicates if the document processing can be restarted.
- **Role**: Workflow control flag.
- **Typical Contents**: Boolean value (True or False).

### table_version
- **Meaning**: Version of the table structure used for the document.
- **Role**: Version control.
- **Typical Contents**: String indicating version, e.g., `v3`.

### force_ocr
- **Meaning**: Indicates if OCR processing is forced for the document.
- **Role**: Processing control flag.
- **Typical Contents**: Boolean value (True or False).

### locked_by
- **Meaning**: Identifier for the user who has locked the document for editing.
- **Role**: Foreign key.
- **Typical Contents**: Integer representing the user ID.

### locked_on
- **Meaning**: Timestamp when the document was locked for editing.
- **Role**: Timestamp field.
- **Typical Contents**: Date and time with time zone.

### lock_renewed_on
- **Meaning**: Timestamp when the document lock was last renewed.
- **Role**: Timestamp field.
- **Typical Contents**: Date and time with time zone.

### lock_key
- **Meaning**: Key associated with the document lock.
- **Role**: Lock control.
- **Typical Contents**: String representing the lock key.

### last_saved_by
- **Meaning**: Identifier for the user who last saved the document.
- **Role**: Foreign key.
- **Typical Contents**: Integer representing the user ID.

### last_saved_on
- **Meaning**: Timestamp when the document was last saved.
- **Role**: Timestamp field.
- **Typical Contents**: Date and time with time zone.

### document_version
- **Meaning**: Version number of the document.
- **Role**: Version tracking.
- **Typical Contents**: Integer representing the document version.

### lock_session_key
- **Meaning**: Session key associated with the document lock.
- **Role**: Lock control.
- **Typical Contents**: String representing the session key.

### sub_org_id
- **Meaning**: Identifier for a sub-organization associated with the document.
- **Role**: Foreign key.
- **Typical Contents**: A UUID string representing the sub-organization.

### doc_source
- **Meaning**: Source system or origin of the document.
- **Role**: Descriptive field.
- **Typical Contents**: String indicating the source, e.g., `doc2app`.

### sub_doc_type
- **Meaning**: Sub-type classification of the document.
- **Role**: Document classification.
- **Typical Contents**: String indicating the sub-type.

### assigned_to_group
- **Meaning**: Identifier for the group to which the document is assigned.
- **Role**: Assignment tracking.
- **Typical Contents**: A UUID string representing the group.

### status_changed_on
- **Meaning**: Timestamp when the document's status was last changed.
- **Role**: Timestamp field.
- **Typical Contents**: Date and time with time zone.

### improve_quality
- **Meaning**: Indicates if quality improvement processes are applied to the document.
- **Role**: Quality control flag.
- **Typical Contents**: Boolean value (True or False).

### priority
- **Meaning**: Processing priority of the document.
- **Role**: Workflow control.
- **Typical Contents**: Integer indicating priority level.

### metadata_field
- **Meaning**: JSON field containing metadata related to the document.
- **Role**: Metadata storage.
- **Typical Contents**: JSON structure with various metadata fields.

### doc_classification_label
- **Meaning**: Label indicating the classification of the document.
- **Role**: Classification label.
- **Typical Contents**: String indicating classification, e.g., `INVOICE`.

### doc_start_page
- **Meaning**: Page number where the document content starts.
- **Role**: Descriptive field.
- **Typical Contents**: Integer indicating the start page.

### doc_classification_class
- **Meaning**: Class indicating the detailed classification of the document.
- **Role**: Classification detail.
- **Typical Contents**: String indicating classification class.

### celery_task_token
- **Meaning**: Token for tracking Celery task associated with the document.
- **Role**: Task tracking.
- **Typical Contents**: String representing the task token.

### celery_task_attempt
- **Meaning**: Number of attempts made for the Celery task.
- **Role**: Task tracking.
- **Typical Contents**: Integer count of task attempts.

### celery_task_priority
- **Meaning**: Priority level of the Celery task.
- **Role**: Task control.
- **Typical Contents**: Integer indicating task priority.

### has_zugferd
- **Meaning**: Indicates if the document is in ZUGFeRD format.
- **Role**: Format indicator.
- **Typical Contents**: Boolean value (True or False).

### has_peppol
- **Meaning**: Indicates if the document is in PEPPOL format.
- **Role**: Format indicator.
- **Typical Contents**: Boolean value (True or False).

### timestamp_for_validation
- **Meaning**: Timestamp for when the document was validated.
- **Role**: Validation tracking.
- **Typical Contents**: Date and time with time zone.

### exception_details
- **Meaning**: Detailed information about exceptions during processing.
- **Role**: Descriptive field.
- **Typical Contents**: Text with exception details.

### has_annotated_version
- **Meaning**: Indicates if there is an annotated version of the document.
- **Role**: Version indicator.
- **Typical Contents**: Boolean value (True or False).

### po_match_status
- **Meaning**: Status of purchase order matching.
- **Role**: Matching status indicator.
- **Typical Contents**: String indicating match status.

### tr_ocr_extracted_data
- **Meaning**: OCR extracted data from the document.
- **Role**: Data storage.
- **Typical Contents**: Text containing extracted data.

### pending_workflow_execution
- **Meaning**: Indicates if there are pending workflow executions.
- **Role**: Workflow status flag.
- **Typical Contents**: Boolean value (True or False).

### extracted_document_id
- **Meaning**: Identifier for the extracted document.
- **Role**: Extraction tracking.
- **Typical Contents**: A UUID string representing the extracted document.

### extracted_supplier_id
- **Meaning**: Identifier for the extracted supplier.
- **Role**: Extraction tracking.
- **Typical Contents**: A UUID string representing the extracted supplier.

### classification_manually_corrected
- **Meaning**: Indicates if the document classification was manually corrected.
- **Role**: Classification status flag.
- **Typical Contents**: Boolean value (True or False).

### supplier_as_org_id
- **Meaning**: Identifier for the supplier treated as an organization.
- **Role**: Foreign key.
- **Typical Contents**: A UUID string representing the supplier organization.

### extracted_data_basic
- **Meaning**: Basic extracted data in JSONB format.
- **Role**: Data storage.
- **Typical Contents**: JSONB structure with extracted data fields.

### celery_task_queue
- **Meaning**: Name of the Celery task queue.
- **Role**: Task management.
- **Typical Contents**: String indicating the queue name.

### extracted_data
- **Meaning**: Extracted data from the document in JSONB format.
- **Role**: Data storage.
- **Typical Contents**: JSONB structure with extracted data fields.

### extracted_data_jsonb
- **Meaning**: JSONB field containing detailed extracted data.
- **Role**: Data storage.
- **Typical Contents**: JSONB structure with extracted data fields.

### warnings
- **Meaning**: Warnings related to document processing stored in JSONB format.
- **Role**: Warning storage.
- **Typical Contents**: JSONB structure with warning messages.
```
