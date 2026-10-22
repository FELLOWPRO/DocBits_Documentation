# XRechnung

{% embed url="https://youtu.be/AxrHNEmmXtg" %}
DocBits Tutorial sulla fattura elettronica: elaborare XRechnung / ZUGFeRD (Factur-X), convalidare dati e automatizzare i flussi di lavoro
{% endembed %}

## Panoramica

Nel pannello di amministrazione XRechnung, incontrerai i seguenti componenti chiave:

## 1. Trasformazione

### Scopo

Il processo di trasformazione è essenziale per convertire i dati grezzi, solitamente in formato XML, in un formato strutturato che soddisfi requisiti specifici, come generare una fattura. In XRechnung, ciò si ottiene principalmente utilizzando XSLT (Extensible Stylesheet Language Transformations). XSLT è un linguaggio progettato per trasformare documenti XML in altri tipi di documenti, come un altro XML, HTML o testo semplice.

### Come funziona

• Modello XSLT: il file XSLT definisce come vengono elaborati i dati XML e come dovrebbe apparire l'output finale. Applica regole e modelli per estrarre, manipolare e produrre dati dal documento XML.

• Elementi e attributi: il file XSLT contiene elementi e attributi specifici che controllano il processo di trasformazione. Ad esempio, \<xsl:value-of> viene utilizzato per estrarre il valore di un nodo specifico dal documento XML.

### Funzioni di amministrazione

• Modifying the XSLT:

• Modifica modelli esistenti: un amministratore può modificare i modelli XSLT esistenti per cambiare il modo in cui vengono trasformati i dati di input XML. Ad esempio, se è necessario estrarre informazioni aggiuntive dal documento XML, un amministratore potrebbe aggiungere nuove regole nel file XSLT.

• Crea nuove versioni: se sono necessarie modifiche, un amministratore può creare una nuova versione del modello XSLT. Ciò garantisce che le versioni precedenti rimangano intatte per riferimento storico o rollback, se necessario.

### Esempio:

Supponiamo che il modello XSLT estragga l’ID della fattura utilizzando:

```xml
<xsl:value-of select="//INVOICE/INVOICE_ID/text()" />
```

Se è necessario estrarre un nuovo campo, ad esempio un numero di riferimento del cliente, un amministratore potrebbe aggiungere:

```xml
<xsl:value-of select="//INVOICE/CUSTOMER_REFERENCE_NUMBER/text()" />
```

## 2. Anteprima

### Scopo

La funzione Anteprima consente agli amministratori di visualizzare l'output generato dalla trasformazione XSLT prima di finalizzarla. Questo passaggio è fondamentale per garantire che le regole di trasformazione funzionino correttamente e che l’output soddisfi gli standard richiesti.

### Come funziona

• Convalida in tempo reale: la funzionalità di anteprima fornisce un rendering in tempo reale di come appariranno i dati trasformati una volta applicati a un documento reale (come una fattura). Ciò aiuta a individuare tempestivamente errori o problemi di formattazione.

• Aggiustamenti: se l'anteprima mostra discrepanze o errori, è possibile apportare modifiche direttamente nel file di trasformazione (XSLT).

### Funzioni di amministrazione

• Personalizzazione dell'anteprima:

• Modifica impostazioni di anteprima: un amministratore può regolare quali parti della trasformazione visualizzare in anteprima. Ad esempio, potrebbero concentrarsi su sezioni specifiche del documento o testare nuove regole aggiunte al modello XSLT.

• Salva e ripeti: dopo aver apportato le modifiche, è possibile aggiornare l'anteprima per visualizzare le modifiche. Questo processo iterativo consente la messa a punto fino al raggiungimento dell'output desiderato.

### Esempio:

Se un amministratore nota che il formato della data nell'anteprima non è corretto (ad esempio, mostrando YYYY-MM-DD invece di DD-MM-YYYY), può modificare XSLT per formattare correttamente la data e vedere immediatamente il risultato nell'anteprima.

## 3. Percorsi di estrazione

### Scopo

I percorsi di estrazione definiscono i percorsi specifici all'interno di una struttura XML o JSON da cui i dati devono essere estratti. Questo processo è essenziale per isolare le informazioni chiave all'interno del documento che verranno utilizzate nella trasformazione o per altre attività di elaborazione.

### Come funziona

• XPath e JSONPath: i percorsi di estrazione utilizzano linguaggi come XPath (per XML) o JSONPath (per JSON) per specificare la posizione dei dati all'interno del documento. Questi percorsi sono cruciali per indicare al sistema esattamente dove trovare e come estrarre le informazioni richieste.

### Funzioni di amministrazione

• Definizione e modifica dei percorsi:

• Modifica percorsi esistenti: un amministratore può modificare i percorsi di estrazione se la struttura dei dati cambia o se è necessario estrarre dati aggiuntivi. Ciò potrebbe comportare la modifica delle espressioni XPath o JSONPath.

• Aggiungi nuovi percorsi: per nuovi campi o punti dati, un amministratore può definire nuovi percorsi di estrazione. Ciò comporterebbe la specifica del percorso corretto nel documento XML o JSON.

### Esempio:

In un documento fattura XML, se il percorso dell’ID della fattura è definito come:

```json
"invoice_id": "//INVOICE/INVOICE_ID/text()"
```

Inoltre, è necessario aggiungere un nuovo campo, ad esempio un indirizzo di spedizione, un amministratore potrebbe aggiungere:

```json
"shipping_address": "//INVOICE/SHIPPING/ADDRESS/text()"
```

## Regole effettivamente utilizzate e attivazione

Le regole specifiche dell’organizzazione hanno la precedenza su quelle predefinite per il formato eDoc rilevato. Verificate la TRANSFORMATION attiva e verificate quale nodo fornisce invoice_type nell’XML trasformato; il percorso dipende dal formato. Save salva una bozza; usate il segno di spunta per attivarla dopo i test. Il rendering di Preview non dimostra il tipo di documento memorizzato. Consultate la [guida alla diagnosi della classificazione](../credit-note-recognized-as-invoice.md) per i codici 381/261, gli script successivi e le precauzioni prima della rielaborazione.
