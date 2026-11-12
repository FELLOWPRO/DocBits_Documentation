---
description: "Percorso dal principiante all’esperto"
---

# Percorso dal principiante all’esperto

Sette livelli portano dal primo sguardo al designer dei workflow fino alla responsabilità di una modifica su un workflow in produzione. Ogni livello indica un obiettivo, i passaggi da svolgere nella propria organizzazione di test e un risultato che si può verificare. Seguiteli in ordine e costruite ogni esercizio da soli: ogni livello si appoggia alla configurazione di quello precedente.

1. [Orientamento e modello di esecuzione](#level-1)
2. [Prima regola propria](#level-2)
3. [Campi, tipi e limiti](#level-3)
4. [Regole aziendali e approvazioni](#level-4)
5. [Controllo Advanced e sotto-workflow](#level-5)
6. [Calcolo, integrazione ed export](#level-6)
7. [Modifiche e gestione esperta](#level-7)

## Prima di iniziare

* Un’organizzazione di test propria, con una fattura sintetica al suo interno. Non esercitatevi mai su documenti dei clienti.
* Il vostro ruolo, la licenza workflow e l’abilitazione Advanced, verificati prima del livello 1.
* Gli esercizi importati restano inattivi finché non li avete testati.
* I dati JSON completi vanno in **Advanced Test → Custom Data**.
* Le approvazioni e le integrazioni reali richiedono utenti e destinazioni di test propri; un test nel designer non le sostituisce.

## 1. Orientamento e modello di esecuzione <a href="#level-1" id="level-1"></a>

{% embed url="https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/workflow-learning-step-01-admin/v1/it.mp4" %}

[Aprire il video con sottotitoli e trascrizione in italiano](https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/workflow-learning-step-01-admin/v1/it.html).

**Obiettivo:** Sapere che cosa avvia un workflow e che cosa un risultato di test può dire, o non dire, su un’esecuzione reale.

1. Controllate l’organizzazione, il vostro accesso, il modulo workflow e l’abilitazione Advanced.
2. Dite When–And–Then con parole vostre, poi spiegate dove finisce una regola lineare e come un grafo Advanced segua invece le proprie uscite collegate.
3. Tenete separate quattro cose che nel designer si somigliano: il filtro sul tipo di documento, l’evento di esecuzione, il salvataggio e l’attivazione.

**Criterio di completamento:** Sapete dire quando una regola viene considerata e quale prova distingue una simulazione da un’esecuzione su un documento reale.

**Approfondimento:** [Quando viene eseguito il mio workflow?](workflow-execution-model.md) · [Cambiare stato senza riavviare il workflow](masterclass/status-and-reentry.md)

## 2. Prima regola propria <a href="#level-2" id="level-2"></a>

{% embed url="https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/workflow-learning-step-02-admin/v1/it.mp4" %}

[Aprire il video con sottotitoli e trascrizione in italiano](https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/workflow-learning-step-02-admin/v1/it.html).

**Obiettivo:** Portare una regola dal designer a un risultato verificato senza toccare un documento.

1. Costruitela nell’Advanced Builder: When Invoice → And invoice\_id = WF-TRAINING-001 → And total\_amount > 1000 → Then wf\_training\_route = REVIEW. Una regola lineare di queste dimensioni non ha bisogno di un nodo di controllo.
2. Salvatela e controllate nell’elenco delle regole che sia ancora inattiva, perché salvare una nuova regola può già attivarla. Advanced Test è una superficie di esecuzione separata: valuta il grafo nel builder, non la regola attivata.
3. Eseguite Advanced Test con dati completi per 999, 1000 e 1000.01. Annotate per ogni caso tipo di campo, operatore e uscita scelta, poi aggiungete un caso in cui l’importo manca del tutto.

**Criterio di completamento:** REVIEW viene raggiunto solo con 1000.01, un importo mancante compare come errore e non come risultato normale sotto la soglia, e alla fine la regola è di nuovo disattivata.

**Approfondimento:** [Caso aziendale Advanced: instradamento delle fatture](advanced-workflow-case-study.md) · [Kit di esercizi workflow](workflow-training-kit.md)

## 3. Campi, tipi e limiti <a href="#level-3" id="level-3"></a>

{% embed url="https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/workflow-learning-step-03-admin/v1/it.mp4" %}

[Aprire il video con sottotitoli e trascrizione in italiano](https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/workflow-learning-step-03-admin/v1/it.html).

**Obiettivo:** Sapere che cosa confronta davvero una condizione prima di fidarvi del suo risultato.

1. Provate il controllo del vuoto su un campo mancante, `null`, testo vuoto, spazi, `false`, `0`, `"0"` e `"false"`, e annotate quali contano come vuoti.
2. Calcolate due volte la stessa tolleranza del 2 per cento: una con l’ordine come riferimento (ordine 100, documento 102.02) e una con il documento come riferimento.
3. Passate da Any a All sulla scheda ordine e contate quante righe sono state realmente confrontate.

**Criterio di completamento:** Spiegate vero, falso ed errore partendo da valore, tipo, riferimento e dati presenti. Nella versione 5 della scheda ordine un documento senza riga confrontabile è un errore di dati e non un’approvazione riuscita.

**Approfondimento:** [Field is, Docfield is e confronto tra due campi](masterclass/field-conditions.md) · [Rendere tolleranze e riferimento ordine non ambigui](masterclass/tolerances-and-po.md)

## 4. Regole aziendali e approvazioni <a href="#level-4" id="level-4"></a>

{% embed url="https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/workflow-learning-step-04-admin/v1/it.mp4" %}

[Aprire il video con sottotitoli e trascrizione in italiano](https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/workflow-learning-step-04-admin/v1/it.html).

**Obiettivo:** Inviare una fattura alla persona giusta tramite una tabella di decisione e poi far girare una catena di approvazione che attende la prima persona che controlla.

**Esercizio 1: tabella di decisione con assegnazione diretta**

1. Create una tabella di decisione con due regole che non possono scattare insieme: revisore A fino a 1000, revisore B oltre 1000, usando `cost_center=4711` e `total_amount`.
2. In **Decision Table has Returns** versione 3 impostate `store_data=wf_store_data`. Assegnate il documento con **Assign document based on decision table** e `assignee_type=user`, usando utenti reali della vostra organizzazione di test.
3. Provate una corrispondenza, nessuna, più di una e un ID utente non valido, e portate mancate corrispondenze ed errori di assegnazione su un ripiego esplicito. Accettate l’assegnazione sul documento stesso.

**Esercizio 2: approvazione sequenziale senza assegnazione diretta**

1. Create una seconda regola separata con le schede sequenziali: la scheda di assegnazione sequenziale in posizione 10 per il revisore A, poi la scheda di attività sequenziale in posizione 20 per il revisore B. Lasciate fuori l’assegnazione diretta in questa esecuzione, perché la finalizzazione verificata può saltare il primo destinatario sequenziale quando il documento è già stato assegnato direttamente nella stessa esecuzione.
2. Approvate come A e controllate che B riceva il documento solo dopo la decisione elaborata di A; approvate poi come B.
3. Rifiutate come A in una nuova esecuzione e confermate che l’export non avviene. Provate poi che cosa succede quando non si riesce a determinare alcun destinatario.

**Criterio di completamento:** Distinguete responsabilità, attività, notifica e approvazione reale; A → approvazione → B → approvazione è avvenuto in questo ordine; un rifiuto di A ha impedito l’export; e un destinatario mancante non è stato contato come approvazione conclusa.

**Approfondimento:** [Seguire la tabella di decisione fino all’assegnazione](masterclass/decision-table-routing.md) · [Distinguere assegnazione, attività e approvazione sequenziale](masterclass/assignment-task-sequential.md)

## 5. Controllo Advanced e sotto-workflow <a href="#level-5" id="level-5"></a>

{% embed url="https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/workflow-learning-step-05-admin/v1/it.mp4" %}

[Aprire il video con sottotitoli e trascrizione in italiano](https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/workflow-learning-step-05-admin/v1/it.html).

**Obiettivo:** Unire correttamente percorsi paralleli e passare lavoro a un altro workflow.

1. Confrontate ALL, ANY e OR su due controlli realmente raggiunti: ALL richiede un’uscita corrispondente da ogni origine, ANY e OR ne richiedono una, e verde più arancione dalla stessa origine contano ancora come una sola origine.
2. Guardate un ramo che l’esecuzione non ha preso, come nel caso MERGE-04: Advanced Test valuta ancora l’unione in attesa, mentre l’esecuzione normale la salta appena un predecessore non arriva mai.
3. Eseguite i sette casi dello studio di caso v2 (sopra, sotto, limite, appena sopra, mancante, numero non valido, altra fattura). Poi chiamate con Run Workflow un vostro workflow inattivo e aprite il percorso nella destinazione stessa.

**Criterio di completamento:** Spiegate la differenza del caso MERGE-04 tra test ed esecuzione del passaggio 2, come vengono contate le origini e dove finisce un errore. Una chiamata Run Workflow verde richiede comunque un controllo nella destinazione. V2 qui indica la seconda versione del grafo dello studio di caso: la scheda di stato di ogni percorso porta direttamente alla scheda di chiusura comune, senza nodo OR in attesa.

**Approfondimento:** [Collegare correttamente Wait ALL, Wait ANY e OR](masterclass/control-nodes.md) · [Capire Run Workflow, le condizioni di destinazione e gli errori](masterclass/run-workflow.md) · [Caso aziendale Advanced: instradamento delle fatture](advanced-workflow-case-study.md)

## 6. Calcolo, integrazione ed export <a href="#level-6" id="level-6"></a>

{% embed url="https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/workflow-learning-step-06-admin/v1/it.mp4" %}

[Aprire il video con sottotitoli e trascrizione in italiano](https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/workflow-learning-step-06-admin/v1/it.html).

**Obiettivo:** Calcolare valori, recuperare un risultato da un sistema esterno ed esportare solo dopo un’approvazione reale.

1. Calcolate una colonna e confrontate tutta la tabella prima e dopo, compresa una riga in cui l’espressione regolare non corrisponde e una divisione per zero.
2. Scrivete il contratto di riscrittura con il sistema esterno: quale campo del documento accoglie il risultato, quale scheda o estensione lo scrive lì e come verificate poi il valore salvato. Un HTTP 200 da solo non è un risultato.
3. Pianificate l’export dopo l’approvazione con la vostra configurazione e annotate che cosa controllerete presso il destinatario.

**Criterio di completamento:** Valori successivi nel campo, ricezione presso il destinatario ed elaborazione nell’ERP hanno ciascuno una prova propria. Una simulazione o un export in coda non è una consegna.

**Approfondimento:** [Calcolare tabelle e verificare la dipendenza dalla regex](masterclass/table-calculations.md) · [Verificare la chiamata API e il riuso della risposta](masterclass/api-response-contract.md) · [Varianti di export, attività aperte e stato di chiusura](masterclass/export-lifecycle.md)

## 7. Modifiche e gestione esperta <a href="#level-7" id="level-7"></a>

{% embed url="https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/workflow-learning-step-07-admin/v1/it.mp4" %}

[Aprire il video con sottotitoli e trascrizione in italiano](https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/workflow-learning-step-07-admin/v1/it.html).

**Obiettivo:** Modificare un workflow che non avete costruito e poter annullare la modifica.

1. Esportate il workflow e annotate le versioni delle schede prima di toccare qualcosa.
2. Dopo la modifica ripetete i casi positivi, negativi, di errore e di limite, più una seconda esecuzione dello stesso caso.
3. Riconducete il primo errore a un input e a una configurazione precisi e tenete l’export salvato come via di ritorno.

**Criterio di completamento:** Sapete accettare la modifica, ripristinare la configurazione salvata e confrontare una nuova esecuzione documentale con le prove. Annotate causa, correzione e limiti che restano.

**Approfondimento:** [Diagnosticare sistematicamente gli errori di workflow](workflow-troubleshooting.md) · [Capire le schede e configurarle in modo affidabile](card-reference-standard.md)

## Verificare le conoscenze

| Domanda | Risposta |
| --- | --- |
| `false` è vuoto in Field is v2? | Sì. Il numero 0 e il testo "false" non sono vuoti. |
| Un test OR verde garantisce l’esecuzione documentale? | No. Nel caso verificato MERGE-04 un test valuta l’unione che un’esecuzione documentale salta quando un predecessore non arriva mai. |
| Run Workflow può chiamare una destinazione inattiva? | Sì, nella chiamata esplicita verificata. Controllate comunque le condizioni della destinazione e il risultato. |
| Un HTTP 200 espone automaticamente api.response.cost\_center? | No. Le azioni verificate non offrono questo contratto di output JSON automatico. |
| Un test verde dimostra la ricezione dell’export? | No. Esecuzione documentale, ricezione presso il destinatario ed elaborazione ERP richiedono prove separate. |

## Registrare ciò che avete accettato

Scaricate `workflow-training-kit-v2.zip` dal [kit di esercizi workflow](workflow-training-kit.md), estraetelo e aprite `acceptance-record-template.json`. È un registro vuoto e non qualcosa da importare; lo stesso ZIP contiene anche i dati, le attese e le risposte di test salvate a cui i livelli fanno riferimento.

Annotate che cosa avete testato e come lo sapete: lo scenario, la configurazione (hash dell’export del workflow, versioni delle schede), che cosa vi aspettavate, che cosa avete osservato e che tipo di prova avete. Tenete separati un test in Advanced Test, un controllo isolato dell’origine, un’esecuzione su documento reale, la ricezione presso il destinatario e l’elaborazione nell’ERP, e lasciate aperti i passaggi che non avete testato.
