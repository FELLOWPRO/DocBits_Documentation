# Condizioni delle regole (Applies when)

## Panoramica

Ogni regola nelle funzioni di regole di DocBits ha una sezione **Applies when**. Essa decide **per quali documenti (e, per le regole di tabella, per quali righe) la regola fa effettivamente qualcosa**. Il compito vero e proprio della regola — generare un errore di convalida, modificare un valore, scegliere un layout — si verifica solo quando la condizione è vera.

Lo stesso costruttore di condizioni è usato in tutte e tre le funzioni di regole:

| Funzione | Etichetta nel costruttore | Quando la condizione è vera… | Quando è falsa… | Quando è lasciata vuota… |
| --- | --- | --- | --- | --- |
| [Regole di convalida personalizzate](custom-validation-rules.md) | Passaggio 2 **Applies when** | viene eseguito il controllo del passaggio 3 | la regola viene saltata — nessun errore, nessun avviso | il controllo viene eseguito su ogni documento |
| [Regole di trasformazione](transformation-rules.md) | Passaggio 2 **Quando corre** → **Solo quando…** | la pipeline modifica il valore | il valore resta com'è | scegliere **Always**: la regola viene eseguita su ogni documento |
| [Regole di selezione del layout](layout-manager/layout-selection-rules.md) | Passaggio 2 **Applies when** | il documento riceve il layout di questa regola (vince la prima corrispondenza) | DocBits prova la regola successiva | la regola corrisponde a ogni documento con la sua priorità |

Imparandolo qui una volta, è possibile usarlo ovunque.

{% hint style="info" %}
Una condizione decide soltanto **se** una regola si applica. Non modifica mai i dati e non mostra mai un messaggio da sola. "La partita IVA del fornitore deve essere compilata" è il **controllo** di una regola di convalida; "solo per le fatture tedesche" è la sua **condizione**.
{% endhint %}

## Leggere una condizione

Una condizione si legge come una frase. Il costruttore qui sotto dice:

> **Se TUTTE** le seguenti condizioni sono vere: la Document Origin **è** Deutsch, il Total Amount è **maggiore di** 250 e (**QUALSIASI** tra: la Currency **è** EUR, la Currency **è vuota**).

<figure><img src="../../../../.gitbook/assets/applies-when-nested-example.png" alt="Una condizione con due righe e un gruppo ANY nidificato"><figcaption><p>Due condizioni combinate con ALL, più un gruppo nidificato combinato con ANY</p></figcaption></figure>

Con questa condizione, la regola si applica a:

| Documento | Origine | Importo totale | Valuta | Si applica? | Motivo |
| --- | --- | --- | --- | --- | --- |
| A | DE | 469,18 | EUR | **sì** | tutte e tre le parti sono vere |
| B | DE | 469,18 | *(vuota)* | **sì** | il gruppo ANY è vero perché la valuta è vuota |
| C | DE | 120,00 | EUR | no | 120 non è maggiore di 250 |
| D | DE | 469,18 | USD | no | nessuna delle righe del gruppo ANY è vera |
| E | AT | 469,18 | EUR | no | l'origine non è DE |

## Gli elementi di base

### Righe di condizione

Ogni riga ha quattro parti:

