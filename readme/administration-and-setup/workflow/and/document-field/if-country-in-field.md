# Se Paese nel campo

<figure><img src="../../../../.gitbook/assets/workflow-card-qa-20261021-card-70b0b5860da5-it.png" alt="Campi della scheda nella versione visualizzata. I campi non sono ancora configurati." width="563"><figcaption><p>Campi della scheda nella versione visualizzata. I campi non sono ancora configurati.</p></figcaption></figure>

Utilizzare questa condizione quando un passaggio di elaborazione aggiuntivo deve dipendere da un gruppo di paesi. L’esempio verifica se il paese letto da un campo del documento appartiene all’Unione europea.

**Posizione:** Workflow standard → condizioni aggiuntive (AND) → Campo del documento. Configurare separatamente l’azione successiva in THEN.

## Configurazione — versione 2

| Impostazione | Valore |
| --- | --- |
| Campo | Un campo di testo esistente contenente il nome del paese |
| Operatore | `is` |
| Regione | Unione europea (UE) |
| Valore di continuazione | `true` |

<!-- workflow-card-practical-example-20261021 -->

## Esempio pratico

| Valore del paese nel campo | Condizione attesa |
| --- | --- |
| `Germany` | Soddisfatta |
| `United States` | Non soddisfatta |

I nomi dei paesi mostrati come codice sono valori di input fissi per questo esempio.

## Limiti e verifiche

`false` non inverte il confronto. Con questa impostazione, nemmeno un paese corrispondente produce una condizione positiva. Per verificare la condizione opposta, selezionare `isnot` con `true`.

Gestire separatamente i campi mancanti e i valori di paese vuoti: possono restituire un risultato di dati mancanti anziché una normale mancata corrispondenza.

L’esame del codice sorgente della versione di sviluppo del 22 ottobre 2026 mostra un errore di conversione per input ISO come `DE` e `DEU`. Questi esempi utilizzano quindi nomi di paesi completi. Verificare separatamente la gestione dei codici ISO nella versione installata.

I gruppi disponibili, tra cui UE, Schengen e NAFTA, provengono dall’implementazione della scheda. Verificare i paesi inclusi nella propria versione prima di utilizzare un gruppo in una regola aziendale.
