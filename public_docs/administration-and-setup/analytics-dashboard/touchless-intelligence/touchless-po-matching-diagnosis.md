# Diagnosi dell'abbinamento PO

<!-- touchless-admin-video-v2-20261104:start -->
**Capitolo video (versione di verifica):** [Seguire un documento](https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/touchless-intelligence-preview-admin/v2/it.html#chapter=07).
<!-- touchless-admin-video-v2-20261104:end -->

## Panoramica

Molte fatture si fermano all'ordine di acquisto. La fattura dice una cosa, l'ordine di acquisto (PO) ne dice un'altra e i controlli configurati non riescono a risolvere la differenza automaticamente. **Un'estrazione corretta può comunque portare a un abbinamento PO bloccato quando i dati del sistema di origine sono diversi.** Una sosta temporanea non è ancora un esito definitivo: un'elaborazione automatica successiva può riuscire, mentre una correzione manuale o un riavvio registrati impediscono a un documento riuscito di essere touchless.

Touchless Intelligence ti mostra **perché** un abbinamento PO è fallito e **come** DocBits ha tentato di abbinare. Questa pagina spiega le due fasi della pipeline coinvolte, i motivi che vedrai e il **PO matching decision flow**, un diagramma che mostra i passaggi di abbinamento uno dopo l'altro.

### Dove vedi l'abbinamento PO in Touchless Intelligence

| Dove                                                                                        | Cosa vedi                                                                                                                                                                       |
| ------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Where touchless is lost first** (scheda di panoramica)                                    | Una barra come _PO line match: PO item mismatch_. Ti dice quanti documenti si sono fermati lì                                                                                   |
| **Supplier opportunities**                                                                  | Un fornitore con la causa principale **PO matching**                                                                                                                            |
| **Supplier Diagnosis**, sezione **How this organisation matches** e **issue cluster**        | Il flusso decisionale con il set di regole della tua organizzazione                                                                                                             |
| **Document Trace**                                                                          | La fase **PO Line Match** con lo stato **blocked** e il motivo                                                                                                                  |
| **Settings → Document Types → More Settings → Purchase Order**                              | Le regole di abbinamento stesse. Vedi [Purchase Order Matching Rules](../../settings/global-settings/document-types/more-settings/purchase-order/purchase-order-matching-rules.md) |

## Le due fasi PO

| Fase                   | Domanda                                            | Si ferma con                                                                                                          |
| ---------------------- | -------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------- |
| **9 · PO Lookup**      | Esiste un ordine di acquisto per questa fattura?   | _Purchase order not found_                                                                                            |
| **10 · PO Line Match** | Ogni riga della fattura corrisponde a una riga PO? | _PO item mismatch_, _PO line identifier mismatch_, _Unit price outside PO tolerance_, _Quantity outside PO tolerance_ |

Un documento che si ferma alla fase 9 o 10 compare con il primo blocco **PO matching** nella coda dei fornitori.

## Motivi per cui un abbinamento PO fallisce

| Motivo che vedi                    | Cosa significa                                                                                             | Causa tipica                                                                                              | Cosa cambiare                                                                                                                                                        |
| ---------------------------------- | ---------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Purchase order not found**       | DocBits non ha trovato alcun ordine di acquisto per il numero PO sulla fattura                             | Il numero PO è letto male o manca; il PO non è ancora stato importato; il PO appartiene a un altro fornitore | Controlla l'estrazione del numero PO per questo fornitore, l'importazione dei dati anagrafici dei PO e il collegamento al fornitore                                   |
| **PO item mismatch**               | Le righe della fattura non corrispondono alle righe del PO                                                 | Il fornitore usa i propri numeri di articolo; la descrizione è diversa; le righe sono state unite o divise | Controlla la mappatura dei numeri di articolo e le **rule priorities** nelle regole di abbinamento; aggiungi una regola per il modo in cui il fornitore identifica le righe |
| **PO line identifier mismatch**    | Il numero o l'identificatore di riga sulla fattura non corrisponde al PO                                    | Il fornitore rinumera le righe                                                                            | Abbina per articolo e quantità invece che per numero di riga                                                                                                          |
| **Unit price outside PO tolerance** | Il prezzo differisce più della tolleranza consentita                                                       | Una variazione di prezzo reale, una differenza di arrotondamento o un'unità di prezzo diversa              | Controlla la **Unit price tolerance** nel set di regole; correggi il PO o chiedi al fornitore                                                                         |
| **Quantity outside PO tolerance**  | La quantità differisce più della tolleranza consentita                                                     | Consegna parziale, consegna in eccesso                                                                    | Controlla **Match quantity on** e la **Quantity tolerance**                                                                                                           |
| **PO matching service error**      | Il servizio di abbinamento non ha potuto rispondere                                                        | Un problema tecnico temporaneo                                                                            | Riavvia i documenti; contatta l'assistenza se si ripete                                                                                                               |
| **Automatic PO export disabled**   | L'impostazione **Auto export if PO matched 100%** è disattivata, quindi i documenti abbinati non vengono esportati automaticamente | L'impostazione è disattivata                                                                              | Attiva l'impostazione se vuoi l'export automatico. Vedi [Auto Export if PO Matched 100%](../../settings/document-processing/module/auto-export-if-po-matched-100.md) |

{% hint style="info" %}
Non tutti i motivi di abbinamento PO si possono risolvere in DocBits. Se il fornitore invia un numero PO sbagliato, la scheda dice **Supplier action only**: il fornitore deve correggere il documento e inviarlo di nuovo.
{% endhint %}

Trovi i casi separati di prezzo e quantità e le loro prove in [Esempi pratici](touchless-examples.md).


## Il PO matching decision flow

Il flusso decisionale mostra come DocBits tenta di abbinare una riga della fattura a una riga PO. Ha **cinque fasi** e vince il primo abbinamento:

1. **Single match validation**: applica le regole in ordine di priorità. È il caso normale, una riga di fattura e una riga PO
2. **Multi match validation**: dopo un abbinamento singolo, quando su un lato sono coinvolte più righe
3. **Total match validation**: solo quando non ha corrisposto nulla. Il totale della riga PO viene confrontato con la somma delle sue righe di tabella
4. **Single mismatch validation**: il prezzo unitario viene ignorato, così una riga può essere abbinata per articolo e quantità anche se il prezzo differisce
5. **Fallback logic**: restano una riga PO e una riga di tabella, quindi vengono accoppiate

Dentro le fasi DocBits prova, in questo ordine:

* **Exact match for all rules**: ogni valore confrontato è identico
* **Tolerance-based match**: i valori numerici possono discostarsi entro la tolleranza
* **Package criteria**: l'ultimo passaggio, basato sui criteri legati al package del set di regole

Ogni passaggio chiede **Match found?** La risposta **Yes** (verde) porta a **Match found** e il documento prosegue. La risposta **No match** (rossa) passa al passaggio successivo e, dopo l'ultimo passaggio, il risultato è **No match found**: il documento si ferma e richiede una persona.

<figure><img src="https://raw.githubusercontent.com/FELLOWPRO/DocBits_Documentation/refs/heads/main/public_docs/.gitbook/assets/touchless-po-matching-flow.png" alt="Il flusso decisionale dell'abbinamento PO: intestazione del set di regole, cinque fasi di abbinamento numerate con i loro passaggi e i punti finali Match found e No match found"><figcaption><p>Il flusso decisionale dell'abbinamento PO, aperto da <strong>How this organisation matches</strong> nella pagina Supplier Diagnosis. L'intestazione mostra il set di regole (versione 7, di proprietà di questa organizzazione) e le tolleranze. Sotto, le cinque fasi con i loro passaggi scorrono dall'alto verso il basso. Il verde porta a <strong>Match found</strong>, il rosso passa al passaggio successivo e termina in <strong>No match found</strong>. Organizzazione di esempio con dati demo.</p></figcaption></figure>

### Cosa ti dice l'intestazione del diagramma

| Campo                                             | Significato                                                                                            |
| ------------------------------------------------- | ------------------------------------------------------------------------------------------------------ |
| **Document type**                                 | Il tipo di documento a cui appartiene il set di regole, per esempio INVOICE                             |
| **Rule set version**                              | La versione delle regole di abbinamento, per esempio v3                                                |
| **Rule set owner**                                | **This organisation** (le tue regole) oppure **Shipped default rule set** (le regole standard di DocBits) |
| **Published**                                     | Quando è stata pubblicata la versione                                                                  |
| **Match quantity on**                             | Quale quantità viene confrontata (quantità ordinata, quantità aperta)                                   |
| **Tolerance amount**                              | Se le tolleranze provengono dagli attributi del tipo di documento o dal set di regole                   |
| **Unit price tolerance** / **Quantity tolerance** | Quanto possono discostarsi un prezzo o una quantità                                                     |
| **Default tolerance**                             | La tolleranza per tutti gli altri valori numerici                                                       |

Nell'esempio sopra le tolleranze mostrano **not configured** e **not in force: attribute decides**. Significa: il set di regole non ha una tolleranza propria e la riga **Tolerance amount** dice che le tolleranze provengono dagli **attributi del tipo di documento**. Una tolleranza decide solo quando è in vigore. Leggi questa riga per prima quando una differenza di prezzo o quantità blocca i documenti: ti dice **dove** cambiare la tolleranza.

Lo stato del set di regole è mostrato come nota: **Active version** (decidono queste regole), **Approved, not active**, **Draft, not yet in force** o **Version state unknown**. Decide solo la versione attiva.

Se le regole di trasformazione hanno modificato un documento prima dell'abbinamento, il diagramma lo indica, per esempio _2 applied: (nomi)_ o _"(regola)" rebuilt (table): the PO match was lost here_. È una causa nascosta frequente: una regola che riformatta una tabella può rompere un abbinamento che prima funzionava.

## Esempi

I numeri negli esempi sono illustrativi.

### Esempio 1: prezzo entro la tolleranza

Una riga di fattura ha un prezzo unitario di **10.40**. La riga PO indica **10.00**. La tolleranza sul prezzo unitario è **5 %**.

* L'**Exact match** fallisce (10.40 non è 10.00).
* Il **Tolerance-based match** riesce: la differenza è **4 %**, entro il 5 %.
* La riga viene abbinata. **Match found.**

Con una tolleranza del **3 %** anche il tolerance-based match fallisce. Dopo tutte le fasi il documento si ferma con **Unit price outside PO tolerance**. Il diagramma mostra esattamente questo percorso e la correzione è la tolleranza (se il 4 % è accettabile per il tuo business) oppure una correzione presso il fornitore.

### Esempio 2: i numeri di articolo del fornitore sono diversi dai tuoi

Un fornitore fattura l'articolo **"A-4711-X"**, il tuo PO indica **"4711"**. Nessuna regola confronta i due valori, quindi non viene trovato alcun abbinamento e Touchless Intelligence raggruppa tutte le fatture di questo fornitore in un cluster: **PO line match, PO item mismatch**, 27 documenti.

* Nel cluster leggi _27 affected, 27 recoverable_, incremento previsto per esempio **+8.7 pp**.
* La correzione è dalla tua parte: aggiungi o riordina una regola che abbina sul numero di articolo del fornitore o sulla descrizione, oppure mantieni i numeri di articolo del fornitore nei dati anagrafici.
* Dopo aver cambiato la regola, applica la modifica con una [proposta di modifica](touchless-change-proposals.md) e leggi la **Change history** due settimane dopo: tasso AP touchless prima e dopo.

### Esempio 3: l'ordine di acquisto non c'è ancora

Le fatture arrivano prima che il PO sia stato importato. Si fermano a **PO Lookup** con **Purchase order not found**. Il cluster mostra un picco breve. La correzione è l'ordine dei tuoi processi, oppure la pianificazione dell'importazione dei PO, non le regole di abbinamento. Controlla **Where touchless is lost first**: una barra _PO lookup: Purchase order not found_ che cresce dopo ogni interruzione dell'importazione indica questa causa.

### Esempio 4: una regola ha ricostruito la tabella

Dopo l'attivazione di una regola di trasformazione per la tabella di un fornitore, il tasso di abbinamento di quel fornitore è calato bruscamente. Il diagramma di un documento interessato dice _"(regola)" rebuilt (table): the PO match was lost here_. La correzione consiste nell'adeguare o annullare la regola di trasformazione, non le regole di abbinamento.

## Una routine per i problemi di abbinamento PO

1. Apri **Where touchless is lost first**. Una fase di abbinamento PO è tra le prime tre?
2. Apri **Supplier opportunities** e ordina per **Expected lift**. Prendi il fornitore con la causa principale **PO matching** e lo stato **RECOVERABLE**.
3. Apri la **Supplier Diagnosis** e leggi il cluster: motivo, documenti interessati, **What to change**, **Missing evidence**.
4. Apri **How this organisation matches** e controlla il set di regole: versione, proprietario e tolleranze.
5. Apri un **documento di esempio** e il suo [Document Trace](touchless-document-trace.md): quale fase, quale motivo?
6. Cambia **una** cosa (ordine delle regole, tolleranza, mappatura degli articoli) con un'anteprima, così la **Change history** può misurarla.

## Pagine correlate

* [Touchless Intelligence](./)
* [Diagnosi fornitori e cluster di problemi](touchless-supplier-diagnosis.md)
* [Document Trace](touchless-document-trace.md)
* [Proposte di modifica e report](touchless-change-proposals.md)
* [Purchase Order Matching Rules](../../settings/global-settings/document-types/more-settings/purchase-order/purchase-order-matching-rules.md)
* [PO Matching Cards: Complete Guide](../../workflow/cards-overview/po-matching-complete-guide.md)

<!-- Documentation review 2026-11-04: extraction quality vs process outcomes; KPI and terminal-outcome definitions checked against DocBits_API c51f350c728acb8ac964098d15f7b006bce273f4, module/automation_intelligence/kpi.py and bucket.py. Existing native screenshots retained and checked separately from illustrative examples. -->

<!-- Completion review 2026-11-04: owned synthetic PO examples, MCP schema/read evidence, human-action classification, KPI labels and screenshot proof limits. -->
