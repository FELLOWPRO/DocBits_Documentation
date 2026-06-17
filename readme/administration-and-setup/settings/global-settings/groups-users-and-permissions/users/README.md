# Utenti

<figure><img src="../../../../../.gitbook/assets/users_settings.png" alt="Gestione utenti"><figcaption><p>Pagina di gestione utenti</p></figcaption></figure>

La pagina Utenti consente agli amministratori di gestire tutti gli account utente della tua organizzazione DocBits. Qui puoi aggiungere nuovi utenti, assegnare ruoli e controllare gli accessi.

## Elenco degli utenti

La tabella degli utenti mostra le seguenti colonne:

| Colonna | Descrizione |
|--------|-------------|
| **Nome** | Il nome completo dell'utente. |
| **E-Mail** | L'indirizzo email dell'utente, usato come identificativo di accesso. |
| **Ultimo accesso** | Data e ora dell'accesso più recente dell'utente. |
| **Admin** | Casella di selezione che indica se l'utente dispone di privilegi di amministratore. Gli Admin possono accedere a tutte le impostazioni e gestire gli altri utenti. |
| **System Admin** | Casella di selezione che indica l'unico System Admin dell'organizzazione, ovvero l'account che DocBits utilizza per le azioni automatiche eseguite dietro le quinte (come importazioni ed esportazioni automatiche). Un System Admin dispone sempre anche dei privilegi di Admin. Consulta [Privilegi di amministratore](admin-privileges.md#admin-vs-system-admin) per la differenza tra Admin e System Admin. |
| **Attivo** | Casella di selezione che indica se l'account utente è attualmente attivo. Gli utenti inattivi non possono accedere. |
| **Azioni** | Menu con opzioni come la modifica dei dati dell'utente, il ripristino delle password o la disattivazione dell'account. |

Usa la barra di **Ricerca** in alto per trovare rapidamente gli utenti per nome o ID.

## Analisi degli accessi

Fai clic su **Analisi degli accessi** per visualizzare i dati sull'attività di accesso nell'intera organizzazione, inclusi la frequenza e gli schemi di accesso.

## Aggiungere un nuovo utente

1. Fai clic sul pulsante **Aggiungi utente** nell'angolo in alto a destra.
2. Compila le informazioni richieste:
   * **Nome utente**: un nome univoco per l'utente.
   * **Nome** e **Cognome**: il nome completo dell'utente.
   * **Indirizzo email**: usato per l'accesso e le notifiche.
   * **Password**: deve rispettare le politiche di sicurezza della tua organizzazione.
   * **Ruolo utente**: assegna il ruolo appropriato (Standard User, Admin o System Admin).
3. Fai clic su **Salva** per creare l'account utente. Il nuovo utente riceverà una notifica via email con i propri dati di accesso.

> **Nota:** il ruolo **System Admin** può essere scelto solo durante la creazione di un utente: non può essere aggiunto o rimosso in un secondo momento. Ogni organizzazione può avere un solo System Admin e selezionarlo concede automaticamente anche i diritti di Admin. Consulta [Privilegi di amministratore](admin-privileges.md#admin-vs-system-admin) per sapere quando utilizzarlo.
