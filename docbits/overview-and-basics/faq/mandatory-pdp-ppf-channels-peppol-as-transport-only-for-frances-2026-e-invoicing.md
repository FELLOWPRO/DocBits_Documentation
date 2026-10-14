# Mandatory PDP/PPF Channels – PEPPOL as Transport Only for France’s 2026 E-Invoicing

## PDP or PPF Required for Domestic B2B E-Invoices

Under France’s 2026 e-invoicing mandate, companies cannot rely solely on the PEPPOL network to exchange domestic B2B invoices. The law requires that all invoices between French VAT-registered businesses be routed through either a certified private platform (PDP) or the state’s public invoicing portal (PPF) to satisfy legal [requirements](https://www.ey.com/en_gl/technical/tax-alerts/france-revises-schedule-for-adopting-e-invoicing-reform) ￼. In other words, businesses will no longer send invoices directly to customers – they must transmit them via an approved e-invoicing platform (a PDP) or via the government [portal](https://www.avalara.com/blog/en/europe/2022/09/france-publishes-updated-specifications-for-e-invoicing-and-e-reporting.html) ￼. This ensures the tax authority receives the required data in real-time. Simply exchanging invoices over PEPPOL without involving an accredited PDP/PPF would not meet the mandated reporting and transmission obligations.

<figure><img src="../../.gitbook/assets/Picture 1.png" alt=""><figcaption></figcaption></figure>

### Introduction to the service offer

The API mode allows users to access all features available to them from the IT tools already deployed within the partner structures. There are two integration methods:

### ·       Integration into Information Systems (IS):

APIs are integrated directly into information systems or management software for parties issuing and receiving invoices or their dematerialising operators (ODs). Users can thus directly access the solution’s features and their upgrades from their usual IT tools, internal or offered by their OD.

APIs can also be integrated into the IS of the PDPs to give them more flexibility (compared with EDI mode), with some APIs dedicated to their use.

### ·       Integration into third-party software:

Editors will be able to offer software based on the APIs. Depending on the mode chosen by the editor, connection can then be effected by the editor, or by the customer itself during installation or deployment in its IS. This third-party software will complement the customer’s information system by adding a communication layer to the PPF.

<figure><img src="../../.gitbook/assets/Picture 6.png" alt=""><figcaption></figcaption></figure>

## PEPPOL Used Only as an Interoperability Layer

France is adopting PEPPOL as part of its infrastructure, but only as a transport layer within the PDP framework, not as an independent compliance route.  The French tax authority (DGFiP) is becoming the Peppol Authority to standardize how PDPs [interconnect](https://www.avalara.com/blog/en/europe/2025/01/e-invoicing-reform-france.html) . All certified PDPs are required to interconnect via the PEPPOL network for exchanging [invoices](https://nymus.be/fr/facturation-electronique-en-france/) .  This means PEPPOL will facilitate interoperability between authorized platforms – not replace the need for those platforms.  In practice, a company may use PEPPOL only by working through a PDP (or the PPF acting in its limited role) that uses PEPPOL to send or receive invoices. This has been confirmed in official guidance: the public portal is focusing on data collection, while invoice distribution will happen exclusively through PDPs, with those PDPs leveraging networks like [PEPPOL](https://edicomgroup.com/blog/status-of-b2b-electronic-invoicing-in-france) for [exchange](https://nymus.be/fr/facturation-electronique-en-france/) .

\


<figure><img src="../../.gitbook/assets/Picture 2.png" alt=""><figcaption></figcaption></figure>

## Connection of a hub:

The hub provides its customers with a web or application solution to enable them to make the various API calls. **It is thus the hub that makes API calls on behalf of all its customers**. In this case, each partner must have a technical account, but only the hub needs an application under PISTE and a connection to the PPF.

<figure><img src="../../.gitbook/assets/Picture 5.png" alt=""><figcaption></figcaption></figure>



Source: Article 91 of France’s 2024 Finance Law (summarized by EY) mandates e-invoices be sent via a certified PDP or the state portal .  The French tax authority’s updates further clarify that after 2024 reforms, businesses must use a registered PDP for B2B e-invoicing (the PPF will no longer serve as a free exchange platform) .  PEPPOL is being implemented to connect these PDPs, not as an alternate channel outside the system . This confirms that using the PEPPOL network alone is insufficient – compliance in France’s 2026 e-invoicing regime requires integration with the PPF or a certified PDP, with PEPPOL serving only as the underlying delivery network among those platforms.

<div><figure><img src="../../.gitbook/assets/Picture 3.png" alt=""><figcaption></figcaption></figure> <figure><img src="../../.gitbook/assets/Picture 4.png" alt=""><figcaption></figcaption></figure></div>
