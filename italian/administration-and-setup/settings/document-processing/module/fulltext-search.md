# Ricerca a testo completo

La ricerca a testo completo consente agli utenti di cercare nel contenuto effettivo dei documenti e in ogni campo estratto, non solo nei nomi dei file e negli ID.

<figure><img src="../../../../.gitbook/assets/fulltext-search-required-dialog.png" alt="Finestra di dialogo „Fulltext Module Required“ quando il modulo è disattivato"><figcaption><p>La finestra «Fulltext Module Required» compare nelle pagine che dipendono dal modulo.</p></figcaption></figure>

## Senza il modulo

Quando la ricerca a testo completo non è attiva, la barra di ricerca della dashboard può interrogare solo un piccolo insieme di campi strutturati. Il testo libero ripiega sul confronto con:

* `filename`
* `ID` del documento
* `invoice_id`
* `purchase_order`

Tutto ciò che non rientra in questi campi viene ignorato. Non esistono ricerca sul contenuto né supporto per intervalli, operatori o filtri intelligenti.

## Con il modulo attivo

L'attivazione della ricerca a testo completo abilita la ricerca su ogni campo estratto del documento e sostituisce la barra di ricerca della dashboard con un linguaggio di interrogazione esteso. Le query possono combinare filtri sui campi, intervalli, operatori logici, date relative e filtri intelligenti.

<figure><img src="../../../../.gitbook/assets/fulltext-search-dashboard-query.png" alt="Barra di ricerca della dashboard con una query per intervallo e l'elenco dei documenti filtrato"><figcaption><p>La barra di ricerca della dashboard accetta il linguaggio di interrogazione esteso. Digitare una query e premere <kbd>Invio</kbd> per filtrare l'elenco dei documenti.</p></figcaption></figure>

### Query mirate per campo

Per cercare su un singolo campo estratto, anteponi il nome del campo seguito da due punti. I nomi seguono la convenzione dell'API (minuscolo, snake\_case) e valgono per ogni campo catturato dai tipi di documento — fornitore, dati di fattura, righe, campi personalizzati.

```
supplier_name: Acme
invoice_id: INV-1234
status: ready_for_validation
```

### Query per intervallo

Gli operatori di confronto funzionano sui campi numerici e di data. Sono supportati sia i confronti aperti sia gli intervalli delimitati.

```
total_amount > 5000
total_amount <= 10000
invoice_due_date between 2026-01-01 and 2026-04-30
```

### Operatori logici

Combina le clausole con `AND`, `OR` e `NOT`, usando le parentesi per fissare la precedenza. Le liste `IN` confrontano un campo con un insieme di valori possibili.

```
supplier_name: Acme AND total_amount > 1000
(status: ready_for_validation OR status: validated) AND invoice_date: this_month
NOT status: archived
status IN (ready_for_validation, exported)
```

### Date relative

Espressioni temporali valutate al momento della query. Possono essere usate ovunque sia attesa una data.

```
imported_on: today()
invoice_date: last_week
imported_on: this_quarter
```

### Filtri intelligenti

Scorciatoie a singolo token per le query più comuni. Funzionano da sole o all'interno di un'espressione più ampia.

```
overdue
@User
#INV-1234
$5k+
```

* `overdue` — documenti la cui scadenza è passata.
* `@User` — filtra per assegnatario; sostituire `User` con il nome utente.
* `#INV-1234` — ricerca rapida per identificativo del documento.
* `$5k+` — importi superiori a 5.000 nella valuta del documento.

## Funzionalità derivate

Due modalità di ricerca specializzate si appoggiano al modulo di ricerca a testo completo. Entrambe richiedono che il modulo sia attivo e non possono essere usate in autonomia.

### Ricerca vettoriale

La ricerca vettoriale individua documenti semanticamente simili alla query, anziché basarsi sulla sola corrispondenza lessicale. La dashboard interpreta ogni query che inizia con `vector:` come ricerca vettoriale, la confronta con gli embedding dei documenti e ordina i risultati per somiglianza.

```
vector: frozen food invoices
```

L'indicizzazione vettoriale si gestisce separatamente dall'indice di testo dalla pagina **Impostazioni ricerca a testo completo**. Disattivandola non vengono più generati embedding per i nuovi documenti, ma l'indice di testo rimane attivo.

### Ricerca IA

La ricerca IA accetta query in linguaggio naturale e usa un LLM per estrarre filtri strutturati, eseguiti poi contro l'indice di testo completo. Anteporre `ai:` alla query.

```
ai: invoices from Ruiz over 1000 last quarter
```

Ricerca IA e ricerca vettoriale non sono intercambiabili: la vettoriale trova contenuti simili, la ricerca IA traduce il linguaggio in filtri. La ricerca IA non ha un interruttore dedicato — si appoggia agli indici esistenti, testo completo e vettoriale.

<figure><img src="../../../../.gitbook/assets/fulltext-search-settings-page.png" alt="Pagina „Impostazioni ricerca a testo completo“ con i sotto-indici Documents, Vector Index e Fulltext (Text)"><figcaption><p>Impostazioni ricerca a testo completo. L'indice vettoriale ha un proprio interruttore; l'indice di testo funziona finché il modulo è attivo.</p></figcaption></figure>

## Prerequisiti

* L'infrastruttura OpenSearch è attiva in background per alimentare l'indice.
* Alla prima attivazione tutti i documenti esistenti vengono reindicizzati. La durata dipende dal numero di documenti dell'organizzazione.
* Solo gli amministratori dell'organizzazione possono attivare o disattivare i moduli.

## Come attivare il modulo

1. Aprire **Impostazioni → Elaborazione documenti → Modulo**.
2. Nel gruppo **Dashboards**, attivare **Full text search**.
3. Confermare la finestra di sottoscrizione, se compare.
4. Attendere il completamento della prima reindicizzazione prima di affidarsi alle query a testo completo.

<figure><img src="../../../../.gitbook/assets/fulltext-search-module-toggle.png" alt="Pagina „Moduli“ con l'interruttore „Full text search“ sotto il gruppo Dashboards"><figcaption><p>L'interruttore <strong>Full text search</strong> si trova in <strong>Modulo → Dashboards &#x26; Analytics</strong>.</p></figcaption></figure>

{% hint style="info" %}
La tariffazione del modulo di ricerca a testo completo è gestita dal vostro contatto commerciale DocBits. La conferma dell'abbonamento appare alla prima attivazione del modulo.
{% endhint %}

## Vedi anche

* [Impostazioni ricerca a testo completo](../../log-settings/fulltext-search-settings.md) — gestione dell'indice e interruttore dell'indice vettoriale.
* [Funzioni Fulltext e Vector Search](../../global-settings/document-types/script/scripting-in-docbits/fulltext-search-functions.md) — API di scripting per `fulltext_search()` e `vector_search()`.
* [Panoramica dei moduli](README.md) — elenco completo dei moduli opzionali di DocBits.
