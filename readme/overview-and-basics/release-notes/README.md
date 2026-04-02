# Note della versione

## **Release HotFix 2 31 marzo 2026**

### Miglioramenti di DocBits:

* **Elaborazione PDF ibrida — Estrazione XML controllata dall'utente:**\
  Quando un PDF contiene dati XML incorporati, gli utenti possono ora scegliere se DocBits deve utilizzare l'XML incorporato per l'estrazione o elaborare il documento come un PDF standard. Questo offre alle organizzazioni il pieno controllo su come vengono gestiti i documenti ibridi, garantendo che venga applicato il metodo di estrazione più adatto al loro flusso di lavoro.

* **AP Assignment Code nella schermata di Approval:**\
  La pagina AP Manager Approval ora include un campo AP Assignment Code, integrato con Infor M3 CRS620. Questo consente agli approvatori di verificare e confermare i codici di assegnazione direttamente durante il processo di approvazione senza passare a sistemi esterni.

* **Corrispondenza del totale PO con il totale del documento:**\
  DocBits ora supporta la corrispondenza del totale dell'ordine di acquisto con il totale del documento, fornendo un ulteriore livello di validazione durante il PO Matching per rilevare le discrepanze più precocemente nel processo.

* **Aggiornamento del numero di articolo fornitore e VPE:**\
  DocBits ora supporta l'aggiornamento dei campi numero di articolo fornitore e VPE (Verpackungseinheit / unità di imballaggio) durante l'elaborazione dei documenti, con i valori sincronizzati verso M3 in fase di esportazione.

* **Classificazione migliorata del layout del documento:**\
  L'ID del layout del documento (tfidf_id) viene ora generato basandosi solo sul testo dell'intestazione, escludendo il testo del piè di pagina. Questo migliora la precisione della classificazione impedendo al contenuto del piè di pagina di influenzare il rilevamento del tipo di documento.

* **Pulsante Export & Next:**\
  È stato aggiunto un nuovo pulsante "Export & Next", che consente agli utenti di esportare il documento corrente e passare immediatamente al successivo nella coda, ottimizzando il flusso di lavoro di revisione ed esportazione.

* **Processo di approvazione per fatture di costo:**\
  Il processo di approvazione per le fatture di costo è stato migliorato con una logica di instradamento e validazione ottimizzata.

### Correzioni di bug:

