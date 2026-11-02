# Correggere un errore OCR in un numero d'ordine

Il terzo carattere di `06O123` è la **lettera O**. Se l'estrazione produce `060123`, utilizzate una trasformazione condizionale del prefisso per correggere questo schema noto senza uno script personalizzato.

## Configurare la correzione del prefisso

1. Aprite **Impostazioni → Tipi di documento → ingranaggio → Regole di trasformazione → Gestisci regole di trasformazione**. Un amministratore dell'organizzazione deve attivare la funzione per il tipo selezionato.
2. Create una regola per un **campo di intestazione** con **Numero d'ordine (`Purchase Order`)** come destinazione. Leggete dal **campo stesso**.
3. Per l'esecuzione condizionale, selezionate il numero d'ordine, **inizia con** e `060`.
4. Rimuovete il passaggio iniziale di eliminazione degli spazi. Aggiungete **Affisso → Rimuovi prefisso → `060`**, poi **Affisso → Aggiungi prefisso → `06O`**. Nel secondo passaggio inserite la O maiuscola. La condizione limita entrambe le operazioni al prefisso interessato; gli altri caratteri restano invariati.
5. Verificate l'anteprima, salvate la regola e riapritela. Provate un documento, salvatelo e ricaricatelo per verificare il numero d'ordine memorizzato.

## Verificare il risultato

| Esempio di input | Risultato atteso | Motivo |
| --- | --- | --- |
| `060123` | `06O123` | Prefisso interessato |
| `060987` | `06O987` | Altro valore interessato; suffisso conservato |
| `06O123` | `06O123` | Già corretto; condizione non soddisfatta |
| `160123` | `160123` | Prefisso diverso; condizione non soddisfatta |
| `1060123` | `1060123` | `060` all'interno del valore non è un prefisso corrispondente |

L'esempio corregge uno schema di estrazione noto. Non dimostra la precisione OCR, l'esistenza dell'ordine o la riuscita dell'abbinamento. Usate la regola solo se la convenzione di numerazione richiede `06O`: verrebbe modificato anche un prefisso `060` legittimo. Aggiungete condizioni sul fornitore quando la convenzione riguarda solo alcuni fornitori.

## Perché due passaggi di affisso?

L'editor attuale richiede un campo di origine separato per passaggi dipendenti dalla posizione, come **Trova e sostituisci**, anche con **Esegui una sola volta per documento** attivo. I due passaggi del prefisso funzionano sullo stesso campo. Dopo la correzione, il valore non inizia più con `060`, quindi la condizione evita altre modifiche ai salvataggi successivi.
