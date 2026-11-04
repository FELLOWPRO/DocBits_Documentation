# Costruttore di layout

{% embed url="https://youtu.be/-m45XGiIeig" %}
DocBits Layout Builder Tutorial: Create Custom Document Layouts for Faster, Cleaner Validation
{% endembed %}

## **Accesso al costruttore di layout**

Innanzitutto, assicurati che la funzionalità del costruttore di layout sia attivata. Questo può essere fatto navigando su Impostazioni → Elaborazione documenti → Modulo → Tipo di documento e assicurati che il cursore del costruttore di layout sia impostato su attivo come mostrato di seguito.

![](https://lh7-us.googleusercontent.com/I0VvFiFftKLoCB47jCAoosfTyqIQgXBoggMFp1QAeIj9xW4yiiIzyk5eIEHZ7duA251Yc4\_ArUKA8e-LjDht13bckAnkAOHOvl1p5k1-Qj\_UkEp2cSZwxHz\_PXe8IQ4\_jglzCtjAJg5pd9m\_hNZEhXA)

Una volta fatto ciò, puoi accedere al costruttore di layout tramite Impostazioni → Tipi di documento, una volta su questa pagina, puoi selezionare tra i vari tipi di documento che hai creato e selezionare "Modifica layout" come mostrato di seguito

![](https://lh7-us.googleusercontent.com/WMD8M0qugnc64ZuyLuEYH5P63qk-Vo86useg32-QyOsP63FJA\_Xh7UzwlwmUR3K9oTd19aXexSitZqQLVEKo26-i8hYWUS9CChzwAS8TgbWoqweFucJcNIgKBruzSd0mxn8zrh9i46lPxKMNDh-YEJ8)

oppure se hai sottotipi di documento all'interno di un tipo di documento creato puoi selezionare "Sottotipi di documento" e selezionare "Modifica layout" per il layout del sottotipo di documento che desideri modificare come mostrato di seguito.

![](https://lh7-us.googleusercontent.com/KfmM8wMGnn5tzXRxF1yT0Efm7X6v0kYeGzgNG3RihERh\_P71tjEVkJh4POMwgqnsCBoE736xI7oHkmpYNUbtAShhE-wAHsnLuxljDtmhGQUyljF\_PmOF2y6c0gIdIk\_jUD3sVNsq5viT2sb236OBYSA)

## **Principi base del gestore di layout**

Dopo aver seguito i passaggi precedenti, raggiungerai una pagina come quella mostrata di seguito.

### **Caricamento di un documento di esempio**

Per caricare un documento nel costruttore di layout, basta navigare a destra dello schermo

![](https://lh7-us.googleusercontent.com/I99BkFDTOloyKwwc0P8O3wf8FbKL3B5Zn5i3GfeRKSSkBdelQ\_HNfI2oJzaXQUi\_UU6R5Vr7jrgcAxIrDmmTKWgTZx90J7izOX0oczWt\_\_qt9VmD1HqafZvqH8vb7xnZMR1m5pjwzsbcnalErYo6dIc)

Clicca sul pulsante "Carica documenti" o trascina e rilascia il documento desiderato nell'area fornita

![](https://lh7-us.googleusercontent.com/GHqGYqvwFvN3z2ojFz\_i7ZLlZhy-A3vsKUmmzOC0NMkPd2-f6\_t\_0USF66W-N3XRqHlmx06QNSQ7U-VTPQPKWdzOhoNcN7LlMk45sKVC6bWN1O92G0r4dKyHQLlgmGZiINYjZ9vZnt89\_BjgzbON2MI)

### **Gruppi**

I gruppi possono essere creati selezionando l'icona seguente.

![](https://lh7-us.googleusercontent.com/eb4jnCmezPFKPwgUisJKvicBqMWuGHW69WIFdtpmQiY-\_78VWmMyMD4TqKMJXwjH1XDnS5RXX0DsJ2\_ur\_GG62L4F7OEzkLrpgwUkiuQjZQPJqQoHIBj6WM33zY0AkYXhI3mKLjZetbEQ2AlhPJ8KV8)

I gruppi ti consentono di creare diverse sezioni su un layout, rendendo più facile separare diversi gruppi di dati o informazioni per rendere più semplice seguire un layout. Puoi creare un titolo per ciascun gruppo in modo che un utente possa sapere quali informazioni troverà in quel gruppo.

![](https://lh7-us.googleusercontent.com/lWqIEC-TCOp4rKytTbhn2fYWY618\_Yra2mjWHA9oMyWPqHXA5JKCLoZoEtM8xQHAkn4HFNTPYpbMePUYnQhQGL0KmgBfTEDWPDAMy7PjZinZl2s\_kHQlsLAGjYbzSINWTme3qRO9tHLcpVaDVvS\_8F4)

### **Elementi del modulo**

![](https://lh7-us.googleusercontent.com/OFBRSGdol7loocu5uGVe4Q8URMDojvXTN0xj3TCgL-jb-wUgt1fjEqfXCyMPz\_HNh94LVVmg6ifQDhxvlQsgbbChRfrw2Ohx4ICOUwHix3iiAFY9hI3BPGBfcNABiHLhgXQJVZmGvEO\_niVWkIXz\_6g)

Si tratta di un insieme di campi predefiniti che possono essere trascinati e rilasciati nel costruttore di layout e sono disponibili per creare il layout desiderato. Questi includono:

* Testo - Questo è un riquadro di testo che crea un campo nel layout in cui è possibile inserire del testo una volta sulla schermata di convalida.
* Etichetta - Questo è un campo che può essere utilizzato per creare testo non modificabile, potrebbe essere utilizzato per creare sottotitoli o qualsiasi altro testo non modificabile desiderato sulla schermata di convalida.
* Casella di controllo - Questo crea un campo di tipo booleano che può essere selezionato o deselezionato.
* Casella di controllo multipla - Questa funziona allo stesso modo della "Casella di controllo" ma può essere utilizzata quando l'utente sa che aggiungerà più caselle di controllo in una sezione.
* Separatore orizzontale - Questo crea una linea orizzontale sul layout che può essere utilizzata per dividere le sezioni all'interno di un gruppo sul layout.
* Tabella di caselle di controllo - Questo consente all'utente di creare una tabella di caselle di controllo costituita da valori personalizzati sugli assi x e y, ad es.

![](https://lh7-us.googleusercontent.com/lMZU68H4i8ELjgenpcNXeNhJ9iwzTWGRkjNMEdV3rqdGwnaRZ\_tvG9mbx2ogXQ2hMciGSp-9m1c5KS9VwGJWzuxcRiaioVDSLTLvh-csHUho4aX25LXrtjhGSfK6yTukufwrjQvZR-JliuhiaPCCxpw)

* Pulsante - Questo crea un pulsante cliccabile sulla schermata di convalida all'interno del layout che può essere impostato su una delle tre funzioni, tra cui: Esporta, Esporta con richiesta speciale o Rifiuta.
* Tabelle estratte - Questo ti consente di posizionare un'area sul layout del documento che illustra la tabella estratta dal documento. Per informazioni clicca qui.
* Pulsanti fattura - Questo elemento ti consente di trascinare e rilasciare un set di pulsanti ottimizzati per le fatture. Quando sei sulla schermata di convalida, se selezioni il tipo di fattura (costo o acquisto) il corrispondente abbinamento PO o Contabilità automatica scomparirà di conseguenza.

![](https://lh7-us.googleusercontent.com/-w5iTr9b\_pcc6Y39osFmuzKQGRa\_e4tAXvQOn1zN8T4HwcuTs\_FP9mFPAJJeABvYKTyiQr3xZALsRgueIDksbswhnY-E9ioT1AIaf8xwAblBckX1f8xzi5v9mLxBRRUZoViDntKK6Nd5fy5sd5Bq5LU)

* Campi QR Code - Questo elemento ti consente di trascinare e rilasciare un blocco che visualizzerà tutte le informazioni estratte da un documento quando è presente un codice QR.
### **Creazione di campi specifici del documento**

L'utente è in grado di creare i propri gruppi e campi personalizzati per un tipo di documento, questo può essere fatto durante la creazione iniziale di un tipo di documento ma anche selezionando "Campi" quando si è sulla pagina dei Tipi di Documento nelle Impostazioni.

![](https://lh7-us.googleusercontent.com/N9i3KnGyXATf5jLVbPQGiPEG9rlz6WqHJ5c8FZnpw3EwmaMnl2cQhMwhug3d-A82caOS6Nxc7LgAVLMtBL404hKR7i39u2RfwzCnohqn1\_mbkMtjzNKThnjGu2ivaFNqKDuobzA6kUdD8gGiQ\_zs3z8)

### **Spazi vuoti**

#### **La regola del 100 percento**

![](https://lh7-us.googleusercontent.com/TwNA3gZrgzhSvZrZOGywGYz92fRkUtjIsr6sDCxEzYgWcfJ9kXuzJKkqNiFyp3H5XXoqUz76TzZ72r86YY\_O3Vw\_rvDKczD\_hdMOIQOFWORr2bo8pGunrAtUklJ1ye7KEQJEjRNqNUNCnXM0boIICUA)

Per creare lo spazio sopra nel layout, un "Etichetta" dagli Elementi del Modulo deve essere utilizzata in modo speciale. Il motivo di ciò è che il Gestore del Layout funziona secondo un sistema di 100 spazi per linea in cui 1 spazio rappresenta l'1 percento di una linea, questo significa che i campi possono occupare solo 100 spazi per linea come mostrato di seguito.

![](https://lh7-us.googleusercontent.com/YTqddzVQPWRuP5ylV6NnMc-KnEgCY0ZxZ8zn0In5d5dOxaWnwGDi4N2qohbobLNphLfVD61sMUE5QlmXJZ3e0tP7Y8no\_wVRy9WTF0nWIN5Tg3t-zLJhs9M-kVYPFV3CyerRZZoK-iMXLmKGcuSY\_Nw)

Ciò significa che l'utente deve costruire il layout linea per linea secondo questa regola. Ad esempio, diciamo che si desidera aggiungere i campi "Nome" e "Data" nella stessa linea ma si vuole che il campo "Nome" sia più grande. Questo può essere fatto trascinando e rilasciando il campo "Testo" dal menu a discesa degli Elementi del Campo e nominando ciascun campo "Nome" e "Data" come mostrato.

![](https://lh7-us.googleusercontent.com/2ru3pj0iD3V6ADqYBjeQPqDT3uvTH\_Al2MV0gpUUQ9MpX0TSFtnjYL6JN0YOkBk9afx2q2YcMo4gWE2jItUAGSEfX79O\_6sFgKwP5FGa98SwzgjGgee1G-2aO6NyqZusf27SbJoWoHmzu51Hx25kVmM)

Il problema ora esiste nel fatto che sono entrambi della stessa dimensione di 33 (questa è la dimensione predefinita di tutti i campi trascinati e rilasciati) ma si desidera che il campo "Nome" sia più grande del campo "Data" e entrambi i campi dovrebbero occupare l'intera linea nel layout. Pertanto, seguendo la regola del 100 percento, è possibile impostare i campi "Nome" e "Data" su qualsiasi combinazione di 100 desiderata. Questo naturalmente dipende da quanto si desidera che sia grande ciascun campo individuale ma per lo scopo di questo esempio imposteremo il campo "Nome" su 70 e il campo "Data" su 30, i risultati sono:

![](https://lh7-us.googleusercontent.com/m411QblkCfsQWllhX74QpANjuVEv3fgM1Nhg8cJjbkNQGcjym6v0JFHIrKyMOAu-MasQ4KH9ZPaxmqNWfhWmAuL6SOZE030NXebb7ERzYxF99hLJC6oGbM-YXp7bNdZuoTaPmsDt7EjpV5BOiflwA4g)

Questa stessa regola si applica a tutti i campi nel Layout Builder.

#### **Creazione di spazi vuoti**

Ora che questa regola è stata spiegata, la creazione di spazi vuoti avrà più senso. Come già menzionato, per creare uno spazio vuoto è necessario utilizzare un "Etichetta" dagli Elementi del Modulo.

Ad esempio, diciamo che si desidera creare uno spazio vuoto tra questi due campi.

![](https://lh7-us.googleusercontent.com/jOms6aTB3wCmX3L-MiUTrOb\_-q3AiFC3Y75TsHJe8QFLru10H9aZKzbE5MfHPZ0v9fqycQeddNPJp7pnRjv17crkrYUymNA8u9bF-3u9IfR6ru\_duavqrLCQocommljzLA00RXs\_lQA4gDH6l\_QvyTs)

Il primo passo è trascinare e rilasciare un "Etichetta" tra questi due campi, una volta aggiunta è possibile fare clic sul campo "Etichetta" appena aggiunto e sulla sinistra ti verranno presentate le proprietà del campo. Ora, allo stesso modo in cui creeresti o cambieresti il nome di un campo come mostrato in precedenza, rimuoverai qualsiasi nome dalla proprietà "Etichetta" come segue

![](https://lh7-us.googleusercontent.com/0Mma4wYIIfAkOyRIFLZtjug7pbWltfaiPm3r\_WgbP5fCgKe2BGD6Qf5YJ5Ns7fBBTRfJ68NlOtmOQrvcOvjyWGxk9v\_XmDj-8moEQhcDUugh\_VO5DdrJLYYV08ftr8YdhuhEM0otWs\_ljew18j7XJFQ)

Il risultato di ciò sarà quindi

![](https://lh7-us.googleusercontent.com/-HqoJUAbcHRCletgSg6gcKXpn6zto1Do8I5EmcEmPWL4qUrMREh-wZdhy7ZKtnbuGjypd7p2mjcIu6LbbfdjA3c1liT2reCQXWiP1VAji08eWc\_bbF\_a0Dd82rJRgCuD5yjdlXL\_DNheMcw-fm6pQnA)

Ora c'è uno spazio tra i due campi. Questo spazio può essere esteso o accorciato secondo la regola del 100 percento discussa in precedenza, e con queste funzioni è possibile creare qualsiasi layout desiderato.
