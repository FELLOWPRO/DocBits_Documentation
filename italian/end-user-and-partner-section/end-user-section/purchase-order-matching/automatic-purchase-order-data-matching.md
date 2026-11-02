# Abbinamento Automatico dei Dati degli Ordini di Acquisto

Docbits è un sistema avanzato progettato per automatizzare l'abbinamento dei dati degli ordini di acquisto (PO) con i documenti delle fatture in arrivo. Questo strumento è specificamente progettato per una gestione efficiente e l'elaborazione dei dati delle fatture all'interno dei sistemi ERP. Questa documentazione spiega le basi dell'abbinamento automatico tramite Docbits e definisce le regole specifiche necessarie per un abbinamento riuscito.

<figure><img src="../../../.gitbook/assets/docbits_purchase_order_invoice_3.svg" alt="DocBits Acquisto Ordine Fattura 3"><figcaption></figcaption></figure>

## **Principi Fondamentali dell'Abbinamento Automatico in Docbits**

**Estrazione dei Dati:** Docbits inizia il processo estraendo i dati rilevanti dai documenti delle fatture digitalizzate. Tipicamente, questi dati includono numeri di articolo, quantità e prezzi unitari di ciascuna riga della fattura. La precisione di questa estrazione è cruciale, poiché costituisce la base per il successivo processo di abbinamento.

**Confronto con i Dati PO:** I dati estratti vengono confrontati con le informazioni corrispondenti negli ordini di acquisto memorizzati. Docbits verifica se i numeri di articolo, le quantità e i prezzi corrispondono a quelli nei PO. Per un abbinamento riuscito, i dati nelle fatture devono corrispondere ai dati negli ordini di acquisto, considerando le soglie di tolleranza definite.

**Abbinamento Automatico:** Sulla base dei risultati del confronto, Docbits esegue l'abbinamento. Il sistema verifica se i criteri di abbinamento rientrano nei limiti di tolleranza impostati. Se questi criteri sono soddisfatti, l'abbinamento è considerato riuscito.

**Reportistica:** Dopo aver completato il processo di abbinamento, Docbits genera report che mostrano lo stato degli abbinamenti. Questi report informano sulle fatture abbinate con successo e identificano quelle con discrepanze.

## **Definizione delle Regole di Abbinamento**

**Numero di Articolo:** Il numero di articolo sulla fattura deve corrispondere esattamente al numero di articolo nell'ordine di acquisto. Non c'è tolleranza per deviazioni nei numeri di articolo.

**Quantità:** La quantità di merci consegnate sulla fattura può variare entro un intervallo di tolleranza predefinito. Tipicamente, una tolleranza del ±5% potrebbe essere accettabile per tenere conto di piccole differenze nelle quantità di consegna.

**Prezzi:** Le deviazioni di prezzo sono tollerabili fino a una soglia impostata. Una tolleranza comune potrebbe essere del ±2% del prezzo per accettare lievi differenze nelle dichiarazioni di prezzo che derivano da differenze di arrotondamento o fluttuazioni di valuta.

## **Stato dell'Abbinamento:**

* **Abbinamento Completo:** Tutti i punti dati (numero di articolo, quantità e prezzo) sono entro i limiti di tolleranza impostati.
* **Abbinamento Parziale:** Uno o più punti dati deviano al di fuori dei limiti di tolleranza, ma le deviazioni sono minime e richiedono una revisione manuale.
* **Nessun Abbinamento:** Deviazioni significative in uno o più punti dati che richiedono correzione immediata o ulteriori indagini.

La definizione precisa di queste regole e l'impostazione dei limiti di tolleranza sono cruciali per l'efficienza dell'abbinamento automatico e la riduzione degli interventi manuali. Docbits consente una configurazione flessibile di questi parametri per soddisfare le esigenze di varie aziende e settori.
