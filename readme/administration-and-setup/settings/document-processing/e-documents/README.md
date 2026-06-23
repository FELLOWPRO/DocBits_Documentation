# Documenti elettronici

DocBits convalida le fatture elettroniche in entrata (e-invoice) rispetto agli standard ufficiali — **XRechnung**, **ZUGFeRD** e **Factur-X** — e instrada eventuali problemi rilevati al gestore giusto. Il gruppo di impostazioni **Documenti elettronici** (in **Elaborazione dei documenti**) ha due pagine:

* **[Regole di validazione](validation-rules.md)**: scegli quali versioni e profili di fattura elettronica accetti e imposta la gravità di ogni regola di validazione per la tua organizzazione.
* **[Instradamento delle notifiche](notification-routing.md)**: assegna i risultati di validazione all'agente AI Workforce che deve gestirli.

Insieme ti permettono di decidere **cosa viene considerato un problema** su una fattura elettronica in entrata e **chi se ne occupa**.

## Attivare o disattivare la convalida delle fatture elettroniche

Le due pagine Documenti elettronici hanno effetto solo dopo che la **convalida delle fatture elettroniche è attivata per il tipo di documento**. L'interruttore si trova sul tipo di documento stesso, non nel menu Documenti elettronici.

Vai a **Impostazioni → Tipi di documento → Fattura → Impostazioni avanzate** e apri la sezione **Convalida fattura elettronica**.

<figure><img src="../../../../.gitbook/assets/edoc_enable_validation_toggle.png" alt="Gli interruttori di convalida della fattura elettronica sul tipo di documento Fattura"><figcaption><p>Attiva o disattiva la convalida delle fatture elettroniche per tipo di documento, con notifica facoltativa al fornitore</p></figcaption></figure>

* **Convalida le fatture elettroniche in entrata**: l'interruttore principale. Quando è **attivo**, ogni fattura caricata viene controllata con le regole Schematron KoSIT XRechnung più i controlli semantici L0 (PDF/A-3) e L4 (IBAN/IVA), usando le gravità impostate nella pagina [Regole di validazione](validation-rules.md). Le fatture non valide vengono bloccate. Quando è **disattivato**, le fatture saltano completamente la convalida delle fatture elettroniche e le pagine Regole di validazione e Instradamento delle notifiche non hanno effetto.
* **Notifica al fornitore in caso di rifiuto**: appare una volta attivata la convalida. Quando è **attivo**, una fattura rifiutata invia un'email al fornitore con l'elenco dei campi mancanti o errati così da poterla riemettere. Chi riceve e gestisce ogni risultato si configura nella pagina [Instradamento delle notifiche](notification-routing.md).

> La convalida delle fatture elettroniche si configura **per tipo di documento**. Attualmente si applica al tipo di documento **Fattura**; attivala su ogni tipo di documento da convalidare.

Puoi anche saltare direttamente qui con la **ricerca rapida globale**: premi <kbd>Cmd</kbd> + <kbd>K</kbd> (<kbd>Ctrl</kbd> + <kbd>K</kbd> su Windows e Linux) ovunque in DocBits e digita *e-invoice*.

<figure><img src="../../../../.gitbook/assets/edoc_quicksearch_einvoice.png" alt="La ricerca rapida globale apre la Convalida fattura elettronica"><figcaption><p>Digita «e-invoice» nella ricerca rapida per saltare direttamente all'interruttore.</p></figcaption></figure>
