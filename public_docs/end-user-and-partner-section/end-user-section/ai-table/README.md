# AI Table

AI Table permette di verificare le righe estratte, correggere colonne e salvare istruzioni per il layout di un fornitore. Scegliere la guida adatta. Structured Output ha una guida dedicata con Predefinito/Sì/No, impostazioni specifiche, anteprima ed esempio completo.

* [Impostazioni e valori specifici](configuration.md)
* [Structured Output per le tabelle](structured-output.md)
* [Colonne e correzioni](columns-and-corrections.md)
* [Istruzioni AI](ai-instructions.md)
* [Tag della tabella AI](ai-table-tags.md)
* [Spiegare l'estrazione e diagnosticare](explain-extraction.md)
* [Assistente e permessi](assistant-and-permissions.md)

<figure><img src="../../../.gitbook/assets/anatomy-ai-table.svg" alt="Illustrazione isometrica di un lettore di tabelle: una testina di lettura con una cartuccia di istruzioni scansiona la tabella di un documento, un pannello di connessione collega ogni colonna restituita a una colonna configurata, e le colonne configurate sono contenitori con una manopola Use AI a tre posizioni ciascuna."><figcaption><p>L&#x27;AI legge la tabella e restituisce colonne. Ogni colonna restituita viene associata a una colonna di tabella configurata (una colonna restituita senza associazione resta nascosta), ogni colonna configurata ha la propria impostazione Use AI (Predefinito, Sì o No), e le istruzioni AI e <strong>Salva come addestramento</strong> influenzano il modo in cui vengono letti i documenti successivi con lo stesso layout del fornitore.</p></figcaption></figure>

## Quando ottieni la tabella AI

* Un amministratore ha attivato l'**Estrazione della tabella AI** (Impostazioni → Elaborazione del documento → Tipi di Documento → Classificazione ed estrazione, vedi [Impostazioni per gli amministratori](#impostazioni-per-gli-amministratori)). Se è disattivata, l'area della tabella mostra *La tabella AI verrà visualizzata qui. Abilitazione in …*.
* Verificare testo leggibile o ingresso Vision. Le regole classiche salvate possono ancora determinare il percorso effettivo; controllare [quale percorso è stato usato](../../../overview-and-basics/faq/document-processing/which-extraction-path-was-used.md).
* Ogni colonna ha una scelta Use AI a tre stati. Controllare anche origine effettiva e regole del fornitore; Structured Output non sostituisce ogni tabella basata su regole.

Quale livello AI legge la tabella (Fast, Full, Nexus) è impostato per organizzazione e può essere sovrascritto per fornitore, vedi Modello di IA Specifico per Fornitore.

## La tabella AI in sintesi

<figure><img src="../../../.gitbook/assets/ai-table-overview-it.png" alt="AI Tabella estratta con le intestazioni delle colonne e quattro righe"><figcaption><p>Le due schede, la AI Tabella estratta e le intestazioni delle sue colonne.</p></figcaption></figure>

* **Schede.** *AI Tabella estratta* è ciò che ha letto l'AI. *Tabella estratta* è la tabella classica ottenuta dalle regole addestrate. La scheda AI si apre per impostazione predefinita quando il documento ha una tabella AI.
* **Intestazione di colonna.** Ogni colonna mostra il proprio nome, un piccolo simbolo di **origine** (passaci sopra il mouse: *IA · mappatura*, *IA · sinonimo* e così via indicano come l'AI ha abbinato la colonna), un menu con i **tre puntini** e, per una colonna mappata, un **pulsante con il nome** su cui puoi fare clic per cambiare quale colonna è.
* **Pulsanti di riga.** La **x** all'inizio di una riga rimuove quella riga. Fai clic con il pulsante destro su una riga per *Select as additional cost* / *Remove as additional cost*.
* **Barra degli strumenti a piè di pagina.** Le icone in fondo alla schermata aggiungono o nascondono colonne e righe, vedi [Barra degli strumenti a piè di pagina](#barra-degli-strumenti-a-pie-di-pagina).
* **Scheda Istruzioni per l'IA** sotto la tabella: prompt, colonne aggiuntive, **Modifica del test**, **Applicare**, **Salva come addestramento**, **Cancellare**, **Esportazione**, vedi [Dai istruzioni all'AI](#dai-istruzioni-allai).

{% hint style="info" %}
I controlli delle colonne funzionano solo se puoi modificare il documento. Se sono disattivati, il documento è in sola lettura oppure è bloccato in un'altra sessione. Quando il banner rosso indica che il documento è bloccato dal tuo stesso utente in un'altra sessione, **Sbloccare** ne assume il blocco.
{% endhint %}


## Impostazioni per gli amministratori

Continua qui: [Impostazioni e valori specifici](configuration.md).

### Usa AI per colonna

Continua qui: [Structured Output per le tabelle](structured-output.md).

<a id="scegliere-la-colonna-giusta-rimappatura"></a>
<a id="il-menu-con-i-tre-puntini"></a>
<a id="barra-degli-strumenti-a-piè-di-pagina"></a>
<a id="barra-degli-strumenti-a-pie-di-pagina"></a>

## Modificare una colonna

Continua qui: [Colonne e correzioni](columns-and-corrections.md).

<a id="suggerisci-con-nexus"></a>
<a id="testare-applicare-salvare-cosa-fa-ogni-pulsante"></a>

## Dai istruzioni all'AI

Continua qui: [Istruzioni AI](ai-instructions.md).


## Vedere cosa ha fatto l'AI

Continua qui: [Spiegare l'estrazione e diagnosticare](explain-extraction.md).


## Esempi pratici

Continua qui: [Spiegare l'estrazione e diagnosticare](explain-extraction.md).

<a id="suggerire-una-regola-al-tuo-amministratore"></a>

## L'Assistente e la tabella AI

Continua qui: [Assistente e permessi](assistant-and-permissions.md).


## Chi può fare cosa

Continua qui: [Assistente e permessi](assistant-and-permissions.md).

## Pagine correlate

* [Tag della tabella AI](ai-table-tags.md)
* [Campi di addestramento Linee/Tabella di addestramento](../../../administration-and-setup/setup/document-training/training-line-fields-table-training/README.md)
* [Touchless Intelligence](../../../administration-and-setup/touchless-intelligence.md)
