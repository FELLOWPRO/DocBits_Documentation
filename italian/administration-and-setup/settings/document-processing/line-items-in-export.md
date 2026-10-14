# Voci di riga nell'esportazione

Cosa succede alla tabella delle voci di riga quando un documento viene approvato ed esportato dipende dal metodo di esportazione. Questa pagina spiega quali colonne lasciano DocBits, quali sono obbligatorie e perché un'esportazione può mostrare meno righe della schermata di validazione.

## Due tipi di esportazione

| Metodo di esportazione | Cosa viene inviato per la tabella |
|---|---|
| **webhook**, **watcher**, **sftp**, **infor_sftp** (JSON / XML) | La tabella così com'è nella schermata di validazione: ogni [colonna della tabella](../global-settings/document-types/table-columns.md) non nascosta di ogni riga, con valore, valore formattato e confidenza. |
| **infor-m3-cloud**, **infor-m3-toml-cloud**, **infor-idm-***, **infor-gls840-onpremise**, **infor-m3-oc-charges-onpremise** (BOD Infor ERP / SAP) | Non la tabella grezza. DocBits costruisce da essa le **righe di ricevimento** e le **righe di costo** (vedi sotto) e le mappa sui campi del BOD con la mappatura configurata in [Esportazione verso INFOR](../../../infor-integration-and-configuration/exporting-to-infor/README.md). |

## Righe di ricevimento e righe di costo (esportazioni Infor)

Una riga di fattura nell'ERP è o una **riga di ricevimento**, che salda un ricevimento di ordine di acquisto, o una **riga di costo**, che contabilizza un importo su un conto contabile con dimensioni. DocBits decide per ogni riga della fattura:

* Le **righe di ricevimento** derivano dal **PO matching**. Ogni riga della fattura abbinata a una riga di PO (Dashboard → PO Match, oppure automaticamente con *PO auto match*) diventa una riga di ricevimento con numero di PO, riga di PO, riga di ricevimento e la quantità e l'importo abbinati. Una fattura senza abbinamento PO **non ha righe di ricevimento**: l'anteprima dell'esportazione mostra allora `receipt_lines: []`, il che è corretto, non un bug.
* Le **righe di costo** derivano dalla **registrazione contabile** creata dal passaggio di contabilità analitica (o da Auto Accounting): conto contabile, dimensioni, importo, quantità per riga. Una fattura senza registrazione contabile non ha righe di costo.
* Le **righe imposta** vengono costruite dagli importi delle imposte dell'intestazione, non dalla tabella.

Quindi, per le esportazioni Infor, la tabella delle voci di riga è l'*input* del PO matching e della contabilità; ciò che l'ERP riceve è il risultato di questi due passaggi. Una riga che non è né abbinata a un PO né contabilizzata non arriva all'ERP.

{% hint style="warning" %}
Perché il PO matching funzioni, la tabella deve avere le colonne predefinite **numero articolo, prezzo unitario, quantità e importo totale**. Se una di esse è nascosta, la schermata di validazione mostra *Line Item Table is missing Mandatory column for PO* e non è possibile costruire righe di ricevimento.
{% endhint %}

## Colonne obbligatorie e finestra di approvazione

Prima che un documento possa essere approvato, DocBits controlla la tabella:

1. Ogni colonna contrassegnata **Obbligatoria** (Impostazioni → Tipi di Documento → Colonne della Tabella) deve avere un valore in ogni riga.
2. Ogni riga deve superare il **controllo del totale riga**: `totale = quantità × prezzo unitario + oneri − sconto` con una tolleranza di 0,02. Le righe che non lo superano vengono evidenziate; il messaggio indica il valore atteso e quello effettivo.
3. La **somma dei totali di riga** viene confrontata con l'importo netto nell'intestazione. Una differenza genera un avviso e non blocca l'approvazione.

La finestra di approvazione elenca ciò che manca ancora. Un amministratore può disattivare tutti i controlli sulla tabella per tipo di documento con **Salta la validazione della tabella** (Tipi di Documento → Altre impostazioni): totali di riga e colonne obbligatorie non vengono più controllati; i controlli dell'intestazione restano attivi.

Dettagli sui messaggi: [Risoluzione dei Problemi di Estrazione delle Tabelle](../../../overview-and-basics/faq/document-processing/table-extraction-troubleshoot.md#messaggi-sulla-tabella).

## Tabella vuota

* Le **esportazioni JSON / XML** inviano il documento con `tables: []` (oppure la tabella con zero righe). Il sistema ricevente deve gestire una tabella vuota.
* Le **esportazioni Infor** senza righe di ricevimento e senza righe di costo inviano solo l'intestazione e le righe imposta. La maggior parte degli ERP rifiuta una fattura senza righe: configura Auto Accounting o una riga di costo predefinita per questi tipi di documento, oppure instradali verso un'esportazione diversa.
* Un tipo di documento **senza tabella** (nessuna tabella configurata) non invia mai dati di riga; è il comportamento atteso per tipi di documento come le conferme d'ordine, che vengono abbinate a livello di intestazione.

## Verificare prima di approvare

Partner e supporto con accesso all'API o all'MCP possono richiedere il payload di esportazione di un documento prima che venga inviato: lo strumento MCP `get_export_preview(doc_id)` restituisce esattamente ciò che l'esportazione invierà, `receipt_lines`, `cost_lines` e `tax_lines` per le esportazioni Infor, `tables` per le esportazioni JSON. Usalo quando l'ERP segnala righe mancanti: se `receipt_lines` è vuoto, la fattura non è stata abbinata a un PO; se `cost_lines` è vuoto, non esiste alcuna registrazione contabile.

## Pagine correlate

* [Esportazione](export.md): configurazioni e metodi di esportazione
* [Colonne della Tabella](../global-settings/document-types/table-columns.md)
* [Esportazione verso INFOR](../../../infor-integration-and-configuration/exporting-to-infor/README.md): mappature dei campi BOD per righe di ricevimento, di costo e imposta
