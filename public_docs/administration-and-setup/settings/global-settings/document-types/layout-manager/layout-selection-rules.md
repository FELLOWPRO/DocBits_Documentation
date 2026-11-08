# Regole di selezione del layout

## Panoramica

Un **layout** stabilisce quali campi e gruppi vede un utente — e in quale ordine — nelle schermate di **convalida**, **approvazione**, **rifiuto** e **revisione** di un documento. I layout si progettano nel [Layout Manager](./).

Tradizionalmente DocBits sceglieva il layout in base all'**origine** del documento: il paese o la regione ricavati dalle impostazioni di lingua del documento, ad esempio `DE` o `US`. Ogni origine aveva la propria copia del layout e nient'altro poteva influenzare la scelta.

Con le **regole di selezione del layout**, i layout diventano elementi riutilizzabili e indipendenti dall'origine, e sono le **regole** a decidere quale layout riceve un documento:

> _Quando_ il documento soddisfa una condizione, _allora_ riceve questo layout. Le regole vengono verificate dall'alto verso il basso; **vince la prima regola che corrisponde**. Se nessuna regola corrisponde, viene utilizzato il **layout predefinito**.

L'origine resta disponibile, come una condizione tra le tante. Una regola può altrettanto bene considerare il fornitore, l'importo, lo stato del documento, il metodo di estrazione o qualsiasi campo dell'intestazione.

### Problemi che risolvono

| Esigenza                                                          | Layout classici basati sull'origine        | Con le regole di selezione                                                            |
| ------------------------------------------------------------------- | ------------------------------------------- | ------------------------------------------------------------------------------------- |
| Le fatture di un fornitore richiedono campi aggiuntivi (progetto, numero doganale) | impossibile senza una nuova origine        | regola _Supplier ID is 20723_ → layout "Fattura con campi progetto"                    |
| I documenti DE, AT e CH devono avere lo stesso aspetto              | tre copie dello stesso layout da mantenere | un solo layout, una regola per origine (o un gruppo ANY) che punta ad esso             |
| Le fatture elettroniche richiedono una schermata più semplice dei PDF scansionati | non possibile                             | regola _Extraction Method is ELECTRONIC\_DOCUMENT_ → layout "Fattura elettronica"       |
| Le fatture di importo elevato richiedono più campi nella schermata di approvazione | non possibile                            | regola di approvazione _Total Amount greater than 10000_ → layout "Approvazione importi elevati" |
| Il secondo approvatore deve vedere una schermata diversa dal primo  | tipo di layout separato "seconda approvazione" | regola di approvazione _Document Status is Pending second approval_ → layout "Seconda approvazione" |

## Attivare i layout basati su regole

I layout basati su regole vengono attivati **per tipo di documento** da un **amministratore dell'organizzazione**.

1. Vai su **Settings → Document Processing → Document Types**.
2. Fai clic sull'icona **settings** (ingranaggio) sulla scheda del tipo di documento.
3. Apri **Manage Layouts** e attiva l'interruttore.

<figure><img src="https://raw.githubusercontent.com/FELLOWPRO/DocBits_Documentation/refs/heads/main/public_docs/.gitbook/assets/lsr-manage-layouts-toggle-en-20261102.png" alt="La sezione Manage Layouts nelle impostazioni aggiuntive di un tipo di documento, con il sottotitolo Enable Layout Management e l'interruttore Manage Layouts attivo."><figcaption><p>L'interruttore Manage Layouts nelle impostazioni aggiuntive di un tipo di documento</p></figcaption></figure>
<!-- English source image: lsr-manage-layouts-toggle-en-20261102.png -->

Il collegamento **Layouts** sulla scheda del tipo di documento ora apre **Layouts & Selection Rules**.

### Cosa succede quando si attiva

DocBits converte i layout esistenti basati sull'origine in regole — una sola volta, per questo tipo di documento e per ciascuna schermata:

* Il layout dell'origine **DEFAULT** diventa il **layout predefinito** (il fallback).
* Ogni layout di un'origine specifica diventa una regola **"Layout for XX"** con la condizione _Document Origin is XX_, che punta a quel layout. Queste regole ricevono priorità a passi di 10 (ad esempio 2000, 2010, 2020 …), così è possibile collocare le proprie regole prima, in mezzo o dopo di esse.

