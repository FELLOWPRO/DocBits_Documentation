# Regole di Trasformazione

## Panoramica

Le regole di trasformazione puliscono o riscrivono i dati estratti **automaticamente** — un campo nell’intestazione, una colonna in una tabella, intere righe di tabella o un attributo del documento — ogni volta che un documento viene elaborato e ogni volta che viene salvato. Sostituiscono i piccoli script che molte organizzazioni usavano scrivere per "taglia sempre questo campo", "imposta di default questa colonna a 1", "mappa i codici unità di questo fornitore" o "raggruppa le righe degli articoli di questo fornitore in una riga totale".

Una regola è definita per **tipo di documento** e viene eseguita su ogni documento di quel tipo. Le regole vengono eseguite **prima** della validazione, degli script e del matching degli ordini di acquisto, quindi tutto ciò che segue vede già i valori trasformati.

## Come accedere

1. Naviga su **Impostazioni → Impostazioni Globali → Tipi di Documento**.
2. Apri il tipo di documento e scegli **Regole di Trasformazione**. La lista mostra ogni regola del tipo con il suo ambito, obiettivo, priorità e se è attiva.
3. Clicca su **Nuova regola** per aprire il generatore di regole, oppure apri una regola esistente per modificarla.

## Anatomia di una regola

| Parte                   | Cos’è                                                                                                                                                                                                                                                    |
| ----------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Nome / chiave**       | Il nome visualizzato mostrato nelle liste, nei messaggi e nella cronologia del matching, e una chiave tecnica che rimane stabile anche se rinomini la regola.                                                                                            |
| **Ambito**              | Dove la regola scrive: un **campo intestazione**, una **colonna tabella**, una **tabella** (intere righe) o un **attributo del documento**. Vedi sotto.                                                                                                  |
| **Obiettivo**           | Il campo, la colonna (con la sua tabella) o la tabella su cui la regola scrive.                                                                                                                                                                          |
| **Fonte**               | Opzionale. Da dove la regola legge il suo input invece che dall’obiettivo stesso: `header.<field>` per un campo intestazione, `doc.<attribute>` per un attributo documento, `row.<column>` per un’altra colonna della stessa riga (solo ambito colonna). |
| **Quando**              | **Sempre**, oppure **solo quando** una condizione è vera (vedi Condizioni).                                                                                                                                                                              |
| **Azioni**              | La lista delle trasformazioni, applicate in ordine; l’output di un’azione è l’input della successiva.                                                                                                                                                    |
| **Priorità**            | Le regole dello stesso ambito vengono eseguite in ordine di priorità crescente (poi per chiave). Usala quando una regola deve vedere il risultato di un’altra.                                                                                           |
| **Esegui una volta**    | La regola si applica a un documento **al massimo una volta**. Necessario per azioni che cambierebbero il valore ad ogni salvataggio (substring, regex\_replace, regex\_extract) e per regole di tabella che non devono ricostruire le righe più volte.   |
| **Registra esecuzione** | Scrive una riga di log per ogni applicazione — utile mentre si affina una nuova regola.                                                                                                                                                                  |

### Ambiti

| Ambito                  | Scrive su                                                               | Regola tipica                                                                               |
| ----------------------- | ----------------------------------------------------------------------- | ------------------------------------------------------------------------------------------- |
| **Campo intestazione**  | un campo intestazione estratto (numero fattura, valuta, …)              | taglia e trasforma in maiuscolo il numero fattura; mappa "EUR€" in "EUR"                    |
| **Colonna tabella**     | una colonna in ogni riga di una tabella                                 | imposta di default `UNIT_PRICE_PER` a 1; rimuove il prefisso "Art.-Nr." dal numero articolo |
| **Tabella**             | le righe di una tabella                                                 | cancella le righe e aggiunge una riga totale per un fornitore che è abbinato sul totale     |
| **Attributo documento** | un attributo del documento stesso (attualmente la sotto-organizzazione) | indirizza i documenti di un fornitore a una sotto-organizzazione                            |