* Corretto un problema in cui l'esportazione Infor SFTP falliva con un errore a causa di un comando di libreria errato.
* Corretto un problema in cui le caselle di controllo booleane non potevano essere visualizzate nella schermata di approvazione.
* Corretto un problema in cui venivano inviati messaggi UNMU anche quando non c'erano discrepanze nell'unità di acquisto.
* Corretto un problema in cui l'imposta sulle vendite veniva erroneamente classificata come addebito nella schermata di PO Matching, risultando in un importo non saldato negativo.
* Corretto un problema in cui l'esportazione falliva quando l'unità di acquisto non era impostata nella conferma d'ordine ma era presente nell'ordine di acquisto.
* Corretto un problema in cui il corpo dell'e-mail mancava per diversi documenti.
* Corretto un problema in cui il numero di articolo del fornitore non era visibile nella schermata di approvazione e gli aggiornamenti non venivano inviati a M3.
* Corretto un problema in cui l'esportazione dei fornitori verso Infor restituiva un errore.
* Corretto un problema in cui il PO Matching produceva errori durante l'elaborazione.
* Corretto un problema in cui la funzione `findAll` non funzionava correttamente negli script dei documenti.
* Corretto un problema in cui la colonna "Updated By" di Watchdog mostrava erroneamente l'utente Fellow Admin invece dell'utente effettivo.
* Corretto un problema in cui il BOD-Mapping non poteva essere configurato nell'interfaccia Watchdog.
* Corretto un problema in cui gli addebiti venivano erroneamente mostrati come importi non saldati invece di essere visualizzati come addebiti.
* Corretto un problema in cui l'abbinamento automatico non funzionava per le fatture multi-riga nonostante la presenza di una configurazione di abbinamento.
* Corretto un problema in cui un trattino ("-") nel numero di articolo veniva considerato durante il PO Matching per l'ordine di acquisto ma ignorato sulla fattura, causando una discrepanza falsa.
* Corretto un problema in cui sia i file PDF che XML venivano caricati nella cartella di esportazione anche quando l'interruttore "Export PDF" era disattivato.
* Corretto un problema in cui uno stato mancante sulla scheda del workflow impediva ai documenti di procedere attraverso il flusso di lavoro.
* Corretto un problema in cui la qualità del documento era significativamente degradata dopo l'importazione.
* Corretto un problema in cui la schermata PO Match generava un errore ("Cannot read properties of null").
* Corretto un problema in cui l'elenco dei valori predefiniti non poteva essere modificato.
* Corretto un problema in cui il workflow non riusciva a leggere correttamente lo stato del campo, causando un instradamento errato.
* Corretto un problema in cui le importazioni di e-mail in entrata fallivano con un errore.
* Corretto un problema in cui le righe mancanti non arrivavano correttamente in M3 durante l'esportazione.
* Corretto un problema in cui le fatture codificate e approvate occasionalmente non venivano aggiornate allo stato "approvato" in M3 tramite l'API APS110.
* Corretto un problema con la configurazione Multi Banking che non funzionava correttamente.
* Corretti molteplici problemi con la visualizzazione e il comportamento di salvataggio dei dashboard condivisi.
* Corretto un problema in cui il campo numero di articolo fornitore era limitato a 30 caratteri, impedendo la memorizzazione di valori più lunghi.
* Corretto un problema in cui i valori di prezzo unitario e prezzo unitario per unità causavano un errore durante l'esportazione.
* Corretto un problema in cui le righe PO con uno stato escluso (ad es. "Closed") potevano ancora essere trascinate e abbinate nella schermata di PO Matching nonostante fossero escluse dalle regole di abbinamento.

### Modifiche alla configurazione:

* Aggiornati i modelli e-mail per rimuovere il pulsante "Go to Task".
* Regolati gli script e le impostazioni dei campi obbligatori sugli elementi di costo.

## **Release HotFix 1 16 marzo 2026**

### Miglioramenti di DocBits:

* **Cronologia documenti nell'esportazione SFTP:**\
  DocBits ora supporta l'inclusione della cronologia completa del documento come parte del payload XML esportato durante l'esportazione su SFTP. Questa funzionalità è configurabile tramite Export Settings e fornisce ai sistemi a valle un registro di audit completo di ogni cambio di stato e azione eseguita su un documento in DocBits — incluso chi ha effettuato la modifica, quando è avvenuta e quali erano gli stati precedente e attuale. Questo è particolarmente prezioso per la conformità, la tracciabilità e l'analisi operativa.
* **Aggiornamento degli addebiti nella conferma d'ordine per Infor On Premise:**\
  I clienti Infor On Premise possono ora elaborare conferme d'ordine che includono addebiti direttamente in DocBits. Gli addebiti vengono completamente aggiornati attraverso l'esportazione, rendendo il processo di conferma d'ordine end-to-end fluido e rimuovendo la necessità di aggiustamenti manuali a valle.
*   **Applicare il Layout predefinito a tutti gli Origins:**\
    Un nuovo pulsante **Apply Default Layout to Origins** è stato introdotto nella schermata di configurazione del layout. Gli amministratori possono ora distribuire il layout predefinito a tutti gli origins all'interno di un'organizzazione con una singola azione, eliminando il laborioso processo manuale di copia e incolla del JSON di layout per ciascun origin individualmente. Questo è particolarmente utile durante l'onboarding di nuovi clienti dove più origins devono essere configurati in modo coerente.

    ![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/image%20(5).png)
