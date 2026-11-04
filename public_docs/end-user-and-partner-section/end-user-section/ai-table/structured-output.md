# Structured Output per le tabelle

Structured Output indica all'AI quali colonne restituire, usando uno schema generato dalla configurazione. Riduce quindi le intestazioni libere da mappare in seguito. **Utilizzare l'estrazione strutturata (IA)** controlla la forma dell'output; modello e Vision controllano il modello e i dati in ingresso.

## Perché l'output strutturato è spesso migliore

| Esempio | Senza schema fisso | Vantaggio di Structured Output |
| --- | --- | --- |
| Intestazioni variabili | «Art.-Nr.», «SKU» e «Item Code» possono produrre chiavi diverse. | La chiave richiesta `ITEM_NUMBER` rimane stabile tra layout e semplifica la mappatura. |
| Due codici articolo | Il codice interno `00127` può essere confuso con quello del fornitore `V-884`. | `ITEM_NUMBER` e `SUPPLIER_ITEM_NUMBER` sono destinazioni separate. Verificare comunque i valori: lo schema impone nomi, non comprensione del contenuto. |
| Colonna progetto personalizzata | Il codice stampato può essere omesso o restituito con un altro nome. | `PROJECT_CODE` impostato su **Sì** viene richiesto esplicitamente. Un dato assente deve comunque essere riconosciuto come mancante. |

Anche il tipo aiuta: le colonne `AMOUNT` sono descritte nello schema come numero o `null`, con un'indicazione del significato. Ciò aiuta, per esempio, a distinguere un divisore di prezzo da un'unità di misura. Gli altri tipi non diventano automaticamente valori JSON con tipo rigorosamente imposto. Conservare gli zeri iniziali degli identificativi.

Non sono garantiti precisione superiore, tempi inferiori o costi minori. Restano possibili valori errati e righe mancanti. Confrontare gli stessi documenti a parità di modello, Vision e addestramento.

## 1. Prerequisiti e impostazione dell'organizzazione

Aprire [Classificazione ed estrazione](../../../administration-and-setup/settings/document-processing/classification-and-extraction/README.md), **Generale → Estrazione**. Le impostazioni dell'organizzazione richiedono i relativi permessi di amministratore e vengono salvate immediatamente.

1. Il tipo di documento corretto deve avere una tabella e le [colonne](../../../administration-and-setup/settings/global-settings/document-types/table-columns/README.md) necessarie.
2. Attivare i percorsi richiesti. Nel percorso PDF basato su regole con fallback AI servono **Table Extraction** e **AI Table Extraction**. Structured Output, da solo, non avvia l'estrazione AI delle tabelle.
3. Impostare **Utilizzare l'estrazione strutturata (IA)** come valore dell'organizzazione. La preferenza tecnica è `USE_STRUCTURED_EXTRACTION`.
4. Verificare testo leggibile o ingresso Vision. Le regole classiche salvate possono ancora determinare il percorso effettivo; controllare [quale percorso è stato usato](../../../overview-and-basics/faq/document-processing/which-extraction-path-was-used.md).

<figure><img src="../../../.gitbook/assets/structured-output-settings-it-20261104.png" alt="Controlli attuali di estrazione. Structured Output è disattivato in questa configurazione esistente, quindi l&#x27;anteprima dello schema non appare. Nessuna impostazione di estrazione è stata modificata."><figcaption><p>Controlli attuali di estrazione. Structured Output è disattivato in questa configurazione esistente, quindi l&#x27;anteprima dello schema non appare. Nessuna impostazione di estrazione è stata modificata.</p></figcaption></figure>

## 2. Impostazioni specifiche del modello di estrazione

L'ambito è l'organizzazione e il modello di estrazione corrente, non tutti i modelli di un fornitore.

| Situazione | Comportamento effettivo |
| --- | --- |
| Attivazione esplicita nel modello di estrazione | Structured Output si applica anche con impostazione organizzativa disattivata. |
| Disattivazione esplicita nel modello di estrazione | Non si applica anche con impostazione organizzativa attivata. |
| Nessuna impostazione specifica | Si applicano l'impostazione organizzativa pertinente e i relativi valori predefiniti. |