<figure><img src="https://raw.githubusercontent.com/FELLOWPRO/DocBits_Documentation/refs/heads/main/public_docs/.gitbook/assets/lsr-default-layout-row-en-20261102.png" alt="La fine dell'elenco delle regole di selezione: le ultime regole di origine Layout for UY e Layout for VN, seguite dalla riga FALLBACK Default layout contrassegnata is_default, usata quando nessuna regola sopra corrisponde."><figcaption><p>Le regole di origine create all'attivazione, seguite dal layout predefinito (FALLBACK)</p></figcaption></figure>
<!-- English source image: lsr-default-layout-row-en-20261102.png -->

Nei layout stessi non viene eliminato né modificato nulla. Subito dopo l'attivazione ogni documento riceve quindi esattamente il layout che riceveva prima. Il comportamento cambia solo quando si aggiungono o si modificano delle regole.

**Disattivando** la funzione, il tipo di documento torna subito alla selezione basata sull'origine. Le regole vengono conservate ma non utilizzate, e tornano a essere efficaci se si riattiva l'interruttore.

## La schermata Layouts & Selection Rules

<figure><img src="https://raw.githubusercontent.com/FELLOWPRO/DocBits_Documentation/refs/heads/main/public_docs/.gitbook/assets/lsr-layouts-overview-en-20261102.png" alt="La scheda Layouts di Layouts and Selection Rules per il tipo di documento INVOICE: le schede delle schermate Field Validation, Approval, Reject e Review, il filtro All, My layouts e System, il pulsante New layout e le schede dei layout con Edit, Clone e Delete."><figcaption><p>La scheda Layouts: ogni layout del tipo di documento come scheda</p></figcaption></figure>
<!-- English source image: lsr-layouts-overview-en-20261102.png -->

