---
hidden: true
---

# In Order Confirmation Purchase Order

### Confronto con l'ordine d'acquisto:

**In Order Confirmation Purchase Order**

<figure><img src="https://lh7-us.googleusercontent.com/glQHETatKah-1YugeLqBb7Jim6lNJxuarRv-KEMv4NPzFfcjSm6mVhTMdI30nxdJ0SHXZ55Oup6KH7K-J6IxjUOiG0wxUX8toAaCopgBJwPyr94CPjoKuauNTmoHGGhg6f3gwHD39W7gpvijg4LQVJ4" alt="" width="563"><figcaption></figcaption></figure>

#### Scheda Logic: Corrispondenza di Quantità, Prezzo unitario o Sconto

Questa scheda logica è progettata per verificare automaticamente che la quantità, il prezzo unitario o lo sconto indicati in una conferma d'ordine corrispondano alle cifre corrispondenti nell'ordine d'acquisto. Questa verifica garantisce coerenza e accuratezza tra ciò che è stato ordinato e ciò che il fornitore conferma di consegnare.

#### Condizione di attivazione

La logica viene attivata quando una qualsiasi delle seguenti condizioni è soddisfatta in una conferma d'ordine rispetto all'ordine d'acquisto originale:

* **Quantity**: La quantità degli articoli ordinati corrisponde alla quantità confermata dal fornitore.
* **Unit Price**: Il prezzo per articolo concordato corrisponde alla conferma del fornitore.
* **Discount**: Eventuali sconti applicati sono coerenti tra l'ordine d'acquisto e la conferma d'ordine.

#### Esiti

* **Equals**: Se la quantità, il prezzo unitario o lo sconto della conferma d'ordine corrispondono esattamente all'ordine d'acquisto, il sistema considera la conferma valida e procede con i passaggi successivi del processo di approvvigionamento.
* **Not Equal**: Se c'è una discrepanza nella quantità, nel prezzo unitario o nello sconto, il sistema segnala la conferma d'ordine per la revisione manuale. Ciò garantisce che eventuali discordanze vengano risolte prima di procedere.

#### Vantaggi

* **Accuratezza e coerenza**: Mantiene l'accuratezza nel processo di approvvigionamento, garantendo che i pagamenti e le consegne avvengano in base a cifre corrette.
* **Efficienza**: Automatizza il processo di verifica, riducendo la necessità di controlli manuali e accelerando l'elaborazione degli ordini.
* **Controllo dei costi**: Aiuta a prevenire pagamenti in eccesso o consegne errate intercettando precocemente le discrepanze nel processo.

<figure><img src="https://lh7-us.googleusercontent.com/DRTMJxJ9XLeC5zWSU8QuZwPLkqHzmCUm9RwiUZIkcc8pVxMZsxLv56dX9spzqr7KeDkTigbeBX2DvAZRe-6MdqOgAnrO-QPnCbi4e6hP4--P_O0A0DSoQJxjGeefOS1p6GuXHs1YXv-A73DXYaE8qlI" alt="" width="563"><figcaption></figcaption></figure>

1. **Definire i parametri di confronto**: Imposta i campi specifici (quantità, prezzo unitario, sconto) che la scheda logica verificherà per individuare una corrispondenza.
2. **Automatizzare la verifica**: Configura il sistema per confrontare automaticamente questi dettagli al ricevimento di una conferma d'ordine.
3. **Personalizzare gli avvisi**: Decidi il workflow per la gestione delle discrepanze, inclusa la personalizzazione degli avvisi per la revisione manuale.

Questa scheda logica è fondamentale per garantire che i dettagli di una conferma d'ordine siano allineati all'ordine d'acquisto originale, salvaguardando l'integrità del ciclo di approvvigionamento. \`\`
