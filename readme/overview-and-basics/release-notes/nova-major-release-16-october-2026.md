# NOVA – Rilascio principale 4 novembre 2026

**Disponibilità di NOVA R1.1:** Disponibile nell’ambiente di test dal **16 ottobre 2026**. Il rilascio in produzione è previsto per il **4 novembre 2026**.

**DocBits è il prodotto. NOVA indica il ciclo di rilascio.** [Guarda il video sul nuovo rilascio di DocBits](https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/nova-release/v1/it.mp4) · [Sottotitoli](https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/nova-release/v1/it.vtt).

**Versioni dei servizi nell’ambiente di test: 16 ottobre 2026**

NOVA include tutte le funzionalità precedentemente disponibili come beta in VESTA come funzionalità standard, insieme alla convalida guidata dei documenti, a più modi per migliorare l'automazione, a controlli più chiari per le fatture elettroniche e a un migliore controllo sugli import e sull'elaborazione dei documenti. Queste note descrivono le aggiunte visibili al cliente nelle versioni del servizio elencate di seguito, rispetto all'ultimo [hotfix VESTA pubblicato, R1.0.15 del 14 ottobre 2026](incremental-updates-14-october-2026.md), inclusi gli hotfix VESTA precedenti.

Lo snapshot identifica le build coperte da queste note. Per la disponibilità nel tuo ambiente sandbox o di produzione e per il passaggio tra i canali, consulta il [ciclo di vita delle release DocBits](../docbits-release-lifecycle-strategy.md). Le funzionalità che dispongono di un interruttore a livello di organizzazione o di tipo di documento devono ancora essere abilitate da un amministratore.

## Ex funzionalità beta VESTA: incluse in NOVA <a href="#former-vesta-beta-features-included-in-nova" id="former-vesta-beta-features-included-in-nova"></a>

**Tutte le precedenti funzionalità beta di VESTA sono incluse come funzionalità standard nell’ambiente di test di NOVA.** Per i clienti che non hanno utilizzato la beta VESTA, ciò espande le funzionalità disponibili per il loro team, incluse **Gestisci layout**, [**Regole di convalida personalizzate**](../../administration-and-setup/settings/global-settings/document-types/custom-validation-rules.md) e [**Regole di trasformazione**](../../administration-and-setup/settings/global-settings/document-types/transformation-rules.md). Le impostazioni dell'organizzazione, gli interruttori per tipo di documento e le autorizzazioni di accesso continuano ad applicarsi.

Le stesse ex funzionalità beta diventeranno funzionalità standard di VESTA con il **prossimo hotfix VESTA, previsto per l'[11 novembre 2026](vesta-hotfix-11-november-2026.md)**. Questo annuncio riguarda le ex funzionalità beta VESTA; le sezioni seguenti descrivono anche ulteriori aggiunte e miglioramenti di NOVA.

## Cosa aggiunge NOVA per i clienti <a href="#what-nova-adds-for-customers" id="what-nova-adds-for-customers"></a>

Il confronto seguente copre le ex funzionalità beta ora disponibili, le nuove capacità e le estensioni delle funzionalità esistenti. La baseline VESTA include funzionalità disponibili solo in beta; la loro inclusione nel set di funzionalità standard di NOVA rappresenta una modifica alla release visibile al cliente.