| Parte | Cos'è |
| --- | --- |
| **Field** | Il valore che viene controllato: un attributo del documento, un campo dell'intestazione, una colonna della tabella o un percorso JSON. Vedere [Campi utilizzabili](#campi-utilizzabili). |
| **Operator** | Come viene confrontato il valore — *is*, *contains*, *greater than*, *is empty* … Vedere [Operatori](#operatori). |
| **Value** | Con cosa viene confrontato il campo. Nascosto per *is empty* / *is not empty*. Per i campi con un elenco fisso di valori (origine, stato, valuta…) il valore si sceglie da un menu a discesa. |
| **Aa** | Ignora maiuscole/minuscole. Disponibile solo per i confronti di testo. Quando è attivo, `gmbh` corrisponde a `GmbH`. |

Fare clic su **✕** per rimuovere una riga.

### ALL e ANY

Il selettore all'inizio di un gruppo decide come vengono combinate le sue righe:

* **Tutte** delle seguenti affermazioni sono vere — ogni riga deve essere vera (AND).
* **ANY** delle seguenti affermazioni sono vere — almeno una riga deve essere vera (OR).

### Gruppi nidificati

Fare clic su **+ Add nested group** per inserire un gruppo dentro un gruppo. Un gruppo nidificato conta come una riga del gruppo padre, quindi si possono mescolare AND e OR:

* *ALL of*: l'origine è DE, **ANY of** (la valuta è EUR, la valuta è vuota)
* *ANY of*: il fornitore è 10040, **ALL of** (il fornitore è 20723, l'importo totale è maggiore di 1000)

I gruppi possono essere nidificati a qualsiasi profondità. Mantenere la leggibilità: due livelli bastano per quasi ogni regola aziendale.

### Una condizione vuota

Se non si aggiunge alcuna riga, la regola non ha condizione e **si applica sempre** (per le regole di layout: corrisponde a ogni documento con la sua priorità). È la scelta giusta per le regole che devono essere eseguite ovunque, come "rimuovi gli spazi dal numero di fattura" o "la quantità deve essere positiva".

## Campi utilizzabili

Aprire il menu a discesa dei campi per vedere tutti i campi, raggruppati in base alla loro provenienza. Digitare per filtrare l'elenco.

<figure><img src="../../../../.gitbook/assets/applies-when-field-picker.png" alt="Il selettore dei campi con i gruppi Document e Header fields"><figcaption><p>Il selettore dei campi: prima gli attributi del documento, poi i campi dell'intestazione del tipo di documento</p></figcaption></figure>

### Attributi del documento (`doc.`)

Informazioni che DocBits conosce sul documento stesso, indipendentemente dai campi estratti:

| Campo nel selettore | Chiave | Valori di esempio | Uso tipico |
| --- | --- | --- | --- |
| **Document Origin** | `doc.doc_origin` | `DE`, `AT`, `US` (mostrati come Deutsch, Austria, Stati Uniti) | regole e layout specifici per paese |
| **Extraction Method** | `doc.extraction_method` | `ELECTRONIC_DOCUMENT`, `FELLOW_KV2`, `MANUAL` | trattare le fatture elettroniche (XRechnung, ZUGFeRD) in modo diverso dai PDF scansionati |
| **Document Status** | `doc.status` | Pronto per la convalida, In attesa di approvazione, In attesa di seconda approvazione... | layout per fase del workflow, regole che si applicano solo prima dell'approvazione |
| **Sub Document Type** | `doc.sub_doc_type` | i propri sottotipi, ad es. nota di credito | regole per un solo sottotipo |

### Campi dell'intestazione (`header.`)

Ogni campo del tipo di documento, ad esempio **Invoice Number** (`header.invoice_id`), **Supplier ID** (`header.supplier_id`), **Total Amount** (`header.total_amount`), **Currency** (`header.currency`), **Supplier Tax ID** (`header.supplier_tax_id`), **Purchase Order** (`header.purchase_order`). Il selettore mostra l'etichetta e, tra parentesi, la chiave tecnica. Il valore utilizzato è il valore corrente del campo — comprese le correzioni apportate da un utente.

### Colonne della tabella (`row.`)

Colonne della riga di tabella corrente, ad esempio `row.QUANTITY` o `row.ITEM_NUMBER`. Compaiono nel selettore come **Table columns** solo nelle regole che vengono eseguite **una volta per riga**:

* regole di convalida con il livello **Table line**
* regole di trasformazione con l'ambito **Table column**

In queste regole la condizione viene verificata **per ogni riga separatamente**. Una riga che non corrisponde viene saltata; le altre righe vengono comunque elaborate.

<figure><img src="../../../../.gitbook/assets/applies-when-row-condition.png" alt="Una condizione di riga: ITEM_NUMBER non è vuoto"><figcaption><p>Una condizione per riga: vengono controllate solo le righe che hanno un numero articolo</p></figcaption></figure>

Le regole eseguite una volta per documento (regole di intestazione, regole sull'intera tabella, regole di layout) non possono usare campi `row.` — non esiste una singola riga che potrebbero esaminare.

### Percorso JSON personalizzato (Advanced)

In fondo al selettore, **Advanced → Custom JSON path…** trasforma il campo in una casella di testo libera contrassegnata da `$path`. Legge un valore in qualsiasi punto dei dati estratti del documento, anche se non è un campo del tipo di documento.

<figure><img src="../../../../.gitbook/assets/applies-when-json-path.png" alt="Una condizione con percorso JSON"><figcaption><p>Una condizione con percorso JSON sul canale di importazione del documento</p></figcaption></figure>

* Il percorso inizia con `$` e usa `.nome` per le chiavi e `[0]` per le posizioni nelle liste, ad esempio `$.metadata.import_channel` o `$.shipping.addresses[0].country`.
* Deve terminare su un singolo valore. Un percorso che termina su una lista o su un oggetto conta come vuoto.
* Le righe con percorso JSON offrono gli operatori *is*, *is not*, *matches*, *is empty* e *is not empty*.

Usare i percorsi JSON con parsimonia. Dipendono dalla struttura interna dei dati estratti; un campo del tipo di documento è più facile da capire e da mantenere.

### Dove si può usare ciascun tipo di campo

| | Convalida: campo intestazione | Convalida: riga di tabella | Convalida: intera tabella | Trasformazione: intestazione / instradamento / righe di tabella | Trasformazione: colonna di tabella | Selezione del layout |
| --- | --- | --- | --- | --- | --- | --- |
| attributi del documento `doc.` | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
| campi dell'intestazione `header.` | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
| colonne della tabella `row.` | – | ✓ | – | – | ✓ | – |
| percorso JSON `$` | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |

## Operatori

<figure><img src="../../../../.gitbook/assets/applies-when-text-operators.png" alt="L'elenco degli operatori per un campo di testo"><figcaption><p>Gli operatori offerti per un campo di testo</p></figcaption></figure>

| Operatore | Vero quando… | Valore | Esempio |
| --- | --- | --- | --- |
| **is** | il campo è uguale al valore | un valore | Supplier ID **is** `20723` |
| **is not** | il campo non è uguale al valore | un valore | Currency **is not** `EUR` |
| **is one of** | il campo è uguale a uno qualsiasi dei valori di un elenco | valori separati da virgole | Supplier ID **is one of** `10040, 10041, 20723` |
| **contains** | il valore compare in un punto qualsiasi del campo | testo | Supplier Name **contains** `GmbH` |
| **starts with** | il campo inizia con il valore | testo | Invoice Number **starts with** `GS-` |
| **ends with** | il campo termina con il valore | testo | Purchase Order **ends with** `-IT` |
| **matches** | un'espressione regolare trova una corrispondenza nel campo | espressione regolare | Invoice Number **matches** `^INV-\d{6}$` |
| **is empty** | il campo non ha valore (mancante o con soli spazi) | – | Purchase Order **is empty** |
| **is not empty** | il campo ha un valore | – | Purchase Order **is not empty** |
| **greater than** / **less than** | il campo è un numero superiore / inferiore al valore | numero | Total Amount **greater than** `10000` |
| **maggiore o uguale** / **minore o uguale** | lo stesso, includendo il valore stesso | numero | Total Amount **less or equal** `250` |

### Quali operatori offre un campo

L'elenco si adatta al tipo del campo:

| Tipo di campo | Operatori |
| --- | --- |
| Testo | tutti gli operatori |
| Numero e importo (Total Amount, Quantity …) | è, non è, maggiore di, minore di, maggiore o uguale, minore o uguale, è vuoto, non è vuoto |
| Campi con elenco fisso (Document Origin, Status, Currency …) | è, non è, è uno di, è vuoto, non è vuoto |
| Data (Invoice Date, Due Date …) | è, non è, è vuoto, non è vuoto |
| Sì/No | è, non è, è vuoto, non è vuoto |
| Percorso JSON personalizzato | is, is not, matches, is empty, is not empty |

{% hint style="warning" %}
**In una condizione le date non possono essere confrontate con *before* o *after*.** "Data di scadenza successiva alla data della fattura" o "data della fattura più vecchia di 90 giorni" vanno nel **controllo** di una regola di convalida (**Compare fields**), non in *Applies when*.
{% endhint %}

## Come vengono confrontati i valori

Conoscere queste regole evita la maggior parte delle sorprese:

1. **I numeri vengono confrontati come numeri.** Se entrambi i lati sembrano numeri, `250`, `250.00` e `250,00` sono uguali. Gli importi formattati secondo le impostazioni locali, come `1.234,56`, vengono interpretati.
2. **Tutto il resto viene confrontato come testo, dopo aver rimosso gli spazi iniziali e finali.** `" EUR "` equivale a `EUR`.
3. **Maiuscole e minuscole contano**, a meno che **Aa** (ignora maiuscole/minuscole) non sia attivo.
4. **Il vuoto è speciale.** Un campo mancante o vuoto:
   * è vero per **is empty** e **is not**,
   * è falso per **is**, **is one of**, **contains**, **starts with**, **ends with**, **matches** e tutti i confronti numerici.

{% hint style="warning" %}
A causa della regola 4, *Currency **is not** EUR* è vera anche per i documenti **senza** valuta. Se non è quello che si desidera, aggiungere una seconda riga *Currency **is not empty***.
{% endhint %}

{% hint style="info" %}
A causa della regola 1, i valori che sembrano numeri vengono confrontati numericamente anche quando sono codici: `007` **is** `7` è vero. Per i codici in cui gli zeri iniziali contano, usare **matches** con un modello come `^007$`.
{% endhint %}

## Esempi

**Solo documenti tedeschi** — `Document Origin` **is** `Deutsch`.

**Solo fatture elettroniche** — `Extraction Method` **is** `ELECTRONIC_DOCUMENT`. Usare **is not** per escluderle, ad esempio per una regola che corregge gli errori dell'OCR.

**Un gruppo di fornitori** — `Supplier ID` **is one of** `10040, 10041, 20723`.

{% hint style="info" %}
Per i campi il cui valore si sceglie da un menu a discesa (origine, stato, valuta), **is one of** consente di scegliere una sola voce. Per accettarne diverse, creare un gruppo **ANY** con una riga **is** per ogni valore.
{% endhint %}

**Fatture di importo elevato di un fornitore** — **All of**: `Supplier ID` **is** `20723`, `Total Amount` **greater than** `10000`.

**Fatture senza ordine d'acquisto** — `Purchase Order` **is empty**. Una condizione tipica per una regola "centro di costo obbligatorio".

**Tutto tranne le note di credito** — `Invoice Type` **is not** `credit_note` (usare i valori che la propria organizzazione memorizza nel campo).

**Fatture arrivate via email** — Custom JSON path `$.metadata.import_channel` **is** `EMAIL`.

**Solo righe articolo** (regole su riga di tabella / colonna di tabella) — `row.ITEM_NUMBER` **is not empty**. Le righe di trasporto o di sconto senza numero articolo vengono saltate.

**Seconda fase di approvazione** (regole di layout nella schermata Approval) — `Document Status` **is** `Pending second approval`.

**UE o valuta mancante** — **All of**: `Document Origin` **is** `Deutsch`, **ANY of** (`Currency` **is** `EUR`, `Currency` **is empty**). È la condizione mostrata all'inizio di questa pagina.

## Testare ed eseguire il debug di una condizione

Ogni funzione consente di provare una condizione prima di farvi affidamento:

* **Regole di convalida** — **Test rule** esegue la regola su un documento reale. "*Rule skipped — scope not matched*" significa che la condizione era falsa per quel documento. Vedere [Test rule](custom-validation-rules.md#testare-la-regola).
* **Regole di trasformazione** — la **Live preview** ha **Condition values**: digitare un valore per ogni campo della condizione e vedere "*Conditions match — rule runs*" oppure "*Conditions do not match — rule is skipped*".
* **Regole di selezione del layout** — il pannello **Live preview · /resolve** mostra quale regola ha corrisposto per un documento di esempio.

### Leggere la traccia della condizione nei log

Attivare **Log execution** in una regola. Ogni valutazione viene allora scritta in **Document Types → (tipo di documento) → Logs**. Aprire una voce: sotto **Log details** ogni riga di condizione è elencata con il valore atteso dalla regola, il valore che il documento aveva effettivamente e se la riga è stata superata.

<figure><img src="../../../../.gitbook/assets/rule-execution-log-detail.png" alt="Una voce di log con la traccia della condizione"><figcaption><p>La voce di log spiega perché la regola è stata saltata: la regola si aspettava <code>abcd</code>, il documento aveva <code>911892112</code></p></figcaption></figure>

I log possono essere cercati per **Rule key**, **Rule ID** o **Document** e filtrati per tipo di regola, esito e data. Disattivare di nuovo **Log execution** al termine — scrive una voce per ogni valutazione e le regole vengono eseguite a ogni salvataggio.

## Errori comuni

| Sintomo | Causa | Soluzione |
| --- | --- | --- |
| La regola non si applica mai | Il valore differisce per maiuscole/minuscole o ortografia (`Gmbh` invece di `GmbH`) | Attivare **Aa**, oppure copiare il valore esattamente dal documento |
| La regola si applica a documenti senza il campo | **is not** è vero per i campi vuoti | Aggiungere *campo* **is not empty** |
| *greater than* non corrisponde mai | Il campo non è un numero, oppure è una data | Usare un campo numerico; confrontare le date in un controllo di convalida |
| La regola si applica a troppi documenti | Le righe sono state combinate con **ANY** invece di **All** | Controllare il selettore di ogni gruppo |
| Le colonne della tabella mancano nel selettore | La regola viene eseguita una volta per documento | Usare il livello **Table line** (convalida) o l'ambito **Table column** (trasformazione) |
| La condizione funzionava nell'anteprima ma non sul documento | L'anteprima usava valori digitati manualmente | Testare con **Test rule** su un documento reale, oppure controllare la traccia nei log |
