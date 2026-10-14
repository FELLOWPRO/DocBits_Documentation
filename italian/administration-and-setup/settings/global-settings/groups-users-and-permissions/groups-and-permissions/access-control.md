# Controllo Accessi

## Panoramica

Il Controllo Accessi definisce, per un singolo **gruppo** (ruolo), esattamente cosa possono fare i suoi membri — sia a **livello di tipo di documento** (quali tipi di documento vedono e quali azioni possono eseguire) sia a **livello di campo** (quali singoli campi possono leggere o modificare).

Le autorizzazioni vengono sempre valutate **per gruppo**. Un utente eredita le autorizzazioni di ogni gruppo a cui appartiene.

{% hint style="info" %}
Il Controllo Accessi viene applicato solo quando il sistema **Gruppi e Autorizzazioni** è attivato (vedi [Attivare le Autorizzazioni](activating-permissions.md)). **Gli amministratori ignorano sempre il Controllo Accessi** e possono vedere e fare tutto, indipendentemente dalle impostazioni di questa pagina.
{% endhint %}

Ogni gruppo può essere configurato per:

* **Accesso al documento** — se il gruppo può utilizzare un tipo di documento.
* **Autorizzazioni di azione** — quali azioni (elencare, visualizzare, modificare, eliminare, aggiornamento di massa, approvare) il gruppo può eseguire e *per quali documenti*.
* **Autorizzazioni di campo** — se ogni singolo campo di un tipo di documento è modificabile, di sola lettura o nascosto.

## Attivazione

1. Vai su **Impostazioni**.
2. Seleziona **Elaborazione Documenti**.
3. Seleziona **Modulo.**
4. Attiva il **Controllo Accessi** abilitando il cursore.

<figure><img src="../../../../../.gitbook/assets/Access-Control3_it.png" alt=""><figcaption></figcaption></figure>

## Aprire il Controllo Accessi di un gruppo

1. Vai su **Impostazioni**.
2. Vai su **Impostazioni Globali**.
3. Seleziona **Gruppi, Utenti e Autorizzazioni**.
4. Seleziona **Gruppi e Autorizzazioni**.
5. Per gestire le autorizzazioni di un gruppo (ad esempio PROCUREMENT\_DIRECTOR), fai clic sui tre puntini a destra.
6. Seleziona **Gestisci Controllo Accessi**.

<figure><img src="../../../../../.gitbook/assets/access_control_open_menu.png" alt="Aprire il menu di riga di un gruppo e scegliere Gestisci Controllo Accessi"><figcaption><p>Nella pagina «Gruppi e Autorizzazioni», apri il menu <strong>⋮</strong> di un gruppo e scegli <strong>Gestisci Controllo Accessi</strong>.</p></figcaption></figure>

## Come viene valutata un'autorizzazione

Quando un utente tenta di fare qualcosa con un documento, DocBits verifica, nell'ordine:

1. **Il sistema Gruppi e Autorizzazioni è attivo e l'utente non è amministratore?** Se è disattivato, o l'utente è amministratore → accesso completo.
2. **Il tipo di documento è abilitato per uno dei gruppi dell'utente?** Se è disabilitato → l'utente non può vedere né utilizzare quel tipo di documento.
3. **Quale ambito di accesso è impostato per l'azione?** (ad esempio *Modifica = Owner*). L'ambito viene confrontato con la relazione dell'utente con *questo specifico documento* — è il proprietario, l'assegnatario, entrambi o nessuno?
4. **Quale autorizzazione di campo si applica?** Anche quando un utente può aprire un documento, i singoli campi possono rimanere nascosti o bloccati.

## Autorizzazioni a livello di tipo di documento

Ogni riga della matrice è un tipo di documento (Invoice, Credit Note, Purchase Order, …).

La prima colonna è un interruttore **Abilitato / Disabilitato**. Disabilitalo e il gruppo non potrà utilizzare affatto quel tipo di documento — scompare dalla loro dashboard. Abilitalo e le sette colonne di azione diventano modificabili.

