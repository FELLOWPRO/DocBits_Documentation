# Fornitori e Ordini di Acquisto

## **Punto di Connessione**

È necessario creare il punto di connessione API di DocBits per poter creare successivamente il flusso di dati.

Innanzitutto, in InforOS, vai su ION Desk → Connetti → Punti di Connessione

![](https://lh7-us.googleusercontent.com/852EogukgFvteFTdg6_a6MPLaBUUqDw1J4x4H2q9BMjaVzZIGlpASC_fImhvAxe-nPBvIvOPFTI0oG8D3RlkAHiFDbLsVrsjaJMD1B5otXyIzPDkvoJvrj-JvMEHao73jgcZ5aKLAP4fCpkP7XV08JE)

Una volta qui, sarà necessario creare un nuovo punto di connessione.

![](https://lh7-us.googleusercontent.com/eh1NyUDTS0k-59ePv89PjZpfh5IT0iyFPoV5M9xmo3fmai-Iz0ptQFXgI9onZM-sTICHii32MkAw22AhZZAT5iKs_Hjw3_NDT49XG_KRONAvyK4OuL-bX667F9UGr-juckRmcE2hATOkSQ5x8QlugxU)

**Seleziona API**

Assegna al punto di connessione un nome e una descrizione che ne descriva la natura e l'ambiente. Nella scheda Connessione, importa l'account di servizio che hai creato per l'ambiente con cui stai lavorando.

![](https://lh7-us.googleusercontent.com/WZKJSckXWzztmEHmySnz6oDSbgFDvPmxku48HCiDJn7O1vTUcpUBYnwDHMT_Ja8aSGd8sFm-YQQYzyn5DnYLw77PQeFwTxcOV6C9aPWHyj2VofevH4S6ciyduIUy5YaNvmuNV6WgVJKOZ89_6oJjuq0)

Passa quindi alla scheda Documenti. Dovrai aggiungere i seguenti BOD al punto di connessione.

![](https://lh7-us.googleusercontent.com/3Q4XIpxXLixaDqXhh7CRKPl0yUwBce34CqLfw0BGS1UFXsvFIaxD6XelEgbnwfYFUCa5En-C1oAZR74C4lQ15as_M7JIQ20Nf9ZVmrVK8zCGuLS2YtphX4bgQ5uOwS2-MJLLZvsflDC31XLrTZzTKCg)

* Ack-SupplierInvoice

Questo BOD viene utilizzato per segnalare su DocBits che si è verificato un errore in Infor. La configurazione per questi due BOD dovrebbe essere simile alla seguente (il nome della chiamata API cambia per ciascuno)

![](https://lh7-us.googleusercontent.com/vmcVsltij144O3NeysAS2YduFNds98X_VJOpn6v356vAZI3v10SO8-ZMBd7zWyBUJKR9-UMQgGcT2U34HdGgpQ8rhtbFxsmuhgwJ_K6qXbtu04AP67G8jrNwkdj32LCgAhy_m4tnFQJApQehnfX8w5Y)

* Sync.PurchaseOrder

La configurazione per questo BOD dovrebbe essere simile alla seguente

![](https://lh7-us.googleusercontent.com/LPmOwFuzOnYNjwcKDfpI2S-IYJPKhjHYy4xKSUtB7EXSmPGfnG1lDfR-q6fdk4Uh9QBr-PIWjkpW3clbq31z8BP4_CGgoryKguS4GhR44gCG8xt6FJxRvqV-1i5Ul_3-wFjmiroYcchb5Ou5wBA0DF0)

* Sync.ReceiveDelivery

La configurazione per questo BOD dovrebbe essere simile alla seguente

![](https://lh7-us.googleusercontent.com/75TPWASsqnzrWdeoyHZ4T23Zm5DbctQLOZKVe4N05ni32ecs0kZmBAihWnr7j0J7TisLvF2lncmUbEGGF9dKz8glVcRe7pmCvmEx8TMTesh0zGeewNpveNIsQqw-gkHvcITTF4a067MhoMgY8Jp6Prc)

Una volta configurati questi BOD, puoi salvare il punto di connessione premendo l'icona situata a destra del pulsante indietro.

## **Flusso dei Dati**

Il flusso dei dati sarà simile al seguente

![](https://lh7-us.googleusercontent.com/yhSunSyXrzx2Q0VIulIa6b989LxG36g5-kyYXGwniU0okKb3cJWDe65GYhpOfkHWTYJR4xdT85Us2Ba7tHhoJsE51I-g-82ZQ2bRM5zkgF5VmaRSno8M5bfhMCbUAw4-xx5oEudkqZWYoeIUUYhJPDU)

(Il motivo per cui sono presenti più API di DocBits è dovuto al fatto che ogni connessione rappresenta un ambiente diverso, il che significa che, a seconda del numero di ambienti che hai, il tuo flusso di dati potrebbe differire leggermente)

Per lo scopo di questa spiegazione, useremo l'esempio di avere quattro ambienti separati.

### **LN**

L'inizio del flusso di dati consiste nella tua applicazione LN

### **API di DocBits**

Qui aggiungerai un'applicazione e selezionerai le API di DocBits che hai creato in precedenza

### **File**

La configurazione dovrebbe apparire come segue

![](https://lh7-us.googleusercontent.com/OEG6wQFd9LT6J_Ttcsdj7GgM2bTxrS-dpO2EbcVx4vGH1NLtZyaRTbYnr4-SDIWL2hk1zeVGr3bjuebNmwAMEx0S0U7xmNGztp-8HVjRLYyc-3lbQBL8lDU_TahhNxBugX_Bnu3QjZsKHX0Pafae-zU)

## **Attivazione BOD di LN**

Una volta completato tutto quanto sopra, sarà necessario navigare su Infor LN e attivare i BOD per consentire ai vari dati principali necessari per Fornitori e Ordini di Acquisto di arrivare in DocBits.

![](https://lh7-us.googleusercontent.com/b6IsSx-x5Ri0cfYU9TTpgipqsoCkDPTxXdKoMBPaumyaopp-NRAJhoNnBfksnVVdz9Y26M0KlfdcKP4S1n_PjcTYKIu3MbVMQIfuIaTYYAL2ctyYsp29mEOrVh2TxmLPkUofeqJQ8nvBQbTOwj0-V0Y)

### **Ordine di Acquisto**

Dal menu sopra, nella scheda del menu di sinistra, seleziona Comune → Messaggistica BOD → Pubblica BOD → Pubblica Dati Transazionali di Gestione Ordini

Seleziona la scheda Ordine di Acquisto e spunta la casella.

![](https://lh7-us.googleusercontent.com/UJlicSuDjbEVtr_pzOeqkP8kkiBJIdAgzPK46FlhubqIIHiaJRYp27B__08e9IcNHdcctrBeBfZ6vFPQI3Xf3duL6R2Hu-iaL9dY7hANmy8ukiL61CTxcel0jd_66GAySp3dC1ptYKBaqLqaP1TwJco)
### **Fornitori**

Dalla homepage di LN, nel menu di sinistra, vai su Comune → BOD-Messaging → Pubblica BOD → Pubblica Dati Master Logistica

Seleziona la scheda PartyMaster e spunta la casella Fornitore → Acquista-da o SupplierPartyMaster.

![](https://lh7-us.googleusercontent.com/KY_cFaUegEZmqAlcsBLVOTaxKOkkBkMeaQUbv996H946oOa-jvxB3lDqrkWV-17elt0mZDGews6Lr_6ojbFXtReDnV1PmqzwLXfE-IX5fKJr2IeJkAdnf1R9Sk5WYoxOLGolgo2MPQ3SNeoPnQ-ysy0)

### **Attivazione BOD**

Una volta selezionati tutti i BOD corretti per la pubblicazione, seleziona la scheda Opzioni.

Dovrebbero essere selezionate le seguenti opzioni.

![](https://lh7-us.googleusercontent.com/7KpYALL1XL0pqWLRCPFng8-WT8IWI4o9lEtrp2zAN5bOBnYdz-6EHfAPc_StaY9raJTWbfrksra9UUxyQAQdtg4nOZggpHox3AV3C_cL9xhDAdHV4n79yyCfbyGH2NmS30fQGfsLTe_4_tXKy54nI8U)

Una volta completato, premi il pulsante PROCESS e i BOD saranno attivati. Comparirà un messaggio a schermo per notificare che i BOD sono stati attivati.

![](https://lh7-us.googleusercontent.com/BPX5vIBHIFv641srJPwW-19Dx1N1T2QnadGwVMQu-6pBZUxnUdOjdY1olMqorIyN_oeTBqz_1knMoYsSxEA-_NtGVx_j9dBixvOfic8rKJDT91tYqwSSLNpk8YkMW8ndelpH9_fzrTZUCMs_vnoxbvM)

Se eseguito con successo, le tabelle Fornitore e Ordine di Acquisto dovrebbero ora essere disponibili in Impostazioni → Ricerca Dati Master.
