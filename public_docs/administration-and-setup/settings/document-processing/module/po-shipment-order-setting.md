# Impostazione dell'Ordine di Spedizione PO

## **Panoramica**

La sezione **Ordine di Spedizione PO** fornisce una panoramica dello stato di consegna e fatturazione degli elementi dell'Ordine di Acquisto corrispondenti. Questa sezione appare all'interno dello schermo di **Corrispondenza dell'Ordine di Acquisto** quando la funzionalità è abilitata.

## **Come Abilitare**

Per attivare questa funzionalità:

1. Vai su **Impostazioni** → **Modulo**.
2. Apri la sezione **Ordine di acquisto** (*Corrispondenza e convalida degli ordini di acquisto*).
3.  Abilita l'opzione **PO Ordine di spedizione**.

    <div align="left"><figure><img src="../../../../.gitbook/assets/po-shipment-order-module-setting-it.png" alt="Sezione Ordine di acquisto in Impostazioni → Modulo con l'interruttore PO Ordine di spedizione" width="563"><figcaption><p>Impostazioni → Modulo → Ordine di acquisto</p></figcaption></figure></div>

La stessa sezione contiene altri due interruttori: **Cruscotto PO** aggiunge alla navigazione un cruscotto degli ordini di acquisto, mentre **Cruscotto dell'ordine di spedizione** aggiunge un cruscotto che elenca le consegne in arrivo per singola riga dell'ordine di acquisto.

## **Dove Appare**

Una volta abilitata, la sezione PO Ordine di spedizione diventa visibile nell'interfaccia di Corrispondenza dell'Ordine di Acquisto.

![](https://docs.docbits.com/~gitbook/image?url=https%3A%2F%2F578966019-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FT2n2w4uDCJvv7CJ5zrdk%252Fuploads%252F2R9tB3JySdIMk8meRSVZ%252FPO-Shipment-Order-1.jpg%3Falt%3Dmedia%26token%3D70aa50f4-84cd-4a55-b580-037b893d1f5b\&width=768\&dpr=4\&quality=100\&sign=e4619335\&sv=2)

### **PO Ordine di spedizione – Descrizioni dei Campi**

* **ID Articolo** Identifica l'articolo specifico nell'ordine di acquisto.
* **Numero di Consegna** Numero di riferimento per la spedizione o consegna.
* **Quantità Spedita** Quantità che è stata consegnata o ricevuta.
* **Quantità Fatturata** Quantità che è già stata fatturata.
* **Quantità Aperta in Fattura** Quantità ancora aperta per la fatturazione (calcolata come _Quantità Spedita - Quantità Fatturata_).
* **Barra di Avanzamento e Percentuale**
  * Mostra quanto della quantità spedita è stata abbinata alle fatture.
  * Parte dal 0% per i nuovi PO.
  * Si aggiorna cumulativamente attraverso più fatture.
  * Riflette il progresso totale degli articoli fatturati rispetto a quelli spediti.
* **Data di Consegna Promessa** La data di consegna prevista per l'articolo dell'ordine di acquisto.
*   **Indicatore di Ritardo**

    Mostra il numero di giorni di ritardo della consegna in base alla **Data di Consegna Promessa**.
