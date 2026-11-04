# Conferma dell'Ordine d'Acquisto

### Confronto con l'Ordine d'Acquisto:&#x20;

**Conferma dell'Ordine d'Acquisto**

<figure><img src="https://lh7-us.googleusercontent.com/glQHETatKah-1YugeLqBb7Jim6lNJxuarRv-KEMv4NPzFfcjSm6mVhTMdI30nxdJ0SHXZ55Oup6KH7K-J6IxjUOiG0wxUX8toAaCopgBJwPyr94CPjoKuauNTmoHGGhg6f3gwHD39W7gpvijg4LQVJ4" alt="" width="563"><figcaption></figcaption></figure>

#### Scheda Logica: Corrispondenza Quantità o Prezzo Unitario o Sconto

Questa scheda logica è progettata per verificare automaticamente che la quantità, il prezzo unitario o lo sconto dettagliati in una conferma d'ordine corrispondano alle cifre corrispondenti nell'ordine d'acquisto. Questa verifica garantisce coerenza e precisione tra ciò che è stato ordinato e ciò che il fornitore conferma di consegnare.

#### Condizione di Attivazione

La logica viene attivata quando una delle seguenti condizioni è soddisfatta in una conferma d'ordine rispetto all'ordine d'acquisto originale:

* **Quantità**: La quantità di articoli ordinati corrisponde alla quantità confermata dal fornitore.
* **Prezzo Unitario**: Il prezzo per articolo concordato corrisponde alla conferma del fornitore.
* **Sconto**: Eventuali sconti applicati sono coerenti tra l'ordine d'acquisto e la conferma d'ordine.

#### Risultati

* **Uguale**: Se la quantità, il prezzo unitario o lo sconto della conferma d'ordine corrispondono esattamente all'ordine d'acquisto, il sistema considera la conferma valida e procede con i passaggi successivi nel processo di approvvigionamento.
* **Non Uguale**: Se c'è una discrepanza nella quantità, nel prezzo unitario o nello sconto, il sistema contrassegna la conferma d'ordine per una revisione manuale. Ciò garantisce che eventuali discrepanze siano risolte prima di procedere.

#### Benefici

* **Precisione e Coerenza**: Mantiene l'accuratezza nel processo di approvvigionamento, garantendo che i pagamenti e le consegne siano effettuati sulla base di cifre corrette.
* **Efficienza**: Automatizza il processo di verifica, riducendo la necessità di controlli manuali e accelerando l'elaborazione degli ordini.
* **Controllo dei Costi**: Aiuta a prevenire sovrapagamenti o consegne errate individuando le discrepanze all'inizio del processo.

<figure><img src="https://lh7-us.googleusercontent.com/DRTMJxJ9XLeC5zWSU8QuZwPLkqHzmCUm9RwiUZIkcc8pVxMZsxLv56dX9spzqr7KeDkTigbeBX2DvAZRe-6MdqOgAnrO-QPnCbi4e6hP4--P_O0A0DSoQJxjGeefOS1p6GuXHs1YXv-A73DXYaE8qlI" alt="" width="563"><figcaption></figcaption></figure>

1. **Definire i Parametri di Confronto**: Impostare i campi specifici (quantità, prezzo unitario, sconto) che la scheda logica controllerà per una corrispondenza.
2. **Automatizzare la Verifica**: Configurare il sistema per confrontare automaticamente questi dettagli al ricevimento di una conferma d'ordine.
3. **Personalizzare gli Avvisi**: Decidere il flusso di lavoro per gestire le discrepanze, inclusa la personalizzazione degli avvisi per la revisione manuale.

Questa scheda logica è fondamentale per garantire che i dettagli di una conferma d'ordine siano in linea con l'ordine d'acquisto originale, salvaguardando l'integrità del ciclo di approvvigionamento. \`\`
