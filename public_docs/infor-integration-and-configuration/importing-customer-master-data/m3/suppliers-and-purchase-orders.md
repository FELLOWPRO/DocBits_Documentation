# Fornitori e ordini di acquisto da Infor M3

Questo esempio collega i BOD dei fornitori e degli ordini di acquisto di M3 a DocBits tramite Infor ION. Le quindici immagini Infor riportate di seguito sono esempi storici di un ambiente cliente e non dimostrano che la tua configurazione M3 funzioni attualmente. Il tuo amministratore Infor deve confermare i nomi dei BOD, le tabelle di origine, la società, la divisione, i nomi delle chiamate API e l'ambiente di destinazione prima di avviare un job. Per questo aggiornamento non è stato eseguito alcun caricamento iniziale M3 e nessun import in DocBits.

La [guida al caricamento iniziale di Infor](https://docs.infor.com/m3udi/16.x/en-us/m3beud/appfoundhs/spl1567531742751.html) spiega le definizioni in EVS006, il verbo e la selezione in EVS007, l'invio e il registro storico. Iniziare con una selezione limitata; un'esecuzione senza restrizioni può generare molti eventi.

## **Punto di connessione**

Per creare in seguito il flusso di dati è necessario creare il punto di connessione DocBits API.

In InforOS, andare su ION Desk → Connect → Connection Points

<figure><img src="https://lh7-us.googleusercontent.com/ySRjNzMXFzwSOYKx9hnlKLPHPuXpmfTvRADBfV6cpT8ajiEUbS4oXpd9InhXG09mHLakhqBTJMH4yQJNG5z9RXmbAjh8YbuGhxnXSeooIH_r3RAGOvJE6Ok67ST_272zFfhB_TTFYg3b-NwFq0CAv2o" alt="Navigazione storica in ION Desk con il gruppo Connect espanso e la voce Connection Points evidenziata."><figcaption><p>Navigazione storica: ION Desk → Connect → Connection Points.</p></figcaption></figure>

Una volta arrivati qui, occorre creare un nuovo punto di connessione.

<figure><img src="https://lh7-us.googleusercontent.com/ZDv-F3iayFqnsvVLlAE1kr0NNncsvuYtzcE_WQj-0ONoE7McRl-f6_DDH9ErQ0KLspZFFJ43t5EfnPBJjVg25YISMEQ--X4MmK6SVWzB60-Fq6mtwdhiOBwSnL-8vASXsto9iab0dnve6eeG8yuqNoI" alt="Pagina Connection Points storica con una freccia verde che punta alla voce Add."><figcaption><p>Azione Add storica per creare un punto di connessione.</p></figcaption></figure>

**Selezionare API**

Assegnare al punto di connessione un nome e una descrizione che ne descrivano la natura e l'ambiente. Nella scheda Connection, importare l'account di servizio creato per l'ambiente con cui si sta lavorando.

<figure><img src="https://lh7-us.googleusercontent.com/UCuGTwKARn3auhYdDDUbQ78Ok3qBNE1KpGEMealfPvgRju4VRLn2AfKaL5tLDcAh00poLHNQU-Q6koBhG5RdxK4CJrrL6Qeb4D52qnhw3aG1LZniuzHRXwOyzGcJvRnQtLGbp6PIseXvWxHlk-AMlz0" alt="Punto di connessione storico DocBits-DEV-Demo-Import con la scheda Connection selezionata e un controllo Import dell'account di servizio."><figcaption><p>Scheda Connection storica. I nomi mostrati si riferiscono all'ambiente di esempio; usare il proprio account di servizio.</p></figcaption></figure>

Passare quindi alla scheda Documents. Al punto di connessione vanno aggiunti i seguenti BOD: non tutti servono per i dati anagrafici di fornitori e ordini di acquisto, ma saranno utili quando si implementano altre funzioni come la contabilità automatica.

<figure><img src="https://lh7-us.googleusercontent.com/25Hizkx23i1c8-QHSrE7mPAH7zW6ux9iHTcP8_l6EJJy548CvuNPF1R86Fuqx5iYZP9HF-Z4G6hntkaUtlOMetHIzAVZyBM6VIQ-vsvy6P5YBuAj4yscdJe8ySOHwIRQwFpShRiFGC83v467LLBaXq8" alt="Scheda Documents storica con i BOD Acknowledge.SupplierInvoice, Sync.ChartOfAccounts, Sync.PurchaseOrder, Sync.RemitToPartyMaster e Sync.SupplierPartyMaster."><figcaption><p>Elenco storico dei documenti ricevuti. Il BOD fornitore mostrato è Sync.RemitToPartyMaster, senza il suffisso Data.</p></figcaption></figure>

Questa configurazione storica usa Sync.RemitToPartyMaster, Sync.SupplierPartyMaster e Sync.PurchaseOrder. Confermare quali BOD richiede la mappatura DocBits; la configurazione può variare in base all'ambiente e alla funzione.

* Sync.RemitToPartyMaster e Sync.SupplierPartyMaster

L'immagine storica seguente mostra Sync.SupplierPartyMaster. Configurare ogni BOD fornitore necessario con il nome della chiamata API e l'operazione di ricezione confermati per il proprio ambiente; la seconda rotta fornitore non è raffigurata.

<figure><img src="https://lh7-us.googleusercontent.com/1SeyL73b7K9vxkTzKk-pumRleoY1sx9MVwgEBMZ-oUf6GXG2C7fKIRMbnhWHHhIQhUDBS3oKQidrQIN08FZ_7eKEt1Yp0cRqnsDlv1R5ShdZdNKmaXmU_19DAVtiT3U0m2qm4cBOj9FcnT0eyawfJXk" alt="Scheda ION API storica con Send to API selezionato, API Call Name Sync.SupplierPartyMaster e operazione POST."><figcaption><p>Rotta SupplierPartyMaster storica. L'immagine mostra una rotta fornitore; confermare separatamente l'operazione di ricezione per ogni BOD richiesto.</p></figcaption></figure>

* Sync.PurchaseOrder

L'immagine storica seguente mostra un'operazione di ricezione degli ordini di acquisto. Confermare l'endpoint attuale e il formato della richiesta per il proprio ambiente.

<figure><img src="https://lh7-us.googleusercontent.com/ljXpQxwepI3u6kcITZfACV9yYL1ZZZtBbWimkXW6aWFTI-yd7Gajrxw2pwxdcF1Xv3KoGDalq72yXvaipjQ-OmbcTzJ0PUUKnmE0pBa5pASEPg0amqKSbU82ZDOKr5alWXynAd53IM2i9HgZ1CsYIB4" alt="Scheda ION API storica con Send to API selezionato per Sync.PurchaseOrder e operazione POST."><figcaption><p>Rotta PurchaseOrder storica. Il vecchio percorso del proxy API Gateway è un esempio, non un indirizzo DocBits universale.</p></figcaption></figure>

Una volta configurati questi BOD, salvare il punto di connessione con l'icona situata a destra del pulsante Indietro.

## **Flusso di dati**

Questo flusso di dati storico è una possibile struttura; verificarne le rotte e l'organizzazione di ricezione nel proprio ambiente.

<figure><img src="https://lh7-us.googleusercontent.com/BtszuCXPwv-WYCGtnd_beU9t0uNntEu6U2iCSstxu1GAziuCfFafQdy2LKZkYw4kbQVfzI5lBYYajOeNwXkn84xy7AXWlCFX4GLo6dukWtfkFPMsXaPga0EkbnrI0bHSKqezXsvYJKymemZYDySIfA8" alt="Flusso storico da M3 attraverso un filtro Sì o No e una suddivisione parallela verso quattro nodi API DocBits, con nodi di unione e di fine."><figcaption><p>Flusso storico. Il ramo No termina prima dei nodi API; il ramo Sì raggiunge i quattro ambienti di esempio.</p></figcaption></figure>

I diversi nodi API DocBits rappresentano ambienti separati in questo esempio. La tua struttura può essere diversa; assicurarsi che i messaggi di test non raggiungano la produzione.

I quattro ambienti sono mostrati solo come esempio.

### **M3**

L'inizio del flusso di dati è costituito dalla tua applicazione M3

### **Filtro**

La configurazione del filtro è la seguente

<figure><img src="https://lh7-us.googleusercontent.com/-rMMaL3ToAoxqMFXybclIcd61H4S25HI90xnHANGl3J7ldZ374_T2V0q__QSwuNSuXfu829G7kYRCfVslx-l9b1j5LAVKonCQqO3aK2FuWNwmtyvytAF6PaIv8jiEJhhxSwU47eKEo1ozbzyndSW7BY" alt="Area Filter Properties storica con la scheda Properties selezionata e i campi Name e Description impostati su Division."><figcaption><p>Nome e descrizione del filtro storici. Il solo nome Division non stabilisce quali record vengono filtrati.</p></figcaption></figure>

<figure><img src="https://lh7-us.googleusercontent.com/npa9V37wV661zRD-pccafrGqw4hRb-Tk7iZ84UyyjE0gtfAcI1ma6_QWS3iEcBW35trveCG3CnXiZAnFIQyYM278XYJqIuzQh3SUmbAxLCmyTCHkiOhpDJwSfFDJtc8PlcbrmrBdZLACsK3B8sCSyDA" alt="Scheda Attributes storica dell'area Filter Properties con i percorsi AccountingEntityID per ChartOfAccounts, PurchaseOrder, RemitToPartyMaster e SupplierPartyMaster."><figcaption><p>Attributi storici: ogni BOD ha un percorso AccountingEntityID. Verificare il percorso di ogni documento nel proprio ambiente.</p></figcaption></figure>

<figure><img src="https://lh7-us.googleusercontent.com/saiZJD9diyo2JC-XV0vYCboPZJP-87zDH7LIGuBNMNzhL5alDZkShpCARfYd21oroC8eYBfYdckJiONty9IuOc7zHkIIlUWNqoxnPfygEc1R1Tnjt1KPZpSTr7-RLaa5lqS3_2DPj96aV0vLdZk2tzw" alt="Scheda Conditions storica dell'area Filter Properties con il documento ChartOfAccounts, la condizione Not Filtered e un'espressione di esempio per AccountingEntityID_3."><figcaption><p>Esempio storico di Conditions. Used Condition indica Not Filtered anche quando è presente un'espressione; verificare la condizione selezionata e il suo effetto invece di presumere che l'espressione sia attiva.</p></figcaption></figure>

(L'ID entità contabile è naturalmente univoco per la tua organizzazione)

### **API DocBits**

Qui si aggiunge un'applicazione e si selezionano le API DocBits create in precedenza

### **Documenti**

Selezionare i documenti assegnati al nodo di origine M3 e ai nodi di ricezione. Verificare che gli attributi del filtro e le rotte di ricezione coprano ogni documento richiesto.

<figure><img src="https://lh7-us.googleusercontent.com/GLI8kFjQHePMo4ZBWIR1WPNAhkvmtG0BfYADpdlmNqEFMYJclMInVYmKPdaElPLyPR5qtkWOKTnqDFXMDV2pML3igNOFyFj3R9fj2XHRAs6-Rl3KWz4a8-ednk15wyLDJUziAR6ZT4GjuZO2ANw1ymY" alt="Flusso M3 storico con l'icona del documento evidenziata e un pannello Documents con Sync.ChartOfAccounts, Sync.PurchaseOrder, Sync.RemitToPartyMaster e Sync.SupplierPartyMaster."><figcaption><p>Selezione storica dei documenti per il flusso M3. Si tratta di un elenco di documenti BOD, non della configurazione di un nodo file.</p></figcaption></figure>

## **Attivazione dei BOD M3**

Aprire l'applicazione Infor M3

In M3 aprire il controllo **Search and Start**, inserire **EVS006** e confermare il programma. Usare la navigazione supportata dal proprio client M3.

<figure><img src="https://lh7-us.googleusercontent.com/Vn2WD1-8RuDURsYmzrTARO4mBafwhBUvDImM3z2Nd_hDnVRWjbHgOoplV8QhBC9QtslnWqZyJNIhudvGFGaEl5S-qgloKn0rpwQsF0EuVnrzVplg1urqvSQ9fNa5Qetx8TwLuxZzL3N7wHz9kX4xr_o" alt="Dialogo Search and Start storico di M3 con la voce evs006 e il pulsante OK."><figcaption><p>Ricerca programma storica: inserire EVS006 in Search and Start.</p></figcaption></figure>

In EVS006 definire i BOD noun richiesti dalla mappatura approvata. L'esempio storico usa SupplierPartyMaster, RemitToPartyMaster e PurchaseOrder. Confermare i nomi delle tabelle M3 nella propria versione prima di creare una definizione di caricamento iniziale.

BOD noun: SupplierPartyMaster

Table: CIDMAS

BOD noun: RemitToPartyMaster

Table: CIDMAS

BOD noun: PurchaseOrder

Table: MPHEAD

Usare l'azione di aggiunta per ogni definizione approvata. Controllare società e divisione prima di proseguire.

<figure><img src="https://lh7-us.googleusercontent.com/3y5xAtk4nSc5Eqk-vOJLL59jQHc1w-Fmtn0PIjSiBWTeOo974zg4UjjrK890MjfnsU1a4UtiSqtwcNlHmr6el6GRBd8GrSN_ZlPk3W_IQIVcppHOYwnAzHEgRF22JmeRRkJSHotXvd3k_94_pYjt6Uw" alt="Ritaglio storico della barra degli strumenti EVS006 con Add evidenziato sopra i campi BOD noun, BOD variant, BOD e Table vuoti."><figcaption><p>Azione Add storica in EVS006. Questo ritaglio non mostra definizioni di caricamento iniziale compilate.</p></figcaption></figure>

Dopo aver aggiunto tutti i BOD, fare clic con il tasto destro sul BOD noun del BOD e selezionare Related → Run

<figure><img src="https://lh7-us.googleusercontent.com/HjkKvk7khjPgpjXmfyTyOLE2vNeB2qt2oN9ShOmrQiYhhvokRlBaZ0rlPtbwWUld54EhUJZLK0OVNGH_eIYzFj22XgFHZccEM9g2nVQ_5BgouHYoMfzfWYQVwluSdcednqrjilSByCdt44ytHgfCNyo" alt="Menu contestuale storico con Related espanso e Run evidenziato; sotto è elencata la voce History."><figcaption><p>Azione storica Related → Run. Con History si controlla in seguito il risultato del caricamento iniziale.</p></figcaption></figure>

L'azione collegata **Run** apre EVS007. Scegliere **Sync** solo se il flusso ION di ricezione lo prevede. Verificare la selezione e i filtri prima dell'invio definitivo; passare alla schermata successiva non dimostra la consegna.

<figure><img src="https://lh7-us.googleusercontent.com/FoJTP89zGI0FwRTyLjkIKfW75MbCrvcvqD_ka--G1SFdzIhBAp7dq63_WKMIEC-ouCHWA7sRd25rWfWclZJmWd7SGIZLwnSQ4id3nq82hOuFV9-mzMHAtGlhfCKtYwcQnrLyMSsrTmKNyME7lpYSeNA" alt="Schermata storica EVS007 Initial Load Job per CIDMAS e SupplierPartyMaster con stato Pending, menu BOD verb aperto e Sync annotato mentre Show è ancora visualizzato."><figcaption><p>Selezione storica del verbo in EVS007 prima dell'esecuzione. L'immagine mostra un job in attesa e un'opzione Sync annotata; non dimostra che Sync sia stato scelto o che i dati siano stati importati.</p></figcaption></figure>

Una notifica di invio conferma che il job è stato richiesto. In EVS006, in **History**, controllare il numero di record elaborati e gli errori. Verificare poi il messaggio e la destinazione in Infor ION.

## Verifica in DocBits

Nell'organizzazione DocBits prevista aprire **Impostazioni → Elaborazione documenti → Ricerca di dati anagrafici → Dati di ingresso BOD → Fornitore**. Selezionare il campo identificativo in **Ricerca per colonna**, inserire in **Ricerca Stringa** un numero o un nome di fornitore noto e avviare la ricerca con la lente. Aprire poi **Ordine di acquisto** e cercare un numero d'ordine noto; se la mappatura separa intestazione e righe, controllare anche **Intestazione Dell'ordine Di Acquisto**. Confrontare identificativi e società con l'origine M3. Una richiesta EVS007 riuscita, da sola, non dimostra che tutti i record siano arrivati.

<figure><img src="../../../.gitbook/assets/dbdc-1139-supplier-it-20261112.png" alt="Vista DocBits in italiano di Ricerca di dati anagrafici con la scheda Fornitore, i campi Ricerca per colonna e Ricerca Stringa e dieci righe fornitore inventate da SUP-1001 a SUP-1010."><figcaption><p>Vista Fornitore nella versione sandbox 11.27.7 con dati di esempio inventati. Cercare un identificativo di test noto e confrontarlo con M3 e ION.</p></figcaption></figure>

<figure><img src="../../../.gitbook/assets/dbdc-1139-purchase-order-it-20261112.png" alt="Vista DocBits in italiano Ordine di acquisto con le schede aperte Fornitore e Ordine di acquisto, gli stessi campi di ricerca e dieci righe d'ordine inventate da PO-4500 a PO-4509."><figcaption><p>Vista Ordine di acquisto nella versione sandbox 11.27.7 con dati di esempio inventati. Le righe non dimostrano un import M3.</p></figcaption></figure>

Le immagini di questa sezione provengono dall'interfaccia sandbox distribuita (versione 11.27.7) con dati di esempio inventati. Non è stato avviato alcun job M3, non è stato importato alcun file e non è stato modificato alcun dato anagrafico; le immagini mostrano dove verificare, non un trasferimento completato. Se manca un record previsto, controllare il registro storico EVS006, il routing ION, la mappatura BOD e l'organizzazione DocBits prima di riprovare.
