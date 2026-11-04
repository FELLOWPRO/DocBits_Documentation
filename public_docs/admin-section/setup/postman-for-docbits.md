# Postman per DocBits

Questa guida ti mostrerà come fare richieste HTTP alla tua organizzazione DocBits tramite Postman. È facile da usare e molto utile per gli amministratori dell'organizzazione.

## Configurazione

Prima di tutto, scarica Postman sul tuo sistema e accedi/registrati.

Segui ora questa guida passo dopo passo per imparare come funzionano le richieste HTTP in Postman.

Autorizzazione in Postman

Prima di poter creare le tue richieste HTTP, devi inserire la tua chiave API da DocBits per autorizzarle.

* Clicca sulla scheda \`Autorizzazione\` e scegli \`Chiave API\` come tipo di autorizzazione.

![](https://lh7-us.googleusercontent.com/L3GaBZJvReeINaKbkq3VYQ9UHTBoKUA3nJkfyLqk61q5xaOJnmMLhbrEbgUgLEyYRkewHuLIAVzoYCZ6quHq0pwx\_69FEYJjzYllivB8WzdAtTFSrzl8VeFthbMsEB9sGjcGlVN38DXEXUwuNEPL6hg)

* Compila i valori. Inserisci "X-API-key" nel campo \`Chiave\` e la tua chiave API come valore (trovata nel menu Impostazioni di DocBits sotto Integrazione) Seleziona Aggiungi a \`Intestazione\`.

&#x20;

* Dovrebbe apparire così:

![](https://lh7-us.googleusercontent.com/SmNfci4z8ECTeXzFPE9YQ8nCzCRHglc\_7RR1cN8a8F7KvYWjJcBnY5wpl7q0AV8bfNLkMk8F4F4aw8j4xMK50HJweBRBPo8EasTn-FG-fmlUJQ41aUX-dvTeWP\_xJQThi8A6EwJl3qIc-Dw1B5W9fVE)

### API DocBits

Disponibile su https://api.polydocs.io

* Clicca su Autorizza nell'angolo in alto a destra

![](https://lh7-us.googleusercontent.com/kuztHpkmRWlOYSU27r97KH15SJHPF\_hn\_eX3C1DYLVYCwMHXfLjYSyFubUCvlQiBt5q3xY0XBPmkcP6AnKF2C0Mdtx3tg\_dU\_qxqAmI6axYIsXR36\_YBz6j455K3-c2SBu4YzmYIXq8VXQxzgL-0j90)

* Inserisci la tua chiave API e conferma cliccando su \`Autorizza\`

![](https://lh7-us.googleusercontent.com/zLhgpdjMnxqNBdjgtDxFEKglICIZul7dgmfFFm2hSnsDQ-HsZHRKRikZ0lcanGYkkZj4waC85mEUFO951ydVnY\_\_m\_TrMrsK3vrDv9FKL-adgWL4lJqp3cSxPeClBm9IHG2cXinRsv12xTeh3psQfO4)

### Crea un nuovo Spazio di lavoro in Postman

* Clicca su Spazi di lavoro e crea un nuovo spazio di lavoro (puoi dargli il nome che desideri)

![](https://lh7-us.googleusercontent.com/3rZw7jhOgVpkZuer58fPEKqDspJjK3S1lp3XpQuvE4c9212a0ALB-p7oLRwPqEbj10MpoCWsb7V9fPqiAdVvigE00x9mN5-lHFXZVVxlkeroBJd2ratgkJVJDM4LJkUJsycyl6tnFKazcFPY-vWtH2Q)

* Devi selezionare la visibilità che determina chi può accedere a questo spazio di lavoro.

![](https://lh7-us.googleusercontent.com/ZajvDtMvfM5J\_Go3n\_PgzD3RXTMQAlST8\_3WnsTQ4-iw7e0QdAa3wqFk7Y0gt78IJVjNTN-5E72c1127CpXJWb8WbfDolxENLqxg5VZLPEK7-hxsNwbAyMceSHfeVy6v-b9QT0kFwnMibWndEAJ2lXA)

* Dopo aver effettuato la tua selezione e cliccato su \`Crea Spazio di lavoro\` seleziona Collezioni sul lato sinistro dell'applicazione e crea una nuova raccolta per le tue richieste HTTP cliccando su \`+\`.

![](https://lh7-us.googleusercontent.com/mbC5t86vaB2G7FQp-40XN-SHc019LKitfUeXRzbcG4HpNai5FPapShx9swHX3mz0va8QFsUQiYn-bhjvER0XYOEDRJpI9x3wG4NgRZCd4beU1NyKJd86bSGubxVbRCtz8HkTDZd28Z7Ice3rmscFMMo)

In questa raccolta, puoi aggiungere più richieste HTTP. Per farlo, clicca sui 3 punti della raccolta e seleziona \`Aggiungi richiesta\`.

![](https://lh7-us.googleusercontent.com/S5W75clJz7JqoIWPbKBjrJqpTAwjS51Pu4dTU160Q7i6oW-HPnb7aN8WRK2AyAb6-HEqTYMZTy9563P0sq53MAjGpVg1JivZX2ATHa6GeFbTX2UCjud7ot8Y\_ksBuUbUfyEfxIDziV8TN3zDfX9Se58)

## Esempio del metodo "GET"

Il metodo GET è molto utile per ottenere informazioni su utenti, sub-organizzazioni, documenti elaborati e molto altro.

* Scegli il metodo GET nella tua richiesta HTTP.
* Autorizzati come descritto sopra.
* Apri https://api.polydocs.io e aggiungi il percorso della funzione dietro l'URL di Polydocs. Per esempio:

![](https://lh7-us.googleusercontent.com/pIdgyqP7g1UwZbY5yaz1KAnKe\_ESs\_kQyiWAXXM-ukRKakS\_\_OL\_LS9J-07hZnZDf8QqtoN\_lKyuhvOIIIF-4Wp0dkofZYQwXZ0hu2RM0YogRxJah-zf8W\_cDNFf8xsec1tYIsfe0SpBuvdCG4WHMU0)

* Ora incolla questo link nella casella di testo accanto al metodo GET in Postman.

Clicca su \`Invia\` e dovresti ricevere tutte le informazioni su ogni utente nella tua organizzazione.

## Esempio del metodo "POST"

Il metodo POST viene solitamente utilizzato per creare utenti o organizzazioni, ad esempio. Questo metodo inserisce informazioni nel database.

Crea Utente

* Seleziona il metodo POST.
* Autorizzati come descritto sopra.
* Apri https://api.polydocs.io e aggiungi il percorso della funzione dietro l'URL di Polydocs. In questo caso:

![](https://lh7-us.googleusercontent.com/Gwabl4pN0k0NanHsFOzJj9s2H7ExS-JcWr-Y4EW0FLUYHfnaOZoMWvldJ6yDI33p\_DThVx0Rd5bi59XdOK11l1knc5rd-E5HXMw6v5E3qvHvKVWHlp21S728SVye6KU2W5ZeXtCIOzxBAcMlA2UNFfQ)

* Ora incolla questo link nella casella di testo accanto al metodo POST in Postman.
* Seleziona la scheda \`Body\` nella tua richiesta HTTP e inserisci le chiavi e i valori per ciascuna credenziale che ha un asterisco rosso accanto al suo nome.

Quando hai finito, dovrebbe apparire così:

![](https://lh7-us.googleusercontent.com/lSExzZSbTcSRvuLDw0HNYE62yI7xs0eUewKuOcABCGYfsRBRbGz1lJxopR4QdUEoniCnZ83FKpz-AHLORP5cXGPrPhgouzE6zO920jA7A3r-Y14wY\_Gc3C98R2fcxXsWRMcle9qT981YWhCnjlUukPE)

Se desideri creare un account amministratore, imposta il valore di \`is\_admin\` su true.

&#x20;Infine, clicca su \`Invia\` e potrai vedere tutte le credenziali che hai impostato nella risposta sottostante. Questo significa che l'utente è stato creato.
### Carica Documento

Puoi anche utilizzare il metodo POST per caricare un documento su DocBits.

* Seleziona il Metodo POST.
* Autorizzati come descritto in precedenza.
* Apri https://api.polydocs.io e aggiungi il percorso della funzione dietro l'URL di Polydocs.

In questo caso:

![](https://lh7-us.googleusercontent.com/-EwhMeH\_WXYVmMKus1-IZKLZNyTcYktcf\_YUT\_m2nfStfKXuBxKBb1MZfUIQCN4ZxNKQkNhvO\_pgnt1EUhNB34qG5AOe4wM0OxGRMQsV9a8h0XUgabqq8mLQhza\_AE7gxBetmb9bJmaWBQqEXrWT0VI)

* Ora incolla questo link nella casella di testo accanto al metodo POST in Postman.
* Seleziona la scheda \`Body\` nella tua richiesta HTTP e scegli \`form-data\`

![](https://lh7-us.googleusercontent.com/TNrKlyorn\_5YrIu5r4vcfyYgAnfhsl-SRVqWg9RoN0X1pUjXtn6J0EI7aeQ-oc2ZtFeTj8POcMXy6CwXzI1jhv-ufb2u7d80SC-lbGXmnx\_jVDunAbRw1jqAsB4PPsEzcFIOPeH5PJZvytUW2kIDYZ4)

![](https://lh7-us.googleusercontent.com/scAJpTSCqYSKYNNGPIrEsL0zDJIa7Dhe9tpqv\_zDjdLyAydugzdGA1s93njbFOOVbVbQf7oDEtRc14Kt4p1TXX8A--WjvRgeXWsAxDNWdrCN2-QDeya6-FFEG4\_-dhYgrj4yrVYllJs8eZsUgKOPvzo)

Inserisci il file nel campo \`KEY\` dove troverai il menu a discesa File nascosto. Seleziona \`File\` e passa al campo \`VALUE\` dove puoi selezionare il tuo file cliccando su \`Select Files\`.

Quando fai clic su \`Send\`, dovresti vedere “success”: true nella risposta.

Dovrebbe apparire così:

![](https://lh7-us.googleusercontent.com/hNtG\_uTWgxww7iOmHLhnDqdrTlHCI1rk31LozG4l2DLPqxzSn9HoKn8CQIjeBgJLV4bxrGCjWOMRykJ3qBdZLYwxrZJGq\_S3tjVwSZmGTiMgVoqM97TTQjmW8CegEL2FV309NBmV0Fv\_vciSdQRFiOI)

## Esempio Metodo "DELETE"

Il metodo DELETE viene utilizzato per eliminare, ad esempio, utenti, organizzazioni e così via.

* Seleziona il Metodo DELETE
* Autorizzati come descritto in precedenza.
* Apri https://api.polydocs.io e aggiungi il percorso della funzione dietro l'URL di Polydocs.

Per esempio:

![](https://lh7-us.googleusercontent.com/-QqSVIELl1IkxYK\_gGDa7nIv\_B1IvO3OjT3Ge6bAXwPl6jVDETuzXwtYJdRSmqLEP2d6B0L6MuwZvgJpI968pzp1APmJmuQ\_qlqYgZZhesocYCJVMCHhIZAKmlvMybUkUGXYZtySrnEbRTwWTritvKo)

* Ora incolla questo link nella casella di testo accanto al metodo DELETE in Postman.
* Sostituisci {user\_id} alla fine dell'URL con l'effettivo ID utente che desideri eliminare. (Puoi ottenere l'user\_id utilizzando il metodo GET).
* Se hai incluso l'user\_id nell'URL, non è necessario aggiungere una chiave e un valore del corpo per esso.
* Quando fai clic su \`Send\`, dovresti vedere “success”: true nella risposta.

Dovrebbe apparire così:

![](https://lh7-us.googleusercontent.com/X8WNtsC9v7jqDIiaVhauJUgZK0yTC1GVz9rBptdiCxyLUiEEfbpIoYHpK7NvlDMTkhgiPyBb22H9GOfDdvmL-dakouTjuRDPwX4YX0Jz5IIo6eHu-wnw1S4jJd5ylHyffUXWKwX6ovDnp\_2WEAtSha4)

## Esempio Metodo "PUT"

Il metodo PUT è principalmente utilizzato per aggiornare i dati dell'utente o dell'organizzazione. È molto facile da capire e utilizzare.

* Seleziona il Metodo PUT.
* Autorizzati come descritto in precedenza.
* Apri https://api.polydocs.io e aggiungi il percorso della funzione dietro l'URL di Polydocs.

Per esempio:

![](https://lh7-us.googleusercontent.com/tC3qtPbFb1GsK6dBmB5Jrv5HqFOYLxNR1XB0PEuA8ipkHnH2ZQ6xrrkImNgbGSMoA6aAGvLr6K3cI4u\_qM96BOvR7AnQzmX17HBMBneNpLBc6RIzspfTYgrCWSj0fSE9mSWLIex3hc\_R-m-PI6zT6Rs)

* Ora incolla questo link nella casella di testo accanto al metodo PUT in Postman.
* Sostituisci {user\_id} alla fine dell'URL con l'effettivo ID utente che desideri eliminare. (Puoi ottenere l'user\_id utilizzando il metodo GET).

## Cambia l'Indirizzo Email di un Utente

* Nel corpo, inserisci “email” come chiave e il nuovo indirizzo email come valore.
* Quindi premi semplicemente \`Send\` e dovresti vedere “success” nella risposta.
