# Architecture

## **DocBits Cloud-Kunde**

## DocBits On-Premise

Doc**Bits** integriert sich nahtlos in Infor LN/M3 über die ION API, ION Desk und die Infor-Standard-BODs. Unsere API-Integration ermöglicht es uns, Daten nach Infor zu exportieren und die Stammdatenvalidierung in Doc**Bits** durchzuführen.

## **DocBits Operator-Architektur**

Alle Verbindungen zwischen den Komponenten werden mit branchenüblichen Verschlüsselungsprotokollen gesichert. SSH, HTTPS und andere sichere Kanäle gewährleisten die Datenintegrität und Vertraulichkeit im gesamten System.

**On-Premise:**

{% content-ref url="https://github.com/Fellow-Consulting-AG/docbits/tree/de/readme/overview-and-basics/architecture/prefect-local-setup-requirements.md" %}
[https://github.com/Fellow-Consulting-AG/docbits/tree/de/readme/overview-and-basics/architecture/prefect-local-setup-requirements.md](https://github.com/Fellow-Consulting-AG/docbits/tree/de/readme/overview-and-basics/architecture/prefect-local-setup-requirements.md)
{% endcontent-ref %}

**Cloud**:

## Daten nach Infor exportieren

Wir verwenden die ION API, um das PDF mit Attributen an IDM und die BOD Sync.CaptureDocument an ION Desk zu senden. In ION Desk transformieren wir die [Sync.CaptureDocument](../../infor-integration-and-configuration/exporting-in-docbits/) je nach verarbeitetem Dokumenttyp in die gewünschten Ziel-BODs. Diese transformierten Infor-BODs werden anschließend automatisch in LN oder M3 importiert.

{% hint style="info" %}
Export nach [Infor](../../infor-integration-and-configuration/exporting-to-infor/)
{% endhint %}

## Stammdatenvalidierung in DocBits

Um den Lieferanten zu identifizieren oder Bestellpositionen zu vergleichen/abzugleichen, aktivieren wir in LN/M3 einen Trigger, der die BODs Sync.RemitToPartyMaster, Sync.SupplierPartyMaster und Sync.PurchaseOrder an Doc**Bits** sendet. Wir konfigurieren diesen Prozess in ION Desk, indem wir den Datenfluss zu einem bestimmten Verbindungspunkt zu Doc**Bits** definieren.

{% hint style="info" %}
[Stammdatenvalidierung](../../administration-and-setup/importing-customer-master-data/)
{% endhint %}

## E-Mail-Import OAuth Office365
