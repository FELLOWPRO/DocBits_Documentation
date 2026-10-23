# Codici d’imposta

## **Creare punti di connessione DocBits**

Apri ION Desk → Connetti → Punti di connessione

![Infor ION Desk con il menu Connect aperto sulla panoramica dei Connection Points](https://lh7-us.googleusercontent.com/QLQB17W\_hywZWBqme8Wio-orbdOdFHXLv5zTd89B3EkeS0WCuuo5Pv1CndLRQ2rFUefvQYM95U2Unhrl3YU3WAR23Ij\_tDw\_TOEVenWjyCh-9H8CPFSezF2gmED7u5QTR7q9WV4CSXRvDqkmKJYPqAI)

Avrai bisogno di 4 punti di connessione per questo flusso dati, 3 punti di connessione API per le diverse categorie di codici tributo (aliquota ordinaria, aliquota ridotta ed esente) e un punto di connessione Applicazione che rappresenta la tua azienda LN.

Per creare nuovi punti di connessione selezionare il pulsante “+ADD””

![Pagina Connection Points in ION Desk con il pulsante Add nella barra degli strumenti](https://lh7-us.googleusercontent.com/cECLuIswRSK3WWhUMi1n3tm2AIcrksZdpz7ZCO6-H\_MzaKe9CDT0w1b7GKJ8GtT\_d6nvvDe4ukLJfWcMocbHZ5dSSCw25Ky7-JUdrYb893GYYyaHL9tTjG1ZniORJPLSu1zJxL3c-1VQRw4IC0LpYuA)

Seleziona “API” in fondo all'elenco delle opzioni

![Menu dei tipi di punto di connessione con l'opzione API in basso](https://lh7-us.googleusercontent.com/bpeLxdmi8b10LLMGy02vMRXuLoic9kFLywnpd6SSYV0fNv82dQahyvaA85mC1PEVScNW4m63fOw89vkhQr0-ou8VWOSjkwGWG5GnP7GQl77THtjXWP3YNo8LUzAstpCs0Q5fOjxaoT\_\_ZKM4jciHA5I)

Verrai indirizzato alla pagina seguente

![Pagina del nuovo punto di connessione API in ION Desk con i campi Name, Description e account di servizio](https://lh7-us.googleusercontent.com/4pcN0B7aibjn\_Qn8nMgkzRc\_NiXev-c1wJudDKo2V5r0ORuajVzfzAWnWu0Wt68hKMKSLYkieUhOYChkcZuCZDWkg-F22Rq2WvVqgPweSg3by2TGrrJHweKWTlf\_DK1X2pCkoNU4yoGo3DyHsoqcGjg)

Qui è dove inserirai tutti i dettagli del punto di connessione TaxCode. Per ciascuno dei tre punti di connessione che creerai, procedi come segue

* Enter a Name: TaxCodeFull, TaxCodeReduced, TaxCodeFree
* Descrizione: può essere uguale al Nome o simile
* Importa un account di servizio che hai creato.

Passa alla scheda “Documents” e seleziona l'icona PLUS per aggiungere il BOD di cui abbiamo bisogno, come di seguito

![Scheda Documents del punto di connessione con l'icona più e le opzioni di direzione BOD Get from API, Send to API e Trigger API](https://lh7-us.googleusercontent.com/byhA18LzkcY9ZyfnzyDlru5qBx88E8U1yggMNNkoHGsYVCbNkflNFXGVvJwMvE\_104VCjoYOM0SQIJVniyBBdn5UKasVR0uat6UvmCmpzz9ZYsY2Wv14B4ElOwqcg2qklxYAQVU84UOG70l3fMLRrwo)

Cerca BOD

![Finestra di dialogo Input Document foreground process per la richiesta ION API con le schede Request Parameters, Request Body e Settings](https://lh7-us.googleusercontent.com/DAKzvEsjCmk1jy7L6GwrVY2DWg3\_InluNftWnR7hGlnyeBxSDW6XTDPBMLqtJuUc9Lq3Nga6-EKS4tZpOjE09h5FUJaTm\_E70UdA4l17jWGQ6BSr121lC3LzhffUXi6Bsk5EZEz4XHyjekk1Njb3H4I)

Cerca il BOD chiamato “Sync.LnTaxCode”, cliccaci sopra e premi “OK” per aggiungere il BOD.

![Elenco di selezione BOD con Sync.LnTaxCode selezionato e il pulsante OK](https://lh7-us.googleusercontent.com/7BLwrq8kr9OTHleI2anmAr2-4ChksQ0pptddwm1quFHquGfnMBEW32RFx31ETGbrxf0KGVr-VzlZC9h9heD3ymTq9L5NZEV1b9E67IIR0is18UGBCoJ5j7KIMmF533EDMvZzgi4LXqAkV9zgCyl0\_Lk)

Passa alla sezione ION API. Sotto API Call Name puoi usare il nome di BOD, Sync.LnTaxCode

Press the “SELECT” button

![Pagina del punto di connessione con la sezione ION API, il campo API Call Name e il pulsante SELECT](https://lh7-us.googleusercontent.com/7MukO6oUAzVBFMPhFepwMvugqnhDDMhX9j7wZRU7BU0OusW3CKpMgqQNC7uNlehPp6eFniVxrX3DxjgsGZ\_Tmt\_cQOWGGiBfXAQfCC85amOGp1VY8RGo3nPABCiwzaIkYmnQF6t3FPVZ1fPV6fLazNc)

Seleziona l’API che hai configurato per l'ambiente con cui stai lavorando e cerca il seguente API. Una volta selezionato, premere “OK”.

![Finestra di dialogo ION API Operation che elenca le operazioni di ricerca dei dati principali di DocBits come Import Xml File e Import Xml Data](https://lh7-us.googleusercontent.com/IpUUqJaXF0MmIeR6gtE9GDCccLfNsQLZ-RSHhQGVwJEj8WJwI-twgiHpFomBKhbnTUUKrhxJ0EUZ7F\_21MCSBjNS2VQq3azprekoxctRJZ-NJUHhb4J9rHUSRDoR\_OCzDHTG5q5KTwWMHOR5qNoNd38)

Successivamente, passa alla scheda Corpo della richiesta.

Qui è dove ci sarà un leggero cambiamento per ogni punto di connessione, questo è visibile nelle mappature dei campi che assegnerai a ciascun codice d’imposta poiché differiscono leggermente.

![Scheda Request Body con il corpo JSON e la voce field_mappings per il codice fiscale](https://lh7-us.googleusercontent.com/f4c-1M9mgCci2jjxkhaCDFX9bRWzMDaRwVv4XiaUH7BpHchPklvMnWoP\_ILSm6VB7GoFJNJzHsEPzk3eCFyLm1Kc3QI8OufjQ1mr7PqowjzViFDWc2opiNE1ODICtI9yEyUOi\_d\_hzN8CGo8gu6Ec84)

Nella riga field\_mappings, sotto valore, inserirai le mappature dei campi specifici per lo specifico punto di connessione del codice d’imposta che stai creando (aliquota ordinaria, aliquota ridotta o esente). Queste mappature sono disponibili su https://docbits.com/doc/field-mappings/.

Il risultato finale dovrebbe essere uguale o simile all'immagine sopra. Fatto ciò, fai clic sull'opzione SAVE che si trova qui.

![Menu in ION Desk con l'opzione SAVE per il punto di connessione](https://lh7-us.googleusercontent.com/LSYrbElw6BgQbbIdSstbakfwLENZ\_09WQcQhjO7kbb2U3jSK\_\_wFnr43tIj2hTHYegQ9lrSZBuJ9N7MNewr2W3yjPCrrVLeP9UAZjvrKKBzeY9h-q6FrVd5gPtlH0iP0GpMcvhGxjAnHN7BlY8CmT3c)

## **Configurazione del flusso di dati**

Passare a ION Desk → Connetti → Flussi di dati

![Infor ION Desk con il menu Connect aperto sulla panoramica dei Data Flows](https://lh7-us.googleusercontent.com/cpWAepQyLP8V0b-Oj7djzl21eZLU2JdnJPEMPs53Uq-adZbaCegl35RjguLx8rsP2E87ZmwbNgISFIpAy6kOeahaBCSygDVSJzmv1GQGn1w1MgR8N08mnnfhb02XjsLnt\_rVJKr4Y0UtiTf14NqTHLQ)

Fare clic su “+ADD” e selezionare il flusso di documenti

![Pagina Data Flows in ION Desk con il menu ADD e l'opzione document flow](https://lh7-us.googleusercontent.com/HYqc\_P2DQjBoc-mpsyZ\_nlPFNiU17ZCLHfiOa282-Sa5JSA3Hv1XlwFjmlPhVGnAaEAqqalJ5ka43AJOzEO3uljwVAogAHkTVer7Q9JgI0WaOVX2Uo5Z8KGEqoa3BH\_zZwup7Bh4lKe4O5kr6hmAZm4)

Crea il seguente flusso di dati trascinando e rilasciando i componenti dal menu a

![Editor del flusso di documenti con i componenti applicazione, documento, filtro e API disposti in una catena](https://lh7-us.googleusercontent.com/V\_aJHPhFJssPUQ4mAHU20SVPSfhqhjU8BOQ2Ws1MtaauKp6OVAENLXod2uQe6Zbuc5JKZx6Bp3WyJtkQtkbnDluZZS5GLMGcaC9EuCrV8cn2aJk2y-Cih3PP2dg-umW0iDhak5UXNUuPxwkgqVg-mvk)

### **Applicazione (LN)**

![Impostazioni della decisione di filtro in ION Desk con i rami Yes e No e i nodi End](https://lh7-us.googleusercontent.com/2CCNlz0S-Z8p\_l9kPPUMqPkreoO3aLy8MkqY6UFMIABJRNFXGTFMXbaw78E42g8fEO4ZxFL\_oJMf2QnWn2xZLtS4zjN8AzCS\_B2i2x-tjWmmjyVLa1jSLQAnSB8-EhNfNISzf2uuX9kcqN-QixUUXvw)

Qui è dove selezionerai la tua azienda LN, il risultato finale dovrebbe essere simile al seguente

![Flusso di dati con il componente applicativo LN e la relativa azienda selezionati](https://lh7-us.googleusercontent.com/b5pb4YfbZMCSi2X-xT4mj-Yw\_Uu77zNyJGl3rntVdqf907PwgX6Z9uQJIoHA2FS5M\_mVbdQgkh0HWgsOgtkoySmtrT7W8CrqsqlCnPEt6hv\_yODGulfp1qdxXvrB1HL-en3W9bY285fC3kARLZfSfck)

### **Documento**

![Selezione del documento per il nodo dell'applicazione con il BOD Sync.LnTaxCode scelto dall'elenco Documents](https://lh7-us.googleusercontent.com/U8cqu3jABU3RQLGEGsS5qCnDkc-boTpAdZEVIUA9AlmD9Oz33JvnzD43SBTmLY55i8Bsr4lbi6udeIimCcRG1NgWbynv6OllCLaJPC50kJ0gPq7rsR5Rvj50yKngMiNvnYoLLT\_Hzn5cyhp18jq\_IyI)

Qui è dove aggiungerai Sync.LnTaxCode BOD di prima, il risultato sarà il seguente

![Flusso di dati con il componente documento Sync.LnTaxCode aggiunto dopo l'applicazione](https://lh7-us.googleusercontent.com/bgC1y3NtmX09XBjng\_pKmP5VQ5w0E\_VuFOfMF1rYs3iGGL5OaMHkKoyQJNtcVtbS6bEvF4KdtFNaX0VxT9MF0P-zTDnOnt5mhA0Gxcs4eMcRLtbXl5a\_8y84XyLyvh61-LdoQ7f15j-wE1nl\_TSYSDg)

### **Filtri**

![Canvas del flusso di dati in ION Desk con tre nodi filtro e i relativi rami Yes e No instradati verso la fine](https://lh7-us.googleusercontent.com/1Cv1XxqdpiNfonz6jdFgz9zGibQTRLd\_0ONFHf3FvzPB9-sQuX4lTUyuDWzm-RffuPf5jDmZAZwUqbXX-1kers1sEb9ykRMHeYYP6zGgF8yZ247Dx0nG04kSYUTTKSwt3NLS-3TwXA5tbvy5z8HA2bw)

#### **Filtro 1 (in alto): aliquota ordinaria**

Il nome e la descrizione dipenderanno dall'ambiente che stai utilizzando e dalle tue preferenze.

![Finestra di dialogo delle proprietà del filtro per il filtro completo del codice IVA con i campi Name e Description](https://lh7-us.googleusercontent.com/WVKWUme9uUjRRn7dZ5c\_RyPk\_GCTFEfiNxU\_H5aA979k5hOv2coDYEJHu4K1EaTLUf8\_Pd9ffOk757DaflF0Se0gZ1ZYvRk4QHlpKP0IeirfNr-L6JU3Z\_xFZJ2eeFI-Rhcctwk9QOHRORGNt1oIEpE)

![Pannello Filter Properties in ION Desk con la condizione su LnTaxCode e il percorso documento RateNumeric](https://lh7-us.googleusercontent.com/1gCPbUtC7KknzEHVZqIMKyjQGmNyNnR4c1mJ5x0LCJnAjd8D3SdW3W6nPMTsLokL-W2-XjoSM9MU1mJ77K12g887r\_jHoHBwquN1Ore2AmyjCaf\_YVT78KiKtY\_itlr-vyMvJrU7YV6ErgVSYbw5SEU)

![Pannello Filter Properties in ION Desk con la condizione COMBI come TaxFull OR Tax16 OR Tax20 su RateNumeric](https://lh7-us.googleusercontent.com/ijzGaLt9Uhzw6Wf66ah3auWo5TbkCnM-xGDYezsXXjPEkdCe5RO1wWfhhhG0qRuKbojijLKUm-WUV21eRdq36moWu9Ft0ujexe\_1lTUUEQbfXPvtrzP7iudkSaG\_oiX\_LV7AqZRGlNAp0OXnN8BXRIM)

#### **Filtro 2 (centrale): aliquota ridotta**

Il nome e la descrizione dipenderanno dall'ambiente che stai utilizzando e dalle tue preferenze.

![Finestra di dialogo delle proprietà del filtro per il filtro del codice fiscale ridotto con i campi Name e Description](https://lh7-us.googleusercontent.com/pKLo6q5zCQOZQhiRppyd8M-nlIrX5leGUiCct4Xn-4teIZTip5GAJVP0EFc2PrJ6EeDmU2KVOHRKVCaaML4sK8jCnsgTmxbTYjc-9CNd6bOfU-WD9tySeKL7gSRltjzoTEI5Ozrd\_s-7qj2KVNOWN7s)

![Pannello Filter Properties in ION Desk con il percorso documento LnTaxCode e l'attributo RateNumeric](https://lh7-us.googleusercontent.com/87PoQQ5q\_35buL\_VNcvz3v-um1upk1U579LDASCJptnnC8ip5mwXxz89d1YmtIK59dOUhl9dfz6BrXBLSNUy6EnWU5uPmUEzbLQv-MwzR0dDkuM1BJ477yre-X4QeJzkkzprF9y5wCWY4zvaooMwIZ0)

![Pannello Filter Properties in ION Desk con la condizione COMBI2 come Tax7 OR Tax5 OR Tax10 su RateNumeric](https://lh7-us.googleusercontent.com/Pa19AN6Mhxbn6bHSc5qKEGM0xRsEV6v77ooyeg5-91i8qGhaThb4328nr\_g6a\_z-7BOCJmWpo8Gbd2twl9FQkOf1Q8QZqOkJmxsIxaTP0R6dASgZdIV6z7p8PFYPYUJ1eKp8btYOBapliANstQSUgAQ)

#### **Filtro 3 (in basso): esente**

Il nome e la descrizione dipenderanno dall'ambiente che stai utilizzando e dalle tue preferenze.

![Finestra di dialogo delle proprietà del filtro per il filtro libero del codice fiscale con i campi Name e Description](https://lh7-us.googleusercontent.com/c\_SuWaZ3gF-FbOPWkxB\_eFgkT-TGJEYwV\_fQT05wGWHFNzI9SDZRQfauVMeBl0rn79QdU-W3kRgN-hWsYkfdMSevlYyiNPxxT\_3RxXcETo-lkjvI5TCygUag91PFJycrRdMA5hSQJCuzt8FekMwpu98)

![Pannello Filter Properties in ION Desk con la condizione su LnTaxCode per il codice fiscale gratuito](https://lh7-us.googleusercontent.com/HGZ8fR6XgYtZ46i8Rov8xIr5J4z8DmGFfJkeovDGzT7S68VYI-OdG5jpMdoOiROIZckYMbVIlPQmS\_kWQazJVbco1t4ZH5Sr73b4xePlisnbm9ZLJrOPwtXn7-90F1FcFH99P6ZKI0hCWdI6z4d7qNA)

![Pannello Filter Properties in ION Desk con la condizione Tax0 e RateNumeric uguale a 0](https://lh7-us.googleusercontent.com/\_APmMO6A2AG2km4H4em-ZMrn6\_XRpO3zxRhZwftiaKi5uoDhv3TTzCBfi8WVDCf6mOQNgtcEJ-z-BmP28J86noGJ5dgqVni2QIxePaO5-LU8fdwRqySUQt\_6wmFWiOFzTMmItcClQPRaSKUaosgWwNk)

### **APIs**

![Flusso di dati con i tre componenti API per i punti di connessione del codice fiscale](https://lh7-us.googleusercontent.com/XDhVCKHYaxrRIFyYfq0guXwnZH6jK-WZIFj2i0Wkr4kxyNcdCH1TzKd0Pb3-H6qs-b7JZ3UUIGm0BVHiUL7Aya-D7YOSV8p8tnwQeAfBN30T4fW5-ANePN1TcvUr1gzLJPwj7rRO4Hw4ziuyYrqZBX8)

Qui è dove selezioni i punti di connessione API creati in precedenza, per farlo seleziona API nel menu a discesa “Select ION API Connector”.

#### **API 1 (in alto): aliquota ordinaria**

Il nome e la descrizione dipenderanno dall'ambiente che stai utilizzando e dalle tue preferenze.

![Impostazioni API nel flusso di dati con il menu a discesa Select ION API Connector per il codice fiscale completo](https://lh7-us.googleusercontent.com/90c2E47fMC9CKNVY8DtgyaNUAqAnQmfErZm\_R-njUlEdIX6mafMUOk3GcAooaWfCzD4-OmdPUq5VSuMXmTSNjVEc924ASIPqmTxAQXqsq6eKs5y82rvwHxqnsT4S-sEm2mQRNwleiubkwIO\_kS9Vwzg)

#### **API 2 (centrale): aliquota ridotta**

Il nome e la descrizione dipenderanno dall'ambiente che stai utilizzando e dalle tue preferenze.

![Impostazioni API nel flusso di dati con il menu a discesa Select ION API Connector per il codice fiscale ridotto](https://lh7-us.googleusercontent.com/vw1hM3W4eCt\_8OG7Ht203tckaWarPOLi463WvQzGgixTMnfk7iC27JzL3iNgd5LmvBzWTFnYa3QNy5y\_oNSHJ9R-Ck5CAgLoBmGurbCn1RZ32jiSJr-LUnL3b0nhHctBqcCx\_25L1Ce-\_va3ZgfKXY8)

#### **API 3 (in basso): esente**

Il nome e la descrizione dipenderanno dall'ambiente che stai utilizzando e dalle tue preferenze.

![Impostazioni API nel flusso di dati con il menu a discesa Select ION API Connector per il codice fiscale libero](https://lh7-us.googleusercontent.com/C0wmqAkrlgyXlMjKsGMOqre4MPLuHawrZB1oYDzkGFocperUB5dKea7kx44hrA\_Kz6Ptx495cQbwq\_EHfEGNvvpr\_0dvCuUS2zz0-SARyuNbf2gKsK3vTdd4Sfg3jWtE1YAN3o0VpoK\_HRn7T-fFOR8)

Una volta fatto tutto quanto sopra, SAVE e ACTIVATE il flusso dei dati premendo i seguenti pulsanti

![Barra degli strumenti del flusso di dati con i pulsanti SAVE e ACTIVATE per il flusso di documenti](https://lh7-us.googleusercontent.com/f8gkYY1Z\_W1if2h1es9vbjebtDX0zGiqY4p9OD68gKSAcNU6si-guvyIg8hzdjP7TulZ6Yq8NcbT2EyuHleVeNxpY\_6TDlbgIUaxDJ72ILcy8kVvFuSja7FT6gpYhMLFGw7wv-r0XyFN8xIrQ3OuUGI)

## **Attivazione dei BOD (LN)**

Open LN in Infor

![Home page di Infor nel browser con le voci Home, Master Data e Publish Logistic Master Data nella navigazione](https://lh7-us.googleusercontent.com/aAKRLInqsogQLv9nye2rHLtVFlW4yaCpnQ8A4cKG5A2145Tl6poOxthfo2InYimNk5dd8RabYrX9xP7sPO0aJ5ThF07ZVfKvUXBqVoxRJg53IhpeOeiA4B\_CGOpeLKWlPbCf4EaFXjgzmBOcezocF9k)

Passare a Comune → BOD Messaggistica → Pubblica BOD → Pubblica dati anagrafici finanziari

![Menu di Infor LN con Common, BOD Messaging, Publish BODs e Publish Financial Master Data](https://lh7-us.googleusercontent.com/pMAgPzyhBNrEsFkTm8-iniHBhEXIPswoJ8URt\_v0fv\_7dSayrS8UkN7F9WMAOZQB9Q6sCe9faRl4rRDDft3VdrzfNUT-IbWxE6GyWPPKZh4R67JRmXmJ2NsTVPdjLo6uJdCpki7QDpgiY\_azWtqaqKA)

Seleziona MORE e clicca su LnTaxCode

![Elenco delle colonne in Publish Financial Master Data con LnTaxCode accanto alle voci AccountingBookDefinition e AccountingEntity](https://lh7-us.googleusercontent.com/MtjE7Glgv7e\_F\_CJ4LXMuWk6SaInmNFlKzhGJu71iGgxRWtjI96lX5J0gqxRcj3y1u4E6Aq-xNEpuf83dsjHh6op0qeH89oBMvlVTTD\_VhGs10-gjuIb0eyc9b3dcCk75Wa5sASreXKW6SbQPYrs8sM)

Spuntare la casella per selezionare i BOD LnTaxCode

![Finestra di dialogo Publish Financial Master Data con la colonna LnTaxCode e i pulsanti PROCESS, CLOSE, SELECT ALL e CLEAR ALL](https://lh7-us.googleusercontent.com/VTFntcBK0GVsUdr\_fZBUaN8rXYdufObLE7PnwwNg9QU69zYwKHvwFZ7En9WZ6p\_WGIkVdqEjBBYeIYSuHHJWBWYonwd6Edtr0ZZuGsX3qhNMDWQWefOaGfrYxrq\_yLm6\_gEw967PGp3HK0hzO-G2XiQ)

Torna alla scheda OPTIONS, la tua configurazione dovrebbe apparire come segue

![Scheda OPTIONS in Publish Financial Master Data con la configurazione per i BOD LnTaxCode](https://lh7-us.googleusercontent.com/2tr7VHNOLActJCiLGC6jyWsdyqwZV7Je6UsekeoBo57qNpOBDYtOQuoelKOdvLMRo6uQJWn1S4ir\_zRZHAx2C96NyKp4ZjIUyFCYt58T59TqO3ml0ZfiEtSLwdRPp9g8pkMemN0xDS5ao8DL5xgosWE)

Quando desideri pubblicare i BOD, seleziona PROCESS.

Il risultato finale dovrebbe darti una tabella simile nel tuo ambiente DocBits.

![Tabella di DocBits con le righe dei codici fiscali importati che mostra i codici BE_NAVL, BE_NAVLRP e BE_NAVM con le relative aliquote](https://lh7-us.googleusercontent.com/4wK-mfKl0UNqvp5ngolE54miiwAKxAcOERO2mSDWzZ5t838VhFZrZGzCMeIyg7WDPpHvNzkeWRJV7ZZdsaxwXiFS9uxm29QZUYHhs9gU2v6QgSz07vfjpHXW3oTb5ZiiiTjI93gmV9MDTHbNWJmrvHY)
