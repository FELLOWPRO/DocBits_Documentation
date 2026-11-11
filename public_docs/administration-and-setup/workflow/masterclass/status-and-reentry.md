---
description: >-
  Usare la scheda Cambiare lo stato in in modo che un cambio di stato non avvii
  di nuovo lo stesso Workflow.
---

# Cambiare lo stato senza riavviare il Workflow

Quando un documento riceve un nuovo stato, DocBits avvia i Workflow previsti per quello stato. Tra questi può esserci anche il Workflow che ha appena cambiato lo stato. Se le sue condizioni corrispondono ancora, viene eseguito di nuovo e crea una seconda attività o una seconda esportazione.

Questa pagina mostra come impostare il Workflow in modo che ogni documento lo attraversi una sola volta.

## L'impostazione decisiva

La scheda [Cambiare lo stato in](../then/status/change-status-to.md) imposta il nuovo stato. La sua impostazione **Attivare i flussi di lavoro** decide se questo cambio di stato può avviare Workflow:

* **Falso:** non viene avviato nessun Workflow. Usare questo valore, a meno che un altro Workflow debba proseguire con il documento.
* **Vero:** DocBits avvia i Workflow le cui condizioni corrispondono al documento nel suo nuovo stato. Tra questi può esserci anche il Workflow che ha eseguito il cambio.

La pagina della scheda descrive tutti gli stati e le versioni della scheda.

## Quali Workflow si avviano dopo un cambio di stato

Con **Attivare i flussi di lavoro** impostato su **Vero**, DocBits esamina ogni Workflow attivo e ne controlla le condizioni su tipo di documento e stato, per esempio una scheda **Document status**. Un Workflow si avvia se il documento, con il suo nuovo stato, corrisponde.

Un Workflow che non controlla lo stato corrisponde a **ogni** stato. Quindi, se cambia lui stesso lo stato, il nuovo stato lo avvia di nuovo.

Impostare un documento sullo stato che ha già non produce alcun effetto: lo stato resta invariato e non si avvia nessun Workflow.

## Esempio: una esecuzione o due

La regola: quando il Workflow ha svolto il suo compito, le sue condizioni non devono più corrispondere.

<figure><img src="../../../.gitbook/assets/status-change-runs-once-vs-twice-it.png" alt="Due Workflow, entrambi con Attivare i flussi di lavoro impostato su Vero. A sinistra la condizione controlla che il tipo sia Fattura e lo stato sia Pronto per la convalida. Dopo il cambio in In attesa di approvazione la condizione non corrisponde più, il Workflow non viene riavviato, risultato 1 attività. A destra la condizione controlla solo che il tipo sia Fattura. Il nuovo stato avvia il Workflow una seconda volta, che crea una seconda attività e imposta di nuovo In attesa di approvazione, senza alcun effetto. Risultato 2 attività." width="800"><figcaption><p>Lo stesso Workflow con e senza condizione sullo stato</p></figcaption></figure>

A destra il Workflow viene eseguito una seconda volta e crea un'attività duplicata. Si ferma lì solo perché il secondo cambio di stato imposta uno stato che il documento ha già.

**Due Workflow possono avviarsi a vicenda.** Se un Workflow imposta **In attesa di approvazione** e un altro riporta il documento a **Pronto per la convalida**, entrambi con **Vero**, continuano ad avviarsi a vicenda. Dare a ogni Workflow una condizione sullo stato da cui parte e usare **Vero** solo dove serve.

## Impostazione passo per passo

1. **Usare la versione 3 di Cambiare lo stato in.** Le versioni precedenti non hanno l'impostazione **Attivare i flussi di lavoro** (vedere [Versioni della scheda](../then/status/change-status-to.md#versioni-della-scheda)).
2. **Controllare lo stato di partenza.** Aggiungere la scheda **E** **Document status** (in **E → Stato**) e impostarla su **È** **Pronto per la convalida**. Vedere [Condizione di stato del singolo documento](../and/status/single-document-status-condition.md). Se lo stato da solo non indica se il passaggio è già stato svolto, controllare anche un campo che il Workflow compila al termine.
3. **Aggiungere l'azione**, per esempio la creazione di un'attività o l'esportazione del documento.
4. **Aggiungere Cambiare lo stato in** e scegliere lo stato successivo, per esempio **In attesa di approvazione**.
5. **Scegliere Attivare i flussi di lavoro.** Iniziare con **Falso**. Scegliere **Vero** solo se un altro Workflow deve proseguire con il nuovo stato.
6. **Provare con un documento reale.** Verificare che sia stata creata esattamente un'attività o un'esportazione e che il documento abbia il nuovo stato.

{% hint style="info" %}
I test nel designer dei Workflow simulano soltanto il cambio di stato. Lo stato non viene salvato e nessun altro Workflow si avvia. Per vedere il comportamento reale, usare un documento reale.
{% endhint %}

## Protezione integrata

DocBits limita i danni quando dei Workflow si avviano a vicenda in continuazione:

* **Una sola esecuzione di Workflow alla volta per documento.** Le esecuzioni per lo stesso documento si attendono a vicenda e ognuna vede il documento come l'ha lasciato la precedente.
* **Limite di esecuzioni.** Per impostazione predefinita, lo stesso Workflow viene eseguito al massimo 50 volte su un documento. Dopo, DocBits smette di avviarlo per quel documento.

Questi limiti fermano la ripetizione prima o poi, ma a quel punto possono già esistere molte attività o esportazioni. Ciò che la evita è una condizione sullo stato. Se un duplicato sarebbe un vero problema, controllarlo anche prima di agire, per esempio verificando se per il documento esiste già un'attività aperta.

## Argomenti correlati

* [Cambiare lo stato in](../then/status/change-status-to.md): la scheda, i suoi stati e le sue versioni
* [Condizione di stato del singolo documento](../and/status/single-document-status-condition.md): controllare lo stato del documento in una condizione
* [Quando viene eseguito il mio workflow?](../workflow-execution-model.md)
* [Panoramica del percorso di apprendimento](../workflow-learning-path.md)
