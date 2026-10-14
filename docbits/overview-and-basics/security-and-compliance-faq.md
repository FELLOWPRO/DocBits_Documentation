# DocBits (FELLOWPRO AG) — Security & Compliance Questionnaire

**Vendor:** DocBits by FELLOWPRO AG | **Hosting:** Frankfurt, Germany | **ISO 27001 Certified** | **Date:** 2026-03-04

---

## Status Legend

| Symbol | Meaning |
|--------|---------|
| ✅ Confirmed | Answer verified from official DocBits documentation or public sources |
| ✅ Partial | Partially answered; additional detail needed from DocBits team |
| ❓ To Confirm | No public information available — must be confirmed directly with DocBits/FELLOWPRO |
| ⚠️ Needs Clarification | Public information raises concerns or ambiguity that requires explicit vendor clarification |

---

## 🔹 Data Location & Residency

### 1. Where exactly is the production environment hosted?

**Response:** Hosted on DigitalOcean cloud infrastructure in Frankfurt, Germany. Uses DigitalOcean Spaces for storage and OpenSearch for log indexing. DocBits is ISO 27001 certified. All connections secured via SSH, HTTPS, and industry-standard encryption protocols.

**Status:** ✅ Confirmed

**Notes:** DigitalOcean Frankfurt confirmed (Spaces + OpenSearch).

---

### 2. Where is the DR (Disaster Recovery) environment hosted?

**Response:** DR leverages secondary backup location in Amsterdam, Netherlands (EU). Combined with primary Frankfurt site, this provides geographic redundancy within the EU.

**Status:** ✅ Confirmed

**Notes:** Frankfurt (primary) + Amsterdam (secondary). Both EU locations. Ask for RTO/RPO targets and failover process details.

---

### 3. Where are backups stored?

**Response:** Backups stored in two EU locations:
- **Primary:** Frankfurt, Germany
- **Secondary:** Amsterdam, Netherlands

Backup schedule: Daily, Weekly, Quarterly, and Yearly backups.

**Status:** ✅ Confirmed

**Notes:** Comprehensive backup schedule (daily/weekly/quarterly/yearly) across two EU locations. All data stays within EU. Confirm backup encryption and restore testing frequency.

---

### 4. Are there geo-partitioning options (e.g., UK-only)?

**Response:** Two data center regions available:
- **Frankfurt, Germany** — for all EU customers
- **New York, USA** — for US customers only

EU customer data is hosted exclusively in Frankfurt. No UK-only option currently available.

**Status:** ✅ Confirmed

**Notes:** EU customers are Frankfurt-only — no cross-region data mixing. UK-only hosting not available; UK customers would be served from Frankfurt. Clarify if additional regions are on the roadmap.

---

### 5. Is data encrypted at rest and in transit?

**Response:** All connections between components are secured using industry-standard encryption protocols (SSH, HTTPS). ISO 27001 certification mandates encryption controls.

**Status:** ✅ Confirmed

**Notes:** Confirm specific encryption standards (e.g., AES-256 at rest, TLS 1.2+ in transit).

---

## 🔹 AI/ML Model Handling

### 6. Are invoice contents sent to any third-party model host (e.g., OpenAI, Azure AI)?

**Response:** AI models are NOT sent to third-party hosts. DocBits uses Mistral AI models running in Frankfurt, Germany — same location as production environment. No data leaves the Frankfurt region for AI processing.

**Status:** ✅ Confirmed

**Notes:** Mistral models hosted in Frankfurt. No third-party API calls for document processing. Fully self-contained.

---

### 7. Are extracted documents used to train broader models across customers?

**Response:** Yes — DocBits uses "AI swarm intelligence" which trains classification and extraction models across all customers. However, the technology works like a map through the data — it learns the coordinates/structural positions of data fields on documents, NOT the actual document content. Raw document data is not shared across tenants.

**Status:** ✅ Confirmed

**Notes:** Swarm intelligence learns structural layout patterns (field coordinates/positions), not document content. This means no customer data (invoice amounts, supplier names, etc.) is shared across tenants — only document structure knowledge.

---

### 8. Can you restrict model training to your tenant only?

**Response:** No per-tenant model isolation option. However, the shared AI models only learn document layout coordinates and structural patterns — not actual document content or business data. Customers can additionally train custom document types scoped to their own tenant.

**Status:** ✅ Confirmed

**Notes:** Low risk: Shared models learn positional/structural data only (coordinates), not business content. Custom document type training remains tenant-scoped.

---

### 9. Where are AI/ML models hosted and executed?

**Response:** AI/ML models (Mistral) are hosted and executed in Frankfurt, Germany — same region as the production environment.

**Status:** ✅ Confirmed

**Notes:** Good: AI processing stays within Frankfurt. No data transfer to external AI infrastructure.

---

### 10. What AI/ML technologies are used (OCR engine, LLM, NLP)?

**Response:** DocBits uses AI, OCR, machine learning for extraction. Supports 120+ languages. Claims 96%+ accuracy. Also uses Gen AI for "AI Tags" feature.

**Status:** ✅ Partial

**Notes:** Ask for specific model details: proprietary vs. third-party OCR, which LLM powers Gen AI features.

---

### 11. Is there an option for on-premise AI model deployment?

**Response:** DocBits architecture documentation references both "DocBits Cloud customer" and "DocBits On premise" deployment options.

**Status:** ✅ Partial

**Notes:** Confirm scope of on-premise option: Does it include full AI processing or only document storage?

---

## 🔹 Data Access & Logging

