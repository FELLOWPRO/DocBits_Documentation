# Architettura

## **Cliente DocBits Cloud**

<figure><img src="../../.gitbook/assets/docbits_cloud_customer_architecture.png" alt="Architettura del cliente DocBits Cloud"><figcaption></figcaption></figure>

## DocBits in locale

<figure><img src="../../.gitbook/assets/docbits_on_premise_architecture.png" alt="Architettura DocBits On Premise"><figcaption></figcaption></figure>

Doc**Bits** si integra perfettamente con Infor LN/M3 attraverso l'API ION, ION Desk e i BOD standard di Infor. La nostra integrazione API ci consente di esportare dati in Infor e di eseguire la validazione dei dati master in Doc**Bits**.

## **Architettura di DocBits Operator**

Tutte le connessioni tra i componenti sono protette con protocolli di crittografia standard del settore. SSH, HTTPS e altri canali sicuri garantiscono l'integrità e la riservatezza dei dati in tutto il sistema.

**In sede:**

<figure><img src="../../.gitbook/assets/Operator_On-Prem.png" alt="Diagramma dell'architettura di Operator On-Prem con DocAgent su un client collegato alla Prefect API e al cloud DocBits"><figcaption></figcaption></figure>

{% content-ref url="prefect-local-setup-requirements.md" %}
[prefect-local-setup-requirements.md](prefect-local-setup-requirements.md)
{% endcontent-ref %}

**Cloud**:

<figure><img src="../../.gitbook/assets/Operator Cloud .png" alt="Diagramma dell'architettura di Operator Cloud con l'estensione Chrome, DocBits Operator Cloud, DocFlow e DocBits AI che si scambiano messaggi di attività e risposte"><figcaption></figcaption></figure>

## Esportazione dei Dati in Infor

Utilizziamo l'API ION per inviare il PDF con gli attributi a IDM e il BOD Sync.CaptureDocument a ION Desk. In ION Desk, trasformiamo il [Sync.CaptureDocument](../../infor-integration-and-configuration/exporting-in-docbits/) nei BOD di destinazione desiderati in base al tipo di documento in fase di elaborazione. Questi BOD Infor trasformati vengono quindi importati automaticamente in LN o M3.

{% hint style="info" %}
Esporta in [Infor](../../infor-integration-and-configuration/exporting-to-infor/)
{% endhint %}

## Validazione dei Dati Master in DocBits

Per identificare il fornitore o confrontare/corrispondere le righe degli ordini di acquisto, attiviamo un trigger in LN/M3 che invia i BOD Sync.RemitToPartyMaster, Sync.SupplierPartyMaster e Sync.PurchaseOrder a Doc**Bits**. Configuriamo questo processo in ION Desk definendo il flusso di dati verso un punto di connessione specifico a Doc**Bits**.

<figure><img src="../../.gitbook/assets/docbits_architecture (1).png" alt="Diagramma dell'architettura DocBits del cluster Kubernetes con bilanciatore di carico, Redis, PostgreSQL, pod di lavoro e archiviazione dati Spaces"><figcaption></figcaption></figure>

{% hint style="info" %}
[Validazione dei Dati Master](../../infor-integration-and-configuration/importing-customer-master-data/)
{% endhint %}

## Importazione Email OAuth Office365

<figure><img src="../../.gitbook/assets/o365_architecture.png" alt="Diagramma dell'importazione e-mail di Office 365 che mostra Microsoft Graph API che emette un token di accesso per il servizio di posta di DocBits e il sistema principale"><figcaption></figcaption></figure>
