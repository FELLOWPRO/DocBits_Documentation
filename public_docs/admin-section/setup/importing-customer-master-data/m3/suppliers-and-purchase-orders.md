# Fornitori e Ordini di Acquisto

## **Punto di Connessione**

È necessario creare il punto di connessione API di DocBits per poter creare successivamente il flusso di dati.

In InforOS, vai su ION Desk → Connetti → Punti di Connessione

![](https://lh7-us.googleusercontent.com/ySRjNzMXFzwSOYKx9hnlKLPHPuXpmfTvRADBfV6cpT8ajiEUbS4oXpd9InhXG09mHLakhqBTJMH4yQJNG5z9RXmbAjh8YbuGhxnXSeooIH\_r3RAGOvJE6Ok67ST\_272zFfhB\_TTFYg3b-NwFq0CAv2o)

Una volta qui, sarà necessario creare un nuovo punto di connessione.

![](https://lh7-us.googleusercontent.com/ZDv-F3iayFqnsvVLlAE1kr0NNncsvuYtzcE\_WQj-0ONoE7McRl-f6\_DDH9ErQ0KLspZFFJ43t5EfnPBJjVg25YISMEQ--X4MmK6SVWzB60-Fq6mtwdhiOBwSnL-8vASXsto9iab0dnve6eeG8yuqNoI)

**Seleziona API**

Assegna al punto di connessione un nome e una descrizione che ne descrivano la natura e l'ambiente. Nella scheda Connessione, importa l'account di servizio che hai creato per l'ambiente con cui stai lavorando.

![](https://lh7-us.googleusercontent.com/UCuGTwKARn3auhYdDDUbQ78Ok3qBNE1KpGEMealfPvgRju4VRLn2AfKaL5tLDcAh00poLHNQU-Q6koBhG5RdxK4CJrrL6Qeb4D52qnhw3aG1LZniuzHRXwOyzGcJvRnQtLGbp6PIseXvWxHlk-AMlz0)

Passa quindi alla scheda Documenti. Dovrai aggiungere i seguenti BOD al punto di connessione, non tutti sono necessari per i dati principali dei fornitori e degli ordini di acquisto ma saranno utili quando verranno implementate altre funzionalità come la Contabilità Automatica.

![](https://lh7-us.googleusercontent.com/25Hizkx23i1c8-QHSrE7mPAH7zW6ux9iHTcP8\_l6EJJy548CvuNPF1R86Fuqx5iYZP9HF-Z4G6hntkaUtlOMetHIzAVZyBM6VIQ-vsvy6P5YBuAj4yscdJe8ySOHwIRQwFpShRiFGC83v467LLBaXq8)

Per ora ci concentreremo solo sui BOD necessari, ovvero: Sync.RemitToPartyMasterData, Sync.SupplierPartyMaster e Sync.PurchaseOrder.

* Sync.RemitToPartyMasterData e Sync.SupplierPartyMaster

La configurazione per questi due BOD dovrebbe assomigliare a quanto segue (il nome della chiamata API cambia per ciascuno)

![](https://lh7-us.googleusercontent.com/1SeyL73b7K9vxkTzKk-pumRleoY1sx9MVwgEBMZ-oUf6GXG2C7fKIRMbnhWHHhIQhUDBS3oKQidrQIN08FZ\_7eKEt1Yp0cRqnsDlv1R5ShdZdNKmaXmU\_19DAVtiT3U0m2qm4cBOj9FcnT0eyawfJXk)

* Sync.PurchaseOrder

La configurazione per questo BOD dovrebbe assomigliare a quanto segue

![](https://lh7-us.googleusercontent.com/ljXpQxwepI3u6kcITZfACV9yYL1ZZZtBbWimkXW6aWFTI-yd7Gajrxw2pwxdcF1Xv3KoGDalq72yXvaipjQ-OmbcTzJ0PUUKnmE0pBa5pASEPg0amqKSbU82ZDOKr5alWXynAd53IM2i9HgZ1CsYIB4)

Una volta configurati questi BOD, puoi salvare il punto di connessione premendo l'icona situata a destra del pulsante indietro.

## **Flusso di Dati**

Il flusso di dati assomiglierà a quanto segue

![](https://lh7-us.googleusercontent.com/BtszuCXPwv-WYCGtnd\_beU9t0uNntEu6U2iCSstxu1GAziuCfFafQdy2LKZkYw4kbQVfzI5lBYYajOeNwXkn84xy7AXWlCFX4GLo6dukWtfkFPMsXaPga0EkbnrI0bHSKqezXsvYJKymemZYDySIfA8)

(Il motivo per cui ci sono più API di DocBits è dovuto al fatto che ogni connessione rappresenta un ambiente diverso, il che significa che, a seconda del numero di ambienti che hai, il tuo flusso di dati potrebbe differire leggermente)

Per questa spiegazione useremo l'esempio di avere quattro ambienti separati.

### **M3**

L'inizio del flusso di dati consiste nella tua applicazione M3

### **Filtro**

La configurazione del filtro appare come segue

![](https://lh7-us.googleusercontent.com/-rMMaL3ToAoxqMFXybclIcd61H4S25HI90xnHANGl3J7ldZ374\_T2V0q\_\_QSwuNSuXfu829G7kYRCfVslx-l9b1j5LAVKonCQqO3aK2FuWNwmtyvytAF6PaIv8jiEJhhxSwU47eKEo1ozbzyndSW7BY)

![](https://lh7-us.googleusercontent.com/npa9V37wV661zRD-pccafrGqw4hRb-Tk7iZ84UyyjE0gtfAcI1ma6\_QWS3iEcBW35trveCG3CnXiZAnFIQyYM278XYJqIuzQh3SUmbAxLCmyTCHkiOhpDJwSfFDJtc8PlcbrmrBdZLACsK3B8sCSyDA)

![](https://lh7-us.googleusercontent.com/saiZJD9diyo2JC-XV0vYCboPZJP-87zDH7LIGuBNMNzhL5alDZkShpCARfYd21oroC8eYBfYdckJiONty9IuOc7zHkIIlUWNqoxnPfygEc1R1Tnjt1KPZpSTr7-RLaa5lqS3\_2DPj96aV0vLdZk2tzw)

(L'ID dell'entità contabile è ovviamente unico per la tua organizzazione)

### **API di DocBits**

Qui aggiungerai un'applicazione e selezionerai le API di DocBits che hai creato in precedenza
### **File**

La configurazione dovrebbe apparire come segue

![](https://lh7-us.googleusercontent.com/GLI8kFjQHePMo4ZBWIR1WPNAhkvmtG0BfYADpdlmNqEFMYJclMInVYmKPdaElPLyPR5qtkWOKTnqDFXMDV2pML3igNOFyFj3R9fj2XHRAs6-Rl3KWz4a8-ednk15wyLDJUziAR6ZT4GjuZO2ANw1ymY)

## **Attivazione M3 BOD**

Vai all'applicazione Infor M3

Una volta nel menu principale, digita Command + R per aprire la casella di ricerca del prompt dei comandi. Quindi digita evs006 e cerca.

![](https://lh7-us.googleusercontent.com/Vn2WD1-8RuDURsYmzrTARO4mBafwhBUvDImM3z2Nd\_hDnVRWjbHgOoplV8QhBC9QtslnWqZyJNIhudvGFGaEl5S-qgloKn0rpwQsF0EuVnrzVplg1urqvSQ9fNa5Qetx8TwLuxZzL3N7wHz9kX4xr\_o)

Una volta su questa pagina, dovrai aggiungere SupplierPartyMaster, RemitToPartyMaster e PurchaseOrder all'elenco.

Nome BOD: SupplierPartyMaster

Tabella: CIDMAS

Nome BOD: RemitToPartyMaster

Tabella: CIDMAS

Nome BOD: PurchaseOrder

Tabella: MPHEAD

Per ciascun caso dovrai premere sull'icona più per aggiungerli all'elenco.

![](https://lh7-us.googleusercontent.com/3y5xAtk4nSc5Eqk-vOJLL59jQHc1w-Fmtn0PIjSiBWTeOo974zg4UjjrK890MjfnsU1a4UtiSqtwcNlHmr6el6GRBd8GrSN\_ZlPk3W\_IQIVcppHOYwnAzHEgRF22JmeRRkJSHotXvd3k\_94\_pYjt6Uw)

Dopo aver aggiunto ciascuno dei BOD, fai clic con il pulsante destro del mouse sul nome BOD del BOD e seleziona Correlati → Esegui

![](https://lh7-us.googleusercontent.com/HjkKvk7khjPgpjXmfyTyOLE2vNeB2qt2oN9ShOmrQiYhhvokRlBaZ0rlPtbwWUld54EhUJZLK0OVNGH\_eIYzFj22XgFHZccEM9g2nVQ\_5BgouHYoMfzfWYQVwluSdcednqrjilSByCdt44ytHgfCNyo)

Verrai portato al seguente menu, dove dovrai cambiare il verbo BOD in Sincronizza e quindi premere AVANTI per attivare i BOD.

![](https://lh7-us.googleusercontent.com/FoJTP89zGI0FwRTyLjkIKfW75MbCrvcvqD\_ka--G1SFdzIhBAp7dq63\_WKMIEC-ouCHWA7sRd25rWfWclZJmWd7SGIZLwnSQ4id3nq82hOuFV9-mzMHAtGlhfCKtYwcQnrLyMSsrTmKNyME7lpYSeNA)

Una volta attivati i BOD, riceverai una notifica che conferma questo.

Se eseguito correttamente, le tabelle Fornitore e Ordine di Acquisto dovrebbero ora essere disponibili in Impostazioni → Ricerca Dati Principali.
