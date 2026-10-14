---
hidden: true
---

# Impostazione dei Modelli EDI

## Ecco le istruzioni passo dopo passo per impostare i modelli EDI:

<figure><img src="../../../../../../.gitbook/assets/docbits_sso_cert_metadata.png" alt="Docbits Sso Cert Metadata"><figcaption></figcaption></figure>

**Definire il descrittore di struttura:**

* Identificare il tipo di messaggio EDI con cui si sta lavorando, ad esempio ANSI X12, EDIFACT o un formato personalizzato.
* Determinare i segmenti, gli elementi e i sottoelementi all'interno della struttura EDI.
* Creare un descrittore di struttura che rifletta accuratamente la gerarchia e l'organizzazione del messaggio EDI. Ciò può essere fatto utilizzando una sintassi speciale come XML o JSON.

<figure><img src="../../../../../../.gitbook/assets/docbits_sso_access_settings.png" alt="Docbits Sso Access Settings" width="273"><figcaption></figcaption></figure>

**Impostare le trasformazioni:**

* Utilizzare uno strumento o un software appropriato che supporti le trasformazioni EDI, come un traduttore EDI.
* Definire le regole per la conversione del messaggio EDI nel formato interno del proprio sistema e viceversa.
* Configurare le trasformazioni per interpretare ed elaborare segmenti, elementi e sottoelementi in base ai requisiti del proprio sistema. Testare accuratamente le trasformazioni per assicurarsi che i dati siano interpretati e formattati correttamente.

<figure><img src="../../../../../../.gitbook/assets/docbits_sso_idp_config.png" alt="Docbits Sso Idp Config" width="268"><figcaption></figcaption></figure>

**Configurare i percorsi di estrazione per un'estrazione e una formattazione dei dati ottimali:**

* Identificare i campi dati da estrarre e trasferire al proprio sistema interno.
* Definire percorsi o regole di estrazione per estrarre i campi dati rilevanti dai messaggi EDI.
* Considerare le diverse variazioni e formati che possono verificarsi nei messaggi EDI in entrata e assicurarsi che i percorsi di estrazione siano sufficientemente flessibili per adattarvisi.
* Convalidare i risultati dell'estrazione per assicurarsi che vengano estratti i campi dati corretti e che siano formattati correttamente.

<figure><img src="../../../../../../.gitbook/assets/docbits_edi_validate_extraction.png" alt="Docbits Edi Validate Extraction" width="92"><figcaption></figcaption></figure>

Definendo attentamente il descrittore di struttura, impostando le trasformazioni e configurando i percorsi di estrazione, è possibile garantire che l'estrazione e la formattazione dei dati vengano eseguite in modo ottimale nei modelli EDI. Ciò contribuirà a migliorare l'efficienza e l'accuratezza delle proprie comunicazioni aziendali elettroniche.
