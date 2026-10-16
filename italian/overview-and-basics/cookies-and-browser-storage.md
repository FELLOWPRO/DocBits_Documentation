# Cookie e archiviazione del browser

Verificato il **16 ottobre 2026**. Il sito pubblico, l'applicazione DocBits e questa documentazione utilizzano cookie e servizi differenti.

## Informativa e finalità

L'[Informativa sulla privacy di DocBits](https://docbits.com/en/privacy-policy/) contiene le sezioni **Cookies** e **Consent with Borlabs Cookie**. Descrive consenso, funzioni essenziali, protezione dai bot, Google Analytics, pubblicità e Leadfeeder. Le analisi possono produrre report su visite, pagine, interazioni e prestazioni, ma la raccolta non si limita a dati anonimi aggregati. L'informativa del sito non determina da sola l'inventario dell'applicazione.

## Inventario dei cookie

**Osservato** indica una nuova visita senza accesso né scelta di consensi facoltativi. **Codice** indica codice o impostazioni infrastrutturali esaminati e non conferma gli attributi di ogni risposta in produzione.

| Cookie / ambito | Finalità e durata | Evidenza e attributi di sicurezza |
| --- | --- | --- |
| `__cf_bm` / sito e app | Protezione Cloudflare dai bot; 30 minuti di inattività | Osservato: `Secure`, `HttpOnly`, `SameSite=None`. [Cloudflare](https://developers.cloudflare.com/fundamentals/reference/policies-compliances/cloudflare-cookies/) cifra le informazioni sui bot, escluse quelle temporali. |
| `pll_language` / sito | Preferenza linguistica; circa un anno | Osservato: `Secure`, leggibile da JavaScript, `SameSite=Lax`. |
| `_lfa` / sito | Analisi Leadfeeder di visitatori e aziende; circa un anno | Osservato: leggibile da JavaScript, `SameSite=Lax`, **senza attributo `Secure`** in questa visita. |
| Cookie di consenso Borlabs / sito | Memorizza consensi e revoche | Dichiarato nell'informativa; nome, attributi effettivi e durata non verificati in questa visita. |
| `session` / autenticazione | Stato di sessione nei flussi di autenticazione | Valori predefiniti del codice: `Secure`, `HttpOnly`, `SameSite=None`; dati di sessione Flask firmati, non cifrati. Il deployment può modificarli. |
| `dbx_td` / autenticazione | Ricorda un dispositivo attendibile, se scelto dopo MFA riuscita; 30 giorni | Codice: `Secure`, `HttpOnly`, `SameSite=None`; token casuale il cui hash è conservato sul server. |
| `prod-sticky` / bilanciamento in produzione | Inoltra richieste allo stesso backend; durata configurata di 300 secondi | Impostazione infrastrutturale verificata; attributi del browser non verificati. |
| `dontAsk` / app | Memorizza una preferenza per un avviso; nessuna scadenza esplicita nella chiamata esaminata | Codice: leggibile da JavaScript; nessuna opzione esplicita `Secure` o `SameSite` in quella chiamata. |

Nessun cookie è stato osservato in una nuova visita alla documentazione. È una rilevazione datata, non l'inventario completo di flussi autenticati, funzionalità facoltative o contenuti esterni incorporati. L'informativa cita ulteriori servizi analitici/pubblicitari i cui cookie non sono stati confermati. Inventario completo e gestione del consenso richiedono verifiche separate di tali flussi.

## Sicurezza e analisi

`Secure` limita l'invio a HTTPS. `HttpOnly` impedisce la lettura da JavaScript. `SameSite` controlla l'invio tra siti. Questi attributi non cifrano il contenuto. Non è corretto dichiarare che tutti i cookie siano cifrati o protetti allo stesso modo. Gli endpoint pubblici supportano TLS 1.2 e 1.3; vedere [Archiviazione sicura delle credenziali](secure-storage-of-credentials.md).

L'archiviazione del browser è usata anche indipendentemente dai cookie. La configurazione Grafana Faro prevede tracciamento persistente delle sessioni, errori, misurazioni delle prestazioni e tracce, con identificativi di utente e organizzazione quando disponibili. La raccolta dipende dalla configurazione del collettore distribuito. Non va descritta come sola analisi anonima e aggregata dei cookie. Anche le preferenze linguistiche usano l'archiviazione locale.

È possibile eliminare cookie e archiviazione dal browser; ciò può rimuovere preferenze e riconoscimento dei dispositivi attendibili. Per un inventario aggiornato o domande sulla privacy: **compliance@fellowpro.com**.
