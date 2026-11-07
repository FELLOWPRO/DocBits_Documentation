# Infrastructure

The **Infrastructure** page gives administrators a live view of where every part of the platform runs (EU or US) and whether processing is healthy. It is read-only, so nothing here is configured.

> **Access:** Infrastructure is an admin-only page. Open **Settings → Organization & Access → Infrastructure**.

The page has three tabs. Each one loads its data the first time you open it, so switching back and forth does not re-fetch everything.

| Tab | Answers |
|-----|---------|
| **Topology** | Where does each component run, and how does a document travel through DocBits? |
| **Processing** | Are the document-processing steps running, and is work backing up? |
| **Scheduled Tasks** | Are the recurring background jobs firing on schedule? |

## Topology

**Topology** opens by default. It shows the platform in two views: **Architecture** and **Process**. Use the toggle above the diagram to switch between them; the indicator beside it reads **live** while the view is streaming its state.

A banner above the diagram summarizes the region check:

* **Green**: all components run in your organization's region, and the banner names that region (for example **EU**).
* **Red**: a component that is marked as critical runs outside your organization's region.
* **Amber**: the advisory notice names components that sit in another region even though the overall check passes. That is a region difference, not a failure.

### Architecture view

The architecture view draws the platform as lanes of component cards, for example Edge / Web, Core API, Import, Background Services and Modules. Arrows show the connections between the cards.

Each card shows the component name, a region badge and, for critical components, a health dot that turns green when the component answers and shows its latency in milliseconds when a value is reported.

| Badge | Meaning |
|-------|---------|
| **EU ✓** / **US ✓** | The component runs in your organization's region. |
| **SHARED** | A global component such as the CDN that has no single region. This is expected. |
| **EU ⓘ** / **US ⓘ** | The component runs in another region and is reported as an advisory. |
| **EU ⚠** / **US ⚠** | The component runs in another region and is reported as an error. Raise it with support. |
| Grey badge, no mark | The region of this component is not known. |

### Process view

The process view animates a single document through the pipeline: the **Email**, **FTP** and **Web** entry sources converge on **API**, then pass **OCR**, **Extraction**, **PO matching**, **Auto Accounting** and **Export**. Every stage connects down to a datastore bar with **Postgres** and file storage. A caption names the step currently being animated, and the play button pauses or resumes the animation.

PO matching and Auto Accounting are optional. When one of them is switched off for your organization, its stage is greyed out and the animation skips it.

### Optional modules

Optional modules (Full-Text Search, DocFlow, Auto-Accounting, DocNet and PO Matching) carry an **active** or **inactive** badge on their card. A deactivated module offers an **Activate** button that takes you to the page where you switch it on: the Modules settings for most modules, or **Document Types** for PO Matching, which is enabled per document type.

## Processing

The **Processing** tab lists the document-processing steps for your organization and tells you whether work is flowing or backing up.

| Column | Description |
|--------|-------------|
| **Process** | The processing step: Document Processing, OCR, TR-OCR, Barcode Split, Barcode Extraction, Extraction and PO Match. |
| **Last run** | How long ago the step last ran. Hover for the exact timestamp. **Never run** means no document has reached this step yet. |
| **Status** | One or more badges (see below). |

The status badges are independent signals:

* Red **Errors (N)**: `N` documents recently failed at this step.
* Amber badge with a count: `N` documents are being processed by this step right now.
* Green **OK**: no recent errors and nothing waiting.

Because errors and work in progress are counted separately, a step can show both at once, so a failure stays visible while other documents are still running.

## Scheduled Tasks

The **Scheduled Tasks** tab lists the recurring background jobs that keep DocBits running, for example cache refreshes, status alerts, document timeouts and outbound syncs. Each row shows whether the job fires on time.

| Column | Description |
|--------|-------------|
| **Task** | The name of the scheduled job, with separators replaced by spaces. |
| **Last run** | How long ago it last ran. Hover for the exact timestamp. **Never run** means it has not fired yet. |
| **Status** | Schedule health (see below). |

| Status | Meaning |
|--------|---------|
| **On schedule** (green) | The task runs at its expected interval. |
| **Delayed** (red) | The task has not run when expected. Investigate or raise it with support. |
| **Unknown** (grey) | The schedule status could not be determined. |

Both tables have a **Refresh** button that reloads the current numbers on demand.
