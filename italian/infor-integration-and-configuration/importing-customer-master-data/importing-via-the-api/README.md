---
description: Inviare dati master a DocBits manualmente tramite API
---

# Importare tramite API

I dati master arrivano normalmente in DocBits in automatico attraverso il flusso di dati ION. Le pagine di questa sezione descrivono come inviare gli stessi dati manualmente tramite l'interfaccia di test dell'API — utile quando si vuole reimportare un record, caricare qualcosa che non è mai arrivato o provare una nuova mappatura dei campi prima di attivare il flusso automatico.

Ogni pagina segue gli stessi cinque passaggi: aprire il link dell'API del proprio ambiente, autorizzarsi con Org ID e API key, compilare il modulo, eseguire e verificare che i dati siano arrivati.

* [Importare Fornitori (Supplier BOD)](supplier-bod.md)
* [Importare Ordini di Acquisto (Purchase Order BOD)](purchase-order-bod.md)
* [Importare Entrate Merci (Receive Delivery BOD)](receive-delivery-bod.md)
* [Importare Dati Master da XML](master-data-xml.md)

## Cosa serve

* **Una API key** — vedere [API Key Management](../../../administration-and-setup/settings/global-settings/integration/api-key-management.md).
* **Il proprio Org ID** — in **Settings → Integration & SSO**, nella sezione **ID**.
* **I dati veri e propri**, come file XML o come contenuto XML da incollare.

{% hint style="warning" %}
Un'importazione scrive direttamente nei dati master della propria organizzazione. Verificare a quale ambiente, a quale regione e a quale organizzazione si punta prima di eseguire.
{% endhint %}
