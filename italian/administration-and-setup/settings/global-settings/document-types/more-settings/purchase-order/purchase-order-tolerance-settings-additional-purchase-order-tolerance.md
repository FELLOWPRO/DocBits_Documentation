# Impostazioni di tolleranza per gli ordini di acquisto / Ulteriore tolleranza per gli ordini di acqui

### **Impostazione per configurare le tolleranze degli ordini di acquisto**

Vai a **Impostazioni → Impostazioni generali → Tipi di documento → Ulteriori impostazioni → Sezione Ordine di acquisto → Impostazione tolleranza PO**

#### **Come funziona**

Quando abilitata, questa impostazione consente di definire tolleranze per **Quantità** e/o **Prezzo unitario**. Queste tolleranze possono essere impostate sia come percentuale che come valore fisso. Ciò significa che una fattura può discostarsi dall'ordine di acquisto (PO) all'interno dell'intervallo di tolleranza specificato senza essere segnalata come una discrepanza, fornendo flessibilità pur garantendo un'elaborazione senza problemi.

<mark style="color:red;">**NOTA**</mark>: Le tolleranze funzionano in entrambe le direzioni; cioè, il valore della fattura può essere sia superiore che inferiore al valore del PO all'interno dell'intervallo consentito.

#### **Configurazione**

* **Abilita l'impostazione:**
  * Attiva l'impostazione tolleranza PO utilizzando il pulsante di attivazione.
* **Configura le tolleranze:**
  * Appariranno quattro campi:
    * Un campo per l'**Importo della tolleranza sulla quantità**.
    * Un campo per l'**Importo della tolleranza sul prezzo unitario**.
  * Dietro ciascun campo, c'è un menu a discesa dove puoi selezionare il tipo di tolleranza:
    * **Percentuale:** Indica una tolleranza percentuale.
    * **Valore:** Indica un importo fisso con cui il valore può differire.

<figure><img src="../../../../../../.gitbook/assets/docbits_purchase_order_table.png" alt="DocBits Acquisto Ordine Tabella"><figcaption></figcaption></figure>

#### **Scenario di esempio:**

* Supponiamo che la **Tolleranza sul prezzo unitario** sia impostata al **5%**.
* L'ordine di acquisto include due righe:
  * **Riga 1:** Prezzo unitario = **$5.00**
  * **Riga 2:** Prezzo unitario = **$2.00**
* Sulla fattura:
  * **Riga 1:** Il prezzo unitario è stato regolato a **$4.80** (**all'interno** della tolleranza del 5%).
  * **Riga 2:** Il prezzo unitario è stato regolato a **$2.20** (**fuori** dalla tolleranza del 5%).
* **Risultato:**
  * La riga 1 **non è segnalata** come una discrepanza perché $4.80 è all'interno del 5% di $5.00.
  * La riga 2 **è segnalata** come una discrepanza perché $2.20 supera la deviazione consentita del 5% da $2.00. L'utente è ora tenuto a prendere provvedimenti per risolvere la discrepanza prima che la fattura possa essere elaborata ulteriormente.

<figure><img src="../../../../../../.gitbook/assets/docbits_po_tolerance_mismatch_example_it.jpg" alt="Docbits Po Tolerance Mismatch Example It"><figcaption></figcaption></figure>

### Impostazione per configurare le ulteriori impostazioni di tolleranza per gli ordini di acquisto

Vai a **Impostazioni → Impostazioni generali → Tipi di documento → Ulteriori impostazioni → Sezione Ordine di acquisto → Impostazione tolleranza PO aggiuntiva**

#### **Come funziona**

Quando abilitata, questa impostazione consente di definire tolleranze per **Spese di trasporto**, **Costi** e/o **Tasse**. Queste tolleranze possono essere impostate sia come percentuale che come valore fisso, consentendo alle fatture di variare leggermente dai valori del PO senza essere segnalate come discrepanze. Questo fornisce ulteriore flessibilità e garantisce che le piccole differenze non interrompano il flusso di lavoro.

<mark style="color:red;">**NOTA**</mark>: Proprio come le impostazioni di tolleranza standard, queste tolleranze si applicano in entrambe le direzioni, consentendo aumenti o diminuzioni all'interno dei limiti stabiliti.

#### **Configurazione**

* **Abilita l'impostazione:**
  * Attiva l'impostazione aggiuntiva di tolleranza PO utilizzando il pulsante di attivazione.
* **Configura le tolleranze:**
  * Sei campi diventeranno visibili:
    * Un campo ciascuno per gli importi di tolleranza per **Spese di trasporto**, **Costi** e **Tasse**.
  * Ogni campo ha un menu a discesa associato dove puoi scegliere il tipo di tolleranza:
    * **Percentuale:** La tolleranza è definita come una percentuale.
    * **Valore:** La tolleranza è definita come un importo fisso.

<figure><img src="../../../../../../.gitbook/assets/docbits_approval.png" alt="DocBits Approvazione"><figcaption></figcaption></figure>
