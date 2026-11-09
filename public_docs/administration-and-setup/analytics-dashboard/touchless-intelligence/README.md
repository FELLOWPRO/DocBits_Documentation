# Touchless Intelligence

Touchless Intelligence risponde a due domande distinte: **DocBits ha estratto correttamente la fattura?** E: **l'intero processo è terminato senza interventi di elaborazione?** Un'estrazione corretta può comunque richiedere rilavorazione quando i dati Infor differiscono. AP indica il team umano della contabilità fornitori.

## Video: funzioni del report Touchless

{% embed url="https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/touchless-intelligence-preview-admin/v2/it.mp4" %}

Questa versione di verifica di 5:56 mostra un report con dati: filtri, KPI e calcolo, andamento, primi bloccanti, prove registrate, cronologia del documento, confronto delle esecuzioni, regole apprese, miglioramenti e cronologia, report di consulenza e risultati MCP reali.

[Aprire il video con sottotitoli italiani e 16 link ai capitoli](https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/touchless-intelligence-preview-admin/v2/it.html). La revisione di ascolto umana di questa nuova versione è ancora in sospeso.

Questi casi didattici spiegano le funzioni del report. Una raccomandazione o un'anteprima non dimostra un'impostazione applicata né un miglioramento misurato. La proposta di modifica MCP mostrata richiede ancora una configurazione di destinazione precisa; anteprima e applicazione non sono disponibili per quella proposta. Alcuni testi nativi del prodotto possono mantenere la lingua originale.

<figure><img src="../../../.gitbook/assets/anatomy-touchless-it.svg" alt="Linea di smistamento isometrica: un nastro trasportatore con 14 varchi, uno spintore che devia un documento in un vassoio di revisione, un contenitore di esportazione con una pila di documenti e un quadrante che indica 78,9 per cento"><figcaption><p>Touchless come linea di smistamento, con i numeri illustrativi dell'esempio di calcolo: i 14 varchi sono le fasi del percorso della pipeline, i fogli ancora sul nastro sono in corso e non vengono conteggiati, un documento che si ferma a un varco viene spinto nel vassoio di revisione con i documenti AP assisted (30) ed eccezione di processo (10), e i documenti pure (120) e solo approvazione (30) nel contenitore di esportazione danno i 150 su 190 del quadrante, ovvero il 78,9 %, oltre il contrassegno dell'obiettivo del 70 %.</p></figcaption></figure>

## Trovare la guida giusta

| Guida | Che cosa copre |
| --- | --- |
| [Metriche e calcolo](touchless-metrics.md) | Categorie di esito, numeratore e denominatore, azioni AP e calcoli |
| [Usare il pannello](touchless-dashboard.md) | Filtri, schede KPI, andamenti, primi bloccanti e controlli |
| [Esempi pratici: prezzo e quantità](touchless-examples.md) | Fatture fittizie e viste PO reali su Dev con differenze di prezzo e quantità |
| [Diagnosi del fornitore e cluster di problemi](touchless-supplier-diagnosis.md) | Dare priorità ai fornitori e alle cause ricorrenti |
| [Diagnosi dell'abbinamento ordini](touchless-po-matching-diagnosis.md) | Capire le regole attive, le tolleranze e il flusso decisionale |
| [Tracciamento del documento](touchless-document-trace.md) | Ispezionare i valori originali, le esecuzioni, i bloccanti e gli interventi |
| [Proposte di modifica e report](touchless-change-proposals.md) | Distinguere anteprima, applicazione, misurazione dell'effetto e annullamento |
| [Spiegare e migliorare Touchless con MCP](touchless-mcp.md) | Spiegare, diagnosticare ed effettuare miglioramenti controllati tramite MCP |

<figure><img src="../../../.gitbook/assets/touchless-overview-it.png" alt="La scheda Touchless Intelligence con cinque indicatori chiave, suggerimenti di miglioramento e il grafico del tasso touchless"><figcaption><p>La scheda Touchless Intelligence: indicatori chiave, miglioramenti, il tasso nel tempo e il grafico del primo punto di perdita. Organizzazione di esempio con dati dimostrativi; i nomi dei fornitori sono fittizi.</p></figcaption></figure>

## Impostazioni del report

**Settings → Module → Dashboards & Analytics**: qui un amministratore gestisce le quattro impostazioni dell'organizzazione che il report legge. Determinano l'obiettivo e la vista dei costi; un campo vuoto significa che DocBits usa il valore predefinito.

| Impostazione | Predefinito | Che cosa controlla |
| --- | --- | --- |
| Touchless target | 70 % | La quota di documenti che dovrebbe passare senza interventi di elaborazione. Il report la usa come contrassegno dell'obiettivo nel grafico del tasso. |
| Minutes per AP intervention | 6 min | Il tempo necessario a un addetto AP per correggere e rilasciare un documento. |
| Hourly cost | 40 | Il costo di un'ora di lavoro AP nella valuta indicata sotto. |
| Currency | EUR | La valuta della vista dei costi, come codice ISO 4217 di tre lettere, ad esempio `EUR`, `CHF` o `USD`. DocBits memorizza il codice in maiuscolo e rifiuta un valore che non sia un codice di valuta, così un errore di battitura non può arrivare al report. |

L'API ricontrolla i valori memorizzati e usa il valore predefinito per un valore con cui non riesce a lavorare.

## Accesso

Questa area appartiene alla [Dashboard di analisi](..). Gli amministratori hanno accesso; gli altri utenti necessitano della concessione del ruolo corrispondente. Analisi IA, modifiche supportate e report di consulenza possono richiedere diritti di amministratore.

<!-- Documentation review 2026-11-04: extraction quality vs process outcomes; KPI and terminal-outcome definitions checked against DocBits_API c51f350c728acb8ac964098d15f7b006bce273f4, module/automation_intelligence/kpi.py and bucket.py. Existing native screenshots retained and checked separately from illustrative examples. -->
<!-- Completion review 2026-11-04: owned synthetic PO examples, MCP schema/read evidence, human-action classification, KPI labels and screenshot proof limits. -->
