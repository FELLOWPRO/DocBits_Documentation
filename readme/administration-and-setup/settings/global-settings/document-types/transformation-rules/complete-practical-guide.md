# Regole di trasformazione: panoramica pratica completa

> Limite noto dell’anteprima (verificato il 29 ottobre 2026, versione 11.15.2): aggiungendo il prefisso `INV-`, l’anteprima modifica erroneamente `INV-4711` in `INV-INV-4711`. Il test indipendente del server mantiene `INV-4711`. Verifica anche l’esecuzione ripetuta con un test del server; un risultato corretto nell’anteprima, da solo, non dimostra l’esecuzione completa al salvataggio.

Data di verifica: 28 ottobre 2026. Gli esempi sono stati verificati con valori di addestramento sintetici su Dev NOVA. Un'anteprima non è prova di una modifica documentale salvata, di una riconciliazione ordine o di un'esportazione ERP.


## Etichette visibili nell’editor

Alcune etichette dell’interfaccia attuale presentano traduzioni imprecise. La tabella riporta il testo effettivamente visualizzato per trovare il passaggio corretto; le spiegazioni funzionali usano la terminologia tecnica. Le schermate mostrano l’interfaccia senza modifiche.

| Operazione | Etichetta visibile |
| --- | --- |
| case | Cambia maiuscole/minuscole |
| trim | Rimuovi gli spazi |
| pad | Pad |
| truncate | Troncare |
| affix | Prefisso/suffisso |
| sanitize | Pulisci |
| substring | Prendi una fetta |
| regex_extract | Estrarre |
| regex_replace | Trova e sostituisci |
| value_map | Valori della mappa |
| date_format | Data di riformattazione |
| number_format | Numero di formato |
| fix_value | Correggere |
| clear | Libero |
| clear_rows | Cancella tutte le righe |
| add_row | Aggiungi riga |


## Quattro ambiti di applicazione

| Ambito | Input e obiettivo | Compito tipico |
| --- | --- | --- |
| Campo di intestazione | Un campo per documento; la fonte può essere un altro campo di intestazione | Ripulire il numero di fattura, riprendere il numero d'ordine |
| Colonna tabella | La colonna selezionata per ogni riga della tabella selezionata | Uniformare codici articolo o codici unità |
| Righe tabella | Intera tabella | Rimuovere righe o aggiungere posizioni definite |
| Routing | Attributo documento `sub_org_id` | Assegnare una sotto-organizzazione esistente |

Gli ambiti si eseguono nell'ordine **Campo di intestazione → Routing → Righe tabella → Colonna tabella**. All'interno di un ambito, priorità e chiave di regola determinano la sequenza. I passaggi di una regola si eseguono dall'alto verso il basso. Una regola successiva può quindi leggere valori già modificati. L'ordine degli ambiti non viene invertito dalla priorità di una singola regola.

## Tutti i passaggi dell'editor

L'editor verificato offre 14 passaggi valore per intestazione/colonna, due passaggi per intere tabelle e un'assegnazione fissa nel Routing. `fix_value` e l'assegnazione fissa di Routing utilizzano entrambi lato server `set_value`. Inoltre l'interfaccia conosce `default`; questo passaggio non è offerto nel menu dei passaggi normali verificato.

