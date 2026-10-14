# Regole di Corrispondenza degli Ordini di Acquisto

## Introduzione: Ordini di Acquisto e Gestione delle Regole PO

La corrispondenza degli Ordini di Acquisto (PO) è un processo critico per garantire la coerenza tra gli Ordini di Acquisto (PO) e le corrispondenti fatture in entrata o ricevute di merci. Un insieme solido di regole è essenziale per ottenere un alto tasso di corrispondenza automatica, prevenire frodi e garantire pagamenti corretti.

Questa pagina di configurazione viene utilizzata per definire e gestire le regole che determinano _come_ le righe dell’ordine di acquisto vengono abbinate al documento in entrata corrispondente (Fattura, Conferma d’Ordine).

{% hint style="info" %}
**Prerequisito:** le regole di corrispondenza sono utilizzate solo quando **PO match server side** è attivato per il tipo di documento (Impostazioni → Tipi di Documento → Altre Impostazioni → Ordine di Acquisto). Con l’interruttore disattivato, DocBits esegue la corrispondenza con il suo matcher integrato (quantità, prezzo unitario, numero articolo, numero ordine di acquisto) e ignora il set di regole.
{% endhint %}

***

## Come Accedere

1.  Navigare su **Impostazioni --> Impostazioni Globali --> Tipi di Documento**

    <figure><img src="../../../../../../.gitbook/assets/image (31).png" alt=""><figcaption></figcaption></figure>


2.  Selezionare il tipo di documento desiderato e cliccare su **Altre Impostazioni**.

    <figure><img src="../../../../../../.gitbook/assets/image (40).png" alt=""><figcaption></figcaption></figure>


3.  Poi andare alla sezione Ordine di Acquisto e cliccare il pulsante (PO match server side), dopo di che cliccare su Configura Regole di Corrispondenza PO

    <figure><img src="../../../../../../.gitbook/assets/image (168).png" alt=""><figcaption></figcaption></figure>

***

<figure><img src="../../../../../../.gitbook/assets/Bildschirmfoto 2025-12-09 um 07.43.15.png" alt=""><figcaption></figcaption></figure>

## Impostazioni Globali (Regole Base)

Queste impostazioni stabiliscono il quadro che si applica a tutte le regole di corrispondenza:

* **Impostazione:** Match Quantity On
  * **Scopo:** Definisce quale quantità della riga dell’ordine di acquisto viene confrontata con la riga del documento — ad esempio la quantità ordinata o la **quantità aperta della fattura** (ordinata meno già fatturata), che è la scelta usuale per le fatture.
  * **Valori Valid:** Quantità o altri campi quantità disponibili nel sistema, a seconda della struttura dati (es. un campo quantità normalizzato alternativo).
  * **Dipendenza:** Determina la base per tutte le regole di corrispondenza che includono la quantità nei criteri di confronto.
* **Impostazione:** Tolleranza Standard (Tolleranza Predefinita)
  * **Scopo:** Definisce quanto un valore numerico sul documento può discostarsi dal valore dell’ordine di acquisto e comunque essere considerato una corrispondenza. Compensa le differenze di arrotondamento. Si applica a **ogni colonna numerica** con l’opzione "Consenti Tolleranza" abilitata — quantità così come prezzo unitario.
  * **Valore Valido:** Un numero decimale. Se viene interpretato come un **valore assoluto** (0.005 = una deviazione fino a 0.005 nella quantità o prezzo confrontati) o come una **percentuale** (0.5 = 0.5 % del valore confrontato) è impostato dal **tipo di tolleranza** del set di regole (`value` o `percent`; i nuovi set di regole usano `value`). Le tolleranze per singolo articolo (vedi [Impostazioni di Tolleranza](purchase-order-tolerance-settings-additional-purchase-order-tolerance.md)) sovrascrivono la tolleranza standard per quell’articolo.
  * **Dipendenza:** Si applica alle regole che utilizzano campi numerici per la corrispondenza e hanno l’opzione "Consenti Tolleranza" abilitata.

***

## Elenco Regole

L’Elenco Regole mostra tutte le regole di corrispondenza disponibili e gestisce il loro ordine di esecuzione.

#### Struttura ed Esecuzione

* **Priorità:** Questo campo numerico (es. 1, 2, 3) determina la sequenza di esecuzione delle regole. Le regole con un numero di priorità più basso vengono tentate per prime. Questo permette agli amministratori di strutturare una gerarchia, tipicamente iniziando con le regole più specifiche e rigorose (es. corrispondenza sia per numero riga che per numero articolo) e passando a regole più ampie o meno restrittive.
* **Nome & Descrizione:** Fornisce un’identificazione chiara e il contesto della regola, spiegando i criteri principali utilizzati (es. "Regola Standard N. 1: Corrispondenza basata su Numero Riga, ID Articolo e Quantità").
* **Attiva:** Un semplice interruttore che consente di attivare o disattivare immediatamente la regola senza dover eliminare la sua configurazione.