| Capacità | Baseline VESTA (inclusa la beta) | Cosa ottengono i clienti con NOVA |
| --- | --- | --- |
| **Utilizzare le ex funzionalità beta** | Funzionalità disponibili tramite la beta VESTA | **Funzionalità regolari di NOVA:** tutte le ex funzionalità beta VESTA sono incluse. La loro introduzione regolare in VESTA è prevista per l'hotfix dell'11 novembre 2026. |
| **Assistenza durante la convalida di un documento** | Assistente impostazioni e Controllo campi intestazione | **Nuovo Assistente di convalida:** identifica i campi bloccanti, passa al valore rilevante, rivedi le correzioni suggerite e mantieni la chat in una finestra separata. |
| **Migliorare l'automazione dalle correzioni quotidiane** | Dashboard Touchless Intelligence, diagnosi del fornitore e proposte di modifica | **Nuovo processo di revisione e misurazione:** invia richieste di miglioramento, rivedi le proposte di regole apprese, visualizza le prove sui documenti interessati, classifica le opportunità e misura i risultati dopo l'attivazione. |
| **Comprendere e risolvere gli errori delle fatture elettroniche** | Controlli e-document, catalogo delle regole e visualizzatore XML | **Convalida e-invoice ampliata:** report raggruppati per livello di convalida, controlli delle policy e cronologia delle modifiche, rifiuto dal report e ispezione XML all'interno delle fatture PDF supportate. |
| **Controllare gli import FTP/SFTP** | Connessioni di import e conservazione o archiviazione dei file sorgente | **Nuova configurazione guidata e controlli:** procedura guidata di connessione, log passo-passo, tentativi configurabili e notifiche di errore, ed eliminazione dei file sorgente dopo un import riuscito. |
| **Lavorare con regole e layout** | Motori di regole, log di esecuzione e trasformazioni dopo la ricerca dei dati anagrafici; i pannelli di gestione richiedevano un link beta | **Accesso più ampio e strumenti migliori:** apri direttamente i pannelli di gestione, cerca e visualizza in anteprima i layout di destinazione, apri l'editor di layout di un documento e registra l'esecuzione della selezione del layout. |
| **Agire dall'Assistente impostazioni** | Chat impostazioni, anteprima/conferma/annullamento e avvisi proattivi sullo stato di salute dell'import | **Azioni aggiuntive:** gestisci le connessioni fallite, visualizza la cronologia delle disattivazioni, modifica gli elementi di configurazione selezionati, crea una regola di convalida inattiva da un catalogo e osserva le spiegazioni della pagina. |
| **Controllare l'elaborazione dei documenti** | Limiti di pagine dell'organizzazione e riavvio del documento | **Nuove scelte a livello di documento:** riavvia con un numero di pagine scelto, visualizza le pagine elaborate rispetto a quelle totali e scegli se estrarre i campi nascosti. |
| **Abbinare consegne complesse** | Abbinamento degli ordini di acquisto e collegamento manuale delle righe | **Abbinamento più flessibile:** seleziona le righe in entrambe le direzioni, conserva facoltativamente ogni sotto-riga del documento abbinato e raggruppa le richieste di esportazione per colonne di riga configurate. |
| **Mantenere distinti i lavori esportati e completati** | Flussi di lavoro di esportazione e Finished esistenti | **Nuovi controlli di stato:** usare Exported per l'elaborazione di follow-up, bloccare facoltativamente i documenti Finished e individuare i documenti trattenuti dal limite di esecuzione del flusso di lavoro. |

### Abilitare le funzionalità che richiedono configurazione

* **Assistente di convalida:** un amministratore dell'organizzazione lo abilita in **Impostazioni → Informazioni azienda → Assistenti**. È separato dall'Assistente impostazioni e rimane disattivato fino all'abilitazione.
* **Report di revisione dei miglioramenti e di consulenza:** richiedono l'accesso come amministratore dell'organizzazione e Analytics. Le proposte apprese necessitano di uno storico delle correzioni; un risultato misurato richiede dati sufficienti e il completamento del periodo di follow-up.
* **Controlli di regole e layout:** i rispettivi interruttori di abilitazione per tipo di documento si applicano ancora. NOVA rende accessibili i pannelli di gestione senza un link beta.
* **Comportamento di elaborazione facoltativo:** configurare la pulizia FTP e i nuovi tentativi per connessione. L'espansione delle sotto-righe da uno a molti e il blocco del documento completato sono impostazioni opt-in.

Per la disponibilità nel proprio ambiente e il passaggio tra canali di rilascio, vedere il [ciclo di vita del rilascio](../docbits-release-lifecycle-strategy.md).

## Guardare i video delle funzionalità <a href="#watch-the-feature-videos" id="watch-the-feature-videos"></a>

Utilizzare queste guide passo-passo insieme alle note di rilascio per comprendere le funzionalità correlate e la loro configurazione. I video disponibili in italiano sono collegati di seguito; gli altri video sono chiaramente etichettati come in inglese.

