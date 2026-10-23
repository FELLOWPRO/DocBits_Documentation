# Architectuur

## **DocBits Cloud-klant**

<figure><img src="../../.gitbook/assets/docbits_cloud_customer_architecture.png" alt="Architectuur voor DocBits Cloud-klanten"><figcaption></figcaption></figure>

## DocBits op locatie

<figure><img src="../../.gitbook/assets/docbits_on_premise_architecture.png" alt="Architectuur van DocBits On Premise"><figcaption></figcaption></figure>

Doc**Bits** integreert naadloos met Infor LN/M3 via de ION API, ION Desk en Infor Standaard BODs. Onze API-integratie stelt ons in staat om gegevens naar Infor te exporteren en masterdata-validatie in Doc**Bits** uit te voeren.

## **DocBits Operator-architectuur**

Alle verbindingen tussen componenten zijn beveiligd met versleutelingsprotocollen volgens de industriestandaard. SSH, HTTPS en andere beveiligde kanalen waarborgen de integriteit en vertrouwelijkheid van gegevens in het hele systeem.

**On premise:**&#x20;

<figure><img src="../../.gitbook/assets/Operator_On-Prem.png" alt="Architectuurdiagram van Operator On-Prem met DocAgent op een clientcomputer die verbinding maakt met de Prefect API en de DocBits-cloud"><figcaption></figcaption></figure>

{% content-ref url="prefect-local-setup-requirements.md" %}
[prefect-local-setup-requirements.md](prefect-local-setup-requirements.md)
{% endcontent-ref %}

**Cloud**:

<figure><img src="../../.gitbook/assets/Operator Cloud .png" alt="Architectuurdiagram van Operator Cloud met de Chrome-extensie, DocBits Operator Cloud, DocFlow en DocBits AI die taak- en antwoordberichten uitwisselen"><figcaption></figcaption></figure>

## Gegevens exporteren naar Infor

We gebruiken de ION API om de PDF met attributen naar IDM te sturen en de BOD Sync.CaptureDocument naar ION Desk. In ION Desk transformeren we de [Sync.CaptureDocument](../../infor-integration-and-configuration/exporting-in-docbits/) naar de gewenste doel-BODs, afhankelijk van het documenttype dat wordt verwerkt. Deze getransformeerde Infor BODs worden vervolgens automatisch geïmporteerd in LN of M3.

{% hint style="info" %}
Exporteren naar [Infor](../../infor-integration-and-configuration/exporting-to-infor/)
{% endhint %}

## Masterdata-validatie in DocBits

Om de leverancier te identificeren of inkooporderregels te vergelijken/te matchen, activeren we in LN/M3 een trigger die de BODs Sync.RemitToPartyMaster, Sync.SupplierPartyMaster en Sync.PurchaseOrder naar Doc**Bits** stuurt. We configureren dit proces in ION Desk door de gegevensstroom naar een specifiek aansluitpunt (connection point) naar Doc**Bits** te definiëren.

<figure><img src="../../.gitbook/assets/docbits_architecture (1).png" alt="DocBits-architectuurdiagram van het Kubernetes-cluster met load balancer, Redis, PostgreSQL, worker-pods en Spaces-datopslag"><figcaption></figcaption></figure>

{% hint style="info" %}
[Masterdata-validatie](../../infor-integration-and-configuration/importing-customer-master-data/)
{% endhint %}

## E-mailimport OAuth Office365

<figure><img src="../../.gitbook/assets/o365_architecture.png" alt="Diagram van de Office 365-e-mailimport dat toont hoe Microsoft Graph API een toegangstoken uitgeeft aan de DocBits-mailservice en het hoofdsysteem"><figcaption></figcaption></figure>
