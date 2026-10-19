# Fellow kv table column rule

## Tabella `public.fellow_kv_table_column_rule`

### Colonne

* `id`: interno
* `docType`: interno
* `tableName`: interno
* `dlfName`: interno
* `multi_line`: boolean
* `filterID1`: interno
* `filterID2`: interno
* `filterID3`: interno
* `tfidf_doc_id`: interno
* `tfidf_id`: interno
* `valuePattern`: interno
* `coordsY0`: integer
* `coordsY1`: integer
* `coordsX0`: integer
* `coordsX1`: integer
* `normalizedY0`: numeric
* `normalizedY1`: numeric
* `normalizedX0`: numeric
* `normalizedX1`: numeric
* `width`: integer
* `height`: integer
* `patternLeft`: interno
* `patternRight`: interno
* `patternAbove`: interno
* `patternBelow`: interno
* `wordLeft`: interno
* `wordAbove`: interno
* `ruleWeight`: integer
* `user_id`: integer
* `org_id`: ID dell'organizzazione
* `created_on`: timestamp with time zone
* `last_modified_on`: timestamp with time zone
* `is_deleted`: boolean
* `is_new`: boolean

### Analisi e descrizione

## Documentazione tecnica della tabella `public.fellow_kv_table_column_rule`

### Introduzione

La tabella `public.fellow_kv_table_column_rule` è progettata per memorizzare regole e pattern per l'elaborazione o l'estrazione di dati dai documenti. Lo si deduce dalla presenza di campi come `docType`, `tableName`, `dlfName` e di vari campi relativi a pattern e coordinate. La tabella sembra facilitare l'applicazione di regole a diversi tipi di documento, consentendo il riconoscimento di pattern e l'estrazione di dati da documenti strutturati come fatture o contratti.

### Descrizione delle colonne

#### id

* **Significato**: identificatore univoco di ogni regola.
* **Ruolo**: chiave primaria.
* **Contenuto tipico**: stringhe UUID.
* **Nota**: essenziale per identificare in modo univoco ogni riga.

#### docType

* **Significato**: tipo di documento a cui si applica la regola.
* **Ruolo**: campo descrittivo.
* **Contenuto tipico**: tipi di documento come 'INVOICE', 'CONTRACT'.
* **Nota**: aiuta a categorizzare le regole per tipo di documento.

#### tableName

* **Significato**: nome della tabella in cui viene applicata la regola.
* **Ruolo**: campo descrittivo.
* **Contenuto tipico**: nomi di tabella come 'INVOICE\_TABLE'.
* **Nota**: indica il contesto in cui viene applicata la regola.

#### dlfName

* **Significato**: nome del campo o della colonna specifici nel documento.
* **Ruolo**: campo descrittivo.
* **Contenuto tipico**: nomi di campo come 'COUNTRY\_ORIGIN'.
* **Nota**: specifica il campo di destinazione per l'estrazione dei dati.

#### multi\_line

* **Significato**: indica se la regola si applica a testo su più righe.
* **Ruolo**: flag booleano.
* **Contenuto tipico**: `True` o `False`.
* **Nota**: utile per gestire i campi di testo su più righe.

#### filterID1, filterID2, filterID3

* **Significato**: filtri o condizioni per l'applicazione della regola.
* **Ruolo**: campi descrittivi o condizionali.
* **Contenuto tipico**: eventualmente stringhe che rappresentano condizioni di filtro.
* **Nota**: utilizzati per affinare l'applicazione della regola in base a determinate condizioni.

#### tfidf\_doc\_id, tfidf\_id

* **Significato**: identificatori relativi all'elaborazione TF-IDF.
* **Ruolo**: ruoli o identificatori simili a chiavi esterne.
* **Contenuto tipico**: stringhe UUID.
* **Nota**: probabilmente legati all'analisi del testo e all'estrazione di caratteristiche.

#### valuePattern

* **Significato**: pattern regex per l'estrazione del valore.
* **Ruolo**: campo pattern.
* **Contenuto tipico**: espressioni regolari.
* **Nota**: definisce il pattern utilizzato per identificare ed estrarre i valori.

#### coordsY0, coordsY1, coordsX0, coordsX1

* **Significato**: coordinate che definiscono il riquadro di delimitazione per l'estrazione.
* **Ruolo**: campi di coordinate.
* **Contenuto tipico**: numeri interi che rappresentano posizioni in pixel.
* **Nota**: definiscono l'area di interesse in un documento per l'estrazione dei dati.

#### normalizedY0, normalizedY1, normalizedX0, normalizedX1

* **Significato**: coordinate normalizzate per l'estrazione.
* **Ruolo**: campi di coordinate.
* **Contenuto tipico**: valori numerici che rappresentano posizioni proporzionali.
* **Nota**: utilizzate per definire aree indipendenti dalla risoluzione.

#### width, height

* **Significato**: dimensioni dell'area definita dalle coordinate.
* **Ruolo**: campi dimensionali.
* **Contenuto tipico**: valori interi.
* **Nota**: aiutano a definire la dimensione dell'area di estrazione.

#### patternLeft, patternRight, patternAbove, patternBelow

* **Significato**: pattern contestuali che circondano i dati di destinazione.
* **Ruolo**: campi pattern.
* **Contenuto tipico**: espressioni regolari.
* **Nota**: forniscono il contesto per capire dove si trovano i dati rispetto al resto del testo.

#### wordLeft, wordAbove

* **Significato**: parole specifiche situate vicino ai dati di destinazione.
* **Ruolo**: campi contestuali.
* **Contenuto tipico**: parole o frasi specifiche.
* **Nota**: aiutano ad affinare la ricerca dei dati di destinazione in base alle parole vicine.

#### ruleWeight

* **Significato**: importanza o priorità della regola.
* **Ruolo**: campo di peso o priorità.
* **Contenuto tipico**: valori interi.
* **Nota**: valori più alti possono indicare una priorità o un'importanza maggiore.

#### user\_id

* **Significato**: identificatore dell'utente che ha creato o modificato la regola.
* **Ruolo**: chiave esterna.
* **Contenuto tipico**: valori interi.
* **Nota**: collega la regola a un utente specifico.

#### org\_id

* **Significato**: identificatore dell'organizzazione associata alla regola.
* **Ruolo**: chiave esterna.
* **Contenuto tipico**: stringhe UUID.
* **Nota**: associa la regola a un'organizzazione.

#### created\_on

* **Significato**: timestamp di creazione della regola.
* **Ruolo**: campo tecnico.
* **Contenuto tipico**: timestamp con fuso orario.
* **Nota**: utile per tracciare la cronologia di creazione della regola.

#### last\_modified\_on

* **Significato**: timestamp dell'ultima modifica della regola.
* **Ruolo**: campo tecnico.
* **Contenuto tipico**: timestamp con fuso orario oppure `None`.
* **Nota**: traccia le modifiche alla regola nel tempo.

#### is\_deleted

* **Significato**: indica se la regola è contrassegnata come eliminata.
* **Ruolo**: flag booleano.
* **Contenuto tipico**: `True` o `False`.
* **Nota**: utilizzato per l'eliminazione logica delle regole.

#### is\_new

* **Significato**: indica se la regola è stata creata di recente.
* **Ruolo**: flag booleano.
* **Contenuto tipico**: `True` o `False`.
* **Nota**: aiuta a identificare le regole aggiunte di recente.