| Azione | Determina se il gruppo può… |
|--------|------------------------------|
| **Elenco** | vedere il tipo di documento nell'elenco della dashboard. |
| **Visualizza** | aprire un documento e vederne i dettagli. |
| **Modifica** | modificare i valori dei campi di un documento. |
| **Elimina** | eliminare un documento. |
| **Aggiornamento di massa** | applicare un aggiornamento di massa a più documenti contemporaneamente. |
| **Prima Approvazione** | concedere l'approvazione di primo livello. |
| **Seconda Approvazione** | concedere l'approvazione di secondo livello. |

### Ambiti di accesso

Ogni colonna di azione è un menu a discesa. Il valore scelto risponde alla domanda *«per quali documenti il gruppo può farlo?»*. I nomi degli ambiti appaiono in inglese nell'interfaccia:

| Ambito | Chi è autorizzato | Effetto su un documento |
|--------|-------------------|--------------------------|
| **No Access** | Nessuno nel gruppo. | L'azione è bloccata per tutti nel gruppo — il pulsante è nascosto o disabilitato. |
| **Everyone** | Ogni membro del gruppo. | Qualsiasi membro del gruppo può eseguire l'azione su **qualsiasi** documento di questo tipo. |
| **Owner** | Solo l'utente che ha **creato / caricato** il documento. | L'azione funziona solo sui documenti caricati dall'utente stesso. |
| **Assignee** | Solo l'utente (o il gruppo) a cui il documento è **assegnato**. | L'azione funziona solo sui documenti assegnati all'utente o a un gruppo a cui appartiene. |
| **Owner & Assignee** | Il proprietario **o** l'assegnatario. | L'azione funziona se l'utente è *o* chi ha caricato *o* l'assegnatario. |

{% hint style="info" %}
**Owner** e **Assignee** dipendono dalla *relazione tra l'utente e ogni singolo documento*, quindi due membri dello stesso gruppo possono avere diritti diversi sulla stessa fattura — vedi l'esempio pratico qui sotto.
{% endhint %}

<figure><img src="../../../../../.gitbook/assets/access_control_matrix.png" alt="Matrice del Controllo Accessi di un gruppo"><figcaption><p>La matrice delle autorizzazioni per tipo di documento. Qui il tipo <strong>Invoice</strong> è abilitato e le sue azioni hanno ambiti di accesso diversi; gli altri tipi sono disabilitati.</p></figcaption></figure>

<figure><img src="../../../../../.gitbook/assets/access_control_scope_dropdown.png" alt="Menu a discesa degli ambiti di accesso"><figcaption><p>Ogni colonna di azione offre gli stessi cinque ambiti di accesso.</p></figcaption></figure>

### L'approvazione richiede anche Modifica

Approvare un documento attiva **due azioni** dietro le quinte: DocBits prima **salva** il documento e poi lo porta allo stato approvato. Il passaggio di salvataggio richiede l'autorizzazione **Modifica**, quindi le due autorizzazioni sono collegate.

Un utente a cui viene concessa solo la **Prima Approvazione** o la **Seconda Approvazione** — ma *non* **Modifica** — incontra un errore di autorizzazione nel passaggio di salvataggio e non può approvare il documento.

{% hint style="warning" %}
Ogni volta che concedi la **Prima Approvazione** o la **Seconda Approvazione**, concedi anche **Modifica** (e **Visualizza**) per lo stesso tipo di documento. Un'autorizzazione di approvazione da sola non è sufficiente.
{% endhint %}

## Autorizzazioni a livello di campo

Fai clic su una riga di tipo di documento per aprire il pannello **Autorizzazioni Campo** sottostante. I campi sono organizzati in schede (ad esempio *Colonne tabella*, *Dettagli della fattura*, *Dettagli di pagamento*, *Imposte e importi*). Ogni campo ha il proprio livello di accesso:

| Livello | Effetto sul campo |
|---------|-------------------|
| **Lettura/Scrittura** | Il campo è visibile **e** modificabile. |
| **Sola lettura** | Il campo è visibile ma **non può essere modificato** (in grigio). |
| **Approvazione** | Il campo può essere modificato, ma la modifica deve passare per un **flusso di approvazione** prima di essere applicata. |
| **Nessun accesso** | Il campo è **completamente nascosto** — l'utente non lo vede mai. |

