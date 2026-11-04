# Corrispondenza automatica dei dati dell'ordine di acquisto

Docbits è un sistema avanzato progettato per automatizzare la corrispondenza dei dati dell'ordine di acquisto (PO) con i documenti delle fatture in arrivo. Questo strumento è specificamente progettato per una gestione efficiente e un'elaborazione dei dati delle fatture all'interno dei sistemi ERP. Questa documentazione spiega i concetti di base della corrispondenza automatica attraverso Docbits e definisce le regole specifiche necessarie per una corrispondenza di successo.

## **Principi fondamentali della corrispondenza automatica in Docbits**

**Estrazione dei dati:** Docbits inizia il processo estraendo i dati rilevanti dai documenti delle fatture digitalizzate. Tipicamente, questi dati includono i numeri degli articoli, le quantità e i prezzi unitari di ciascuna riga della fattura. La precisione di questa estrazione è cruciale, poiché costituisce la base per il successivo processo di corrispondenza.

**Confronto con i dati dell'ordine di acquisto:** I dati estratti vengono confrontati con le informazioni corrispondenti negli ordini di acquisto memorizzati. Docbits verifica se i numeri degli articoli, le quantità e i prezzi corrispondono a quelli nei PO. Per una corrispondenza di successo, i dati nelle fatture devono corrispondere ai dati negli ordini di acquisto, considerando le soglie di tolleranza definite.

**Corrispondenza automatica:** Sulla base dei risultati del confronto, Docbits esegue la corrispondenza. Il sistema verifica se i criteri di corrispondenza rientrano nei limiti di tolleranza impostati. Se questi criteri sono soddisfatti, la corrispondenza è considerata riuscita.

**Segnalazione:** Dopo aver completato il processo di corrispondenza, Docbits genera report che mostrano lo stato delle corrispondenze. Questi report informano sulle fatture corrispondenti con successo e identificano quelle con discrepanze.

## **Definizione delle regole di corrispondenza**

**Numero dell'articolo:** Il numero dell'articolo sulla fattura deve corrispondere esattamente al numero dell'articolo nell'ordine di acquisto. Non è prevista alcuna tolleranza per deviazioni nei numeri degli articoli.

**Quantità:** La quantità di merci consegnate sulla fattura può variare entro un intervallo di tolleranza predefinito. Tipicamente, una tolleranza del ±5% potrebbe essere accettabile per tener conto di differenze minori nelle quantità di consegna.

**Prezzi:** Le deviazioni dei prezzi sono tollerabili fino a una soglia prestabilita. Una tolleranza comune potrebbe essere del ±2% del prezzo per accettare lievi differenze nelle dichiarazioni di prezzo che derivano da differenze di arrotondamento o fluttuazioni valutarie.

## **Stato della corrispondenza:**

* **Corrispondenza completa:** Tutti i punti dati (numero dell'articolo, quantità e prezzo) rientrano nei limiti di tolleranza impostati.
* **Corrispondenza parziale:** Uno o più punti dati deviano al di fuori dei limiti di tolleranza, ma le deviazioni sono minime e richiedono una revisione manuale.
* **Nessuna corrispondenza:** Deviazioni significative in uno o più punti dati che richiedono correzione immediata o ulteriori indagini.

La definizione precisa di queste regole e l'impostazione dei limiti di tolleranza sono cruciali per l'efficienza della corrispondenza automatica e la riduzione delle interventi manuali. Docbits consente una configurazione flessibile di questi parametri per soddisfare le esigenze di varie aziende e settori industriali.
