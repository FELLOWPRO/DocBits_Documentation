# Date or Time

<figure><img src="../../../../.gitbook/assets/image (5) (1) (1) (1) (1) (1).png" alt="" width="563"><figcaption></figcaption></figure>

## **Scopo:**

Questa scheda DocBits verifica se un valore data/ora specificato rientra in un intervallo definito. Consente ai workflow di proseguire o arrestarsi a seconda che la condizione sia soddisfatta, rendendola adatta a operazioni sensibili al tempo o alla pianificazione dei workflow.

## **Funzionalità:**

* **Validazione data/ora:** Questa scheda valuta se una determinata data/ora rientra in un intervallo specificato utilizzando le seguenti condizioni:
  * **Is:** Verifica se la data/ora rientra nell'intervallo definito di inizio e fine (inclusi).
  * **Is Not:** Garantisce che la data/ora ricada al di fuori dell'intervallo definito.

**Intervallo data/ora:** Gli utenti specificano i valori di data/ora di inizio e fine per definire l'intervallo di confronto.

## **Utilizzo:**

Questa scheda è ideale per la pianificazione, i controlli di conformità o la validazione di condizioni basate sul tempo nei workflow. Ad esempio, può essere utilizzata per garantire che le attività vengano eseguite solo durante intervalli temporali predefiniti o per verificare le scadenze.

## **Scenario di esempio:**

* Un utente configura la scheda per verificare se la **data di invio** di una fattura **è compresa tra** **"2024-11-01"** e **"2024-11-30"**. Se la data di invio rientra in questo intervallo, il workflow procede all'elaborazione del pagamento. In caso contrario, il workflow attiva una notifica per un'ulteriore revisione.

Utilizzando la scheda "Date/Time Range Validation", le organizzazioni possono garantire una pianificazione accurata, migliorare la conformità e semplificare i workflow aderendo a vincoli temporali predefiniti.
