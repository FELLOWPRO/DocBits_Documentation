# Avviare un caricamento iniziale dei fornitori da Infor M3

Usa questa procedura solo dopo che l'amministratore Infor ha confermato l'azienda, la divisione, il BOD `SupplierPartyMaster` e la rotta ION di DocBits. Un caricamento iniziale senza restrizioni può inviare tutti i fornitori idonei, quindi concordate prima una selezione ristretta. Le undici schermate di Infor M3 riportate qui sotto sono esempi storici: confrontale con il tuo tenant prima di eseguire un job. Questo aggiornamento della pagina non ha eseguito alcun job M3 né importato fornitori in DocBits.

Infor documenta la [procedura di caricamento iniziale EVS006](https://docs.infor.com/m3core/latest/en-us/useradminlib_cloud/m3cecoreag_cloud/hmo1553266924239.html) e le [opzioni di selezione ed esecuzione EVS007](https://docs.infor.com/m3udi/16.x/en-us/m3beud/appfoundhs/spl1567531742751.html). Se le etichette sono diverse, segui la procedura approvata del tuo tenant.

* [ ] Apri Infor OS e l'applicazione M3 con un account autorizzato ai caricamenti iniziali. Prima di continuare, verifica l'azienda e la divisione previste.

<figure><img src="../../../.gitbook/assets/6cf93500-2e90-4cfc-a9fb-5873e5dcb953.png" alt="Schermata iniziale storica di Infor M3 con il menu dei moduli a sinistra e l'elenco Recent con EVS006 Initial Load e BOD Processor Administration"><figcaption><p>Schermata iniziale storica di Infor M3 con EVS006 Initial Load e BOD Processor Administration nell'elenco Recent.</p></figcaption></figure>

* [ ] Apri **Initial Load. Open (EVS006)** con la ricerca programmi del tuo tenant.

<figure><img src="../../../.gitbook/assets/f77b242e-eb2f-43b6-8a2e-03d264198e0c.png" alt="Finestra di ricerca e avvio storica di Infor M3 con campo di input vuoto e pulsante OK"><figcaption><p>Finestra di ricerca e avvio storica di Infor M3 con il campo di input e il pulsante OK.</p></figcaption></figure>

* [ ] In EVS006 crea una definizione di caricamento iniziale per **SupplierPartyMaster**. L'esempio storico usa **CIDMAS** come tabella. Chiedi all'amministratore M3 di confermare che questa combinazione BOD/tabella sia valida nella tua versione e integrazione.

<figure><img src="../../../.gitbook/assets/827a9dbb-c974-4da7-9bd3-f8e87adad60f.png" alt="Finestra di ricerca e avvio storica con evs006 digitato nel campo di input"><figcaption><p>Esempio storico della finestra di ricerca e avvio con EVS006 nel campo di input.</p></figcaption></figure>

<figure><img src="../../../.gitbook/assets/e30c7b86-dcfb-41d2-bd32-447b60e4581b.png" alt="Elenco storico EVS006 Initial Load con il BOD noun SupplierPartyMaster e la tabella CIDMAS compilati"><figcaption><p>Elenco storico EVS006 Initial Load con SupplierPartyMaster come BOD noun e CIDMAS come tabella.</p></figcaption></figure>

* [ ] Seleziona **Create** e controlla la definizione prima di procedere.

<figure><img src="../../../.gitbook/assets/30eee6b2-24ed-4e1f-8812-1304e7dede8e.png" alt="Elenco storico EVS006 con il pulsante della barra degli strumenti Create (più) evidenziato in rosso"><figcaption><p>Elenco storico EVS006 con il pulsante Create evidenziato.</p></figcaption></figure>

<figure><img src="../../../.gitbook/assets/461b72d3-d576-4c92-95c2-d175183088af.png" alt="Pannello di creazione storico EVS006 per la tabella CIDMAS con il campo BOD description ancora vuoto"><figcaption><p>Pannello di creazione storico EVS006 per CIDMAS con il campo BOD description ancora vuoto.</p></figcaption></figure>

* [ ] Inserisci una **BOD Description** chiara, per esempio **Caricamento iniziale SupplierPartyMaster per DocBits**.

<figure><img src="../../../.gitbook/assets/4dc345a8-8eca-4e03-800a-37a670f8792e.png" alt="Pannello di creazione storico EVS006 con BOD description impostata su SupplierPartyMaster"><figcaption><p>Pannello di creazione storico EVS006 con SupplierPartyMaster inserito come BOD description.</p></figcaption></figure>

* [ ] Seleziona **Next** e, dove disponibile, definisci una selezione concordata. Infor consiglia criteri di selezione per evitare di generare troppi eventi.

<figure><img src="../../../.gitbook/assets/315aa54b-f0bd-4057-a1ed-e476c9000725.png" alt="Pannello di creazione storico EVS006 con il pulsante Next evidenziato in basso a destra"><figcaption><p>Pannello di creazione storico EVS006 con il pulsante Next evidenziato.</p></figcaption></figure>

* [ ] Prosegui con le impostazioni di esecuzione. Controlla di nuovo azienda, divisione e selezione.

<figure><img src="../../../.gitbook/assets/c0ff3fe1-a393-43cc-96a5-3e0cb1d878b7.png" alt="Finestra di testo storica in EVS006 con campi di testo vuoti e il pulsante Next"><figcaption><p>Finestra di testo storica EVS006 con i campi di testo e il pulsante Next.</p></figcaption></figure>

* [ ] Nella definizione SupplierPartyMaster scegli **Related → Run**. Si apre **Initial Load Job. Open (EVS007)**; non è ancora la prova che DocBits abbia ricevuto i dati.

<figure><img src="../../../.gitbook/assets/d819fdd5-5b4a-48ef-9412-f211c0d2355f.png" alt="Elenco storico EVS006 con il menu contestuale aperto sulla riga SupplierPartyMaster e la voce Related > Run"><figcaption><p>Elenco storico EVS006 con il menu Related → Run aperto sulla riga SupplierPartyMaster.</p></figcaption></figure>

* [ ] Scegli **Sync** solo se il flusso ION di destinazione prevede Sync.SupplierPartyMaster. Conferma filtri e destinazione prima di inviare EVS007. Un caricamento iniziale completo può generare molti eventi.

<figure><img src="../../../.gitbook/assets/m3-supplier-initial-load-job-historical-id-masked-20261102.png" alt="Initial Load Job storico EVS007 per CIDMAS e SupplierPartyMaster con verbo BOD Sync e stato 1-Pending"><figcaption><p>Initial Load Job storico EVS007 con CIDMAS, SupplierPartyMaster, Sync e stato 1-Pending. L'identificativo del job è mascherato; lo stato Pending non prova un'importazione completata.</p></figcaption></figure>

## Verifica del risultato

Dopo un'esecuzione autorizzata, controlla **Related → History** in EVS006 per il numero di record elaborati e per eventuali errori. Verifica poi il messaggio SupplierPartyMaster in Infor ION e conferma che sia arrivato all'organizzazione DocBits configurata. Solo allora cerca un fornitore atteso in DocBits sotto **Impostazioni → Ricerca di dati anagrafici → Fornitore**. Usa il controllo di ricerca con il numero o il nome del fornitore; non dare per scontato che tutti i fornitori M3 siano arrivati solo perché il job è stato inviato.

<figure><img src="../../../.gitbook/assets/m3-supplier-master-data-it-20261113.png" alt="Scheda Fornitore in Impostazioni, Ricerca di dati anagrafici della Sandbox DocBits 11.27.7 con il selettore Ricerca per colonna, il campo Ricerca Stringa e righe di fornitori inventate"><figcaption><p>Dati inventati nella Sandbox DocBits 11.27.7: scheda Fornitore con il selettore Ricerca per colonna e il campo Ricerca Stringa. Queste righe dimostrative non provano un'importazione da M3.</p></figcaption></figure>

La schermata mostra dati sintetici già presenti nella Sandbox Test A. Durante questo aggiornamento della documentazione non è stato collegato alcun tenant M3. Se il fornitore atteso manca, confronta la cronologia EVS006, il routing ION e l'organizzazione DocBits prima di rieseguire il caricamento.

### Alternativa: Cruscotto fornitori

Se nella tua organizzazione è attivo il Portale fornitori, i fornitori importati compaiono anche nella pagina **Cruscotto Fornitori**, perché entrambe le viste leggono gli stessi dati anagrafici dei fornitori. Cerca per nome o numero del fornitore con **Ricerca per nome, numero**.

<figure><img src="../../../.gitbook/assets/m3-supplier-management-search-it-20261113.png" alt="Campo di ricerca Ricerca per nome, numero nella pagina Cruscotto Fornitori della Sandbox DocBits 11.27.7 con otto fornitori inventati"><figcaption><p>Dati inventati nella Sandbox DocBits 11.27.7: campo di ricerca Ricerca per nome, numero nel Cruscotto Fornitori.</p></figcaption></figure>