*   **Selezione del tipo di documento per l'importazione FTP:**\
    Le configurazioni di importazione FTP ora supportano l'assegnazione del tipo di documento per cartella. Durante la configurazione di un'importazione FTP, gli utenti possono specificare quale tipo di documento — come Fattura o Conferma d'Ordine — deve essere applicato a tutti i documenti importati da quella cartella. I documenti vengono classificati automaticamente all'importazione, eliminando la necessità di assegnazione manuale del tipo di documento dopo l'acquisizione. Questo supporta le organizzazioni che gestiscono più tipi di documento attraverso diverse sotto-organizzazioni e cartelle.

    ![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/image%20(4).png)
* **Esportazione verso GLS840 per Infor On Premise:**\
  DocBits ora supporta l'esportazione di documenti verso il programma GLS840 per i clienti Infor On Premise, ampliando la gamma di destinazioni di esportazione supportate per gli ambienti on-premise.
*   **Miglioramenti dell'interfaccia per Watchdog e configurazione di esportazione:**\
    Le schermate di configurazione Watchdog e di configurazione dell'esportazione sono state aggiornate con un'interfaccia utente migliorata, offrendo un layout più pulito e un'esperienza più intuitiva per gli amministratori che gestiscono queste impostazioni.

    ![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/image%20(1).png)

    ![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/image%20(2).png)

### Correzioni di bug:

* Corretto un problema in cui gli utenti con diritti di visualizzazione validi non potevano visualizzare i documenti — la logica dei permessi è stata ristrutturata con un controllo del livello di accesso che sostituisce il precedente approccio di filtraggio basato sui gruppi.
* Migliorata la gestione delle eccezioni in molteplici aree dell'applicazione per una maggiore stabilità.
* Risolto un problema in cui le colonne di tipo booleano non venivano gestite correttamente durante l'estrazione dei campi.
* Corretto un problema di autenticazione asincrona nell'endpoint di caricamento file.
* Risolti problemi di visualizzazione dell'interfaccia per la tabella PO nella schermata di validazione.
* Aggiornato il modello di script per includere commenti di tracciamento delle modifiche per una migliore verificabilità.
* Corretto un problema con i campi a tendina che non si comportavano correttamente nella schermata di validazione.
* Corretto un problema in cui il campo sotto-organizzazione non era precompilato durante l'aggiornamento delle assegnazioni dei documenti dal dashboard.

## **Release Winter Summit 10 dicembre 2025**

### Miglioramenti di DocBits:

*   **Personalizzazione avanzata delle regole di corrispondenza ordini:**\
    DocBits ora fornisce un controllo più granulare e personalizzabile sulle regole di corrispondenza degli ordini di acquisto. Gli amministratori possono configurare con precisione quali colonne devono essere valutate durante il processo di corrispondenza per ogni tipo di documento, assicurando che vengano considerati solo i campi più rilevanti. Inoltre, le tolleranze possono essere definite a livello di colonna, consentendo una maggiore flessibilità nella gestione di piccole discrepanze. Ogni regola può anche essere configurata per applicarsi alla corrispondenza manuale, alla corrispondenza automatica o a entrambe, offrendo ai team la possibilità di adattare il flusso di lavoro di corrispondenza ai loro requisiti operativi esatti. Questi miglioramenti migliorano significativamente l'adattabilità e la precisione del processo di corrispondenza degli ordini di acquisto.

    ![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/release_notes_12_2025_3.png)
*   **Supporto per più conti finanziari dei fornitori:**\
    DocBits ora supporta la gestione di più conti finanziari per i fornitori tramite il RemitToPartyMaster BOD fornito da Infor. Questo miglioramento consente alle organizzazioni di mantenere più record di conti di rimessa per un singolo fornitore, migliorando la flessibilità e l'accuratezza nell'elaborazione dei pagamenti. È stata introdotta una nuova impostazione di configurazione per abilitare o disabilitare questa capacità, consentendo agli amministratori di attivare la funzionalità in base alle loro esigenze operative.

    ![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/release_notes_12_2025_1.png)
