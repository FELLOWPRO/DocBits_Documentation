# Se Paese nel campo

<figure><img src="../../../../.gitbook/assets/workflow-card-qa-20261021-card-70b0b5860da5-it.png" alt="Campi della scheda nella versione visualizzata. I campi non sono ancora configurati." width="563"><figcaption><p>Campi della scheda nella versione visualizzata. I campi non sono ancora configurati.</p></figcaption></figure>

Uso previsto: un passaggio di elaborazione aggiuntivo dipende da un gruppo di paesi. L’esempio seguente descrive una regola di appartenenza all’Unione europea.

## Limitazione attuale — codice sorgente verificato il 22 ottobre 2026

I test locali del codice sorgente con il tipo nativo della selezione della regione falliscono prima del confronto del paese e restituiscono `missing_variable` o `error`. I nomi completi dei paesi non aggirano questo problema. Per questa versione non è stata verificata un’esecuzione riuscita sul backend distribuito.

**Posizione:** Workflow standard → condizioni aggiuntive (AND) → Campo del documento. Configurare separatamente l’azione successiva in THEN.

## Configurazione — versione 2

| Impostazione | Valore |
| --- | --- |
| Campo | Un campo di testo esistente contenente il nome del paese |
| Operatore | `is` |
| Regione | Unione europea (UE) |
| Valore di continuazione | `true` |

<!-- workflow-card-practical-example-20261021 -->

## Esempio previsto — verificare la correzione prima dell’uso

Verificare la correzione ed entrambi i casi dell’esempio nella versione installata prima di attivare questa regola. La tabella descrive la regola aziendale prevista, non un’esecuzione riuscita confermata.

| Valore del paese nel campo | Raggruppamento dei paesi previsto |
| --- | --- |
| `Germany` | All’interno dell’UE |
| `United States` | Al di fuori dell’UE |

I nomi dei paesi mostrati come codice sono valori di input fissi per questo esempio.

## Limiti e verifiche

`false` non inverte il confronto. Con questa impostazione, nemmeno un paese corrispondente produce una condizione positiva. Per verificare la condizione opposta, selezionare `isnot` con `true`.

Gestire separatamente i campi mancanti e i valori di paese vuoti: possono restituire un risultato di dati mancanti anziché una normale mancata corrispondenza.

Il problema di conversione ISO per input come `DE` e `DEU` è indipendente. Sostituire i codici ISO con i nomi completi dei paesi non risolve l’errore di selezione della regione.

I gruppi disponibili, tra cui UE, Schengen e NAFTA, provengono dall’implementazione della scheda. Verificare i paesi inclusi nella propria versione prima di utilizzare un gruppo in una regola aziendale.