### 12. Who (vendor support/engineers) can access raw documents and Infor ERP / SAP data?

**Response:** FELLOWPRO AG has a designated Data Protection Officer (Daniel Jordan). DPAs with subprocessors are in place per GDPR. ISO 27001 mandates access controls.

**Status:** ✅ Partial

**Notes:** Ask DocBits: Exact list of personnel roles with raw document access. Is access need-based / on-demand only?

---

### 13. What access controls and logging exist for vendor personnel?

**Response:** ISO 27001 certification requires documented access controls, audit trails, and security measures. DocBits maintains audit trail for compliance and review.

**Status:** ✅ Partial

**Notes:** Ask for: RBAC details, MFA requirements, privileged access management (PAM), and whether access is logged with immutable audit trails.

---

### 14. How long are access logs retained?

**Response:** Logs are stored on DigitalOcean Spaces in Frankfurt and OpenSearch. Customer-accessible logs retained for 30 days. Internal logs retained for 3 months.

**Status:** ✅ Confirmed

**Notes:** DigitalOcean Spaces + OpenSearch in Frankfurt. 30-day customer access / 3-month internal retention. Confirm if logs are immutable/tamper-proof.

---

### 15. How long are uploaded documents / extracted data retained in DocBits?

**Response:** Customers can configure data retention in settings. Options: 30 days or 3 months. After the configured period, documents and extracted data are automatically deleted from DocBits servers.

**Status:** ✅ Confirmed

**Notes:** Customer-configurable retention (30 days / 3 months). Confirm: Does deletion include all copies (DigitalOcean Spaces, OpenSearch, AI training data)?

---

### 16. Can customers request data deletion on demand?

**Response:** FELLOWPRO AG complies with GDPR data subject rights including erasure requests. DPO processes these requests per GDPR Art. 17.

**Status:** ✅ Confirmed

**Notes:** Confirm: Does deletion cover all copies including backups and AI training data derived from the tenant?

---

### 17. What subprocessors have access to customer data?

**Response:** Cloudflare is used for bot protection/DDoS. DPAs are in place with all subprocessors per GDPR requirements.

**Status:** ✅ Partial

**Notes:** Request full subprocessor list. Cloudflare confirmed; ask about cloud hosting provider, AI service providers, etc.

---

### 18. What certifications and compliance frameworks does DocBits hold?

**Response:** ISO 27001 certified. GDPR compliant. Maintains DPAs with all subprocessors. Designated DPO.

**Status:** ✅ Confirmed

**Notes:** Ask: SOC 2 Type II? Penetration test reports? ISO 27701 (privacy)? Annual audit schedule?

---

## 🔹 Integration Scope (Infor ERP / SAP)

### 19. What is the exact list of data fields pulled from ERP masters for validation?

**Response:** Master data imported via Infor BODs:
- **Suppliers:** Sync.SupplierPartyMaster, Sync.RemitToPartyMaster
- **Purchase Orders:** Sync.PurchaseOrder
- **Chart of Accounts:** Sync.CodeDefinition (ChartOfAccounts)
- **Flex Dimensions:** Sync.CodeDefinition (FlexDimensions)
- **Tax Codes:** via BOD publish

**Status:** ✅ Confirmed

**Notes:** Ask DocBits for complete BOD list and field-level mapping documentation for your specific ERP configuration.

---

### 20. What specific header fields are exported back to the ERP?

**Response:** Header export fields include: SupplierCode, PurchaseType, InvoiceType, InvoiceNumberSupplier, InvoiceDate, InvoiceAmount, InvoiceCurrency, RateDeterminer, RateDate, TaxCountry, TransactionEntryDate, Reference, IDMReference, TaxBaseAmount, InvoiceDocumentType, and more.

**Status:** ✅ Confirmed

**Notes:** Review field mapping file for your specific environment. Confirm all static fields match your ERP company setup.

---

### 21. Are write-back operations scoped only to AP/PO interface objects?

**Response:** Export uses Sync.CaptureDocument BOD which is transformed to target BODs (e.g., AP invoice BODs) in ION Desk. Data also exported to Infor IDM for document archival.

**Status:** ✅ Partial

**Notes:** Confirm: Does DocBits write ONLY to AP invoice and PO receipt objects? Any other ERP modules touched? What about IDM write scope?

---

### 22. What integration method is used (ION API, BODs, direct DB)?

**Response:** Integration via Infor ION API, ION Desk, and Infor Standard BODs. No direct database access. Uses ION API files and service accounts for authentication.

**Status:** ✅ Confirmed

**Notes:** Good: No direct DB access. All communication via Infor standard integration layer.

---

### 23. What authentication/authorization is used for ERP connectivity?

**Response:** Uses ION API Files (OAuth2 client credentials) with ION API Client IDs and service accounts created in InforOS.

**Status:** ✅ Confirmed

**Notes:** Ensure service accounts follow least-privilege principle. Review permissions granted to the DocBits ION API user.

---

### 24. Is data transfer between DocBits and the ERP encrypted end-to-end?

**Response:** All connections between components secured using industry-standard encryption (SSH, HTTPS).

**Status:** ✅ Confirmed

**Notes:** ION API communication uses HTTPS/TLS. Confirm minimum TLS version (1.2+).

---

### 25. What document types are supported beyond AP invoices?

**Response:** Supports invoices, delivery notes/bills, quotations, order confirmations, contracts, and more. Handles PO and non-PO invoices.

**Status:** ✅ Confirmed

**Notes:** Clarify which document types write back to the ERP vs. are only stored in IDM.
