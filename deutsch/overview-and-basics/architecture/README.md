# Architektur

## **DocBits Cloud-Kunde**

<figure><img src="../../.gitbook/assets/docbits_cloud_customer_architecture.png" alt="DocBits Cloud Customer Architecture"><figcaption></figcaption></figure>

## DocBits On-Premise

<figure><img src="../../.gitbook/assets/docbits_on_premise_architecture.png" alt="DocBits On Premise Architecture"><figcaption></figcaption></figure>

Doc**Bits** integriert sich nahtlos in Infor LN/M3 über die ION API, ION Desk und die Infor-Standard-BODs. Unsere API-Integration ermöglicht es uns, Daten nach Infor zu exportieren und die Stammdatenvalidierung in Doc**Bits** durchzuführen.

## **DocBits Operator-Architektur**

Alle Verbindungen zwischen den Komponenten werden mit branchenüblichen Verschlüsselungsprotokollen gesichert. SSH, HTTPS und andere sichere Kanäle gewährleisten die Datenintegrität und Vertraulichkeit im gesamten System.

**On-Premise:**&#x20;

<figure><img src="../../.gitbook/assets/Operator_On-Prem.png" alt=""><figcaption></figcaption></figure>

{% content-ref url="prefect-local-setup-requirements.md" %}
[prefect-local-setup-requirements.md](prefect-local-setup-requirements.md)
{% endcontent-ref %}

**Cloud**:

<figure><img src="../../.gitbook/assets/Operator Cloud .png" alt=""><figcaption></figcaption></figure>

## Daten nach Infor exportieren

Wir verwenden die ION API, um das PDF mit Attributen an IDM und die BOD Sync.CaptureDocument an ION Desk zu senden. In ION Desk transformieren wir die [Sync.CaptureDocument](../../infor-integration-and-configuration/exporting-in-docbits/) je nach verarbeitetem Dokumenttyp in die gewünschten Ziel-BODs. Diese transformierten Infor-BODs werden anschließend automatisch in LN oder M3 importiert.

{% hint style="info" %}
Export nach [Infor](../../infor-integration-and-configuration/exporting-to-infor/)
{% endhint %}

## Stammdatenvalidierung in DocBits

Um den Lieferanten zu identifizieren oder Bestellpositionen zu vergleichen/abzugleichen, aktivieren wir in LN/M3 einen Trigger, der die BODs Sync.RemitToPartyMaster, Sync.SupplierPartyMaster und Sync.PurchaseOrder an Doc**Bits** sendet. Wir konfigurieren diesen Prozess in ION Desk, indem wir den Datenfluss zu einem bestimmten Verbindungspunkt zu Doc**Bits** definieren.

<figure><img src="../../.gitbook/assets/docbits_architecture (1).png" alt=""><figcaption></figcaption></figure>

{% hint style="info" %}
[Stammdatenvalidierung](../../infor-integration-and-configuration/importing-customer-master-data/)
{% endhint %}

## E-Mail-Import OAuth Office365

<figure><img src="../../.gitbook/assets/o365_architecture.png" alt=""><figcaption></figcaption></figure>