* **Layouts / Selection rules** (nell'intestazione della pagina) consentono di passare dall'elenco dei layout all'elenco delle regole. I numeri indicano quanti ce ne sono.
* **Field Validation / Approval / Reject / Review** cambiano la **schermata**. Ogni schermata ha i propri layout, le proprie regole e il proprio layout predefinito — una regola di approvazione non modifica mai la schermata di convalida.
* Nella scheda **Layouts** è possibile creare, modificare, clonare ed eliminare layout. Ogni scheda indica se una regola utilizza il layout ("Not targeted by rules" se nessuna lo fa). Filtra con **All / My layouts / System**; i layout di sistema sono forniti con DocBits e possono essere visualizzati e clonati, ma non modificati.

{% hint style="info" %}
La prima e la seconda approvazione condividono i layout e le regole **Approval**. Per assegnare alla seconda fase di approvazione una schermata propria, aggiungi una regola Approval con la condizione _Document Status is Pending second approval_ — vedi l'[esempio](layout-selection-rules.md#different-screens-for-first-and-second-approval).
{% endhint %}

## Come viene scelto un layout

Ogni volta che un documento viene aperto, e di nuovo dopo il salvataggio, DocBits decide il suo layout per la schermata corrente:

1. Le **regole attive** della schermata vengono verificate in ordine di **priorità** (prima il numero più basso). **Vince la prima regola la cui condizione è vera** e viene utilizzato il suo layout.
2. Se nessuna regola corrisponde, viene utilizzato il **layout predefinito**.
3. Se non esiste nemmeno un layout predefinito, DocBits ripiega sulla classica scelta basata sull'origine.

Le regole il cui layout è stato eliminato o è vuoto vengono saltate.

### Un esempio pratico

Regole della schermata **Field Validation**:

| Priorità | Regola                  | Condizione                                   | Layout                         |
| -------- | ----------------------- | -------------------------------------------- | ------------------------------ |
| 5        | Fatture Behaelterbau    | _Supplier ID is HP0000278_                   | Fattura con campi progetto     |
| 10       | Fatture elettroniche    | _Extraction Method is ELECTRONIC\_DOCUMENT_  | Fattura elettronica            |
| 2020     | Layout for DE           | _Document Origin is DE_                      | Field Validation Layout (DE)   |
| —        | Layout predefinito      | —                                            | Field Validation Layout (Base) |

Quale layout riceve ciascun documento:

| Documento | Fornitore  | Estrazione   | Origine | Layout                         | Perché                                                 |
| --------- | ---------- | ------------ | ------- | ------------------------------ | ------------------------------------------------------ |
| 1         | HP0000278  | fattura elettronica | DE      | Fattura con campi progetto     | la priorità 5 corrisponde per prima; le regole successive non vengono verificate |
| 2         | 10040      | fattura elettronica | DE      | Fattura elettronica            | la priorità 5 non corrisponde, la 10 sì                 |
| 3         | 10040      | PDF scansionato | DE      | Field Validation Layout (DE)   | corrisponde solo la regola di origine                   |
| 4         | 10040      | PDF scansionato | US      | Field Validation Layout (Base) | nessuna regola corrisponde → predefinito                |

**L'ordine conta**: colloca le regole specifiche (un solo fornitore) sopra quelle generali (un solo paese).

### Quando un utente modifica un campo che le regole considerano

Il layout viene sempre scelto in base ai valori **correnti** del documento. Se un utente corregge, ad esempio, il fornitore nella schermata di convalida, DocBits sceglie di nuovo il layout dopo il salvataggio e la schermata può passare a un altro layout. Nessun dato va perso: un campo che non fa parte del nuovo layout mantiene il proprio valore; semplicemente non viene mostrato finché non si applica di nuovo un layout che lo contiene.

## Gestire le regole di selezione

<figure><img src="https://raw.githubusercontent.com/FELLOWPRO/DocBits_Documentation/refs/heads/main/public_docs/.gitbook/assets/lsr-rules-list-en-20261102.png" alt="La scheda Selection rules della schermata Field Validation: una tabella con le colonne Priority, Rule e condizioni, Target layout, Source e Active, la prima riga contrassegnata FIRST, maniglie di trascinamento a sinistra e un menu a tre punti su ogni riga."><figcaption><p>La scheda Selection rules della schermata Field Validation</p></figcaption></figure>
<!-- English source image: lsr-rules-list-en-20261102.png -->

Ogni riga mostra la **priorità** (la prima riga è contrassegnata da **FIRST**), il **nome e la chiave della regola** con le sue **condizioni**, il **layout di destinazione**, il badge della **origine** e un interruttore **Active**.

| Attività             | Come                                                                               |
| -------------------- | ---------------------------------------------------------------------------------- |
| Creare una regola    | **New rule**                                                                       |
| Modificare una regola | Fai clic sulla riga                                                               |
| Cambiare l'ordine    | Trascina la maniglia a sinistra della riga verso l'alto o verso il basso. Il nuovo ordine viene salvato subito. |
| Disattivare una regola | Interruttore **Active**. Le regole inattive vengono ignorate.                     |
| Duplicare o eliminare | Menu **⋮** della riga                                                             |
| Cercare una regola   | **Search rules…**                                                                  |

Il badge dell'**origine** indica da dove proviene una regola: le regole **System** sono fornite con DocBits. Modificarne una crea una copia per la propria organizzazione, mostrata come **Customized**; l'originale resta intatta e può essere ripristinata. Le regole create dall'utente sono **Custom**.

### Il layout predefinito

L'ultima riga, contrassegnata da **FALLBACK** e **is\_default**, è il layout predefinito: viene utilizzato ogni volta che nessuna regola sopra corrisponde e non ha condizioni. Viene creato quando si attiva la funzione (a partire dal layout dell'origine DEFAULT).

{% hint style="info" %}
Per usare un altro layout di fallback, crea una regola **senza alcuna condizione** e assegnale il numero di priorità più alto, in modo che venga verificata per ultima. Corrisponde a ogni documento a cui non corrisponde nessuna regola precedente, prima di arrivare al layout predefinito.
{% endhint %}

## Creare una regola

Fai clic su **New rule** nella scheda Selection rules della schermata che desideri modificare.

<figure><img src="https://raw.githubusercontent.com/FELLOWPRO/DocBits_Documentation/refs/heads/main/public_docs/.gitbook/assets/lsr-rule-editor-en-20261104.png" alt="L'editor delle regole di selezione del layout per una fattura: la frase riassuntiva in alto, poi Step 1 Scope and priority con Rule name, Rule key, Document Type, Layout Type, Priority e una casella Log execution, Step 2 Applies when con la condizione Document Origin is AR e i pulsanti Add Condition e Add nested group, Step 3 Target layout con il layout Field Validation Layout (AR) selezionato, e il pannello di anteprima in tempo reale a destra con Sample document, matched_by, Resolved layout, Priority hit e watched_fields."><figcaption><p>L'editor delle regole: ambito e priorità, le condizioni, il layout di destinazione e l'anteprima in tempo reale di ciò che la regola farebbe.</p></figcaption></figure>
<!-- English source image: lsr-rule-editor-en-20261104.png -->

