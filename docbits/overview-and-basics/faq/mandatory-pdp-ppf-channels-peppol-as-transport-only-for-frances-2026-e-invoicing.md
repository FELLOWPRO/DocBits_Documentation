# France E-Invoicing: Approved Platforms and PEPPOL

## Current Rules and Timetable

For French domestic B2B invoices within the scope of the reform between businesses subject to VAT, invoice exchange must go through an **approved platform (plateforme agréée, PA; formerly PDP)**. The **public invoicing portal (PPF)** serves the public directory and tax-data collection functions; it is not an alternative invoice exchange platform for these transactions.

* **1 September 2026:** All businesses in scope must be able to receive electronic invoices. Large enterprises (GE) and intermediate-sized enterprises (ETI) must also issue electronic invoices and meet their e-reporting obligations from that date.
* **1 September 2027:** Issuance and e-reporting obligations apply to small and medium-sized enterprises (PME) and micro-enterprises.

The applicable obligation depends on the transaction's scope and the business category. Refer to the official [approved platform guidance](https://www.impots.gouv.fr/facturation-electronique-et-plateformes-agreees), [implementation timetable](https://www.impots.gouv.fr/professionnel/questions/partir-de-quand-suis-je-concerne-par-la-reforme-de-la-facturation) and [ministry response](https://www.senat.fr/questions/base/2026/qSEQ260107185.html).

## PEPPOL and Interoperability

PEPPOL can provide transport and interoperability between connected systems and platforms. Using PEPPOL does not replace the requirement to use a PA for invoice exchanges within the French mandate. Do not treat a PEPPOL connection alone as evidence that French exchange and reporting obligations are fulfilled.

## Historical Technical Context

The six diagrams and the API descriptions below are retained from earlier PPF/PDP material for historical technical context. They use the former terminology and architecture; they do not describe a current option to exchange mandated B2B invoices through the PPF. Check current PA and public-service specifications before implementing an integration.

<figure><img src="../../.gitbook/assets/Picture 1.png" alt="Diagram of an invoice lifecycle from Supplier through Submitted, Received by the platform and Made available states with Rejected, Refused, Disputed, Partially approved, In hand and Completed outcomes"><figcaption></figcaption></figure>

### Historical API Service Model

The earlier API model described accessing available functions from the IT tools deployed by partner organizations, through two integration methods:

* **Information systems (IS):** APIs were described as integrated into the systems of invoice issuers, recipients or their dematerialisation operators (ODs). Some APIs were intended for PDP systems, offering an alternative to EDI integration.
* **Third-party software:** Software publishers could add a communication layer to customer systems. Earlier references to a connection to the PPF belong to that historical model and are not a current invoice exchange route.

<figure><img src="../../.gitbook/assets/Picture 6.png" alt="Diagram of an Issuer OD-PDP and Receiver OD-PDP linked through service portals and third-party software with a data control and recovery step between them"><figcaption></figcaption></figure>

### Historical Interconnection Diagram

This diagram illustrates the earlier platform interconnection context. Current implementation must follow PA requirements; no general requirement that every exchange use a single transport network is asserted here.

<figure><img src="../../.gitbook/assets/Picture 2.png" alt="Diagram of three numbered control layers, technical controls, application controls and functional and business controls, each feeding into a following process step"><figcaption></figcaption></figure>

### Historical Hub Connection

The earlier hub model described a web or application solution in which **the hub made API calls on behalf of its customers**. It referred to a technical account for each partner and an application under PISTE plus a PPF connection for the hub. These are historical architecture details, not a verified current integration procedure.

<figure><img src="../../.gitbook/assets/Picture 5.png" alt="Hub model diagram showing one partner with one technical account, the hub, one application under PISTE and one connection"><figcaption></figcaption></figure>

### Historical References

The earlier material cited [the former timetable and legal overview](https://www.ey.com/en_gl/technical/tax-alerts/france-revises-schedule-for-adopting-e-invoicing-reform), [2022 specifications](https://www.avalara.com/blog/en/europe/2022/09/france-publishes-updated-specifications-for-e-invoicing-and-e-reporting.html), [a 2025 reform overview](https://www.avalara.com/blog/en/europe/2025/01/e-invoicing-reform-france.html), [platform interconnection background](https://nymus.be/fr/facturation-electronique-en-france/), [PEPPOL background](https://edicomgroup.com/blog/status-of-b2b-electronic-invoicing-in-france) and [exchange background](https://nymus.be/fr/facturation-electronique-en-france/). These links and the remaining diagrams are retained as historical context. Use the official sources above for current obligations, including the distinction between PA invoice exchange and PPF public functions. The earlier reference to Article 91 of the 2024 Finance Law does not establish a current PPF exchange option.

<div><figure><img src="../../.gitbook/assets/Picture 3.png" alt="Diagram of reception of an EDI flow and flow 2 via API passing functional controls for semantic format, directory and data consistency before incorporation of invoicing data and an invoice submitted outcome"><figcaption></figcaption></figure> <figure><img src="../../.gitbook/assets/Picture 4.png" alt="Diagram of an EDI flow and API flow passing functional controls and specific business rules before rejection or refusal of the invoice or an invoice received and made available"><figcaption></figcaption></figure></div>