**Flusso di Esecuzione:** Il sistema esegue la corrispondenza in sequenza a cascata. Se una regola (es. Priorità 1) corrisponde con successo a una riga, il processo per quella riga si interrompe. Se non viene trovata corrispondenza, il sistema procede alla regola successiva nella sequenza di priorità (es. Priorità 2). Ogni esecuzione è registrata sul documento; la **cronologia delle corrispondenze** nella schermata di Corrispondenza Ordine di Acquisto mostra quale regola è stata tentata, quale ha corrisposto e quali sono state saltate e perché.

***

## Configurazione Regola (Impostazioni Dettagliate)

Quest’area di configurazione dettagliata definisce la logica specifica e i criteri per una singola regola.

#### Parametri Base

* **Tipo di Regola:** Specifica la cardinalità della corrispondenza.

| Tipo di regola       | Cosa fa                                                                                                                                                                                                | Uso tipico                                                                     |
| -------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------ |
| **Single match**     | Una riga dell’ordine di acquisto a una riga del documento. Ogni colonna configurata deve corrispondere (entro la tolleranza dove consentito).                                                          | Il caso standard.                                                              |
| **Multi match**      | Diverse righe dell’ordine di acquisto a una riga del documento, o diverse righe del documento a una riga dell’ordine di acquisto. Le quantità sono **sommate**, il prezzo unitario è confrontato come **media**, le altre colonne devono corrispondere. | Consegne frazionate, una riga fattura che copre diverse righe d’ordine.        |
| **Match on total**   | Confronta un **importo** — di solito l’importo netto della riga del documento contro il **totale** dell’ordine di acquisto — e corrisponde all’intero ordine di acquisto in una volta sola.               | Fornitori che fatturano un importo forfettario, fatture di servizi, fatture a riga singola. |

* **Corrispondenza Automatica:** Se abilitato, il sistema tenterà di applicare questa regola interamente in modo automatico. È richiesta alta affidabilità nei criteri per il processo automatico.
* **Corrispondenza Manuale:** Se abilitato, questa regola può essere presentata o applicata da un utente durante la fase di riconciliazione manuale, offrendo un set predefinito di criteri di confronto per risolvere le eccezioni.
* **Fallback:** Una regola contrassegnata come fallback viene eseguita in una fase successiva, solo per le coppie di righe ancora non abbinate dopo l’esecuzione di tutte le regole regolari. Usala per la regola "più permissiva" che dovrebbe catturare ciò che le regole rigorose hanno mancato.

#### Condizioni di Attivazione

Una regola può avere **condizioni di attivazione** — espressioni che devono essere vere prima che la regola venga eseguita. Se una condizione è falsa, la regola viene **saltata per questo documento** (la cronologia delle corrispondenze la mostra come "non eseguita" con la motivazione). Le espressioni utilizzano i conteggi delle righe che vengono abbinate:

| Espressione               | Significato                                                             |
| ------------------------ | ----------------------------------------------------------------------- |
| `[[count(po_lines)]]`    | numero di righe dell’ordine di acquisto disponibili per la corrispondenza |
| `[[count(table_lines)]]` | numero di righe del documento mappate per la corrispondenza             |

Confrontale con `==`, `!=`, `>`, `>=`, `<`, `<=` e combina più condizioni con `&` (e). Esempi:

* `([[count(po_lines)]] > 1) & ([[count(table_lines)]] > 1)` — solo per documenti con più righe su entrambi i lati (tipico per una regola multi match).
* `([[count(po_lines)]] == 1) & ([[count(table_lines)]] == 1)` — solo per documenti a riga singola contro un ordine a riga singola.
* `([[count(po_lines)]] >= 1) & ([[count(table_lines)]] >= 1)` — ogni volta che c’è qualcosa da abbinare.

{% hint style="warning" %}
Le condizioni di attivazione sono la ragione più comune per cui una regola "non fa nulla". Una regola match-on-total con la condizione `[[count(table_lines)]] > 1` non viene mai eseguita per una fattura a riga singola — e una [regola di trasformazione](../../transformation-rules.md) che riduce la fattura a una riga totale produce esattamente un documento di questo tipo. Controlla i conteggi nella cronologia delle corrispondenze prima di modificare la regola stessa.
{% endhint %}