| Passaggio | Varianti e parametri | Esempio | Limite e controprova |
| --- | --- | --- | --- |
| Modificare maiuscole/minuscole (`case`) | upper, lower, title, capitalize | `inv-4711` → `INV-4711` | Title: `acme gmbh` → `Acme Gmbh`; capitalize: `aCME GMBH` → `Acme gmbh`. Nomi propri/abbreviazioni possono cambiare in modo tecnicamente indesiderato. Per `capitalize` l'anteprima browser verificata lascia il resto invariato, mentre il server lo scrive in minuscolo; verificare il valore server separatamente. |
| Trim (`trim`) | entrambi / sinistra / destra; carattere vuoto = spazio | `  4711  ` → `4711` | `47 11` rimane conservato. Sinistra carattere `0`: `004711` → `4711`, ma `000` → vuoto. I caratteri sono un insieme, non un testo prefisso completo. |
| Riempimento (`pad`) | lunghezza minima, un carattere di riempimento, sinistra/destra | Lunghezza 10, sinistra `0`: `4711` → `0000004711` | Già 11 caratteri rimangono 11 caratteri. Destra `_`, lunghezza 6: `ABC` → `ABC___`. |
| Troncamento (`truncate`) | lunghezza massima | Lunghezza 10: `ABCDEFGHIJKL` → `ABCDEFGHIJ` | `ABC` rimane `ABC`. Il taglio perde informazioni e può far collassare numeri. |
| Affisso (`affix`) | aggiungere/rimuovere prefisso/suffisso | `INV-` + `4711` → `INV-4711` | Un affisso esatto esistente non viene aggiunto due volte. La rimozione agisce solo sul bordo corrispondente e rispetta le maiuscole. |
| Ripulire caratteri (`sanitize`) | mantenere alfanumerico / lettere / cifre / alfanumerico + spazi; oppure rimuovere classe di caratteri | `DE 123.456.789` → `DE123456789` | I segni possono essere semanticamente rilevanti. Durante la rimozione l'input è una classe di caratteri regex; proteggere correttamente il trattino, ad es. `.\-/`. |
| Sottostringa (`substring`) | inizio + lunghezza **oppure** inizio + fine; indici negativi possibili | Inizio 3, fine 7: `DE-4711-X` → `4711` | L'inizio conta da 0, la fine è esclusiva. Inizio −4: ultimi quattro caratteri. Necessaria fonte originale separata. |
| Estrazione (`regex_extract`) | espressione regolare, gruppo di cattura | `PO[- ]?(\d+)`, gruppo 1: `Order PO-45001234` → `45001234` | Prima corrispondenza; gruppo 0 = corrispondenza completa. Senza corrispondenza: vuoto. Necessaria fonte separata. |
| Cerca e sostituisci (`regex_replace`) | pattern, sostituto, numero | `\s+` → spazio: `ACME    GmbH` → `ACME GmbH` | Numero 0 = tutte, 1 = prima corrispondenza. Necessaria fonte separata. Verificare separatamente regex browser/server per pattern complessi. |
| Mappatura valori (`value_map`) | coppie complete da→a; ignorare maiuscole; sostituto senza corrispondenza | `stk` → `PCE` con `STK→PCE` e maiuscole ignorate | Sostituto vuoto significa **mantenere input**. `BOX` rimane `BOX`; un sostituto fisso `C62` sovrascriverebbe `BOX`. Il trim non avviene automaticamente. |
| Formattare data (`date_format`) | pattern di output, ad es. `%d.%m.%Y`, `%m/%d/%Y`, `%Y-%m-%d`, `%d %b %Y` | `2026-10-28` → `28.10.2026` nel target testo | Per campi intestazione DATE il valore salvato può rimanere ISO e solo la visualizzazione cambiare. Testo illeggibile rimane invariato; il test server indica il motivo. |
| Formattare numero (`number_format`) | de_DE / en_US / en_GB / fr_FR; min./max. cifre decimali | `1234.5` → `1234,50` oppure `1234.50` nel risultato server verificato | Nessun separatore delle migliaia nel risultato server verificato. Nessuna conversione di valuta o unità. Verificare separatamente arrotondamento e rielaborazione. |
| Valore fisso (`fix_value` nell'editor, `set_value` nell'API) | un valore fisso | `USD` → `EUR` | Sovrascrive anche valori esistenti. Non confondere con un valore predefinito. |
| Svuotare (`clear`) | nessun parametro | `Altwert` → `""` | Svuota il valore; non elimina né la definizione del campo né il documento. |
| Elimina tutte le righe (`clear_rows`) | solo righe tabella | 2 posizioni → 0 | Può invalidare riferimenti di riga e riconciliazione PO esistente. |
| Aggiungi riga (`add_row`) | inizio/fine; per colonna valore fisso o fonte intestazione | Quantità `1`, importo netto da `header.total_net_amount` | Senza eliminazione precedente solo con esecuzione una tantum appropriata. Nessuna aggregazione automatica delle posizioni esistenti. |
| Sotto-organizzazione fissa (`set_value`, Routing) | target esistente dalla selezione sotto-organizzazioni | Fornitore A → Sotto-organizzazione Nord | Nessun attributo di stato/utente/autorizzazione arbitrario. In alternativa assegnazione tramite `value_map` e fonte. |

