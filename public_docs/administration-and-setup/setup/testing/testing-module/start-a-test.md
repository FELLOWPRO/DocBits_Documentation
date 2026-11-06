# Avviare un test

Un test è un modello più un input. Il modulo Testing lo esegue e lo gestisce; si sceglie come avviarlo. Tutti e tre i
modi sono equivalenti e ogni esecuzione confluisce nei [Log](logs.md).

| Modo | Quando utilizzarlo | Mostrato nei log come |
|---|---|---|
| **Nel browser** | Si desidera eseguire subito una verifica e seguirla. | **Pagina** |
| **Assistente AI (MCP)** | Si lavora con un assistente AI collegato a DocBits e si desidera che esegua e valuti le verifiche. | **Agente MCP** |
| **Dall'esterno (Playwright o REST)** | L'automazione dei test o la pipeline CI avvia le verifiche, ad esempio dopo un deployment. | **Playwright** |

In ogni caso i clic avvengono in una **scheda del browser DocBits di un amministratore dell'organizzazione**, con i permessi di
quella persona. La scheda deve restare aperta; ricaricarla o chiuderla termina l'esecuzione. L'unica eccezione è un passaggio **Ricarica pagina**
del test stesso (vedere [Ricaricare e riprendere](reload-and-resume.md)).

## Avviare nel browser

1. Aprire **Impostazioni → Testing**, scheda **Input**.
2. Selezionare **Avvia** sull'input (oppure aprire l'input e selezionare **Avvia**).
3. Se il modello modifica dati, DocBits chiede: *Questo modello scrive dati. Conferma per iniziare.* Selezionare **Avvia** per continuare.
4. Il test viene eseguito in questa scheda. Nella pagina Testing il pannello **Esecuzione in diretta** mostra lo stato, l'**Azione in corso**,
   l'avanzamento dei passaggi e **Pausa**, **Riprendi** e **Ferma**. Quando il test apre un'altra pagina, un piccolo indicatore
   nell'angolo in basso a destra ne mostra l'avanzamento. Quando il test termina, l'indicatore mostra il risultato
   con **Apri log** e **Chiudi**.
5. Al termine del test, aprire la scheda **Log** per leggere il risultato.

<figure><img src="../../../../.gitbook/assets/testing-12-confirm-writes-it.png" alt="Conferma prima di un test che scrive dati"><figcaption><p>Conferma prima di un test che scrive dati.</p></figcaption></figure>

<figure><img src="../../../../.gitbook/assets/testing-13-live-run-it.png" alt="Pannello Esecuzione in diretta dopo il superamento del test"><figcaption><p>Pannello Esecuzione in diretta dopo il superamento del test.</p></figcaption></figure>

<figure><img src="../../../../.gitbook/assets/testing-14-run-indicator-it.png" alt="Indicatore di esecuzione nell'angolo in basso a destra in un'altra pagina"><figcaption><p>Indicatore di esecuzione nell'angolo in basso a destra in un'altra pagina.</p></figcaption></figure>

{% hint style="info" %}
**Caricamenti durante un test:** se la propria organizzazione ha sotto-organizzazioni e la dashboard le mostra tutte, la finestra
di caricamento chiede normalmente a quale sotto-organizzazione appartiene il documento. Mentre un test è in esecuzione, il caricamento viene indirizzato alla
**prima sotto-organizzazione proposta dalla finestra**, senza chiedere. Per caricare in una sotto-organizzazione specifica, avviare il
test dalla vista di quella sotto-organizzazione.
{% endhint %}

## Consentire gli avvii dall'esterno

Un assistente AI o uno script Playwright non può fare clic da solo; chiede a DocBits di eseguire un test **in una scheda del browser che
è stata registrata**:

1. Aprire **Impostazioni → Testing**, scheda **Input**, nella scheda del browser che deve eseguire i test.
2. Attivare **Consenti avvii dall'esterno**. La scheda ora accetta gli avvii e mostra il proprio ID di sessione.
3. Lasciare la scheda aperta. La registrazione termina quando la scheda viene ricaricata o chiusa.

<figure><img src="../../../../.gitbook/assets/testing-15-remote-start-it.png" alt="Consenti avvii dall'esterno attivato, con l'ID di sessione"><figcaption><p>Consenti avvii dall'esterno attivato, con l'ID di sessione.</p></figcaption></figure>

L'editor degli input ricorda i tre modi sotto **Avvia dall'esterno:** **Questa pagina**, **agente MCP**,
**Playwright o REST**.

