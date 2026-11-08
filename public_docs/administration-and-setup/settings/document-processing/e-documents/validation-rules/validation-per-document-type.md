# Validazione per ogni tipo di documento

Gli amministratori decidono, per ogni tipo di documento, se DocBits convalida le fatture elettroniche in entrata e se un controllo non superato blocca il documento. Ogni modifica viene confermata e registrata nel [registro delle modifiche](validation-change-log.md).

> Solo gli **amministratori dell'organizzazione** possono cambiare queste impostazioni. Gli altri utenti vedono la tabella in sola lettura oppure non la vedono.

## La tabella

Vai a **Settings → E-Documents → E-Invoice Validation**. La scheda **Rules and policy** inizia con la tabella **Validation for each document type**.

<figure><img src="../../../../../.gitbook/assets/einvoice-validation-settings-it-20261104.png" alt="Validazione e blocco per tipo di documento. I nomi configurati sono nascosti. Esempio su Dev."><figcaption><p>Validazione e blocco per tipo di documento. I nomi configurati sono nascosti. Esempio su Dev.</p></figcaption></figure>

| Interruttore | Cosa fa |
| --- | --- |
| **Enabled** | DocBits convalida ogni fattura elettronica in entrata di questo tipo di documento e salva un [rapporto di convalida](validation-report.md). |
| **Blocking** | Un risultato di tipo errore blocca il documento, che passa allo stato **Error**. Quando il blocco è disattivato, DocBits salva il rapporto e il documento prosegue. Puoi attivare **Blocking** solo quando **Enabled** è attivo. |

Se un tipo di documento ha sovrascritture per sottotipi, la tabella mostra una nota al riguardo.

## Cambiare un'impostazione

1. Seleziona l'interruttore che vuoi cambiare.
2. DocBits mostra **Confirm validation change** con il tipo di documento e la modifica, ad esempio *QUOTE: Abilitato → Attivo*.

<figure><img src="../../../../../.gitbook/assets/einvoice-validation-confirm-it.png" alt="Conferma di una modifica delle impostazioni. La modifica è stata annullata per questa schermata."><figcaption><p>Conferma di una modifica delle impostazioni. La modifica è stata annullata per questa schermata.</p></figcaption></figure>

3. Leggi la nota: **I report già salvati non vengono modificati.** La modifica si applica solo ai nuovi controlli, anche quando l'elaborazione di un documento viene riavviata.
4. Seleziona **Confirm change**, oppure **Cancel** per mantenere l'impostazione precedente.

Se non hai l'autorizzazione, DocBits mostra un messaggio che indica che serve un amministratore dell'organizzazione, e non cambia nulla.

## Pagine correlate

* [Validazione della fattura elettronica](./)
* [Registro delle modifiche](validation-change-log.md)
* [Configurazione della validazione e versioni accettate](validation-setup.md)
* [Rapporto di convalida](validation-report.md)
* [Attivare o disattivare la convalida delle fatture elettroniche](../#attivare-o-disattivare-la-convalida-delle-fatture-elettroniche)