### Valore predefinito tramite interfaccia

`default` aggiunge il suo valore solo in caso di input mancante/vuoto. Con predefinito `1`, `null` e `""` danno il valore `1`; `0` rimane `0`, `100` rimane `100`. Questo è verificato lato server. L'editor normale non ha per questo, nello stato verificato, un passaggio proprio. Il caso semplice funzionalmente corrispondente si può spesso rappresentare con **Target vuoto → Valore fisso**. Questa è una condizione di regola con assegnazione, non una voce di menu nascosta.

## Nove sequenze pratiche dettagliate

- [01 · Fondamenti, ambiti di applicazione e test sicuri](01-foundations.md)
- [02 · Pulizia testo: scrittura, trim e caratteri](02-text-cleaning.md)
- [03 · Modellare numeri: riempimento, troncamento, prefisso e suffisso](03-numbers-and-affixes.md)
- [04 · Sottostringhe e pattern: taglio, estrazione, sostituzione](04-substrings-and-patterns.md)
- [05 · Mappature valori e regole per riga tabella](05-value-mapping.md)
- [06 · Formattare correttamente date e numeri](06-dates-and-numbers.md)
- [07 · Riprendere campi, valori fissi, svuotare e valori predefiniti](07-field-copy-and-defaults.md)
- [08 · Ricostruire righe tabella](08-table-rows.md)
- [09 · Routing, sequenza, dati anagrafici e ripetizioni](09-routing-and-execution.md)

| Sequenza | Contenuto | Punto di verifica concreto |
| --- | --- | --- |
| 01 Fondamenti | Obiettivo, fonte, quattro ambiti, pipeline, condizioni, anteprima, salvataggio | Caso adatto, caso contrario, regola salvata riaperta |
| 02 Pulizia testo | Tutte e quattro le scritture, trim, tutte le modalità di ripulitura | Spazi interni, sequenza pura di zeri, caratteri semanticamente rilevanti |
| 03 Numeri | Riempimento, troncamento, tutte e quattro le varianti affisso | Numero troppo lungo, prefisso già presente, prefissi doppi |
| 04 Pattern | Sottostringa, indici negativi, estrazione/gruppi, sostituzione/numero | Fonte separata, nessuna corrispondenza, più corrispondenze |
| 05 Mappatura | Coppie, maiuscole, sostituto, applicazione per riga | `STK→PCE`, `BOX` sconosciuto, riapplicazione su `PCE` |
| 06 Formati | Data, DATE vs. testo, data illeggibile, formati numeri | Valore server effettivo invece della presunta visualizzazione browser |
| 07 Ripresa campo | Altra fonte, target vuoto, valore fisso, svuotare, valore predefinito API | Proteggere numero d'ordine corretto esistente; zero rimane zero |
| 08 Tabelle | Eliminare, aggiungere, valori colonna statici e dinamici | Sequenza, ripetizione, numero righe e riferimenti PO |
| 09 Interazione | Routing, fasi, lookup, esecuzione una tantum, protocolli | Fonte intestazione ripulita, condizione saltata, secondo salvataggio |

## Condizioni e fonti

Con "Sempre" la regola vale senza limitazione funzionale per il tipo documento. "Solo se…" la limita tramite condizioni. I valori di intestazione stanno nel contesto `header.*`, le caratteristiche documento in `doc.*`; `row.*` è disponibile solo nel contesto di riga di una regola colonna. Gruppi annidati E/O consentono criteri combinati. Per i singoli operatori vale la documentazione separata delle condizioni di regola.

**Esempio ripresa campo:** Target `purchase_order`, fonte `header.invoice_id`, condizione `header.purchase_order` è vuoto, passaggi Trim → Maiuscole. `  po-4711  ` dà `PO-4711`. Un numero d'ordine già correttamente compilato deve rimanere invariato. Non svuotare la fonte sbagliata: copiare con elaborazione non sposta la fonte.

