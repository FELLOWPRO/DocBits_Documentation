# Postman per DocBits

Questa guida ti mostrerà come effettuare richieste HTTP alla tua organizzazione DocBits tramite Postman. È facile da usare e molto utile per gli amministratori dell'organizzazione.

## Configurazione

Innanzitutto, scarica Postman sul tuo sistema e accedi/registrati.

Ora segui questa guida passo passo per scoprire come funzionano le richieste HTTP in Postman.

Authorization in Postman

Prima di poter creare le tue richieste HTTP, devi inserire la tua chiave API da DocBits per autorizzarle.

* Fare clic sulla scheda \`Authorization\` e scegliere \`API Key\` come tipo di autorizzazione.

![Richiesta Postman con la scheda Authorization aperta e l'elenco Type con Inherit auth from parent, Bearer Token, Basic Auth, Digest Auth, OAuth 1.0 e OAuth 2.0](https://lh7-us.googleusercontent.com/L3GaBZJvReeINaKbkq3VYQ9UHTBoKUA3nJkfyLqk61q5xaOJnmMLhbrEbgUgLEyYRkewHuLIAVzoYCZ6quHq0pwx\_69FEYJjzYllivB8WzdAtTFSrzl8VeFthbMsEB9sGjcGlVN38DXEXUwuNEPL6hg)

* Compila i valori. Inserisci “X-API-key” nel campo \`Key\` e la tua chiave API come valore (che si trova nel menu Impostazioni DocBits sotto Integrazione). Seleziona Aggiungi a \`Header\`.

&#x20;

* Dovrebbe assomigliare a questo:

![Scheda Authorization di Postman con il tipo API Key, la Key x-api-key, il campo Value per la chiave API e la selezione Header in Add to](https://lh7-us.googleusercontent.com/SmNfci4z8ECTeXzFPE9YQ8nCzCRHglc\_7RR1cN8a8F7KvYWjJcBnY5wpl7q0AV8bfNLkMk8F4F4aw8j4xMK50HJweBRBPo8EasTn-FG-fmlUJQ41aUX-dvTeWP\_xJQThi8A6EwJl3qIc-Dw1B5W9fVE)

### API DocBits

Available at https://api.polydocs.io

* Fare clic su Autorizza nell'angolo in alto a destra

![Pulsante Authorize nell'angolo in alto a destra della vista API di Postman](https://lh7-us.googleusercontent.com/kuztHpkmRWlOYSU27r97KH15SJHPF\_hn\_eX3C1DYLVYCwMHXfLjYSyFubUCvlQiBt5q3xY0XBPmkcP6AnKF2C0Mdtx3tg\_dU\_qxqAmI6axYIsXR36\_YBz6j455K3-c2SBu4YzmYIXq8VXQxzgL-0j90)

* Inserisci la tua chiave API e conferma facendo clic su \`Authorize\`

![Finestra Available authorizations con la voce APIKeyHeader di tipo apiKey, il Name X-API-KEY, In header, un campo Value vuoto e il pulsante Authorize](https://lh7-us.googleusercontent.com/zLhgpdjMnxqNBdjgtDxFEKglICIZul7dgmfFFm2hSnsDQ-HsZHRKRikZ0lcanGYkkZj4waC85mEUFO951ydVnY\_\_m\_TrMrsK3vrDv9FKL-adgWL4lJqp3cSxPeClBm9IHG2cXinRsv12xTeh3psQfO4)

### Creare un nuovo spazio di lavoro in Postman

* Fai clic su Aree di lavoro e crea una nuova area di lavoro (puoi chiamarla come preferisci

![Panoramica delle aree di lavoro di Postman con il pulsante Create Workspace e l'elenco delle aree visitate di recente](https://lh7-us.googleusercontent.com/3rZw7jhOgVpkZuer58fPEKqDspJjK3S1lp3XpQuvE4c9212a0ALB-p7oLRwPqEbj10MpoCWsb7V9fPqiAdVvigE00x9mN5-lHFXZVVxlkeroBJd2ratgkJVJDM4LJkUJsycyl6tnFKazcFPY-vWtH2Q)

* È necessario selezionare la visibilità che determina chi può accedere a questo spazio di lavoro.

![Finestra Create workspace con i campi Name e Summary, le opzioni di visibilità Personal, Private, Team, Partner e Public e i pulsanti Create Workspace e Cancel](https://lh7-us.googleusercontent.com/ZajvDtMvfM5J\_Go3n\_PgzD3RXTMQAlST8\_3WnsTQ4-iw7e0QdAa3wqFk7Y0gt78IJVjNTN-5E72c1127CpXJWb8WbfDolxENLqxg5VZLPEK7-hxsNwbAyMceSHfeVy6v-b9QT0kFwnMibWndEAJ2lXA)

* Dopo aver effettuato la selezione e aver fatto clic su \`Create Workspace\`, seleziona Raccolte sul lato sinistro dell'applicazione e crea una nuova raccolta per le tue richieste HTTP facendo clic su \`+\`.

![Barra laterale di Postman con il gruppo Collections e la voce New Collection per creare una raccolta](https://lh7-us.googleusercontent.com/mbC5t86vaB2G7FQp-40XN-SHc019LKitfUeXRzbcG4HpNai5FPapShx9swHX3mz0va8QFsUQiYn-bhjvER0XYOEDRJpI9x3wG4NgRZCd4beU1NyKJd86bSGubxVbRCtz8HkTDZd28Z7Ice3rmscFMMo)

In questa raccolta puoi aggiungere più richieste HTTP. Per fare ciò, clicca sui 3 punti della raccolta e seleziona \`Add request\`.

![Menu contestuale di una raccolta in Postman con le voci Share, Move, Run collection, Edit, Add request, Add folder, Monitor collection, Mock collection, Create a fork, Create pull request, Merge changes e Pull changes](https://lh7-us.googleusercontent.com/S5W75clJz7JqoIWPbKBjrJqpTAwjS51Pu4dTU160Q7i6oW-HPnb7aN8WRK2AyAb6-HEqTYMZTy9563P0sq53MAjGpVg1JivZX2ATHa6GeFbTX2UCjud7ot8Y\_ksBuUbUfyEfxIDziV8TN3zDfX9Se58)

## Esempio del metodo "GET"

Il metodo GET è molto utile per ottenere informazioni su utenti, sotto-organizzazioni, documenti elaborati e molto altro.

* Scegli il metodo GET nella tua richiesta HTTP.
* Autorizzarti come descritto sopra.
* Apri https://api.polydocs.io e aggiungi il percorso della funzione dietro Polydocs URL. Ad esempio:

![Documentazione API per l'operazione GET /users/get_users intitolata Get Users con la sezione Parameters senza voci e la sezione Responses con il codice 200 Successful Response](https://lh7-us.googleusercontent.com/pIdgyqP7g1UwZbY5yaz1KAnKe\_ESs\_kQyiWAXXM-ukRKakS\_\_OL\_LS9J-07hZnZDf8QqtoN\_lKyuhvOIIIF-4Wp0dkofZYQwXZ0hu2RM0YogRxJah-zf8W\_cDNFf8xsec1tYIsfe0SpBuvdCG4WHMU0)

* Ora incolla questo collegamento nella casella di testo accanto al metodo GET in Postman.

Fai clic su \`Send\` e dovresti ricevere tutte le informazioni su ogni utente della tua organizzazione.

## Esempio del metodo "POST"

Il metodo POST viene solitamente utilizzato, ad esempio, per creare utenti o organizzazioni. Questo metodo inserisce le informazioni nel database.

Create User

* Seleziona il metodo POST.
* Autorizzarti come descritto sopra
* Apri https://api.polydocs.io e aggiungi il percorso della funzione dietro Polydocs URL. In questo caso:

![Documentazione API per l'operazione POST /users/create intitolata Create User con i campi obbligatori first_name, last_name, email e password nel corpo della richiesta e il campo booleano is_admin](https://lh7-us.googleusercontent.com/Gwabl4pN0k0NanHsFOzJj9s2H7ExS-JcWr-Y4EW0FLUYHfnaOZoMWvldJ6yDI33p\_DThVx0Rd5bi59XdOK11l1knc5rd-E5HXMw6v5E3qvHvKVWHlp21S728SVye6KU2W5ZeXtCIOzxBAcMlA2UNFfQ)

* Ora incolla questo collegamento nella casella di testo accanto al metodo POST in Postman.
* Seleziona la scheda \`Body\` nella tua richiesta HTTP e inserisci le chiavi e i valori per ciascuna credenziale che ha un asterisco rosso accanto al nome.

Quando hai finito, dovrebbe assomigliare a questo:

![Scheda Body di Postman con form-data selezionato e le righe first_name con First_Name, lastname con Last_Name, email con test@test.com, password e is_admin con False](https://lh7-us.googleusercontent.com/lSExzZSbTcSRvuLDw0HNYE62yI7xs0eUewKuOcABCGYfsRBRbGz1lJxopR4QdUEoniCnZ83FKpz-AHLORP5cXGPrPhgouzE6zO920jA7A3r-Y14wY\_Gc3C98R2fcxXsWRMcle9qT981YWhCnjlUukPE)

Se desideri creare un account amministratore, imposta il valore \`is\_admin\` su true.

Infine, fai clic su \`Send\` e potrai vedere tutte le credenziali che hai impostato nella risposta seguente. Ciò significa che l'utente è stato creato.

### Caricare un documento

Puoi anche utilizzare il metodo POST per caricare un documento su DocBits.

* Seleziona il metodo POST.
* Autorizzarti come descritto sopra.
* Apri https://api.polydocs.io e aggiungi il percorso della funzione dietro Polydocs URL.

In questo caso:

![Documentazione API per l'operazione POST /document/process intitolata Process con i campi facoltativi source, org_id, priority, sub_org_id e metadata nel corpo della richiesta e il campo obbligatorio file di tipo string binary](https://lh7-us.googleusercontent.com/-EwhMeH\_WXYVmMKus1-IZKLZNyTcYktcf\_YUT\_m2nfStfKXuBxKBb1MZfUIQCN4ZxNKQkNhvO\_pgnt1EUhNB34qG5AOe4wM0OxGRMQsV9a8h0XUgabqq8mLQhza\_AE7gxBetmb9bJmaWBQqEXrWT0VI)

* Ora incolla questo collegamento nella casella di testo accanto al metodo POST in Postman.
* Seleziona la scheda \`Body\` nella tua richiesta HTTP e scegli \`form-data\`

![Richiesta Postman POST https://api.polydocs.io/document/process con la scheda Body aperta, form-data selezionato e una riga KEY vuota per il file](https://lh7-us.googleusercontent.com/TNrKlyorn\_5YrIu5r4vcfyYgAnfhsl-SRVqWg9RoN0X1pUjXtn6J0EI7aeQ-oc2ZtFeTj8POcMXy6CwXzI1jhv-ufb2u7d80SC-lbGXmnx\_jVDunAbRw1jqAsB4PPsEzcFIOPeH5PJZvytUW2kIDYZ4)

![Richiesta Postman POST https://api.polydocs.io/document/process con la scheda Body aperta, form-data selezionato e la riga file con il valore Mango_invoice.pdf](https://lh7-us.googleusercontent.com/scAJpTSCqYSKYNNGPIrEsL0zDJIa7Dhe9tpqv\_zDjdLyAydugzdGA1s93njbFOOVbVbQf7oDEtRc14Kt4p1TXX8A--WjvRgeXWsAxDNWdrCN2-QDeya6-FFEG4\_-dhYgrj4yrVYllJs8eZsUgKOPvzo)

Inserisci il file nel campo \`KEY\` dove troverai il menu a discesa File nascosto. Seleziona \`File\` e spostati nel campo \`VALUE\` dove potrai selezionare il tuo file facendo clic su \`Select Files\`.

Quando fai clic su \`Send\`, dovresti vedere “success”: true nella risposta.

Dovrebbe assomigliare a questo:

![Richiesta Postman POST https://api.polydocs.io/document/process con Status 200 OK e la risposta JSON con success true, il doc_id e il nome file Mango_invoice.pdf](https://lh7-us.googleusercontent.com/hNtG\_uTWgxww7iOmHLhnDqdrTlHCI1rk31LozG4l2DLPqxzSn9HoKn8CQIjeBgJLV4bxrGCjWOMRykJ3qBdZLYwxrZJGq\_S3tjVwSZmGTiMgVoqM97TTQjmW8CegEL2FV309NBmV0Fv\_vciSdQRFiOI)

## Esempio del metodo "DELETE"

Il metodo DELETE viene utilizzato per eliminare, ad esempio, utenti, organizzazioni e così via.

* Seleziona il metodo DELETE
* Autorizzarti come descritto sopra.
* Apri https://api.polydocs.io e aggiungi il percorso della funzione dietro Polydocs URL.

Ad esempio:

![Documentazione API per l'operazione DELETE /users/delete/{user_id} intitolata Delete User con il parametro di percorso user_id](https://lh7-us.googleusercontent.com/-QqSVIELl1IkxYK\_gGDa7nIv\_B1IvO3OjT3Ge6bAXwPl6jVDETuzXwtYJdRSmqLEP2d6B0L6MuwZvgJpI968pzp1APmJmuQ\_qlqYgZZhesocYCJVMCHhIZAKmlvMybUkUGXYZtySrnEbRTwWTritvKo)

* Ora incolla questo collegamento nella casella di testo accanto al metodo DELETE in Postman.
* Sostituisci {user\_id} alla fine di URL con l'utente effettivo ID che desideri eliminare. (Puoi ottenere il user\_id utilizzando il metodo GET).
* Se hai incluso user\_id in URL, non è necessario aggiungere una chiave del corpo e un valore per esso.
* Quando fai clic su \`Send\`, dovresti vedere “success”: true nella risposta.

Dovrebbe assomigliare a questo:

![Richiesta Postman DELETE https://api.polydocs.io/users/delete/508 con Status 200 OK e la risposta JSON success true](https://lh7-us.googleusercontent.com/X8WNtsC9v7jqDIiaVhauJUgZK0yTC1GVz9rBptdiCxyLUiEEfbpIoYHpK7NvlDMTkhgiPyBb22H9GOfDdvmL-dakouTjuRDPwX4YX0Jz5IIo6eHu-wnw1S4jJd5ylHyffUXWKwX6ovDnp\_2WEAtSha4)

## Esempio del metodo "PUT"

Il metodo PUT viene utilizzato principalmente per aggiornare i dati dell'utente o dell'organizzazione. È molto facile da capire e da usare.

* Seleziona il metodo PUT.
* Autorizzarti come descritto sopra.
* Apri https://api.polydocs.io e aggiungi il percorso della funzione dietro Polydocs URL.

Ad esempio:

![Documentazione API per l'operazione PUT /users/update/{user_id} intitolata Update User con il parametro di percorso user_id e i campi first_name, last_name, email, is_organisation_admin e password nel corpo della richiesta](https://lh7-us.googleusercontent.com/tC3qtPbFb1GsK6dBmB5Jrv5HqFOYLxNR1XB0PEuA8ipkHnH2ZQ6xrrkImNgbGSMoA6aAGvLr6K3cI4u\_qM96BOvR7AnQzmX17HBMBneNpLBc6RIzspfTYgrCWSj0fSE9mSWLIex3hc\_R-m-PI6zT6Rs)

* Ora incolla questo collegamento nella casella di testo accanto al metodo PUT in Postman.
* Sostituisci {user\_id} alla fine di URL con l'utente effettivo ID che desideri eliminare. (Puoi ottenere il user\_id utilizzando il metodo GET).

## Modificare l’indirizzo e-mail di un utente

* Nel corpo, inserisci “email” come chiave e il nuovo indirizzo email come valore.
* Quindi premi semplicemente \`Send\` e dovresti vedere “success” nella risposta.
