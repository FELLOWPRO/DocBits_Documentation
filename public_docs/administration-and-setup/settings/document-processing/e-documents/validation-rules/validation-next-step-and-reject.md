# Passo successivo e rifiuto di un documento

> In questa versione alcuni testi dell’interfaccia possono essere ancora in inglese o tradotti in modo errato. La guida ne spiega il significato; le schermate mostrano l’interfaccia originale.

Dopo aver letto il [rapporto di convalida](validation-report.md), il rapporto ti dice cosa fare. Puoi anche rifiutare il documento.

## Cosa fare dopo

<figure><img src="../../../../../.gitbook/assets/einvoice-report-next-step-it-20261104-v2.png" alt="Valutazione, passo successivo e azioni del rapporto."><figcaption><p>Valutazione, passo successivo e azioni del rapporto.</p></figcaption></figure>

La **Valutazione** dice in una frase se la fattura è conforme. Il blocco **Passo successivo** ti dice cosa fare:

| Risultato | Passo successivo |
| --- | --- |
| Almeno un **errore** | Chiedi al mittente una fattura corretta, oppure rifiuta il documento. Una fattura corretta è un nuovo documento. |
| Solo **avvertenze** | Puoi proseguire con il documento. |

I pulsanti alla fine del rapporto:

* **Rifiuta il documento**: apre la finestra di rifiuto (vedi sotto).
* **Rapporto (HTML)** e **Rapporto (XML)**: scaricano il rapporto, ad esempio per inviarlo al fornitore.
* **Chiudi**: chiude il rapporto e ti riporta al documento.

## Rifiutare un documento

<figure><img src="../../../../../.gitbook/assets/einvoice-reject-dialog-it-20261104-v2.png" alt="Finestra di rifiuto della fattura fittizia. Il rifiuto è stato annullato."><figcaption><p>Finestra di rifiuto della fattura fittizia. Il rifiuto è stato annullato.</p></figcaption></figure>

1. Nel rapporto, seleziona **Rifiuta il documento**.
2. Controlla il **Motivo**. DocBits lo compila dagli errori del rapporto. Puoi modificare il testo.
3. Seleziona **Rifiuta il documento** per confermare. Lo stato cambia in **Rifiutato**. Il motivo viene salvato come nota e il rapporto rimane associato al documento.

Seleziona **Annulla** per lasciare il documento com'è.

> Solo gli utenti autorizzati a modificare i documenti vedono **Rifiuta il documento**. Il pulsante è nascosto quando il documento è già rifiutato o completato.
