# Attività e notifiche

### Panoramica

L'impostazione **Attività e notifiche** (Tasks & Notifications) attiva la gestione delle attività integrata in DocBits. Quando è attivata, i membri del team possono creare attività, assegnarsi documenti a vicenda (ad esempio per validazione, correzione o approvazione) e ricevere notifiche al riguardo.

Questa impostazione è **disattivata per impostazione predefinita**. Quando è attivata, sotto di essa compaiono altre quattro opzioni:

* **Conteggio attività nel cruscotto**: mostra nel cruscotto quali documenti hanno attività aperte.
* **Consenti il filtro "Tutti" per gli utenti non amministratori**: permette agli utenti che non sono amministratori di vedere tutte le attività.
* **Eliminazione attività da parte di non amministratori**: stabilisce quali attività possono eliminare gli utenti che non sono amministratori.
* **Completamento attività da parte di non amministratori**: stabilisce quali attività possono chiudere gli utenti che non sono amministratori.

Queste opzioni non limitano mai gli amministratori dell'organizzazione.

### Cosa fa?

* **Attivata** — Le funzioni Attività e notifiche diventano disponibili in DocBits. Gli utenti possono assegnare attività, monitorarne lo stato e ricevere notifiche quando qualcosa richiede la loro attenzione.
* **Disattivata** — L'assegnazione delle attività e le notifiche correlate vengono disattivate. La disattivazione disattiva anche **Conteggio attività nel cruscotto**.

### Conteggio attività nel cruscotto
L'opzione **Conteggio attività nel cruscotto** stabilisce se il cruscotto indica quali documenti hanno attività aperte. Non si tratta di un contatore complessivo: l'indicazione compare per ogni singolo documento.

* **Attivata** — Un documento con attività nello stato **Aperto** o **In corso** mostra un'icona delle attività nell'elenco del cruscotto. Passando il mouse sopra l'icona viene mostrato quante attività aperte ha il documento, ad esempio "2 Attività aperte". Le attività completate, rifiutate o eliminate non vengono conteggiate.
* **Disattivata** — L'icona viene nascosta. Le attività continuano a funzionare normalmente.

{% hint style="info" %}
**Conteggio attività nel cruscotto** dipende da **Attività e notifiche**. Se disattivi Attività e notifiche, viene disattivata anche l'indicazione delle attività nel cruscotto.
{% endhint %}

### Consenti il filtro "Tutti" per gli utenti non amministratori

La panoramica delle attività ha un filtro **Assegnato a** con le opzioni **Tutti** e **Assegnato a me**. Gli amministratori dispongono sempre di entrambe le opzioni.

* **Attivata** — Anche gli utenti che non sono amministratori possono scegliere **Tutti** e vedere tutte le attività dell'organizzazione.
* **Disattivata** (predefinito) — Gli utenti che non sono amministratori dispongono solo di **Assegnato a me**, quindi la panoramica mostra le attività assegnate a loro.

### Eliminazione attività da parte di non amministratori
**Eliminazione attività da parte di non amministratori** stabilisce quali attività e notifiche possono eliminare gli utenti che non sono amministratori. Gli amministratori possono sempre eliminare tutte le attività.

| Opzione | Gli utenti non amministratori possono eliminare |
| --- | --- |
| **Nessuna** | Nessuna attività. |
| **Solo attività create** | Le attività che hanno creato. |
| **Attività create e assegnate** | Le attività che hanno creato e quelle assegnate a loro o a uno dei loro gruppi. Questa regola vale finché l'opzione non è mai stata modificata. |
| **Tutte le attività** | Tutte le attività. |

Gli utenti possono sempre eliminare le attività che hanno creato, tranne con **Nessuna**. Un'attività non assegnata a nessuno può quindi essere eliminata solo dall'utente che l'ha creata, dagli amministratori o con **Tutte le attività**. Un'attività di cui non è registrato chi l'ha creata, ad esempio una creata dal sistema, può essere eliminata solo dagli utenti a cui è assegnata (con **Attività create e assegnate**), dagli amministratori o con **Tutte le attività**.

{% hint style="warning" %}
Eliminare un'attività la rimuove dall'elenco delle attività senza che venga presa una decisione. Se le attività devono essere chiuse solo tramite una decisione, imposta **Eliminazione attività da parte di non amministratori** su **Nessuna** e **Completamento attività da parte di non amministratori** (vedi sotto) su **Solo per amministratori**.
{% endhint %}

### Completamento attività da parte di non amministratori
**Completamento attività da parte di non amministratori** stabilisce quali utenti non amministratori possono chiudere un'attività, cioè impostarla su **Fatto** o **Rifiutato**. Gli amministratori possono sempre chiudere le attività, qualunque sia l'opzione selezionata.

| Opzione | Chi può chiudere un'attività |
| --- | --- |
| **Comportamento predefinito** | L'impostazione non aggiunge alcuna restrizione. Gli utenti possono chiudere le attività assegnate a loro o a uno dei loro gruppi, come prima che l'impostazione esistesse. Questa regola vale finché l'opzione non è mai stata modificata. |
| **Amministratori e utenti assegnati** | Gli amministratori e gli utenti a cui l'attività è assegnata, direttamente o tramite uno dei loro gruppi. Un'attività assegnata a qualcun altro, o a nessuno, non può essere chiusa dagli altri utenti. DocBits verifica questa regola anche quando un'attività viene modificata tramite l'API. |
| **Solo per amministratori** | Solo gli amministratori. |