*   **Aggiunto accesso utente ai risultati di estrazione OCR:**\
    Il pulsante **Vista OCR** nella schermata di convalida dei campi è ora disponibile per tutti gli utenti che hanno accesso alla convalida, anziché essere limitato agli amministratori. Con questo aggiornamento, qualsiasi utente autorizzato può rivedere direttamente i risultati di estrazione OCR, facilitando la convalida dell'accuratezza dei dati e il monitoraggio delle prestazioni complessive dell'OCR. Questo miglioramento promuove una maggiore trasparenza e migliora l'efficienza del flusso di lavoro di convalida.

    ![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/release_notes_12_2025_2.png)
* **Rendering dinamico delle colonne nelle schermate di approvazione:**\
  Visualizzazioni di approvazione migliorate per visualizzare dinamicamente solo le colonne configurate per il confronto nelle preferenze del database di ciascuna organizzazione. In precedenza, alcune colonne specifiche dell'organizzazione apparivano vuote quando non erano configurate per il confronto, causando confusione. Ora, le visualizzazioni di approvazione mostrano solo i campi che vengono attivamente confrontati. Ciò fornisce schermate di approvazione più chiare e specifiche per l'organizzazione senza colonne vuote o irrilevanti.
* **Campo tipo ordine aggiunto alla ricerca dati anagrafici**:\
  L'elenco di intestazione ordine di acquisto ora include una colonna "Tipo ordine" nella ricerca dati anagrafici, fornendo capacità di categorizzazione aggiuntive.
* **Miglioramenti al dashboard filtri personalizzati:**\
  La funzionalità di condivisione del dashboard è stata migliorata per fornire maggiore flessibilità agli utenti condivisi. Le persone che hanno dashboard condivisi con loro ora possono regolare e modificare i filtri del dashboard, consentendo loro di personalizzare le informazioni visualizzate in base alle loro esigenze specifiche. Questo miglioramento supporta un'esperienza di visualizzazione più personalizzata e interattiva, assicurando che gli utenti possano facilmente perfezionare le informazioni sui dati più rilevanti per le loro attività.
* **Prefissi personalizzabili per le colonne della schermata di approvazione:**\
  È stata introdotta una nuova opzione configurabile per visualizzare prefissi prima delle colonne dei documenti nelle schermate di approvazione. Questa funzionalità può essere gestita direttamente all'interno del generatore di layout, dando agli amministratori il controllo completo sulla visualizzazione dei prefissi e sui tipi di documento a cui si applicano. Abilitando questa opzione, gli utenti ottengono un contesto più chiaro e una migliore leggibilità durante la revisione dei documenti durante il processo di approvazione.

### Miglioramenti generali

* Migliorata la registrazione degli errori per le tabelle mal addestrate nell'estrazione delle tabelle.
* Aggiunto un limite di condivisione per i dashboard fino a 10 utenti o 5 gruppi, insieme a un messaggio di errore chiaro quando viene raggiunto il limite.
* Migliorata la gestione degli errori per i dashboard personalizzati quando un utente tenta di creare un dashboard con un nome già esistente.

### Correzioni di Bug:

* Risolto un problema per cui le email sembravano inviate con successo dalla sezione Dettagli Fornitore ma non venivano consegnate ai destinatari.
* Risolto un problema per cui i campi a discesa aggiunti alle schermate di approvazione/rifiuto non venivano visualizzati.
* Risolto un problema per cui tutti i documenti esportati erano contrassegnati come ultimo aggiornamento dall'utente sbagliato.
* Risolto un problema per cui i documenti mostravano lo stato "Flusso di lavoro in corso" ma non venivano eseguiti flussi di lavoro e il registro rimaneva vuoto.
* Risolto un problema per cui utenti non correlati venivano assegnati ai documenti al momento dell'esportazione senza svolgere alcun lavoro su di essi.
* Risolto un problema per cui utenti con autorizzazioni corrette non potevano rifiutare documenti assegnati e ricevevano errori.
* Risolto un problema per cui le icone del flusso di documenti non venivano visualizzate per alcune organizzazioni.
* Risolto un problema per cui appariva un popup durante il caricamento di documenti tramite trascinamento sul dashboard.
* Risolto un problema per cui i flag E-TEXT venivano visualizzati come abilitati nell'interfaccia utente anche se la risposta API mostrava tutti i valori come falsi.
* Risolto un problema per cui si verificava un errore durante il caricamento di documenti contenenti pagine vuote.
* Risolto un problema per cui i collegamenti ipertestuali delle attività nelle notifiche email non reindirizzavano gli utenti alla schermata di approvazione corretta.
* Risolto un problema per cui la selezione della sotto-organizzazione trasversale causava la mancata visualizzazione dei fornitori nella Ricerca dei Dati Anagrafici. Gli utenti possono ora visualizzare correttamente i dati dei fornitori inter-organizzativi.

