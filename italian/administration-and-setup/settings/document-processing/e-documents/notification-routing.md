# Instradamento delle notifiche

<figure><img src="../../../../.gitbook/assets/edoc_notification_routing.png" alt="Rotte di notifica"><figcaption><p>Assegnazione dei risultati di validazione agli agenti</p></figcaption></figure>

La pagina **Instradamento delle notifiche** (**Documenti elettronici → Azioni**) assegna i risultati di validazione agli **agenti AI Workforce**. Ogni risultato bloccante attiva esattamente un agente — quello il cui prefisso di codice corrisponde più a lungo. Tutto ciò che non corrisponde ricade sull'agente di notifica al fornitore predefinito.

## Rotte di notifica

Scegli chi gestisce ogni tipo di problema della fattura. Tutto ciò che non è elencato va all'agente predefinito:

| Rotta | Risultati coperti |
|-------|-------------------|
| **Regole aziendali colombiane** | Risultati delle regole aziendali specifiche della Colombia. |
| **Regole aziendali tedesche** | Risultati delle regole aziendali specifiche della Germania. |
| **Controlli IBAN / conto bancario** | Risultati sui dati di pagamento (checksum IBAN, lunghezza, paese). |
| **Controlli partita IVA** | Risultati sul formato della partita IVA. |
| **Tutto il resto** | Il fallback predefinito per tutto ciò che non corrisponde sopra. |

Per ogni rotta, scegli l'agente responsabile dal menu a discesa. **Avanzate (regole di codice personalizzate)** consente di instradare in base a un codice di risultato esatto quando serve un controllo più preciso.

## Agenti disponibili

<figure><img src="../../../../.gitbook/assets/edoc_notification_agents.png" alt="Registro degli agenti disponibili"><figcaption><p>Registro di sola lettura degli agenti AI Workforce</p></figcaption></figure>

La sezione **Agenti disponibili** è un registro di sola lettura degli agenti AI Workforce forniti con la tua installazione, ad esempio:

| Agente | Scopo |
|--------|-------|
| **Notifica fornitore predefinita** | E-mail generica di notifica al fornitore; l'agente jolly quando nessun agente più specifico corrisponde. |
| **Banking Bot** | Modello specializzato per i risultati sui dati di pagamento (correzioni IBAN/BIC). |
| **Tax Bot** | Notifica al fornitore specifica per la partita IVA. |
| **Compliance Bot** | Gestisce i risultati di conformità. |

Ogni agente mostra il proprio task Celery e i prefissi di codice di risultato che gestisce per impostazione predefinita.
