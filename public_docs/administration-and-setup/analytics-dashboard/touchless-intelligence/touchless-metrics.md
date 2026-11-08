# Metriche e calcolo

<!-- touchless-admin-video-v2-20261104:start -->
**Capitolo video (versione di verifica):** [Calcolo dei tassi](https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/touchless-intelligence-preview-admin/v2/it.html#chapter=03).
<!-- touchless-admin-video-v2-20261104:end -->

### Estrazione corretta e processo touchless sono due cose diverse

**DocBits può leggere correttamente ogni valore di una fattura e la fattura può comunque richiedere l'attenzione di AP, perché i dati del sistema di origine sono diversi.** AP significa Accounts Payable, il team che elabora le fatture dei fornitori. Verifica separatamente queste due domande:

| Domanda | Confronta | Cosa ti dice il risultato |
| --- | --- | --- |
| **DocBits ha letto correttamente il documento?** | La fattura originale rispetto ai campi di intestazione e alle righe di tabella estratti, prima di qualsiasi correzione manuale | Qualità dell'estrazione: il valore estratto corrisponde a ciò che c'è realmente sulla fattura? |
| **Il processo poteva concludersi senza un intervento?** | La fattura estratta correttamente rispetto all'ordine di acquisto e ai dati anagrafici forniti da Infor ERP, insieme alla cronologia di elaborazione registrata | Automazione del processo: i controlli configurati, l'abbinamento e l'export potevano concludersi senza una correzione o un riavvio? |

Un valore diverso in Infor non ti dice di per sé quale lato sia sbagliato. Controlla la fattura, l'ordine concordato e i dati effettivamente importati in DocBits. L'origine può essere errata, l'importazione può essere obsoleta oppure il fornitore può aver fatturato un valore diverso.

{% hint style="info" %}
**Il tasso touchless misura il processo, non l'accuratezza dell'estrazione.** Un documento in AP assisted non dimostra un errore di estrazione di DocBits. Viceversa, una fase di estrazione superata o un punteggio di confidenza alto non dimostrano che ogni valore sia corretto. Per stabilirlo occorre confrontare il documento originale con i valori estratti.
{% endhint %}

Ogni documento termina in esattamente **uno** esito:

| Esito                 | Significato                                                                                         | Conteggio nel tasso                                                                        |
| --------------------- | --------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------ |
| **Pure touchless**    | Elaborato dall'importazione all'export con **nessun intervento umano**                              | Sì, come successo                                                                          |
| **AP touchless**      | Eseguito automaticamente e una persona ha dato solo l'**approvazione di business**. Nessuna correzione necessaria | Sì, come successo                                                                          |
| **AP assisted**       | Concluso con successo, ma una persona ha dovuto **correggere un campo, riavviare il documento** o intervenire in altro modo; può servire anche quando l'estrazione era corretta | Sì, fuori dal numeratore touchless; non identifica di per sé la causa |
| **Process exception** | Terminato con un **errore**, **rifiutato**, **respinto dall'ERP** o **bloccato** nella pipeline     | Sì, come mancato successo                                                                  |
| **In progress**       | Non ancora concluso                                                                                 | **No**. Non ha ancora un esito                                                              |
| **Not eligible**      | Eliminato, archiviato, documento di test o tipo di documento escluso                                | **No**                                                                                     |

L'**AP touchless rate**, che include i documenti con sola approvazione, è:

```
rate = (Pure touchless + AP touchless)
       ÷ (Pure touchless + AP touchless + AP assisted + Process exception)
```

Qui **AP touchless** al numeratore è l'esito del documento "sola approvazione". L'**AP touchless percentage** del pannello è il tasso combinato: documenti pure più documenti con sola approvazione. **Non sommare le due percentuali mostrate.** Il tasso pure usa al numeratore solo i documenti pure, con lo stesso denominatore.

I documenti ancora **in progress** o **not eligible** non entrano mai nel calcolo. Questo protegge il tasso: un documento arrivato cinque minuti fa non può abbassarlo.

{% hint style="info" %}
**Un tocco conta per sempre.** Una volta che una persona ha toccato un documento, questo resta conteggiato come toccato, anche se una successiva esecuzione automatica non avrebbe richiesto nessuno. **Riavviare un documento non lo rende di nuovo touchless.** Il tasso riflette il lavoro che è stato fatto.
{% endhint %}

### Esempio di calcolo (numeri illustrativi)

In 30 giorni sono arrivati 200 documenti:

| Esito                         | Documenti |
| ----------------------------- | --------- |
| Pure touchless                | 120       |
| AP touchless                  | 30        |
| AP assisted                   | 30        |
| Process exception             | 10        |
| In progress                   | 8         |
| Not eligible (documenti di test) | 2      |

* Denominatore: 120 + 30 + 30 + 10 = **190**. Gli 8 documenti in progress e i 2 not eligible restano fuori.
* **Pure touchless**: 120 ÷ 190 = **63,2 %**
* Quota con **sola approvazione**: 30 ÷ 190 = **15,8 %**. È la quota di quell'esito, non il tasso AP touchless combinato.
* **AP touchless rate**: (120 + 30) ÷ 190 = **78,9 %**

La scheda mostra un **obiettivo** (70 % se la tua organizzazione non ne usa un altro). In questo esempio il tasso AP combinato è sopra 70%, mentre il tasso pure di 63,2% è sotto. Confronta l'obiettivo con il tasso indicato dalla scheda o dal grafico pertinente.

Fai clic su **How touchless is calculated** in alto a destra per aprire questa spiegazione dentro DocBits, con i numeri del tuo periodo (documenti nel periodo, ancora in progress, esclusi, misurati).

<figure><img src="https://raw.githubusercontent.com/FELLOWPRO/DocBits_Documentation/refs/heads/main/public_docs/.gitbook/assets/touchless-report-methodology-en-20261104.png" alt="Popolazione di addestramento attuale: 201 fatture completate ammissibili, nessuna ancora in elaborazione o esclusa. Le 107 fatture completamente automatiche danno 53,2%; aggiungendo 11 fatture con sola approvazione si ottengono 118 e 58,7%. Questi tassi di processo non misurano l'accuratezza dell'estrazione."><figcaption><p>Popolazione di addestramento attuale: 201 fatture completate ammissibili, nessuna ancora in elaborazione o esclusa. Le 107 fatture completamente automatiche danno 53,2%; aggiungendo 11 fatture con sola approvazione si ottengono 118 e 58,7%. Questi tassi di processo non misurano l'accuratezza dell'estrazione.</p></figcaption></figure>
<!-- English source image: touchless-report-methodology-en-20261104.png -->

### Esempio: estrazione corretta al 100%, AP touchless all'80%

Supponiamo che una verifica delle fatture originali e dei loro valori estratti confermi che **tutte le 100 fatture completate e ammissibili sono state estratte correttamente**. I loro esiti di elaborazione sono:

| Cosa è successo | Documenti | Esito |
| --- | --- | --- |
| Fattura e dati di origine coincidevano; l'intero processo si è concluso automaticamente | 70 | Pure touchless |
| Fattura e dati di origine coincidevano; era necessaria solo l'approvazione di business | 10 | AP touchless (esito sola approvazione) |
| I dati della fattura sono stati estratti correttamente, ma i dati Infor importati erano diversi. AP ha chiarito la discrepanza e ha riavviato manualmente i documenti in DocBits dopo la correzione dei dati di origine; i documenti si sono poi conclusi con successo | 20 | AP assisted |

* **Documenti estratti correttamente in questo campione verificato:** 100 ÷ 100 = **100%**.
* **Pure touchless rate:** 70 ÷ 100 = **70%**.
* **AP touchless rate:** (70 + 10) ÷ 100 = **80%**.

Non c'è contraddizione: l'estrazione era corretta su tutte le fatture, mentre 20 hanno richiesto un intervento di elaborazione a causa dei dati di origine. Il **dato del 100% di estrazione è un risultato illustrativo di una verifica separata dei documenti**, non un KPI aggiuntivo mostrato da questo pannello. Non calcolarlo dai soli esiti touchless.

### Esempi: che cosa ha dovuto fare davvero AP?

I casi seguenti sono illustrativi e non sono i singoli documenti dietro gli screenshot. Gli esiti positivi presuppongono che l'elaborazione sia conclusa, compresa la conferma ERP dove richiesta.

| Caso | Fattura originale / estrazione DocBits / dati di origine | Azione e esito di AP | Dove indagare |
| --- | --- | --- | --- |
| **Errore di estrazione** | Numero PO `45001234` / estratto erroneamente come `45001284` / l'ordine corretto `45001234` esiste in Infor | AP corregge il numero estratto; la fattura si chiude come **AP assisted** | Estrazione per questo fornitore |
| **Discrepanza nel sistema di origine** | Prezzo unitario €10.00 / estratto correttamente €10.00 / l'ordine Infor importato indica €9.00, fuori dalla tolleranza configurata | AP conferma che €10.00 è il prezzo concordato, dispone la correzione dell'ordine e riavvia manualmente la fattura in DocBits; si chiude come **AP assisted** | Dati dell'ordine in Infor e sua importazione |
| **Ritardo nell'importazione** | Il numero PO è corretto sulla fattura e in DocBits / l'ordine esiste in Infor ma non è arrivato in DocBits | Se una successiva importazione e un nuovo tentativo si concludono automaticamente senza intervento umano o approvazione registrati, l'esito può restare **Pure touchless**. Un riavvio manuale seguito da successo dà **AP assisted** | Momento dell'importazione e cronologia delle esecuzioni reali |
| **Rifiuto ERP** | L'estrazione è corretta, ma l'ERP rifiuta il documento esportato | **Process exception** finché è classificato come rifiuto ERP definitivo, anche se qualcuno era intervenuto in precedenza | Rifiuto ERP e prove dell'export |

**Anche una piccola correzione registrata o un riavvio manuale contano come intervento.** AP assisted significa "una persona ha contribuito a elaborare il documento"; non è il nome di un assistente AI separato. Un problema nei dati di origine e un problema di estrazione possono quindi avere lo stesso esito ma richiedere correzioni diverse.

La classificazione usa gli eventi registrati da DocBits. Non dare per scontato che un lavoro svolto solo in Infor, senza un corrispondente evento registrato in DocBits, venga automaticamente conteggiato come intervento AP. Tieni quel lavoro anche nella diagnosi.

### Quali azioni di AP contano come intervento?

Quanto segue presuppone una conclusione positiva, compresa la conferma ERP richiesta. Contano l'azione registrata e chi l'ha eseguita, non quanto è durato il lavoro.

| Azione | Effetto sull'esito del documento |
| --- | --- |
| Aprire, leggere, filtrare, confrontare o visualizzare in anteprima | Non crea di per sé un intervento di elaborazione; Pure Touchless resta possibile |
| Dare l'approvazione di business, compresa una seconda approvazione | AP Touchless, se non c'è stato un intervento di elaborazione |
| Modificare e salvare un campo di intestazione o una cella di tabella | AP Assisted; conta anche una sola correzione salvata |
| Convalidare manualmente e far avanzare un documento, anche senza correggere un valore | AP Assisted; la convalida manuale è distinta dalla sola approvazione |
| Riavviare manualmente l'elaborazione o l'export | AP Assisted; una successiva esecuzione automatica non elimina l'intervento |
| Nuovo tentativo automatico del sistema o scrittura automatica del workflow | Non crea di per sé un intervento umano; i tocchi umani precedenti restano |
| Correggere i dati solo in Infor | Il lavoro esterno non è automaticamente un evento registrato in DocBits; documentalo a parte e controlla l'azione successiva in DocBits |
| Rifiuto ERP definitivo dopo una correzione | Prevale Process exception; l'intervento resta nella cronologia |

Un clic su Save senza prova di un valore modificato non dimostra una correzione. Controlla se ha attivato anche la convalida manuale o un riavvio.

### L'etichetta AP ha due significati

| Posizione | Significato |
| --- | --- |
| Percentuale AP in evidenza | Pure + sola approvazione combinati: (120 + 30) / 190 = 78.9% |
| Conteggio documenti sotto quella percentuale nel report corrente | Pure + sola approvazione combinati: 150 = 120 + 30 |
| Categoria di esito AP Touchless, come il bucket MCP `AP_TOUCHLESS` | Categoria separata sola approvazione: 30 / 190 = 15.8% |
| Linea AP blu nello [screenshot del trend del pannello](touchless-dashboard.md) corrente | Tasso Pure + sola approvazione combinato in ogni punto, con la popolazione di quel punto |

Le categorie di esito finali sommano al 100% della popolazione misurata. Le percentuali Pure e AP combinata in evidenza si sovrappongono e non devono essere sommate.

### Quanto sono attuali i numeri

Gli esiti vengono **ricalcolati ogni 15 minuti**. L'esito di un documento può cambiare anche dopo la sua prima comparsa: l'ERP può confermare un export ore dopo. La riga **Data as of …** in fondo alla scheda mostra quando i numeri sono stati calcolati l'ultima volta.





## Pagine correlate

* [Touchless Intelligence](./)
* [Usare il pannello](touchless-dashboard.md)
* [Esempi pratici: prezzo e quantità](touchless-examples.md)
* [Diagnosi fornitori e cluster di problemi](touchless-supplier-diagnosis.md)
* [Diagnosi dell'abbinamento PO](touchless-po-matching-diagnosis.md)
* [Document Trace](touchless-document-trace.md)
* [Proposte di modifica e report](touchless-change-proposals.md)
* [Spiegare e migliorare Touchless con MCP](touchless-mcp.md)

<!-- Documentation review 2026-11-04: extraction quality vs process outcomes; KPI and terminal-outcome definitions checked against DocBits_API c51f350c728acb8ac964098d15f7b006bce273f4, module/automation_intelligence/kpi.py and bucket.py. Existing native screenshots retained and checked separately from illustrative examples. -->
<!-- Completion review 2026-11-04: owned synthetic PO examples, MCP schema/read evidence, human-action classification, KPI labels and screenshot proof limits. -->
