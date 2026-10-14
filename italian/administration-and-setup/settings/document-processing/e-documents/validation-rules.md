# Regole di validazione

<figure><img src="../../../../.gitbook/assets/edoc_validation_rules_setup.png" alt="Configurazione della validazione e versioni accettate"><figcaption><p>Configurazione della validazione e versioni XRechnung accettate</p></figcaption></figure>

La pagina **Regole di validazione** (**Documenti elettronici → Regole**) controlla come DocBits convalida le fatture elettroniche in entrata. Si basa sul set di regole ufficiale **KoSIT XRechnung + ZUGFeRD** più i codici di rilevamento interni del validatore, e ti consente di sovrascrivere la gravità di ogni regola per la tua organizzazione.

## Configurazione della validazione

La scheda **Configurazione della validazione** mostra il tuo profilo di validazione attuale (ad esempio *B2G — Public Sector Receiver*). Fai clic su **Modifica risposte** per rieseguire la procedura guidata di configurazione e cambiare lo standard rispetto al quale convalidi.

## Versioni XRechnung accettate

Il gate **Versioni XRechnung accettate** elenca tutte le versioni di XRechnung. Seleziona le versioni che accetti: i documenti il cui CustomizationID è fuori da questo elenco vengono rifiutati con `VAL-VERSION-NOT-ALLOWED` prima di qualsiasi altro controllo. Un elenco vuoto significa "accetta tutto". Ogni versione è contrassegnata come **current**, **deprecated** o **EOL** insieme alla sua data di rilascio.

## Profili accettati e modello di gravità

<figure><img src="../../../../.gitbook/assets/edoc_validation_rules_severity.png" alt="Profili accettati e legenda delle gravità"><figcaption><p>Profili accettati e significato di ciascuna gravità</p></figcaption></figure>

Scegli quali **profili** accettare (BASIC WL, BASIC, EN 16931 / COMFORT, EXTENDED, XRECHNUNG (CIUS)) tramite **Accetta tutto** / **Cancella**, quindi **Salva**.

Ogni regola di validazione ha una **gravità** che decide cosa succede quando si attiva:

| Gravità | Effetto |
|---------|---------|
| **FATAL** | Interrompe immediatamente l'elaborazione. Nessun livello successivo viene controllato; il documento passa in Errore. |
| **ERROR** | Il documento viene rifiutato. Gli altri rilevamenti dello stesso documento vengono comunque mostrati; la notifica al fornitore (se abilitata) viene attivata. |
| **WARNING** | Compare nel report di validazione, ma il documento prosegue normalmente nel flusso. |
| **INFO** | Solo log di audit. Nessun effetto visibile all'utente né rifiuto. |

## Sovrascrivere la gravità delle regole

<figure><img src="../../../../.gitbook/assets/edoc_validation_rules_table.png" alt="La tabella delle regole di validazione"><figcaption><p>La tabella completa delle regole con sovrascrittura della gravità per regola</p></figcaption></figure>

La tabella delle regole elenca tutte le regole di validazione (oltre 1.600 in totale). Filtra per **Livello (Layer)**, **Profilo** o **Versione**, oppure cerca per codice o campo. Per ogni regola puoi sovrascrivere la **Gravità** dal menu a discesa per adattarla alla policy della tua organizzazione — ad esempio, riducendo una regola da `ERROR` a `WARNING` in modo che non rifiuti più il documento.