Le regole vengono eseguite ambito per ambito in questo ordine: intestazione → documento → tabella → colonna. Una regola di colonna vede quindi già le righe che una regola di tabella ha aggiunto.

### Condizioni ("solo quando")

Una condizione confronta un valore del documento con una costante. Il valore proviene da un campo intestazione (`header.<field>`), un attributo documento (`doc.<attribute>`) o, per regole di colonna, una colonna della riga corrente (`row.<column>`).

| Operatore                                  | Significato          |
| ------------------------------------------ | -------------------- |
| is / is not                                | confronto esatto     |
| is one of / is not one of                  | valore in una lista  |
| contains, starts with, ends with           | confronto testuale   |
| is empty / is not empty                    | non serve valore     |
| greater than, less than, at least, at most | confronto numerico   |
| matches                                    | espressione regolare |

Le condizioni possono essere raggruppate con **all of** (e) e **any of** (o) e negate con **not**. Esempio: _solo quando `header.supplier_id` è `20723`_ — la regola si esegue solo per un fornitore.

### Azioni

Azioni per campi intestazione e colonne tabella (formano una pipeline; il valore entra dall’alto e esce dal basso):

| Azione          | Effetto                                                                                                                         |
| --------------- | ------------------------------------------------------------------------------------------------------------------------------- |
| `trim`          | rimuove spazi bianchi (o caratteri specificati) a sinistra, destra o entrambi i lati                                            |
| `case`          | maiuscolo, minuscolo, titolo o capitalizza                                                                                      |
| `pad`           | riempie fino a una lunghezza con un carattere, a sinistra o a destra                                                            |
| `truncate`      | taglia a una lunghezza massima                                                                                                  |
| `affix`         | aggiunge un prefisso o suffisso, oppure lo rimuove                                                                              |
| `sanitize`      | mantiene solo una classe di caratteri (alfanumerici, alfabetici, numerici, alfanumerici + spazio) o rimuove un set di caratteri |
| `substring`     | prende una parte del valore tramite inizio e lunghezza o fine                                                                   |
| `regex_replace` | sostituisce ciò che corrisponde a un’espressione regolare                                                                       |
| `regex_extract` | mantiene ciò che cattura un’espressione regolare                                                                                |
| `value_map`     | mappa valori in altri valori (opzionalmente case-insensitive, con un default)                                                   |
| `date_format`   | riformatta una data (l’input deve essere la data ISO che DocBits memorizza in `value`)                                          |
| `number_format` | riformatta un numero                                                                                                            |
| `default`       | imposta un valore solo quando il campo è vuoto                                                                                  |
| `set_value`     | imposta un valore fisso, qualunque fosse il contenuto del campo                                                                 |
| `clear`         | svuota il campo                                                                                                                 |

Azioni per ambito **tabella** (agiscono sulle righe, non sui valori, e non possono essere miscelate con le azioni sopra):

| Azione       | Effetto                                                                                                                                                                  |
| ------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| `clear_rows` | elimina ogni riga della tabella                                                                                                                                          |
| `add_row`    | aggiunge una riga alla fine o all’inizio; ogni colonna riceve un valore fisso o un valore letto dall’intestazione (`header.<field>`) o dal documento (`doc.<attribute>`) |

{% hint style="info" %}
`substring`, `regex_replace` e `regex_extract` modificano nuovamente un valore se eseguiti su un valore già trasformato. Combinali con **Esegui una volta**, oppure scrivi l’espressione regolare in modo che una seconda esecuzione non abbia più nulla da modificare.
{% endhint %}

## Quando vengono eseguite le regole

* Durante l’elaborazione, dopo l’estrazione e prima della validazione, degli script e del matching degli ordini di acquisto.
* Ad **ogni salvataggio** del documento in cui i dati estratti sono cambiati. Le regole senza **Esegui una volta** vengono applicate di nuovo a ogni salvataggio; poiché ogni azione eccetto le tre sopra è idempotente, un valore già nella forma obiettivo resta invariato.

