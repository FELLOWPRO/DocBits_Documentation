# Architectuur

Cloud klant:

<figure><img src="../../.gitbook/assets/architecture1.avif" alt=""><figcaption></figcaption></figure>

On premise:

<figure><img src="../../.gitbook/assets/architecture2.avif" alt=""><figcaption></figcaption></figure>

Doc**Bits** integreert naadloos met Infor LN/M3 via de ION API, ION Desk en Infor Standaard BODs. Onze API-integratie stelt ons in staat om gegevens naar Infor te exporteren en masterdata-validatie in Doc**Bits** uit te voeren.

## Gegevens exporteren naar Infor

We gebruiken de ION API om de PDF met attributen naar IDM te sturen en de BOD Sync.CaptureDocument naar ION Desk. In ION Desk transformeren we de Sync.CaptureDocument naar de gewenste doel BODs op basis van het documenttype dat wordt verwerkt. Deze getransformeerde Infor BODs worden vervolgens automatisch geïmporteerd naar LN of M3.

{% hint style="info" %}
Exporteer naar [Infor](../../infor-integration-and-configuration/exporting-to-infor/)
{% endhint %}

## Masterdata-validatie in DocBits

Om de leverancier te identificeren of inkooporderelementen te vergelijken/te matchen, activeren we een trigger in LN/M3 die de Sync.RemitToPartyMaster, Sync.SupplierPartyMaster en Sync.PurchaseOrder BODs naar Doc**Bits** stuurt. We configureren dit proces in ION Desk door de gegevensstroom naar een specifiek aansluitpunt naar Doc**Bits** te definiëren.

<figure><img src="../../.gitbook/assets/architecture3.avif" alt=""><figcaption></figcaption></figure>

{% hint style="info" %}
[Masterdata-validatie](../../infor-integration-and-configuration/importing-customer-master-data/)
{% endhint %}

## E-mail Import OAuth Office365

![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/o365_architecture.png)