Nella schermata di convalida di un documento adatto, aprire **Altre opzioni** (tre punti). Se esiste un contesto di modello di estrazione, un amministratore può modificare **Utilizzare l'estrazione strutturata (IA)**. La conferma salva il valore e riavvia il documento; Annulla scarta la modifica. Non cambia altri modelli dello stesso fornitore né rielabora automaticamente i documenti storici.

**Nuovi modelli fornitori:** senza regole di formattazione della tabella salvate e senza un valore Structured Output proprio, l'elaborazione può attivarlo automaticamente e salvare la scelta nel modello, anche con l'organizzazione disattivata. Il comportamento è controllato da `STRUCTURED_EXTRACTION_FOR_NEW_SUPPLIERS` (attivo per impostazione predefinita); la schermata descritta non contiene un ulteriore interruttore per questa opzione. Una scelta esplicita esistente viene rispettata.

L'elenco [Modello AI](../../../administration-and-setup/settings/document-processing/classification-and-extraction/ai-model.md) mostra i valori dei modelli di estrazione; gli interruttori Structured Output sono indicatori. Modificare il valore dal menu del documento. **Elimina voce** può rimuovere insieme le impostazioni specifiche di modello AI, E-Text e altre opzioni. Non è una disattivazione mirata. L'attivazione automatica può ripetersi se il modello torna a essere considerato nuovo.

## 3. Use AI: Predefinito, Sì o No

Aprire le [colonne di tabella](../../../administration-and-setup/settings/global-settings/document-types/table-columns/README.md) del tipo di documento e della tabella corretti. **Utilizzare l'IA (Use AI)** è un menu a tre stati, non una casella. La modifica viene salvata immediatamente.

| Scelta attuale | Effetto sullo schema base |
| --- | --- |
| **Predefinito · richiesto** oppure **Predefinito · non richiesto** | Usa la selezione DocBits per quel tipo e nome di colonna. Predefinito non significa sempre attivo né sempre disattivo. |
| **Sì · richiesto** | Richiede esplicitamente la colonna configurata all'AI. |
| **No · non richiesto** | La esclude dallo schema base anche se normalmente viene richiesta. |

Tornare a **Predefinito** rimuove la scelta esplicita. Una nuova colonna personalizzata normalmente non appartiene alla selezione AI predefinita: scegliere **Sì** per richiederla. Le colonne AI predefinite non coincidono con tutte le colonne fornite. Verificare effetto indicato e anteprima.

**Obbligatoria**, **Sola lettura** e **Nascosta** controllano completezza, modificabilità e visibilità; non sostituiscono la scelta AI. **No** non elimina la colonna né cancella valori e non impedisce a regole, script o altre fonti di compilarla. Addestramento del fornitore e tag AI possono ampliare la richiesta effettiva: risolvere anche lì eventuali contraddizioni. L'interruttore non sostituisce automaticamente un risultato basato soltanto su regole.

<figure><img src="../../../.gitbook/assets/structured-output-column-choice-it-20261104.png" alt="Menu Use AI attuale con Predefinito, Sì e No. Nessuna opzione è stata modificata. Le celle dei titoli sono nascoste per riservatezza."><figcaption><p>Menu Use AI attuale con Predefinito, Sì e No. Nessuna opzione è stata modificata. Le celle dei titoli sono nascoste per riservatezza.</p></figcaption></figure>

## 4. Leggere l'anteprima

Con l'interruttore dell'organizzazione attivo compare **Cosa richiede l'IA**. Scegliere fattura, conferma d'ordine, documento di trasporto, ordine cliente o preventivo. I collegamenti di modifica aprono i campi o le colonne pertinenti. L'anteprima non esegue un'estrazione.

* **Richiesto:** campi di intestazione e colonne inclusi nello schema base; un indicatore contrassegna i valori AI ereditati.
* **Non richiesto:** colonne configurate fuori dalla selezione corrente.
* **Valori predefiniti disattivati:** campi o colonne esclusi esplicitamente che normalmente verrebbero richiesti.
* **Strict e conteggio:** lo schema base è rigoroso fino al limite DocBits attuale di **100 proprietà**. Si contano campi di intestazione richiesti, contenitore della tabella e colonne di posizione distinte richieste, non le righe. Superato il limite, lo schema guida il modello senza vincolo rigoroso.