## Regole di trasformazione e matching degli ordini di acquisto

Le regole di tabella e di colonna modificano ciò che il matcher degli ordini di acquisto vede:

* Una regola di tabella che **ricostruisce** le righe (per esempio cancella tutte le righe e aggiunge una riga totale) mantiene un abbinamento ordine di acquisto esistente finché produce **le stesse righe di nuovo** — i valori sono confrontati per significato, quindi `1.0` e `1.00` sono la stessa riga. Le righe mantengono la loro identità e l’abbinamento sopravvive a ogni salvataggio.
* Se una regola **sostituisce o rimuove righe già abbinate**, l’abbinamento non può essere mantenuto. Il documento registra quale regola lo ha eliminato, la schermata di Purchase Order Matching mostra questo come motivo ("_L’abbinamento PO non è stato salvato: la regola di trasformazione "…" ha ricostruito la tabella_") e gli amministratori ricevono un link alla regola. La **cronologia del matching** del documento mostra un passaggio _Regole di trasformazione_ prima della prima fase di matching con le regole eseguite.
* Il numero di righe dopo le regole è ciò che contano le [condizioni di attivazione](https://github.com/Fellow-Consulting-AG/docbits/tree/it/readme/administration-and-setup/settings/global-settings/document-types/more-settings/purchase-order/purchase-order-matching-rules.md#activation-conditions) delle regole di matching. Una regola che raggruppa una fattura in **una** riga ha senso solo insieme a una regola match sul totale attiva per documenti a riga singola (`[[count(table_lines)]] >= 1`).

## Esempi

**Pulisci il numero fattura** — campo intestazione `invoice_id`, sempre: `trim` → `case` maiuscolo.

**Imposta di default la base prezzo** — colonna tabella `UNIT_PRICE_PER` della tabella righe, sempre: `default` `1`.

**Mappa i codici unità di un fornitore** — colonna tabella `UNIT` della tabella righe, solo quando `header.supplier_id` è `10040`: `value_map` `{ "STK": "PCE", "KG": "KGM" }`.

**Una riga totale per un fornitore abbinato sul totale** — ambito tabella sulla tabella righe, solo quando `header.supplier_id` è `20723`: `clear_rows`, poi `add_row` con `POSITION` = `001`, `UNIT_PRICE` = `1.0`, `QUANTITY` = `header.total_net_amount`, `NET_AMOUNT` = `header.total_net_amount`. Abbinala a una regola match sul totale la cui condizione di attivazione accetta documenti a riga singola.

**Indirizza un fornitore a una sotto-organizzazione** — attributo documento `sub_org_id`, solo quando `header.supplier_id` è uno di `[…]`: `set_value` `<id sotto-organizzazione>`.

## Risoluzione dei problemi

| Sintomo                                                         | Cosa controllare                                                                                                                                                                                |
| --------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| La regola non ha cambiato nulla                                 | È attiva? Il tipo di documento corrisponde? La condizione è vera per questo documento (confronta il valore esatto, spazi inclusi)? Una regola con **Esegui una volta** è già stata applicata?   |
| Il valore cambia di nuovo a ogni salvataggio                    | La pipeline contiene `substring`, `regex_replace` o `regex_extract`. Attiva **Esegui una volta** o rendi l’espressione idempotente.                                                             |
| L’abbinamento ordine di acquisto si perde dopo il salvataggio   | Una regola di tabella ha sostituito le righe abbinate. Il motivo nel documento indica la regola; fai in modo che la regola riproduca le stesse righe, oppure impostala su **Esegui una volta**. |
| Una regola di matching non si esegue mai dopo la trasformazione | La regola ha cambiato il numero di righe; aggiusta la condizione di attivazione della regola di matching.                                                                                       |