<figure><img src="../../../../.gitbook/assets/testing-16-start-from-outside-it.png" alt="Riga Avvia dall'esterno nell'editor degli input"><figcaption><p>Riga Avvia dall'esterno nell'editor degli input.</p></figcaption></figure>

## Condividere un link di avvio

Un link di avvio apre la finestra di avvio di un modello, già compilata, così un collega o una pipeline CI non deve
scegliere nuovamente il modello e i relativi valori:

`https://<your-environment>/settings/testing?run=<template>&version=<version>&input=<input>&autostart=1`

| Elemento | Funzione |
|---|---|---|
| **run** | Il modello da aprire, identificato dalla sua chiave (la riga sotto il nome del modello nella finestra, ad esempio `default-smoke-analytics`). Obbligatorio. |
| **version** | Apre questa versione salvata. Se omesso, viene aperta la versione più recente. |
| **input** | Precompila i campi con un input salvato, indicato tramite nome o ID. I parametri contrassegnati come sensibili non vengono mai compilati. |
| **autostart=1** | Avvia il test non appena la pagina è aperta, ma solo se il modello è di sola lettura. Un modello che scrive dati attende comunque la conferma. |

Per ottenere il link, aprire la finestra di avvio di un modello e passare ad **Avvia dall'esterno**. Il blocco
**Link di avvio** contiene il link di quel modello, mentre **Playwright con link di avvio** contiene uno snippet che
apre il link e attende il risultato.

<figure><img src="../../../../.gitbook/assets/testing-start-link-dialog-it.png" alt="Finestra di avvio nella vista Avvia dall'esterno con il link di avvio copiabile e un esempio Playwright"><figcaption><p>La finestra di avvio nella vista <strong>Avvia dall'esterno</strong>: il link di avvio copiabile e un esempio Playwright che lo apre. Una sessione compare sotto <strong>Sessione che esegue il test</strong> quando una scheda accetta avvii dall'esterno.</p></figcaption></figure>

Per chi apre il link:

* DocBits apre **Impostazioni → Testing**, scheda **Modelli**, con la finestra di avvio del modello. Il link funziona
  solo per chi può aprire Impostazioni → Testing, perché l'esecuzione utilizza la scheda del browser e i permessi di quella persona.
* Un modello, una versione o un input non riconosciuto genera un errore sotto le schede e non avvia nulla.
* Con `autostart=1`, un modello di sola lettura si avvia immediatamente. In tutti gli altri casi il test attende che si
  selezioni **Avvia**; un modello che scrive dati richiede comunque la conferma.
* Dopo la lettura, i parametri vengono rimossi dalla barra degli indirizzi: ricaricando la pagina, il test non viene
  avviato una seconda volta.

Il **?** accanto alle schede e nella finestra di avvio apre la pagina corrispondente di questa documentazione nella
lingua dell'interfaccia.

## Avviare da un assistente AI (MCP)

Se il proprio assistente AI è collegato a DocBits (vedere [DocBits MCP](../../../../advanced-functions-and-tools/docbits-mcp/README.md)
e [Configurare DocBits con Claude o Codex](../../../../advanced-functions-and-tools/docbits-mcp/configuration-with-claude-or-codex.md)):

1. Consentire gli avvii dall'esterno in una scheda del browser (vedere sopra).
2. Rivolgersi all'assistente, ad esempio: *"Elenca i miei input di test DocBits e avvia 'Fattura LT-2026-0001 pronta per la validazione'
   nella mia scheda del browser registrata. Poi dimmi il risultato."*
3. L'assistente chiede quale scheda utilizzare se ne è registrata più di una e chiede conferma prima di avviare un test che
   modifica dati. Poi legge il log e riporta il risultato.

## Avviare da Playwright o da un altro strumento (REST)

L'automazione dei test avvia un input con una sola chiamata API e poi ne legge il log. Occorrono:

* un token di un amministratore dell'organizzazione (vedere [Chiave API](../../../settings/global-settings/integration/api-key.md));
* l'ID dell'input;
* l'ID di sessione di una scheda del browser con **Consenti avvii dall'esterno** attivato.

La chiamata e un esempio si trovano in [Per sviluppatori](for-developers.md).

## Ambienti cliente

In sandbox e in produzione il badge **Ambiente** è rosso. I test che modificano dati richiedono una conferma esplicita a ogni
avvio e i passaggi di esportazione, eliminazione o approvazione vengono bloccati, a meno che il modello non dichiari di scrivere dati. Se possibile, eseguire
i test che scrivono in un ambiente di test.