**Esempio codice articolo:** Tabella `INVOICE_TABLE`, colonna `ITEM_NUMBER`, rimuovi prefisso `Art.-Nr. ` → mantieni alfanumerico → maiuscole. `Art.-Nr. ab-12/3` dà `AB123`. Adatto solo se il sistema target si aspetta esattamente questa forma.

**Esempio riga totale:** Per un fornitore chiaramente delimitato prima `clear_rows`, poi `add_row`; `POSITION=001`, `QUANTITY=1`, `NET_AMOUNT` dall'importo netto dell'intestazione. Se una riconciliazione ordine sulla somma totale sia funzionalmente corretta viene deciso dalla configurazione PO aggiuntiva e da un test di riconciliazione separato.

## Ripetizione ed esecuzione una tantum

Le regole possono essere eseguite in più cicli di elaborazione e al salvataggio. Verificare sempre **l'intera pipeline**, non solo la stabilità di un singolo passaggio.

* `substring`, `regex_extract` e `regex_replace` non possono nel contratto server verificato leggere il proprio valore di target. È richiesta una fonte separata; `run_once` non revoca questa prescrizione.
* Aggiungere un affisso esatto già esistente è stabile. Rimuovere un prefisso presente più volte può invece rimuovere ulteriormente ad ogni ciclo.
* `A→B` e `B→C` nella stessa mappatura valori possono con due cicli da `A` fare infine `C`. Testare gli output nuovamente come input.
* `clear_rows → add_row` ricostruisce una tabella in modo limitato. `add_row` senza eliminazione precedente richiede un'appropriata esecuzione una tantum, altrimenti la tabella cresce ad ogni salvataggio.
* "Solo una volta per documento" marca una regola effettivamente applicata. Condizioni non soddisfatte non consumano l'applicazione. Senza un documento/prova di applicazione leggibile affidabile, l'esecuzione di una regola una tantum viene rinviata.

## Dopo il lookup e prima della riconciliazione ordine

"Esegui anche dopo la ricerca dati anagrafici" aggiunge una fase dopo il popolamento lookup e prima della riconciliazione PO. Solo le regole corrispondentemente marcate vengono eseguite in questa fase aggiuntiva. Gli altri cicli rimangono. Combinato con esecuzione una tantum, la regola attende al primo ciclo di estrazione la fase successiva; se la fase lookup non avviene, un ciclo regolare successivo è possibile. La visualizzazione delle fasi dell'editor attuale mostra queste differenze.

## Un collaudo di accettazione affidabile

1. Definire obiettivo funzionale, formato sistema target e ambito di applicazione.
2. Preparare un valore grezzo adatto, un caso contrario, un valore vuoto e un risultato già elaborato.
3. Verificare condizioni e tutti i valori intermedi nell'anteprima.
4. Eseguire test lato server sullo stesso esempio; confrontare particolarmente pattern complessi e formati numeri/date.
5. Salvare la regola e riaprirla. Utilizzare una regola attiva solo nell'ambito di test previsto.
6. Salvare su un documento isolato, ricaricare e verificare valore e visualizzazione; per le tabelle anche numero righe e valori colonna.
7. Salvare ancora una volta. Il risultato non deve essere ulteriormente modificato o moltiplicato involontariamente.
8. Se funzionalmente richiesto, verificare anche riconciliazione PO e ricezione effettiva nel sistema target. Un protocollo di trasformazione da solo non prova questi risultati.

## Cosa una trasformazione non risolve automaticamente

Nessun nuovo riconoscimento OCR, nessuna conversione matematica di unità o valuta, nessuna aggregazione tabellare arbitraria e nessuna registrazione ERP completa. Il Routing è limitato all'attributo documento offerto. Disponibilità e visualizzazione esatta dipendono dalla versione impiegata, dal tipo documento e dalla configurazione organizzativa.

## Documento di esercitazione coerente

{% file src="../../../../../.gitbook/assets/transformation-training-invoice-it-20261028.pdf" %}
Scarica fattura di addestramento
{% endfile %}

Il documento fittizio contiene due posizioni, diverse grafie dell'unità e un riferimento d'ordine nel testo libero. Per test di regola riproducibili i valori di partenza sono preparati miratamente; questo non è prova di un'estrazione OCR automaticamente esente da errori.
