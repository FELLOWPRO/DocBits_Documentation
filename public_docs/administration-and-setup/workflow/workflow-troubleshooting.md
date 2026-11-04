---
description: "Diagnosticare workflow mediante eventi, dati, percorsi scelti e risultati effettivi."
---

# Diagnosticare sistematicamente i problemi di workflow

Partire da una singola esecuzione interessata. Annotare organizzazione e ambiente, nome e revisione salvata, riferimento documentale, data e fuso orario e messaggio esatto del nodo. Nelle risposte di test usare anche `execution_id`. Escludere chiavi d’accesso e dati cliente non protetti dalle evidenze condivise.

## Dal sintomo alla verifica

| Sintomo | Evidenza da cercare | Correzione e nuovo test |
| --- | --- | --- |
| Nessuna esecuzione | Licenza, modulo, attivazione, filtri temporali ed evento | Correggere ingresso e filtri; ripetere l’evento reale. Start manuale non lo dimostra. |
| Azione grigia | Risultato del predecessore e uscita collegata | Seguire il percorso scelto. Un nodo saltato non è fallito autonomamente. |
| Condizione arancione | Chiave, tipo, valore e operatore letti | Distinguere risultato negativo ed errore. Provare sotto, sulla e sopra la soglia. |
| Nodo rosso | Primo errore e input necessari | Correggere dati o configurazione; ripetere caso fallito e positivo. |
| Wait ALL non prosegue | Ogni sorgente e la relativa uscita | Non richiedere insieme percorsi esclusivi. Dimostrare un percorso possibile per ogni sorgente necessaria. |
| Attività o esportazioni duplicate | Ripetizioni, eventi, cambi di stato e Run Workflow | Limitare condizioni e transizioni; eseguire due volte lo stesso caso. Valutare protezione dalla concorrenza nel processo destinatario. |
| Variabile che influenza altri workflow | Variabile organizzativa condivisa | Controllare dipendenze. La persistenza è indipendente dal canvas; riprovare i workflow interessati. |
| Test riuscito senza effetto | Cosa è stato confrontato o simulato | Verificare assegnazione sul documento, attività nella relativa area e ricezione a destinazione. Lo stato da solo non basta. |
| Esportazione avviata senza ricezione | Cronologia, risposta e dati del destinatario | Diagnosticare prima di ripetere; controllare se la prima richiesta è già stata elaborata. |

## Interpretare i messaggi

Nel [caso Advanced](advanced-workflow-case-study.md), un importo assente segue rosso verso la correzione. Gestore e unione OR possono riuscire mentre l’insieme conserva l’errore iniziale. Una condizione normalmente falsa segue arancione e può terminare correttamente sulla via standard.

Due collegamenti dalla stessa sorgente non sono due approvazioni indipendenti. Le unioni valutano i risultati collegati delle sorgenti. Controllare il flusso completo: un test parziale da un nodo intermedio può omettere predecessori necessari.

## Dimostrare la correzione

1. Conservare evidenza originale e aspettativa funzionale.
2. Modificare dati o configurazione in modo mirato. Cambiare l’aspettativa solo se cambia il requisito.
3. Ripetere errore, caso positivo e soglie interessate con il [pacchetto](workflow-training-kit.md).
4. Salvare la regola e verificarne separatamente l’attivazione.
5. Confrontare una nuova esecuzione reale con la precedente. I vecchi log descrivono la revisione originaria.

Registrare causa, correzione, risultato dimostrato e limiti residui. Separare attesa ed esecuzione: un tempo totale lungo non identifica da solo un nodo lento.

## WF-04: Esercizio e collaudo

Iniziare con invalid-number. Salvare il primo errore amount e risultato error. Ripetere con above e confrontare le prove. Conservare il vecchio errore; la gestione riuscita non basta.

[Percorso](workflow-learning-path.md)

## Ripetere i test di scheda con ambito esplicito

Nel designer Dev esaminato, ripetere un test avviato da un nodo selezionato è passato al grafo completo. Aprire nuovamente il test dal menu contestuale della scheda e controllare i nodi effettivamente visitati. Un risultato di sei nodi non dimostra un test isolato dello stato vuoto. Il contatore di azioni fallite può includere una condizione non soddisfatta: leggere anche uscita scelta, log e risultato complessivo.