{% hint style="info" %}
Le regole di campo si applicano allo stesso modo a **tutti** i membri del gruppo — non dipendono dal proprietario/assegnatario. Usale per nascondere o bloccare campi sensibili (ad esempio uno sconto o un importo totale) per un intero gruppo.
{% endhint %}

<figure><img src="../../../../../.gitbook/assets/access_control_field_permissions.png" alt="Pannello Autorizzazioni Campo"><figcaption><p>Il pannello «Autorizzazioni Campo» per il tipo Invoice. <code>CUSTOMER_DISCOUNT</code> è nascosto (Nessun accesso) mentre gli altri campi restano in Lettura/Scrittura.</p></figcaption></figure>

## Esempio pratico: cosa fa il Controllo Accessi su una fattura reale

Supponiamo di creare un gruppo **AP_CLERK** per i tuoi contabili fornitori e di configurare il tipo di documento **Invoice** così:

**Autorizzazioni di tipo di documento per Invoice**

| Azione | Ambito |
|--------|--------|
| Abilitato | ✅ Sì |
| Elenco | Everyone |
| Visualizza | Everyone |
| Modifica | Owner & Assignee |
| Elimina | No Access |
| Aggiornamento di massa | No Access |
| Prima Approvazione | Assignee |
| Seconda Approvazione | No Access |

**Autorizzazioni di campo per Invoice**

| Campo | Livello |
|-------|---------|
| `TOTAL_AMOUNT` | Sola lettura |
| `CUSTOMER_DISCOUNT` | Nessun accesso |
| *(tutti gli altri campi)* | Lettura/Scrittura |

Ora segui un documento concreto — la fattura **INV-4711**, che **Maria ha caricato** e che è **assegnata a Maria**. Sia Maria sia il suo collega Tom sono nel gruppo **AP_CLERK**.

**Maria (proprietaria *e* assegnataria di INV-4711):**

* ✅ Vede INV-4711 nell'elenco della dashboard *(Elenco = Everyone)*.
* ✅ Lo apre *(Visualizza = Everyone)*.
* ✅ Modifica il nome del fornitore e le righe *(Modifica = Owner & Assignee — è la proprietaria)*.
* 🔒 Vede `TOTAL_AMOUNT`, ma il campo è in grigio e non può modificarlo *(Sola lettura)*.
* 🚫 Non vede mai il campo `CUSTOMER_DISCOUNT` *(Nessun accesso)*.
* 🚫 Il pulsante **Elimina** è nascosto *(Elimina = No Access — nessuno nel gruppo può eliminare)*.
* ✅ Può concedere la **prima approvazione** *(Prima Approvazione = Assignee — è l'assegnataria)*.

**Tom (stesso gruppo, ma *non* ha caricato INV-4711 e *non* gli è assegnata):**

* ✅ Lo vede nell'elenco e ✅ lo apre *(Elenco e Visualizza = Everyone)*.
* 🚫 Non può modificare nulla — il documento si apre in **sola lettura** *(Modifica = Owner & Assignee — Tom non è nessuno dei due)*.
* 🔒 / 🚫 Vede esattamente la stessa visibilità dei campi di Maria: `TOTAL_AMOUNT` bloccato, `CUSTOMER_DISCOUNT` nascosto *(le regole di campo valgono per l'intero gruppo)*.
* 🚫 Non può concedere la prima approvazione *(Prima Approvazione = Assignee — non Tom)*.
* 🚫 Non può eliminare *(No Access)*.

**Cosa mostra questo esempio**

* **Everyone** apre un documento a tutti i membri del gruppo; **Owner / Assignee** restringe un'azione alle persone collegate a quel documento specifico.
* **No Access** rimuove un'azione (Elimina) o nasconde un campo (`CUSTOMER_DISCOUNT`) per l'intero gruppo.
* **Sola lettura** mantiene un campo visibile come riferimento (`TOTAL_AMOUNT`) ma impedisce le modifiche.
* Due persone nello **stesso gruppo** possono avere **diritti diversi sulla stessa fattura**, solo in base a chi l'ha caricata e a chi è assegnata.
