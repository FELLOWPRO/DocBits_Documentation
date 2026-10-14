# Architettura

## Cliente cloud

<figure><img src="../../.gitbook/assets/architecture1.avif" alt=""><figcaption></figcaption></figure>

## In sede

<figure><img src="../../.gitbook/assets/architecture2 (1).avif" alt="Docbits Architecture Diagram On Premise"><figcaption></figcaption></figure>

Doc**Bits** si integra perfettamente con Infor LN/M3 attraverso l'API ION, ION Desk e i BOD standard di Infor. La nostra integrazione API ci consente di esportare dati in Infor e di eseguire la validazione dei dati master in Doc**Bits**.

## Esportazione dei Dati in Infor

Utilizziamo l'API ION per inviare il PDF con gli attributi a IDM e il BOD Sync.CaptureDocument a ION Desk. In ION Desk, trasformiamo il Sync.CaptureDocument nei BOD desiderati in base al tipo di documento in fase di elaborazione. Questi BOD Infor trasformati vengono quindi importati automaticamente in LN o M3.

{% hint style="info" %}
Esporta in [Infor](../../infor-integration-and-configuration/exporting-to-infor/)
{% endhint %}

## Validazione dei Dati Master in DocBits

Per identificare il fornitore o confrontare/corrispondere le righe degli ordini di acquisto, attiviamo un trigger in LN/M3 che invia i BOD Sync.RemitToPartyMaster, Sync.SupplierPartyMaster e Sync.PurchaseOrder a Doc**Bits**. Configuriamo questo processo in ION Desk definendo il flusso di dati a un punto di connessione specifico a Doc**Bits**.

<figure><img src="../../.gitbook/assets/architecture3.avif" alt=""><figcaption></figcaption></figure>

{% hint style="info" %}
[Validazione dei Dati Master](../../infor-integration-and-configuration/importing-customer-master-data/)
{% endhint %}

## Importazione Email OAuth Office365

![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/o365_architecture.png)