L'anteprima esclude addestramento e tag del fornitore. Istruzioni aggiuntive possono consentire un output aperto prima dell'apprendimento delle mappature; le colonne sorgente apprese possono permettere di nuovo un output chiuso. «Strict» non dimostra quindi la modalità di ogni esecuzione. L'anteprima organizzativa può mancare se è attivo soltanto il modello di estrazione: non cambiare l'impostazione globale solo per visualizzarla.

Senza una configurazione utilizzabile dei campi di intestazione non può essere costruito uno schema completo. Un interruttore attivo non ne dimostra l'uso. Controllare l'esecuzione tramite **Spiega estrazione** e i log disponibili; [Tabella AI](README.md) descrive viste e permessi.

## 5. Esempio: fattura con due codici e un progetto

Questo esempio sintetico definisce un risultato da verificare, non un'estrazione eseguita.

| Articolo | Articolo fornitore | Quantità | Prezzo unitario | Importo riga | Progetto |
| --- | --- | --- | --- | --- | --- |
| `00127` | `V-884` | 2 | 12,50 | 25,00 | `PRJ-42` |
| `00208` | `V-990` | 1 | 7,00 | 7,00 | `PRJ-42` |

1. Scegliere **Fattura** e verificare la selezione AI per `ITEM_NUMBER`, `SUPPLIER_ITEM_NUMBER`, `QUANTITY`, `UNIT_PRICE` e `TOTAL_AMOUNT`.
2. Nella stessa tabella, creare una colonna di testo con titolo letterale `Project Code`, che genera il nome tecnico `PROJECT_CODE`. Scegliere **Sì · richiesto**. Usare **No · non richiesto** consapevolmente; una colonna obbligatoria deve conservare una fonte.
3. Controllare organizzazione e modello di estrazione corrente. Nell'anteprima Fattura, se disponibile, `PROJECT_CODE` deve risultare richiesto. Con Predefinito questa colonna personalizzata normalmente non lo sarebbe.
4. Caricare nuovamente un documento di prova autorizzato o riavviarlo. Il cambio non modifica retroattivamente le tabelle estratte. Controllare anche mappature e istruzioni salvate.
5. Attendere due righe: `ITEM_NUMBER` = `00127`/`00208`, `SUPPLIER_ITEM_NUMBER` = `V-884`/`V-990` e `PROJECT_CODE` = `PRJ-42` in entrambe. Verificare zeri iniziali, quantità, prezzi e importi; 25,00 + 7,00 = 32,00 netti. Il totale corretto non dimostra ogni singolo valore.
6. Ripetere con l'intestazione «SKU» e con un documento senza progetto. Le colonne devono rimanere stabili, senza valori inventati. Se i codici vengono scambiati, aggiungere e provare una mappatura o istruzione inequivocabile e ricontrollare entrambe le colonne.

Il vantaggio è una struttura richiesta stabile tra layout. Correttezza dei dati, campi obbligatori, abbinamento ordini ed esportazione richiedono verifiche separate.

## 6. Problemi comuni

| Osservazione | Controllo successivo |
| --- | --- |
| Colonna personalizzata assente | Tipo e tabella corretti, scelta Sì, anteprima, valore del modello e tag; riestrarre. |
| Colonna predefinita vuota | Scelta No esplicita? Se richiesta ma assente dal documento, trattare il dato come mancante. |
| Comportamento diverso dall'impostazione globale | Impostazione specifica, attivazione automatica e percorso effettivo. |
| Colonne diverse o aggiuntive | Mappature apprese, tag, output aperto e limite dell'esecuzione reale. |
| Documenti vecchi invariati | Rielaborare; prima verificare l'effetto sulle correzioni manuali. |

Approfondimenti: [Modificare le colonne](../../../administration-and-setup/settings/global-settings/document-types/table-columns/editing-and-deleting-columns.md), [Tag e istruzioni](ai-table-tags.md), [Modello AI e valori specifici](../../../administration-and-setup/settings/document-processing/classification-and-extraction/ai-model.md).
