# Documenti elettronici e configurazione EDI

{% embed url="https://youtu.be/AxrHNEmmXtg" %}
DocBits Tutorial sulla fattura elettronica: elaborare XRechnung / ZUGFeRD (Factur-X), convalidare dati e automatizzare i flussi di lavoro
{% endembed %}

Selezionare il tipo di documento e il formato elettronico nelle impostazioni dei documenti elettronici. Questa configurazione elabora i messaggi EDI in ingresso; non configura la loro trasmissione in uscita.

<figure><img src="../../../../../.gitbook/assets/site-all-edi-list-it.png" alt="Formato EDI esistente con i quattro attributi configurati."><figcaption><p>Formato EDI esistente con i quattro attributi configurati.</p></figcaption></figure>

* STRUCTUREDESCRIPTOR: un descrittore di struttura JSON analizza il messaggio EDI originale e genera JSON. DocBits crea quindi un XML intermedio.

* TRANSFORMATION: un foglio XSLT converte l’XML intermedio nell’XML standard per le elaborazioni successive.

* PREVIEW: un foglio XSLT crea una presentazione leggibile dall’XML trasformato. La schermata dell’editor mostra il codice sorgente, non il documento renderizzato.

* EXTRACTIONPATHS: la configurazione JSON associa campi e colonne a espressioni XPath valutate sull’XML trasformato.

<figure><img src="../../../../../.gitbook/assets/site-all-edi-detail-it.png" alt="Attributo STRUCTUREDESCRIPTOR attivo: descrittore di struttura JSON nell’editor di sola lettura."><figcaption><p>Attributo STRUCTUREDESCRIPTOR attivo: descrittore di struttura JSON nell’editor di sola lettura.</p></figcaption></figure>

## Regole effettivamente utilizzate e attivazione

Se una nota di credito elettronica appare come Invoice, seguite la [guida alla diagnosi della classificazione](credit-note-recognized-as-invoice.md). Descrive la sorgente personalizzata o predefinita effettivamente utilizzata, i codici del tipo, Extraction Paths e l’attivazione in sicurezza.

## Guide per paese

Consultate le guide per paese per le etichette esatte dei formati, la sintassi, i limiti delle versioni e lo stato di configurazione esaminato. [Formati eDocs, versioni e guide per paese](supported-electronic-documents/README.md).


Le viste mostrano una configurazione e una versione esistenti. Le impostazioni variano in base al tipo di documento e al formato. Convalidare le modifiche in una bozza prima dell’attivazione.

Nella versione dell’interfaccia illustrata, l’intestazione Version del pannello delle versioni resta in inglese. Gli identificatori tecnici degli attributi e il codice di configurazione restano invariati.
