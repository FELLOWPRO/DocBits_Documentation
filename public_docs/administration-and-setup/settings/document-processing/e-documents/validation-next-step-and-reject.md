# Passo successivo e rifiuto di un documento

Dopo aver letto il [rapporto di convalida](validation-report.md), il rapporto ti dice cosa fare. Puoi anche rifiutare il documento.

## Cosa fare dopo

<figure><img src="../../../../.gitbook/assets/einvoice-report-next-step-it.png" alt="La fine del rapporto con la valutazione, il passo successivo e i pulsanti"><figcaption><p>La valutazione, il passo successivo e i pulsanti alla fine del rapporto</p></figcaption></figure>

La **Valutazione** dice in una frase se la fattura è conforme. Il blocco **Passo successivo** ti dice cosa fare:

| Risultato | Passo successivo |
| --- | --- |
| Almeno un **errore** | Chiedi al mittente una fattura corretta, oppure rifiuta il documento. Una fattura corretta è un nuovo documento. |
| Solo **avvertenze** | Puoi proseguire con il documento. |

I pulsanti alla fine del rapporto:

* **Rifiuta il documento**: apre la finestra di rifiuto (vedi sotto).
* **Rapporto (HTML)** e **Report (XML)**: scaricano il rapporto, ad esempio per inviarlo al fornitore.
* **Chiudi**: chiude il rapporto e ti riporta al documento.

## Rifiutare un documento

<figure><img src="../../../../.gitbook/assets/einvoice-reject-dialog-it.png" alt="La finestra Rifiuta il documento con il motivo compilato dal rapporto"><figcaption><p>Il motivo viene compilato dagli errori del rapporto. Puoi modificarlo.</p></figcaption></figure>

1. Nel rapporto, seleziona **Rifiuta il documento**.
2. Controlla il **Motivo**. DocBits lo compila dagli errori del rapporto. Puoi modificare il testo.
3. Seleziona **Rifiuta il documento** per confermare. Lo stato cambia in **Rifiutato**. Il motivo viene salvato come nota e il rapporto rimane associato al documento.

Seleziona **Annullamento** per lasciare il documento com'è.

> Solo gli utenti autorizzati a modificare i documenti vedono **Rifiuta il documento**. Il pulsante è nascosto quando il documento è già rifiutato o completato.
