# Contabilità automatica

## **Prerequisiti**

* Flusso dati funzionante da M3 a DocBits
* Ambiente DocBits configurato correttamente

## **Configurazione Infor**

In Infor, aprire l'applicazione ION Desk. Nella scheda sinistra, andare su Connetti → Punti di connessione

&#x20;

![](https://lh7-us.googleusercontent.com/Gl49rTfnpYQjXjpUNF3SEouZiJ4pPeHVk60d7dyHizfPLT6sn4AoKVQPPvpgg2cD4ts40hDeWQRs3BqmKW-CAco7Dt0oWKF7ukQJUVDBgSUoMNHt\_gRkqLxkF5CC\_CNGpVRzrNs7rfF1msK320\_J02g)

Qui è dove creerai il punto di connessione necessario per importare i tuoi dati da M3 che sono richiesti per la Contabilità automatica.

Clicca su "+AGGIUNGI" per creare un nuovo punto di connessione, seleziona l'opzione API come segue

![](https://lh7-us.googleusercontent.com/ctE76pck6mGmBVxRIMhHyn0TbSKKsiGjO7rO185fjndTIo7qYyvSZS3neUdV2CWPqBSangpJ4oG\_g946\_KyOwWyJvacZe5htWiQLTZQLzfNHvsHDhmMQmjh7MrGsqKp6sm-XPcGmEwrH2ZMYCd0bUl8)

Dovrai configurare il punto di connessione API chiamato:

* Piano dei conti

### **Piano dei conti**

La scheda di connessione per il tuo punto di connessione Piano dei conti dovrebbe assomigliare a quanto illustrato di seguito. Assegna al punto di connessione un nome e una descrizione appropriati, oltre ad importare il Servizio Account che hai creato.

![](https://lh7-us.googleusercontent.com/p-jly6\_S96TsCmpFg9oOob0h7Q7NBlTxRKgNCphiy5QfbK\_lrLMAR2miVUQh-fXrCfGdZr17ongp5c9bnK6HuHCVuDArHhYcmKDlAyO52tGcxg-VXBLXZ1ka8yqZ4DWnxFFMxUKkE7jgvCgr7P-nzdU)

![](https://lh7-us.googleusercontent.com/GkX20Q23htKae7OOcGnJ5J6f0L4I69vOU9jYBpY1m9bpDPdtsD584mh\_9IaZF37Ne1OY2uOPgFxYYjwTrBOoZqahpJLlY3n3qmBn0sgzC0eVu91wE0NWBvESBFJmeVTITQoqUTEU56tHEj47-LQmI6E)

Dovrai aggiungere due BOD in questa sezione per questo punto di connessione. Questi sono Sync.ChartOfAccounts e Sync.CodeDefinition, per aggiungere questi BOD fai quanto segue:

#### **Sync.ChartOfAccounts**

* Clicca sull'icona PIÙ (+)

![](https://lh7-us.googleusercontent.com/hFWg7-4Osuy9Q0uZYqT9yfAPFYsBi7yitHj7BBxQ94vbsDVg-GuCeTBakvV2eQNjqMGwDAF90nO5h-OxFR8HtYEiYcALdBq5Fdj\_Gl-wU8QePGV4Wr3\_78OK22nUY35dfCQhUPQIp\_qkdHN0wr7V-VY)

* Seleziona "Invia a API"

![](https://lh7-us.googleusercontent.com/jA97YupOjXJlRFRxduo\_tYO4YYDZoT0mHxWaPWfJGyU4RTNSVNRAIAsR5mzRyLh1iusHl0cBKUxhYj3hQMzacGdN2QGsvPGy1vHeq\_JNhDqxc-SI5HtZh\_Z\_zmaSjyJwmr2337tzYSWfqDl3JGkjBqY)

* Cerca il BOD Sync.ChartOfAccounts

![](https://lh7-us.googleusercontent.com/hzuwy-VU8xpgQ85NGHAk9u-m-\_Sw4iffT0SNtWTJw9iWHRIsIvGTEYQgJYi7CUoYC7\_Yp2KDtsohRQkNtIgr1VutFbR8mTkT\_5HmJ7ecgW8pcGuZTuwxtPDOlJpWuONq3WPIupRRBxBJPlsYQ9w-bxo)

![](https://lh7-us.googleusercontent.com/6p8nXaRAI0ucRzmyKfYYg3J8MmHXVgHs-KxcItxeZ6wbefK1YdMrYSblHwnXkSiajApB5ds\_EgpJJWYjfbKOjHdsh-H49jG45weOX9v0YBSAqdXmKgoaBcP7A4zDyINMNVt7RWgbQ51WxNTsfBllvQ4)

* Passa alla scheda API ION, copia il nome dell'API e cerca la Chiamata API premendo il pulsante SELEZIONA

![](https://lh7-us.googleusercontent.com/aRXjuD3nkYsFNM2eYkfmHrshU3ycmN5G4OGSFFadbSToy3pHKYWMw6apbyMhJ9o-5xB6UDA4rbdPjZWAdP-OCH8gQFWV5vWXp0rqLxP9DozP4yMS074\_nsHzirJUgBfkBkQ8Ydp\_WjImf2bx3pDnLPE)

* Nel prodotto, seleziona il Punto finale API che hai creato per l'ambiente con cui stai lavorando, che hai creato in ION API. Cerca la seguente chiamata API, seleziona la chiamata API e premi OK.

![](https://lh7-us.googleusercontent.com/LQWk7uiEPCxJcohMmIuRrg2p\_wwE\_h5GoEEP3Y2IdpKARppHoGB4Rt1KRM\_2AiXyG0-ieIV7BM51IRN5exKkhG8eLTkKCftm88j2NLc15X50VLu9t1sZZnQ7DsIIvgUsxz7oryzVIkfmifw-m3qkLDY)

* Successivamente, passa alla scheda Corpo della richiesta

![](https://lh7-us.googleusercontent.com/0tnYxKvtW5Fw7yJfW0QBMclidw5kKJB4oi6M932hGO8ROokbMXbyFcjPQq\_LSVe8hv3ZyVVWqjDO4vMMRgPm1L2iXV3pSoiyzrxGLvBTx4kwt5uo6XtHEt25PRVdM6aIddhHDrT7HGzx3JaZ1F02-YI)

* Qui è dove configurerai il mapping dei campi per questo BOD, la tua configurazione dovrebbe assomigliare a quanto segue. I mapping dei campi sono disponibili qui.

![](https://lh7-us.googleusercontent.com/3giuZYeQjdZZHAg7W-pcAHB\_69KP8Ukh\_0NhATYBxvrS\_Qy3yH58fQyrp6GKfOzi1xJms5KV-XVNnAWtX6VmIBwdxSVum9JA6-H9W3XIUYKiTEK3IWoKA560a5I2lwmYd0kitdfC4pRkQVULyWp9PpA)

Una volta completati i passaggi sopra, avrai configurato con successo il BOD Sync.ChartOfAccounts. Clicca sull'icona PIÙ per aggiungere il prossimo e ultimo BOD.
#### **Sync.CodeDefinition**

La scheda di connessione per il tuo punto di connessione CodeDefinition dovrebbe assomigliare a quanto illustrato di seguito. Assegna al punto di connessione un nome e una descrizione appropriati, nonché importa il Service Account che hai creato.

* Seleziona "Invia a API"

![](https://lh7-us.googleusercontent.com/YLaFsc0K1Lzruo84Np3EdCTF1xsaQOLRypNpgZB7L9keTh1TwPOMnjBxJYnBOj8GrNSG\_URcRGgv\_p70-pjhBed-wvURRW08YtEWjmACMc3CleRPrHia6nihWQwVOUaZ3qHD\_zLy2W\_iMQ0I77cY\_Bs)

* Cerca il BOD Sync.CodeDefinition

![](https://lh7-us.googleusercontent.com/f3ikl4jh0PBhYmP3r80BrHuGGu9w9MHe-E0VmyXOCmFEkkK92cxgVimwyP8RF0kF2GruVaeDjiYRKuONX5bQ2ZBRmdKFx8Bf9cHvX5q-xYnXNH0a2xnR4eg1ynyWbRRRoY5xn28HJ\_ziRiKcTN43aHQ)

![](https://lh7-us.googleusercontent.com/nXQZ1LLZsrndggHkAmRtMlV7YzFemnjC9CnS4AdUVDits4zNfzlaqKdHnNcLyTtDkQSX3SB8R3fnZhGBPd-By8C364IIYc4vE2VXNXzoa4LfHP6irTiAg\_N\_2BHSYBLzaQyMCN1w5LdFiiqeiiwAXuk)

* Passa alla scheda ION API, copia il nome dell'API e cerca la chiamata API premendo il pulsante SELEZIONA

![](https://lh7-us.googleusercontent.com/LbHmVr1PimQkPu-t6VMvNVk9wVXeQBHOu-X4pW-9vGm-dON2buizVGbKekGL7tY1t4OkwQtzhl7uDhq908UxCfDCJaRDEukpk-07pJjLO-ezRUHgblp3REm0qrKF9wOtMkNWJlVVNVhmfzZ0TtUsqQQ)

![](https://lh7-us.googleusercontent.com/K-kDDTSaZiothC4o3JDihhVJFNt0PiBnLK7kF6RcBOX9EpzutfLHGstzvywBBqaEqm4WqOSQSxtvxRPtbVafPlhtf\_YMVkXjhTkvnGwLzwH\_p-YgRCGAu-DzA94MHjqQoAYTSBPgojcGlJs7tBRcpME)

* Successivamente, passa alla scheda Corpo della richiesta

![](https://lh7-us.googleusercontent.com/DfT6FtrbW7LbK4b4I6ssYDWOaPgUxkWsuTDpvQGw549tPFxgEU\_gmh3UwXTbyKHZR8SOHXPHDdobEhA91RIMB57ZAVatrZEsad2QW6QHiUkdZoyW\_yE\_iIGDgs2IrY0I6qL1JTZxksYoaLKu0Il8smU)

* Qui configurerai il mapping dei campi per questo BOD, la tua configurazione dovrebbe assomigliare a quanto segue. I mapping dei campi sono disponibili qui.

![](https://lh7-us.googleusercontent.com/nqK7x1Km4wIP9aWnvMlSHl1\_omw22GRKONfB-zc8ikn\_rSsl60Ksml0oQacs8UNmPSLFSKPD7Eo9FsH42RjDo4oragvHZJHFW\_yv62KXDrF3SKnDN2-X6vqYJ5a-3bYkkvPDlNJSxFylvtAFr-2Kt8Y)

Una volta completati i passaggi sopra indicati, avrai configurato con successo il BOD Sync.CodeDefinition per la tabella dei dati principali M3FlexDimensions.

## **Flusso dati**

Dovrai configurare il seguente flusso dati per l'Auto Accounting:

* ChartOfAccounts

### **ChartOfAccounts**

Una panoramica di questo flusso dati appare come mostrato di seguito (il numero di punti di connessione API DocBits alla fine dipende dal numero di ambienti diversi che stai configurando).

![](https://lh7-us.googleusercontent.com/RfkP8xiF2vDzQhBNa66L0NQHk7TGjj52aK3hWoisEnWbdG3l-SZKKw8mYJ3b28ShXZ9omPS6WdNiXaCpYRQzwfges0SKznwQal7K2ElILbGBJNYu3VFm6gDQJMHYRItAFX0cdRZjXgCk2FQqHJ4iSjY)

### **Azienda M3**

![](https://lh7-us.googleusercontent.com/tqYoI-gLUpe0c0x1T-WhP0\_FolVzPGHhFY8m52Fw38mJNzsDvjb7stRrBfWVjXLnFrJTTy2lyd9Dmva3\_EPG5eRWyf5ATA2cTWvCj3Ksa4Fu4pHF6rNFjfd3Cjei0UlibT0HAQYE0V22bdTStjY61zk)

La configurazione per questo punto di connessione dipende dall'azienda M3 che contiene i dati principali che desideri importare in DocBits, la tua dovrebbe assomigliare a quanto mostrato di seguito.

![](https://lh7-us.googleusercontent.com/wpSluEs21T5wXG0egZPfUCYBP6X\_uUm6XAh-PyD8RrojTuIztzRJzhVYdzcNI5dQGGDsrhSKx\_K2-y0JDmK9w41fVUXWcW1N2lz5rizXcMnn5BuiaGRy-TEOBryGxvP9mBGJTZ16lMisoC\_YumwpS9Q)

### **Documenti**

![](https://lh7-us.googleusercontent.com/uR6XaFI7TPQ4L8Suom25PBdtXdL4i100Juz7kRBxT5rdxhejZW7nPtVIlEGjWWnZLbo9ipx7G95NBFV8dd-g4vw\_vM-uPApJ02QdxvCmX27bwAW\_qUWUXajV6BFVmIfzTQ46Zj4DybsYKKblXjuWc6w)

I seguenti documenti devono essere aggiunti al flusso dati:

* Sync.ChartOfAccounts
* Sync.CodeDefinition

![](https://lh7-us.googleusercontent.com/6Bq-yQ9Yaf2OJwjBxyFvqAMUitcovquo\_iU4hc-pgag1iDwLcstggVjLsdY3bRl9XWNc3mKOwZrY1FSlu47IzxxUQHFkjIAl1r08Iw9UbKaaMh4WiWrqFuSObdTjEvCEI5IDvD\_Pys8jAydydJgbsK8)
### **Filtro**

![](https://lh7-us.googleusercontent.com/LyKGzQUEswTD1XfpNDPSHjChgqNFfs4guXfM0KNuW2fPoiaeUo4uPrlGgwt3RepWUGQmu_trUMiWb68cUjUAwXU9IRoWOsv9M2l5v4zFfBkEcioz5ok7Eoss7I-tBKtpD7wVUkGWi3U3ySrIQ_fDPiY)

Per il secondo percorso del flusso di dati (in base all'instradamento nel flusso di dati), applichiamo un filtro con la seguente configurazione.

![](https://lh7-us.googleusercontent.com/7xdqGdo9bS6_IIzTVYF_08woBXvhIVkA-c6-ZrDpDEzmEDFzDZSuxZ5LYHKVUhJqYq4Wlq1FXPfr5myjKFUsMbnJrefc_L7URD7AbEq_D90jEw7o8Yrhg5XZwLdU83OwlZVXqlYla61b0LyISXeBLWk)

![](https://lh7-us.googleusercontent.com/OdI-0FaqDaPKy2g9Mr8HUx_oGRZkDrkeI6P1rWqOounpDauMThaqzs2wOawmw3RwcMlQHgI6wj16RXQDAP_JNMGkxvmiEnPJ_bvse2CvMegPwinSIJRLmXaCzfjxtB1FDqnqPOMwrMYNKJyiC2sGUe8)

![](https://lh7-us.googleusercontent.com/RMPIV6ZWsUcBA6klny6Ln-_nhMGl1zdEHfUKK56owelabcG-6gM1S_eqWAVLTeOHdec3D5D6xVJeC5evnJC61L8daV6IbJbCmMashkWXSK4Tv4RdE_erjR-Mk2RihPodIG4HrqSOQ8hi7SG3xctXd-E)

### **DocBits (ChartOfAccounts)**

![](https://lh7-us.googleusercontent.com/Npm92rS_EO5roSy3tldC88hFIyiDnZjHnnVSkkKyfmNrOcbuVj4LPNrcsWvOT8IHNQKGMqIZymG9q3VMGG6RwvuRBqZgmhHxqXn1oieajDmz8giQxSr8wOFzb8TQTJJWwj912-sDRtkrDAXCr7ne-pk)

Qui è dove aggiungi il punto di connessione API ChartOfAccounts che hai creato in precedenza, la configurazione per questo dovrebbe assomigliare a questa

![](https://lh7-us.googleusercontent.com/Dw4y6OMuMAYHZjH1etj_FqdsaFxaRhQyk6_PaxXrWLhrNirEn7xQc5uIpbDT6Wz85XvZgY02aNuWfbYKBzo6W9aavN_Asu5ENfr2dszWYQqs9sy6zl4o0NxRe3IPXodLIGf9JkbK2_UtYe4dVii0JbM)

## **Attivazione BOD**

Una volta completato tutto quanto sopra, dovrai navigare su Infor M3 e attivare i BOD per far sì che i vari dati principali di cui hai bisogno per l'Auto Accounting arrivino in DocBits.

Inizia premendo Command + r, per aprire il menu di prompt, digita "evs006" e premi invio.

![](https://lh7-us.googleusercontent.com/pzAL0cnM94AUE4KmTyBV8OPU9ft_g9o0-KB9Ib0AjrvG7Q59GHT-2biP4n7yFyXRxQ0gjy85G6MWMWUeMIWJcTQ9TKwzCEywd7I_6_vV-muepobkW0O-4-CZxsmjOEQ7uM1frZpTLqlLS3aSYkEuwAw)

Ti verrà mostrato il seguente menu

![](https://lh7-us.googleusercontent.com/Wx41TNpg1zuaf1rXIBvSCVzSRf6q74rdLs91el21iErqQnDiF4cv7X0nyDaS2Gjimj7xbfAK-7mo6sXN6fkK934mHnCnivFTz9NqHi6dBoMYiRT_vLrkVUlFd_T4Oan3Zkq3WKLoI-kmsElHSKO7zY0)

Per aggiungere i vari BOD dovrai inserire i nomi dei BOD e i nomi delle tabelle per ciascun BOD singolarmente.

![](https://lh7-us.googleusercontent.com/5gVWRDm_8CSyoQRkq-7LuI8MLU1BjRN6Z6YCcVZp7G3Be62nQBht-eUNZreTzV2rFWYK_RcKiyzwTTlT5y5X8eGf-Z7qDavDyHML0zv6Yt6jGu2z9d-nL0K-m446nDZa2-aiFLnnzjAwk8pTT4RQK6Q)

I BOD che devi aggiungere includono:

* ChartOfAccounts
* CodeDefinition
* CodeDefinitionAccountingDimension

Per aggiungere il nuovo BOD, dopo aver inserito il Nome del BOD e il Nome della Tabella, premi sull'icona pLUS indicata di seguito

![](https://lh7-us.googleusercontent.com/66wclj8g8RAYT9-UIgRMs0qnuA9srmWv21PdqdNm_q5icGmabL17-DpLOSs4pm6Nj3xJN-9xt7io_5GZGfzSQ2qt_8Y--CJFou6FaOdufiuxOdKHrUUYELNdGy9e-gnWg_hAMSfs_NJa6zYBMpoyTVs)

I nomi dei BOD e delle tabelle sono i seguenti.

**ChartOfAccounts**

* Nome del BOD: ChartOfAccounts
* Nome della Tabella: FCHACC

**CodeDefinition**

* Nome del BOD: CodeDefinitionAccountingDimension
* Nome della Tabella: FCHACC

### **Pubblicazione BOD**

Dopo aver aggiunto ciascun BOD, fai clic destro sul BOD aggiunto, seleziona Correlati e quindi Esegui.

![](https://lh7-us.googleusercontent.com/225-ujyGzG_RJOXgbx8NOh_4s-Sn_o80b_h0DTsJqfr6OcyPUwkWLF2lfEyzFFFKddKmlWd32bb94qeYlOdVBTI8RL0r6ZfZKloVTrAYLNp-U5gL3aJhW4d72ExkkyM4AydLczsPvdE1cRDfGNKupdA)

Verrai portato a questa schermata.

Cambia il Verbo BOD in "sync" e premi AVANTI.

![](https://lh7-us.googleusercontent.com/3DyjXUSlAF7msQT1OAO3aCr1U9R68XZj0oE_yJwsBrBj-FkiZR-oRYQYSClHG0iN0FXFdDdKQA1hOBlw3jc-lXQCWkiDFa0IweuQnoR8k-Mgyp1HeI5ImJqNogz-Q3b3P33ywb0B2o1pZ-TkZ7mAwZA)

Una volta premuto AVANTI, riceverai una notifica che indica che il processo di pubblicazione dei BOD è iniziato.
### **Elemento di costo**

Per importare la tabella m3costingelement in DocBits, è necessario seguire i seguenti passaggi.

Dalla Homepage di M3, digitare Command + r e cercare il prompt "PPS280".

Selezionare una qualsiasi delle righe visualizzate. Nel menu successivo, selezionare STRUMENTI e "Esporta su Excel".

![](https://lh7-us.googleusercontent.com/I8SYWm-JwpyYRHFUp2obGtXcsa7m\_blJ\_lTrnhczztRIXIN5gfxCt3eRw6ZI42fH6AwnsKyv4ux5-rhaT505PsyDFFI\_anUNvmACFyx\_ssgxaqWq25vLt\_E5s310HNoiPPLf35qJlYtstjpj5Cc4aB4)

Selezionare "Esporta tutte le righe" e poi premere ESORTA.

![](https://lh7-us.googleusercontent.com/wtjHI9L4YUhf-yJFjcPGu218Vis\_zELtCIfpmkIUKgasfrdfNW-dr\_J1DqXlfD-SBrnVduDrMLAIAQh6UTlzBqEP\_JPXP48elGMyGj0ByZbX7TpqlnIfRZ4ZoD0pyCo-AKigeKjlHN6cFcdpeClZ9L4)

Una volta scaricato, sarà necessario modificare il file Excel prima di convertirlo in un file CSV.

Sarà necessario aprire il file Excel, che avrà un aspetto simile a quanto mostrato di seguito.

![](https://lh7-us.googleusercontent.com/l4WbidK-5zSEQ6rwqhknudPBmmDji0f1WwTh-kHomSkgEOA7s4m72cLw8z-4nflqBvPp\_2AajIEZDZz4dRLs8jlAeYHp4ee2tDysxYy8YBjj4ktHxdUXpxO\_Z34c8\_f0cNMX-9lp0lT5wOZoH1QUCgE)

Da questo foglio Excel sono necessarie solo le prime 2 colonne, modificare il foglio Excel in modo che il risultato finale sia simile a quanto segue.

![](https://lh7-us.googleusercontent.com/QaNRlKHrU6kZWFqmwYR8C\_\_nLVOeqowAxJlvooSVBIAF5ayx2xZtUppsn0jzBcJVi90vemM3tZMZOjn549N3RzMuWuE3w911WLVS5NMuiUmnfXM\_xUXbqmzBtiQZstnpEYj1dUSbs\_IkAydlhBfdmcc)

Una volta completato, salvare il file come CSV.

Una volta ottenuto il file CSV, andare alla seguente pagina web. Questo dipende dall'ambiente che si sta utilizzando:

* Prod: http://api.docbits.com/
* Sandbox: http://sandbox.api.docbits.com/
* Stage: http://stage.api.docbits.com/
* Demo: http://demo.api.docbits.com/
* Dev: http://dev.api.docbits.com/

Qui sarà necessario caricare manualmente la tabella CostingElement tramite un'API. Fare clic sul pulsante Autorizza.

![](https://lh7-us.googleusercontent.com/tyzOq3BR2QqTguQFKicxo0dE5j5hGsP-BhfVbS81O\_mxN5bSVp40jYfgsVJcE\_rBLFMDJNvbPkPIdjPqaqoNbHBBM-9hx0i-U4VAH9ISBYhpwKgqQeUEd67VV1E4izwNyxbAwwrhCmrAo1uIKhLherY)

Sarà necessario inserire la Chiave API del proprio ambiente DocBits. Questa si trova in Impostazioni sotto Integrazione.

![](https://lh7-us.googleusercontent.com/4ADnevq6kq\_vbxUJpyPbHNcGvRvpO-l9Gwd8ZaYf\_vO4uWhSl1jmKNpddmHGc9ZHMMbXCgLOElLDYbNwB3INmBDETecPrDnpI601IUOZQlT7tc7OLSPXwkooOJFNwML2i\_gvBPuE8CvfwRpX-ZIlb\_g)

Una volta completato, cercare l'API chiamata master\_data\_lookup/import\_data e compilare le informazioni richieste. Una volta completato, fare clic su ESEGUI per attivare l'API.

![](https://lh7-us.googleusercontent.com/8UD4FhFv2dRB4cMjCDL4G9ndjH7laVMKWqdeMaJGgEo48-UVvucB1uOydzNdfFy0yPM5bb66mZB4k9uJR7TTiEREGFaV2EqW01gxJpTyuUfGNh5QmBjySkyhZ56gWV8sYs8WI5RnHcENtXgjTU0vg0Q)

Se eseguito correttamente, la tabella M3CostingElement dovrebbe ora trovarsi nel tuo ambiente DocBits. La Contabilità Automatica per M3 è stata configurata per il tuo ambiente.
