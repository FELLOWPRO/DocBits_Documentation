# Key Concept: Tolerance Window

Prima di esaminare gli operatori, è importante capire come viene calcolata la finestra di tolleranza.

## Cos'è una finestra di tolleranza?

La finestra di tolleranza definisce un intervallo di date accettabili attorno alla data di consegna promessa dell'ordine d'acquisto.

**Esempio:**

* Data dell'ordine d'acquisto: **9 gennaio**
* Giorni di tolleranza: **3**
* Finestra di tolleranza: **6 gennaio → 12 gennaio**

> <mark style="color:red;">Solo gli</mark> <mark style="color:red;"></mark><mark style="color:red;">**Allowed Tolerance Days**</mark> <mark style="color:red;"></mark><mark style="color:red;">selezionati (giorni della settimana) vengono conteggiati nel calcolo di questa finestra.</mark>

### Esempio di timeline visiva

```
← Past                           Future →
|-----|-----|-----|-----|-----|-----|-----|
     6 Jan      9 Jan      12 Jan
   (Start)    (PO Date)     (End)
```

### Comportamento degli operatori spiegato con esempi

* **Equals (=)**
  * **Significato:**\
    La data di consegna della riga articolo deve ricadere _all'interno_ della finestra di tolleranza.
  * **Date valide:**
    * Qualsiasi data tra il **6 gen e il 12 gen** (inclusi)
  * **Date non valide:**
    * Qualsiasi data **precedente al 6 gen**
    * Qualsiasi data **successiva al 12 gen**
* **Not Equals (≠)**
  * **Significato:**\
    La data di consegna della riga articolo deve ricadere _al di fuori_ della finestra di tolleranza.
  * **Date valide:**
    * Qualsiasi data **precedente al 6 gen**
    * Qualsiasi data **successiva al 12 gen**
  * **Date non valide:**
    * Date tra il **6 gen e il 12 gen**
* **Greater or Equals (≥)**
  * **Significato:**\
    La data di consegna della riga articolo deve essere all'**inizio della finestra di tolleranza** o successiva.
  * **Date valide:**
    * **6 gen → qualsiasi data futura**
  * **Date non valide:**
    * Qualsiasi data **precedente al 6 gen**
  * <mark style="color:red;">**Importante:**</mark>\
    Questo operatore consente date _all'interno_ della finestra di tolleranza **e oltre di essa**.
* **Lesser or Equals (≤)**
  * **Significato:**\
    La data di consegna della riga articolo deve essere alla **fine della finestra di tolleranza** o precedente.
  * **Date valide:**
    * Qualsiasi data passata fino al **12 gen**
  * **Date non valide:**
    * Qualsiasi data **successiva al 12 gen**
* **Greater Than (>)**
  * **Significato:**\
    La data di consegna della riga articolo deve essere _strettamente successiva_ alla finestra di tolleranza.
  * **Date valide:**
    * **13 gen → qualsiasi data futura**
  * **Date non valide:**
    * Qualsiasi data **pari o precedente al 12 gen**
* **Lesser Than (<)**
  * **Significato:**\
    La data di consegna della riga articolo deve essere _strettamente precedente_ alla finestra di tolleranza.
  * **Date valide:**
    * Qualsiasi data **precedente al 6 gen**
  * **Date non valide:**
    * Qualsiasi data **pari o successiva al 6 gen**

## Come gli "Allowed Tolerance Days" influenzano la finestra di tolleranza

Nel calcolo della finestra di tolleranza, **vengono conteggiati solo i giorni della settimana selezionati**.\
I giorni non selezionati (come i weekend o i giorni feriali esclusi) vengono **saltati completamente**

#### Esempio: calcolo della tolleranza basato sui giorni della settimana

**Configurazione:**

* Data dell'ordine d'acquisto: **mercoledì 9 gennaio**
* Giorni di tolleranza: **3**
* Allowed Tolerance Days: **lunedì, martedì, mercoledì, giovedì, venerdì**
* Weekend (sabato, domenica): **Non selezionati**

#### Calcolo passo dopo passo

Partendo dalla data dell'ordine d'acquisto (**9 gen**):

**Conteggio all'indietro (3 giorni di tolleranza):**

* Martedì 8 gen → **Giorno 1**
* Lunedì 7 gen → **Giorno 2**
* Domenica 6 gen → _Saltato (non consentito)_
* Sabato 5 gen → _Saltato (non consentito)_
* Venerdì 4 gen → **Giorno 3**

➡ **Data di inizio della tolleranza: venerdì 4 gennaio**

**Conteggio in avanti (3 giorni di tolleranza):**

* Giovedì 10 gen → **Giorno 1**
* Venerdì 11 gen → **Giorno 2**
* Sabato 12 gen → _Saltato_
* Domenica 13 gen → _Saltato_
* Lunedì 14 gen → **Giorno 3**

➡ **Data di fine della tolleranza: lunedì 14 gennaio**

#### Finestra di tolleranza risultante

```
4 January  →  14 January
```

#### Perché è importante

Se gli Allowed Tolerance Days sono configurati in modo errato:

* Le date di consegna potrebbero apparire **inaspettatamente valide o non valide**
* Le consegne anticipate o in ritardo potrebbero non essere rilevate correttamente
