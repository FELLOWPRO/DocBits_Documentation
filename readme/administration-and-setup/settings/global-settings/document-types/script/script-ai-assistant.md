# Assistente AI nell'editor di script

L'editor di script dispone di un **Assistente AI** integrato che scrive e spiega gli script DocBits al posto vostro. Descrivete in linguaggio naturale cosa deve fare lo script e l'assistente risponde con codice Python che potete copiare nell'editor.

{% hint style="info" %}
L'Assistente AI fa parte di **DocNet**. La vostra organizzazione ha bisogno di un abbonamento DocNet attivo per utilizzarlo. Vedere [Piano di abbonamento](../../subscription-plan/README.md) e [Modulo](../../../document-processing/module/README.md).
{% endhint %}

## Aprire l'assistente

1. Andate su **Impostazioni → Tipi di Documento**, aprite il tipo di documento e cliccate su **Script**.
2. Cliccate su **Nuovo**, oppure aprite come bozza una versione di script esistente.
3. Cliccate sull'icona del robot accanto al nome dello script. Il pannello **Assistente AI** si apre sul lato destro dell'editor.

## Cosa conosce l'assistente

A ogni domanda DocBits invia all'assistente:

* il **riferimento di scripting** (le funzioni descritte in [Script in DocBits](scripting-in-docbits/README.md)),
* il **tipo di documento** dello script,
* lo **script attuale** dell'editor,
* i **nomi dei campi e delle colonne di tabella** che la vostra organizzazione utilizza per questo tipo di documento.

Grazie ai nomi dei campi, l'assistente utilizza i vostri campi reali, ad esempio `invoice_date` o `purchase_order`, in `get_field_value()` e `set_field_value()`.

## Scrivere uno script con l'assistente

1. Inserite la richiesta nella casella in fondo al pannello, ad esempio: *Imposta la valuta su EUR se è vuota.*
2. Premete **Invio** o cliccate sull'icona di invio. La risposta compare progressivamente.
3. Cliccate sull'icona di copia (suggerimento **Copia per l'editore**) accanto a un blocco di codice per inserire il codice nell'editor di script.
4. Controllate il codice, assegnate un nome allo script e salvatelo come bozza.

Le domande successive funzionano nello stesso pannello. Incollate un messaggio di errore oppure chiedete *Perché questo script non imposta la data di scadenza?* e l'assistente esamina lo script attuale nell'editor.

## Verificate sempre il risultato

{% hint style="warning" %}
L'assistente può commettere errori. Leggete il codice generato, verificate che i nomi dei campi corrispondano al vostro tipo di documento e testate lo script con un documento di prova prima di attivarlo. Vedere [Test degli script](testing-scripts.md).
{% endhint %}

Gli script vengono eseguiti solo con le funzioni di script consentite. Se uno script chiama una funzione che non esiste, DocBits lo rifiuta con il messaggio *Unknown function*.

## Utilizzo e limiti

* Ogni risposta mostra sotto il testo il numero di token utilizzati (input, output e totale).
* L'utilizzo viene registrato come utilizzo DocNet della vostra organizzazione.
* DocBits rifiuta la richiesta quando l'abbonamento DocNet manca (*DocNet subscription required*), è scaduto (*DocNet subscription expired*) oppure la quota è esaurita (*DocNet quota exhausted*).

## Pagine correlate

* [Creazione e modifica degli script](creating-and-editing-scripts.md)
* [Funzioni di Campo](scripting-in-docbits/field-functions.md)
* [Scripts de Ejemplo](scripting-in-docbits/sample-scripts/README.md)
* [Attivare e gestire gli script](script-activation-and-management.md)
