# Validazione delle fatture elettroniche

{% embed url="https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/einvoice-validation/v1/it.mp4" %}

La pagina **Validazione delle fatture elettroniche** (**Settings → E-Documents → E-Invoice Validation**, percorso `/settings/einvoice-validation`; in precedenza _Validation Rules_) controlla come DocBits valida le fatture elettroniche in ingresso. Si basa sul set di regole ufficiale **KoSIT XRechnung + ZUGFeRD** e sui codici di riscontro interni del validatore, e permette di sovrascrivere la gravità di ogni regola per la tua organizzazione.

> Questa pagina riguarda le **fatture elettroniche** (XRechnung, ZUGFeRD, Factur-X). Non è la stessa cosa di **Data Validation Rules**, che controllano i campi estratti dai documenti.

## Cosa c'è in questa pagina

<figure><img src="../../../../../.gitbook/assets/einvoice-validation-settings-it-20261104.png" alt="Validazione e blocco per tipo di documento. I nomi configurati sono nascosti. Esempio dell'ambiente di sviluppo."><figcaption><p>Validazione e blocco per tipo di documento. I nomi configurati sono nascosti. Esempio dell'ambiente di sviluppo.</p></figcaption></figure>

| Argomento | Cosa fa | Per chi |
| ----------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------- |
| [Configurazione della validazione e versioni accettate](validation-setup.md) | La procedura guidata, le versioni XRechnung accettate, i profili accettati e cosa significa ogni gravità. | Amministratori dell'organizzazione |
| [Gravità delle regole](validation-rule-severities.md) | La tabella delle regole: modificare la gravità di ogni regola per la tua organizzazione. | Amministratori dell'organizzazione |
| [Validazione per tipo di documento](validation-per-document-type.md) | Attivare la validazione (**Enabled**) e decidere se un controllo fallito blocca il documento (**Blocking**). Ogni modifica richiede una conferma. | Amministratori dell'organizzazione |
| [Registro delle modifiche](validation-change-log.md) | Ogni modifica delle impostazioni: quando, chi, quale regola, da → a. | Amministratori dell'organizzazione |
| [La schermata di errore di una fattura elettronica rifiutata](validation-error-screen.md) | Cosa vedi quando carichi un XML errato: la spiegazione, la riga difettosa e il passo successivo. | Tutti coloro che elaborano fatture |
| [Report di validazione](validation-report.md) | Cosa vede un utente quando una fattura fallisce: i riscontri in linguaggio chiaro. Si apre dal documento, non da questa pagina. | Tutti coloro che elaborano fatture |
| [Passo successivo e rifiuto di un documento](validation-next-step-and-reject.md) | Cosa fare dopo aver letto il report, i download del report e **Reject document**. | Tutti coloro che elaborano fatture |