La frase in alto riassume la regola man mano che la costruisci — "When doc.doc_origin = AR, an INVOICE document gets the origin-ar layout for Field validation. Checked at priority 0 — the first matching rule wins."

### Step 1 — Scope & priority

| Impostazione                        | Cosa fa                                                                                                            |
| ----------------------------------- | ----------------------------------------------------------------------------------------------------------------- |
| **Rule Name**                       | Mostrato nell'elenco delle regole. Descrivi il caso aziendale: "Fatture Behaelterbau", "Fatture elettroniche", "Approvazione importi elevati". |
| **Rule key**                        | Generata dal nome; resta invariata se rinomini la regola.                                                          |
| **Document Type** / **Layout type** | Il tipo di documento e la schermata a cui si riferisce la regola. Ricavati dal punto in cui hai fatto clic su **New rule**. |
| **Priority**                        | I numeri più bassi vengono verificati per primi. Lascia degli intervalli (5, 10, 20 …) per poter inserire regole in seguito. |
| **Log execution**                   | Registra ogni valutazione della regola, così puoi ricostruire in seguito perché un documento ha corrisposto o no. Lasciala disattivata finché non ti serve questa traccia. |

### Step 2 — Applies when

La condizione che un documento deve soddisfare. Puoi usare:

* **attributi del documento**: Document Origin, Extraction Method, Document Status, Sub Document Type,
* **campi dell'intestazione**: Supplier ID, Total Amount, Currency, Purchase Order e ogni altro campo del tipo di documento,
* un **percorso JSON personalizzato** (Advanced).

Le colonne della tabella non sono disponibili: il layout viene scelto una sola volta per l'intero documento.

Lascia vuoto il passaggio per far corrispondere tutti i documenti a questa priorità. Il funzionamento delle condizioni — ALL / ANY, gruppi nidificati, tutti gli operatori, valori vuoti, maiuscole/minuscole — è spiegato in [Condizioni delle regole (Applies when)](../rule-conditions-applies-when.md).

### Step 3 — Target layout

Fai clic sul layout che il documento deve ricevere. L'elenco mostra i tuoi layout e i layout di sistema della schermata selezionata. Un layout non può essere eliminato finché una regola punta ancora ad esso.

### Anteprima in tempo reale · /resolve

Il pannello a destra mostra cosa fa la regola per un documento di esempio che ha i valori delle tue condizioni:

| Riga                | Significato                                                                                           |
| ------------------- | ----------------------------------------------------------------------------------------------------- |
| **Sample document** | I valori utilizzati per l'anteprima, ricavati dalle tue condizioni                                    |
| **matched\_by**     | `rule` se ha corrisposto una regola, altrimenti il layout predefinito                                 |
| **Resolved layout** | Il layout che riceverebbe il documento di esempio                                                     |
| **Priority hit**    | La priorità della regola che ha corrisposto                                                           |
| **watched\_fields** | I campi da cui dipende la scelta del layout. Quando un utente ne modifica uno, il layout viene scelto di nuovo. |

Fai clic su **Create Rule** (o **Save rule** in modifica) per salvare. **Cancel** riporta all'elenco delle regole.

## Esempi

### Campi aggiuntivi per un fornitore

Schermata **Field Validation** · priorità **5** · _Supplier ID is HP0000278_ · destinazione _Fattura con campi progetto_ (un clone del tuo layout standard con i campi aggiuntivi progetto e centro di costo).

### Un layout per più paesi

Schermata **Field Validation** · priorità **100** · **ANY of**: _Document Origin is Deutsch_, _Document Origin is Austria_, _Document Origin is Switzerland_ · destinazione _Fattura DACH_. Disattiva le regole migrate "Layout for AT" e "Layout for CH" se puntano a copie più vecchie.

### Una schermata più semplice per le fatture elettroniche

