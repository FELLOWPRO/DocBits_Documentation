---
description: "Configurare le schede usando nome, versione, input, ambito, risultati ed effetti."
---

# Comprendere e configurare le schede workflow

Scegliere una scheda in base a operazione e ambito. **Field is** controlla presenza o vuoto; **Docfield is** confronta valori. Assegnazione documentale, attività e notifica hanno effetti diversi. Una categoria non sostituisce il riferimento della versione specifica.

## Contenuto di un riferimento completo

| Elemento | Domanda necessaria |
| --- | --- |
| Identità | Nome visibile, tipo tecnico, versione e ruolo When/And/Then? |
| Prerequisiti | Licenza, autorizzazioni e dati necessari? |
| Input | Tipo, valore, predefinito e scelte ammesse per ogni parametro? |
| Ambito | Campo, riga, tutte le posizioni o variabile organizzativa? |
| Risultati | Successo, falso o errore? Cosa usa la scheda successiva? |
| Effetti | Documenti, attività o sistemi esterni modificati? Cosa simula il test? |
| Esempi | Quale configurazione e input completi producono ogni risultato? |
| Limiti e versioni | Dati assenti, limiti esatti e versioni precedenti? |

## Esempio compilato: Docfield is

**Tipo tecnico:** `condition_docfield_operator_value` · **Versione:** 2 · **Ruolo:** And. Richiede documento con layout definito e campo da controllare.

| Input | Configurazione |
| --- | --- |
| Field Name | `total_amount`, chiave tecnica e non etichetta tradotta |
| Operator | `gt` / Maggiore di |
| Field Value | `1000`, senza simbolo monetario |

La scheda confronta il campo del documento corrente con il valore configurato. Non cambia stato, non crea attività e non esporta. In Advanced, vero segue Success, falso segue Failed Condition ed errore di valutazione segue Error. In Standard, una condizione non soddisfatta interrompe la sequenza lineare.

Casi effettivamente verificati: **1785** → Success; **999** e **1000** → Failed Condition; **1000,01** → Success; numero assente o non valido → Error. JSON usa il punto decimale. Questi risultati descrivono questa configurazione numerica, non tutti i tipi e operatori.

Distinguere la scheda da quelle esplicite di tolleranza. Non dedurre uguaglianza o operatori inclusivi dal solo `gt`; verificare la combinazione necessaria con i propri limiti.

## Passi successivi

Collegare successo a revisione, falso al percorso standard ed errore alla correzione dei dati. Il [caso completo](advanced-workflow-case-study.md) presenta configurazione, schede successive e risultati reali. Il [modello di esecuzione](workflow-execution-model.md) spiega salvataggio e attivazione; la [diagnosi](workflow-troubleshooting.md) aiuta a indagare risultati diversi.

## WF-05: Esercizio e collaudo

Descrivere Run Workflow e una scheda PO con la stessa struttura: parametri, valori predefiniti esaminati, percorsi, effetti e versioni. Verificare destinazione inattiva, dati assenti e base percentuale.

[Percorso](workflow-learning-path.md)