## Release Autumn Summit 22 Ottobre 2025

### Miglioramenti di DocBits:

*   #### Miglioramenti al Design del Modello Email:

    L'editor del modello email è stato ridisegnato per fornire una struttura più chiara e un'esperienza più fluida. La selezione dei campi del documento è ora più intuitiva e gli allegati possono essere inclusi direttamente nei modelli. Questi miglioramenti rendono più veloce e semplice creare email professionali e personalizzate.

    ![](https://docs.docbits.com/~gitbook/image?url=https%3A%2F%2F578966019-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FT2n2w4uDCJvv7CJ5zrdk%252Fuploads%252Fdv4oDlfkRyD0W9yWGAA4%252Fimage.png%3Falt%3Dmedia%26token%3D14bf7ebd-d886-4758-8184-d7b94447518a\&width=768\&dpr=4\&quality=100\&sign=88405d9c\&sv=2)
*   #### Miglioramenti al Dashboard:

    Il dashboard è stato ampliato per migliorare la navigazione e la personalizzazione. Con nuove schede, gli utenti possono passare più rapidamente tra diversi tipi di documenti, riducendo il tempo trascorso nella ricerca della visualizzazione corretta.

    ![](https://docs.docbits.com/~gitbook/image?url=https%3A%2F%2F578966019-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FT2n2w4uDCJvv7CJ5zrdk%252Fuploads%252FmpO7WSIrkL0I8Rje3HQt%252Fimage.png%3Falt%3Dmedia%26token%3D77d03fe7-e626-4645-b191-e332715a25fb\&width=768\&dpr=4\&quality=100\&sign=93fa9925\&sv=2)
*   #### Dashboard di Filtri Personalizzati:

    Inoltre, i dashboard possono ora essere personalizzati e filtrati in base alle preferenze individuali. Questi dashboard personalizzati possono anche essere condivisi con i colleghi, facilitando la creazione di visualizzazioni di report coerenti per l'intero team.

    ![](https://docs.docbits.com/~gitbook/image?url=https%3A%2F%2F578966019-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FT2n2w4uDCJvv7CJ5zrdk%252Fuploads%252Fn5rPvGnRltT3mTIDoJwV%252Fimage.png%3Falt%3Dmedia%26token%3D22d065e3-81eb-4f16-828c-7f9134c25b1b\&width=768\&dpr=4\&quality=100\&sign=eb11d3a3\&sv=2)
*   #### Registri di Notifiche Email:

    È disponibile una nuova funzionalità di registrazione per tutte le notifiche email. Gli utenti possono ora consultare un elenco delle notifiche inviate, facilitando la verifica delle consegne e la risoluzione dei problemi in caso di mancata ricezione delle email.
*   #### Supporto Fattura Elettronica: e-SLOG 1.6 & 2.0:

    È stato introdotto il supporto per formati di fattura elettronica aggiuntivi. Il sistema può ora elaborare e generare le versioni e-SLOG 1.6 e 2.0, ampliando la compatibilità con partner e requisiti normativi.
*   #### Miglioramenti alla Rilevazione dei Duplicati:

    Il rilevamento dei duplicati è stato potenziato con due potenti opzioni di configurazione. L'**Intervallo di Rilevamento dei Duplicati** consente di definire un intervallo di tempo per controllare i duplicati in modo più preciso, mentre l'impostazione **Vietare l'Esportazione dei Duplicati** impedisce automaticamente l'esportazione dei documenti rilevati come duplicati. Insieme, questi miglioramenti forniscono maggiore controllo e garantiscono una maggiore precisione dei dati.

    ![](https://docs.docbits.com/~gitbook/image?url=https%3A%2F%2F578966019-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FT2n2w4uDCJvv7CJ5zrdk%252Fuploads%252FXHRKTmuSxTlDt9lDEkE7%252Fimage.png%3Falt%3Dmedia%26token%3D96b56af6-c644-4b0f-a488-8bc16a03c11f\&width=768\&dpr=4\&quality=100\&sign=9b723b7f\&sv=2)
*   #### Miglioramenti all'Albero delle Decisioni:

    Gli alberi decisionali sono ora più versatili, con la capacità di restituire i valori dei campi del documento. Ciò consente una logica di automazione più avanzata, consentendo ai flussi di lavoro di prendere decisioni basate sui dati effettivi del documento.
*   #### Nuove Carte di Flusso di Lavoro:

    Due nuove carte di flusso di lavoro ampliano le capacità di automazione. La prima consente di verificare se un documento appartiene a una specifica sotto-organizzazione, facilitando la gestione delle configurazioni multi-entità. La seconda introduce un controllo della tolleranza della data di consegna, che confronta le date di consegna con la data attuale in giorni lavorativi per aiutare a gestire ed applicare i requisiti di consegna in modo più efficace.
*   #### Miglioramenti all'Esportazione CSV:

    La funzionalità di esportazione CSV è stata significativamente migliorata. Invece di esportare solo i documenti visualizzati nella pagina corrente, il sistema esporta ora tutti i documenti in un set di dati. Ogni esportazione crea un registro e il CSV risultante viene inviato automaticamente via email, garantendo un processo di esportazione più completo e affidabile.
*   #### Intervallo di Eliminazione dell'Ordine di Acquisto:

    Una nuova opzione di configurazione consente agli amministratori di definire un intervallo di tempo per l'eliminazione dell'ordine di acquisto. Questo miglioramento aggiunge flessibilità e controllo sulle politiche di conservazione dei dati, garantendo che gli ordini di acquisto vengano rimossi solo quando appropriato.

### Correzioni di Bug

* Risolto un problema in cui i dati precedenti venivano inclusi durante l'esportazione dei documenti.
* Corretto il filtro per gli Errori di Esportazione, che in precedenza mostrava anche altri stati.
* Risolto un mismatch di validazione della tabella in cui "Prezzo Unitario" causava errori ma "Prezzo Unitario Per" no, nonostante i valori fossero corretti.
* Risolto un problema in cui l'aggiunta di una nuova colonna al dashboard falliva.
* Corretto un problema in cui i compiti non erano visibili nella colonna dei compiti del dashboard.
* Risolto il comportamento di ordinamento casuale in modo che le liste seguano ora un ordine coerente.
* Risolto un problema in cui non era possibile interrompere la modifica delle dimensioni delle colonne.
* Risolto un bug che impediva il matching manuale delle linee nella schermata di corrispondenza degli ordini di acquisto.
* Corretto un problema in cui l'opzione di allegato email veniva reimpostata dopo il salvataggio.
* Risolto un problema in cui l'auto contabilizzazione mostrava inizialmente gli ID del database all'apertura per la prima volta.
* Corretto il comportamento del campo fuzzy in modo che i valori non vengano più sovrascritti in modo errato.
* Risolto un problema in cui i campi nell'auto conto scomparivano dopo aver eliminato il contenuto.
* Corretto un bug in cui l'utente non poteva rinominare "Nome" e "Cognome" nella finestra di impostazioni.
* Risolto un problema in cui i documenti potevano rimanere bloccati in "flusso di lavoro in corso".
* Risolto un problema di colore dell'icona del menu in cui i colori dell'organizzazione selezionata non venivano applicati correttamente.
* Corretto un problema in cui i codici QR talvolta non venivano riconosciuti.
* Risolto un problema in cui gli account non potevano essere rimossi con il tasto backspace per inserirne uno diverso.
* Risolto un mix di lingue dopo il login seguente alla push in produzione.



## Release Spring Bloom – 23 aprile 2025

### Miglioramenti di DocBits:

* **Opzione di Filtro per il Registro di Importazione Email:** Gli utenti ora hanno la possibilità di filtrare i registri di importazione e ordinare la tabella per una panoramica più chiara ed efficiente. Questo miglioramento semplifica il processo di identificazione e gestione delle voci email, migliorando la risoluzione dei problemi e la gestione complessiva dei registri.
* **Supporto Multilingue per la Lista dei Valori:** Abbiamo ampliato le capacità multilingue alla funzionalità Lista dei Valori. Gli amministratori possono ora definire etichette in più lingue, assicurando che l'etichetta corretta venga visualizzata automaticamente in base alle impostazioni della lingua di sistema dell'utente. Questo miglioramento promuove una maggiore accessibilità e localizzazione, rendendo più facile per gli utenti di tutto il mondo interagire con la piattaforma nella loro lingua madre.
* **Miglioramenti ai Dettagli Utente nelle Impostazioni:** L'interfaccia delle impostazioni ora visualizza informazioni complete sugli utenti. Gli amministratori possono facilmente visualizzare le affiliazioni ai gruppi, i dettagli delle sotto-organizzazioni e ulteriori dati chiave, consentendo una migliore gestione dei ruoli degli utenti e una comprensione più chiara delle strutture del team.
* **Informazioni di Contabilità Automatica nella Schermata di Approvazione:** La schermata di approvazione ora presenta dettagli di contabilità automatica insieme alle informazioni sulle fatture. Questo miglioramento fornisce una visione più profonda dei dati delle transazioni, facilitando processi di revisione più fluidi e decisioni più informate riguardo alle fatture.
* **Contatore delle Attività per Documenti nella Vista Dashboard:** I documenti nella dashboard possono ora indicare le attività aperte ad essi associate e visualizzare il numero totale di attività in sospeso. Questa funzionalità fornisce agli utenti una panoramica rapida delle azioni in sospeso, migliorando la gestione delle attività e l'efficienza del flusso di lavoro.
* **Selezione del Modello AI Basato sul Fornitore:** Gli utenti possono ora selezionare il modello AI utilizzato per l'estrazione dei dati su base per-fornitore. Questo miglioramento consente un'ottimizzazione più precisa, garantendo una migliore accuratezza di estrazione per diversi fornitori e migliorando i risultati complessivi del processo di elaborazione dei dati.
* **Log di Flusso di Lavoro Migliorati per le Schede degli Alberi Decisionali:** I log ora visualizzano l'output dell'albero decisionale, rendendo più facile tracciare e comprendere come sono state prese le decisioni all'interno dei flussi di lavoro.
*   **Introduzione di un Nuovo Setup di Auto-Test per Migliorare la Funzionalità e la Stabilità del Sistema:**

    Siamo entusiasti di annunciare l'implementazione di un nuovo sistema di test automatizzati progettato per migliorare la funzionalità e l'affidabilità complessive della nostra piattaforma. Questo nuovo setup eseguirà controlli costanti e approfonditi sul nostro sistema per identificare eventuali problemi prima che impattino sulla tua esperienza. Automatizzando questi test, possiamo garantire risposte più rapide a potenziali problemi e mantenere i più alti standard di qualità per il nostro sistema.

    ​

### Correzioni di Bug

* Risolto un problema in cui i compiti non apparivano nella schermata di validazione/approvazione.
* Sistemata la posizione del pulsante Avanti/Indietro in modo che rimanga statico.
* Risolti problemi di scorrimento nelle visualizzazioni dello script e dell'albero decisionale, assicurando che i pulsanti di azione rimangano fissi durante lo scorrimento.
* Rimossa la campo del paese di origine dalle fatture elettroniche.
* Risolto un problema con il contatore dei compiti che visualizzava un numero inaccurato di compiti.
* Aggiunte traduzioni mancanti.
* Corretto i campi personalizzati per visualizzare nomi descrittivi invece di ID.
* Aggiornata la lista delle scorciatoie per la schermata di corrispondenza PO.
* Risolto un problema in cui i documenti venivano scaricati con un nome file errato.
* Sistemate le incoerenze di ordinamento nella tabella delle righe delle fatture all'interno della corrispondenza PO.
* Risolto un problema che influenzava la funzionalità di creazione dei compiti.
* Risolto un problema nella corrispondenza PO in cui l'ordinamento della tabella delle fatture si resetterebbe quando si abbina una riga.
* Risolti problemi di contabilità automatica assicurando che i riferimenti di prenotazione si dividano correttamente quando un importo è diviso.
* Aggiornate le informazioni sull'host ClickHouse.
* Risolto un problema in cui documenti duplicati non venivano riconosciuti come duplicati.
* Sistemati problemi di esportazione causati da riferimenti di prenotazione troppo lunghi.
* Risolto un problema in cui le caselle di controllo di sola lettura non erano di sola lettura.
* Risolto un problema in cui gli utenti potevano essere aggiunti a una sotto-organizzazione due volte.
* Risolto un problema in cui cambiare la sotto-organizzazione per un documento causava il ripristino dell'utente o del gruppo assegnato.

​

## Release Hot Fix Winter Frost 10 Aprile 2025

### Miglioramenti di DocBits:

* **Funzione Script `set_column_date_value` Migliorata:** La funzione `set_column_date_value` ora include il supporto per l'opzione `skip_weekend`, consentendo ai valori di data di saltare automaticamente i fine settimana quando applicati.
* **Supporto per il Caricamento di File Migliorato:** I file PNG e JPEG possono ora essere caricati direttamente e vengono automaticamente convertiti in formato PDF per una gestione dei documenti semplificata.
* **Aggiornamenti della Funzionalità Watchdog:**
  * Ora supporta l'esportazione in **Enaio** per una migliore integrazione del sistema.
  * Capacità di parsing migliorate per estrarre informazioni dalle strutture XML di `Sync.ContentDocument`, consentendo un'elaborazione dei dati più efficiente.

### Correzioni di Bug

* Risolto un problema su una funzione script.
* Risolto un problema in cui gli ordini di acquisto avevano uno stato errato dopo essere stati aggiornati.

## Release Hot Fix Winter Frost 11 marzo 2025

### Miglioramenti di DocBits:

* **Estrazione Dati Migliorata:** Aggiunta un'opzione per estrarre il **Purchase Order** o il **Item Number** da una riga sopra o sotto.
* **Accesso Espanso alle Sotto-Organizzazioni Incrociate:** Gli utenti non amministratori possono ora accedere anche alla funzionalità **Cross Sub-Organizations**.

### **Correzioni di Bug:**

* Risolto un problema in cui gli utenti non potevano essere aggiunti a un gruppo.
* Risolto un problema con i fallimenti di importazione email.
* Risolto un problema con la formazione sul campo su documenti con più di una pagina
* Risolto un problema in cui gli script non funzionavano correttamente.
* Risolto un problema in cui i dati del documento non venivano visualizzati correttamente
* Risolto un problema con l'impostazione dell'aggiornamento automatico dell'ordine di acquisto
* Risolto un problema in cui i token di abbonamento venivano visualizzati in modo errato
* Risolto un problema in cui la schermata delle attività visualizzava una versione obsoleta del documento
* Risolto un problema che causava il mancato cambiamento dello stato dei documenti
* Risolto un problema in cui i token di abbonamento venivano visualizzati in modo errato
* Risolto un problema in cui la schermata delle attività visualizzava una versione obsoleta del documento
* Risolto un problema che causava il mancato cambiamento dello stato dei documenti