#### Confronto Colonne (Criteri di Corrispondenza)

Questa è la definizione centrale della logica della regola, specificando quali campi devono corrispondere tra i documenti.

1. Definizione delle Colonne da Confrontare:
   * **Colonne PO:** Il campo estratto dai dati dell’Ordine di Acquisto (es. numero riga).
   * **Colonne Tabella Estratte:** Il campo corrispondente estratto o parsato dal documento in entrata (Fattura/Conferma d’Ordine) (es. `POSITION`).
2. **Tipo di Confronto:** Definisce la natura della corrispondenza richiesta (es. Tt per confronto Testo/Stringa, richiedendo una corrispondenza esatta carattere per carattere; # per confronto Numerico).
3. **Consenti Tolleranza:** Per i campi numerici (quantità, prezzo), attivando questa opzione il sistema applica la Tolleranza Standard Globale definita in precedenza. Se _non_ abilitata per un campo numerico, i valori devono corrispondere esattamente.
4. **Ignora nella Corrispondenza Manuale:** Se selezionato, questo criterio è rilassato durante l’intervento manuale. Utile per campi come descrizioni o riferimenti interni che possono variare leggermente, permettendo all’utente di ignorare piccole discrepanze non critiche.

**Quali colonne possono essere confrontate**

| Colonna                         | Lato documento                           | Lato ordine di acquisto                  | Nota                                                                                                                                                                                                                             |
| ------------------------------- | --------------------------------------- | ---------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Numero riga                     | `POSITION`                              | `line_number`                            | Testo, esatto. Utile solo quando il fornitore stampa i numeri delle righe d’ordine sul documento.                                                                                                                                |
| Identificatore articolo         | `ITEM_IDENTIFIER`                       | `item_identifier`                        | Testo, esatto. Numero articolo o numero articolo fornitore, anche tramite la [Mappa Numero Articolo Fornitore](supplier-item-number-map-admin-documentation.md).                                                                 |
| Quantità normalizzata effettiva | `QUANTITY_EFFECTIVE_NORMALIZED`         | `quantity_effective_normalized`          | Numerico. La quantità selezionata da **Match Quantity On**, convertita nella stessa unità su entrambi i lati (conversione codice unità, quantità "per").                                                                           |
| Prezzo unitario normalizzato effettivo | `UNIT_PRICE_EFFECTIVE_NORMALIZED`       | `unit_price_effective_normalized`        | Numerico. Il prezzo unitario per singola unità dopo sconti e dopo **Unit Price Per** — e, se [Calcola prezzo unitario PO](calculate-po-unit-price.md) è attivo, il prezzo calcolato dall’importo e quantità della riga d’ordine. |
| Importo netto                   | `NET_AMOUNT`                           | `total_amount`                           | Numerico. Usato dalle regole match-on-total.                                                                                                                                                                                     |

**Esempio: Regola PO-Match Rigorosa (`DefaultRule#1`)**

Una regola rigorosa tipica combina controlli di identità obbligatori con controlli di valore:

* **Identità Obbligatoria:** Numero Riga e Identificatore Articolo devono corrispondere esattamente (confronto Testo, senza tolleranza).
* **Controlli di Valore:** Quantità Normalizzata Effettiva e Prezzo Unitario Normalizzato Effettivo devono corrispondere (confronto Numerico, tolleranza consentita). Solo se tutti e quattro i criteri sono soddisfatti (con tolleranza per i valori) viene eseguita una corrispondenza automatica.

***

## Il set di regole predefinito

Ogni organizzazione inizia con lo stesso set di regole predefinito. È un buon riferimento quando si costruisce il proprio:

| Regola                     | Tipo / priorità                | Colonne confrontate                                                      | Condizione di attivazione                              |
| -------------------------- | ------------------------------ | ----------------------------------------------------------------------- | ----------------------------------------------------- |
| `DefaultRule#1`            | single match, priorità 1       | numero riga, identificatore articolo, quantità (tol.), prezzo unitario (tol.) | sempre                                                |
| `DefaultMultiMatchRules#1` | multi match, priorità 1, fallback | identificatore articolo, quantità (tol.), prezzo unitario (tol.)      | `count(po_lines) > 1` e `count(table_lines) > 1`      |
| `DefaultTotalMatchRules#1` | match on total, priorità 1     | importo netto ↔ totale ordine di acquisto (nessuna tolleranza)          | `count(po_lines) >= 1` e `count(table_lines) > 1`     |
| `DefaultRule#2`            | single match, priorità 2, fallback | identificatore articolo, quantità (tol.), prezzo unitario (tol.)      | sempre                                                |
| `DefaultRule#3`            | single match, priorità 2, fallback | quantità (tol.), prezzo unitario (tol.)                               | `count(po_lines) == 1` e `count(table_lines) == 1`    |

Leggendolo dall’alto verso il basso: prima la regola rigorosa (numero riga e articolo devono essere stampati sul documento), poi i fallback senza il numero riga, infine un’ultima risorsa per documenti a riga singola che confronta solo quantità e prezzo.

***

## Impatto sul Processo di Corrispondenza PO

Il set di regole definito governa direttamente l’efficienza e l’integrità del flusso di lavoro di corrispondenza PO:

* **Prioritizzazione e Fallback:** La Priorità definita assicura che il sistema tenti prima il metodo di corrispondenza più affidabile. Se le regole rigorose e ad alta priorità falliscono, il sistema ricorre a regole più ampie, mirando a minimizzare il numero di eccezioni indirizzate agli utenti.
* **Controllo della Qualità della Corrispondenza:** Regole più severe (che richiedono corrispondenze più esatte e meno tolleranza) producono meno corrispondenze automatiche, ma altamente affidabili. Regole più permissive aumentano il tasso di corrispondenza automatica ma aumentano il rischio di falsi positivi.
* **Gestione delle Eccezioni (Corrispondenza Manuale):** Abilitando regole per la Corrispondenza Manuale, il sistema fornisce opzioni strutturate per gli utenti. Se una transazione non soddisfa i criteri di corrispondenza automatica, diventa un’eccezione. L’utente può quindi tentare di risolvere l’eccezione applicando una regola manuale predefinita, che potrebbe avere criteri più rilassati (es. ignorare una piccola discrepanza testuale come da impostazione "Ignora nella Corrispondenza Manuale").

## Cos’altro influenza il risultato

* **Quando la corrispondenza viene eseguita:** durante l’elaborazione del documento, quando un utente clicca su **Auto PO Match**, e **ad ogni salvataggio** in cui il numero dell’ordine di acquisto è cambiato o non è mai stato cercato prima (per esempio quando i dati anagrafici lo hanno inserito dopo l’elaborazione). Un salvataggio non sovrascrive mai una corrispondenza già esistente.
* **[Regole di trasformazione](../../transformation-rules.md)** vengono eseguite prima della corrispondenza e possono modificare le righe — e con esse i conteggi delle righe che le condizioni di attivazione osservano. Una regola tabella che ricostruisce le righe mantiene una corrispondenza esistente finché le righe restano le stesse; se sostituisce righe abbinate, la corrispondenza viene eliminata e il nome della regola è mostrato come motivo.
* **[Calcola prezzo unitario PO](calculate-po-unit-price.md)** modifica quale prezzo unitario le regole confrontano sul lato ordine di acquisto.
* **[Impostazioni di tolleranza](purchase-order-tolerance-settings-additional-purchase-order-tolerance.md)** e **[stati disabilitati](purchase-order-disable-statuses.md)** decidono quanto è rigoroso il confronto e quali righe dell’ordine di acquisto sono offerte.

## Risoluzione dei problemi

| Sintomo                                                         | Cosa controllare                                                                                                                                                                                   |
| ---------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| "Nessuna corrispondenza" anche se ogni valore coincide          | Aprire la cronologia delle corrispondenze: quale regola è stata eseguita, su quale colonna ha fallito (la deviazione è mostrata per colonna), la regola è stata saltata da una condizione di attivazione? |
| Prezzo unitario non corrisposto esattamente dell’aliquota fiscale | Il totale dell’ordine di acquisto include l’imposta; attivare [Calcola prezzo unitario PO](calculate-po-unit-price.md) (prima importo netto) o confrontare l’importo netto della riga.                  |
| Una regola match-on-total non viene mai eseguita                 | La sua condizione di attivazione richiede più di una riga documento. Impostare `[[count(table_lines)]] >= 1` o non ridurre le righe con una regola di trasformazione.                                |
| Il set di regole non ha alcun effetto                           | **PO match server side** è disattivato per il tipo di documento, oppure il set di regole modificato è ancora una bozza — attivare la versione.                                                     |

***

## Personalizzare le Regole di Corrispondenza PO

Per modificare le regole di corrispondenza PO, la versione predefinita può essere clonata cliccando su **"Configura Versioning"** e utilizzando l’opzione **"Clona come Bozza"** dalle opzioni disponibili nella scheda

<figure><img src="../../../../../../.gitbook/assets/image (197).png" alt=""><figcaption></figcaption></figure>