# Fornitori e ordini di acquisto da Infor LN

Questo esempio descrive la rotta Infor ION per i BOD di fornitori e ordini di acquisto e dove verificarli in DocBits. Le quattordici schermate Infor riportate sotto sono esempi storici di un tenant. Verifica punti di connessione, nomi delle chiamate API e opzioni di pubblicazione LN con l'amministratore dell'integrazione; non sono state controllate in un tenant Infor per questo aggiornamento. Durante questo aggiornamento non è stato pubblicato né importato alcun BOD.

Infor descrive il [publisher dei dati anagrafici logistici LN](https://docs.infor.com/ln/latest/en-us/lnolh/tcolh/help/tc/bod/tcbod0200m000.html) e il [publisher transazionale di Order Management](https://docs.infor.com/ln/2025.x/en-us/lnolh/tdolh/help/td/bod/tdbod0200m000.html). Le loro modalità hanno effetti diversi: **Count** riporta i totali dei record senza pubblicare; **Simulate** genera un risultato di prova senza confermare la pubblicazione; **Publish** invia i dati selezionati. La pubblicazione può raggiungere tutti i sottoscrittori, quindi controlla l'intervallo di società e i sottoscrittori prima di eseguirla.

## **Punto di connessione**

Dovrai creare il connection point DocBits API per poter creare successivamente il data flow.

Per prima cosa, in InforOS, vai su ION Desk → Connect → Connection Points

<figure><img src="https://lh7-us.googleusercontent.com/852EogukgFvteFTdg6_a6MPLaBUUqDw1J4x4H2q9BMjaVzZIGlpASC_fImhvAxe-nPBvIvOPFTI0oG8D3RlkAHiFDbLsVrsjaJMD1B5otXyIzPDkvoJvrj-JvMEHao73jgcZ5aKLAP4fCpkP7XV08JE" alt="Navigazione storica di Infor ION Desk con Connect espanso e Connection Points evidenziato."><figcaption><p>Esempio di navigazione storico: ION Desk → Connect → Connection Points.</p></figcaption></figure>

Una volta qui, dovrai creare un nuovo connection point.

<figure><img src="https://lh7-us.googleusercontent.com/eh1NyUDTS0k-59ePv89PjZpfh5IT0iyFPoV5M9xmo3fmai-Iz0ptQFXgI9onZM-sTICHii32MkAw22AhZZAT5iKs_Hjw3_NDT49XG_KRONAvyK4OuL-bX667F9UGr-juckRmcE2hATOkSQ5x8QlugxU" alt="Schermata storica Connection Points con una freccia verde che indica Add."><figcaption><p>Scegli Add per creare un connection point; l'annotazione verde segnala l'azione in questa interfaccia storica.</p></figcaption></figure>

**Seleziona API**

Assegna al connection point un nome e una descrizione che ne indichino la natura e l'ambiente. Nella scheda Connection, importa il service account che hai creato per l'ambiente con cui stai lavorando.

<figure><img src="https://lh7-us.googleusercontent.com/WZKJSckXWzztmEHmySnz6oDSbgFDvPmxku48HCiDJn7O1vTUcpUBYnwDHMT_Ja8aSGd8sFm-YQQYzyn5DnYLw77PQeFwTxcOV6C9aPWHyj2VofevH4S6ciyduIUy5YaNvmuNV6WgVJKOZ89_6oJjuq0" alt="Connection point API storico DocBits-DEV-Demo-Import con Connection selezionato e un controllo Import del service account."><figcaption><p>Scheda Connection storica. I nomi del service account e della connessione mostrati appartengono all'ambiente di esempio.</p></figcaption></figure>

Quindi passa alla scheda Documents. Dovrai aggiungere al connection point i seguenti BOD.

<figure><img src="https://lh7-us.googleusercontent.com/3Q4XIpxXLixaDqXhh7CRKPl0yUwBce34CqLfw0BGS1UFXsvFIaxD6XelEgbnwfYFUCa5En-C1oAZR74C4lQ15as_M7JIQ20Nf9ZVmrVK8zCGuLS2YtphX4bgQ5uOwS2-MJLLZvsflDC31XLrTZzTKCg" alt="Scheda Dokumente (Documents) storica in tedesco con le chiamate API Ack-SupplierInvoice, Sync.PurchaseOrder e Sync.ReceiveDelivery e i BOD ricevuti."><figcaption><p>Scheda Dokumente (Documents) storica. Questo ritaglio mostra tre rotte; non mostra la configurazione completa dei fornitori.</p></figcaption></figure>

* Ack-SupplierInvoice

Questo BOD serve a segnalare a DocBits che in Infor si è verificato un errore. La rotta Acknowledge.SupplierInvoice mostrata sotto è un esempio di conferma delle fatture. Verifica il nome della chiamata API e se questa rotta è necessaria per il tuo flusso fornitori e ordini di acquisto.

<figure><img src="https://lh7-us.googleusercontent.com/vmcVsltij144O3NeysAS2YduFNds98X_VJOpn6v356vAZI3v10SO8-ZMBd7zWyBUJKR9-UMQgGcT2U34HdGgpQ8rhtbFxsmuhgwJ_K6qXbtu04AP67G8jrNwkdj32LCgAhy_m4tnFQJApQehnfX8w5Y" alt="Scheda ION API storica in tedesco per Ack-SupplierInvoice con un'operazione POST selezionata."><figcaption><p>Rotta di conferma storica. Ack-SupplierInvoice è un nome di chiamata API di esempio; Acknowledge.SupplierInvoice è il BOD ricevuto.</p></figcaption></figure>

* Sync.PurchaseOrder

L'esempio storico sotto mostra un'operazione di ricezione; verifica l'operazione e il formato della richiesta attuali per il tuo ambiente.

<figure><img src="https://lh7-us.googleusercontent.com/LPmOwFuzOnYNjwcKDfpI2S-IYJPKhjHYy4xKSUtB7EXSmPGfnG1lDfR-q6fdk4Uh9QBr-PIWjkpW3clbq31z8BP4_CGgoryKguS4GhR44gCG8xt6FJxRvqV-1i5Ul_3-wFjmiroYcchb5Ou5wBA0DF0" alt="Scheda ION API storica con Send to API selezionato per Sync.PurchaseOrder e un'operazione POST configurata."><figcaption><p>Rotta storica degli ordini di acquisto. Verifica l'operazione di ricezione del tuo ambiente DocBits invece di copiare il vecchio percorso del proxy.</p></figcaption></figure>

* Sync.ReceiveDelivery

L'esempio storico sotto mostra un'operazione di ricezione; verifica l'operazione e il formato della richiesta attuali per il tuo ambiente.

<figure><img src="https://lh7-us.googleusercontent.com/75TPWASsqnzrWdeoyHZ4T23Zm5DbctQLOZKVe4N05ni32ecs0kZmBAihWnr7j0J7TisLvF2lncmUbEGGF9dKz8glVcRe7pmCvmEx8TMTesh0zGeewNpveNIsQqw-gkHvcITTF4a067MhoMgY8Jp6Prc" alt="Scheda ION API storica in tedesco per Sync.ReceiveDelivery con un'operazione POST configurata."><figcaption><p>Rotta storica dei dati di ricezione. Verifica se ReceiveDelivery è necessario per la tua integrazione e quale operazione lo riceve.</p></figcaption></figure>

Una volta configurati questi BOD, puoi salvare il connection point premendo l'icona situata a destra del pulsante Indietro.

## **Flusso di dati**

Il data flow avrà un aspetto simile al seguente

<figure><img src="https://lh7-us.googleusercontent.com/yhSunSyXrzx2Q0VIulIa6b989LxG36g5-kyYXGwniU0okKb3cJWDe65GYhpOfkHWTYJR4xdT85Us2Ba7tHhoJsE51I-g-82ZQ2bRM5zkgF5VmaRSno8M5bfhMCbUAw4-xx5oEudkqZWYoeIUUYhJPDU" alt="Flusso documentale storico da un nodo LN attraverso una divisione parallela verso quattro nodi DocBits API, seguita da una giunzione e dal nodo End."><figcaption><p>Flusso storico con quattro ambienti. La divisione e la giunzione sono visibili; il numero e le destinazioni dei nodi dipendono dal tuo progetto di integrazione.</p></figcaption></figure>

I diversi nodi DocBits API di questo esempio storico rappresentano ambienti separati. Il tuo progetto di produzione può usare un numero diverso di nodi; non instradare mai dati di test in un'organizzazione di produzione.

L'illustrazione seguente usa quattro ambienti solo come esempio.

### **LN**

L'inizio del data flow è costituito dalla tua applicazione LN

### **DocBits API**

Qui aggiungerai un'applicazione e selezionerai le DocBits API create in precedenza

### **Documenti**

Controlla l'elenco dei documenti assegnati al flusso. Anche i messaggi dei fornitori mostrati qui richiedono rotte di ricezione corrispondenti nel connection point API. La configurazione delle loro chiamate API non è visibile nel ritaglio delle tre rotte precedente; verifica con l'amministratore dell'integrazione quali operazioni sono necessarie.

<figure><img src="https://lh7-us.googleusercontent.com/OEG6wQFd9LT6J_Ttcsdj7GgM2bTxrS-dpO2EbcVx4vGH1NLtZyaRTbYnr4-SDIWL2hk1zeVGr3bjuebNmwAMEx0S0U7xmNGztp-8HVjRLYyc-3lbQBL8lDU_TahhNxBugX_Bnu3QjZsKHX0Pafae-zU" alt="Area di disegno storica del flusso con il pannello Dokumente in tedesco sotto, che elenca Sync.PurchaseOrder, Sync.ReceiveDelivery, Sync.RemitToPartyMaster e Sync.SupplierPartyMaster."><figcaption><p>Elenco documenti storico del flusso. I messaggi dei fornitori compaiono qui insieme ai messaggi degli ordini di acquisto e delle ricezioni.</p></figcaption></figure>

## **Attivazione dei BOD in LN**

Dopo che l'amministratore dell'integrazione ha controllato il connection point, le rotte dei documenti e il data flow attivo, usa la sessione di pubblicazione LN adatta. Segui ogni identificatore di test attraverso LN, ION e DocBits; attivare un BOD da solo non dimostra che un record sia arrivato.

<figure><img src="https://lh7-us.googleusercontent.com/b6IsSx-x5Ri0cfYU9TTpgipqsoCkDPTxXdKoMBPaumyaopp-NRAJhoNnBfksnVVdz9Y26M0KlfdcKP4S1n_PjcTYKIu3MbVMQIfuIaTYYAL2ctyYsp29mEOrVh2TxmLPkUofeqJQ8nvBQbTOwj0-V0Y" alt="Home page storica di Infor LN in tedesco con un elenco di preferiti; il menu Publish BODs non è aperto."><figcaption><p>Pagina iniziale LN storica. Usa la navigazione descritta sotto per trovare la sessione di pubblicazione adatta.</p></figcaption></figure>

### **PurchaseOrder**

Dal menu precedente, nella scheda del menu a sinistra, seleziona Common → BOD-Messaging → Publish BODs → Publish Order Management Transactional Data

Seleziona la scheda PurchaseOrder e spunta la casella.

<figure><img src="https://lh7-us.googleusercontent.com/UJlicSuDjbEVtr_pzOeqkP8kkiBJIdAgzPK46FlhubqIIHiaJRYp27B__08e9IcNHdcctrBeBfZ6vFPQI3Xf3duL6R2Hu-iaL9dY7hANmy8ukiL61CTxcel0jd_66GAySp3dC1ptYKBaqLqaP1TwJco" alt="Sessione storica Publish Order Management Transactional Data con la scheda PurchaseOrder e la casella selezionate e i campi dell'intervallo ordini visibili."><figcaption><p>Selezione PurchaseOrder storica. Controlla l'intervallo ordini e gli stati prima di pubblicare.</p></figcaption></figure>

### **Fornitori**

Dalla home page di LN, nella scheda del menu a sinistra, vai su Common → BOD-Messaging → Publish BODs → Publish Logistics Master Data

Seleziona la scheda PartyMaster e spunta la casella Supplier → Buy-from oppure SupplierPartyMaster.

<figure><img src="https://lh7-us.googleusercontent.com/KY_cFaUegEZmqAlcsBLVOTaxKOkkBkMeaQUbv996H946oOa-jvxB3lDqrkWV-17elt0mZDGews6Lr_6ojbFXtReDnV1PmqzwLXfE-IX5fKJr2IeJkAdnf1R9Sk5WYoxOLGolgo2MPQ3SNeoPnQ-ysy0" alt="Sessione storica Publish Logistic Master Data con PartyMaster selezionato e la casella Supplier Buy-from spuntata."><figcaption><p>Selezione dei fornitori storica in PartyMaster. Scegli i ruoli partner richiesti dalla tua integrazione e controlla l'intervallo di selezione.</p></figcaption></figure>

### **Attivazione dei BOD**

Dopo aver spuntato per la pubblicazione tutti i BOD corretti, seleziona la scheda Options.

Controlla le opzioni del tuo tenant. L'esempio storico evidenzia Publish e Use Process/Sync Verb; non sono impostazioni valide per ogni integrazione.

<figure><img src="https://lh7-us.googleusercontent.com/7KpYALL1XL0pqWLRCPFng8-WT8IWI4o9lEtrp2zAN5bOBnYdz-6EHfAPc_StaY9raJTWbfrksra9UUxyQAQdtg4nOZggpHox3AV3C_cL9xhDAdHV4n79yyCfbyGH2NmS30fQGfsLTe_4_tXKy54nI8U" alt="Scheda Options storica di LN con Publish e Use Process/Sync Verb evidenziati e un intervallo di società visibile."><figcaption><p>Esempio storico della scheda Options. Qui sono selezionati Publish e Use Process/Sync Verb; verifica modalità, intervallo di società e sottoscrittori per la tua esecuzione.</p></figcaption></figure>

Prima di **Process**, usa **Count** o **Simulate** e controlla il numero di record e l'intervallo di società, se la tua versione di LN offre queste modalità. Pubblica solo con l'approvazione dell'amministratore dell'integrazione. Una conferma che i BOD sono stati attivati non dimostra la consegna a DocBits.

<figure><img src="https://lh7-us.googleusercontent.com/BPX5vIBHIFv641srJPwW-19Dx1N1T2QnadGwVMQu-6pBZUxnUdOjdY1olMqorIyN_oeTBqz_1knMoYsSxEA-_NtGVx_j9dBixvOfic8rKJDT91tYqwSSLNpk8YkMW8ndelpH9_fzrTZUCMs_vnoxbvM" alt="Scheda Options storica di LN con il pulsante Process evidenziato prima dell'esecuzione."><figcaption><p>Azione Process storica prima dell'esecuzione. Questa schermata non contiene alcun risultato di pubblicazione né la conferma che DocBits abbia ricevuto i dati.</p></figcaption></figure>

## Verifica in DocBits

Controlla in Infor ION che la consegna all'organizzazione DocBits prevista sia riuscita. Apri quindi **Impostazioni → Elaborazione documenti → Ricerca di dati anagrafici**. In **Dati di ingresso BOD** apri **Fornitore**. Scegli il campo identificativo in **Ricerca per colonna**, inserisci in **Ricerca Stringa** un numero o un nome di fornitore noto e usa la lente per cercare. Apri **Ordine di acquisto** e cerca un numero d'ordine noto. Controlla anche **Intestazione dell'ordine di acquisto** se la tua mappatura separa intestazione e righe. Confronta gli identificatori e la società con LN; non dedurre che tutti i record siano arrivati solo perché il messaggio di pubblicazione è andato a buon fine. Nell'interfaccia italiana le intestazioni di colonna della tabella restano in inglese, ad esempio Supplier Id e Supplier Name.

<figure><img src="../../../../.gitbook/assets/dbdc-1146-supplier-it-20261112.png" alt="Vista Fornitore di Ricerca di dati anagrafici in DocBits in italiano con i campi Ricerca per colonna e Ricerca Stringa e dieci righe fornitore di esempio inventate da SUP-1001 a SUP-1010."><figcaption><p>Vista di verifica dei fornitori nella versione 11.27.7 del sandbox con righe di esempio inventate. Cerca un identificatore di test noto e confrontalo con LN e ION.</p></figcaption></figure>

<figure><img src="../../../../.gitbook/assets/dbdc-1146-purchase-order-it-20261112.png" alt="Vista Ordine di acquisto di Ricerca di dati anagrafici in DocBits in italiano con le schede Fornitore e Ordine di acquisto, gli stessi campi di ricerca e dieci righe d'ordine di esempio inventate da PO-4500 a PO-4509."><figcaption><p>Vista di verifica degli ordini di acquisto nella versione 11.27.7 del sandbox con righe di esempio inventate. Le righe non dimostrano alcuna importazione da LN.</p></figcaption></figure>

Le viste inglesi in Dev sono state controllate il 29 ottobre 2026 senza pubblicare BOD, importare file o modificare dati anagrafici; in quelle immagini le righe dei record erano escluse. Le due schermate in italiano provengono dalla versione 11.27.7 del sandbox e mostrano righe di esempio inventate al posto di dati anagrafici reali; illustrano dove verificare, non un trasferimento da LN completato. Se il record atteso manca, controlla i log di pubblicazione LN, l'instradamento ION, l'organizzazione e la mappatura dei BOD prima di riprovare.