Con **Amministratori e utenti assegnati** o **Solo per amministratori**, un utente che non può chiudere un'attività:

* non vede il pulsante verde **Fatto** nella pagina dell'attività, e l'elenco degli stati offre solo **Aperto** e **In corso**;
* non può fare clic sul cerchio di stato dell'attività nel pannello delle attività del documento. Passando il mouse sopra compare il messaggio "Non è consentito contrassegnare questa attività come completata o rifiutata.";
* non vede **Contrassegnare come fatto** per quell'attività nell'elenco delle attività, e **Contrassegnare come fatto** per una selezione resta nascosto finché è selezionata un'attività di questo tipo;
* non può trascinare l'attività nella colonna **Fatto** o **Rifiutato** della bacheca delle attività. La scheda torna nella sua colonna e viene mostrato lo stesso messaggio.

L'impostazione limita solo la chiusura. Gli utenti mantengono tutti gli altri diritti che avevano prima: gli utenti a cui un'attività è assegnata possono comunque modificarla, salvarla, spostarla tra **Aperto** e **In corso** e riaprirla dopo che è stata completata. Gli utenti a cui un'attività non è assegnata non potevano cambiarne lo stato prima, e continuano a non poterlo fare.

Per i tipi di documento con **Storia dell'approvazione** attivata, **Approvare** completa comunque attività aperte del documento, qualunque sia l'opzione selezionata qui: le attività assegnate all'approvatore o a uno dei suoi gruppi, e le attività non assegnate a nessuno. Se l'approvatore è un amministratore, vengono completate tutte le attività aperte del documento.

#### Attività sui documenti rimandati alla validazione

Poiché con **Amministratori e utenti assegnati** o **Solo per amministratori** gli utenti non possono chiudere da soli le proprie attività, quando un documento in attesa di approvazione viene rimandato alla validazione è DocBits stesso a chiudere le attività aperte del documento:

* **Riavviare il flusso di lavoro** nella schermata di approvazione: tutte le attività aperte del documento vengono rifiutate.
* **Rifiutare e correggere**: tutte le attività aperte del documento vengono rifiutate.
* **Approvare e correggere**: vengono completate le attività che **Approvare** completerebbe (vedi sopra), solo per i tipi di documento con **Storia dell'approvazione** attivata. Tutte le altre attività aperte vengono rifiutate.

Le attività aperte vengono chiuse prima che il documento torni alla validazione. I workflow avviati dal cambio di stato possono poi creare nuove attività per tutto ciò che richiede ancora attenzione.

Con **Comportamento predefinito**, le attività aperte restano aperte quando un documento viene rimandato indietro, come in precedenza.

### Vantaggi

* **Responsabilità chiare**: I documenti possono essere assegnati alla persona giusta invece di affidarsi alle e-mail.
* **Niente viene dimenticato**: Le notifiche ricordano agli utenti i documenti che richiedono un loro intervento.
* **Lavoro aperto a colpo d'occhio**: Con Conteggio attività nel cruscotto, il cruscotto mostra quali documenti hanno ancora attività aperte.
* **Decisioni tracciabili**: Con le opzioni di eliminazione e completamento, le attività escono dalla coda solo tramite una decisione o un amministratore.

### Come usarla

1. Vai su **Impostazioni**.
2. Seleziona **Elaborazione dei documenti**.
3. Seleziona **Modulo**.
4. Apri la sezione **Tipo di documento**.
5. Attiva **Attività e notifiche**.
6. (Facoltativo) Attiva **Conteggio attività nel cruscotto** per mostrare l'icona delle attività nel cruscotto.
7. (Facoltativo) Attiva **Consenti il filtro "Tutti" per gli utenti non amministratori** se tutti gli utenti devono vedere tutte le attività.
8. (Facoltativo) Scegli in **Eliminazione attività da parte di non amministratori** quali attività possono eliminare gli utenti.
9. (Facoltativo) Scegli in **Completamento attività da parte di non amministratori** chi può chiudere le attività.

Le opzioni di eliminazione e completamento vengono salvate non appena scegli un valore.

### Quando usare questa funzione

* **Team che condividono il lavoro sui documenti**: Attivala quando più persone validano o approvano documenti e devono passarsi il lavoro a vicenda.
* **Visibilità del carico di lavoro**: Attiva anche Conteggio attività nel cruscotto quando il team deve vedere nel cruscotto quali documenti hanno ancora attività aperte.
* **Attività che solo un amministratore o una decisione devono chiudere**: Imposta **Completamento attività da parte di non amministratori** su **Solo per amministratori** o **Amministratori e utenti assegnati**, ed **Eliminazione attività da parte di non amministratori** su **Nessuna**, quando gli utenti non devono rimuovere attività che non sono state effettivamente svolte.
* **Configurazioni a utente singolo o completamente automatizzate**: Puoi lasciarla disattivata se nessuno deve assegnare documenti o monitorare attività.