* [Scegliere l'automazione giusta — incluso dove si inseriscono le Regole di abbinamento degli ordini di acquisto](https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/choose-automation/v1/it.mp4)
* [Regole di trasformazione](https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/transformation-rules/v1/it.mp4)
* [Regole di convalida personalizzate (Video in inglese)](https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/custom-validation-rules/v1/en.mp4)
* [Layout e regole di selezione (Video in inglese)](https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/layouts/v1/en.mp4)
* [Touchless Intelligence](https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/touchless-intelligence/v1/it.mp4)
* [Convalida delle fatture elettroniche](https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/einvoice-validation/v1/it.mp4)
* [Utenti e accesso amministratore](https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/users/v1/it.mp4)
* [Sub-organizzazioni](https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/sub_organizations/v1/it.mp4)

### AI Table: sei brevi video

Questi video sono in inglese. Guardare la serie completa o scegliere l'argomento necessario.

1. [Leggere la tabella AI](https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/ai-table-part1/v1/en.mp4)
2. [Correggere una colonna e insegnare a DocBits](https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/ai-table-part2/v1/en.mp4)
3. [Tre problemi tipici](https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/ai-table-part3/v1/en.mp4)
4. [Righe di sconto, imposta e quantità zero](https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/ai-table-part4/v1/en.mp4)
5. [Cosa legge già correttamente l'AI](https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/ai-table-part5/v1/en.mp4)
6. [L'Assistente e chi può modificare cosa](https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/ai-table-part6/v2/en.mp4)

Per screenshot e istruzioni dettagliate, vedere la [guida AI Table](../../end-user-and-partner-section/end-user-section/ai-table/README.md).

## Assistente di convalida: aiuto sul documento corrente

* **Individuare ciò che blocca il progresso.** Chiedere perché un documento non può procedere. L'assistente identifica i campi interessati, spiega il problema e offre un salto al campo o alla cella della tabella. Utilizza il documento corrente e i diritti di accesso dell'utente.
* **Esaminare le correzioni suggerite nel contesto.** Dove supportato, i revisori possono applicare un valore di campo o di tabella proposto, utilizzare un candidato dei dati anagrafici, ripetere una ricerca o aprire la schermata di abbinamento pertinente. Le modifiche al modulo rimangono soggette al normale processo di revisione e salvataggio del documento. I documenti in sola lettura e gli utenti senza permesso di modifica non ricevono azioni di modifica.
* **Chiedere informazioni su abbinamento e contabilità.** L'assistente può spiegare il contesto dell'ordine di acquisto o contabile quando aperto su quelle schermate. Le modifiche al modulo di convalida vengono effettuate sulla schermata di convalida.
* **Comprendere un miglioramento prima di utilizzarlo.** Le spiegazioni collegano una regola o un'impostazione proposta ai valori effettivi del documento. Possono includere un diagramma e una spiegazione narrata nella lingua dell'utente quando disponibile. I suggerimenti rimangono focalizzati sul documento corrente.
* **Lavora con la chat in una finestra separata.** Apri la conversazione in una finestra a comparsa durante la revisione del documento. Le azioni che modificano il modulo rimangono nella finestra del documento.
* **Visualizza maggiori dettagli dietro i valori estratti.** La vista dell'origine del valore aggiunge dettagli quali OCR rispetto al livello di testo del PDF, la corrispondenza delle regole di estrazione e la ricerca che ha fornito un valore. La spiegazione della tabella AI aggiunge consigli di configurazione più azionabili e conteggi più chiari.

Un amministratore dell'organizzazione abilita l'Assistente di convalida separatamente dall'Assistente impostazioni in **Impostazioni → Informazioni azienda → Assistenti**.

## Trasforma le correzioni ripetute in miglioramenti dell'automazione

La dashboard esistente di [Touchless Intelligence](../../administration-and-setup/touchless-intelligence.md) acquisisce un processo di revisione e follow-up:

* **Proposte di regole apprese.** Le correzioni manuali ripetute possono suggerire una [regola di trasformazione](../../administration-and-setup/settings/global-settings/document-types/transformation-rules.md). Gli amministratori vedono cosa scriverebbe, gli esempi di supporto e i documenti su cui sostituirebbe un valore accettato dal team. Una proposta viene revisionata prima di diventare una regola attiva.
* **Richieste di miglioramento dai revisori.** Gli utenti possono inviare un miglioramento dall'assistente documenti affinché un amministratore lo revisioni in Touchless Intelligence. La richiesta mantiene insieme la spiegazione e la decisione.
* **Misura cosa è successo dopo l'attivazione.** Per le regole di trasformazione supportate, DocBits confronta le correzioni manuali prima e dopo l'attivazione e mostra il tasso touchless accanto a esse. La misurazione utilizza periodi di 14 giorni e identifica dati insufficienti anziché inventare un miglioramento. La modifica di una regola avvia una nuova misurazione per quella revisione.
* **Report di consulenza.** Gli amministratori possono generare una vista classificata delle opportunità di miglioramento in estrazione, dati anagrafici, abbinamento ordini di acquisto, contabilità, impostazioni e flusso di elaborazione. L'impatto stimato è etichettato come stima finché non è stato misurato.
* **Consigli di abbinamento specifici per fornitore.** Problemi ripetuti di abbinamento fornitore e articolo possono informare proposte per tolleranze o [regole di abbinamento degli ordini di acquisto](../../administration-and-setup/settings/global-settings/document-types/more-settings/purchase-order/purchase-order-matching-rules.md). I consigli distinguono un ordine di acquisto mancante da un problema di regola o tolleranza.
* **Riepiloghi di follow-up.** Un riepilogo settimanale per amministratori riunisce le richieste di miglioramento aperte, le principali opportunità e le misurazioni completate quando c'è qualcosa da segnalare. I richiedenti possono essere notificati quando un risultato misurato è disponibile.

## Assistente impostazioni: azioni aggiuntive e spiegazioni delle pagine

L'[Assistente impostazioni](../../administration-and-setup/settings/global-settings/company-information/settings-assistant.md), inclusi gli avvisi proattivi di salute email/FTP, è già stato rilasciato in VESTA. NOVA aggiunge azioni e contesto a quell'esperienza esistente:

* **Azioni di connessione da un avviso di salute.** Apri la connessione interessata, rivedi l'azione disponibile e confermala dall'assistente. Gli avvisi di salute possono anche essere ignorati. Le schede di avviso di base per canale e le relative informazioni su errore/ripetizione esistono già in VESTA.
* **Cronologia di disattivazione visibile.** Dove registrata, un'importazione disabilitata mostra quando è stata spenta e da chi.
* **Azioni aggiuntive revisionate.** Gli amministratori possono anteprima e confermare modifiche supportate quali l'attivazione di tipi di documento, il rinominare un gruppo, la modifica della modalità di ricerca di un campo di ricerca, l'eliminazione di un campo o la creazione di una regola di convalida personalizzata inattiva dal catalogo.
* **Gestisci connessioni di importazione fallite.** Le schede supportate possono disattivare o eliminare una connessione dopo la conferma. Le azioni reversibili offrono un annullamento; l'eliminazione permanente è identificata come tale.
* **Spiegazioni delle pagine.** Le pagine delle impostazioni selezionate offrono video con sottotitoli e trascrizioni, inclusi layout, utenti, sotto-organizzazioni, regole di trasformazione e convalida delle fatture elettroniche dove una versione linguistica è disponibile.

## Regole e layout: accesso diretto e migliori diagnostiche

* **I controlli beta precedenti diventano funzionalità standard.** Gestisci layout, [Regole di convalida personalizzate](../../administration-and-setup/settings/global-settings/document-types/custom-validation-rules.md) e [Regole di trasformazione](../../administration-and-setup/settings/global-settings/document-types/transformation-rules.md) sono visibili nelle impostazioni avanzate del tipo di documento di NOVA senza un link beta. I loro interruttori di abilitazione rimangono sotto il controllo dell'amministratore. Questi controlli sono inclusi nell'hotfix VESTA pianificato per l'11 novembre 2026 insieme a tutte le altre funzionalità beta precedenti di VESTA.
* **Diagnostiche delle regole più utili.** Le regole di selezione del layout acquisiscono un'opzione **Registra esecuzione**. La ricerca delle regole accetta identificatori di regole e l'apertura di un editor carica la regola salvata corrente. Il log di esecuzione delle regole esistente rimane il luogo per rivedere cosa è stato eseguito.
* **Scegliere e aprire i layout con più contesto.** Cercare i layout di destinazione, visualizzarne in anteprima il contenuto e aprire direttamente la destinazione da una regola di selezione. Le regole di selezione dell'approvazione accettano correttamente i tipi di layout di approvazione supportati. Gli amministratori ricevono inoltre un collegamento rapido dalla convalida del documento all'editor di layout di quel tipo di documento.
* **Selezionare più valori di condizione.** Le condizioni come **è uno di** supportano più valori selezionati.
* **Trovare più rapidamente i campi di rilevamento dei duplicati.** Il selettore di campi nelle impostazioni di duplicazione del tipo di documento è ricercabile.

Le trasformazioni dopo la ricerca dei dati anagrafici, il log di esecuzione di base delle regole, gli editor di regole più ampi e le correzioni alla clonazione delle regole standard hanno già implementazioni nella baseline VESTA. NOVA mantiene tale funzionalità e rende disponibili come funzionalità standard i precedenti controlli di gestione beta.

Per i passaggi di configurazione, gli esempi e i test, vedere [Regole di convalida personalizzate](../../administration-and-setup/settings/global-settings/document-types/custom-validation-rules.md) e [Regole di trasformazione](../../administration-and-setup/settings/global-settings/document-types/transformation-rules.md). Per scegliere quale layout utilizza un documento, vedere [Regole di selezione del layout](../../administration-and-setup/settings/global-settings/document-types/layout-manager/layout-selection-rules.md).

## Convalida delle fatture elettroniche: risultati più chiari e controlli delle policy

* **Un report organizzato per livello di convalida.** I risultati sono raggruppati in sintassi, schema, regole di business, regole di controllo incrociato e regole specifiche per paese, con gruppi aggiuntivi per altri controlli di standard e controlli dei valori. I messaggi e i riepiloghi utilizzano la lingua dell'utente ove siano disponibili le traduzioni.
* **Controlli più completi e risultati più chiari.** Il validatore e il report aggiornati distinguono errori, avvisi e la severità effettiva dopo la configurazione specifica dell'organizzazione. La pagina è denominata **Convalida delle fatture elettroniche**.
* **Policy per tipo di documento.** Gli amministratori possono verificare se la convalida delle fatture elettroniche è abilitata e se i fallimenti bloccano l'elaborazione. La vista delle policy identifica le sostituzioni dei sottotipi e le modifiche alle policy sono registrate in una cronologia delle modifiche.
* **Ispezionare l'XML all'interno di una fattura PDF.** Il visualizzatore XML può leggere l'XML incorporato nei PDF ZUGFeRD/Factur-X supportati, aprire la posizione referenziata da un risultato e tornare al documento.
* **Rifiutare con una motivazione registrata.** Un revisore autorizzato può rifiutare un documento idoneo dal report di convalida. Il report prepara una motivazione basata sui suoi errori affinché il revisore la verifichi prima della conferma.
* **Ulteriori correzioni di formato.** Le fatture CII della utility EDNA vengono riconosciute e le correzioni alla mappatura IVA di XRechnung migliorano il modo in cui i valori delle fatture pertinenti raggiungono i campi DocBits.

Vedere [Regole di convalida dei documenti elettronici](../../administration-and-setup/settings/document-processing/e-documents/validation-rules.md).

## Importazioni FTP/SFTP ed e-mail

* **Configurazione guidata FTP/SFTP.** La procedura guidata di connessione separa i dettagli del server, le opzioni di importazione e la configurazione. I controlli di connessione e gli errori più chiari aiutano gli amministratori a identificare una connessione errata o una cartella di origine mancante.
* **Log di importazione per passaggio.** Verificare l'avanzamento di un file attraverso l'importazione FTP, inclusi il caricamento e l'azione configurata sul file di origine.
* **Comportamento configurabile di ritentativi e notifiche.** Impostare l'intervallo tra i ritentativi successivi, la durata dei ritentativi e i destinatari delle notifiche. Quando la finestra di ritentativi è esaurita, la connessione può essere disabilitata automaticamente e i destinatari notificati; la procedura guidata mostra l'avviso di disattivazione.
* **Eliminazione dopo un'importazione riuscita.** Oltre a conservare o archiviare i file di origine, gli amministratori possono scegliere di eliminarli dal server FTP/SFTP dopo un'importazione riuscita. L'archiviazione e l'eliminazione sono alternative separate.
* **Recupero delle importazioni più affidabile.** Le esecuzioni FTP sovrapposte sono impedite dal caricare due volte lo stesso file di origine. La modifica di una connessione preserva la password memorizzata a meno che non venga sostituita. La gestione delle e-mail non contrassegna un messaggio per l'eliminazione quando la copia non è riuscita.
* **Supporto per e-mail firmate.** I messaggi S/MIME con firma opaca contenenti fatture possono essere estratti anziché ignorati.
* **Cronologia e stato della configurazione delle e-mail.** Le impostazioni di importazione mostrano chi ha salvato o attivato l'ultima volta una configurazione. L'interruttore per le e-mail in ingresso riflette lo stato attivo memorizzato, inclusa una configurazione appena salvata.

Vedere [Importazione FTP](../../end-user-and-partner-section/end-user-section/how-to-import-documents/ftp.md) e [Testare una connessione di importazione FTP](../../administration-and-setup/settings/document-processing/import/test-ftp-import-connection.md).

## Elaborazione ed estrazione dei documenti

* **Riavvio con un numero di pagine scelto.** La dashboard aggiunge un'azione di riavvio che consente ai revisori di specificare quante pagine elaborare per quel documento, entro il suo effettivo numero di pagine.
* **Visualizzare il limite di elaborazione.** La dashboard può mostrare le pagine elaborate rispetto al totale per un documento limitato. L'impostazione **Pagine da elaborare** dell'organizzazione è raggruppata sotto Elaborazione documenti in **Classifica ed estrai**.
* **Controllare l'estrazione dei campi nascosti.** Gli amministratori possono scegliere se i campi nascosti partecipano all'estrazione tramite l'impostazione **Estrai campi nascosti**.
* **Lavorare più velocemente su batch più grandi.** I riavvii in blocco dei documenti, gli import CSV dei dati master, l'elaborazione PDF e l'estrazione dei campi basata su regole ricevono miglioramenti delle prestazioni.
* **Estrazione AI più resiliente.** I timeout vengono segnalati come timeout e i guasti dei modelli supportati possono passare a un altro modello disponibile. Ulteriori correzioni gestiscono chiavi ripetute nell'output AI, sinonimi di campo configurati e definizioni di tabelle salvate vuote.
* **Mantenere il valore appena inserito.** Salvare una cella di tabella senza prima fare clic altrove preserva il valore digitato. Le date con nomi di mesi confusi dall'OCR vengono gestite in modo più affidabile.

## Abbinamento, approvazione ed esportazione degli ordini di acquisto

La [guida alle Regole di abbinamento degli ordini di acquisto](../../administration-and-setup/settings/global-settings/document-types/more-settings/purchase-order/purchase-order-matching-rules.md) spiega come abilitare l'abbinamento basato su regole, configurare tipi di abbinamento e tolleranze, impostare l'ordine di esecuzione e gestire le versioni delle regole.

* **Abbinare in entrambe le direzioni.** Selezionare le righe del documento e collegarle alle righe dell'ordine di acquisto, oppure partire dalle righe dell'ordine di acquisto. Questo è utile quando molte righe della nota di consegna si riferiscono a una sola riga dell'ordine di acquisto.
* **Preservare il dettaglio delle righe uno-a-molti.** Una configurazione di abbinamento può ora mantenere una sub-riga individuale per ogni riga del documento quando più righe corrispondono a una riga dell'ordine di acquisto. Questa opzione è disattivata per impostazione predefinita. L'esportazione generica tramite API può raggruppare le richieste per colonne di riga configurate, supportando consegne o container che richiedono record di destinazione separati.
* **Configurare il fallback dell'ultima riga.** Le organizzazioni possono controllare se la riga rimanente del documento e dell'ordine di acquisto può essere abbinata tramite il fallback a riga singola.
* **Abbinamento e visualizzazione più accurati.** Le correzioni preservano la corretta base di prezzo per gli abbinamenti convertiti in pacchetti, ereditano lo stato della riga dell'ordine di acquisto nelle righe di pianificazione e mostrano le quantità ricevute dalle righe di ricezione.
* **Prevenire l'approvazione prematura e il lavoro duplicato.** L'approvazione finale è bloccata mentre le discrepanze rilevanti dell'ordine di acquisto rimangono non approvate. L'esecuzione ripetuta del flusso di lavoro non crea un altro task aperto per lo stesso gruppo e i controlli di esportazione duplicata vengono eseguiti prima dell'approvazione.
* **Separare Exported da Finished.** Le azioni di esportazione possono selezionare lo stato dopo un'esportazione riuscita. **Exported** ha il proprio badge nella dashboard. Le organizzazioni che abilitano il blocco del documento completato impediscono ai flussi di lavoro ordinari o ai riavvii di riaprire i documenti completati; le sovrascritture autorizzate vengono registrate.
* **Risoluzione dei problemi del flusso di lavoro più chiara.** Un filtro della dashboard trova i documenti trattenuti dal limite di esecuzione del flusso di lavoro. Le esecuzioni del flusso di lavoro possono essere ispezionate in un popup e un cambio di stato rifiutato nomina lo stato del documento.
* **Ulteriori correzioni di esportazione.** I tentativi di convalida e approvazione M3 sono regolati e le configurazioni di esportazione dei fornitori condizionali vengono gestite correttamente.

## Usabilità quotidiana e accesso

* **Navigazione più affidabile.** Gli indirizzi dei documenti aggiornati hanno redirect per i link più vecchi. I deep link NOVA mantengono il canale previsto durante l'accesso e il progresso del caricamento mostra quale parte della pagina viene preparata.
* **Preferenze di lavoro personali.** L'ordine delle colonne dell'ordine di acquisto viene salvato per utente e la schermata di approvazione ricorda il pannello laterale aperto dell'utente.
* **Viste di task e dashboard più affidabili.** I task senza assegnatario possono essere elencati, aperti e assegnati. La board dei task si ricarica quando l'organizzazione selezionata è pronta, gli intervalli di data personalizzati della dashboard vengono applicati correttamente e le righe di documento duplicate vengono evitate.
* **Etichette e log migliori.** Gli amministratori possono modificare le chiavi di traduzione dei campi e delle colonne di tabella. Le colonne del log dei documenti possono essere ridimensionate, le colonne della dashboard personalizzate gestiscono identificatori di campo misti maiuscole/minuscole e le etichette e i nomi dei file lunghi si adattano in modo più coerente.
* **Ambito delle notifiche.** Le regole di email sullo stato del documento possono essere limitate a una sub-organizzazione.
* **Onboarding dei fornitori.** I link magici per la registrazione al Portale Fornitori rimangono validi per **21 giorni invece di 7 giorni**. Gli amministratori possono anche configurare l'intestazione dell'errore di caricamento per un campo file in un layout fornitore.
* **Affidabilità dell'accesso.** L'accesso SAML non riutilizza più sessioni scadute o revocate. L'accesso di gestione supporta il passaggio MFA obbligatorio e le iscrizioni inattive non possono ricevere un nuovo invito per impostare la password.
* **Immagini della Bacheca Idee.** Le immagini caricate vengono archiviate e servite separatamente dalla descrizione dell'idea, migliorando la gestione delle immagini.
* **Cambio controllato del canale.** L'impostazione Canale di rilascio può essere resa di sola lettura quando il cambio non è abilitato per l'ambiente. Seguire l'annuncio di rilascio per la disponibilità.

## Assistenti connessi e strumenti di integrazione

Per le organizzazioni e i partner che utilizzano l'integrazione DocBits MCP, NOVA aggiunge strumenti per elencare le regole di convalida risolte, testare una regola su un documento senza salvare le modifiche e spiegare le prove dell'esecuzione delle regole archiviate. Gli assistenti connessi possono anche elencare le richieste di miglioramento e inviare un'approvazione autorizzata dall'amministratore tramite lo stesso processo di revisione dell'app web. Si applicano le autorizzazioni esistenti per organizzazione e documento.

## Funzionalità già presenti in VESTA

NOVA trasferisce anche le funzionalità elencate di seguito. Dove l'accesso era precedentemente limitato alla beta di VESTA, la disponibilità standard fa parte di questa release di NOVA ed è pianificata per l'hotfix di VESTA dell'11 novembre 2026. L'elenco descrive la funzionalità precedente, insieme alle modifiche di disponibilità e ai miglioramenti spiegati sopra:

* L'originale Assistente impostazioni, la sua ricerca nella documentazione, il flusso di base anteprima/conferma/annulla e gli avvisi proattivi sulla salute dell'importazione email/FTP.
* I livelli AI Fast, Full, Nexus e Auto e l'impostazione della modalità visiva.
* Il Controllo Campo Intestazione e l'originale report sull'origine del valore.
* La prima release di Touchless Intelligence, la diagnosi del fornitore, l'analisi in blocco e il diagramma decisionale dell'ordine di acquisto.
* I motori di regole sottostanti per convalida, trasformazione e selezione del layout, le trasformazioni dopo la ricerca dei dati anagrafici e il log di base dell'esecuzione delle regole.
* Miglioramenti precedenti alla ricerca nella dashboard, MFA, domini email organizzativi verificati, tolleranza degli addebiti e aumento del limite di esecuzione del workflow a 50.

Consultare l'[hotfix VESTA del 14 ottobre](incremental-updates-14-october-2026.md), l'[hotfix del 15 settembre](incremental-updates-15-september-2026.md) e le [note di rilascio precedenti](README.md#vesta-hotfix-releases) per la cronologia dei rilasci di VESTA.

## Versioni del servizio NOVA

Queste sono le versioni e le date di distribuzione della **build di NOVA disponibile nell’ambiente di test dal 16 ottobre 2026**. Il rilascio in produzione è previsto per il **4 novembre 2026**; questa istantanea dell’ambiente di test non determina le versioni definitive di produzione. Le date si riferiscono alla distribuzione dei singoli servizi.

| Servizio | Versione | Timestamp di distribuzione |
| --- | --- | --- |
| API Service | `13.26.5` | 16.10.2026 11:57:49 |
| Auth Bridge | `0.5.11` | 08.10.2026 10:56:15 |
| Auth Service | `1.84.3` | 16.10.2026 12:19:50 |
| Auto Accounting | `1.23.6` | 15.09.2026 09:42:57 |
| Barcode Service | `1.20.3` | 15.10.2026 14:17:18 |
| Docflow Service | `2.13.9` | 15.10.2026 16:14:37 |
| Docnet Service | `1.59.1` | 12.10.2026 00:59:12 |
| Email Service | `1.44.4` | 16.10.2026 11:44:58 |
| Extraction Service | `1.63.1` | 15.10.2026 19:34:17 |
| FTP Service | `1.37.4` | 15.10.2026 10:42:01 |
| Fulltext Service | `1.46.1` | 12.10.2026 05:16:16 |
| Ideas Service | `0.5.6` | 14.10.2026 12:06:00 |
| OCR Service | `1.11.8` | 12.10.2026 01:00:00 |
| Operator Service | `1.45.0` | 12.10.2026 09:35:25 |
| PO Match Service | `1.65.7` | 14.10.2026 16:14:20 |
| Web App | `10.72.2` | 16.10.2026 12:04:41 |

I numeri di versione avanzano indipendentemente sui due canali. Un numero più alto non significa di per sé che un servizio abbia una nuova funzionalità per il cliente. Le modifiche esaminate per Auto Accounting, Barcode, Docnet, Fulltext, OCR e Operator sono modifiche di manutenzione o di affidabilità dell'elaborazione; non introducono un flusso di lavoro separato per il cliente in questo confronto. Gli aggiornamenti di Auth Bridge migliorano l'affidabilità della sincronizzazione degli account tra regioni.
