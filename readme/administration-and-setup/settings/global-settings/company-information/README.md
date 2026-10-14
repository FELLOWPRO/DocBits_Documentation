# Company Information

<figure><img src="../../../../.gitbook/assets/company_information.png" alt="Modulo Company Information nell'organizzazione di test DocBits Sandbox in inglese"><figcaption><p>Company Information: modifica il nome dell'organizzazione, l'indirizzo, gli identificatori legali e i recapiti, quindi seleziona Save.</p></figcaption></figure>

La pagina Company Information ti permette di gestire il profilo della tua azienda, le preferenze e i dettagli dell'abbonamento. È organizzata nelle sezioni seguenti:

## Company Information

Questa sezione contiene i dati principali della tua azienda, raggruppati in quattro aree:

### Company Identity

* **Name** *(obbligatorio)*: la ragione sociale della tua azienda.

### Address

* **Street + Number**: l'indirizzo (via e numero civico) della tua azienda.
* **Postal Code**: il codice postale (CAP).
* **City**: il nome della città.
* **Country**: seleziona il tuo paese dal menu a discesa.

### Legal Information

* **Company ID**: un identificatore univoco della tua azienda, usato per le integrazioni e come riferimento interno.
* **Tax ID**: il tuo numero di identificazione fiscale per la rendicontazione finanziaria.
* **Commercial Register ID**: il tuo numero di registro commerciale per la documentazione legale.

### Contact

* **Official Company Phone Number**: il numero di telefono principale della tua azienda.
* **E-Mail**: l'indirizzo e-mail principale usato per le comunicazioni ufficiali.

Dopo aver inserito o aggiornato i campi, fai clic su **Save** per applicare le modifiche. Le icone **?** accanto agli identificatori legali mostrano indicazioni aggiuntive sul campo. Seleziona il titolo della sezione per espandere o comprimere il modulo.

## E-mail domains

Gli amministratori dell'organizzazione possono aprire **Settings → Company Information → E-mail domains** per gestire i domini usati per l'assegnazione automatica all'organizzazione. Quando una persona accede con Microsoft o Google e non è ancora membro di un'organizzazione, DocBits può assegnarla a questa organizzazione se il suo indirizzo e-mail utilizza uno dei domini elencati. Un dominio può appartenere a una sola organizzazione.

<figure><img src="../../../../.gitbook/assets/company_email_domains_en.png" alt="Sezione E-mail domains espansa con elenco dei domini vuoto, campo di inserimento e pulsante Add domain"><figcaption><p>La sezione E-mail domains in inglese prima dell'aggiunta di un dominio. Inserisci un dominio aziendale, quindi seleziona Add domain.</p></figcaption></figure>

Inserisci solo il dominio, ad esempio `example.com`, nel campo e seleziona **Add domain** oppure premi Invio. Il primo dominio diventa il dominio primario. Se sono elencati più domini, usa **Make primary** su un'altra riga per cambiarlo, oppure l'icona del cestino per rimuovere un dominio. Errori come un dominio non valido, un provider di posta personale o un dominio già assegnato altrove compaiono sotto il campo. **No domains assigned yet** significa che questa organizzazione non ha alcuna regola di dominio.

Prima di aggiungere un dominio, verifica quale organizzazione deve ricevere i nuovi accessi. Per gestire le appartenenze esistenti, continua con [Utenti](../groups-users-and-permissions/users/README.md).

## Company Preferences

Configura le impostazioni predefinite valide per tutta l'azienda:

* **Date Pattern**: scegli come vengono visualizzate le date in tutto DocBits (ad es. `%m/%d/%Y`, `%d.%m.%Y`).
* **Amount Formatting**: seleziona il formato numerico degli importi (ad es. Deutsch per `1.000,00`, English per `1,000.00`).
* **New Version Info Dialog**: attiva o disattiva la visualizzazione di una notifica agli utenti quando viene rilasciata una nuova versione di DocBits.

Fai clic su **Save** dopo aver apportato le modifiche.

## App-Color

Personalizza il colore principale dell'interfaccia di DocBits. È utile per distinguere visivamente ambienti diversi (ad es. dev e produzione).

* **Color**: inserisci un codice colore esadecimale (ad es. `#2388AE`) oppure usa il selettore di colori.
* Fai clic su **Save** per applicare, oppure su **Reset** per ripristinare il colore predefinito.

## Subscription Plan

Visualizza i tuoi piani di abbonamento attivi e i relativi dettagli:

* **Plan Name**: il nome di ciascun piano attivo (ad es. DocBits, DocFlow Users, DocSearch).
* **Days Left**: quanti giorni mancano alla scadenza del piano.
* **Start Date / End Date**: il periodo di abbonamento.
* **Users Count**: il numero totale di utenti della tua organizzazione.
* **Sub Organizations Count**: il numero di sotto-organizzazioni configurate.
* **Suppliers Count**: il numero di fornitori registrati.

## Subscription Usage

Monitora il consumo mensile di token e workflow:

| Colonna | Descrizione |
|--------|-------------|
| **Type** | Il tipo di utilizzo (Document o Workflow). |
| **From / To** | Le date del periodo di fatturazione. |
| **Tokens Used** | Il numero di token consumati nel periodo corrente. |
| **Remaining Tokens** | I token ancora disponibili nel periodo corrente. |

Usa il pulsante **Select** per filtrare per intervalli di date specifici.
