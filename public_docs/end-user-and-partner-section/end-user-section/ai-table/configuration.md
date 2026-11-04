# Impostazioni e valori specifici

[AI Table](README.md) · [Structured Output per le tabelle](structured-output.md)

## Impostazioni per gli amministratori

Apri **Impostazioni → Elaborazione del documento → Tipi di Documento → Classificazione ed estrazione**, scheda **Generale**, sezione **Estrazione**.

<figure><img src="../../../.gitbook/assets/structured-output-settings-it-20261104.png" alt="Controlli attuali di estrazione. Structured Output è disattivato in questa configurazione esistente, quindi l&#x27;anteprima dello schema non appare. Nessuna impostazione di estrazione è stata modificata."><figcaption><p>Controlli attuali di estrazione. Structured Output è disattivato in questa configurazione esistente, quindi l&#x27;anteprima dello schema non appare. Nessuna impostazione di estrazione è stata modificata.</p></figcaption></figure>

* **Estrazione della tabella** attiva la tabella classica.
* **Estrazione della tabella AI** attiva o disattiva la tabella AI per l'organizzazione.
* **Utilizzare l'estrazione strutturata (IA)**: L'interruttore imposta il valore organizzativo dell'output strutturato. Le colonne richieste dipendono da Predefinito/Sì/No in Use AI, dalle impostazioni del modello di estrazione e dall'addestramento del fornitore. La guida completa spiega configurazione, anteprima ed esempio. [Structured Output per le tabelle](structured-output.md).
* **Salva le regole di estrazione (solo amministratore)**: se attivo, solo gli amministratori dell'organizzazione possono salvare ed esportare le regole di estrazione.

<figure><img src="../../../.gitbook/assets/ai-table-settings-extraction-admin-only-it.png" alt="Interruttore Salva le regole di estrazione (solo amministratore)"><figcaption><p><strong>Salva le regole di estrazione (solo amministratore)</strong> controlla chi può usare <strong>Salva come addestramento</strong>.</p></figcaption></figure>

### Usa AI per colonna

Scelta a tre stati: Predefinito eredita la selezione AI del tipo di documento, Sì richiede esplicitamente la colonna e No la esclude dallo schema base. È separata da Obbligatoria, Sola lettura e Nascosta. [Structured Output per le tabelle](structured-output.md).


Structured Output ha una propria impostazione organizzazione/modello di estrazione, separata dal livello AI. Modificarla in Altre opzioni del documento; la conferma salva il valore specifico e riavvia quel documento. Gli indicatori nell'elenco sono di sola lettura. Eliminare una voce può rimuovere più impostazioni specifiche insieme. [Structured Output per le tabelle](structured-output.md).
