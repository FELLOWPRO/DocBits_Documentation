# Risoluzione dei problemi

## Non trovo Testing in Impostazioni

La pagina viene mostrata solo agli amministratori dell'organizzazione. Rivolgersi a un amministratore della propria organizzazione.

## La pagina indica che Testing è disattivato

Un amministratore dell'organizzazione deve attivare **Abilita Testing per l'organizzazione** nella parte superiore della pagina.
Fino ad allora non viene eseguito nulla, nemmeno da un assistente AI o dall'esterno.

## L'esecuzione non è riuscita

Aprire il log nella scheda **Log** e guardare il primo passaggio non riuscito e il suo codice di errore:

| Messaggio | Di solito significa | Che cosa fare |
|---|---|---|
| Un elemento non è stato trovato o non è visibile | La pagina appare diversa nella propria organizzazione oppure si carica lentamente | Aprire la pagina manualmente e controllarla; adattare il proprio modello oppure controllare i valori dell'input |
| Un campo o uno stato non corrisponde | Il documento ha un valore diverso da quello previsto dall'input | Controllare il documento; correggere il valore previsto nell'input |
| Impossibile aprire la pagina | ID documento errato oppure permesso mancante | Controllare l'ID nell'input e i permessi dell'utente che ha avviato la scheda |
| Tempo scaduto | Il passaggio o l'intero test ha richiesto troppo tempo | Eseguire di nuovo; se si ripete, controllare le prestazioni della pagina |
| Bloccato dall'ambiente | Il test scrive dati in un ambiente cliente | Confermare l'avvio oppure eseguirlo in un ambiente di test |

## L'esecuzione risulta "Bloccato"

L'esecuzione non ha potuto essere valutata: alcuni passaggi sono stati saltati (ad esempio un passaggio di screenshot, che il browser non può acquisire)
oppure manca una conferma. Un'esecuzione bloccata non viene mai conteggiata come superata. Rimuovere il passaggio dal proprio modello oppure
riavviarla con la conferma.

## "Per iniziare, registra una sessione del browser." / nessuna scheda accetta avvii

Gli avvii da un assistente AI o dall'esterno richiedono una scheda del browser con **Consenti avvii dall'esterno** attivato. Aprire
la scheda Input in una scheda che resta aperta, attivare l'opzione e utilizzare il relativo ID di sessione. Un ricaricamento termina la registrazione.

## L'esecuzione si è fermata o mostra Annullato / Non consegnabile

La scheda che eseguiva il test è stata ricaricata, chiusa o ha perso la connessione, oppure nessuna scheda ha risposto in tempo. Tenere la scheda aperta
e in primo piano fino al termine dell'esecuzione, poi avviare di nuovo. Un test con un passaggio **Ricarica pagina** termina allo stesso modo se la pagina non torna entro circa due minuti
(vedere [Ricaricare e riprendere](reload-and-resume.md)).

## "Non è ancora possibile avviare qui i modelli Playwright."

I modelli il cui **Esecutore** è **Playwright** vengono eseguiti dalla propria automazione dei test. È possibile salvare input per essi, ma non
avviarli da questa pagina.

## Non posso eliminare un modello

Si possono eliminare solo i modelli propri dell'organizzazione (**personalizzato**). I modelli integrati e predefiniti non possono essere eliminati; utilizzare
**Modifica una copia** per ottenere una versione propria.
