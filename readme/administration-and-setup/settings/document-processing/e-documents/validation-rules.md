# Validazione della fattura elettronica

La pagina **Validazione della fattura elettronica** (**Impostazioni → Documenti elettronici → Validazione della fattura elettronica**, percorso `/settings/einvoice-validation`; in precedenza chiamata *Regole di validazione*) controlla come DocBits convalida le fatture elettroniche in entrata. Si basa sul set di regole ufficiale **KoSIT XRechnung + ZUGFeRD** più i codici di rilevamento interni del validatore, e ti consente di sovrascrivere la gravità di ogni regola per la tua organizzazione.

> Questa pagina riguarda le **fatture elettroniche** (XRechnung, ZUGFeRD, Factur-X). Non è la stessa cosa delle **Regole di validazione dei dati**, che controllano i campi estratti dai documenti.

## Cosa trovi in questa pagina

<figure><img src="../../../../.gitbook/assets/einvoice-validation-settings-it.png" alt="La pagina Validazione della fattura elettronica con la tabella Validazione per ogni tipo di documento"><figcaption><p>La pagina Validazione della fattura elettronica. La scheda <strong>Regole e politiche</strong> inizia con la tabella <strong>Validazione per ogni tipo di documento</strong>. Organizzazione di esempio.</p></figcaption></figure>

| Argomento | Cosa fa | Per chi |
| --- | --- | --- |
| [Configurazione della validazione e versioni accettate](validation-setup.md) | La procedura guidata di configurazione, le versioni XRechnung accettate, i profili accettati e il significato di ogni gravità. | Amministratori dell'organizzazione |
| [Gravità delle regole](validation-rule-severities.md) | La tabella delle regole: cambia la gravità di ogni regola per la tua organizzazione. | Amministratori dell'organizzazione |
| [Validazione per ogni tipo di documento](validation-per-document-type.md) | Attiva la validazione (**Abilitato**) e decidi se un controllo non superato blocca il documento (**Blocco**). Ogni modifica richiede una conferma. | Amministratori dell'organizzazione |
| [Registro delle modifiche](validation-change-log.md) | Ogni modifica delle impostazioni: quando, chi, quale regola, da → a. | Amministratori dell'organizzazione |
| [La schermata di errore per una fattura elettronica rifiutata](validation-error-screen.md) | Cosa vedi quando carichi un XML errato: la spiegazione, la riga errata e il passo successivo. | Chiunque elabora fatture |
| [Rapporto di convalida](validation-report.md) | Cosa vede un utente quando una fattura non supera il controllo: i risultati in linguaggio semplice. Si apre dal documento, non da questa pagina. | Chiunque elabora fatture |
| [Passo successivo e rifiuto di un documento](validation-next-step-and-reject.md) | Cosa fare dopo aver letto il rapporto, il download del rapporto e **Rifiuta il documento**. | Chiunque elabora fatture |
