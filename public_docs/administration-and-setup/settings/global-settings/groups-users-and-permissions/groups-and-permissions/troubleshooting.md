# Risoluzione dei Problemi relativi al Controllo degli Accessi e alle Autorizzazioni

Se gli utenti riscontrano restrizioni di accesso inaspettate, come documenti mancanti, impossibilità di modificare campi o azioni negate, utilizzare la seguente checklist per identificare e risolvere il problema in base alla configurazione delle autorizzazioni in DocBits.

### 1. Verifica se il Controllo degli Accessi è Abilitato

Le impostazioni di Controllo degli Accessi si applicano solo se la funzionalità è **abilitata**.

* Naviga su: `Impostazioni` > `Elaborazione Documenti` > `Modulo`.
* Assicurati che l'interruttore del **Controllo degli Accessi** sia attivato.
* Se disabilitato, tutti gli utenti hanno tipicamente accesso illimitato indipendentemente dalle autorizzazioni di gruppo o campo.

### 2. Controlla le Assegnazioni di Gruppo

Assicurati che l'utente sia correttamente assegnato ai gruppi appropriati:

* Naviga su: `Impostazioni` > `Impostazioni Globali` > `Gruppi, Utenti e Autorizzazioni`.
* Seleziona **Gruppi e Autorizzazioni**.
* Conferma che l'utente sia elencato nel gruppo previsto.
* Se il gruppo utilizza un controllo degli accessi specifico, l'assegnazione mancante del gruppo bloccherà l'accesso ai documenti e alle azioni.

### 3. Revisione delle Autorizzazioni di Accesso del Gruppo

L'accesso è concesso per tipo di documento e per azione:

* Nella schermata di **Controllo degli Accessi** per il gruppo, controlla il tipo di documento (ad esempio, Fattura, Ordine di Acquisto).
* Convalida autorizzazioni come:
  * **Elenco**, **Visualizza**, **Modifica**, **Elimina**, **Aggiornamento di Massa**
  * Livelli di **Approvazione** (1°, 2°), **Sblocca Documento**
* Assicurati che il livello di accesso non sia limitato a **Proprietario** o **Amministratore** a meno che appropriato.

### 4. Conferma le Autorizzazioni a Livello di Campo

L'accesso può essere anche limitato al **livello di campo**, il che potrebbe bloccare la modifica o la visibilità:

* Nella configurazione del Controllo degli Accessi del gruppo, naviga al tipo di documento e controlla le impostazioni a livello di campo.
* Conferma se i campi sono impostati su:
  * **Lettura/Scrittura**, **Sola Lettura**, **Scrittura Proprietario**, **Nessuno**
* Aggiusta se necessario in base al ruolo dell'utente.

### 5. Controlla l'Impostazione "Solo Documenti Assegnati"

Questa impostazione globale limita la visibilità dei documenti:

* Naviga su: `Impostazioni` > `Impostazioni Globali` > `Gruppi, Utenti e Autorizzazioni`.
* Se **Solo Documenti Assegnati** è **abilitato**, gli utenti possono vedere solo i documenti assegnati esplicitamente a loro o al loro gruppo.
* Se gli utenti non riescono a vedere i documenti attesi:
  * Controlla le assegnazioni dei documenti.
  * Disabilita temporaneamente l'impostazione per testare se è la causa principale.

### 6. Test con un Utente o Gruppo con Accesso Confermato

Per isolare il problema:

* Accedi con un utente di un gruppo che ha accesso confermato.
* Confronta la visibilità dei documenti e le azioni disponibili.
* Questo aiuta a determinare se il problema è specifico dell'utente, del gruppo o dell'intero sistema.

### 7. Ricontrolla le Assegnazioni dei Documenti

Se "Solo Documenti Assegnati" è **abilitato**, assicurati che:

* Il documento sia **assegnato** all'utente o a uno dei loro gruppi.
* Utilizza i controlli di assegnazione nella vista dettagli documento per effettuare o rivedere le assegnazioni.

### 8. Reimposta o Riconfigura le Autorizzazioni

Se le autorizzazioni sono state modificate di recente o gli utenti sono stati spostati tra i gruppi:

* Conferma che le impostazioni di Controllo degli Accessi riflettano le nuove configurazioni di gruppo.
* Regola le autorizzazioni dei campi e dei documenti se necessario.
* Se non sei sicuro, crea un gruppo di test con ampie autorizzazioni e testa il comportamento di accesso prima di applicare modifiche ai gruppi attivi.
