---
hidden: true
---

# Supplier on Invoice

<figure><img src="../../../../.gitbook/assets/image (1) (1) (2).png" alt=""><figcaption></figcaption></figure>

## **Scopo**

Questa scheda DocBits consente un confronto dettagliato, confrontando il fornitore della fattura con quello della conferma d'ordine. Si dovrebbe garantire che il fornitore che ha emesso la fattura sia lo stesso indicato nella conferma d'ordine.

## **Funzionalità:**

* **Supplier on Invoice Supplier on Purchase Order:** Questa scheda verifica se il fornitore nella fattura è lo stesso indicato nella conferma d'ordine oppure no.
* **Valore dell'operatore:** Gli utenti possono impostare condizioni specifiche come: se il fornitore che ha emesso la fattura è lo stesso indicato nel PO oppure no. Gli operatori disponibili includono:
  * **Is (=):** Verifica se il fornitore nella fattura corrisponde al fornitore nella conferma d'ordine.
  * **Is not (≠):** Garantisce che il fornitore che ha emesso la fattura sia lo stesso indicato nella conferma d'ordine.

## **Utilizzo:**

Questa scheda è utile per garantire che l'intero processo venga gestito con lo stesso fornitore e che tutto sia coerente. Ciò assicura che, in presenza di discrepanze, l'attenzione venga rivolta alla verifica di tali discrepanze, evitando di pagare la fattura a un fornitore errato che non ha nulla a che fare con l'ordine e la conferma d'ordine.

## **Scenario di esempio:**

* Viene effettuato un ordine, poi arriva la conferma d'ordine e quindi viene emessa la fattura. L'intero processo di ordinazione viene eseguito con un unico fornitore. Se così non fosse, la scheda può determinare immediatamente che esistono discrepanze tra i fornitori e garantisce così che non vengano effettuati pagamenti errati e che la fattura sia gestita solo con il fornitore che è stato anche coinvolto nell'intero processo.

Utilizzando la scheda "Supplier on Invoice … Supplier on Purchase Order", le aziende possono automatizzare la verifica dei fornitori che emettono le fatture e delle conferme d'ordine associate.
