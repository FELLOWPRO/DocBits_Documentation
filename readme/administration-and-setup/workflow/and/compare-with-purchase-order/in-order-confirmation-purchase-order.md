---
hidden: true
---

# Confrontare una conferma d'ordine con un ordine d'acquisto

Usa **Compare with Purchase Order** nel Workflow Builder quando una conferma d'ordine deve essere verificata rispetto al relativo ordine d'acquisto. Aggiungi la scheda sotto **And...**, quindi scegli i dati dell'ordine, un operatore e cosa deve accadere con il risultato. Gli screenshot qui sotto mostrano due versioni della scheda disponibili nell'interfaccia in inglese. I loro campi sono ancora segnaposto; impostali per il tuo workflow prima di salvare.

## Scrivere il risultato in un campo

<figure><img src="../../../../.gitbook/assets/dbdc-133-workflow-card-write-text.png" alt="Scheda Compare with Purchase Order nel Workflow Builder con i segnaposto Order Data, Operator, Text, Field Name e Result of condition." width="563"><figcaption>Versione 2: scrive un testo in un campo in base al risultato della condizione.</figcaption></figure>

Scegli gli **Order Data** della conferma d'ordine e un **Operator** per il confronto con l'ordine d'acquisto. Inserisci il **Text** da scrivere, seleziona il **Field Name** e scegli il **Result of condition** che deve attivare la scrittura.

## Confrontare i dati

<figure><img src="../../../../.gitbook/assets/dbdc-133-workflow-card-compare-as.png" alt="Scheda Compare with Purchase Order nel Workflow Builder con i segnaposto Any/All, Order Data, Operator e Comparison Data." width="563"><figcaption>Versione 4: confronta i dati selezionati della conferma d'ordine con i dati dell'ordine d'acquisto.</figcaption></figure>

Scegli **Any/All** per decidere se deve corrispondere una sola o tutte le condizioni selezionate. Quindi seleziona **Order Data**, **Operator** e **Comparison Data** per il confronto con l'ordine d'acquisto.

Per i passaggi correlati, consulta [Workflow](../../README.md) e [Compare with Purchase Order](README.md).