Schermata **Field Validation** · priorità **10** · _Extraction Method is ELECTRONIC\_DOCUMENT_ · destinazione _Fattura elettronica_ (senza i campi legati all'OCR).

### Una schermata di approvazione più rigorosa per importi elevati

Schermata **Approval** · priorità **10** · _Total Amount greater than 10000_ · destinazione _Approvazione importi elevati_ (con centro di costo, responsabile del budget e numero di contratto).

### Schermate diverse per la prima e la seconda approvazione

Schermata **Approval** · priorità **5** · _Document Status is Pending second approval_ · destinazione _Second Approval Layout_. I documenti nella prima fase di approvazione non corrispondono e ricevono il layout predefinito di Approval.

<figure><img src="https://raw.githubusercontent.com/FELLOWPRO/DocBits_Documentation/refs/heads/main/public_docs/.gitbook/assets/lsr-rule-editor-approval-en-20261104.png" alt="Una regola di selezione Approval nell'editor: Rule name Layout for DE, priorità 2000, le condizioni Document Status is Pending second approval e Document Origin is Deutsch, il layout di destinazione Second Approval Layout (DE) e l'anteprima in tempo reale che mostra il documento di esempio, matched_by rule, il layout risolto e priority hit 2000."><figcaption><p>Una regola Approval per la seconda fase di approvazione — l'anteprima in tempo reale a destra mostra già che questa regola vince con priorità 2000.</p></figcaption></figure>
<!-- English source image: lsr-rule-editor-approval-en-20261104.png -->

### Una schermata di rifiuto speciale per alcuni fornitori

Schermata **Reject** · priorità **10** · _Supplier ID is one of_ `10040, 10041` · destinazione _Rifiuto con codici motivo_.

## Buone pratiche

* **Prima le regole specifiche, poi quelle generali.** Regole per fornitore sopra le regole per paese, regole per paese sopra il layout predefinito.
* **Lascia intervalli di priorità** (5, 10, 20 …) in modo che le nuove regole si inseriscano senza rinumerare.
* **Basa le condizioni su campi affidabili.** Fornitore e origine vengono impostati presto e cambiano raramente. Le condizioni su campi che gli utenti modificano spesso fanno cambiare layout alla schermata mentre lavorano.
* **Clona, non ripartire da zero.** Clona il tuo layout standard e adattalo, così tutti i layout mantengono la stessa struttura di base.
* **Controlla l'anteprima in tempo reale** e apri un documento reale di ogni tipo dopo aver modificato le regole.
* **Mantieni un layout predefinito sensato** per ogni schermata, in modo che nessun documento resti senza layout.

## Risoluzione dei problemi

| Sintomo                                                        | Cosa controllare                                                                                                                      |
| -------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------ |
| Un documento riceve il layout sbagliato                        | Corrisponde prima una regola precedente. Esamina le regole sopra di essa, oppure la **Priority hit** nell'anteprima.                    |
| Viene usato il layout predefinito anche se una regola dovrebbe corrispondere | La regola è **Active**? La condizione corrisponde al valore esatto (maiuscole/minuscole, spazi)? La regola si trova nella scheda della **schermata** giusta? |
| Il layout cambia mentre un utente lavora                        | È stato modificato un campo in **watched\_fields**. Basa la regola su un campo più stabile.                                            |
| Un layout non può essere eliminato                             | Una regola punta ancora ad esso. Cambia prima la destinazione di quella regola o eliminala.                                            |
| Non viene mostrato alcun layout                                | Nessuna regola ha corrisposto, non esiste un layout predefinito e per questa schermata non esiste un layout basato sull'origine. Aggiungi una regola senza condizione come catch-all. |
| Dopo l'attivazione non è cambiato nulla                        | Comportamento previsto: l'attivazione riproduce la precedente scelta basata sull'origine. Aggiungi le tue regole.                      |
| La seconda approvazione mostra il layout della prima approvazione | Aggiungi una regola Approval su _Document Status is Pending second approval_ sopra le altre regole Approval.                        |

## Correlati

* [Condizioni delle regole (Applies when)](../rule-conditions-applies-when.md)
* [Regole di convalida personalizzate](../custom-validation-rules.md)
* [Regole di trasformazione](../transformation-rules/)
* [Navigare nel Layout Manager](navigating-the-layout-manager.md)
