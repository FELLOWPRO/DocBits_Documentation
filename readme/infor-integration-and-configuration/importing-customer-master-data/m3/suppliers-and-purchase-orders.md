# Fornitori e ordini di acquisto

## **Punto di connessione**

Sarà necessario creare il punto di connessione DocBits API per creare successivamente il flusso di dati.

In InforOS, vai a ION Desk → Connetti → Punti di connessione

![Menu di navigazione di Infor ION Desk con le voci Home, Data Flows, API Flows e Mappings](https://lh7-us.googleusercontent.com/ySRjNzMXFzwSOYKx9hnlKLPHPuXpmfTvRADBfV6cpT8ajiEUbS4oXpd9InhXG09mHLakhqBTJMH4yQJNG5z9RXmbAjh8YbuGhxnXSeooIH\_r3RAGOvJE6Ok67ST\_272zFfhB\_TTFYg3b-NwFq0CAv2o)

Una volta qui, dovrai creare un nuovo punto di connessione.

![Pagina Connection Points in ION Desk con le icone della barra degli strumenti e un elenco vuoto di punti di connessione](https://lh7-us.googleusercontent.com/ZDv-F3iayFqnsvVLlAE1kr0NNncsvuYtzcE\_WQj-0ONoE7McRl-f6\_DDH9ErQ0KLspZFFJ43t5EfnPBJjVg25YISMEQ--X4MmK6SVWzB60-Fq6mtwdhiOBwSnL-8vASXsto9iab0dnve6eeG8yuqNoI)

**Select API**

Assegnare al punto di connessione un nome e una descrizione che descriva la sua natura e il suo ambiente. Nella scheda Connessione, importa l'account di servizio che hai creato per l'ambiente con cui stai lavorando.

![Impostazioni del punto di connessione per DocBits-DEV-Demo-Import in ION Desk con Name, Description e account di servizio sotto la scheda Connection](https://lh7-us.googleusercontent.com/UCuGTwKARn3auhYdDDUbQ78Ok3qBNE1KpGEMealfPvgRju4VRLn2AfKaL5tLDcAh00poLHNQU-Q6koBhG5RdxK4CJrrL6Qeb4D52qnhw3aG1LZniuzHRXwOyzGcJvRnQtLGbp6PIseXvWxHlk-AMlz0)

Successivamente, passa alla scheda Documenti. Sarà necessario aggiungere i seguenti BOD al punto di connessione, non tutti sono necessari per i dati anagrafici del fornitore e dell'ordine d'acquisto ma saranno utili quando è necessario implementare altre funzionalità come la contabilità automatica.

![Scheda Documents del punto di connessione ION Desk che elenca i Connection Documents tra cui Acknowledge.SupplierInvoice, Sync.PurchaseOrder, Sync.RemitToPartyMaster e Sync.SupplierPartyMaster](https://lh7-us.googleusercontent.com/25Hizkx23i1c8-QHSrE7mPAH7zW6ux9iHTcP8\_l6EJJy548CvuNPF1R86Fuqx5iYZP9HF-Z4G6hntkaUtlOMetHIzAVZyBM6VIQ-vsvy6P5YBuAj4yscdJe8ySOHwIRQwFpShRiFGC83v467LLBaXq8)

Per ora ci concentreremo solo sui BOD necessari, ovvero: Sync.RemitToPartyMasterData, Sync.SupplierPartyMaster e Sync.PurchaseOrder.

* Sync.RemitToPartyMasterData and Sync.SupplierPartyMaster

La configurazione per questi due BOD dovrebbe essere simile alla seguente (API Nome chiamata che cambia per ciascuno)

![Configurazione Send to API per Sync.SupplierPartyMaster con il prodotto DocBits-DEV e l'operazione post CustomerApi/DocBits-DEV/prod/import/supplier_bod](https://lh7-us.googleusercontent.com/1SeyL73b7K9vxkTzKk-pumRleoY1sx9MVwgEBMZ-oUf6GXG2C7fKIRMbnhWHHhIQhUDBS3oKQidrQIN08FZ\_7eKEt1Yp0cRqnsDlv1R5ShdZdNKmaXmU\_19DAVtiT3U0m2qm4cBOj9FcnT0eyawfJXk)

* Sync.PurchaseOrder

La configurazione per questo BOD dovrebbe essere simile alla seguente

![Configurazione Send to API per Sync.PurchaseOrder con Product DocBits-DEV e operazione post CustomerApi/DocBits-DEV/prod/import/purchase_order_bod](https://lh7-us.googleusercontent.com/ljXpQxwepI3u6kcITZfACV9yYL1ZZZtBbWimkXW6aWFTI-yd7Gajrxw2pwxdcF1Xv3KoGDalq72yXvaipjQ-OmbcTzJ0PUUKnmE0pBa5pASEPg0amqKSbU82ZDOKr5alWXynAd53IM2i9HgZ1CsYIB4)

Una volta configurati questi BOD, è possibile salvare il punto di connessione premendo l'icona situata a destra del pulsante Indietro.

## **Flusso di dati**

Il flusso di dati sarà simile al seguente

![Diagramma del flusso di dati ION che collega M3, un Filter e diverse applicazioni dell'API DocBits a un elemento End](https://lh7-us.googleusercontent.com/BtszuCXPwv-WYCGtnd\_beU9t0uNntEu6U2iCSstxu1GAziuCfFafQdy2LKZkYw4kbQVfzI5lBYYajOeNwXkn84xy7AXWlCFX4GLo6dukWtfkFPMsXaPga0EkbnrI0bHSKqezXsvYJKymemZYDySIfA8)

(Il motivo per cui sono presenti più API DocBits è dovuto al fatto che ciascuna connessione rappresenta un ambiente diverso, il che significa che, a seconda della quantità di ambienti di cui disponi, il flusso di dati potrebbe differire leggermente)

Ai fini di questa spiegazione utilizzeremo l'esempio di avere quattro ambienti separati.

### **M3**

L'inizio del flusso di dati è costituito dalla tua applicazione M3

### **Filtro**

La configurazione del filtro è la seguente

![Finestra di dialogo Filter Properties in ION Desk con le schede Properties, Attributes e Conditions e i campi Name e Description](https://lh7-us.googleusercontent.com/-rMMaL3ToAoxqMFXybclIcd61H4S25HI90xnHANGl3J7ldZ374\_T2V0q\_\_QSwuNSuXfu829G7kYRCfVslx-l9b1j5LAVKonCQqO3aK2FuWNwmtyvytAF6PaIv8jiEJhhxSwU47eKEo1ozbzyndSW7BY)

![Scheda Filter Attributes che elenca righe di Document Path Filtered Data Type per ChartOfAccounts, PurchaseOrder, RemitToPartyMaster e SupplierPartyMaster per AccountingEntityID](https://lh7-us.googleusercontent.com/npa9V37wV661zRD-pccafrGqw4hRb-Tk7iZ84UyyjE0gtfAcI1ma6\_QWS3iEcBW35trveCG3CnXiZAnFIQyYM278XYJqIuzQh3SUmbAxLCmyTCHkiOhpDJwSfFDJtc8PlcbrmrBdZLACsK3B8sCSyDA)

![Scheda Filter Conditions con Document ChartOfAccounts, la condizione Not Filtered e l'espressione AccountingEntityID_3 equals 780_AAA](https://lh7-us.googleusercontent.com/saiZJD9diyo2JC-XV0vYCboPZJP-87zDH7LIGuBNMNzhL5alDZkShpCARfYd21oroC8eYBfYdckJiONty9IuOc7zHkIIlUWNqoxnPfygEc1R1Tnjt1KPZpSTr7-RLaa5lqS3\_2DPj96aV0vLdZk2tzw)

(L'entità contabile ID ovviamente è unica per la tua organizzazione)

### **API DocBits**

Qui aggiungerai un'applicazione e selezionerai i DocBits API che hai creato in precedenza

### **File**

La configurazione dovrebbe apparire come segue

![Flusso di dati ION da M3 attraverso un filtro verso le applicazioni DocBits-DEV-P, DocBits-DEV-S e DocBits-DEV-D con i documenti ChartOfAccounts, PurchaseOrder, RemitToPartyMaster e SupplierPartyMaster](https://lh7-us.googleusercontent.com/GLI8kFjQHePMo4ZBWIR1WPNAhkvmtG0BfYADpdlmNqEFMYJclMInVYmKPdaElPLyPR5qtkWOKTnqDFXMDV2pML3igNOFyFj3R9fj2XHRAs6-Rl3KWz4a8-ednk15wyLDJUziAR6ZT4GjuZO2ANw1ymY)

## **Attivazione dei BOD M3**

Passare all'applicazione Infor M3

Una volta nel menu principale, digita Comando + R per aprire la casella di ricerca del prompt dei comandi. Quindi digita evs006 e cerca.

![Pannello Search and Start in Infor M3 aperto sopra il menu principale](https://lh7-us.googleusercontent.com/Vn2WD1-8RuDURsYmzrTARO4mBafwhBUvDImM3z2Nd\_hDnVRWjbHgOoplV8QhBC9QtslnWqZyJNIhudvGFGaEl5S-qgloKn0rpwQsF0EuVnrzVplg1urqvSQ9fNa5Qetx8TwLuxZzL3N7wHz9kX4xr\_o)

Una volta in questa pagina, dovrai aggiungere SupplierPartyMaster, RemitToPartyMaster e PurchaseOrder all'elenco.

BOD noun: SupplierPartyMaster

Table: CIDMAS

BOD noun: RemitToPartyMaster

Table: CIDMAS

BOD noun: PurchaseOrder

Table: MPHEAD

Per ogni caso dovrai premere l'icona più per aggiungerli all'elenco.

![Elenco di attivazione BOD basato su eventi EVS006 in Infor M3 con una barra degli strumenti Actions e il pulsante Apply](https://lh7-us.googleusercontent.com/3y5xAtk4nSc5Eqk-vOJLL59jQHc1w-Fmtn0PIjSiBWTeOo974zg4UjjrK890MjfnsU1a4UtiSqtwcNlHmr6el6GRBd8GrSN\_ZlPk3W\_IQIVcppHOYwnAzHEgRF22JmeRRkJSHotXvd3k\_94\_pYjt6Uw)

Dopo aver aggiunto ciascuno dei BOD, fare clic con il tasto destro sul nome BOD del BOD e selezionare Correlati → Esegui

![Menu contestuale del clic destro in Infor M3 con le opzioni Drill down, Select, Change, History, Copy, Delete e Display](https://lh7-us.googleusercontent.com/HjkKvk7khjPgpjXmfyTyOLE2vNeB2qt2oN9ShOmrQiYhhvokRlBaZ0rlPtbwWUld54EhUJZLK0OVNGH\_eIYzFj22XgFHZccEM9g2nVQ\_5BgouHYoMfzfWYQVwluSdcednqrjilSByCdt44ytHgfCNyo)

Verrai portato al menu seguente, dove dovrai cambiare il verbo BOD in Sync e quindi premere NEXT per attivare i BOD.

![Pannello di attivazione BOD in Infor M3 per la tabella CIDMAS con nome BOD SupplierPartyMaster e stato del lavoro Pending](https://lh7-us.googleusercontent.com/FoJTP89zGI0FwRTyLjkIKfW75MbCrvcvqD\_ka--G1SFdzIhBAp7dq63\_WKMIEC-ouCHWA7sRd25rWfWclZJmWd7SGIZLwnSQ4id3nq82hOuFV9-mzMHAtGlhfCKtYwcQnrLyMSsrTmKNyME7lpYSeNA)

Una volta attivati i BOD, riceverai una notifica di conferma.

Se eseguito correttamente, le tabelle Fornitore e Ordine d'acquisto dovrebbero ora essere disponibili in Impostazioni → Ricerca dati anagrafici.
