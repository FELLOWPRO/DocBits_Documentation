# Script

<figure><img src="../../../../../.gitbook/assets/Bildschirmfoto%202024-05-08%20um%2009.43.25.png" alt=""><figcaption></figcaption></figure>

{% embed url="https://youtu.be/n8NpWWIjmlA" %}
DocBits Document Scripts Explained: Automate Custom Logic in Your Document Workflow
{% endembed %}

#### Panoramica

Gli script in Docbits sono tipicamente scritti in un linguaggio di scripting supportato dal sistema Python. Vengono attivati durante il flusso di elaborazione dei documenti per applicare logiche aziendali complesse o per garantire l'integrità e l'accuratezza dei dati prima che i dati vengano ulteriormente elaborati o archiviati.

#### Funzionalità Chiave e Opzioni

1. **Gestione degli Script**:

* **Nome**: A ciascuno script viene assegnato un nome univoco per l'identificazione.
* **Tipo di Documento**: Associa lo script a un tipo di documento specifico, determinando su quali documenti lo script verrà applicato.
* **Attivazione su**: Definisce quando lo script viene attivato (ad esempio, durante il caricamento del documento, prima dell'esportazione dei dati, dopo la convalida dei dati).
* **Stato Attivo/Inattivo**: Consente agli amministratori di attivare o disattivare gli script senza cancellarli, offrendo flessibilità nei test e nella distribuzione.

2. **Editor degli Script**:

* Fornisce un'interfaccia in cui gli script possono essere scritti e modificati. L'editor supporta tipicamente l'evidenziazione della sintassi, l'evidenziazione degli errori e altre funzionalità per assistere nello sviluppo degli script.
* **Esempio di Script**: Gli script possono includere operazioni come il loop attraverso le righe della fattura per convalidare i totali o per rimuovere voci che non soddisfano determinati criteri.

<figure><img src="../../../../../.gitbook/assets/Bildschirmfoto%202024-05-08%20um%2009.43.37.png" alt=""><figcaption></figcaption></figure>

{% @jira/embed url="https://fellowpro.atlassian.net/browse/DOCB-2498" %}
